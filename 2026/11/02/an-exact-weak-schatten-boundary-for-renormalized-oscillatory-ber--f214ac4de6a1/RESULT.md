# An exact weak-Schatten boundary for renormalized oscillatory Bergman semicommutators

## Finding

Fix an integer \(d\ge1\), a weight parameter \(\alpha>-1\), and a nonzero real frequency \(s\). On the normalized analytic weighted Bergman space \(A^2_\alpha(\mathbb B_d)\) define the unimodular radial symbol
\[
u_s(z)=\exp\bigl(is\log(1-\|z\|^2)\bigr).
\]
Let \(T_f=P_\alpha M_f\vert_{A^2_\alpha}\) be its bounded Toeplitz operator, and consider the semicommutator
\[
Q_s=T_{u_s}T_{u_{-s}}-T_{u_su_{-s}}=T_{u_s}T_{u_{-s}}-I.
\]
Put \(\beta=\alpha+1\) and
\[
c_{\alpha,s}=\left|\frac{\Gamma(\beta+is)}{\Gamma(\beta)}\right|^2.
\]
Then \(0<c_{\alpha,s}<1\) and \(Q_s\) is **noncompact**, with essential spectrum equal to the singleton \(\{c_{\alpha,s}-1\}\). There is exactly one scalar \(\gamma\in\mathbb C\) for which \(Q_s+\gamma I\) is compact, namely \(\gamma=1-c_{\alpha,s}\). The centered operator
\[
R_s=Q_s+(1-c_{\alpha,s})I
\]
is positive, nonzero and compact. For its singular values arranged in nonincreasing order with multiplicity,
\[
\boxed{\lim_{j\to\infty}j^{1/d}s_j(R_s)=\frac{c_{\alpha,s}s^2}{(d!)^{1/d}}.}
\]
In particular, for every \(p>0\),
\[
R_s\in\mathcal S_p\quad\Longleftrightarrow\quad p>d,
\]
and the weak endpoint has the exact logarithmic coefficient
\[
\boxed{\lim_{N\to\infty}\frac{1}{\log N}\sum_{j=1}^N s_j(R_s)^d=\frac{(c_{\alpha,s}s^2)^d}{d!}.}
\]
Equivalently, the singular-value counting function obeys
\[
\#\{j:s_j(R_s)>t\}\sim\frac{(c_{\alpha,s}s^2)^d}{d!\,t^d}\quad(t\downarrow0).
\]

## Assumptions and scope

The complex unit ball is \(\mathbb B_d=\{z\in\mathbb C^d:\|z\|<1\}\). Use probability-normalized Lebesgue measure
\[
\mathrm d\mu_\alpha(z)=\frac{\Gamma(d+\alpha+1)}{\pi^d\Gamma(\alpha+1)}(1-\|z\|^2)^\alpha\,\mathrm dV(z),
\]
and \(A^2_\alpha(\mathbb B_d)\) is its holomorphic \(L^2\) subspace. The symbol \(u_s\) is bounded and infinitely differentiable inside the ball but oscillates without a continuous boundary extension when \(s\ne0\). The homogeneous degree-\(n\) subspace \(\mathcal H_n\) has dimension \(m_n=\binom{n+d-1}{d-1}\). The notation \(\mathcal S_p\) includes \(0<p<1\) via the usual summability of singular values.

## Proof

**Exact diagonal reduction.** Rotational symmetry makes \(T_{u_s}\) scalar on each \(\mathcal H_n\). Radial polar integration reduces its eigenvalue to the beta ratio
\[
\lambda_n(s)=\frac{\int_0^1 t^{n+d-1}(1-t)^{\alpha+is}\,\mathrm dt}{\int_0^1 t^{n+d-1}(1-t)^\alpha\,\mathrm dt}=\frac{\Gamma(\beta+is)}{\Gamma(\beta)}\,\frac{\Gamma(n+d+\beta)}{\Gamma(n+d+\beta+is)}.
\]
The adjoint relation \(T_{u_s}^*=T_{u_{-s}}\) implies \(Q_s\vert_{\mathcal H_n}=(|\lambda_n(s)|^2-1)I\). Set \(x_n=n+d+\beta\). The Weierstrass gamma product for positive real \(x\) gives
\[
\frac{\Gamma(x)^2}{|\Gamma(x+is)|^2}=\prod_{k=0}^\infty\left(1+\frac{s^2}{(x+k)^2}\right).
\]
Consequently, with \(c=c_{\alpha,s}\), the eigenvalue of \(R_s\) on \(\mathcal H_n\) is **exactly**
\[
r_n=c\left[\prod_{k=0}^\infty\left(1+\frac{s^2}{(x_n+k)^2}\right)-1\right]>0.
\]
The product strictly decreases when \(x_n\) increases, and tends to one. Hence \(r_n\downarrow0\), proving positivity, compactness and the strict degree-block ordering. Furthermore, \(c\in(0,1)\): if \(X\) is a nondegenerate Gamma random variable of shape \(\beta\), then \(\Gamma(\beta+is)/\Gamma(\beta)=\mathbb E[e^{is\log X}]\), whose modulus is strictly less than one because \(s\ne0\). Thus the eigenvalues of \(Q_s\) approach \(c-1\ne0\). A diagonal operator with these finite-dimensional blocks has essential spectrum exactly this limit point. Adding a scalar yields compactness only if it cancels the limit.

**Sharp first-order defect.** Taking logarithms of the gamma product, using \(\log(1+y)=y+O(y^2)\) for small positive \(y\), and comparing sums with integrals gives, at fixed \(s\),
\[
\log\frac{\Gamma(x)^2}{|\Gamma(x+is)|^2}=s^2\sum_{k\ge0}(x+k)^{-2}+O\!\left(\sum_{k\ge0}(x+k)^{-4}\right)=\frac{s^2}{x}+O(x^{-2}).
\]
Thus \(r_n=c s^2/n+O(n^{-2})\) as \(n\to\infty\).

**Dimension-dependent singular counting.** Every \(r_n\) occurs with multiplicity \(m_n\); these blocks are already in decreasing singular-value order. The cumulative multiplicity through degree \(n\) is
\[
M_n=\sum_{k=0}^n m_k=\binom{n+d}{d}\sim\frac{n^d}{d!}.
\]
For any singular index \(j\) in the degree-\(n\) block, \(j\sim n^d/d!\). Combining with \(r_n\sim c s^2/n\) proves the displayed exact singular coefficient, the sharp \(p>d\) Schatten criterion, and the counting asymptotic. Since \(r_n^d=(c s^2)^d n^{-d}+O(n^{-d-1})\) and \(m_n=n^{d-1}/(d-1)!+O(n^{d-2})\), one has
\[
\sum_{k=0}^n m_k r_k^d=\frac{(c s^2)^d}{(d-1)!}\log n+O(1).
\]
Replacing complete degree blocks by any singular-value cutoff changes the sum by at most \(O(n^{-1})\). As \(\log M_n=d\log n+O(1)\), this proves the exact logarithmic endpoint coefficient.

## Verification

The supplied checker independently evaluates beta/gamma moments, compares exact gamma ratios with truncated Euler products, tests strict positivity and block ordering, and checks the first-order and dimension-scaled singular limits across dimensions one through four. It passed 336 high-precision finite assertions. These tests are corroborative, not a proof of infinite-dimensional or asymptotic statements; the preceding derivation supplies those proofs. Run `python VERIFY_CHECK.py` with Python and `mpmath` installed.

## Relationship to prior work

Tang, Wang and Zheng [1] establish semicommutator trace formulas for smooth symbols on weighted Bergman spaces of disks and balls; their hypotheses require boundary regularity absent for the oscillating unimodular \(u_s\) considered here. Suárez [2] describes radial Toeplitz eigenvalue sequences on the analytic disk; the moment formula underlies the present explicit calculations, but his characterization does not state this scalar-renormalized product's sharp higher-dimensional singular-value law. Bendaoud, Kupin, Toumache, Touré and Zarouf [3] investigate Schatten classes for radial Toeplitz operators, an important possible source of broader coverage; the available abstract does not establish the present exact product/correction/endpoint statement, while comparison with its full paper remains incomplete. The contribution assessed here is the **specific canonical scalar defect and exact weak-Schatten law in all complex dimensions**, not radial diagonalization or general trace formulas.

## Limitations

The proof treats one fixed nonzero logarithmic frequency and one standard power-weighted ball Bergman space at a time. It neither gives estimates uniform as \(s\to0\) nor extends to arbitrary rough radial symbols. The asymptotic is in degree/singular index at fixed finite dimension. Full historical priority remains uncertain because a related radial-Schatten article's full text was not accessible; no independent validation has been performed.

## References

1. X. Tang, Y. Wang and D. Zheng, *Trace Formula of Semicommutators*, arXiv:2210.04148v1 (first public 2022-10-09), https://arxiv.org/html/2210.04148v1 .
2. D. Suárez, *The eigenvalues of limits of radial Toeplitz operators*, arXiv:0710.0797 (2007), https://arxiv.org/abs/0710.0797 .
3. Z. Bendaoud, S. Kupin, K. Toumache, B. Touré and R. Zarouf, *Toeplitz operators with radial symbols on Bergman space and Schatten-von Neumann classes*, Journal of Mathematical Physics, Analysis, Geometry 16 (2020), 3–26, DOI: 10.15407/mag16.01.003 .
