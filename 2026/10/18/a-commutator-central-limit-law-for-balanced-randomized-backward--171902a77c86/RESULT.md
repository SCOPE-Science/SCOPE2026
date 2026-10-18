# A commutator central limit law for balanced randomized backward-Euler splitting

## Finding

Let \(H_1,H_2\) be real symmetric positive-semidefinite matrices of a fixed finite dimension \(d\geq 1\), let \(T>0\), and let \(u_0\in\mathbb R^d\) be deterministic. Write
\[
 A=\frac{H_1+H_2}{2},\quad Q=H_1^2+H_2^2,\quad J=[H_1,H_2]=H_1H_2-H_2H_1,\quad u(t)=e^{-tA}u_0.
\]
For \(N\geq1\), put \(h=T/(2N)\) and \(R_i(h)=(I+hH_i)^{-1}\). Starting at \(X_0=u_0\), independently and with equal probabilities choose at each of the \(N\) blocks either \(X_k=R_2(h)R_1(h)X_{k-1}\) or \(X_k=R_1(h)R_2(h)X_{k-1}\). Every block uses *both* component resolvents, exactly once; only their order is randomized.

Then as \(N\to\infty\):
\[
\frac{\mathbb E X_N-u(T)}h\longrightarrow
 V_T:=\frac14\int_0^T e^{-(T-s)A}Q u(s)\,ds,
\]
\[
h^{-3/2}(X_N-\mathbb E X_N)\ \Longrightarrow\ \mathcal N(0,K_T),
\qquad
h^{-3}\operatorname{Cov}(X_N)\longrightarrow K_T,
\]
with entrywise (equivalently, operator-norm) covariance convergence and
\[
K_T=\frac18\int_0^T e^{-(T-s)A}J u(s)u(s)^\top J^\top e^{-(T-s)A}\,ds.
\]
In particular \(\mathbb E\|X_N-u(T)\|^2=h^2\|V_T\|^2+o(h^2)\). In dimension \(d=2\), noncommutativity \(J\ne0\) and nonzero \(u_0\) imply \(\operatorname{tr}K_T>0\): the random-error exponent \(3/2\) is sharp. Conversely \(J=0\) makes the entire balanced trajectory deterministic for every \(N\) and \(h\).

For an equal-cost comparison, take \(2N\) *independent-with-replacement* uniform draws from \(\{H_1,H_2\}\), perform one backward-Euler resolvent at each step of length \(h=T/(2N)\), and call its terminal iterate \(Y_{2N}\). Its leading stochastic behavior is instead
\[
h^{-1/2}(Y_{2N}-\mathbb E Y_{2N})\ \Longrightarrow\ \mathcal N(0,K_T^{\mathrm{iid}}),\quad
h^{-1}\operatorname{Cov}(Y_{2N})\longrightarrow K_T^{\mathrm{iid}},
\]
where
\[
K_T^{\mathrm{iid}}=\frac14\int_0^T e^{-(T-s)A}(H_1-H_2)u(s)u(s)^\top(H_1-H_2)e^{-(T-s)A}\,ds.
\]
Thus using each component once per pair removes the leading \(h^{1/2}\)-scale sampling fluctuations at *the same number of resolvent solves*. The remaining fluctuations measure noncommutativity, not component imbalance. The total error against the exact evolution still has an order-\(h\) deterministic bias.

## Assumptions and scope

All matrices, the initial vector, and \(T\) are fixed as \(h\downarrow0\); the dimension does not grow. The coefficient operators are symmetric and positive semidefinite, so each backward-Euler resolvent is a well-defined Euclidean contraction at every positive step. Each block order is an independent fair coin flip; the two selections *within* a block are perfectly negatively dependent. Results concern the linear gradient flow \(u'(t)=-Au(t)\) without additive forcing. The covariances refer to randomness in update orders, not spatial truncation or stochastic oracle errors.

## Proof

**1. Exact paired expansion.** Define \(B_+(h)=R_2(h)R_1(h)\), \(B_-(h)=R_1(h)R_2(h)\), \(M_h=(B_++B_-)/2\), and \(D_h=(B_--B_+)/2\). Resolvent Taylor expansions, valid uniformly for sufficiently small positive \(h\), give
\[
M_h=I-2hA+h^2\left(Q+\frac{H_1H_2+H_2H_1}{2}\right)+O(h^3),
\qquad D_h=\frac{h^2}{2}J+O(h^3).
\]
Since \(e^{-2hA}=I-2hA+2h^2A^2+O(h^3)\) and \(2A^2=(H_1^2+H_2^2+H_1H_2+H_2H_1)/2\),
\[
M_h-e^{-2hA}=\frac{h^2}{2}Q+O(h^3).
\]
All \(O(\cdot)\) constants depend only on the fixed matrices and, where relevant, \(T\) and \(u_0\).

**2. Mean error.** Independence makes \(\mathbb E X_N=M_h^Nu_0\). Telescoping its difference from the exact macro-step semigroup gives
\[
M_h^N-e^{-TA}=\sum_{k=1}^N M_h^{N-k}(M_h-e^{-2hA})e^{-2h(k-1)A}.
\]
Both \(M_h\) and the semigroup are contractions. The single-step expansion shows, uniformly in \(0\leq k\leq N\), that \(\|M_h^k-e^{-2khA}\|=O(h)\). Dividing the above telescoping identity by \(h\), substituting the expansion and applying the matrix-valued Riemann-sum limit at spacing \(2h\), yields \(V_T\) with coefficient \(1/4\).

**3. Pathwise control and martingale decomposition.** Write \(B_{\varepsilon_k}=M_h+\varepsilon_kD_h\), where \(\varepsilon_k\) are independent Rademacher signs (with the sign attached to \(B_-\)). Each \(B_{\varepsilon_k}\) is a contraction and \(\|B_{\varepsilon_k}-e^{-2hA}\|=O(h^2)\); elementary telescoping therefore gives the *deterministic* bound
\[
\max_{0\leq k\leq N}\|X_k-u(2kh)\|\leq C h.
\]
Subtracting the mean and iterating the exact recursion gives an orthogonal-martingale-sum representation
\[
X_N-\mathbb E X_N=\sum_{k=1}^N M_h^{N-k}\varepsilon_kD_hX_{k-1}.
\]
The \(k\)-th summand is a martingale difference with respect to its natural filtration, as its matrix coefficient is deterministic and \(X_{k-1}\) is measurable with respect to earlier signs.

**4. Gaussian limit and covariance.** Replace \(X_{k-1}\) in that sum by \(u(2h(k-1))\), \(D_h\) by \(h^2J/2\), and \(M_h^{N-k}\) by \(e^{-2h(N-k)A}\). The uniform \(O(h)\) replacements and orthogonality of distinct martingale increments give an \(L^2\) total remainder \(O(h^{5/2})\), which is negligible after normalization by \(h^{3/2}\). The resulting leading array consists of independent centered vectors, each of norm \(O(h^2)\), so normalized individual increments are \(O(h^{1/2})\); the Lindeberg condition holds. Its covariance after division by \(h^3\) is
\[
\frac{h}{4}\sum_{k=1}^N e^{-2h(N-k)A}J u(2h(k-1))u(2h(k-1))^\top J^\top e^{-2h(N-k)A}.
\]
The mesh is \(2h\), giving exactly the coefficient \(1/8\) in \(K_T\). The multivariate Lindeberg–Feller theorem (or Cramér–Wold plus the scalar theorem) proves the distributional conclusion. The \(L^2\) remainder also proves covariance convergence. Together with the mean expansion this implies the stated mean-square expansion.

**5. Independent-with-replacement comparison.** For single-step operators \(R_1,R_2\), the centered half-difference is \((R_1-R_2)/2=-h(H_1-H_2)/2+O(h^2)\); their mean is \(I-hA+O(h^2)\). Its deterministic mean trajectory differs from \(u(kh)\) by \(O(h)\). The same telescoping-martingale representation together with contraction and orthogonality yields \(\sup_{k\leq 2N}\mathbb E\|Y_k-u(kh)\|^2=O(h)\). Replacing random past states by the exact trajectory makes an \(o(h^{1/2})\) contribution in \(L^2\). The independent leading increments are of order \(h\) with covariance Riemann sum \((h/4)\int_0^T\cdots\,ds\), giving \(K_T^{\mathrm{iid}}\) and the corresponding CLT by the same Lindeberg argument.

**6. Sharpness and commutation.** For any nonzero skew-symmetric \(2\times2\) matrix \(J\), \(J\) is invertible. At all \(s\in[0,T]\), the vectors \(e^{-(T-s)A}J e^{-sA}u_0\) are nonzero when \(u_0\ne0\); their squared norms integrate to \(8\operatorname{tr}K_T>0\). If \(J=0\), symmetric matrices \(H_1,H_2\) and their resolvents commute, hence \(B_+=B_-\) exactly and no randomness remains. This proves both statements.

## Verification

The included `paired_split_verify.py` uses exact SymPy rational arithmetic to test the order-two resolvent expansions, the commutator sign, and the covariance recursion against complete enumeration of every order sequence through five blocks. It also tests that commuting resolvents eliminate order randomness. Independent numerical quadrature and deterministic covariance recursions check the limiting constants; these numerical checks corroborate but do not substitute for the proof.

For the strictly positive-definite example
\[
H_1=\begin{pmatrix}2&0\\0&1\end{pmatrix},\quad H_2=\begin{pmatrix}2&1\\1&2\end{pmatrix},\quad u_0=\begin{pmatrix}1\\2\end{pmatrix},\quad T=1,
\]
we have \(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), and quadrature gives \(\operatorname{tr}K_T\approx0.02305850\) versus \(\operatorname{tr}K_T^{\mathrm{iid}}\approx0.06185139\). At \(N=800\), the computed trace ratios \(\operatorname{tr}\operatorname{Cov}(X_N)/(h^3\operatorname{tr}K_T)\approx0.997515\) and \(\operatorname{tr}\operatorname{Cov}(Y_{2N})/(h\operatorname{tr}K_T^{\mathrm{iid}})\) approach one. No finite experiment is used to establish the limiting theorem.

## Relationship to prior work

Eisenmann and Stillfjord [1] introduce randomized implicit operator splitting with independently sampled operators and establish general expected-error bounds, principally of temporal order one half; some smoother settings achieve order one. Their scheme and Theorem 5.2 do not describe pairwise without-replacement ordering or its exact centered commutator covariance and Gaussian limit. Childs, Ostrander, and Su [2] study randomized order in products of unitary exponentials, demonstrating improvement through permutation mixing, but not resolvent-flow fluctuations or the present covariance formula. Chen, Huang, Kueng, and Tropp [3] establish concentration for random unitary product formulas, not this finite-dimensional dissipative implicit scheme's Gaussian limit or equal-cost comparison. Veldman and Zuazua [4] analyze independently selected matrix subsets in continuous-time random splitting for linear-quadratic control and quantify mean errors, but do not use a pairwise randomized implicit-resolvent order or establish the present commutator central-limit covariance. The result is an explicit second-order-ordering-noise classification within a restricted linear model, not a claim that randomization or commutator limits are new in general.

## Limitations

This theorem assumes a *fixed finite dimension*, symmetric positive semidefinite components, two components, independent fair order selection across pairs, and no forcing or approximation errors in the resolvent solves. It makes no general statement for nonlinear maximal-monotone operators, inhomogeneous evolution, non-self-adjoint matrices, nonuniform clocks, or growing dimension. The error \(\|X_N-u(T)\|\) is typically first order because of deterministic discretization bias; only the *centered stochastic* fluctuations are of order \(h^{3/2}\). Zero covariance is possible beyond trivial vector examples, and no full classification of those higher-dimensional cancellations is asserted. The literature comparison cannot exclude uncatalogued equivalent derivations.

## References

[1] M. Eisenmann and T. Stillfjord, *A randomized operator splitting scheme inspired by stochastic optimization methods*, arXiv:2210.05375 (first public version 2022-10-11), https://arxiv.org/abs/2210.05375. Primary MSC 65M12.

[2] A. M. Childs, A. Ostrander, and Y. Su, *Faster quantum simulation by randomization*, arXiv:1805.08385 (2018), https://arxiv.org/abs/1805.08385.

[3] C.-F. Chen, H.-Y. Huang, R. Kueng, and J. A. Tropp, *Concentration for random product formulas*, arXiv:2008.11751 (2020), https://arxiv.org/abs/2008.11751.

[4] D. W. M. Veldman and E. Zuazua, *A framework for randomized time-splitting in linear-quadratic optimal control*, arXiv:2109.13798 (2021), https://arxiv.org/abs/2109.13798.
