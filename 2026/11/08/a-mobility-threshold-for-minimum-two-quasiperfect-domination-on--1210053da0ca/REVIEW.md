# Scientific review

## Correctness — PASS

The full proof starts with the outside-square equation \(1\le r_i+c_j\le2\). An empty row and an empty column would contradict domination, giving the sharp lower bound. At optimum all-row or all-column occupancy is forced; the only allowed large fiber has size \(m\), yielding the two rectangular families and the three square families. Exact intersections prove all isolated configurations. On injection states the one-square graph is the standard arrangement graph, and a dependency-digraph argument proves the exact distance \(t+c\). Independent finite implementations check the claims on explicitly stated ranges. No finite check is treated as an infinite proof.

## Originality — PASS, with limits

The closest [1,2]-set papers are Chellali et al. (2013), which explicitly discusses the two-row product example, and Cáceres et al. (preprint 2014, journal 2017), whose claw-free theorem implies the minimum cardinality but not the listed optimum-set classification or exchange graph. Separately, Day and Tripathi (1992) introduced arrangement graphs and their properties: the known arrangement-graph degree and diameter are not claimed as new, only their identification as the mobile sector of this dominating-set reconfiguration space. The claim excludes the covered two-row case and does not claim a new numerical minimum. Complete statement-level comparison, not just title matching, distinguishes the proposed configuration-space theorem from the cited general existence theorem. Relevant searchable mathematical records and closest archived claims showed no equivalent complete theorem. Historical priority is not independently certified; unindexed work remains a risk.

## Value — PASS

The phenomenon is structural: for every rectangular board of short side at least three, the optimum placements split into exactly \(n\) immobile configurations and a connected, explicitly quantified nonattacking-rook sector. The square boundary has no legal move at all. This exact mobility transition is not specified by knowing the classical minimum domination number or the existence of a quasiperfect optimum. The pre-existing arrangement-graph diameter becomes the exact relocation cost only because of the new isomorphism; this carries operational information beyond optimum cardinality.

## Relevant comparisons and scope

The 2013 paper's \(K_p\square K_2\) example is a covered boundary, excluded from the theorem. The 2014/2017 claw-free theorem covers \(\gamma_{1,2}=\gamma\), not optimum-set multiplicities or reconfiguration distances. Day–Tripathi arrangement-graph properties apply only after identifying the optimum-state graph; prior graph-theoretic results on that network do not identify it with quasiperfect rook placements. Related studies of identifying codes, total domination or Roman domination on rook graphs impose different constraints and do not imply the stated classification. Inaccessible or unindexed historical work remains a priority risk. The proof and two programs are included and self-contained.

Self-review: passed. Independent audit: not yet performed.
