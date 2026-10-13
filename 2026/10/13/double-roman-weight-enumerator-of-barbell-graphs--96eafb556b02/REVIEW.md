# Self-review

## Correctness
PASS. The proof conditions one clique side on the two bridge-endpoint labels. The four endpoint rows are derived from exhaustive local cases: endpoint label \(3\) protects the side automatically; endpoint label \(2\) fails only on \(\{0,1\}\)-assignments containing a zero; endpoint labels \(0\) or \(1\) require either an internal \(3\), at least two internal \(2\)'s, or the unique exceptional pattern of one internal \(2\) with all other internal labels \(1\). The endpoint-\(0\) bridge correction is then exact. Gluing the two endpoint-conditioned sides gives \(\operatorname{tr}(M_n^2)\). The packaged verifier independently checks every labeling for \(2\le n\le5\). For \(n\ge4\), the minimum-layer proof separately shows each clique side has weight at least \(3\), with equality exactly for a single label \(3\).

## Originality
PASS with residual literature risk. The 2016 introductory paper defines the invariant and gives general minimum-weight results, not an all-function barbell enumerator. The open full text of Yang–Zhou (2020) was inspected and contains no “barbell”, “polynomial”, or “clique” occurrence. The closest broader source found is the Banerjee–Henning–Pradhan block-graph algorithm, which computes the minimum double Roman domination number in block graphs but does not, from its accessible abstract, imply the full weight distribution. published-finding corpus searches under barbell, two-clique bridge, block-graph, polynomial, enumerator, and minimum-function formulations returned no equivalent or stronger statement.

## Value
PASS. A barbell is a minimal nontrivial clique-sum obstruction to treating the two cliques independently: only the two bridge endpoints can receive help from the opposite side. The four-state transfer matrix isolates exactly that interaction and counts all feasible functions, not merely the optimum. The formula also exposes a sharp small-order boundary—multiplicities \(4\), \(13\), then \(n^2\)—and shows that from \(n\ge4\) the minimum functions decouple completely into one label \(3\) per clique. This is a natural coefficientwise refinement of an optimization invariant on a standard block-graph family.

The closest prior literature and remaining limitations are described in `RESULT.md` and `AUDIT.json`. The finite verifier is a consistency check; the infinite statement rests on the symbolic state decomposition.

Self-review: passed. Independent audit: not yet performed.
