# Independent mathematical audit

## correctness

PASS

Retaining each letter's first and last positions preserves singletons, diagonal pairs, and every distinct pair ab because ab is present exactly when first(a)<last(b). The resulting word has length at most 2q, with equality in the minimum precisely when all aa are present. Minimum representatives then have exactly two occurrences per letter; arbitrary representatives need only have at least two. Among these classes the only variable observations are ordered pairs of distinct letters, with ab missing exactly when last(b)<first(a). This identifies the observation set with the reversed complement of the strict interval order on distinct letters and proves both injectivity and reversal of inclusion. For surjectivity the strict predecessor sets in a (2+2)-free poset are nested: incomparable sets would supply a predecessor of each upper vertex missing below the other, giving an induced (2+2). For an element x let i be its predecessor-set index and j the first index of a set containing x, or one past the end. Then j>i and the interval [2i,2j−1] has the right strict comparisons; perturb ties within endpoint type without crossing an endpoint of the other type and read the endpoints in order. This yields the desired doubled word. Renaming commutes with the bijection; q=1 yields one deepest class, represented by aa. The independent endpoint enumeration gives 1,3,19,207,3451 signature/order classes through q=5; replay: python3 /workspace/branches/44766552-aa02-4b69-ae48-315dc237b573/independent_endpoint_check.py. This is not a reproduction of the frozen verifier's all-signature traversal. The denominators 152 and 2326 are from Table B.1 of arXiv:1310.1278; the labelled Brightwell–Keller asymptotic on p. 2 has 12√3/π^(5/2), (q!)²√q, exponential base 6/π² and relative error O(1/q), as stated.

## originality

PASS

The supported distinct result is the canonical all-alphabet identification of the deepest two-subsequence layer with labelled interval orders, including reverse inclusion and behavior under renaming. The interval-order characterization, exact counts and asymptotic are existing results transported by that identification; the binary layer is also covered by a prior special case. No absolute priority is asserted.

## value

PASS

The layer is selected by an intrinsic extremum, not by a convenient small alphabet. The identification gives an all-alphabet structural description with an order-theoretic interpretation of inclusion, and transfers counts, asymptotics and letter-renaming orbits. It is useful independently of the first few enumerated values; those values and the poset asymptotic alone are not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
