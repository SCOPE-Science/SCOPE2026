# Scientific review

## Correctness: PASS

The all-length derivation proves strict stability of the absorbing path generator, establishes uniqueness of the continuous Lyapunov solution, and verifies the displayed parity-dependent matrix entry by entry through path-neighbor cancellation. The initial-state formula and unique loss optimum follow from the diagonal. Rational arithmetic checks validate 7,475 explicit matrix entries; independent complex Lyapunov solvers compare 110 full matrices and 1,375 diagonal values. The proof, not the bounded tests, supports the claim for all integers \(n\ge2\) and all \(\gamma>0\). A full absorption-time *distribution* is not established.

## Originality: PASS relative to searched records, with documented risk

Comparisons addressed the Poisson measurement model of Varbanov–Krovi–Brun (arXiv:0803.3446), stroboscopic renewal detection of Friedman–Kessler–Barkai (arXiv:1603.02046), imaginary-impurity lattice scattering of Burke–Wiersig–Haque (arXiv:1910.07439), and semi-infinite absorbing walks (arXiv:2605.08056). None of the inspected full texts was found to state, or provide without an additional nontrivial specialization, the same explicit finite-path survival matrix and positional optimum. Related work on localized loss by Wiersig (doi:10.1103/PhysRevA.98.052105) was available only in abstract and remains a priority risk. General Lyapunov and Zeno principles are acknowledged as known; originality is attributed solely to the new closed expression and optimization. Relevant prior result-record searches and accessible local claims likewise did not identify coverage. Non-detection is not proof of global priority.

## Mathematical value: PASS

A finite quantum transport process that is completely absorbing nevertheless has a counterintuitive nonmonotone *mean* lifetime for sources away from the sink. The result determines the entire operator for arbitrary coherent sources—not merely one numerical lifetime—and shows a position-only optimal loss that is invariant under extending the far end of the chain. These exact facts connect trapping efficiency, coherent transport, boundary geometry and the quantum Zeno regime, without presupposing a broader theorem.

## Risks and bounds

The sink must be at an endpoint, the path finite and unweighted, and the Hamiltonian the adjacency matrix. The finding does not claim novelty of the Lyapunov technique or historical priority under inaccessible full text; it does not address other measurement conventions or disorder.

Self-review: passed. Independent audit: not yet performed.
