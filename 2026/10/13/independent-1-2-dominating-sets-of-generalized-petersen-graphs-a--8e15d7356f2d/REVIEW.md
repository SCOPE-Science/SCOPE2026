# Independent mathematical audit

## correctness

PASS

The three spoke states encode independence and both degree constraints with the centered five-column window. For n≥5, the trace has exactly one fixed-index walk per labeled configuration, including periodic words, and the appended symbols give the selected count. An independent exact construction of the 81-state graph gave 89 arcs and cyclic SCC sizes 17,3,3. In the main SCC the simple-cycle types (length, selected count) are (5,4), (6,4) three times, (7,5), and (12,8). The two disjoint length-six cycles cancel the length-twelve term in the determinant, and the other SCCs each contain a single (3,2) cycle. With A=z^4t^5+3z^4t^6+z^5t^7 and q=z²t³ this gives det(I−tM)=(1−A)(1−q)². The formal derivative yields tA′/(1−A)+6q/(1−q), and removing 6q gives the asserted series. For the first term the supported (n,w) are nonempty sums of the types (5,4),(6,4),(7,5), with nonnegative excess 3w−2n; for the second term they are multiples of (3,2) with n≥6. There is no t⁸ term. At n≡4 mod 6 an excess of 1 would require exactly one (7,5) plus (6,4) terms, which makes n odd; the next permitted excess is 4. Sharp orders in the four nonmultiples-of-three residue classes are 5+6r,7+6r,14+6r,10+6r with weights 4+4r,5+4r,10+4r,8+4r. This and multiples of three give the exact minimum and existence statement. The independent script returned AUDIT_OK, including the exact cycle determinant, shared-state witnesses and coefficient-level direct labeled-subset checks for orders 5–10. Replay: python3 /workspace/review-evidence/independent_transfer_audit.py. The frozen verifier was inspected but not run; finite checks of orders alone do not prove the infinite assertions.

## originality

PASS

The ordinary minimum and the same-cardinality transfer strategy for maximal independent sets are already covered separately. The distinct supported result is the exact restricted enumerator for labeled independent [1,2]-sets, with the sole feasibility gap and independent attainment of the ordinary minimum otherwise. The frozen related-work sentence about (2-d)-kernels reverses the neighbor direction: they require each outside vertex to have at least two neighbors in the selected set. This does not affect the definition or proof of the finding.

## value

PASS

The exact cardinality enumerator resolves the loss of feasibility at n=8 under an additional natural constraint and proves that the constraint does not otherwise increase the minimum. It distinguishes admissible maximal independent sets from the unfiltered ones at every size and graph order; a recomputation of the ordinary minimum alone would not have this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
