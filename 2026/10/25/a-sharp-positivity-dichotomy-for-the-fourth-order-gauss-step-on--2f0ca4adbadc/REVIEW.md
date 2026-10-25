# Self-review

## Correctness — PASS

The proof fixes nonnegative conductances and the exact connectivity condition \(\tau>0\), derives the spectrum and Cayley–Hamilton identity, and obtains a polynomial quotient whose exact off-diagonal entries have quadratic sign polynomials. The positive-definite scalar Gauss stability function proves diagonal positivity and mass conservation. A single heavy edge is the only possible source of sign failure; its quadratic has exactly one positive root, giving the sharp closed threshold and proving nonreentry. The Green-kernel equivalence and two-site comparison follow from explicit matrix identities. The standalone symbolic and rational direct-inversion checks were replayed successfully. Finite matrices are corroboration, not proof of universal quantifiers.

## Originality — PASS, with residual risk

Actual public research-index searches compared three-site reversible Markov chains, weighted triangles and paths, [2/2] Padé rational integration, and endpoint positivity. The closest published finite-state Padé result establishes minimal dimension eight for **arbitrarily small-step** failure on possibly directed generators, not the present three-site **finite-step** classification. The reviewed full texts of Horváth (1998) and Zappavigna et al. (2012) concern broad scheme-wide positivity and general Metzler counterexamples; neither supplies the sharp graph-specific weight criterion. Gottlieb–Shu–Tadmor (2001) establishes general SSP context. Accessible earlier unweighted graph-specialization results cover cases of this theorem but not variable weights. As usual, specialized work not found or not inspected could affect novelty.

## Value — PASS

For the smallest nontrivial symmetric network, the theorem completely classifies unconditional versus finite-horizon positivity of a fourth-order A-stable integrator, identifies a structural conductance imbalance threshold and a Green-kernel interpretation, and determines the safe timestep without numerical sweeps. The failure occurs despite exact spectral stability at every positive step; a simple weighted-path witness establishes minimal state count, and the strong-edge asymptotic quantifies stiffness. These are natural finite-dimensional numerical-diffusion questions, not arbitrary numerical samples or a mere named substitution.

## Scope and unresolved issues

All proof statements hold for precisely three undirected sites with nonnegative symmetric conductances; nothing is asserted for stages, nonlinear dynamics, or higher dimensions. Novelty is assessed against the listed primary texts, a published finite-state comparison, mathematical record searches and accessible prior results. The scientific novelty of this exact classification requires independent literature review. An independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
