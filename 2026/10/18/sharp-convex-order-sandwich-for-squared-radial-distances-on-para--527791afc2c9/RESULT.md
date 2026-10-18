# Sharp convex-order sandwich for squared radial distances on parallelogram boundaries

## Finding

Let \(P\) be any nondegenerate Euclidean parallelogram, centered at the origin, with perimeter \(4L\), where \(L>0\). Choose \(X_P\) uniformly with respect to arclength on its boundary and put \(Z_P=\|X_P\|_2^2\). Let \(U\) be uniform on \([-1,1]\), and define the square and degenerate-needle benchmarks
\[
Z_{\rm sq}=\frac{L^2}{4}(1+U^2),\qquad Z_{\rm nd}=L^2U^2.
\]
**Theorem.** For *every* continuous convex \(\Phi:[0,L^2]\to\mathbb R\),
\[
\boxed{\mathbb E\Phi(Z_{\rm sq})\le\mathbb E\Phi(Z_P)\le\mathbb E\Phi(Z_{\rm nd}).}
\]
All three laws have mean \(L^2/3\); these inequalities are genuine convex-order domination, not merely bounds for increasing tests. If \(\Phi\) is strictly convex, the left equality holds precisely when \(P\) is a Euclidean square, and the right inequality is strict for every nondegenerate \(P\). The right bound is sharp along parallelograms collapsing to a line segment of length \(2L\).

In particular, for every \(p>-1\) with \(p\notin\{0,2\}\), the power-weighted perimeter average \(\mathbb E\|X_P\|_2^p\) has the uniquely optimal square and sharp needle bounds: the above order holds for \(-1<p<0\) and \(p>2\), and reverses for \(0<p<2\). Its exact benchmark values are
\[
\mathbb E\|X_{\rm sq}\|_2^p=\left(\frac L2\right)^p\int_0^1(1+t^2)^{p/2}\,dt,
\qquad \mathbb E\|X_{\rm nd}\|_2^p=\frac{L^p}{p+1}.
\]
At \(p=0\) and \(p=2\), these averages are shape-independent. Multiplication by \(4L\) converts averages into the corresponding radial weighted perimeters.

## Assumptions and scope

Write \(P=\{tu+sv:-1\le t,s\le1\}\), where \(u,v\in\mathbb R^2\) are nonparallel and nonzero, and put \(a=\|u\|_2\), \(b=\|v\|_2\), \(L=a+b\), \(c=\langle u,v\rangle/(ab)\). Then \(a,b>0\) and \(|c|<1\). The reference square has side length \(L\), hence perimeter \(4L\). The reference needle is the *limiting doubled-edge arclength law*: it is not a nondegenerate body. All sampling is with respect to normalized Euclidean boundary length, not uniform angular direction or area. The center is the midpoint of the diagonals; a translated origin is not covered.

## Proof

**1. Exact law and common mean.** The four edges are sampled by first choosing the two edges parallel to \(u\) with probability \(a/L\), and the two edges parallel to \(v\) with probability \(b/L\). With independent \(T\sim\operatorname{Unif}[-1,1]\) and symmetric sign \(S\in\{-1,+1\}\), the respective boundary points are \(Tu+Sv\) and \(Su+Tv\). Their squared lengths are
\[
Z_a=b^2+a^2T^2+2ab\,cST,\qquad
Z_b=a^2+b^2T^2+2ab\,cST.\tag{1}
\]
Since \(\mathbb ET^2=1/3\) and \(\mathbb E S=0\),
\[
\mathbb EZ_P=\frac{a(b^2+a^2/3)+b(a^2+b^2/3)}{L}=\frac{L^2}{3}.\tag{2}
\]
The same mean holds for both benchmarks.

**2. Angle reduction and sharp needle comparison.** For any convex \(\Phi\), the function
\[
h_d(s)=\frac{\Phi(d+s)+\Phi(d-s)}2
\]
is nondecreasing in \(s\ge0\) as long as the arguments remain in its domain: convexity of \(\Phi\) gives increasing symmetric secant spreads. Conditional on \(T\) and edge type in (1), the sign average is such an \(h_d(2ab|cT|)\). Therefore the expectation of \(\Phi(Z_P)\) is nondecreasing in \(|c|\). At \(c=0\) it is the rectangular law with the same side lengths, so
\[
Z_{a,b,0}\le_{\rm cx}Z_P\le_{\rm cx}Z_{a,b,1}.\tag{3}
\]
Here the \(c=1\) law denotes the collinear limit. Its *signed coordinate* is uniform on \([-L,L]\): the four signed edge intervals \([b-a,L]\), \([-L,a-b]\), \([a-b,L]\), \([-L,b-a]\) have respective constant density contributions \(1/(4L)\). Their sum is \(1/(2L)\) everywhere in \([-L,L]\). Thus \(Z_{a,b,1}\) is distributed as \(L^2U^2\), regardless of \(a,b\). The second inequality in (3) is strict for strictly convex \(\Phi\) when \(|c|<1\), because \(ab>0\) and \(T\ne0\) almost surely.

**3. A single-crossing proof for rectangles.** Interchange the generators, if necessary, so \(a\ge b>0\). The cumulative distribution function \(F_{a,b}\) for \(Z_{a,b,0}\) is
\[
F_{a,b}(s)=\begin{cases}
\dfrac{\sqrt{(s-a^2)_+}+\sqrt{(s-b^2)_+}}L,&s<a^2+b^2,\\
1,&s\ge a^2+b^2,
\end{cases}\tag{4}
\]
where \(z_+=\max\{0,z\}\). For \(a=b=L/2\) this becomes
\[
F_{\rm sq}(s)=\begin{cases}
0,&s<L^2/4,\\
2\sqrt{s-L^2/4}/L,&L^2/4\le s<L^2/2,\\
1,&s\ge L^2/2.
\end{cases}\tag{5}
\]
If \(a>b\), there is precisely one sign change of \(F_{a,b}-F_{\rm sq}\), at
\[
s_*=\frac{L^2-b^2}{3},\qquad \frac{L^2}{4}<s_*<\frac{L^2}{2},\quad s_*\le a^2.
\]
Indeed, below \(L^2/4\) the square CDF vanishes; for \(L^2/4\le s<a^2\) with \(s<L^2/2\), comparison of (4)--(5) reduces to comparing \(s-b^2\) with \(4(s-L^2/4)\), whose difference is \(L^2-b^2-3s\). For \(a^2\le s<L^2/2\), concavity of \(\sqrt{\cdot}\) gives
\[
F_{a,b}(s)\le\frac2L\sqrt{s-\frac{a^2+b^2}{2}}
<\frac2L\sqrt{s-\frac{L^2}{4}}=F_{\rm sq}(s),
\]
since \(a^2+b^2>L^2/2\). Above \(L^2/2\) the square CDF equals one. Consequently, \(F_{a,b}-F_{\rm sq}\) is nonnegative below \(s_*\) and nonpositive above it, with a strict sign on nonempty intervals.

Both laws have the same mean by (2), so their CDF difference integrates to zero over \([0,L^2]\). Its partial integral \(\int_0^t(F_{a,b}-F_{\rm sq})\,ds\) is therefore nonnegative for every \(t\). The standard integrated-CDF characterization of convex order (or the integral representation of convex functions by positive-part hinges) yields \(Z_{\rm sq}\le_{\rm cx} Z_{a,b,0}\). Strict inequality for strictly convex tests follows from the strict CDF crossing unless \(a=b\). Combining with (3) proves the theorem. The case \(a=b\) is equality for rectangles, and angle strictness forces \(c=0\) for a square.

**4. Power laws and sharpness.** The functions \(s\mapsto s^{p/2}\) are strictly convex for \(-1<p<0\) and \(p>2\), strictly concave for \(0<p<2\), and constant/affine at \(p=0,2\). The needle moment is finite exactly for \(p>-1\). The formulas are direct integration of the benchmark laws. Approaching \(|c|=1\) with fixed \(a,b\) gives sharp convergence of the positive and integrable negative-power moments. For the latter, uniform integrability follows from the fact that the signed collinear densities remain bounded near zero after integration over the four edge intervals and from \(p>-1\).

A useful check at the fourth radial moment is
\[
\mathbb E\|X_P\|_2^4=\frac{L^4}{5}-\frac{\operatorname{area}(P)^2}{12},\tag{6}
\]
obtained by expanding (1). This identity follows also by simplification of the published boundary-moment equations in reference [3] and **is not itself asserted to be an independent new discovery**. The new assertion is the uniform comparison for the *entire convex-function class*, including the square extremizer.

## Verification

Run `python scripts/check_convex_order.py` with NumPy installed. It checks exact quadratic/fourth-moment identities against deterministic high-order Gaussian quadrature; evaluates multiple nonlinear convex test functions and hinges for 140 aspect-ratio/angle configurations; and verifies the predicted single crossing for 58 rectangle ratios and 130 thresholds each. Successful output begins `RADIAL_CONVEX_ORDER_CHECK_OK`. The universal conclusion rests on the complete inequalities in steps 1--4, not finite tests.

## Relationship to prior work

Csató, Giovagnoli and Roy [1, Theorem 1.4 and Corollary 1.5] prove needle comparisons for selected radial weights under two reflection axes or four-quadrant convexity. Their theorem explicitly does not cover all centrally symmetric curves, and it does not give the simultaneous square lower envelope for all convex tests of squared distance. Sachs's earlier second-moment identity for centrally symmetric parallelograms is discussed in [1, Introduction, pp. 2--3]; the shape-independence at \(p=2\) is already known. A published parallelogram fourth-chord computation [3] includes the raw fourth radial boundary moment, hence formula (6) is included only as an algebraic consistency check; a fourth-moment formula does not imply the stop-loss inequalities or comparisons for every convex test. Tokmachev [2] compares *interior* with *boundary* distributions for one fixed body; its pairwise comparisons do not compare boundary laws of different parallelograms at equal perimeter.

## Limitations

This is a theorem for planar Euclidean nondegenerate parallelograms centered at their diagonal intersection, at a fixed Euclidean perimeter. It does not claim an extremizer among arbitrary convex curves, a translated-origin version, or a higher-dimensional analogue. The needle is a limiting double-edged segment, not a member of the nondegenerate class. Historical priority cannot be certified from finite indexed and primary-text comparisons; source [2] was assessed at abstract level because its full text was not accessible here.

## References

[1] G. Csató, D. Giovagnoli, P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, first posted 2026-08-20, https://arxiv.org/abs/2608.19851, especially Theorem 1.4, Corollary 1.5, and §3.3.

[2] A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869v1, first posted 2026-07-09, https://arxiv.org/abs/2607.08869.

[3] *Fourth-chord moment amplification and angular phase transition for parallelograms*, publicly available mathematical research record, first posted 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e.
