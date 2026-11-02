# Self-review of strict-core partitions on degree-two friendship networks

## Correctness — PASS

The theorem fixes each quantifier: every finite simple graph of maximum degree at most two, every integer capacity \(k\ge1\), every coalition partition with groups of size at most \(k\), and every possible deviating coalition obeying the same capacity. Utility is the number of graph neighbors in a coalition. The full proof first reduces deviations to connected pieces without changing utilities, then forces components of size at most \(k\) to remain whole and forces every run in a larger path/cycle to have exactly \(k\) vertices. The proposed full-run tilings are immune to weak blockers: a strictly improved endpoint would force an entire \(k\)-vertex run plus an outside vertex into a deviation. The count separates the \(k\) cyclic phases of each large cycle from unrestricted capacity-respecting unions of labeled small components. The latter obey a directly derived weighted set-partition exponential formula. Capacity \(k=1\), the case \(k=2\), isolated vertices, and components of order exactly \(k\) are addressed explicitly.

The packaged standard-library verifier enumerates all graph isomorphism types of maximum degree two through eight vertices, every admissible partition, and every weak blocker for capacities one through five where applicable. It passed 570 instances and 614,381 partition checks. This finite test is corroborating evidence, not an infinite-family proof. Residual scientific risks include inadvertent preference-model changes if the unit-edge assumption is relaxed and ordinary/strict-core convention confusion; these are excluded in the theorem statement.

## Originality — PASS with residual priority uncertainty

Levinger, Hazon, Simola, and Azaria (arXiv:2306.01378, initial public posting 2 June 2023, Sections 3 and 5.2 and Appendix A.5) supply the bounded-size coalition framework, complexity results, and a complete-graph strict-core obstruction. Their stated results do not imply the exact order-divisibility criterion on degree-two networks or the classification/count of all stable partitions. Igarashi and Elkind (AAMAS 2016, Sections 2, 3, 5.2) consider graph-restricted communication and path/tree strict-core examples under a different connected-coalition feasibility regime and more general preferences; they do not supply the cardinality-bounded unit-friendship classification. Hanaka, Köhler, and Lampis (arXiv:2402.10815v1, Sections 2 and 5) study ordinary-core conditions and deviations limited in size, not the present strict-core plus full coalition-capacity requirements. A related 2023 paper on friends, enemies, and neutrals was available only at abstract level and is not asserted to be uncovered in its full text. Literature searches for aliases, capacity restrictions, path/cycle equilibrium enumeration, and small-component partitions revealed no identified stronger statement. This is a best-knowledge priority assessment, not a proof of worldwide uniqueness.

## Mathematical value — PASS

A natural social-network boundary is classified completely rather than illustrated by an arbitrary instance. For uniform positive-friendship utilities, one can decide whether a strictly core-stable allocation exists in linear time, construct one, classify *every* allocation, and count them by a closed multivariate expression. The formula distinguishes large-cycle rotations from small-community mergers and exposes a sparse path obstruction already at \(k+1\) agents. These properties provide exact baseline cases and structural limits for capacity-bounded coalition formation; no claims are made about general trees or weighted agents.

## Scope and remaining uncertainty

The combinatorial classification is proved only for maximum degree two, symmetric unit friendship weights, and weak blockers with both current and deviating coalitions size-restricted. Counting is formulaic, not asserted polynomial in variable capacity. Searches may miss equivalent terminology or earlier exact counts; no independent external validation was performed.

Self-review: passed. Independent audit: not yet performed.
