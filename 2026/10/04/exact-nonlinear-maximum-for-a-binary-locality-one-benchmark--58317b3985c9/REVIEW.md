# Same-model review

## Correctness
**PASS.** The upper bound is proved structurally. Binary local distance \(2\) on a two-coordinate recovery view forces the two coordinate functions to agree up to a fixed complement. Hence all coordinates lie in equivalence classes of size at least \(2\), and the code injects into a weighted binary quotient. At length \(9\), either there are at most three classes, giving at most \(8\) words immediately, or the class sizes are \((2,2,2,3)\); slicing on the weight-\(3\) coordinate then gives two length-three distance-\(2\) binary codes, each of size at most \(4\). The eight-word witness is explicit. `verify.py` checks the witness and exhausts every reduced weighted quotient case.

## Originality
**PASS.** The closest primary source, Kang--Xiong arXiv:2609.16044v1, defines the same nonlinear locality model and reports for \((2,9,3,1,2)\) the bounds \(8\le M_{\max}\le64/5\); its theorem of seven exact maxima does not include this row. Exact-tuple, verbal-alias, broader-locality, and published semantic-literature searches did not locate the exact value \(8\). The closest published neighboring LRC record proves different locality-one tuples and does not imply this one. Residual risk remains that the elementary locality-one class reduction may be implicit in older literature; the exact target value itself was not found.

## Value
**PASS.** The claim closes a concrete nonlinear-size gap in a recent certified benchmark table and shows that nonlinearity gives no advantage at that parameter. It is not a routine recomputation of the LP: the stronger bound comes from a structural quotient argument that handles arbitrary overlapping selected recovery views.

## Closest literature and limitations
The decisive comparison is Kang--Xiong, arXiv:2609.16044v1, Table V.1 and Theorem V.1. Li--Wei--Xiong, arXiv:2608.05758v1, is broader background for nonlinear LRC LP bounds. A published research record titled *Exact maxima for the three residual three-block LRC cases* covers neighboring exact tuples but not \((2,9,3,1,2)\). The present theorem is restricted to the binary tuple \((n,d,r,\delta)=(9,3,1,2)\); no larger-alphabet or general-parameter formula is claimed.

Same-model review: passed. Independent audit: not yet performed.
