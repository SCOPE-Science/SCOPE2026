# Fourth-root high-tilt fingerprints and exact inverse-Gaussian marginal criterion for coupled multitype clocks

## Finding
For a coupled multitype inverse-Gaussian subordinator with nonsingular \(M\)-matrix parameter \(B\), the first nontrivial correction to the leading coordinate Laplace exponent is a fourth root, and it detects the off-diagonal entries of the relevant row of \(B\):
\[
\lim_{t\to\infty}\frac{\Psi_i(t)-\eta_i\sqrt{2t}}{t^{1/4}}=2^{3/4}\sum_{j\ne i}\eta_j\sqrt{-B_{ij}}.
\]
In particular, for strictly positive \(\eta\), a coordinate is a classical inverse-Gaussian (IG) subordinator exactly when its corresponding row of \(B\) has zero off-diagonal entries. This is a one-coordinate statement, and does not require that \(B\) be diagonal.

## Assumptions and scope
Fix an integer \(d\ge2\). Let \(B=(B_{ij})\) be a real nonsingular \(M\)-matrix: all off-diagonal entries are nonpositive, all diagonal entries are strictly positive, and \(B^{-1}\) is entrywise nonnegative. Let \(\eta\in(0,\infty)^d\). By the established multitype inverse-Gaussian construction [1, Theorem 2.2 and Lemma 4.1], for each \(u\in[0,\infty)^d\), there is a unique nonnegative vector \(z(u)\) solving
\[
 B^\top z(u)+\tfrac12 z(u)^{\circ2}=u.
\]
The associated subordinator \(Z\) has \(\mathbb E\exp(-\langle u,Z_h\rangle)=\exp(-h\eta^\top z(u))\) for \(h\ge0\). For fixed \(i\), write \(\Psi_i(t)=\eta^\top z(t e_i)\), so \(\mathbb E e^{-tZ_{h,i}}=e^{-h\Psi_i(t)}\). Set \(a_{kj}=-B_{kj}\ge0\) for \(k\ne j\), and \(b_j=B_{jj}>0\). All limits below are for fixed \(B,\eta,i,d\) and \(t\to\infty\).

## Proof
The defining component equations, with \(z=z(t e_i)\), are
\[
 \tfrac12 z_j^2+b_jz_j=t\mathbf1_{\{j=i\}}+\sum_{k\ne j}a_{kj}z_k,\qquad 1\le j\le d.
\]
All components are nonnegative. Put \(r=z_i\), \(M=\max_{j\ne i}z_j\), and \(C=1+\max_j\sum_{k\ne j}a_{kj}\). At an index attaining the maximum \(M\), the nonnegative equation gives \(M^2/2\le C(r+M)\), so \(M=O(1+\sqrt r)\). The equation for \(r\) implies \(r^2/2+b_ir=t+O(M)\), and consequently \(r=O(1+\sqrt t)\): otherwise the quadratic left-hand side would dominate both \(t\) and the \(O(\sqrt r)\) remainder. It follows that \(M=O(t^{1/4})\). Because its equation has a nonnegative right-hand addition to \(t\), \(r\ge \sqrt{b_i^2+2t}-b_i\). Its upper bound from the quadratic equation with an \(O(t^{1/4})\) extra term now yields
\[
 r=\sqrt{b_i^2+2t}-b_i+O(t^{-1/4})=\sqrt{2t}-b_i+O(t^{-1/4}).
\]
For every \(j\ne i\), the component equation becomes
\[
 \tfrac12 z_j^2+b_jz_j=a_{ij}r+O(M)
  =a_{ij}\sqrt{2t}+O(t^{1/4}+1).
\]
Divide by \(t^{1/2}\). Since \(z_j=O(t^{1/4})\), the linear term vanishes. Nonnegativity then gives the exact componentwise limits
\[
 \lim_{t\to\infty} t^{-1/4}z_j=2^{3/4}\sqrt{a_{ij}},\qquad j\ne i.
\]
The formula includes \(a_{ij}=0\), for which the limit is zero. Finally \(r-\sqrt{2t}=O(1)\), and summing against the fixed positive weights \(\eta_j\) proves the displayed fourth-root coefficient.

If every \(a_{ij}=0\) for \(j\ne i\), the vector with \(z_i=\sqrt{b_i^2+2t}-b_i\) and all other entries zero solves the equations exactly. Uniqueness [1] gives \(\Psi_i(t)=\eta_i(\sqrt{b_i^2+2t}-b_i)\), the classical IG subordinator exponent. Conversely, if some \(a_{ij}>0\), strict positivity of \(\eta_j\) makes the fourth-root coefficient positive. Every drift-free classical IG Laplace exponent is \(c(\sqrt{\beta^2+2t}-\beta)\) with \(c,\beta>0\), and differs from its leading \(c\sqrt{2t}\) term by a bounded quantity. A drifted IG exponent has a linear leading term, incompatible with \(\Psi_i(t)\sim\eta_i\sqrt{2t}\). Hence the positive fourth-root correction precludes any classical IG law. The conclusion holds at each fixed \(h>0\) because its Laplace exponent is \(h\Psi_i\).

## Verification
The included dependency-free checker evaluates the exact two-type triangular solution for multiple couplings and tilts, verifies its coupled quadratic system, the decoupled marginal, and convergence of the normalized fourth-root correction toward the derived coefficient. These finite tests corroborate algebra; the preceding estimates, not numerical extrapolation, establish the limit for every fixed nonsingular \(M\)-matrix.

## Relationship to prior work
Wang, Xu and Zhu [1] established the coupled quadratic Laplace exponent, its uniqueness, and the diagonal independent-IG case. Those are inputs, not the new result. The new statements evaluate the high-frequency asymptotics for each coordinate in arbitrary coupled systems and give a necessary-and-sufficient row criterion for a classical IG marginal, including coupled matrices with selected IG coordinates. Chaumont and Marolleau [2] established general additive-Lévy-field first-passage transform identities. Their framework is closely related to the origin of the coupled system; the present computation concerns the explicit fourth-root coefficient and its marginal interpretation. No assertion of publication priority or independence is made.

## Limitations
Only one-coordinate Laplace tilts are analyzed. The expansion is pointwise for fixed matrix and immigration vector; no uniformity as coupling coefficients vanish or dimension grows is shown. The criterion requires strictly positive immigration in every coordinate; zero weights can conceal nonzero couplings. The result neither identifies \(B\) from the coefficient alone nor proves sample-path approximations. General first-passage formulae in older literature could contain an equivalent evaluation not located in this review; independent literature audit remains outstanding.

## References
[1] Y. Wang, W. Xu and L. Zhu, *A Hawkes Microfoundation for Multitype Inverse Gaussian Subordinators*, arXiv:2610.10525v1, first posted 2026-10-07, Sections 2, 4 and 6; https://arxiv.org/html/2610.10525v1.

[2] L. Chaumont and M. Marolleau, *Fluctuation theory for spectrally positive additive Lévy fields*, arXiv:1912.10474v1 (2019), *Electronic Journal of Probability* 25 (2020); https://arxiv.org/abs/1912.10474.
