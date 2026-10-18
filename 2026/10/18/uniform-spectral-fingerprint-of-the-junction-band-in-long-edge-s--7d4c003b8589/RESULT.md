# Uniform spectral fingerprint of the junction band in long edge-subdivided regular networks

## Finding

Let \(G\) be any finite connected simple \(d\)-regular graph, with \(d\geq3\), adjacency eigenvalues \(d=\mu_1\geq\cdots\geq\mu_n\). Replace every edge of \(G\) by a path of exactly \(\ell\) edges, and denote the resulting graph by \(G^{(\ell)}\). Consider its unit-hopping adjacency Hamiltonian \(A_{G^{(\ell)}}\). Define
\[
\rho=\sqrt{d-1},\qquad \lambda_0=\frac d\rho,
\qquad c_d=\frac{(d-2)^2}{2(d-1)^{3/2}}.
\]
There exists \(\ell_0(d)\) such that for every integer \(\ell\geq\ell_0(d)\) the adjacency matrix of \(G^{(\ell)}\) has exactly \(n\) eigenvalues above \(2\), counted with multiplicity. There is a one-to-one order-preserving map from the entire parent adjacency spectrum to these eigenvalues, \(\mu\mapsto\Lambda_\ell(\mu)\), characterized exactly by
\[
\Lambda_\ell(\mu) U_{\ell-1}(\Lambda_\ell(\mu)/2)
 -d U_{\ell-2}(\Lambda_\ell(\mu)/2)=\mu,
\qquad \Lambda_\ell(\mu)>2,
\]
where \(U_k\) is the degree-\(k\) Chebyshev polynomial of the second kind, normalized by \(U_0(z)=1\) and \(U_1(z)=2z\). Uniformly for \(\mu\in[-d,d]\),
\[
\boxed{\ \Lambda_\ell(\mu)=\frac d{\sqrt{d-1}}+
 \frac{(d-2)^2}{2(d-1)^{3/2}}\,
 \mu\,(d-1)^{-\ell/2}
 +O_d\!\left(\ell(d-1)^{-\ell}\right).\ }
\]
The error constant and cutoff depend on \(d\) only, **not** on the size or shape of \(G\). Consequently, writing \(W_\ell\) for the spectral width of precisely this above-\(2\) band,
\[
\lim_{\ell\to\infty}(d-1)^{\ell/2}W_\ell
=c_d\bigl(d-\mu_n\bigr).
\]
The maximal degree-controlled limiting width \(2dc_d\) occurs exactly when the connected parent graph is bipartite. Every other parent adjacency eigenvalue is likewise recovered by rescaling the narrow junction-band levels. These statements concern all eigenvalues above \(2\); they are not an assertion that all eigenvalues of the enlarged graph are near \(\lambda_0\).

## Assumptions and scope

The parent \(G\) is finite, undirected, simple, connected and regular of integer degree \(d\geq3\). Edge inflation is uniform: each original edge is replaced by \(\ell\) unit-weight edges with \(\ell-1\) new degree-two vertices; \(\ell\geq2\). The underlying one-particle Hamiltonian has zero diagonal potential and hopping amplitude \(1\), so is the adjacency matrix. For the alternative physics sign convention \(H=-t A\), with \(t>0\), the identified positive-adjacency band corresponds to the negative-energy band, and its width is multiplied by \(t\). The high-energy threshold \(2\) is the top of the infinite unit-hopping chain spectrum. Uniform error notation \(O_d\) means an absolute bound with constants depending only on \(d\), valid for every parent graph and every \(\mu\in[-d,d]\).

## Proof

**1. Exact Schur reduction to the parent adjacency spectrum.** Fix \(\lambda>2\). On the inflated path connecting junction vertices \(v\) and \(w\), write the endpoint amplitudes \(x_v,x_w\), and let the intermediate amplitudes satisfy the recurrence
\[
\lambda\psi_j=\psi_{j-1}+\psi_{j+1},\qquad
\psi_0=x_v,\quad \psi_\ell=x_w.
\]
Since the path Dirichlet eigenvalues \(2\cos(k\pi/\ell)\) lie strictly in \((-2,2)\), the recurrence has a unique solution for \(\lambda>2\). In particular,
\[
\psi_1=
\frac{U_{\ell-2}(\lambda/2)x_v+x_w}
{U_{\ell-1}(\lambda/2)}.
\]
Summing these amplitudes over the \(d\) incident edges at each junction yields
\[
\left[\lambda U_{\ell-1}(\lambda/2)-dU_{\ell-2}(\lambda/2)\right]x_v
=\sum_{w\sim v}x_w.
\]
Thus \(\lambda>2\) is an eigenvalue of the inflated graph precisely when the bracketed scalar is some parent adjacency eigenvalue \(\mu\), with the same geometric multiplicity; extension of each junction eigenvector along the paths is unique. A purported inflated eigenvector vanishing at every junction would solve a homogeneous Dirichlet problem on each internal path and therefore be zero. As the matrices are symmetric, geometric and algebraic multiplicities agree.

**2. The near-junction root and its uniform expansion.** Introduce the spectral parameter
\[
 u=\frac{\lambda+\sqrt{\lambda^2-4}}2>1,
\qquad \lambda=u+u^{-1},
\qquad \rho=\sqrt{d-1}>1.
\]
Using \(U_{\ell-1}(\lambda/2)=(u^\ell-u^{-\ell})/(u-u^{-1})\), the secular equation is exactly equivalent, for \(u>1\), to
\[
 F_{\ell,\mu}(u):=
 u^2-(d-1)
 +\bigl((d-1)u^2-1\bigr)u^{-2\ell}
 -\mu(u^2-1)u^{-\ell}=0.\tag{1}
\]
Here \(\mu\in[-d,d]\), a uniform interval independent of the graph size. On a fixed small neighborhood of \(\rho\), the last two terms of (1) are \(O_d(\rho^{-\ell})\) in the shrinking interval \(|u-\rho|\le C_d\rho^{-\ell}\), and their \(u\)-derivatives are \(O_d(\ell\rho^{-\ell})\). These estimates are uniform in \(\mu\). For sufficiently large \(\ell\), choose a fixed \(C_d>0\) exceeding the leading perturbation coefficient, and note that (1) takes opposite signs at the two endpoints \(\rho\pm C_d\rho^{-\ell}\), because the leading term \(u^2-\rho^2\) has endpoint magnitude \(2\rho C_d\rho^{-\ell}\). Moreover,
\[
\partial_u F_{\ell,\mu}(u)=2\rho+O_d(\ell\rho^{-\ell})>0
\]
throughout this interval. Hence (1) has a unique root \(u_{\ell,\mu}\) there. A first-order Taylor expansion of (1), with \(\delta=u_{\ell,\mu}-\rho\), gives, uniformly for \(\mu\in[-d,d]\),
\[
2\rho\delta=\mu(d-2)\rho^{-\ell}
+O_d(\ell\rho^{-2\ell}),
\quad\text{so}\quad
\delta=\frac{\mu(d-2)}{2\rho}\rho^{-\ell}
+O_d(\ell\rho^{-2\ell}).
\]
(The nonzero term of size \(\rho^{-2\ell}\) in (1) is absorbed in that error.) Since \(d(u+u^{-1})/du|_{u=\rho}=1-\rho^{-2}=(d-2)/(d-1)\), the stated expansion for \(\Lambda_\ell(\mu)\) follows. This constructs a root \(\lambda>2\) for every parent eigenvalue with constants uniform in all parent graphs.

**3. No missing positive-junction eigenvalues.** Delete the \(n\) original junction vertices from \(G^{(\ell)}\). The remaining induced graph is the disjoint union of \(|E(G)|\) paths on \(\ell-1\) vertices, whose largest adjacency eigenvalue equals \(2\cos(\pi/\ell)<2\). By the Cauchy interlacing theorem, the enlarged adjacency matrix has at most \(n\) eigenvalues strictly above \(2\). Step 2 constructs \(n\) of them, counting parent eigenspace dimensions, so there are exactly \(n\) and no further roots above \(2\). The argument also covers repeated parent eigenvalues.

**4. Ordering and the width.** In the root neighborhood, \(\partial_u F_{\ell,\mu}>0\), while
\[
\partial_\mu F_{\ell,\mu}=-(u^2-1)u^{-\ell}<0.
\]
The implicit derivative \(du_{\ell,\mu}/d\mu\) is strictly positive. Since \(u+u^{-1}\) is strictly increasing on \(u>1\), the spectral map is order-preserving. Its extremal arguments are \(d\) and \(\mu_n\); subtracting the two uniform expansions proves the width formula. For a connected regular graph, \(\mu_n\ge-d\), with equality if and only if the graph is bipartite, which proves the final characterization.

## Verification

The self-contained numerical replay is `verify.py` (Python 3 with NumPy and SciPy; see `requirements.txt`). It builds each edge-inflated adjacency matrix directly and compares **all** eigenvalues above \(2\) against independently root-solved exact secular equations, checks the Chebyshev identity, and compares the first-order expansion and band widths on six graph families (including both bipartite and nonbipartite parents) at path lengths \(8,12,16\). The replay returns `VERIFY_OK: 294 numerical assertions in six graph families`. These tests are finite diagnostics, **not** evidence of the uniform infinite-length theorem; the proof is in the four steps above.

## Relationship to prior work

Berkovits, *Localization and Flat Bands in Bond-Inflated Lattices* (arXiv:2604.12759; the abstract also uses the title *Edge-Inflated Lattices*), studies bond inflation and identifies the junction energy \(d/\sqrt{d-1}\), exponential localization, and qualitatively exponentially small junction-band broadening. Those facts are prior work. In particular, the order-of-magnitude width suppression is **not** claimed new here.

Kumar, Mohar, Pragada, and Zhan, *Subdivision and Graph Eigenvalues* (arXiv:2303.10488), study arbitrary graph subdivision and prove convergence of leading eigenvalues to limits determined by junction degrees, as well as bounds on the number outside \([-2,2]\). Those limiting and counting facts are also prior work.

The claim assessed here is narrower and quantitative: a graph-size-uniform first-order spectral transformation of **every** junction-band eigenvalue, with its exact coefficient and error, identifying the whole parent adjacency spectrum after rescaling, and a sharp asymptotic width/bipartiteness criterion. A known exact subdivision polynomial or a more general spectral perturbation theorem could imply this specialization; the absence of such coverage has not been independently certified.

## Limitations

This is a theorem for uniform edge inflation on finite connected simple regular graphs of fixed degree \(d\ge3\) and uniform real hopping. It does not cover irregular parents, variable inflation lengths, diagonal potentials, magnetic phases, interactions, or disorder. The cutoff is only asserted to depend on \(d\); an optimized explicit minimal cutoff is not proved. Results for periodic infinite-volume Bloch bands are not asserted. The asymptotic error is uniform over finite parent size but not over degree tending to infinity. The evidence for originality is a comparison with accessible primary literature and scientific-index results, not independent exhaustive certification.

## References

1. R. Berkovits, *Localization and Flat Bands in Bond-Inflated Lattices*, arXiv:2604.12759v1 (first publicly posted 2026-04-14); full HTML presentation: https://arxiv.org/html/2604.12759.
2. H. Kumar, B. Mohar, S. Pragada, and H. Zhan, *Subdivision and Graph Eigenvalues*, arXiv:2303.10488v1 (first posted 2023-03-18), https://arxiv.org/abs/2303.10488.
