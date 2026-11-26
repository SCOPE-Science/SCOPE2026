# Independent mathematical audit

## correctness

PASS

The frozen structural criterion and counts check, but the final assessment is of the narrower and strengthened enumerative claim in /workspace/repairs/3/RESULT.md. The initially unseen line-graph vertices are exactly the edges induced by the unused endpoints W. A first force on a cycle there is impossible because its source would see both incident unobserved cycle edges at one endpoint. Since a nonempty selected edge meets two parts, any residual leaf has a permanently observed edge to a used vertex in another part. That edge sees the single unobserved leaf edge, so all residual forests can be stripped. The allowed multipartite residual profiles have support at most one, or support two with a singleton. Apply subset inversion to the indicator f(T) of that profile condition. Its transform α(B)=Σ_(T⊆B)(−1)^(|B|−|T|)f(T) satisfies f(W)=Σ_(B⊆W)α(B). Exchanging this sum with the edge-selection enumerator leaves terms (1+z)^e(a−u) when B has profile u, since selecting any edge incident to B is then forbidden. For the transform weight after factoring (−1)^|u|, the empty subset contributes 1, each occupied part contributes −1, and each pair contributes u_i+u_j−u_i u_j by summing over t_i=1 or t_j=1 and subtracting the common singleton pair. The empty selection is counted by f(V(H)), which is 1 only for a star in this family, and is subtracted. The resulting single sum enumerates all coefficients. An independent replay of the frozen two-sum formula and direct forcing on nine profiles passed (python3 /workspace/checks/frozen_review_checks.py power). A fresh compact-formula verifier ran successfully on 21 profiles and 25,942 labelled edge selections, including the (1,2,3) example and star boundary tests through K_(1,12): python3 /workspace/repairs/3/verify_compact_polynomial.py. Both are finite checks, not the all-parameter proof.

## originality

PASS

The frozen claim package cannot pass as a new structural criterion plus new rook and triangular enumerations: these are covered. The repaired record does not claim those as contributions. Its distinct result is an evaluated subset-transform coefficient giving the whole polynomial with one sum over part profiles, for all root multipartite lists including mixed sizes and at least three parts. Neither the general placement criterion nor the exact enumerators restricted to rook and triangular graphs give these explicit weights for mixed profiles. The repair proves and checks the single-sum formula; it is not just a certificate or disclaimer for the covered claims.

## value

PASS

The repaired enumerator addresses a natural question beyond recognizing or minimizing a placement: it gives directly every cardinality coefficient for a broad labelled graph family, including mixed profiles not covered by the rook or triangular formulas. The evaluated profile weight replaces enumeration of edge subsets or a separate inner subset inversion at each residual profile with a single finite sum of binomial coefficients and powers. For a fixed number of parts the number of summands is polynomial in the root order, rather than exponential in the root edge count. This value rests on the explicit uniform evaluation, not on novelty of Möbius inversion or on recalculating known special cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
