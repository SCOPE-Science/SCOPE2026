# Self-review

## Correctness (PASS)

The exact domain is any nonempty complete-bipartite graph and arbitrary initial strategy/game labels under independent fair coordinate copying from one common sampled neighbor. The six-category backward pair-chain construction, nontrivial transition rates, full stationarity equations, normalization, singleton-part cases and absorption-to-stationarity limit are proved in RESULT.md. Complete forward-state absorption calculations independently matched 3,648 terminal-pair probabilities on six small graphs; 196 exact-rational parameter instances checked the six weights. The proof covers all positive integer part sizes; finite tests are supporting evidence, not an infinite proof. The original source's update rule is verified at \(w=0\), \(p_s=p_g=1\) from equations (10)–(11). Risk: none identified within these exact hypotheses, though an independent mathematical audit has not occurred.

## Originality (PASS, with priority risk)

The closest primary source, Sadekar et al. (arXiv:2311.11128v1, 2023), is read across its model and results sections: it specifies the mechanism and investigates selective and quasi-stationary cooperative behavior rather than computing this unconditional two-coordinate, topology-specific joint fixation law. Standard voter ancestry (Aldous–Fill, section 14.3) derives single-coordinate coalescence, but the two coordinate ancestors here can split after meeting. The multi-locus Moran/Wright–Fisher theory of Bhaskar–Song (2009) works with random mating, mutation, and genetic matching rather than a fixed complete-bipartite social graph and arbitrary initial label assignments. Artime et al. (2017) use different multilayer coupling plus ageing. Targeted literature and semantic research-index searches considered alias formulations (shared-donor two-locus linkage, coupled voter-model consensus, pair genealogy) without identifying a result whose hypotheses and conclusion imply the displayed \(K_{a,b}\) law. Residual risk: a specialized, unindexed coupled-copying theorem might already contain it; absence in search is not proof of novelty.

## Mathematical value (PASS)

The motivating model attributes network-dependent strategy/game association to coevolutionary dynamics. The theorem supplies a nonselective, exact finite-population control: a persistent correlation of \(1/5\) in the extreme hub example, contrasting with a vanishing ancestral linkage in balanced bicliques. It gives all joint terminal-label probabilities, not just a simple expectation, and pinpoints a structural graph boundary. This is a useful analytical diagnostic for separating inheritance geometry from selective feedback, while explicitly not extending terminal calculations to quasi-stationary distributions. The result is a motivated graph-wide classification, not an arbitrary numerical slice.

## Scientific scope and prior-work limitations

Exact neutrality, a uniformly selected focal and neighbor, equal independent adoption probabilities one half, complete bipartite topology, no mutation. The question is distinct from positive-selection behavior and nonabsorption-conditioned statistics. Citations and research-priority limitations are in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
