# Scientific review

## Correctness

PASS. The inclusion and antitonicity argument establishes \(F^3=F\) for the exact stated open-neighborhood operator. The output decomposition into empty-row/empty-column rectangle and isolated active rooks is a direct exhaustive case distinction. The residual realizability criterion \(\eta(p,q)\) is both necessary and sufficient, including the \((0,0)\), \((1,1)\), one-zero and boundary cases. Every nontrivial rectangle is intrinsically identifiable in the output as the unique nontrivial rook-graph component; the matching-only overlap is removed by the separate square-board exclusion. The fixed-state count follows from maximal nonattacking rook placements. The analytic two-row count treats the \(2\)-by-\(2\) overlap separately. Direct, independently implemented row/column checks examined 2,811,728 configurations across fifteen board sizes and established exact equality of predicted and observed recurrent sets as well as counts. Tests are corroborative, not the infinite proof.

## Originality

PASS, with historical-priority qualification. The closest antecedent is the standard fixed-point correspondence for negative conjunctive networks: it does not cover the full periodic-image classification or two-cycle census. The 2015 survey and 2020 parallel-Boolean literature give general period restrictions under different self-dependence conventions rather than this graph-specific exact census. Later MIS-network research focuses on sequential updates. Direct searches of the available research-record index and the accessible prior findings identified no implication that already gives the rectangle-plus-matching structure or exact \(Q_{a,b}\) formula. In particular the previous graph-join NOR result concerns \(G\vee H\) and does not specialize to \(K_a\square K_b\). Residual risk: an unindexed equivalent result using relation polarities, formal concepts, or Boolean closures could predate this formulation, and not every historical full text was accessible.

## Value

PASS. The theorem is a complete all-parameter classification of a natural graph Boolean dynamical system. It explains an exact, exceptional square-board hole in the recurrent partial-matching strata, gives an explicit finite binomial census over all rectangular boards, and yields the compact nontrivial family \(Q_{2,b}=2^b-1\). This resolves the orbit-number question left open by generic period-two bounds for this graph family, rather than merely restating that all orbits have period at most two.

## Closest literature and limitations

The open-access 2015 survey of Aledo–Martinez–Valverde was read in its definitions and dynamical sections. Aracena–Richard–Salinas (arXiv:1507.06141) was read from the full primary PDF, including the fixed-point/maximal-independent-set result and scope. Indexed extended material of the later Aledo et al. 2020 and Gadouleau–Kutner 2024/2025 studies was compared, with access and scope limitations identified in AUDIT.json. The proof is for synchronous open-neighborhood NOR, not self-inclusive minterm/NOR or sequential MIS updates. Exact all-size claims rest on proof, not finite coverage.

Self-review: passed. Independent audit: not yet performed.
