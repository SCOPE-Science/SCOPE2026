# Self-review

## Correctness
PASS. The forbidden collision relation for an \(r\)-forward-independent set is coordinatewise: on a free \(\mathbb Z^n\)-action, two markers conflict exactly when their displacement lies in \([-r,r]^n\setminus\{0\}\). A maximal independent set for this finite-range box graph therefore gives the required separation. Applying maximality to \((r,\ldots,r)\cdot x\) puts a marker at a forward displacement in \([0,2r]^n\), so the total forward length is at most \(2nr\). The same finite-window LOCAL-to-Borel transfer quoted in the source then yields the Borel statement.

## Originality
PASS. The closest full-text result, Gao--Hu--Zou Theorem 3.1, gives \(2n^2r\), and Proposition 3.4 shows that the extra factor \(n\) comes from replacing the coordinate conflict box by an ordinary graph-distance ball. Searches for the exact \(2nr\) bound, box-independent marker formulation, and aliases returned no covering result. The related Shinko--Weilacher--Yu work supplies the transfer framework but no such quantitative bound was found in the material inspected.

## Value
PASS. The claim improves a newly introduced quantitative marker theorem by a factor growing with the number of commuting generators and isolates the correct geometry of the independence constraint. It is a reusable structural refinement, not a routine parameter substitution.

## Closest literature and limitations
The closest literature is Gao--Hu--Zou, arXiv:2608.15422, and Shinko--Weilacher--Yu, arXiv:2608.18439. The theorem concerns only the free part, retains bounded-to-one hypotheses, and does not claim optimality of \(2nr\). The full text of the latter preprint was not independently inspected, so a residual coverage risk remains.

Self-review: passed. Independent audit: not yet performed.
