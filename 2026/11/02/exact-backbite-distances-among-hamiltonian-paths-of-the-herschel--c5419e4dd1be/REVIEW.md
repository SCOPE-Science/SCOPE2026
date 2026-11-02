# Scientific review: exact Herschel backbite distances

## Correctness

**PASS.** The graph is given by a complete eleven-vertex adjacency rule, and the local backbite operation is explicit and reversible. The two methods agree on \(222\) reversal-identified Hamiltonian paths, \(444\) legal moves, connectivity, the all-source distance histogram, radius \(8\), diameter \(9\), the \(12\) disjoint extremal pairs, and endpoint-class totals. One verification builds paths by depth-first extension; the other exhausts all \(\binom{18}{10}=43758\) candidate edge sets, constructs edges by a different pairwise edge-set criterion, and checks the endpoint counts with a subset dynamic program. The proof explains why these finite searches are exhaustive and why the path-exchange condition is exactly a backbite. The explicit diameter witness is checked from a breadth-first distance-sphere certificate.

## Originality

**PASS, qualified.** The closest direct prior frameworks are the 2005 Oberdorf–Ferguson–Jacobsen–Kondev backbite sampling paper and Kazazi's 2026 Hamiltonian-path reconfiguration manuscript. The accessible text of the former studies square-lattice polymers, and the latter gives sufficient connectivity conditions and disconnected constructions, not an exact Herschel computation; its spanning-squared-path theorem is inapplicable to this bipartite graph. The Herschel graph's classical definition and traceability are known. Targeted searches for the graph name together with backbite, path rotation, \(222\), and exact metric quantities did not reveal the claimed classification. The closest indexed research result on the Herschel graph concerns its independence complex and does not imply a Hamiltonian-path reconfiguration metric. Unindexed historical calculations remain a residual risk; failure to locate one is not proof of absolute priority.

## Value

**PASS.** The Herschel graph is the smallest non-Hamiltonian polyhedral graph, so its entire spanning-path configuration space is a canonical sparse, three-connected test case for backbite connectivity outside dense/squared-path hypotheses. The sharp nine-move conversion bound, all-pair distances, endpoint classification, and matching of extremal pairs are exact properties needed to understand and benchmark this natural local move, rather than an arbitrary parameter slice. The result does not claim a general mixing-time theorem or other downstream consequence.

## Verification limits

The result is finite and exhaustive rather than an infinite-family theorem. The computational programs themselves, complete within the same package, must be executed to reproduce the numerical claims. Historical source comparisons support a qualified originality judgment, not a guarantee of universal priority.

Self-review: passed. Independent audit: not yet performed.
