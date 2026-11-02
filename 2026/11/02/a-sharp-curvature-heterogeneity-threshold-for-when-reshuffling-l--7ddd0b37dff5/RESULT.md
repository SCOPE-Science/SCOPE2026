# A sharp curvature-heterogeneity threshold for when reshuffling loses to independent SGD

## Finding
Let the two component losses be strictly convex scalar quadratics with cancelling linear terms. Compare stationary squared error at **epoch endpoints** after two gradient calls, using either a newly and uniformly reshuffled order per epoch or independent uniform sampling with replacement at every call. Even when every component-gradient map is a strict contraction, reshuffling can have **larger** stationary error. There is a unique sharp boundary in curvature heterogeneity:
\[
\rho_* = \frac{1-v_*}{1+v_*}=0.280918564899747229\ldots,
\]
where \(v_* = \sqrt{w_*}\) and \(w_*\) is the unique root in \((0.315146,0.315147)\) of
\[
H(w)=224w^7+896w^6+96w^5-3405w^4+1956w^3+350w^2-148w-17.
\]
**There exists an individually contractive step size for which random reshuffling is strictly worse than independent sampling if and only if**
\[
\frac{\min(a,b)}{\max(a,b)}>\rho_*.
\]
At equality, reshuffling is never worse but ties the independent method at precisely one interior step size; below the curvature ratio threshold, reshuffling is strictly better at every individually contractive step. The classification includes an exact two-interval reversal window for intermediate heterogeneity, not merely the existence of a bad example.

## Assumptions and scope
Fix arbitrary \(a,b>0\) and \(d\in\mathbb R\setminus\{0\}\), and set
\[
f_1(x)=\frac a2x^2+dx,\qquad f_2(x)=\frac b2x^2-dx,
\qquad F(x)=\frac{f_1(x)+f_2(x)}2.
\]
The unique minimizer of \(F\) is \(0\). At each gradient evaluation use the same positive step \(\eta\), with \(0<\eta<2/\max(a,b)\). The independent method chooses each component with probability \(1/2\), independently at every step. The reshuffled method independently chooses order \((1,2)\) or \((2,1)\), each with probability \(1/2\), at the beginning of every epoch. All initial points are deterministic and finite; stationary quantities are the limits at even-numbered gradient calls. Computation uses exact real arithmetic.

Write
\[
u=\frac{a+b}{2},\quad h=\eta u,\quad v=\frac{|a-b|}{a+b},\quad
r_1=1-\eta a,\quad r_2=1-\eta b,\quad q=r_1r_2.
\]
Thus \(0\le v<1\), \(0<h<h_{\max}(v)=2/(1+v)\), and \(|r_1|,|r_2|<1\). Without loss, relabel the components so \(a=u(1-v)\), \(b=u(1+v)\).

The exact limiting mean-squared errors are
\[
S_{\rm iid}=\frac{\eta^2d^2}{1-(r_1^2+r_2^2)/2},\qquad
S_{\rm rr}=\frac{\eta^2d^2(r_1-r_2)^2}{4(1-q)^2}
+\frac{\eta^2d^2(2-r_1-r_2)^2}{4(1-q^2)}.
\]
For \(w=v^2\), define the quartic
\[
P(h,w)=w(w-1)^2h^4+(3w^2-4w+1)h^3
+(-2w^2+5w-5)h^2+(8-2w)h-4.
\]
The sign of the performance difference is exactly the sign of \(P\):
\[
\frac{S_{\rm rr}}{S_{\rm iid}}-1
=\frac{2P(h,v^2)}{[2-h(1-v^2)]^2(1+q)}.
\]

The complete admissible step-size phase diagram is:

1. For \(0\le v<1/2\), \(P\) has exactly one zero in the open stable interval. Reshuffling is strictly better before that zero and strictly worse afterward.
2. For \(v=1/2\), the same ranking holds; a second zero is at the **excluded** stability endpoint.
3. For \(1/2<v<v_*\), \(P\) has exactly two zeros in the stable interval. Reshuffling is strictly worse only between them, and strictly better outside their closed interval.
4. For \(v=v_*\), \(P\) has one double zero \(h_*=1.168357641771163576\ldots\) in the stable interval: the methods tie there and reshuffling is strictly better elsewhere.
5. For \(v_*<v<1\), reshuffling is strictly better throughout the stable interval.

An explicit heterogeneous example is \(a=1\), \(b=3\), \(\eta=3/5\), for which both gradient maps are strict contractions and
\[
\frac{S_{\rm rr}}{S_{\rm iid}}=\frac{2235}{2057}>1.
\]

## Proof
A component update maps the error to \(r_i x-\eta\varepsilon_i d\), where \(\varepsilon_1=1\) and \(\varepsilon_2=-1\). The independent sequence has limiting mean zero, since the mean multiplier \((r_1+r_2)/2\) is strictly contractive. Its second-moment recursion has limiting multiplier \((r_1^2+r_2^2)/2<1\); the mixed term vanishes with the mean, yielding the stated \(S_{\rm iid}\).

A two-call reshuffled epoch has the common multiplier \(q\) and affine increments \(\eta d(1-r_2)\) and \(\eta d(r_1-1)\). The increments are independent across epochs, have mean \(\eta d(r_1-r_2)/2\), and variance \(\eta^2d^2(2-r_1-r_2)^2/4\). Since \(|q|<1\), the stationary epoch mean and centered variance are respectively \(\eta d(r_1-r_2)/[2(1-q)]\) and \(\eta^2d^2(2-r_1-r_2)^2/[4(1-q^2)]\). Their sum gives \(S_{\rm rr}\). Exact rational algebra now yields the displayed \(P\) identity. Its denominator is strictly positive because \(0<h<h_{\max}\) and \(|q|<1\).

It remains to classify positive roots of \(P(h,v^2)\) in the **moving open interval** \(0<h<2/(1+v)\). The boundary identities are
\[
P(0,v^2)=-4,\qquad
P\!\left(\frac2{1+v},v^2\right)
=\frac{4v^2(v-1)(2v-1)}{(v+1)^2}.
\]
The only possible interior multiple-root parameters are detected by the exact resultant
\[
\operatorname{Res}_h(P,\partial_h P)
=-4w^3(w-1)^4H(w).
\]
An exact Sturm sequence gives exactly two zeros of \(H\) in \((0,1)\): one each in the disjoint rational intervals \((0.315146,0.315147)\) and \((0.819561,0.819562)\). At such a root, the linear subresultant is a nonzero factor times \(A(w)h+B(w)\), where
\[
A(w)=32w^7+20w^6-158w^5-395w^4+476w^3+62w^2+10w+1,
\]
\[
B(w)=16w^6+84w^5+369w^4-461w^3-59w^2-19w-2.
\]
Direct rational interval bounds show that the common root \(-B/A\) lies in \((1.16,1.18)\) for the first parameter and in \((1.19,1.22)\) for the second. The first lies inside its stable interval (whose endpoint exceeds \(2/1.57\)), whereas the second lies outside (whose endpoint is less than \(2/1.9\)). Thus there is exactly **one interior** tangency event.

By Sturm's theorem applied to \(P\), the numbers of distinct roots in the open stable intervals at the rational sample values \(v=1/4,1/2,11/20,2/3,19/20\) are respectively \(1,1,2,0,0\). These counts cannot change between the isolated discriminant events or boundary crossings; the only interior boundary crossing as \(v\) varies through \((0,1)\) occurs at \(v=1/2\). The signs follow from \(P(0,v^2)<0\), the boundary formula, and multiplicities; at the first discriminant event the two interior simple roots merge into the single even-multiplicity root. For \(v=0\), \(P(h,0)=(h-1)(h-2)^2\) and \(h=2\) is excluded. This proves all five cases and the algebraic threshold \(\rho_*\). The standalone exact-arithmetic certificate reproduces the resultant, subresultants, rational root isolations, root counts and symbolic performance identity.

## Verification
Run `python verify.py` after installing SymPy (see `requirements.txt`). Its checks use exact rational arithmetic and Sturm root counts; the numerical decimal approximations are not the basis of the proof. In particular the program verifies the critical nonstandard root classification, two independent exact counterexamples, and five affine-recursion cross-checks. No sampling experiment is used to infer an infinite or universal statement. All derived formulas were checked against their original affine recurrences.

## Relationship to prior work
Koloskova, Doikov, Stich and Jaggi (first submitted May 30, 2023, arXiv:2305.19259), in their paper now titled *On Convergence of Incremental Gradient for Non-Convex Smooth Functions*, develop general data-order convergence bounds. Their Section 5.2 discusses reshuffling bounds; their quadratic experiments use a **shared** Hessian. Those bounds neither assert nor imply this exact heterogeneous-curvature stationary phase diagram. Ying, Yuan, Vlaski and Sayed (2018, arXiv:1803.07964), Section V-A, derive exact quadratic stationary formulas for a **common** design matrix, hence the same component Hessian. That work anticipates the equal-curvature mechanism but does not cover the new heterogeneous threshold. The precise comparison here is with-replacement stationary mean-square error at equal numbers of component-gradient calls, not a best-tuned complexity rate or an unconditional superiority claim.

## Limitations
Only two scalar, strictly convex and noninterpolating components are considered, with independent fresh permutations, exact arithmetic, and the individually contractive range. No conclusion is made for larger datasets, momentum, higher dimensions, floating-point implementations, nonquadratic objectives, or optimal step selection. The source literature contains more general rate bounds and shared-Hessian error formulas; priority of the specific algebraic heterogeneity threshold should be independently assessed. The equality at the critical parameter is a genuine stationary comparison, not equality of finite-time error trajectories. Independent scientific validation has not been performed.

## References
- A. Koloskova, N. Doikov, S. U. Stich, M. Jaggi, *On Convergence of Incremental Gradient for Non-Convex Smooth Functions*, arXiv:2305.19259; initial submission May 30, 2023. https://arxiv.org/abs/2305.19259
- B. Ying, K. Yuan, S. Vlaski, A. H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, arXiv:1803.07964; initial submission March 21, 2018. https://arxiv.org/abs/1803.07964
- J. Cha, J. Lee, C. Yun, *Tighter Lower Bounds for Shuffling SGD: Random Permutations and Beyond*, arXiv:2303.07160; initial submission March 13, 2023. https://arxiv.org/abs/2303.07160
