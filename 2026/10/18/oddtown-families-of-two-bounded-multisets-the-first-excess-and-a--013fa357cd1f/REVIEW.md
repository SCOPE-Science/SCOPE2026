# Scientific review

## Correctness: PASS

The intersection is correctly normalized as \(I(x,y)=\sum_i\min\{x_i,y_i\}\). The initial-segment embedding proves only the general \(2n\) upper bound and is explicitly credited to the standard Oddtown argument. Direct verification of all 45 pairs in the ten-word block and the disjoint-support argument prove the general lower bound. Exact maximum values through five coordinates are certified by complete lexicographic enumeration of **all** increasing cliques of the compatibility graph, not by randomized sampling. An independent initial-segment bitmask representation is checked against the direct minimum-sum implementation. The finite certificate is not represented as proof of a general exact formula.

## Originality: PASS, with residual risk

Zou, arXiv:2606.03613, proves restricted-intersection theorems for ordinary subsets; his upper bound specializes to the acknowledged \(2n\) bound here, not to the block amplifier or exact profile. Shankar, arXiv:2607.23117, studies lattice-path common edges, a different intersection operation. Banerjee and Dewan, arXiv:2610.21636, study even-cardinality (Eventown) multiset families; their hypotheses exclude the odd members in this finding. Searches of multiset, order-ideal and Oddtown aliases and related mathematical research records found no mathematically dominating prior theorem or equivalent 10-word construction. A differently phrased, uncatalogued order-ideal construction remains a bibliographic risk.

## Value: PASS

The first deviation from classical Oddtown occurs at the natural smallest order four, and the explicit six-coordinate amplifier establishes a persistent positive asymptotic density gap. This advances a well-motivated extremal comparison while stopping short of unsupported general exactness claims. It gives a reproducible obstruction and reusable lower-bound pattern.

## Limits

The precise value of \(O_2(n)\) for \(n\ge6\), the optimal limiting ratio, and uniqueness of extremizers are not established. The five small maxima use finite enumeration; a human reproduction and external expert validation have not been performed. Literature priority could change with undiscovered equivalent formulations.

Self-review: passed. Independent audit: not yet performed.
