# Independent mathematical audit

## correctness

PASS

The exact final theorem has fully quantified domain k>=2, graph F_k=K1 vee(kK2), nonnegative integer pebbles and legal two-for-one moves. Reconstructed hub potential E=h+sum f(a_i,b_i), f=floor(a/2)+floor(b/2)-delta where delta=1 precisely for (1,1) or a lone odd pile. For all legal moves the three exact potential changes (outer-to-hub, hub-to-outer, intra-pair) are nonpositive, including parity and zero-pile boundary cases. The constructive one-pair elimination treats both-even, mixed parity, both odd, lone odd of size >=5, lone size 3 and size 1, and (1,1), with hub reserve 0/1/2 as applicable. Eliminate f>0 first, zero next and f=-1 last: if E>=1 then H>=m+1 ensures enough reserve before each negative pair, leaving exactly E pebbles at the hub. Necessity follows monotonicity. For unrestricted stacking, the first single-support time is preceded by two source pebbles; the unique exceptional q=3 outer-terminal state is handled explicitly via immediate predecessors with positive potential. The universal local inequality 2f(a,b)>=a+b-4 has equality only for (1,1), so t>=4k implies E>=1; the explicit size (4k-1) configuration has E=0 and multiple occupied vertices. An independent clean-room dynamic program checked the two reachability criteria on 34+1286+50387=51707 configurations for k=1,2,3, all sizes 1..4k, and independently checked 14641 ordered local count pairs (0..120)^2 with move inequalities and sharp bound. These finite checks corroborate but do not prove the all-k quantifiers; the algebraic and constructive proof covers them.

## originality

PASS

Qualified best-of-knowledge originality after comparing the SAME destination-consolidation invariant at theorem/implication level. Csernák–Soukup 2026 introduce stack(G), compute complete/multipartite/path families and prove stack(G) >= 3 alpha(G)+1, but the k>=2 friendship graph lies outside their exact graph classes. Their bound specializes only to 3k+1, not 4k, and cannot imply the exact necessary-and-sufficient configurationwise hub-surplus criterion. The 2021 friendship-graph paper computes cover pebbling, which has an incompatible target (occupy all vertices), whereas the new claim empties all but one vertex. Checked same-graph Resultary records and the original authors' released finite report: none of the inspected exact reported entries gives this all-k theorem. Absence of a matching indexed source is not proof of priority; risk of unindexed or unpublished equivalent work is retained.

## value

PASS

A natural infinite graph class (triangle friendship/windmill graphs, k>=2) receives both a sharp exact value for a newly introduced and mathematically motivated consolidation invariant and a stronger complete configurationwise decision rule. The parity-corrected hub potential is a genuine structural obstruction and constructive certificate, not a direct textbook substitution: every viable configuration can be actually consolidated at the prescribed hub by local elimination. The exact threshold 4k exceeds the prior sharpest directly applicable general lower bound 3k+1 by k-1 and supplies a transparent tight witness in every order. The result is not a recomputation of known cover-pebbling tables or an unmotivated finite slice, and a future researcher studying stacking in block graphs or triangle cacti can use the local criterion and extremal family as a benchmark; no new theorem for the entire cactus class is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
