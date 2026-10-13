# Degree-norm calibration law and lattice crossover for common-mode graph-state phase noise
## Finding
Let \(G=(V,E)\) be a finite, simple, undirected graph with \(|V|=n\). The ideal \(n\)-qubit graph state is
\[
|G\rangle=\prod_{\{u,v\}\in E}\mathrm{CZ}_{uv}|+\rangle^{\otimes n}.
\]
The preparation model here replaces every edge gate in a single preparation by a controlled-phase gate
\[
\operatorname{diag}(1,1,1,-e^{i\varepsilon}),
\]
where **the same** random \(\varepsilon\) is shared by all edges in that preparation. Between independently repeated preparations, \(\varepsilon\) is redrawn from the centered Gaussian distribution with variance \(\sigma^2\). In particular, this is neither an independent edge-error model nor an independent single-qubit Pauli channel.

The quantity studied is ensemble-averaged fidelity to the **unmeasured full graph state**:
\[
F_G(\sigma)=\mathbb E_{\varepsilon}|\langle G|G_\varepsilon\rangle|^2.
\]
For a uniformly random vertex bit string \(X\in\{0,1\}^V\), let
\[
H_G(X)=\sum_{\{u,v\}\in E}X_uX_v,
\]
and let \(Y\) be an independent copy. Then the following finite identity is exact for every \(G\) and \(\sigma\ge0\):
\[
\boxed{F_G(\sigma)=\mathbb E_{X,Y}\exp\left[-\frac{\sigma^2}{2}(H_G(X)-H_G(Y))^2\right].}
\]
Write
\[
m_G=|E|,\qquad S_G=\sum_{v\in V}\deg_G(v)^2.
\]
The exact pairwise energy-difference variance is
\[
\boxed{\operatorname{Var}(H_G(X)-H_G(Y))=\frac{S_G+m_G}{8}.}
\]

**Degree-norm calibration theorem.** Let \(G_n\) be any sequence of finite simple graphs (the index need not equal the vertex count) with
\[
S_{G_n}\longrightarrow\infty,\qquad
\frac{m_{G_n}}{S_{G_n}}\longrightarrow0,\qquad
\frac{\max_v\deg_{G_n}(v)}{\sqrt{S_{G_n}}}\longrightarrow0.
\]
Then for every fixed \(c\ge0\),
\[
\boxed{F_{G_n}\left(\frac{c}{\sqrt{S_{G_n}}}\right)\longrightarrow\frac1{\sqrt{1+c^2/8}}.}
\]
Thus under these conditions the relevant common-phase calibration precision is controlled by the root sum of squared vertex degrees, rather than by just the edge count. For complete graphs \(K_n\), this gives the critical scale \(\sigma\asymp n^{-3/2}\).

**Exact lattice crossover for complete graphs.** Let \(K,L\) be independent \(\operatorname{Bin}(n,1/2)\) random variables. Then
\[
F_{K_n}(\sigma)
=4^{-n}\sum_{k,l=0}^n\binom nk\binom nl
\exp\left[-\frac{\sigma^2}{2}\left(\binom k2-\binom l2\right)^2\right].
\]
Put
\[
\Theta(t)=\sum_{r\in\mathbb Z}\exp(-t^2r^2/8),\qquad t>0.
\]
For fixed \(c\ge0\),
\[
\boxed{F_{K_n}(c/n^{3/2})\to(1+c^2/8)^{-1/2}.}
\]
In the complementary regime \(\sigma_n\ge0\) with \(n^{3/2}\sigma_n\to\infty\),
\[
\boxed{F_{K_n}(\sigma_n)\sim\frac{\Theta(n\sigma_n)}{\sqrt{\pi n}}.}
\]
This one formula resolves three subregimes:
\[
\begin{aligned}
n\sigma_n&\to0 &&\Longrightarrow&&F_{K_n}(\sigma_n)\sim\frac{\sqrt8}{\sigma_n n^{3/2}},\\
n\sigma_n&\to c\in(0,\infty)&&\Longrightarrow&&\sqrt{\pi n}F_{K_n}(\sigma_n)\to\Theta(c),\\
n\sigma_n&\to\infty&&\Longrightarrow&&\sqrt{\pi n}F_{K_n}(\sigma_n)\to1.
\end{aligned}
\]
The last statement includes every fixed \(\sigma>0\). The nonzero plateau at each finite \(n\) reflects coincidences of the discrete quadratic phases, not a continuous approximation artifact.

**Dominant-hub exception and preparation-graph contrast.** Let \(T_n=K_{1,n-1}\) be the \(n\)-vertex star. For fixed \(c\ge0\),
\[
\boxed{F_{T_n}(c/n)\to\frac{1+e^{-c^2/8}}2.}
\]
The star does not satisfy the no-dominant-degree hypothesis; its calibration response at \(\sigma\asymp n^{-1}\) is genuinely non-Gaussian. For every \(c>0\), using the *same* calibration standard deviation \(c/n\) on the two physically distinct preparation graphs yields
\[
F_{K_n}(c/n)\to0,
\qquad
F_{T_n}(c/n)\to\frac{1+e^{-c^2/8}}2>0.
\]
Although the ideal graph states for the complete graph and star are related by local Clifford operations, the specified **preparation noise mechanism** is not invariant under replacing one edge-gate circuit by the other.

## Assumptions and scope
All graphs are simple and have no self-loops. The graph state is prepared from \(|+\rangle^{\otimes n}\) using commuting controlled phases on the prescribed edges. The random phase error has the same value on all edges within one preparation and is Gaussian with mean zero and variance \(\sigma^2\). There is no separate stochastic error on vertices, no independent edge-angle component, and no adaptive correction. The output fidelity is averaged over independent preparations, **after** squaring the state overlap; it is not the modulus square of an averaged amplitude.

The general limit is a theorem for sequences satisfying its three displayed graph conditions. It is not asserted for sparse bounded-degree regular graphs or hub-dominated graphs. The star theorem gives a specific boundary outside this class. The complete-graph crossover assumes the positive-width asymptotic regime indicated in each statement; in particular \(\Theta(t)\) is defined for \(t>0\), and the \(c=0\) exact no-noise case is handled by the first limit.

## Proof
**Exact fidelity reduction.** For \(z\in\{0,1\}^V\), the ideal computational-basis amplitude of \(|G\rangle\) is \(2^{-n/2}(-1)^{H_G(z)}\). The coherent common-angle gate error multiplies it by \(e^{i\varepsilon H_G(z)}\). Consequently,
\[
\langle G|G_\varepsilon\rangle
=2^{-n}\sum_{z\in\{0,1\}^V}e^{i\varepsilon H_G(z)}
=\mathbb E_X e^{i\varepsilon H_G(X)}.
\]
Taking its modulus square introduces an independent \(Y\), and the centered Gaussian characteristic function \(\mathbb E e^{i\varepsilon a}=e^{-\sigma^2a^2/2}\) gives the exact identity.

**The degree decomposition.** Put \(Z_v=X_v-1/2\). Every edge contributes
\[
X_uX_v=\frac14+\frac12Z_u+\frac12Z_v+Z_uZ_v,
\]
so
\[
H_G(X)=\frac{m_G}4+\frac12\sum_v\deg(v)Z_v+\sum_{uv\in E}Z_uZ_v.
\]
The linear and quadratic parts are orthogonal in \(L^2\), and all distinct quadratic edge monomials are pairwise orthogonal, even if the edges share a vertex. Since \(\operatorname{Var}(Z_v)=1/4\),
\[
\operatorname{Var}(H_G(X))=\frac{S_G}{16}+\frac{m_G}{16}.
\]
Subtracting the independent copy doubles this variance and proves the displayed finite identity.

**Universal degree-norm law.** Write
\[
\frac{H_G(X)-H_G(Y)}{\sqrt{S_G}}=L_G+Q_G,
\]
where
\[
L_G=\frac1{2\sqrt{S_G}}\sum_v\deg(v)(X_v-Y_v)
\]
and \(Q_G\) is the difference of quadratic parts divided by \(\sqrt{S_G}\). The independent summands of \(L_G\) are centered, bounded, have total variance \(1/8\), and their maximum absolute size tends to zero under \(\max_v\deg(v)/\sqrt{S_G}\to0\). The elementary triangular-array Lindeberg central limit theorem therefore gives
\[
L_G\Longrightarrow N(0,1/8).
\]
Pairwise orthogonality gives
\[
\mathbb E[Q_G^2]=\frac{m_G}{8S_G}\longrightarrow0.
\]
Thus the entire normalized difference converges in law to \(N(0,1/8)\). Applying the bounded continuous function \(z\mapsto e^{-c^2z^2/2}\) yields
\[
\lim F_G(c/\sqrt{S_G})
=\mathbb E_{Z\sim N(0,1/8)}e^{-c^2Z^2/2}
=(1+c^2/8)^{-1/2}.
\]
This proves the universal assertion, with no independence assumption between edge phases (the edge phases are deliberately identical).

**Complete-graph binomial formula.** For \(K_n\), all edges among the selected one-vertices contribute, so \(H_{K_n}(X)=\binom K2\) with \(K\sim\operatorname{Bin}(n,1/2)\). The exact binomial double sum follows. Here \(S_{K_n}=n(n-1)^2\), \(m_{K_n}=n(n-1)/2\), and the universal limit gives the \(n^{-3/2}\) critical window.

**Uniform lattice crossover.** Let \(D=K-L\) and \(W=K+L\). The algebraic identity
\[
\binom K2-\binom L2=\frac{D(W-1)}2
\]
rewrites the Gaussian factor as \(\exp[-\sigma_n^2D^2(W-1)^2/8]\). The exact difference law, by Vandermonde's identity, is
\[
\Pr(D=r)=4^{-n}\binom{2n}{n+r},\qquad -n\le r\le n.
\]
By the central binomial approximation, uniformly for \(|r|=o(\sqrt n)\),
\[
\Pr(D=r)=\frac{1+o(1)}{\sqrt{\pi n}}.
\]
Also \(W/n\to1\) with exponentially small probability of a fixed-proportion deviation, uniformly for the central difference window. Put \(t_n=n\sigma_n\) and \(a_n=\sqrt n\,t_n=n^{3/2}\sigma_n\to\infty\). The terms relevant to the Gaussian sum have \(|D|=O(1/t_n)\) when \(t_n\to0\), hence \(|D|=o(\sqrt n)\); for \(t_n\) bounded away from zero, only bounded \(D\) contribute. On either window, replace \(\Pr(D=r)\) by \((\pi n)^{-1/2}\) and \((W-1)/n\) by one. The errors are relative \(o(1)\): to make the exchange uniform, restrict first to \(|t_nr|\le M_n\) with \(M_n\to\infty\) slowly enough that \(M_n/a_n\to0\) and \(M_n^2n^{-1/3}\to0\), and to \(|W-n|\le n^{2/3}\); outside these restrictions, binomial concentration and Gaussian tails contribute \(o(\Theta(t_n)/\sqrt n)\). When \(t_n\) grows, the \(r=0\) summand separately supplies the same normalization while all nonzero differences are negligible. Thus
\[
F_{K_n}(\sigma_n)=\frac{1+o(1)}{\sqrt{\pi n}}\sum_{r\in\mathbb Z}e^{-t_n^2r^2/8}.
\]
For \(t\downarrow0\), a Riemann-sum approximation gives \(\Theta(t)\sim\sqrt{8\pi}/t\). For fixed positive \(t\), the series is continuous. For \(t\to\infty\), only \(r=0\) survives. These prove the three subregimes.

**The star exception.** Write the hub bit as \(B\sim\operatorname{Bernoulli}(1/2)\), and let \(M\sim\operatorname{Bin}(n-1,1/2)\) be the number of selected leaves, independent of \(B\). Then
\[
H_{T_n}(X)=BM.
\]
Since \(M/n\to1/2\) in probability, \(H_{T_n}(X)/n\Longrightarrow B/2\). The independent-copy difference divided by \(n\) tends to \((B-B')/2\). The bounded Gaussian fidelity functional consequently tends to
\[
\mathbb E\exp[-c^2(B-B')^2/8]
=\frac12(1+e^{-c^2/8}).
\]
The complete-graph lattice formula at \(\sigma_n=c/n\), for \(c>0\), instead gives \(F_{K_n}(c/n)\sim\Theta(c)/\sqrt{\pi n}\to0\). The comparison follows.

## Verification
All universal results are analytic and are proved above. The bundled standard-library checker reconstructs finite computational-basis amplitudes, checks the exact degree-square variance identity for stars, cycles, and complete graphs, compares exact finite complete-graph fidelity with the binomial formula, and numerically tests the critical, theta-crossover, saturation, and star-limit statements. The finite tests corroborate formulas but do not establish any of the asymptotic assertions.

Reproduce the finite checks by executing the bundled `artifacts/verify.py` with Python 3. No nonstandard dependencies or data files are required.

## Relationship to prior work
Numajiri, Yamashika, Tanizawa, Yoshii, Takeuchi, and Tsuchiya (arXiv:2510.00548v1) map graph-state fidelity under independent identically distributed **single-qubit Pauli noise** to classical partition functions. They analyze connectivity-dependent fidelity on regular lattices and the complete graph, and identify correlated noise as a natural extension. Their model is not a common coherent calibration angle shared by every entangling edge, and their complete-graph formula does not imply the lattice crossover here.

Szymański, Vandré, and Gühne (arXiv:2402.00937) **already introduce this same physical common-phase Gaussian edge-error model** for weighted graph-state preparation. In their Section 4.2 they use a lowest-order density-matrix approximation and study robustness of subsequent Bell/GHZ extraction and postselection on specially constructed linear networks. The physical noise model is therefore explicitly credited as prior. Their state-extraction analysis does not classify full-state fidelity for arbitrary graph degree profiles, the complete graph's \(n^{-3/2}\) precision threshold and theta crossover, or the star/complete fidelity separation.

Alexander, Özdemir, and Tame (arXiv:2602.13026v1) study weighted star and complete graph states, including Gaussian perturbations of **independently sampled** edge weights in numerical work. Their analytic formulas concern quantum Fisher information and phase-estimator variance under uniformly weighted graphs, not ensemble-averaged full-state fidelity under a shared random phase. Their comparison of star and complete architectures motivates considering topology; it does not dominate the claim here.

The probability decomposition, elementary triangular-array limit, local central binomial asymptotics, and Jacobi theta function are standard mathematical tools. The result claims no novelty for those ingredients individually; it identifies and rigorously unifies their consequences for the specific correlated quantum-preparation fidelity observable.

## Limitations
The claims are exact for an idealized common-mode Gaussian coherent phase error with identical value on every edge within a preparation. They are not direct predictions for hardware with independent gate errors, qubit decoherence, non-Gaussian drift, error correction, readout noise, or pulse scheduling effects. Graphs that violate the stated degree conditions need separate analysis; the star is one such exception, not a classification of every hub-dominated graph.

Fidelity is measured against the uncorrected ideal computational graph state. Local-Clifford equivalence of two noiseless graph states does not identify their noisy preparation circuits or their resulting fidelities. The theta-crossover formula is asymptotic; it is not an exact finite-size equality. No claim of arbitrary optimal graph choice or computational advantage is made.

## References
1. T. Numajiri, S. Yamashika, T. Tanizawa, R. Yoshii, Y. Takeuchi, and S. Tsuchiya, *Phase Transitions and Noise Robustness of Quantum Graph States*, arXiv:2510.00548v1 (first public 2025-10-01); *Quantum* **10**, 2094 (2026), DOI 10.22331/q-2026-05-05-2094.
2. K. Szymański, L. Vandré, and O. Gühne, *Useful entanglement can be extracted from noisy graph states*, arXiv:2402.00937v1 (first public 2024-02-01); *Quantum* **10**, 1977 (2026), DOI 10.22331/q-2026-01-21-1977.
3. B. J. Alexander, Ş. K. Özdemir, and M. S. Tame, *Weighted graph states as a resource for quantum metrology*, arXiv:2602.13026v1 (first public 2026-02-13).
