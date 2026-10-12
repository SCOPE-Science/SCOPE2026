# Review of Rigidity of maximum two-use pentagon zero-error codes

## Correctness
PASS. The proof reduces a maximum code to a one-point-per-row transversal. A two-point row forces its two neighboring rows empty and leaves at most two points on the remaining adjacent pair of rows, so such a code has size at most \(4\). For a five-point transversal, adjacent row values differ by \(\pm2\); summing the five increments modulo \(5\) forces all signs equal. The exhaustive verifier independently reproduces the maximum, the ten-code census, and the symmetry orbit.

## Originality
PASS. Shannon’s original article was inspected at the exact channel and block length: it gives the five-word witness \(00,12,24,31,43\) but does not state an equality-case census. A later full-text treatment likewise presents the five-message two-use phenomenon and the strong-product formulation without the ten-code rigidity statement. Exact-parameter searches found no source implying the classification. Residual risk remains that an obscure unindexed note recorded the elementary census.

## Value
PASS. This is the equality structure of the first and most famous example where zero-error coding across uses beats the naive product construction. The result explains that all optimal two-use codes have the same affine geometry, rather than merely furnishing another optimum witness.

## Closest literature and limitations
The closest literature is Shannon’s 1956 construction and later expositions of the pentagon channel. The claim is restricted to two channel uses and does not classify higher strong powers or reprove the asymptotic capacity theorem.

Self-review: passed. Independent audit: not yet performed.
