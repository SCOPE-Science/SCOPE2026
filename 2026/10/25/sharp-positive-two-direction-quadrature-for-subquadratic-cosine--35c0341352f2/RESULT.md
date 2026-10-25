# Sharp positive two-direction quadrature for subquadratic cosine brightness

## Finding
For every real \(0<p<2\), define
\[
c_p=\frac{\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma(1+p/2)}.
\]
Among all normalized nonnegative rules on two (possibly coalescing) unoriented directions, the exact worst-planar-convex-body relative error in reconstructing the rotational average of the \(p\)-brightness observable is
\[
\boxed{\mathcal E_p^{(2)}=\frac12\left(c_p-\frac12\right)}.
\]
The optimal rule is unique modulo rotation, reversal of unoriented directions and relabeling: two perpendicular directions, each with weight \(1/2\).

There is also a uniform quantitative rigidity statement. If \(0\le\varepsilon<1/4\) and a rule has error at most \(\mathcal E_p^{(2)}+\varepsilon\), its weight and angular separation satisfy
\[
\boxed{\left|w-\frac12\right|\le2\varepsilon,\qquad
 |u\cdot v|\le\sqrt{1-(1-4\varepsilon)^{2/p}}.}
\]
The classical Cauchy case \(p=1\) is explicitly **prior-covered** by a stronger all-nodes planar theorem; the new range is \(0<p<2\), \(p\ne1\). The formula includes the covered case to exhibit one unified subquadratic transition, not to claim its priority.

## Assumptions and scope
Let \(K\subset\mathbb R^2\) be a compact full-dimensional convex body, let \(S_K\) denote its surface-area measure on the unit circle, and let \(S(K)=S_K(S^1)>0\) be its Euclidean perimeter. Let \(\sigma\) be normalized uniform circular measure. For \(p>0\) and a unit direction \(u\), put
\[
\mathcal B_pK(u)=\frac12\int_{S^1}|u\cdot n|^p\,dS_K(n),
\quad
\overline{\mathcal B_pK}=\int_{S^1}\mathcal B_pK(u)\,d\sigma(u)=\frac{c_pS(K)}2.
\]
A two-node rule is \(\mu=w\delta_u+(1-w)\delta_v\) with \(0\le w\le1\) and \(u,v\in S^1\). Its calibrated estimate is \(Q_\mu(K)=w\mathcal B_pK(u)+(1-w)\mathcal B_pK(v)\), with error
\[
\mathcal E_p(\mu)=\sup_{K\text{ full dimensional}}
\frac{|Q_\mu(K)-\overline{\mathcal B_pK}|}{S(K)}.
\]
Each orientation is unoriented because the kernel is even. The universal supremum is over all such \(K\), independent of the rule.

## Proof
**1. Reduce the convex-body supremum to a scalar angular discrepancy.** For a unit normal \(n\), write
\[
F_\mu(n)=w|u\cdot n|^p+(1-w)|v\cdot n|^p.
\]
Exchanging integrals and using the definition of \(c_p\) gives
\[
\frac{Q_\mu(K)-\overline{\mathcal B_pK}}{S(K)}
=\frac1{2S(K)}\int_{S^1}(F_\mu(n)-c_p)\,dS_K(n).
\]
Consequently \(\mathcal E_p(\mu)\le\tfrac12\|F_\mu-c_p\|_\infty\). To attain its sharp supremum, let \(n_0\) be a direction realizing the absolute maximum; use increasingly thin, long rectangles whose two long edge normals are \(\pm n_0\). Their normalized surface-area measures converge weakly to \((\delta_{n_0}+\delta_{-n_0})/2\). Since \(F_\mu-c_p\) is even and continuous, the ratio converges to \(\tfrac12|F_\mu(n_0)-c_p|\). Thus
\[
\boxed{\mathcal E_p(\mu)=\tfrac12\|F_\mu-c_p\|_\infty.}\tag{1}
\]
This is also a special case of the sharp defect identity of An (2026); the identity itself is not a novelty claim.

**2. Universal obstruction and equality conditions.** Choose unit vectors perpendicular to \(u\) and \(v\). If \(s=|\det(u,v)|\le1\), then \(F_\mu\) has the respective values \((1-w)s^p\) and \(ws^p\) at these two normals. Therefore
\[
\min_nF_\mu(n)\le\min(w,1-w)s^p\le\frac12.
\]
For \(0<p<2\), the normalized circular mean \(c_p\) is strictly greater than \(1/2\), since \(|\cos\theta|^p>|\cos\theta|^2\) on an open angular set. Equation (1) now proves
\[
\mathcal E_p(\mu)\ge\frac12\left(c_p-\frac12\right).
\]
Equality requires \(\min(w,1-w)s^p\ge1/2\), forcing \(w=1/2\) and \(s=1\). Hence every possible optimizer has equally weighted perpendicular directions.

**3. Sharpness: the upper deviation is never dominant.** For this perpendicular rule, rotate coordinates and put \(a=p/2\in(0,1)\). Then
\[
F(\theta)=\frac12\bigl(|\cos\theta|^p+|\sin\theta|^p\bigr)
=2^{-a}g(|\cos2\theta|),
\quad g(t)=\frac{(1+t)^a+(1-t)^a}{2}.
\]
Concavity of the power function gives \(\min F=1/2\) (at coordinate directions) and \(\max F=2^{-a}\) (at their bisectors). The symmetric generalized binomial expansion for \(0\le t<1\) is
\[
g(t)=1-\sum_{k\ge1}b_kt^{2k},\qquad
b_k=-\binom a{2k}>0.
\]
The coefficients are summable up to the endpoint \(t=1\), and \(\sum_{k\ge1}b_k=1-2^{a-1}\), because \(g(1)=2^{a-1}\). For uniformly distributed \(\theta\), \(T=|\cos2\theta|\) satisfies \(\mathbb E T^{2k}\le\mathbb E T^2=1/2\) for every \(k\ge1\). Positivity and monotone convergence thus give
\[
\begin{aligned}
c_p=\mathbb E F(\theta)
&=2^{-a}\left(1-\sum_{k\ge1}b_k\mathbb E T^{2k}\right)\\
&\ge2^{-a}\left(1-\frac12(1-2^{a-1})\right)
=\frac{2^{-a}+1/2}{2}.
\end{aligned}
\]
This is exactly \(2^{-a}-c_p\le c_p-1/2\). Hence the maximum angular discrepancy is \(\|F-c_p\|_\infty=c_p-1/2\); the universal lower bound is attained. Every equality and boundary assertion follows without numerical approximation.

**4. Quantitative rigidity.** Suppose \(\mathcal E_p(\mu)\le\tfrac12(c_p-1/2)+\varepsilon\), with \(0\le\varepsilon<1/4\). By equation (1), \(\min F_\mu\ge1/2-2\varepsilon\). Using the two perpendicular test normals from step 2 yields
\[
\min(w,1-w)s^p\ge1/2-2\varepsilon.
\]
Because both factors on the left are respectively at most \(1/2\) and \(1\), we deduce \(\min(w,1-w)\ge1/2-2\varepsilon\) and \(s^p\ge1-4\varepsilon\). Thus \(|w-1/2|\le2\varepsilon\) and \(|u\cdot v|=\sqrt{1-s^2}\le\sqrt{1-(1-4\varepsilon)^{2/p}}\). These are necessary stability estimates, not asserted to have individually optimal constants.

## Verification
The complete all-exponent result rests on the four analytic proof steps, including the sign and absolute summability of generalized binomial coefficients, exact angular mean, thin-rectangle sharpness argument and equality analysis. The accompanying standalone `verify.py` independently evaluates the gamma normalization, compares both angular extremal deviations, tests many off-optimal rules against the lower bound and checks the necessary stability inequalities. Its finite floating-point checks are corroboration, not an infinite proof.

## Relationship to prior work
An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs* (first public 2026-09-05, arXiv:2609.05869v1) supplies the general norm identity in step 1, a full finite-exactness criterion and a non-exactness conclusion for non-even power kernels. Those statements do **not** optimize the sharp worst-case error among all calibrated positive two-node rules or imply its unique optimizer and rigidity. An's October 8 followup (arXiv:2610.11814v1) analyzes circle designs, Gauss–Chebyshev quadrature, reconstruction and a regular grid for the classical Cauchy kernel; it does not provide the above full range of power-kernel minimax values.

The published published-finding corpus finding *Sharp positive \(N\)-direction Cauchy quadrature and angular rigidity* (October 11, 2026) **already proves the specialization \(p=1\)**, and more generally every number of nodes for the classical Cauchy kernel. We make no priority claim for this included specialization, nor for the reduction in step 1. The additional claim is the full subquadratic continuum \(0<p<2\), \(p\ne1\), with an all-parameter proof and the indicated precise two-node stability bounds. Neither an all-nodes proof for exponent one nor absence of any finite exact rule implies these sharp non-unit-exponent minimax constants. Literature indexed under power-cosine transforms, convex approximation or two-atom quadrature remains a residual priority risk.

## Limitations
The theorem assumes real \(0<p<2\), fixed calibrated nonnegative two-node rules and perimeter-normalized worst error over all planar full-dimensional convex bodies. It is silent about \(p>2\), signed weights, more than two nodes, adaptive directions or higher-dimensional convex bodies. The angular bound is necessary and no assertion of best possible stability constants is made. The supremum over bodies can be approached by degenerating rectangles; no finite-area maximizing body is asserted. This is a self-review mathematical argument and numerical cross-check, not independent audit.

## References
1. C. An, *Exact Finite Integral Geometry: Directional Kernels and Spherical Designs*, arXiv:2609.05869v1, 2026-09-05, especially its sharp norm identity and \(p\)-kernel theorem.
2. C. An, *Gauss–Chebyshev Quadrature, \(\mathbb S^1\)-Designs, and the Planar Minkowski Inverse Problem*, arXiv:2610.11814v1, 2026-10-08.
3. *Sharp positive \(N\)-direction Cauchy quadrature and angular rigidity*, published-finding corpus published research, 2026-10-11, identifier `2026/10/11/SCOPE-sharp-positive-n-direction-cauchy-quadrature-and-angular-rigidit--33b1062b46ae`, especially its RESULT.md and its acknowledged use of An's norm identity.
