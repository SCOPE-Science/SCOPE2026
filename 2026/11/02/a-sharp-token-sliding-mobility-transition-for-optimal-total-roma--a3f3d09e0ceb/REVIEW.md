# Self-review

## Correctness — PASS

The stated range is \(k\ge2\), \(n\ge k(k+1)\). The proof independently characterizes minimum total Roman functions by excluding every possible number of label-\(2\) vertices other than \(k+1\). It then counts disjoint block configurations, derives every slide degree from the unused pool, proves the partition invariant at the sharp boundary, and proves connectivity above the boundary by (i) transpositions between occupied and unused elements using an intermediate unused block and (ii) a direct connectivity argument for \(K(N,k)\) when \(N\ge2k+1\). These steps handle both equality thresholds and the smallest case \(k=2\). The standalone verifier directly checks the original Roman condition, transition graph, components and degrees for small parameters; it executed to `VERIFY_OK` from the actual packaged file. Finite tests support but do not replace the general proof.

## Originality — PASS, subject to publication-priority uncertainty

Zec and Grbić (arXiv:2204.05664, Section 2.1) establish the minimum total Roman weight and construct disjoint optimal defender blocks. Brešar and collaborators (arXiv:2312.15464, Section 3) treat neighboring Kneser multiple-domination optimization problems. Neither provides the component trichotomy for sliding between optimal Roman labelings. Bousquet and collaborators (arXiv:1812.05419) concern matching token jumping, not adjacency-restricted Kneser token sliding. Lam, Phan and Hoang (arXiv:2506.07821, Sections 1–4) establish a framework and general structural results for clique reconfiguration but do not specialize to this sharp Kneser component transition. Matching graphs by Eroh and Schultz (1998) is related through a different move relation; only its abstract was inspected, so a previously unindexed or differently named analogue remains a residual priority risk. Actual semantic record searches returned no statement implying the trichotomy. A negative search is not proof of novelty.

## Mathematical value — PASS

The natural space of minimum Roman defenses has an exact and sharp mobility threshold, not implied by its pre-existing minimum weight or the number of optimal placements. At one boundary every defense is immobilized; at the next, the space splits into nontrivial complete components indexed by equal-block partitions; one extra available ground element connects all defenses. The result also gives exact labeled configuration, component and transition counts throughout the entire parameter domain. This supports structural study of optimal domination reconfiguration without inventing a downstream application.

## Limitations and closest prior results

The proof does not describe shortest slide distances or the spectrum of nonminimum Roman labelings. Priority uncertainty remains for older matching-graph studies and unindexed clique/partition reconfiguration literature. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
