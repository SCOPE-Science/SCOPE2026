# Independent mathematical audit

## correctness

PASS

The original internal Shapley identity and directed-cycle calculation are correct. Reassessed the repaired claim directly on the source equations for every finite loopless graph: for target j with m_j ranked in-neighbors, Delta_j(t)/t occurs in the self term (8) and exactly t-1 terms (9) for the predecessors, and the terminal subtraction b_j(m_j)/(m_j+1) occurs m_j+1 times. Thus the sum of external contributions for j telescopes to b_j(m_j)-b_j(0)-b_j(m_j)=0, including m_j=0 and ties. The printed internal sum counts each reciprocal pair's total arc weight once across the endpoints. Definition 2.1 gives all-arc weight as v(N), hence the displayed vector's efficiency shortfall is exactly the weight of one-way arcs; nonnegative weights ensure strict failure if one is positive. The internal replacement is independently justified by two-player unanimity linearity. For the unit 3-cycle each player's printed external terms are +1/2 and -1/2, the reciprocal contribution is zero, and the exact coalition worth is cardinality. Thus the printed and true vectors are zero and all ones respectively. Replay via arXiv:2605.18157v1 Definition 2.1, the b_j(0)=0 convention preceding Definition 2.2, and Corollary 3.3 equations (8)–(9); proofs and verification scope are in the repaired files. The frozen script was inspected, not executed; it checks the finite witness, not the symbolic efficiency identity or text of the preprint.

## originality

PASS

Originality passes for the repaired source-specific quantitative defect, not the original record's prominently displayed internal formula as a new identity. An exact earlier copy of that formula is Proposition 3.6 of Bandhana–Kroupa–García, not merely a related general principle. The repair relegates it to credited background and proves how much the printed full vector falls short of efficiency, with a directed witness. The inspected precedents do not give this diagnosis of Corollary 3.3.

## value

PASS

The repaired result quantifies a failure of a claimed way to compute all players' Shapley allocations: in networks with many one-way arcs the printed credit can lose the entire grand-coalition worth, not just change a tie or a normalization. The symbolic deficit is a practical check for that printed method and the cycle makes the issue independently reproducible. This is a motivated correction to a specific preprint rather than a rediscovery of the familiar endpoint-sharing identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
