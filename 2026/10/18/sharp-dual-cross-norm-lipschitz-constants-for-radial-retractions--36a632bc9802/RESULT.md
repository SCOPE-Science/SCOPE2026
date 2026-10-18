# Sharp dual cross-norm Lipschitz constants for radial retractions of finite-dimensional \(\ell_p\) balls

## Finding
Let \(n\ge2\), \(1<p<\infty\), \(p'=p/(p-1)\), and \(w_1,\ldots,w_n>0\). On real \(\mathbb R^n\), consider radial retraction onto the unit \(\ell_p\)-ball,
\[
R_p(x)=\frac{x}{\max\{1,\|x\|_p\}}.
\]
For \(\|x\|_{\infty,w}=\max_i|x_i|/w_i\) and its dual norm \(\|x\|_{1,w}=\sum_iw_i|x_i|\), define the optimal global Lipschitz constants \(L_{\infty,w}(R_p)\) and \(L_{1,w}(R_p)\), respectively, measuring inputs and outputs with the **same indicated coordinate norm** even though the ball itself uses \(\|\cdot\|_p\). Put \(m=\min_iw_i\) and
\[
B_s(w)=\left(\sum_{i=1}^n(w_i/m)^s-1\right)^{1/s},\quad
F_s(k)=\max_{t\ge0}\frac{1+kt}{1+t^s}\qquad(s>1,k>0).
\]
Then the two **sharp global constants** are exactly
\[
\boxed{L_{\infty,w}(R_p)=F_p(B_p(w)),\qquad L_{1,w}(R_p)=F_{p'}(B_{p'}(w)).}
\]
The scalar maximizer is unique and positive, determined by
\[
k=s t^{s-1}+(s-1)k t^s.
\]
Both constants are attained as suprema of exterior limiting derivative norms; explicit maximizing unit directions are given in the proof.

For each of the two coordinate norms separately, the constant is uniquely minimized among positive weights up to common scaling by equal weights. Its minimal values are \(F_p((n-1)^{1/p})\) and \(F_{p'}((n-1)^{1/p'})\). Writing \(c_s=(s-1)^{(s-1)/s}/s\), these have distinct exact leading dimension laws:
\[
L_{\infty,\mathbf1}(R_p)=c_p(n-1)^{1/p}+O_p(1),\qquad
L_{1,\mathbf1}(R_p)=c_{p'}(n-1)^{1/p'}+O_p(1).
\]
For every \(p\ne2\), the ordering of these two constants in the unweighted two-dimensional case is the **reverse** of their ordering for all sufficiently large dimensions. At \(p=2\), both are instead identically \((1+\|w\|_2/m)/2\), for every weight vector and dimension.

## Assumptions and scope
All vectors and derivatives are **real**; \(n\ge2\), \(1<p<\infty\), and every weight is strictly positive. The ball defining \(R_p\) is the standard unweighted \(\ell_p\)-ball; the two weighted norms are used solely as input/output error metrics. Constants are optimal over all distinct input pairs in \(\mathbb R^n\), not merely infinitesimal derivatives. The one-dimensional case is trivial, with constant \(1\); the limiting exponent cases \(p=1\) and \(p=\infty\) are not included.

## Proof
**1. Reduction to tangential projections.** For \(r=\|x\|_p>1\), let \(u=x/r\), \(\|u\|_p=1\), and \(\phi_i=\operatorname{sgn}(u_i)|u_i|^{p-1}\). Then \(\phi\cdot u=1\) and
\[
DR_p(x)=r^{-1}(I-u\phi^{\mathsf T}).
\]
Inside the unit ball the derivative is \(I\). The map is continuous and piecewise continuously differentiable on each line segment: its intersection with the strictly convex unit \(\ell_p\)-sphere has at most two points. Integrating the derivative along any segment gives a global Lipschitz upper bound by \(\max\{1,\sup_{\|u\|_p=1}\|I-u\phi^{\mathsf T}\|\}\) in either coordinate norm. Conversely, differences at exterior points \(x=ru\), followed by \(r\downarrow1\), approximate every tangential derivative norm. Thus equality holds. All the displayed maximized norms below exceed \(1\), so the interior derivative does not alter the answer.

**2. Weighted maximum norm.** The induced norm of a real matrix in \(\|\cdot\|_{\infty,w}\) is its maximum weighted absolute row sum. The row indexed by \(i\) of \(I-u\phi^{\mathsf T}\) has norm
\[
1-|u_i|^p+\frac{|u_i|}{w_i}\sum_{j\ne i}w_j|u_j|^{p-1}.
\]
Fix \(a=|u_i|\in[0,1]\). Hölder gives the sharp bound
\[
\sum_{j\ne i}w_j|u_j|^{p-1}\le
\left(\sum_{j\ne i}w_j^p\right)^{1/p}(1-a^p)^{(p-1)/p};
\]
equality is attained when \(|u_j|\) for \(j\ne i\) is proportional to \(w_j\). Put \(k_i=(\sum_{j\ne i}w_j^p)^{1/p}/w_i\) and \(t=a/(1-a^p)^{1/p}\). The optimal row value is \((1+k_it)/(1+t^p)\). For fixed \(\sum_jw_j^p\), the quantity \(k_i^p=(\sum_jw_j^p)/w_i^p-1\) is largest precisely when \(w_i=m\). Since \(F_p(k)\) increases strictly in \(k>0\), the global maximum is \(F_p(B_p(w))\). For a minimizing-weight index \(i\) and maximizing \(t\), take
\[
u_i=\frac{t}{(1+t^p)^{1/p}},\qquad
u_j=\frac{w_j}{(\sum_{\ell\ne i}w_\ell^p)^{1/p}(1+t^p)^{1/p}}\quad(j\ne i),
\]
with positive coordinates (and arbitrary individual sign choices); this supplies equality for the boundary derivative. Strict Hölder equality and the unique scalar maximizer show that, up to those signs and the choice of any index of minimal weight, all maximizing directions arise this way.

**3. Weighted sum norm.** The induced norm of a real matrix in \(\|\cdot\|_{1,w}\) is its maximum weighted absolute column sum. For column \(i\), the expression is
\[
1-|u_i|^p+\frac{|u_i|^{p-1}}{w_i}\sum_{j\ne i}w_j|u_j|.
\]
Hölder with conjugate exponents \(p,p'\) bounds the sum by \((\sum_{j\ne i}w_j^{p'})^{1/p'}(1-a^p)^{1/p}\); equality holds when \(|u_j|\) is proportional to \(w_j^{1/(p-1)}\). With \(k_i=(\sum_{j\ne i}w_j^{p'})^{1/p'}/w_i\), write \(t=a/(1-a^p)^{1/p}\). The column value becomes \((1+k_it^{p-1})/(1+t^p)\). Substituting \(v=t^{p-1}\) turns it into \((1+k_iv)/(1+v^{p'})\), which is \(F_{p'}(k_i)\). Again \(k_i\) is maximal at an index with \(w_i=m\); equality is realized by
\[
u_i=\frac{t}{(1+t^p)^{1/p}},\qquad
u_j=\frac{(w_j/B)^{1/(p-1)}}{(1+t^p)^{1/p}}\quad(j\ne i),
\]
where \(B=(\sum_{\ell\ne i}w_\ell^{p'})^{1/p'}\), and \(v=t^{p-1}\) is the positive maximizer of \(F_{p'}(k_i)\). These, with arbitrary coordinate signs and any minimum-weight index, exhaust maximizing derivative directions by Hölder equality and scalar uniqueness.

**4. Scalar uniqueness and dimension effects.** Differentiating \((1+kt)/(1+t^s)\) shows the sign of the derivative equals the sign of \(k-s t^{s-1}-(s-1)kt^s\), strictly decreasing from \(k>0\) to a negative value. This proves unique positive maximization. The optimal weights follow from \(B_s(w)\ge(n-1)^{1/s}\), with equality exactly when all weights equal, and strict monotonicity of \(F_s\).

For \(k>0\),
\[
c_sk\le F_s(k)\le c_sk+1,\qquad
c_s=\max_{t\ge0}\frac{t}{1+t^s}=\frac{(s-1)^{(s-1)/s}}s,
\]
proving the dimension laws. To prove the finite-versus-large-dimensional reversal, note first that \(F_s(1)\) strictly increases in \(s>1\): every maximizing \(t\) lies in \((0,1)\) (values at \(t\ge1\) are at most \(1\)), and for such \(t\) the denominator \(1+t^s\) strictly decreases in \(s\). Thus in dimension two the larger of \(p,p'\) gives the larger Lipschitz constant, whereas the leading exponents \(1/p\) and \(1/p'\) show that the smaller of \(p,p'\) wins for all sufficiently large \(n\). Finally \(F_2(k)=(1+\sqrt{1+k^2})/2\), and \(1+B_2(w)^2=\|w\|_2^2/m^2\), giving the claimed Hilbert specialization.

## Verification
The included self-contained Python program `verification.py` performs 4,371 deterministic assertion groups (several contain multiple inequalities). It checks the exact scalar optimizer, both induced derivative norms and equality witnesses for many exponents, dimensions, and positive weights, uniform analytic upper bounds on random sphere directions, exterior finite differences, the Hilbert specialization, and the asymptotic bounds. Run `python verification.py` with a standard Python interpreter; successful execution prints `VERIFY_OK 4371 assertion groups, multiple assertions per group`. The proof above, not finite computations, establishes the universal claims.

## Relationship to prior work
Rieffel's 2005 preprint, Section 8, develops radial retractions and the general Lipschitz bound \(2\) **when the same ambient norm defines both the ball and input/output distances**. Thele's 1974 radial-projection results and Kapoor–Mathur's 1983 metric-projection-bound approach likewise concern the native norm. Christianson and coauthors (2022) discuss the same-norm radial constant and its geometric estimates. These do not supply the two distinct weighted-coordinate cross-norm constants, which may grow with dimension. The case \(p=2\) is already a known special case of the weighted Euclidean-ball computation; its appearance here verifies compatibility rather than claiming separate novelty. The new statement is the full all-exponent pair and its conjugate dimension reversal.

## Limitations
Only real finite-dimensional spaces and \(1<p<\infty\) are covered; no complex-field or endpoint-exponent formula is claimed. The finite computations are corroborative, not a proof for infinitely many parameter choices. The full texts of Thele (1974) and Kapoor–Mathur (1983) were not available for direct inspection, so a historically equivalent cross-norm formulation cannot be categorically excluded. The formulas describe radial retraction, not arbitrary nonlinear or nearest-point projections in a different metric.

## References
1. M. A. Rieffel, *Lipschitz extension constants equal projection constants*, arXiv:math/0508097, publicly submitted 2005-08-04, Section 8. https://arxiv.org/html/math/0508097v5
2. R. L. Thele, *Some results on the radial projection in Banach spaces*, Proc. Amer. Math. Soc. 42 (1974), 483–486. DOI: 10.1090/S0002-9939-1974-0328550-1.
3. O. P. Kapoor and S. B. Mathur, *Metric projection bound and the Lipschitz constant of the radial retraction*, J. Approx. Theory 38 (1983), 66–70.
4. K. Christianson et al., *Chasing convex bodies and functions with black-box advice*, arXiv:2206.11780 (2022), Section 4.1 and Appendix C. https://arxiv.org/html/2206.11780v1
