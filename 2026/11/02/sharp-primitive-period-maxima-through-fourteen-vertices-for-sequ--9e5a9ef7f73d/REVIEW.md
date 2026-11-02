# Self-review

## Correctness — PASS

The update uses the closed-neighborhood \((1,3)\) convention, with a current one preserved exactly when at least two *other* neighbors are one. The proof reduces scan-order variability by the established cycle-equivalence theorem for tree sequential dynamical systems. The exhaustive leaf-augmentation generator supplies every unlabelled tree through order \(14\), with AHU canonical deduplication and class counts \((1,1,1,2,3,6,11,23,47,106,235,551,1301,3159)\). The exact functional-graph traversal checks every one of the \(2^n\) configurations for all \(5447\) trees. The maximal-period table is crosschecked by an alternative Python indegree-pruning algorithm through order \(12\), a separate tree-generator comparison at order \(14\), and an independent direct \(106\)-step witness replay. No claim is made about order greater than \(14\). Remaining risks: finite-search implementation defects, mitigated by algorithmic and code-level crosschecks; the imported published click-equivalence result must be interpreted for fixed local rules.

## Originality — PASS, qualified

Macauley–Mortveit (arXiv:0802.4412) provides order-equivalence of periodic behavior, not maximal period over all tree shapes. Kuhlman–Mortveit–Murrugarra–Kumar (arXiv:1108.2974) exhibits long cycles using structured tree families, including an explicit \(3p-2\)-vertex realization, but does not prove the present minimal-order and bounded-tree-maximality results. Later GDSCalc work (2015) examines certain designated tree families. Targeted research-record and literature searches found no matching table or stronger result implying it. Residual risk: independently reported equivalent finite tables in unindexed literature or data sets.

## Mathematical value — PASS

The maximum least period over all fixed-order trees is the natural extremal answer to the earlier large-period-existence question. Exhaustive optimality at fourteen vertices, a primitive \(106\)-orbit on a concrete small tree, and exact minimum-size thresholds for several long periods are substantial nontrivial finite dynamical facts. This is not a generic enumeration of arbitrary slices: tree order, period, and the fixed bi-threshold rule are the canonical parameters in the cited problem, and the new optimum sharpens the size required by a known explicit construction.

Self-review: passed. Independent audit: not yet performed.
