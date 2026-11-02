# Exact reversibility criterion and a finite nonequilibrium witness for Bell-matching measurement dynamics

## Finding

A stochastic matching chain induced by single-site and Bell-pair measurements is reversible **if and only if** the reciprocal pair-sampling weights are sums of vertex potentials. This completely classifies the equilibrium sector among all positive, state-independent pair-sampling laws and gives an exact product-form stationary distribution there. For the distance-weighted open-chain protocol, every positive distance exponent produces an explicit nonzero five-transition cycle affinity, already on four consecutive sites.

**Theorem.** Fix an integer \(N\ge4\), a probability \(0<p<1\), and strictly positive symmetric weights \(w_{ij}=w_{ji}>0\), \(1\le i<j\le N\). Put \(W=\sum_{i<j}w_{ij}\). On partial matchings of the complete graph, choose at every step a uniformly random vertex and erase its incident edge with probability \(p\), or choose an unordered pair with probability \((1-p)w_{ij}/W\) and perform the Bell-matching update described below. The finite irreducible chain is reversible exactly when there exist real numbers \(v_1,\ldots,v_N\), with \(v_i+v_j>0\), such that
\[
\boxed{w_{ij}^{-1}=v_i+v_j\quad\text{for every }i<j.}
\]
Equivalently, for every four distinct indices \(a,b,c,d\),
\[
\boxed{w_{ab}^{-1}+w_{cd}^{-1}
=w_{ac}^{-1}+w_{bd}^{-1}
=w_{ad}^{-1}+w_{bc}^{-1}.}
\]
In exactly these reversible cases, the unique stationary measure is
\[
\boxed{\pi(M)=\frac1Z\prod_{\{i,j\}\in M}
\frac{N(1-p)w_{ij}}{2pW},\qquad
Z=\sum_{M}\prod_{\{i,j\}\in M}\frac{N(1-p)w_{ij}}{2pW}.}
\]

For open-chain distance weights \(w_{ij}=|i-j|^{-\alpha}\), \(\alpha\ge0\), reversibility occurs **exactly at \(\alpha=0\)**. On any four consecutive vertices, the forward/reverse product of transition probabilities around the five-state cycle defined in the proof is
\[
\boxed{R=2^{-\alpha},\qquad\log R=-\alpha\log 2.}
\]
This ratio is independent of \(N\) and \(p\). It is the orientation-specific Kolmogorov cycle ratio, not the total stationary entropy-production rate.

## Assumptions and scope

A partial matching is any set of disjoint unordered vertex pairs; unmatched vertices are allowed. For Bell selection of \(i,j\), if they are paired to one another nothing changes. Otherwise erase their existing incident edges, if present, add \(\{i,j\}\), and, if both had distinct former partners, also pair those two partners. If exactly one had a former partner, that partner becomes unmatched. These are the outcome-independent matching rules of the measurement-only Bell-pair model. Site measurement at vertex \(i\) erases its incident edge, or does nothing if unmatched.

The pair weights are prescribed independently of the current matching. All measurement outcomes are ignored because they alter Bell labels but not the matching. No claim is made for the full trajectory state including measurement labels. The theorem concerns the complete finite matching-state space, not only the states reached before mixing from an initial empty matching.

## Proof

**Irreducibility and positivity.** Each existing edge can be erased by measuring either endpoint, with positive probability. Any target matching can then be built by Bell-measuring its disjoint edges one by one. Consequently the chain is irreducible and has a unique strictly positive stationary measure. Its empty state has a positive self-transition, so the chain is also aperiodic.

Write
\[
b_{ij}=\frac{(1-p)w_{ij}}{W},\qquad d=\frac{2p}{N},\qquad z_{ij}=\frac{b_{ij}}d.
\]
Whenever \(i,j\) are unmatched, the only direct move adding \(\{i,j\}\) has probability \(b_{ij}\), and the reverse move deleting that edge has probability \(d\). If the chain is reversible, detailed balance on such an edge-addition transition requires \(\pi(M\cup\{i,j\})/\pi(M)=z_{ij}\). Constructing every matching from the empty matching proves that **any reversible measure must be** \(Z^{-1}\prod_{e\in M}z_e\).

It remains to check the other elementary moves. When a Bell measurement replaces a single edge \(\{a,c\}\) by \(\{a,b\}\), leaving the previous partner \(c\) unmatched, the forward and reverse probabilities are \(b_{ab}\) and \(b_{ac}\). Their detailed-balance ratio agrees identically with the proposed product weights, because \(z_{ac}b_{ab}=z_{ab}b_{ac}\).

A transition from two edges \(\{a,c\},\{b,d\}\) to \(\{a,b\},\{c,d\}\) occurs upon Bell measurement of either \(\{a,b\}\) or \(\{c,d\}\); its probability is \(b_{ab}+b_{cd}\). The reverse probability is \(b_{ac}+b_{bd}\). Product-form detailed balance is therefore equivalent to
\[
 z_{ac}z_{bd}(b_{ab}+b_{cd})
 =z_{ab}z_{cd}(b_{ac}+b_{bd}),
\]
which, after division by the product of the four strictly positive \(b\)'s, is precisely
\[
 b_{ab}^{-1}+b_{cd}^{-1}=b_{ac}^{-1}+b_{bd}^{-1}.
\]
The common normalization connecting \(b\) to \(w\) cancels. All distinct-index choices and the third pairing of a quadruple give the complete three-way four-point identity. No other off-diagonal transitions exist: site moves delete one edge, and Bell moves add an edge, replace one edge, or reconnect two edges. Thus the four-point identity is both necessary and sufficient for full detailed balance and the stated stationary law.

**Vertex-potential equivalence.** Put \(r_{ij}=1/w_{ij}\). An additive representation \(r_{ij}=v_i+v_j\) immediately implies the four-point identities. Conversely, given the identities choose
\[
v_1=\frac{r_{12}+r_{13}-r_{23}}2,\quad
v_2=\frac{r_{12}+r_{23}-r_{13}}2,\quad
v_3=\frac{r_{13}+r_{23}-r_{12}}2,
\]
and \(v_i=r_{1i}-v_1\) for every \(i\ge4\). The quadruple identities involving \(1,2,3,i\) give \(r_{2i}=v_2+v_i\) and \(r_{3i}=v_3+v_i\); identities involving \(1,2,i,j\) then give \(r_{ij}=v_i+v_j\) for all \(i,j\ge4\). Since every \(r_{ij}>0\), all required pair sums are positive even when an individual potential is negative.

**Finite cycle witness.** Let \(a,b,c,d\) be four distinct sites, with all other vertices left unmatched throughout. Traverse the states
\[
\varnothing\longrightarrow
\{ac\}\longrightarrow
\{ac,bd\}\longrightarrow
\{ab,cd\}\longrightarrow
\{ab\}\longrightarrow\varnothing,
\]
where \(ac\) abbreviates the unordered edge \(\{a,c\}\). The forward and reverse products are positive and their ratio is
\[
 R_{a,b,c,d}=
 \frac{b_{ac}b_{bd}(b_{ab}+b_{cd})}{b_{ab}b_{cd}(b_{ac}+b_{bd})}
 =\frac{w_{ab}^{-1}+w_{cd}^{-1}}{w_{ac}^{-1}+w_{bd}^{-1}}.
\]
The two deletion probabilities \(d\) cancel. This also gives an elementary necessity proof by Kolmogorov's cycle criterion. For consecutive \(a,b,c,d\) in increasing order and \(w_{ij}=|i-j|^{-\alpha}\), the four edges used in this cycle have respective distances \(1,1,2,2\); hence \(R=2^{-\alpha}\). For every \(\alpha>0\) this ratio is not one and the chain is not reversible. At \(\alpha=0\), all weights are uniform and the additive criterion holds, completing the classification.

## Verification

The standalone `verify_matching_chain.py` constructs every partial matching and transition probability using exact rational arithmetic, directly from the update rules rather than from the detailed-balance formulas. It checks normalization and detailed-balance identities for \(N=4,5,6\), including vertex-additive weights with positive or signed potentials and distance weights at exponents one and two. In the nonadditive cases the exact cycle ratios equal \(1/2\) and \(1/4\), respectively. The finite-state calculations are independent finite checks; the universal all-\(N\), all-positive-weight conclusions are proved above.

For uniform weights, the formula specializes to common edge activity \(z=(1-p)/(p(N-1))\). Thus the exact finite matching-size law is \(\Pr\{|M|=k\}\propto\frac{N!}{(N-2k)!2^k k!}z^k\), for \(0\le k\le\lfloor N/2\rfloor\); this established type of monomer–dimer combinatorics is not independently claimed as a novelty.

## Relationship to prior work

Holdhusen, McAmis, and Rahmani introduced the measurement-only Bell-matching dynamics and studied its entanglement regimes, including uniform sampling and power-law sampling. Their main text and supplementary combinatorial analysis provide matching update rules and a uniform-pairing entropy calculation, but not the all-weight detailed-balance classification or explicit nonzero finite Kolmogorov affinity established here. The uniform combinatorial sector is **acknowledged prior modeling**, not presented as a new matching representation.

The product-form measure belongs to the established monomer–dimer Gibbs family studied by Heilmann and Lieb; the new issue is the **necessary-and-sufficient sampling-law condition under the specified Bell-reconnection dynamics**, not the existence of matching partition functions. Kolmogorov's cycle criterion is classical and is used, rather than claimed, in proving the explicit obstruction. A general detailed-balance or matching-process theorem not identified in the inspected literature may subsume this specialization.

## Limitations

Only finite, positive-weight, state-independent, outcome-averaged matching chains with \(0<p<1\) are considered. For vanishing weights or endpoint protocols \(p=0,1\), irreducibility can fail and the theorem does not apply without modification. Nonreversibility of the matching process is not a quantitative result about the full quantum channel, physical heat, or thermodynamic-limit entropy scaling. The explicit cycle affinity does not determine the stationary entropy-production rate. Literature-wide priority remains subject to specialist comparison, particularly with general stochastic-matching dynamics.

## References

1. W. Holdhusen, B. M. McAmis, and A. Rahmani, *Classical Cellular Automaton for Measurement-Only Entanglement Transitions*, arXiv:2609.28743 (first submitted 2026-09-23; v2 2026-10-14), https://arxiv.org/html/2609.28743v2 . The main text and supplemental Sections I–III were inspected for the matching dynamics and prior combinatorics.
2. O. J. Heilmann and E. H. Lieb, *Theory of monomer-dimer systems*, Communications in Mathematical Physics **25** (1972), 190–232, https://doi.org/10.1007/BF01877590 .
3. F. P. Kelly, *Reversibility and Stochastic Networks*, Wiley (1979), ch. 1, for general Markov-chain reversibility and cycle criteria; see also the accessible account in *A Tutorial on the Spectral Theory of Markov Chains* (2023), https://doi.org/10.1162/neco_a_01611 .
