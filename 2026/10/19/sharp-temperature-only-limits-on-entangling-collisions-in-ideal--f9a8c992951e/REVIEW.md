# Scientific assessment: sharp thermal entangling-collision horizon

## Correctness — PASS

Two independently defined ideal pairwise collision unitaries preserve diagonal target populations. Matrix multiplication gives the exact target recurrence and a two-qubit X-state. Its partial transpose contains a single potentially negative two-by-two block whose determinant reduces to the explicit quadratic \(F(z)\). Its unique positive root proves the exact collision count, and elementary global logarithmic bounds yield the coupling-independent sharp cap. The approach-to-identity limit proves optimality *over nonzero couplings*, not at zero coupling itself. A standalone 4-by-4 implementation with exact-rational sign tests passed 1302 assertions. The proof, rather than finite testing, establishes the universal parameters and integer endpoints.

## Originality — PASS, with identified risk

The 2026 source studies both two-qubit gates, their target thermalization, and numerical transient system–ancilla negativity. Those ingredients are excluded from the novelty claim. The assessed extension is the exact entanglement cut-off in collision index, its sharp temperature-only maximum over every nontrivial gate angle, and the contrast between two exchange structures. The different ancilla–ancilla-memory and network-entanglement collision models do not imply a sharp bound for the present pre-reset *target–fresh-ancilla* entanglement observable. A separate section of the motivating source's supplemental material was inaccessible for independent full-document assessment, and more general entanglement-breaking-index or collision-channel results could subsume the calculation. No exhaustive uniqueness certification is asserted.

## Value — PASS

The number of collisions during which a bath qubit becomes entangled with a battery target is an observable resource window, not an arbitrary parameter slice. The exact answer distinguishes ordinary and anti-thermalizing gates even though both reduce the target's population error by the same factor each cycle. A universal two-event ordinary cap, an exponentially temperature-dependent sharp anti-thermal count cap, and the disparate fixed-angle and optimized low-temperature laws provide a substantive physical boundary and a guide to collision-selection experiments. The count is not misrepresented as entanglement magnitude or a device-independent resource.

## Closest work and limits

See Pal et al., arXiv:2609.04905v1 (main ideal-gate relations and transient negativity), Lalita–Banerjee arXiv:2506.23818v1 (non-Markovian two-system-qubit collisions), and Doğan et al. arXiv:2604.01773v1 (network-node entanglement). The theorem assumes fresh thermal ancillas, exact gates, no intercollision free rotations, and a ground-initialized target. No independent external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
