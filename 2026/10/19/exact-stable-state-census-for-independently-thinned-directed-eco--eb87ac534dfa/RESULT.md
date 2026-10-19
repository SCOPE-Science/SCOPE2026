# Exact stable-state census for independently thinned directed ecological cycles

## Finding
Consider a directed ecological inhibition cycle on \(n\ge3\) species. Every directed inhibition link is independently retained with probability \(q\in[0,1]\). With a common strength \(\sigma>0\), the population equation is
\[
\dot x_i=x_i\bigl(1-x_i-\sigma e_i x_{i+1}\bigr),\qquad i\in\mathbb Z/n\mathbb Z,
\]
where \(e_i\in\{0,1\}\) indicates the presence of the link from species \(i+1\) to species \(i\). An equilibrium is called **stable** here precisely when the complete \(n\times n\) Jacobian is Hurwitz (all eigenvalues have strictly negative real part), including the transverse eigenvalues of extinct species. Let \(S\) be the number of these stable equilibria in the nonnegative orthant.

**Theorem.** Assume \(\sigma\ne1\), and for odd \(n\) additionally assume \(\sigma\ne\sec(\pi/n)\).

1. If \(0<\sigma<1\), every link realization has exactly one stable equilibrium, with all \(n\) species present.
2. If \(\sigma>1\) and \(n\) is even, an intact cycle has exactly two stable equilibria (the two alternating \(0,1\) configurations), whereas every cycle with at least one deleted link has exactly one stable equilibrium.
3. If \(\sigma>1\) and \(n\) is odd, a fully retained cycle has exactly one stable equilibrium if \(\sigma<\sec(\pi/n)\), and none if \(\sigma>\sec(\pi/n)\). Every cycle with a deleted link has exactly one stable equilibrium.

Consequently, in the strong-inhibition regime the complete probability law of \(S\) is
\[
\begin{array}{c|ccc}
\text{case}&\Pr(S=0)&\Pr(S=1)&\Pr(S=2)\\\hline
n\ \text{even},\ \sigma>1&0&1-q^n&q^n\\
n\ \text{odd},\ 1<\sigma<\sec(\pi/n)&0&1&0\\
n\ \text{odd},\ \sigma>\sec(\pi/n)&q^n&1-q^n&0.
\end{array}
\]
For \(0<\sigma<1\), \(\Pr(S=1)=1\) regardless of parity.

Every incomplete cycle has a unique stable equilibrium that attracts all trajectories with strictly positive initial abundances; at \(\sigma>1\), its coordinates belong to \(\{0,1\}\). Define \(K\) as its number of surviving species on an incomplete cycle, and set \(K=0\) on intact cycles merely for the next expectation. Then
\[
\mathbb E K=\begin{cases}
\dfrac{n(1-q^n)}{1+q},&n\text{ even},\\[6pt]
\dfrac{n(1-q^{n+1})}{1+q},&n\text{ odd},
\end{cases}\qquad \sigma>1.
\]
For a fixed \(\sigma>1\) and retention \(q_n=1-\lambda/n\), \(\lambda>0\), the exceptional probability \(q_n^n\) converges to \(e^{-\lambda}\): this is the probability of two stable states along even sizes, and of no stable state along sufficiently large odd sizes.

## Assumptions and scope
The graph contains only the \(n\) possible oriented successive links, with no additional interactions. Growth and self-limitation rates are identically one, and each present link has inhibitory coefficient \(\sigma\). The random graph is sampled once and then held fixed; there is no dynamical edge resampling. Equilibria are counted among \(x_i\ge0\), not only strictly positive coexistence equilibria. Stability means Hurwitz linear stability, deliberately excluding threshold cases \(\sigma=1\) and, when \(n\) is odd, \(\sigma=\sec(\pi/n)\). Assertions about attractors other than equilibria are not made.

## Proof
**1. A broken cycle.** If any \(e_i=0\), the interaction graph is acyclic. Topologically order its vertices so that each rate equation depends only on itself and previously ordered populations. The first coordinate obeys \(\dot x=x(1-x)\) and converges to one from every positive initial value. Recursively, an equation \(\dot x_i=x_i(a_i(t)-x_i)\) has \(a_i(t)\to a_i^*=1-\sigma e_i x_{i+1}^*\). When \(a_i^*\ne0\), every positive solution converges to \(\max(0,a_i^*)\), by scalar comparison with logistic equations of constant coefficients \(a_i^*\pm\epsilon\). If \(\sigma<1\), all limiting coordinates are strictly positive and at most one. If \(\sigma>1\), each limiting coordinate is zero or one, and the recursion alternates them wherever links are present. Neither regime produces \(a_i^*=0\). This constructs the single equilibrium attracting all strictly positive states. Any Hurwitz equilibrium necessarily selects, inductively, the same coordinate at every step: setting a coordinate to zero while its net invasion growth is positive would introduce a positive Jacobian eigenvalue. In this ordering the Jacobian is triangular, with diagonal entries \(-x_i^*<0\) at present species and \(a_i^*<0\) at absent ones, proving Hurwitz stability and uniqueness among stable equilibria.

**2. An intact cycle: interior states.** At every strictly positive equilibrium,
\[
x_i+\sigma x_{i+1}=1.
\]
The cyclic shift matrix \(P\) has eigenvalues \(\exp(2\pi i k/n)\). Since \(\sigma\ne1\), \(I+\sigma P\) is invertible and the sole positive equilibrium is \(x_i^*=(1+\sigma)^{-1}\). The Jacobian there equals \(-(I+\sigma P)/(1+\sigma)\), with eigenvalues
\[
\mu_k=-\frac{1+\sigma\exp(2\pi i k/n)}{1+\sigma}.
\]
For even \(n\), the minimal real part of the roots of unity is \(-1\), giving stability precisely for \(\sigma<1\). For odd \(n\), the minimal real part is \(-\cos(\pi/n)\), giving stability precisely for \(\sigma<\sec(\pi/n)\).

**3. An intact cycle: boundary states.** Every equilibrium coordinate satisfies \(0\le x_i\le1\). If \(0<\sigma<1\), a zero coordinate has transverse invasion eigenvalue \(1-\sigma x_{i+1}>0\), and cannot occur at a Hurwitz equilibrium. If \(\sigma>1\), a zero coordinate at a Hurwitz equilibrium must have positive invasion suppression \(\sigma x_{i+1}>1\), so two consecutive zeros are forbidden. In particular, the predecessor of a zero must be positive and therefore equals one, because its successor is zero. The predecessor of this unit coordinate must be zero, since a positive coordinate there would have to equal \(1-\sigma<0\). Repeated backward propagation by two sites shows that the zeros and ones alternate around the cycle. An odd cycle cannot alternate consistently, so it has no Hurwitz boundary equilibrium. An even cycle has exactly two such alternating configurations. Their Jacobians have diagonal eigenvalues \(-1\) on occupied sites and \(1-\sigma<0\) on empty sites, since no two occupied sites interact and the remaining Jacobian is block triangular. These two are Hurwitz. Combining with Step 2 gives the full count.

**4. Random deletion and richness.** The intact-cycle event has probability \(q^n\); every other realization is acyclic, hence Step 1 yields the stated three cases. In the strong-inhibition regime, at a designated vertex of an incomplete cycle the equilibrium equals one exactly when the number \(r\) of consecutive present links encountered in the forward direction before the first absent link is even. The joint event \(r=j\) and incompleteness has probability \((1-q)q^j\) for \(0\le j<n\). Summing over even \(j\), multiplying by \(n\), and using rotational symmetry gives
\[
\mathbb E K=n(1-q)\sum_{0\le2j<n}q^{2j},
\]
which is the displayed parity-dependent expression. The formulas extend to \(q=1\) by continuity and direct interpretation. Finally, \((1-\lambda/n)^n\to e^{-\lambda}\). For fixed \(\sigma>1\), \(\sec(\pi/n)\to1\) on odd sizes, so the odd high-inhibition case eventually applies.

## Verification
The included standalone program `verify.py` enumerates all \(2^n\) retained-edge realizations and all \(2^n\) candidate equilibrium supports for \(3\le n\le7\), using independent linear solves and full Jacobian spectra. It checks \(992\) graph/parameter combinations across \(\sigma=1/2,5/4,3/2,5/2\). It separately enumerates link configurations for \(3\le n\le11\) to test the probability-weighted richness formula at three retention probabilities. All tests passed on extraction. These finite tests are supplementary; the arbitrary-size conclusions are proved in Steps 1–4.

## Relationship to prior work
Nassor, Biermé, Herniou and Madec (2026) introduce a system-centered probability framework for the multiplicity and richness of stable generalized Lotka–Volterra equilibria, illustrating it mainly by Monte Carlo samples of ten-species systems. The theorem here supplies a fully explicit, finite-size distribution of stable-equilibrium multiplicity and survival richness for a natural independently diluted cyclic interaction family. It does not claim novelty for the classical generalized Lotka–Volterra equation, the root-of-unity spectral calculation, or the general existence of cyclic ecological instability. Classical results on stable community multiplicity and recent sparse-network mean-field stability models are complementary: they do not themselves state this exact directed-cycle Bernoulli law. The spectral threshold has analogues in established negative-feedback-cycle theory; the contribution here is its combination with a complete boundary-state census, topology-dependent multiplicity, and exact dilution probabilities.

## Limitations
The full interaction graph is restricted to one oriented cycle with independent deletions and uniform link weight; conclusions do not extend automatically to undirected, reciprocal or general random interaction networks. In particular, the probability \(q^n\) should not be interpreted as a universal random-graph stability law. The critical parameter equalities are excluded. For intact odd cycles above the threshold, the theorem asserts absence of Hurwitz equilibria, not absence of equilibria, nor existence or nonexistence of limit cycles. The values for stable richness exclude intact graphs by definition of \(K\), and the paper does not assert uniqueness of all (including unstable) equilibria on a broken cycle.

## References
1. H. Nassor, H. Biermé, E. Herniou and S. Madec, *A system-centered probabilistic formalism linking multiple equilibria and biodiversity in ecological and evolutionary models*, arXiv:2609.17232v1 (first posted 2026-09-15), https://arxiv.org/abs/2609.17232.
2. W. E. Hong and R. L. Pego, *Exclusion and multiplicity for stable communities in Lotka–Volterra systems*, arXiv:2102.00611, https://arxiv.org/abs/2102.00611.
3. T. Ö. Çelik, V. A. Isoldi, I. Portakal and G. Zucal, *Stable Coexistence in Ecologies and Games*, arXiv:2609.09286v1 (2026), https://arxiv.org/abs/2609.09286.
4. M. Tarabolo, L. Dall'Asta and R. Mulet, *Sparse Interactions Reshape Stability in Random Lotka–Volterra Dynamics*, arXiv:2512.22563v1 (2025), https://arxiv.org/abs/2512.22563.
5. K.-W. Chen and C.-W. Shih, *Stoichiometric balance and sustained rhythms*, Journal of Mathematical Biology (2026), https://doi.org/10.1007/s00285-026-02419-w.
