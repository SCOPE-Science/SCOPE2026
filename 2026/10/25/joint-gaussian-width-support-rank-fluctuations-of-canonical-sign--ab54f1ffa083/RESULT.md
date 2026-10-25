# Joint Gaussian width–support-rank fluctuations of canonical signohedra

## Finding
For every integer \(d\ge2\), let \(C_d=[-1,1]^d\), let \(\Diamond_d=\{x\in\mathbb R^d:\|x\|_1\le1\}\), and equip their polar Minkowski sum
\[
\Sigma_d=(C_d+\Diamond_d)^\circ
=\{x\in\mathbb R^d:\|x\|_1+\|x\|_\infty\le1\}
\]
with the standard ambient Euclidean metric. This is the canonical cube–crosspolytope-polar realization of a signohedron. Let \(U_d\) be uniform on the Euclidean unit sphere \(S^{d-1}\). Write \(W_d=w_{\Sigma_d}(U_d)=h_{\Sigma_d}(U_d)+h_{\Sigma_d}(-U_d)\) for its directional width, and let \(K_d\) be the number of nonzero coordinates in the almost surely unique vertex exposed by \(U_d\).

Write \(\phi\) for the standard Gaussian density, \(\overline\Phi\) for its survival function, and define \(t_d>0\) as the unique solution of
\[
2d\bigl[\phi(t_d)-t_d\overline\Phi(t_d)\bigr]=t_d.
\]
Then, as \(d\to\infty\),
\[
\boxed{\left(t_d^2\left(\frac{\sqrt d}{2}W_d-t_d\right),\ \frac{K_d-t_d^2}{t_d}\right)
\ \Longrightarrow\ \mathcal N_2\!\left(\binom{0}{0},
\begin{pmatrix}2&-1\\-1&1\end{pmatrix}\right).}
\]
Moreover,
\[
\boxed{t_d^2=2\log d-3\log\log d-\log(4\pi)+o(1),\qquad
\frac{K_d}{2\log d}\xrightarrow{\mathbb P}1.}
\]
The random width has the matching first-order mean behavior
\[
\mathbb E W_d\sim2\sqrt{\frac{2\log d}{d}}.
\]
The negative off-diagonal covariance records the competition between a larger-than-typical supporting value and the number of coordinates needed to attain it.

## Assumptions and scope
All dimensions \(d\) are integers tending to infinity; the underlying body is the specified **Euclidean** realization \(\Sigma_d\), not an arbitrary affine realization of the same face lattice. Gaussian variables used below are independent standard real Gaussians. The Gaussian limit is weak convergence under the uniform spherical distribution of directions. No assertion about individual unequal-weight monotone-path polytopes is made. For every finite \(d\ge2\), ties in the exposed vertex occur only on a spherical measure-zero set, which fixes the definition of \(K_d\).

## Proof
**1. Exact vertex support and an empirical threshold.** For a real vector \(g\), let \(y_1\ge\cdots\ge y_d\ge0\) be the decreasing rearrangement of \((|g_1|,\ldots,|g_d|)\), and put \(S_k=\sum_{i=1}^k y_i\). In an orthant, rearrangement allows the maximizer of \(g\cdot x\) to have nonnegative, decreasing coordinate magnitudes. Write these magnitudes as \(x_i=\sum_{k=i}^d a_k\), with \(a_k\ge0\). The constraint \(\|x\|_1+\|x\|_\infty\le1\) becomes \(\sum_{k=1}^d(k+1)a_k\le1\), while the objective becomes \(\sum_{k=1}^d S_ka_k\). Hence
\[
 h_{\Sigma_d}(g)=\max_{1\le k\le d}\frac{S_k}{k+1}.
\]
The maximizing vertex has exactly \(k\) nonzero entries, each of magnitude \(1/(k+1)\), with the signs of the corresponding entries of \(g\). These vertices agree with the known signed-support vertex description of the canonical signohedron, and are not claimed as a new face enumeration.

Define, for \(z\ge0\),
\[
F_d(z)=\sum_{i=1}^d(|g_i|-z)_+-z,
\qquad N_d(z)=\sum_{i=1}^d\mathbf1_{\{|g_i|>z\}}.
\]
For nonzero \(g\), the function \(F_d\) decreases strictly from a positive number to a negative number and has one positive zero \(H_d\). Since \(\max_k\{S_k-(k+1)z\}=F_d(z)\) whenever \(F_d(z)\ge0\), the zero is precisely \(H_d=h_{\Sigma_d}(g)\). For a Gaussian vector, almost surely no coordinate magnitude equals \(H_d\), and the exposed rank is exactly \(K_d=N_d(H_d)\).

**2. Deterministic Gaussian threshold.** Let \(Y=|Z|\) for \(Z\sim N(0,1)\). Direct integration gives
\[
 m_1(t):=\mathbb E(Y-t)_+=2[\phi(t)-t\overline\Phi(t)],
\quad m_2(t):=\mathbb E(Y-t)_+^2
 =2[(1+t^2)\overline\Phi(t)-t\phi(t)].
\]
The strictly decreasing function \(d m_1(t)-t\) has one zero \(t_d\). Gaussian Mills expansions give
\[
 m_1(t)=\frac{2\phi(t)}{t^2}\left(1-\frac3{t^2}+O(t^{-4})\right),
\quad m_2(t)=\frac{4\phi(t)}{t^3}(1+O(t^{-2})),
\quad 2\overline\Phi(t)=\frac{2\phi(t)}t(1+O(t^{-2})).
\]
It follows that \(t_d\to\infty\), \(2d\phi(t_d)/t_d^3\to1\), and
\[
 t_d^2=2\log d-3\log\log d-\log(4\pi)+o(1).
\]
For brevity write \(t=t_d\), and set \(p=2\overline\Phi(t)\). The threshold equation implies
\[
 dp=t^2+O(1),\qquad d m_2(t)\longrightarrow2,
\qquad \frac{2d\phi(t)}{t^3}\longrightarrow1.
\]
In fact the first two quantities obey the finite identity \(d m_2(t)=dp-t^2\), from which \(dp-t^2\to2\).

**3. The joint triangular-array central limit theorem.** For independent \(Y_i=|G_i|\), define
\[
 B_d=F_d(t)=\sum_i(Y_i-t)_+-t,
\qquad A_d=\frac{N_d(t)-dp}{t}.
\]
These are centered sums of independent triangular-array terms. Their covariance tends to
\[
 \operatorname{Var}(B_d)\to2,
\quad \operatorname{Var}(A_d)\to1,
\quad \operatorname{Cov}(B_d,A_d)
 =\frac{d(1-p)m_1(t)}{t}=1-p\to1.
\]
The array satisfies the multivariate Lindeberg condition. Indeed \(d\mathbb E(Y-t)_+^3=O(t^{-1})\) by the same Gaussian-tail expansion, and \(dp/t^3=O(t^{-1})\); these estimates bound the third absolute moments of every fixed linear combination of the centered summands after the indicated scaling. Thus
\[
 (B_d,A_d)\Longrightarrow\mathcal N_2\left(0,
\begin{pmatrix}2&1\\1&1\end{pmatrix}\right).
\]

**4. Root displacement and exposed-rank response.** The identity
\[
 F_d(z)-F_d(t)=-\int_t^z (N_d(v)+1)\,dv
\]
holds for all \(z\ge0\), with the integral understood with its natural sign. Since \(N_d(t)\) is binomial with \(dp/t^2\to1\), one has \(N_d(t)/t^2\to1\) in probability. For each fixed \(M\), the expected number of observations in \([t-M/t^2,t+M/t^2]\) is \(O(Mt)\), hence their number is \(O_{\mathbb P}(t)=o_{\mathbb P}(t^2)\). Therefore, uniformly on this window, \(N_d(v)/t^2\to1\) in probability. Tightness of \(B_d\), monotonicity of \(F_d\), and this integral identity show that its zero satisfies
\[
 t^2(H_d-t)=B_d+o_{\mathbb P}(1).
\]
For a fixed real \(u\), the signed count \(N_d(t+u/t^2)-N_d(t)\) has mean \(-ut+o(t)\) and variance \(O(t)\), since the absolute-normal density is \(2\phi\) and \(2d\phi(t)/t^3\to1\). Monotonicity and a finite grid upgrade this pointwise estimate to uniformity on every bounded interval of \(u\). Substituting the tight random displacement \(u=t^2(H_d-t)\) gives
\[
 \frac{K_d-t^2}{t}=A_d-B_d+o_{\mathbb P}(1).
\]
Consequently, the limiting covariance matrix of \((t^2(H_d-t),(K_d-t^2)/t)\) is
\[
 \begin{pmatrix}2&1-2\\1-2&1+2-2\end{pmatrix}
 =\begin{pmatrix}2&-1\\-1&1\end{pmatrix}.
\]
In particular \(K_d/t^2\to1\) in probability.

**5. Conversion to uniformly random spherical directions.** Let \(G=(G_1,\ldots,G_d)\), \(R=\|G\|_2\), and \(U=G/R\). Then \(U\) is uniform spherical, \(R=\sqrt d+O_{\mathbb P}(1)\), and the signohedron is centrally symmetric, so
\[
 \frac{\sqrt d}{2}W_d(U)=\frac{\sqrt d}{R}H_d.
\]
As \(H_d=O_{\mathbb P}(\sqrt{\log d})\), multiplication by \(t^2\) makes the radial-normalization error \(O_{\mathbb P}((\log d)^{3/2}/\sqrt d)=o_{\mathbb P}(1)\). Exposed ranks are unaffected by positive rescaling of a direction. This proves the stated spherical joint limit.

Finally \(\mathbb E W_d=2\mathbb E H_d/\mathbb ER\) by Gaussian polar decomposition. Since \(H_d/t\to1\) in probability and \(H_d\le\max_i|G_i|\), the standard Gaussian maximum second-moment bound \(\mathbb E\max_i|G_i|^2=O(\log d)\) ensures uniform integrability of \(H_d/t\). Also \(\mathbb ER\sim\sqrt d\); hence \(\mathbb E W_d\sim2\sqrt{2\log d/d}\). This completes the proof.

## Verification
The accompanying `verify.py` reconstructs the support optimization by an independent linear program in dimensions \(2\) through \(8\), compares its optimum to the exact sorted-partial-sum formula, checks the fixed-point equation and exposed ranks, evaluates Gaussian excess moments by independent quadrature, and tests finite-dimensional moment identities. It also reports seeded finite-sample diagnostics of the proposed joint normal limit. Run `python verify.py` with NumPy and SciPy. Finite simulations do not establish convergence, and the slowly converging Gaussian-tail corrections are visible at practical dimensions.

## Relationship to prior work
Black and De Loera (2021, first public arXiv version 2021-02-02, primary MSC2020 52B05) proved the combinatorial realization of signohedra by cube–crosspolytope polars and exhibited their signed-support vertex description. The exact support representation here follows readily from their realization and standard rearrangement. Its role is an input, **not** the claimed discovery. The asserted contribution is the explicit logarithmic support-rank concentration and the *joint* second-scale Gaussian limit for intrinsic Euclidean directional width and exposed-vertex rank, including its negative covariance. Standard Gaussian Mills ratios and triangular-array central limit theory supply familiar probabilistic tools. These ingredients alone do not state the resulting signohedron-specific joint metric law. Similar threshold fluctuations may be expressible through known empirical-process or norm-duality frameworks; this is a residual bibliographic risk, not a claim of proved global uniqueness.

## Limitations
The result concerns one canonical signed-symmetric Euclidean realization, not every polytope combinatorially equivalent to a signohedron. It is a weak limit as \(d\to\infty\), not a finite-dimensional normal identity or an explicit Berry–Esseen bound. The first-order mean-width equivalent is established; no finer expansion of its expectation is claimed. No independent mathematical audit or full bibliographic certification has been performed.

## References
1. A. E. Black and J. A. De Loera, *Monotone Paths on Cross-Polytopes*, arXiv:2102.01237, first submitted 2021-02-02. See especially Theorem 1.1(d) and Section 3 for the canonical polar realization and signed-support vertices. https://arxiv.org/abs/2102.01237
2. Standard facts on Gaussian tails (Mills-ratio expansion), triangular-array central limit theorems, and Gaussian radial/angular independence are used in their classical forms; proofs of the required special-case estimates are provided above.
