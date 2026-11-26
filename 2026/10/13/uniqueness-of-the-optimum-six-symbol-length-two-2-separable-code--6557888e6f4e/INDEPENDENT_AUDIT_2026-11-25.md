# Independent mathematical audit

## correctness

PASS

A descendant collision between different coalitions of size ≤2 requires the two opposite diagonals of a rectangle: when one coordinate is constant the other coordinate set determines the coalition. Hence the graph is C4-free. Pair nonrepetition bounds the six neighborhood sizes by sum_i binom(d_i,2)≤15; balancing at total 17 already gives 16. At total 16 there are only three profiles meeting the bound. Five triples covering every pair are impossible by parity of the five pairs through a point, and a 4-block forces both triples to repeat the pair outside it. For the remaining profile (3,3,3,3,2,2), the four points outside the leave {a,b} each belong to exactly one 2-block by parity and the two 2-blocks exhaust these incidences. The 2-block matching and the two matchings induced by triples through a and b must be the three distinct matchings of K4. The stated Fano completion and representative follow. The 15·3·2·6!=64800 count labels these data without overcounting; there is already one side-preserving orbit and the full-group stabilizer is 16. Independent pair-mask backtracking checked all degree profiles, found 90 unordered block families with labeled points and verified all their Fano completions. Direct labeled orbit generation with an unsorted transpose verified the full group action (python3 /workspace/branches/independent_checks.py 4). The frozen script's helper sorts transpose rows; the analytic proof and the independent unsorted check verify the labeled transpose action without relying on that implementation detail.

## originality

PASS

The C4-free equivalence, numerical maximum, and Fano-deletion construction are not credited as new. The supported distinct result is that every maximum is such a deletion and the exact labeled census. The strongest accessible related statements give an extremal value or a construction, not rigidity; an important historical source remains uninspected in full.

## value

PASS

The natural six-symbol optimum is already known, but completing every equality case to the same Fano incidence structure explains rigidity rather than recomputing that value. It determines the only maximum-code isomorphism type and its multiplicity for exact classification or code generation. The matching description is a usable structural certificate for the complete finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
