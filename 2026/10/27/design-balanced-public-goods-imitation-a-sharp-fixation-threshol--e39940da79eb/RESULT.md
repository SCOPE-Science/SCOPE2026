# Design-balanced public-goods imitation: a sharp fixation threshold and a Fano-plane non-lumpability witness

## Finding

**Theorem (balanced incidence, fixation, and stochastic geometry).** Let \(v\ge3\), \(2\le g<v\), and let \(H\) be a finite simple \(g\)-uniform hypergraph in which every vertex belongs to exactly \(d>0\) hyperedges. Each player chooses cooperation (\(1\)) or defection (\(0\)); each edge implements the linear public-goods payoff with unit cost and a common normalized synergy \(r>0\). The final payoff is the arithmetic mean of the player's payoffs over incident edges. The following statements hold.

1. Every strategy configuration gives equal payoffs to all cooperators and equal payoffs to all defectors **if and only if** every unordered pair of vertices belongs to the same positive number \(\lambda\) of hyperedges, i.e. \(H\) is a \(2\)-\((v,g,\lambda)\) design. For such a design, all cooperator–defector payoff gaps equal
   \[
   \gamma_v(r)=r\frac{v-g}{v-1}-1.
   \]
2. On every such design, use the following elementary *best-earner imitation* rule: select a focal vertex uniformly; select one of its incident hyperedges uniformly; identify a highest-payoff vertex in that edge; and let the focal player copy its strategy with probability \((\pi_{\max}-\pi_{\mathrm{focal}})/\Delta\), for a fixed sufficiently large \(\Delta>0\). From **every mixed configuration**, the process almost surely reaches all defectors when \(r<r_*(v,g)\), reaches all cooperators when \(r>r_*(v,g)\), and makes no changes when \(r=r_*(v,g)\), where
   \[
   r_*(v,g)=\frac{v-1}{v-g}.
   \]
   In either strict regime, the takeover is monotone and has finite expectation. The conclusion includes designs with no permutation symmetry beyond the pair-count condition.
3. If \(H\) contains *every* \(g\)-subset as an edge and \(r>r_*\), the number of cooperators is a pure-birth Markov chain. With \(k\) cooperators the transition probability to \(k+1\) in a single elementary update is
   \[
   p_k=\frac{\gamma_v(r)}{\Delta}\frac{v-k}{v}\left(1-\frac{\binom{v-1-k}{g-1}}{\binom{v-1}{g-1}}\right),\qquad 1\le k<v,
   \]
   with the convention \(\binom ab=0\) for integers \(a<b\) and \(b\ge0\). Hence its exact mean time to all cooperation from \(k_0\ge1\) is
   \[
   \mathbb E_{k_0}\tau=\frac{\Delta}{\gamma_v(r)}\sum_{k=k_0}^{v-1}\frac{v}{(v-k)\bigl(1-\binom{v-1-k}{g-1}/\binom{v-1}{g-1}\bigr)}.
   \]
   For fixed integer \(g\ge2\), fixed \(r>1\), and the normalization \(\Delta=rg-1\), the one-cooperator takeover obeys the exact leading-order law
   \[
   \mathbb E_1\tau\sim \frac{rg-1}{r-1}\frac{g}{g-1}\,v\log v\quad(v\to\infty).
   \]
   This is measured in *single focal-player updates*, not population sweeps.
4. Equal-payoff-by-strategy does **not** imply that the number of cooperators itself forms a Markov chain on an arbitrary design. For the seven-point Fano plane with its seven triple edges, two configurations with exactly three cooperators give different one-step cooperator-increase probabilities:
   \[
   \Pr(3\to4\mid\{0,1,2\})=\frac47\frac{\gamma_7(r)}{\Delta},\qquad
   \Pr(3\to4\mid\{0,1,3\})=\frac37\frac{\gamma_7(r)}{\Delta}\qquad(r>3/2).
   \]
   The first cooperator triple is a line and the second is not. For \(r=2\), \(\Delta=5\), these are respectively \(4/105\) and \(1/35\).

## Assumptions and scope

The vertex set is \(V=\{0,\ldots,v-1\}\). The edge set consists of distinct size-\(g\) subsets, each vertex having positive common hyperdegree \(d\). The state is \(s\in\{0,1\}^{V}\). For edge \(e\), agent \(i\in e\) receives the raw per-edge payoff \(r\sum_{u\in e}s_u-s_i\); the agent's final payoff is
\[
\pi_i(s)=\frac1d\sum_{e\ni i}\left(r\sum_{u\in e}s_u-s_i\right).
\]
The normalized synergy \(r\) is the source model's synergy divided by group size, not the unnormalized multiplier. Equal payoff within each action class is required for *every* binary strategy state; a singleton or empty class satisfies its equality vacuously. A design means each pair of distinct vertices is contained in exactly \(\lambda>0\) edges. The integer identity \(d(g-1)=\lambda(v-1)\) follows by counting incident pairs.

An elementary update independently draws \(i\) uniformly from \(V\) and \(e\) uniformly from the \(d\) edges containing \(i\). The focal player compares its payoff with the largest payoff among all vertices of \(e\), and copies a maximizer's strategy with probability \((\pi_{\max}-\pi_i)/\Delta\), otherwise staying unchanged. For any fixed \(r\), take \(\Delta>0\) at least the maximum possible payoff range across all strategy states; ties among maximizers are immaterial, because the copying probability then vanishes or all maximizers share one action when the payoff gap is nonzero. A valid convenient normalization for \(r>1\) is \(\Delta=rg-1\), since the global upper payoff is at most \(rg-1\), the lower cooperator payoff is at least \(r-1\ge0\), and defector payoffs are nonnegative. There is no mutation, no changing edge game state, and all individuals use the same positive \(r\).

## Proof

**Payoff identity and converse.** Put \(M=\sum_u s_u\), and let \(m_{ij}\) be the number of edges containing the two distinct vertices \(i\) and \(j\). Counting each player's own strategy \(d\) times and all other participants by pair multiplicity gives
\[
\pi_i(s)=(r-1)s_i+\frac r d\sum_{j\ne i}m_{ij}s_j.
\]
If \(m_{ij}=\lambda\) for all distinct pairs, then
\[
\pi_i(s)=\frac{r\lambda}{d}M+\left(r\left[1-\frac\lambda d\right]-1\right)s_i.
\]
Counting a fixed vertex with a second vertex yields \(\lambda/d=(g-1)/(v-1)\), proving both the action-class payoff property and \(\gamma_v(r)\). Conversely, fix a state with exactly one cooperator \(i\). Every defector \(j\ne i\) receives \(r m_{ij}/d\). The hypothesized equality among defectors therefore forces \(m_{ij}\) to be independent of \(j\ne i\). Repeating for every \(i\), and invoking \(m_{ij}=m_{ji}\), shows a *single* constant \(\lambda\) works for every unordered pair. It is strictly positive because the hypergraph contains at least one edge and \(g\ge2\). This proves necessity without importing any design theorem.

**Fixation.** If \(\gamma_v(r)>0\), every cooperator earns strictly more than every defector, regardless of the strategy arrangement. A cooperator can never turn into a defector. If the state is mixed, take any defector \(i\) and any cooperator \(j\); by \(\lambda>0\), an edge contains both. Focal selection of \(i\) and of that edge has positive probability, and then \(i\) changes to cooperation with conditional probability \(\gamma_v(r)/\Delta>0\). Thus any mixed state has a strictly positive one-step chance of increasing \(M\), and \(M\) never decreases. The finite state space implies finite mean waiting at every level (for example, use the minimum of these finitely many positive one-step probabilities), and almost-sure absorption at \(M=v\). The same argument interchanges the two actions when \(\gamma_v(r)<0\), yielding all defection. When \(\gamma_v(r)=0\), every player has the same payoff regardless of action; all proposed copying probabilities are zero. Solving \(\gamma_v(r)=0\) gives \(r_*=(v-1)/(v-g)\).

**Complete-hypergraph transition and mean time.** Each vertex now belongs to \(d=\binom{v-1}{g-1}\) edges. Given \(M=k\), an increase needs the focal player to be one of \(v-k\) defectors. Of the \(d\) incident edges, exactly \(\binom{v-1-k}{g-1}\) consist exclusively of defectors; every other selected edge contains a cooperator and consequently has maximal payoff exceeding that of the focal player by precisely \(\gamma_v(r)\). This gives \(p_k\). Permutation symmetry makes \(p_k\) independent of the positions of cooperators, and the count is a pure-birth chain. The number of elementary trials until the first increase at level \(k\) is geometric with mean \(1/p_k\); summing levels gives the exact hitting time.

For completeness, when \(r<r_*\), the complete hypergraph instead gives a pure-death chain with transition probability
\[
q_k=\frac{-\gamma_v(r)}{\Delta}\frac{k}{v}\left(1-\frac{\binom{k-1}{g-1}}{\binom{v-1}{g-1}}\right),
\]
and mean time to all defection from \(k_0\) cooperators
\[
\mathbb E_{k_0}\tau_D=\frac{\Delta}{-\gamma_v(r)}\sum_{k=1}^{k_0}\frac{v}{k\bigl(1-\binom{k-1}{g-1}/\binom{v-1}{g-1}\bigr)}.
\]
For \(g=2\), the positive-side exact formula simplifies to \(\mathbb E_1\tau=2\Delta(v-1)H_{v-1}/\gamma_v(r)\), where \(H_m=\sum_{j=1}^{m}1/j\).

**Large-population asymptotic.** Keep \(g\ge2\) and \(r>1\) fixed, so \(r>r_*(v,g)\) for all sufficiently large \(v\), and \(\gamma_v(r)\to r-1\). Let \(C_{v,k}=1-\binom{v-1-k}{g-1}/\binom{v-1}{g-1}\). For \(k\le\varepsilon v\), with a fixed sufficiently small \(\varepsilon>0\), inclusion–exclusion over the \(g-1\) sampled coplayers gives uniformly
\[
C_{v,k}=\frac{(g-1)k}{v-1}\left[1+O_g(\varepsilon)\right].
\]
Consequently the contribution from \(k\le\varepsilon v\) to the dimensionless holding-time sum is \([1+O_g(\varepsilon)]v\log v/(g-1)+O_g(v)\). Writing \(j=v-k\) for the high-cooperation end, for \(j\le\varepsilon v\) the no-cooperator-edge probability is at most \((j/(v-1))^{g-1}\), so \(C_{v,v-j}=1+O_g(\varepsilon)\); its contribution is \([1+O_g(\varepsilon)]v\log v+O_g(v)\). On the middle interval \(\varepsilon v<k<(1-\varepsilon)v\), both \((v-k)/v\) and \(C_{v,k}\) are bounded away from zero, so the total holding-time sum is \(O_{g,\varepsilon}(v)\). First send \(v\to\infty\), then \(\varepsilon\downarrow0\), obtaining \(\frac g{g-1}v\log v\) for the dimensionless sum. Multiplication by \(\Delta/\gamma_v(r)\to(rg-1)/(r-1)\) proves the displayed asymptotic.

**Fano-plane rate distinction.** Choose the seven size-three edges
\[
012,\;034,\;056,\;135,\;146,\;236,\;245.
\]
Every vertex belongs to three edges, and every vertex pair belongs to exactly one edge. For a cooperator set \(S\), the probability of increasing the cooperator count when \(\gamma_7(r)>0\) is \(\frac{\gamma_7(r)}{7\Delta}\sum_{i\notin S}\frac{a_i(S)}3\), where \(a_i(S)\) counts edges containing \(i\) and at least one vertex of \(S\). Direct edge counting gives \(\sum_{i\notin\{0,1,2\}}a_i=12\) and \(\sum_{i\notin\{0,1,3\}}a_i=9\). These yield \(4\gamma_7(r)/(7\Delta)\) and \(3\gamma_7(r)/(7\Delta)\), respectively. Because both states have exactly three cooperators but distinct one-step probabilities of moving to four, the count process is not strongly lumpable by cooperator number. For \(r=2\), \(\gamma_7(r)=1/3\) and \(\Delta=5\), giving the stated exact rates. This completes the theorem.

## Verification

The accompanying standalone Python 3 file `verify.py` uses exact rational numbers to reconstruct payoffs for every strategy profile of the Fano plane and six complete uniform hypergraphs, check the pairwise design identity, compare the analytic count transition probability with exhaustive edge sampling, and reproduce both Fano rates. It also checks the harmonic identity for complete pairwise games through population size 30 and performs non-proving numerical sanity tests of the leading asymptotic. Execute `python verify.py` with no external dependencies; the expected outcome begins `PASS:`. The finite computational checks are not a proof of the all-size assertions; those are established above.

## Relationship to prior work

Wei, Xiong, Li, Feng, and Szolnoki (2026) introduce the normalized hyperedge public-goods payoffs, highest-payoff imitation, and environmental game transitions on random uniform hypergraphs. The theorem studies the scientifically natural *constant game-state* submodel with equal synergy on every edge and deterministic balanced block designs, rather than reproducing their numerical random-network phase diagrams. Alvarez-Rodriguez and colleagues (2021) develop the same higher-order best-earner imitation framework and relate dense hypergraphs to well-mixed replicator dynamics. Their replicator approximation and reported large-population relaxation scale do not yield an exact finite-population incidence if-and-only-if condition, full-configuration monotone fixation for all block designs, Fano non-lumpability, or an exact discrete expected absorption time. In particular, this theorem's finite-population threshold tends to the well-mixed threshold \(1\) as \(v\to\infty\); it does not assert that the prior asymptotic statement is invalid. Wang and Su (2026) study network public-goods cooperation conditions under weak selection and different update rules; these are not the strong best-earner imitation law considered here. Liu and Masuda (2023) study fixation on hypergraphs under *constant type fitness*, using birth--death edge-wide reproduction and a majority-constrained variant; these are also different mechanisms from comparing actual public-goods payoffs and updating a single selected player. Their exact Markov count reductions on complete hypergraphs are credited as structurally analogous, but their state changes and type fitness do not imply the present payoff-incidence equivalence or Fano strong-update conclusion.

The balanced incomplete block design concept and pair-incidence counting, harmonic identities, and geometric waiting-time calculus are classical mathematical tools. Novelty is claimed only for their combined exact implication for this specified stochastic public-goods imitation mechanism and the sharp geometric non-lumpability boundary witness, subject to historical-priority risk.

## Limitations

This theorem does not cover heterogeneous player degrees, nonconstant payoffs across edges, mutations, game-state transitions, Fermi/pairwise imitation updates, or arbitrary network protocols. Exact cooperator-count Markov formulas require the complete uniform hypergraph; the Fano example shows why one cannot extrapolate these formulas to all designs. The claimed direction of fixation does not imply a common fixation-time law for all balanced designs. The asymptotic is in elementary single-player updates with fixed group order and fixed normalized synergy above one; it does not hold uniformly as synergy approaches the threshold or as group size grows with population size. The theorem was reviewed within its own proof and exact checks; no independent external scientific audit or comprehensive exhaustive historical-priority audit has been performed.

## References

1. N. Wei, X. Xiong, Q. Li, M. Feng, A. Szolnoki, *Cooperation in Public Goods Games over Uniform Random Hypergraphs with Game Transitions*, arXiv:2603.22967 (first public version March 24, 2026); *Journal of the Royal Society Interface* 23 (2026), DOI: 10.1098/rsif.2025.1319.
2. U. Alvarez-Rodriguez, F. Battiston, G. F. de Arruda, Y. Moreno, M. Perc, V. Latora, *Evolutionary dynamics of higher-order interactions in social networks*, arXiv:2001.10313; *Nature Human Behaviour* 5 (2021), 586–595, DOI: 10.1038/s41562-020-01024-1.
3. C. Wang and Q. Su, *Public goods games on any population structure*, *Science Advances* 12 (2026), eaeb1263, DOI: 10.1126/sciadv.aeb1263; earlier public version arXiv:2411.00398.

4. R. Liu and N. Masuda, *Fixation dynamics on hypergraphs*, arXiv:2301.05343; *PLOS Computational Biology* 19 (2023), e1011494, DOI: 10.1371/journal.pcbi.1011494.
