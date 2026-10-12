# Review of Equality cases for the length-three two-user binary adder bound

## Correctness
PASS. The claim uses the published distance-class inequalities \(N_k\le {3\choose k}2^k\) and \(N_k\le {3\choose k}2^{3-k}\), whose sum gives \(14\). Equality forces the cardinality profile \((2,7)\) or \((7,2)\). For the two-word side, a direct coordinate analysis counts exactly \(2^{3-r}\) disjoint cross-row collision pairs when the two words have Hamming distance \(r\); a seven-word partner can destroy all of them by one omission exactly when \(r=3\), and then the omission must be one endpoint. The exhaustive verifier checks every ordered pair of nonempty subsets and reproduces the count and structure.

## Originality
PASS with a stated residual historical risk. The directly relevant 1983 full text supplies the general upper-bound machinery but not the equality classification; its worked finite example is at length five. Exact-parameter and alias searches did not locate a published statement of the \(n=3\) classification or its count of \(16\) ordered extremizers. The closest 1992 graph-theoretic paper concerns a linear first code and maximum independent sets; only abstract-level material was accessible, so it is not used for a whole-document noncoverage assertion. Even a fixed-repetition-code maximum of seven would not by itself imply the global statement that every product-optimal pair has the antipodal-minus-one form.

## Value
PASS. Equality structure for a sharp general zero-error bound is a natural question, and \(n=3\) is the first odd block length immediately after the classical sharp length-two example. The result does more than recompute the number \(14\): it gives all equality cases, their exact count, and a one-orbit rigidity statement. This supplies a compact finite benchmark for graph-based and additive-combinatorial constructions of binary-adder code pairs.

## Closest literature and limitations
The main comparison is van Tilborg's 1983 general upper-bound paper, supplemented by the 1985 construction paper and the 1992 graph-theoretic construction paper. The finding is finite and makes no asymptotic claim. An obscure historical table or example could still duplicate the small equality classification.

Self-review: passed. Independent audit: not yet performed.
