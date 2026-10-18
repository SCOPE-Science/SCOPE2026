# Mathematical review

## Correctness — PASS

The graph convention and full face predicate agree with the stated bidirectional multipath definition. The finite verifier constructs every face on \(8,10,12\) oriented arc vertices and gives an explicit matching plus complete directed-Hasse acyclicity certificate for each. The reductions have one ordinary critical zero-cell and respectively \((3\text{ in degree }1,2\text{ in degree }2)\), \((1\text{ in degree }2,2\text{ in degree }3)\), and \((1\text{ in degree }2,2\text{ in degree }4)\). The four-vertex case has exactly two tetrahedral boundaries connected by four edges. For the other two, the consistently oriented cycle boundaries generate both top homology summands. The five-vertex attaching degrees therefore vanish. The six-vertex integral two-cocycle has mod-two nontrivial class and literally zero Alexander–Whitney square; the free top cohomology forces both Hopf invariants to vanish. The exact certificate enumerates all relevant faces, checks every Hasse arrow and tests every coboundary and cup-square evaluation; no infinite inference from sample computation is made.

## Originality — PASS (subject to literature-coverage risk)

Caputi–Collari–Smith (arXiv:2601.05670v1, 9 January 2026) give homology for all bidirectional cycles but explicitly state their homotopy wedge conjecture as open, including at the end of Section 3. These homology groups do not resolve the potential Hopf map in the six-vertex case. Caputi–Collari–Di Trani–Smith (Mathematika 2024, e12235, Section 4.2) restrict their polygon theorem to directed polygons without bidirectional edges, so cannot imply the present classification. A separate mathematical-record search for bidirectional multipath homotopy types, cycle-free chessboard reductions, equivalences and attaching maps revealed no result implying this exact three-case wedge decomposition. Unindexed/unpublished equivalent proofs remain possible; the comparison is not a universal novelty certificate.

## Value — PASS

This resolves the first three nontrivial instances of a specifically published homotopy-type conjecture, rather than merely repeating already computed Betti numbers. For the six-vertex cycle, homology and the discrete-Morse cell counts allow nontrivial \(\pi_3(S^2)\)-attaching maps; the new explicit integral cup-square obstruction calculation is needed to show they vanish. The result offers a reproducible combinatorial and unstable-homotopy benchmark for any proposed uniform approach. The limited three-case scope is intentional and does not claim a general formula.

## Scope and risks

Only the three labeled finite complexes are classified; a later graph order can involve other unstable torsion obstructions. No equivariant statement or general shellability assertion is made. Unindexed equivalent work remains a residual originality risk. The supplied verifier is exhaustive for these three finite graph orders and uses only the Python standard library.

Self-review: passed. Independent audit: not yet performed.
