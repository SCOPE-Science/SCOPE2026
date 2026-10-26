# Sharp imbalance ceiling for coherent transfer across a single-edge clique bottleneck

## Finding

Let the barbell \(B_{a,b}\) consist of a clique on \(a\) vertices and a clique on \(b\) vertices, joined by exactly one unweighted edge, with \(a,b\ge3\). Use the degree-normalized adjacency Hamiltonian \(H_{a,b}=D^{-1/2}AD^{-1/2}\). Let \(|L_a\rangle\) and \(|R_b\rangle\) be the uniform unit vectors on the left and right cliques, respectively, and let \(\Pi_R\) project onto all vertices of the right clique.

Suppose \(a,b\to\infty\) along **any** integer sequence for which \(a/b\to\rho\in(0,\infty)\). Then for every \(\tau\ge0\), locally uniformly in \(\tau\),

\[
\bigl|\langle R_b|e^{-i\tau abH_{a,b}}|L_a\rangle\bigr|^2
\longrightarrow F_\rho(\tau),\qquad
\|\Pi_R e^{-i\tau abH_{a,b}}|L_a\rangle\|^2
\longrightarrow F_\rho(\tau),
\]
\[
F_\rho(\tau)=\frac{4}{(\rho+\rho^{-1})^2}
\sin^2\!\left(\frac{\rho+\rho^{-1}}2\tau\right).
\]

The corresponding **all-time** optimal probabilities have the same sharp limit:

\[
\lim_{\substack{a,b\to\infty\\a/b\to\rho}}\sup_{t\ge0}\bigl|\langle R_b|e^{-itH_{a,b}}|L_a\rangle\bigr|^2
=\lim_{\substack{a,b\to\infty\\a/b\to\rho}}\sup_{t\ge0}\|\Pi_R e^{-itH_{a,b}}|L_a\rangle\|^2
=\frac{4\rho^2}{(1+\rho^2)^2}.
\]

Here each limit is taken along the stated sequence of graphs; \(\sup_{t\ge0}\) is taken **before** that limit. The first maximum of the limiting, nontrivial oscillation occurs at scaled time \(\tau=\pi/(\rho+\rho^{-1})\); a finite-size near-maximizer is
\[
t_{a,b}=\frac{\pi a^2b^2}{a^2+b^2}.
\]
Consequently, asymptotically perfect coherent transfer between the cliques is possible exactly when their sizes are asymptotically equal (\(\rho=1\)); every fixed nonunit limiting size ratio imposes a strict fidelity deficit. Conversely, if \(t_{a,b}=o(ab)\), then the right-clique probability tends to zero.

For a **localized initial state** at any nonbridge left-clique vertex \(|v\rangle\), the same right-clique measurement has a smaller sharp optimum:
\[
\lim_{\substack{a,b\to\infty\\a/b\to\rho}}
a\sup_{t\ge0}\|\Pi_R e^{-itH_{a,b}}|v\rangle\|^2
=\frac{4\rho^2}{(1+\rho^2)^2}.
\]
Thus collective preparation permits order-one transfer, while nonbridge-vertex preparation permits only order-\(1/a\) transfer under the identical Hamiltonian.

## Assumptions and scope

The graph is simple, connected and unweighted, with exactly one bridge edge. Both cliques have at least three vertices. The Hamiltonian is the **symmetric degree-normalized adjacency**, not ordinary adjacency or the combinatorial graph Laplacian. Evolution is closed, coherent, unmeasured unitary evolution. The initial states, the right-clique measurement, and the order of the scaling and time supremum are as specified above. The asymptotic regime requires \(a/b\to\rho\) with \(0<\rho<\infty\); no claim is made for a ratio tending to zero or infinity.

## Proof

**1. An exact invariant sector.** Let \(|I_a\rangle\) be the normalized uniform vector over the \(a-1\) *nonbridge* vertices of the left clique, \(|\ell\rangle\) the left bridge vertex, \(|r\rangle\) the right bridge vertex, and \(|I_b\rangle\) the right nonbridge uniform vector. The four-dimensional span is exactly invariant. In the ordered basis \((I_a,\ell,r,I_b)\), the restricted operator is

\[
Q_{a,b}=\begin{pmatrix}
\dfrac{a-2}{a-1}&a^{-1/2}&0&0\\
a^{-1/2}&0&(ab)^{-1/2}&0\\
0&(ab)^{-1/2}&0&b^{-1/2}\\
0&0&b^{-1/2}&\dfrac{b-2}{b-1}
\end{pmatrix}.
\]

This follows directly by summing the normalized edge weights: a nonbridge vertex has degree \(a-1\), a bridge vertex on that side has degree \(a\), and similarly on the other side. The orthogonal complement consists of the zero-sum nonbridge modes, which are exact eigenvectors supported in their originating cliques. Also,
\[
|L_a\rangle=\sqrt{\frac{a-1}{a}}|I_a\rangle+a^{-1/2}|\ell\rangle,
\qquad |R_b\rangle=\sqrt{\frac{b-1}{b}}|I_b\rangle+b^{-1/2}|r\rangle.
\]
Thus both collective states differ from their nonbridge-uniform representatives in norm by \(O(k^{-1/2})\), where \(k=\min(a,b)\), uniformly under the ratio hypothesis.

**2. The two nearly stationary modes.** Reorder the quotient into the two interiors followed by the two bridge coordinates. Then
\[
Q_{a,b}=\begin{pmatrix}D&E\\E&C\end{pmatrix},\quad
D=\begin{pmatrix}(a-2)/(a-1)&0\\0&(b-2)/(b-1)\end{pmatrix},
\quad E=\operatorname{diag}(a^{-1/2},b^{-1/2}),
\quad C=\begin{pmatrix}0&(ab)^{-1/2}\\(ab)^{-1/2}&0\end{pmatrix}.
\]
As \(k\to\infty\), this matrix has two eigenvalues near \(1\) and two near \(0\). For each upper eigenpair \((\lambda,(u,v))\), the bridge coordinate is \(v=(\lambda I-C)^{-1}Eu\). Substitution gives the *exact* Schur-complement equation
\[
\bigl[D+E(\lambda I-C)^{-1}E\bigr]u=\lambda u.
\]
For the two upper eigenvalues \(\lambda=1+O(k^{-2})\): to see the improved order, initially place \(\lambda\) near \(1\) by spectral separation; the displayed equation has \(D+E(\lambda I-C)^{-1}E=I+O(k^{-2})\) because the diagonal terms \(-1/(a-1)\) and \(+1/a\) cancel to first order. A second expansion yields, uniformly as \(a/b\) remains in a compact subset of \((0,\infty)\),
\[
D+E(\lambda I-C)^{-1}E=I+K_{a,b}+O(k^{-3}),\qquad
K_{a,b}=\begin{pmatrix}-a^{-2}&(ab)^{-1}\\(ab)^{-1}&-b^{-2}\end{pmatrix}.
\]

The matrix \(K_{a,b}\) has simple eigenvalues \(0\) and \(-a^{-2}-b^{-2}\), with normalized eigenvectors proportional to \((a,b)\) and \((b,-a)\). Their separation is of order \(k^{-2}\), so the \(O(k^{-3})\) perturbation does not change their asymptotic spectral projections. In particular, the upper quotient eigenvalues are
\[
\lambda_+=1,\qquad \lambda_-=1-a^{-2}-b^{-2}+O(k^{-3}).
\]
The first equality is exact: the full normalized adjacency of any connected graph has Perron eigenvector \(D^{1/2}\mathbf1\). The upper eigenvectors have bridge coordinates of norm \(O(k^{-1/2})\); their interior vectors approach \((a,b)/\sqrt{a^2+b^2}\) and \((b,-a)/\sqrt{a^2+b^2}\). The spectral projection of an interior-uniform vector onto the remaining two quotient eigenvectors has norm \(O(k^{-1/2})\), so its dynamical contribution stays of that order *uniformly for all times*.

**3. Transfer formula and sharp optimization.** The two significant spectral cross-coefficients between \(I_a\) and \(I_b\) are
\[
\frac{ab}{a^2+b^2}+o(1),\qquad -\frac{ab}{a^2+b^2}+o(1).
\]
Therefore, uniformly in real \(t\), the exact amplitude equals
\[
\langle I_b|e^{-itQ_{a,b}}|I_a\rangle=
\frac{ab}{a^2+b^2}\bigl(e^{-it\lambda_+}-e^{-it\lambda_-}\bigr)+o(1).
\]
The error is uniform in \(t\) because it involves only errors in four finite-dimensional spectral projections, not Taylor expansions of long-time phases. For \(t=\tau ab\), the relative phase tends to \(\tau(\rho+\rho^{-1})\). Squaring gives the asserted \(F_\rho\), locally uniformly in \(\tau\). The difference between the uniform-clique amplitudes and the interior amplitudes is uniformly \(O(k^{-1/2})\). The bridge components of the evolved interior state are uniformly \(O(k^{-1/2})\), so the whole right-clique measurement also converges to the same limit.

The triangle inequality for the two upper spectral terms proves the all-time upper bound \(2ab/(a^2+b^2)+o(1)\) on the transfer amplitude; adding the negligible bridge mass proves the same squared upper bound for right-clique probability. Choosing \(t=\pi/(\lambda_+-\lambda_-)\) makes their relative phase exactly opposite and attains the bound asymptotically. The stated explicit \(t_{a,b}\) has the same relative phase up to \(o(1)\). If \(t=o(ab)\), the relative phase vanishes and the same uniform spectral decomposition yields a vanishing right-side probability.

**4. Local-state obstruction.** For every nonbridge vertex \(v\) on the left, decompose exactly
\[
|v\rangle=(a-1)^{-1/2}|I_a\rangle+|d_v\rangle,
\qquad H_{a,b}|d_v\rangle=-\frac{1}{a-1}|d_v\rangle.
\]
The vector \(|d_v\rangle\) is zero-sum on the left nonbridge vertices and has identically zero right-side component at every time. Consequently, for every real \(t\),
\[
\|\Pi_R e^{-itH_{a,b}}|v\rangle\|^2
=\frac{1}{a-1}\|\Pi_R e^{-itH_{a,b}}|I_a\rangle\|^2.
\]
The preceding all-time optimization also applies to \(|I_a\rangle\). Taking the supremum, multiplying by \(a\), and passing to the limit proves the local-preparation law.

## Verification

Run `python barbell_verification.py` with NumPy. The program independently builds the full \((a+b)\)-dimensional normalized adjacency and the four-dimensional invariant quotient. Across six pairs of small clique sizes and six observation times, it checks exactly the quotient transfer probability, the total right-clique probability, and the localized-state dark-mode identity against separately evolved full matrices (108 comparisons). For eight larger graph sizes it compares the first macroscopic peak and upper spectral gap with the derived asymptotics (24 tests). For four size pairs and five scaled times it checks both collective and total right-clique probabilities against the limiting profile (40 tests): **172 finite numerical diagnostics in total**. The diagnostics are not an exhaustive or infinite proof; the argument above establishes the limits.

## Relationship to prior work

Dhamapurkar and Subrahmanyam (2026), arXiv:2603.05643v1, study the **equal-clique** normalized-adjacency barbell, its exact spectrum, and vertex-initial localization through inverse participation ratios. Their equal-clique spectral information and zero-sum dark modes are antecedents, not claimed here. The present claim identifies the sharp **unequal-size** collective-transfer law, a global-in-time imbalance ceiling, and a quantitative collective-versus-single-vertex preparation contrast.

Duda and Wong (2024), arXiv:2408.08244, investigate **equal-clique, oracle-assisted spatial search**, with tunable bridge weights, under ordinary adjacency or combinatorial-Laplacian walks; the present claim is an unmarked, unweighted, degree-normalized walk. Coutinho and Baptista (2022), arXiv:2209.04668, characterize normalized-Laplacian *vertex* transfer and periodicity, not collective-transfer limits on asymmetric barbells. Novo and collaborators (2014/2015), arXiv:1412.7209, establish general invariant-subspace/Lanczos reduction and related quantum transport methods, which motivate but do not furnish the asymptotic imbalance law for this graph and preparation. Generic two-level perturbation methods are used, not claimed as new.

## Limitations

The result concerns a one-particle, undriven, noiseless, degree-normalized walk on two growing cliques with **comparable** sizes. It does not assert exact perfect transfer at finite sizes, transfer for fixed localized bridge-vertex preparation, robustness to noise, an energy-constrained state-preparation protocol, or the regime where the clique-size ratio tends to zero or infinity. The explicit peak time is asymptotic and need not be the first local maximum at finite size. Finite simulations corroborate but do not prove the infinite-family claim. The originality comparison is best-knowledge rather than a universal proof of priority; uninspected general spectral-transfer theorems remain a possible source of implicit coverage.

## References

1. S. Dhamapurkar and K. V. Subrahmanyam, *Localization Without Disorder: Quantum Walks on Structured Graphs*, arXiv:2603.05643v1 (first public 2026-03-05), https://arxiv.org/html/2603.05643v1.
2. J. Duda and T. G. Wong, *Searching Weighted Barbell Graphs with Laplacian and Adjacency Quantum Walks*, arXiv:2408.08244, https://arxiv.org/html/2408.08244v2.
3. G. Coutinho and P. F. Baptista, *Quantum Walks in the Normalized Laplacian*, arXiv:2209.04668, https://arxiv.org/abs/2209.04668.
4. L. Novo, S. Chakraborty, M. Mohseni, H. Neven and Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209, https://arxiv.org/abs/1412.7209.
