# Scientific review

## Correctness

PASS. The one-clique update is obtained directly from \(k-z\) and \(k-u+v\) neighbor-one counts, so the proof covers every possible initial configuration and includes lazy ties. For odd \(m\), each clique becomes uniform by the second step and the exceptional weak-majority cases are counted by inclusion-exclusion. For even \(m\), the balanced/unbalanced dichotomy gives exhaustive first-entry cases with exact multiplicities. The \(m=2\) exception is handled separately. Exhaustive microscopic verification covers all \(349520\) labelled states on sizes \(2\) through \(9\), independently confirming the entry-time histograms, orbit counts and basin exclusion. Finite checks do not substitute for the all-size proof.

## Originality

PASS with historical-equivalence risk. The closest directly inspected primary work on deterministic majority (Kaaser–Mallmann-Trenn–Natale, arXiv:1508.03519v1, especially definitions, Section 3 and appendices) gives period-two convergence and general upper bounds but not a barbell-specific exact time histogram or bridge-locked orbit census. Benjamini et al., arXiv:1405.2486, give broad eventual-period results and random-graph questions, not the stated formula. Masuda, arXiv:1403.4763, examines the same broad two-clique topology but uses stochastic link-based copying rather than synchronous majority. The classic Goles–Olivos period theorem is strictly weaker. A related census on matching-coupled cliques cannot be transferred by edge deletion: the neighbor majorities and bridge constraints differ. No exact matching public statement was located, but incomplete historical indexing remains a risk.

## Mathematical value

PASS. A natural minimal bridge between two densely internally connected communities generates a parity bifurcation: odd cliques always settle, whereas even cliques support a large, exactly enumerable synchronized two-cycle class. Unlike a mere period upper bound, the theorem resolves the entire finite-time basin distribution, proves nonperiodic states cannot feed that oscillatory class, and identifies a sharp four-step exceptional delay. It also distinguishes order \(m^{-1}\) recurrent oscillation probability from order \(m^{-1/2}\) maximal-delay probability in uniform initial states. These are intrinsic dynamical invariants of a standard modular network, not arbitrary sampled parameters.

## Sources and limits

Primary sources: Goles–Olivos (1980); Kaaser–Mallmann-Trenn–Natale (2015, full HTML inspected); Benjamini et al. (2014, accessible text inspected); Masuda (2014, full preprint text inspected). Direct independent scholarly validation remains outstanding. All claims apply only to equal cliques with a single bridge, synchronous lazy-tie majority, and labelled states.

Self-review: passed. Independent audit: not yet performed.
