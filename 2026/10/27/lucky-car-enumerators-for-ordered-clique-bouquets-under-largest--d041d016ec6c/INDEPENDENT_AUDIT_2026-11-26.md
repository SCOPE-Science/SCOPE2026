# Independent mathematical audit

## correctness

PASS

In the complete-clique step the smallest label must be preferred, since a car can move only to larger labels. More generally, an omitted label before a used larger label would have to be filled by an earlier overflow while all larger vertices were already filled; the later car would then fail. Thus distinct preferences are an initial interval. Conversely, their positive multiplicities produce a low block filled by first occurrences and a disjoint high block filled by repeats, by induction; the repeats cannot reach the not-yet-used preferences since their total is at most t−k. This gives u(1+u)^(t−1) for a block with t>0 vacancies, and 1 for t=0. The hub must be preferred, and the c initial hub preferences occupy the hub and the highest c−1 labels. Each peripheral car stays in its own block, and a filled high suffix cannot change the choice of the largest available greater neighbor. Its remaining block must contribute exactly as many cars as vacancies. Ordered disjoint preference intervals give the product without shuffles. For a nonempty remaining prefix, its last block j and length h contribute u^(j+1)(1+u)^(s_(j−1)+h−1), and the empty prefix contributes u. Summing h gives the claimed polynomial. For a swap, later terms are unchanged; with q=1+u, the two terms differ, after the common factor, by (q−u)(q^(a−1)−q^(b−1)). This proves the nonzero coefficientwise comparison for unequal blocks as well as both extremal orders. Evaluation at u=1 gives the stated totals and the examples follow at the specified labelings.

## originality

PASS

Credit the supported multi-clique bouquet formula and the coefficientwise order theorem, not the complete-graph lucky refinement already implied by Hallam–Molebash–Porter. The close primary work counts different subfamilies on other graphs and poses the connected gluing and increasing/lucky questions, rather than supplying this bouquet decomposition.

## value

PASS

The family is a connected test case for the gluing and statistic-refinement questions in the foundational paper. The formula resolves not just a total but a full distribution, and its exchange law quantifies how the label order changes every coefficient for a fixed unlabeled profile. This is stronger than calculating a few small examples or the already covered complete graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
