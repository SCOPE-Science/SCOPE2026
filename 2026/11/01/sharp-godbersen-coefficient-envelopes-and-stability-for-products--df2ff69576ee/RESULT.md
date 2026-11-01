# Sharp Godbersen coefficient envelopes and stability for products of planar convex bodies

## Finding
Let \(m\ge2\) and let \(Q_1,\ldots,Q_m\) be arbitrary full-dimensional compact planar convex bodies, embedded in pairwise orthogonal two-planes. Set \(n=2m\), \(K=Q_1\times\cdots\times Q_m\), and
\[
r_i=\frac{V_2(Q_i,-Q_i)}{\operatorname{area}(Q_i)}\in[1,2],\qquad
C_k=[t^k]\prod_{i=1}^m(1+2r_i t+t^2).
\]
Here \(V_d\) denotes the usual symmetric normalized mixed volume. For every \(0\le k\le 2m\), the **exact normalized mixed-volume profile** is
\[
\boxed{\frac{V_{2m}(K[2m-k],(-K)[k])}{\operatorname{vol}_{2m}(K)}=\frac{C_k}{\binom{2m}{k}}.}
\]
Write \(T_{m,k}=[t^k](1+4t+t^2)^m\), \(B_{m,k}=\binom{2m}{k}\), and \(\bar r=m^{-1}\sum_i r_i\). The following inequalities hold simultaneously for all indices \(1\le k\le2m-1\):
\[
\boxed{B_{m,k}\le C_k\le [t^k](1+2\bar r t+t^2)^m\le T_{m,k},}
\]
and the **sharp global affine stability estimate** is
\[
\boxed{T_{m,k}-C_k\ge\frac{T_{m,k}-B_{m,k}}{m}\sum_{i=1}^m(2-r_i).}
\]
The coefficient \((T_{m,k}-B_{m,k})/m\) is the largest possible for every \(m,k\). The upper and lower coefficient envelopes are attained precisely when every factor is a triangle and every factor is centrally symmetric, respectively. In the fixed-average upper estimate, for \(2\le k\le2m-2\), equality holds precisely when all the \(r_i\) are equal. In the affine stability estimate, for these interior indices, equality holds precisely when all factors are triangles or all factors are centrally symmetric. For \(k=1\) or \(2m-1\) the fixed-average and affine estimates are equalities for every choice of factors.

Every vector \((r_1,\ldots,r_m)\in[1,2]^m\) is realized by some such product; thus the fixed-average envelope is also an exact attainable optimization result. In the central index \(k=m\), the optimal ratio to the universal Godbersen bound has the sharp asymptotic
\[
\boxed{\sup_K\frac{V_{2m}(K[m],(-K)[m])}{\binom{2m}{m}\operatorname{vol}_{2m}(K)}
=\frac{[t^m](1+4t+t^2)^m}{\binom{2m}{m}^2}
\sim\sqrt{\frac{3\pi m}{2}}\left(\frac38\right)^m.}
\]
The supremum is taken over the entire Cartesian-product class, and is attained exactly by products of triangles.

## Assumptions and scope
Each \(Q_i\) has positive area. Orthogonal factors and Euclidean Lebesgue volume are used; an invertible affine image has the same normalized mixed-volume profile. The coefficient notation \([t^k]\) extracts the coefficient of \(t^k\). The normalization is fixed by
\[
\operatorname{vol}_d(A+tB)=\sum_{k=0}^d\binom dk V_d(A[d-k],B[k])t^k\quad(t\ge0).
\]
The endpoint indices \(k=0,2m\) yield \(C_k=1\) identically, so the nontrivial claims concern \(1\le k\le2m-1\). The factor quantity \(2-r_i=(6\operatorname{area}(Q_i)-\operatorname{area}(Q_i-Q_i))/(2\operatorname{area}(Q_i))\) is exactly the normalized planar Rogers--Shephard deficit. The result concerns products of planar factors, not arbitrary bodies in \(\mathbb R^{2m}\).

## Proof
**1. Factor parameters and the exact polynomial.** The planar mixed-area identity gives
\[
\operatorname{area}(Q_i+t(-Q_i))=\operatorname{area}(Q_i)(1+2r_it+t^2).
\]
At \(t=1\), planar Rogers--Shephard and Brunn--Minkowski bounds give \(4\operatorname{area}(Q_i)\le\operatorname{area}(Q_i-Q_i)\le6\operatorname{area}(Q_i)\). Hence \(1\le r_i\le2\). Equality at the lower end characterizes centrally symmetric bodies, and equality at the upper end characterizes triangles. Orthogonality and Fubini give
\[
\frac{\operatorname{vol}_{2m}(K+t(-K))}{\operatorname{vol}_{2m}(K)}=\prod_{i=1}^m(1+2r_it+t^2).
\]
Comparing Minkowski polynomial coefficients proves the exact profile.

**2. Both sharp envelopes.** Every coefficient of the product is nondecreasing in each \(r_i\), since the coefficient of \(t^k\) in its derivative with respect to \(r_i\) is
\[
2[t^{k-1}]\prod_{j\ne i}(1+2r_jt+t^2)>0\quad(1\le k\le 2m-1).
\]
The strict inequality follows because the remaining polynomial has strictly positive coefficients in every degree from \(0\) through \(2m-2\). Thus its coordinatewise minima and maxima occur only at the all-one and all-two vectors. At the all-one vector, the polynomial is \((1+t)^{2m}\); at the all-two vector, it is \((1+4t+t^2)^m\). This establishes the coefficient envelopes and both equality classifications.

**3. Fixed-average envelope.** Expanding by the number of linear-in-\(t\) factor choices yields the coefficientwise identity
\[
\prod_i(1+2r_it+t^2)=\sum_{j=0}^m2^j e_j(r_1,\ldots,r_m)t^j(1+t^2)^{m-j},
\]
where \(e_j\) is the \(j\)-th elementary symmetric polynomial. Maclaurin's inequality gives \(e_j(r_1,\ldots,r_m)\le\binom mj\bar r^j\). Every factor multiplying \(e_j\) has nonnegative coefficients. It follows *coefficientwise* that
\[
\prod_i(1+2r_it+t^2)\preceq(1+2\bar r t+t^2)^m.
\]
For even \(k\) with \(2\le k\le2m-2\), the coefficient of \(e_2\) in degree \(k\) is positive. For odd \(k\) with \(3\le k\le2m-3\) (necessarily \(m\ge3\)), the coefficient of \(e_3\) is positive. Equality in Maclaurin's inequality for either \(e_2\) or \(e_3\) therefore forces all positive \(r_i\) to be equal. The parity distinction is essential: the \(e_2\) summand has only even powers. For the two end indices the coefficient depends only on \(e_1\) and equality is automatic.

**4. Sharp affine stability.** Let \(F_k(s)=[t^k](1+2st+t^2)^m\) for \(1\le s\le2\). Expanding \((1+t^2+2st)^m\) shows that \(F_k\) is an increasing polynomial in \(s\) whose coefficients in powers of \(s\) are nonnegative. It is convex; for \(2\le k\le2m-2\) a positive term of degree at least two makes it strictly convex on \([1,2]\). Accordingly
\[
C_k\le F_k(\bar r)\le(2-\bar r)F_k(1)+(\bar r-1)F_k(2).
\]
Using \(F_k(1)=B_{m,k}\), \(F_k(2)=T_{m,k}\), and \(2-\bar r=m^{-1}\sum_i(2-r_i)\) gives the claimed inequality. Strict convexity and the coordinate range imply that equality in the interior-index stability inequality occurs only for the all-one or all-two vectors. At all-one the quotient of both sides by \(\sum_i(2-r_i)=m\) is exactly \((T_{m,k}-B_{m,k})/m\), so no larger universal coefficient works. At the end indices, \(F_k\) is affine and equality is automatic.

**5. Attainability of every parameter.** Fix any nondegenerate planar triangle \(T\) and the centrally symmetric body \(S=(T-T)/2\). The Minkowski interpolation \(Q_\theta=(1-\theta)T+\theta S\), \(0\le\theta\le1\), remains full-dimensional. Its mixed-area ratio \(V_2(Q_\theta,-Q_\theta)/\operatorname{area}(Q_\theta)\) is continuous, starts at \(2\) and ends at \(1\). The intermediate-value theorem provides every target \(r\in[1,2]\). Select the factors independently; selecting all ratios equal realizes the fixed-average envelope.

**6. Central asymptotic.** Write \(H_m=[t^m](1+4t+t^2)^m\). Let independent variables \(Y_i\) take values \(0,1,2\) with probabilities \(1/6,4/6,1/6\). They have mean \(1\), variance \(1/3\), and lattice span one, and
\[
H_m=6^m\Pr\left(\sum_{i=1}^mY_i=m\right).
\]
The standard lattice local central limit theorem therefore gives \(H_m\sim6^m\sqrt{3/(2\pi m)}\). Stirling's formula gives \(\binom{2m}{m}^2\sim16^m/(\pi m)\). Dividing establishes the displayed sharp central-index asymptotic. The identity \(H_m=\sum_{j=0}^{\lfloor m/2\rfloor}\frac{m!}{j!^2(m-2j)!}4^{m-2j}\) also supplies exact integer evaluation at every finite dimension.

## Verification
Run `python3 verify_mixed_products.py` using Python 3 with no external dependencies. The script independently checks the planar Minkowski-polynomial normalization for triangles and squares through exact rational convex-hull area; confirms the two envelopes, the sharp affine inequality and its permitted equality cases at 10,938 coefficient assignments for rational factor parameters with \(1\le m\le6\); and cross-checks central integer coefficients via an independent factorial sum in seven dimensions. The program prints `VERIFY_OK 10957` and central ratios. These tests verify the packaged implementation and examples; the infinite-dimensional claims follow from the analytic arguments above, not finite enumeration. The numerical approach to the asymptotic is illustrative; the proof uses the lattice local central limit theorem and Stirling's formula.

## Relationship to prior work
Kotrbatý and Mouamine proved the universal Godbersen inequality and discussed how its proof relates to Rogers--Shephard stability. Fryš, Kotrbatý, Mouamine and Wang settled the full equality characterization, including a higher-order generalization. Neither statement alone determines exact coefficient envelopes for arbitrary Cartesian products of planar factors, nor a sharp coefficient linear in their individual normalized Rogers--Shephard deficits. The classical planar bounds and equality cases are explicitly used as inputs here, not claimed as new.

Related prior computations concern a single truncated simplex and the optimal two-test-body Bézout coefficient of Cartesian products. The former has a different family of bodies and the latter a different mixed-volume functional; neither of the inspected statements supplies the present sharp fixed-average envelope or coefficientwise affine stability. As with other results obtained from elementary mixed-volume identities, a historically unindexed equivalent tensorization remains a possible priority risk.

## Limitations
The theorem makes no claim of a better coefficient for general nonproduct convex bodies, of a Hausdorff or Banach--Mazur stability rate, or of a general higher-order difference-body inequality. The sharp stability coefficient measures deficits of the planar factors; it does not control geometric distance of each factor to a triangle. The central limit is for \(m\to\infty\) along even ambient dimension. The elementary analytic proof does not establish bibliographic uniqueness, and the originality conclusion has not been independently audited.

## References
1. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387, first submitted 22 July 2026, https://arxiv.org/abs/2607.20387.
2. F. Fryš, J. Kotrbatý, M. A. Mouamine and S. Wang, *Higher-order Godbersen inequality and a characterization of simplices via the face lattice*, arXiv:2610.06806v2, first submitted 5 October 2026, https://arxiv.org/html/2610.06806v2.
3. R. Schneider, *Convex Bodies: The Brunn--Minkowski Theory*, second expanded edition, Cambridge University Press (2014), for normalized mixed volumes, classical Brunn--Minkowski and Rogers--Shephard inequalities, and their equality cases.
4. K. Böröczky, *The stability of the Rogers--Shephard inequality and of some related inequalities*, Advances in Mathematics 190 (2005), 47--76; cited as background, not as a source of the new sharp factor-deficit coefficient.
