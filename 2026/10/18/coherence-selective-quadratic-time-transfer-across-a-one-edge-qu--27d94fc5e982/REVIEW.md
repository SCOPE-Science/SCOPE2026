# Scientific review

## Correctness — PASS

The central estimate follows from an exact invariant subspace decomposition. Sum-zero nonbridge vectors are eigenvectors with eigenvalue \(-1/(n-1)\), proving the exact launch-state factorization. Reflection symmetry gives two real symmetric two-by-two matrices, each with only one top eigenvector carrying a squared nonbridge weight of at least \(1-n/(n-1)^2\). Eigenphase projectors therefore approximate the bright-to-right amplitude uniformly for **all** real times. Off-resonant bridge population contributes at most \(4n/(n-1)^2\). The resulting probability error is at most \(8n/(n-1)^2\), and the top even–odd splitting equals \(2n^{-2}+O(n^{-3})\). The scaling law, preparation criterion and first threshold-time limit follow by elementary compact-time uniform convergence and the dark upper bound. The standalone program gave 482 finite checks with an independent full-matrix construction; finite sampling is supporting evidence, not a substitute for the proof.

## Originality — PASS, with residual risk

The full normalized-adjacency barbell eigenspectrum, clique-supported dark modes, and qualitative slow leakage are already established by Dhamapurkar and Subrahmanyam (arXiv:2603.05643). We do not claim them. Their study centers on eigenstate and time-averaged inverse participation ratios and expressly does not establish transport performance bounds. The candidate result instead resolves all-time transfer for every coherent packet from the left nonbridge region, with a quantitative universal error, sharp preparation criterion, earliest high-probability arrival time, and a vertex-versus-uniform contrast. Duda and Wong (arXiv:2408.08244) treat weighted, oracle-driven search with a different Hamiltonian and are not a stronger statement about this unmarked model. Brown, Martin, and Wright (arXiv:2103.08837) describe **exact** group state transfer for adjacency walks; their inspected full-text theorem and examples do not treat the barbell packet transfer; our quantitative approximate opposite-clique population does not follow directly from that definition. Independent published-index similarity searches found nearby but non-dominating state-transfer results; absence of a result is not a novelty certificate. The old exact eigenspectrum, together with standard spectral perturbation, might make this transfer law an implicit consequence of broader prior theory. That is the principal residual originality risk.

## Value — PASS

The precise question is how a single-edge quantum bottleneck combines localization of individual vertices with coherent packet transport. The quantitative theorem reveals that the same graph can preserve **almost all** mass in a localized single-vertex launch yet transfer **almost all** mass in a prepared uniform launch, and it proves the transition occurs on the quadratic time scale. The state-preparation obstruction \(w(\psi)\) holds exactly at finite size; the time-uniform two-level error is independent of observation time. These are motivated transport diagnostics, not merely the restatement of an eigenvalue or a tiny numerical refinement.

## Literature relationships and limits

The source paper's exact spectral basis and dark modes remain credited as prior; a general two-level near-degeneracy theorem or unpublished packet analysis could imply the new statements. The fixed model excludes arbitrary bridge weights, nonuniform clique sizes, decoherence, oracle potentials, initial bridge-site amplitude, vertex-to-vertex perfect state transfer, and first-passage interpretation. Numerical tests address finitely many graph sizes and sample times; analytical bounds control the asserted infinite family.

Self-review: passed. Independent audit: not yet performed.
