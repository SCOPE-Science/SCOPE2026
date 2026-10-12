# Review: arithmetic loss-pattern classification and survival plateaux

## Correctness — PASS

For every integer \(M\ge1\), nonempty even-sublattice loss set \(S\), and strictly positive alternating hoppings and loss rates, the clean Hamiltonian factors through a bidiagonal \(T\). The sine eigenvectors of \(TT^\dagger\) give a complete, simple nonzero-energy spectrum, while the A-only state is the unique zero mode. The simultaneous nodal congruences are exactly \(g\)-divisibility, yielding \(2g-1\) dark modes. The dissipativity identity characterizes *all* nondecaying modes, and the orthogonally reducing dark/complement decomposition validates the infinite-time limit. The roots-of-unity calculation supplies the exact two-case survival probability. The included finite-dimensional script checks 2,343 parameter-site configurations and explicit time evolution but is not needed for the general proof.

## Originality — PASS, with explicit risk

The closest inspected source, Wang–Zhang (arXiv:2607.10218v1), explains the dark-node mechanism for one loss in an even chain, not the arithmetic sparse-loss classification in odd chains. Yang–Molignini–Bergholtz (arXiv:2305.00031) gives the protected boundary mode and detailed first-B / all-B loss examples. Thiel and collaborators (doi:10.1103/PhysRevResearch.2.043107) establish general dark-state spectral projection ideas for repeated measurements. The new claim is not the underlying criterion, but its complete \(g\)-dependent mode count and rate-independent residue-class survival law, including extra bulk dark pairs absent from the specialized predecessors. Claim-specific semantic and published-literature searches found no equivalent claim. A differently indexed or implicit prior specialization may exist, so priority is not independently certified.

## Value — PASS

Sparse lossy-site placement is a concrete mathematical-physics control question. The theorem gives an exact criterion for eliminating every nonzero-frequency dark bulk mode, an exact count and energy list when this fails, and a sharp measurable distinction between source residue classes. For instance, in an 11-site chain with loss at \(k=2\), the B-source survival plateau is \(1/3\) on odd B-index positions and zero on even B-index positions, regardless of strictly positive loss rate. This structural all-size classification adds information beyond merely observing the topological boundary state.

## Scope and limitations

Only the one-particle/no-jump sector of ideal Markovian particle loss is proved. Coupling disorder, loss on A sites, gain, dephasing, and interacting fermions are outside scope; total survival probability may converge while individual coherent amplitudes oscillate. No quantitative lower bound on nonzero decay rates or global multi-particle mixing time is claimed.

Self-review: passed. Independent audit: not yet performed.
