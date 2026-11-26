# Independent mathematical audit

## correctness

PASS

The difference in zero counts between the prefix and suffix of length k is (H_k+H_(2n−k))/2, and each height is nonnegative. Thus both heights must vanish, making k even. Complementary border lengths are equivalent, so the shortest has k=2j≤n. A first synchronized return of two Dyck words read respectively from the front and back decomposes the pair at a unique positive size j; arbitrary independent Dyck remainders give the convolution S−1=ES. Cutting the target word at its first symmetric return pair gives the E_j end block pair and an arbitrary middle Dyck word of size n−2j, including the empty middle. This proves both generating functions. Independently, setting a_m=C_m/4^m, the bordered fraction is the sum of (E_j/16^j) a_(n−2j)/a_n. For j≤n/4 the ratio is bounded and tends to one at each fixed j. For j>n/4, E_j/16^j≤C_j²/16^j=O(n^−3), so summability of a_m=Θ((m+1)^−3/2) bounds the remaining total by O(n^−3/2). Therefore the limiting unbordered fraction is 1−E(1/16)=1/S(1/16) without needing complex continuation. The stated partial-sum expression telescopes by the central-binomial recurrence and tends by Stirling to 16/π−4; the numerical value agrees. Direct ballot generation and literal zero counts for all proper lengths reproduced every shortest-border frequency through n=12, and exact fractions checked the partial sums through N=100. Replay: python /workspace/review_checks/dyck.py; output /workspace/review_checks/dyck.txt. The supplied script was inspected, not executed.

## originality

PASS

Credit exact overlap for the Catalan-square synchronized-renewal kernel, but not for the shortest abelian-border law on the Catalan language or its density. The closest paper with abelian borders counts the statistic over unrestricted input words, and the closest catalogue renewal theorem applies to a pair of equal-length Dyck paths, not the symmetric ends and variable middle of one word. The supported distinct contribution is the bridge to the intrinsic Dyck-word statistic and the resulting whole distribution and limit, not the Catalan-square sum or the first-return block numbers alone.

## value

PASS

The shortest-border distribution on a natural constrained word family answers more than an isolated coefficient query. The first symmetric return decomposition explains the Catalan-square kernel, and the explicit positive limiting density distinguishes this setting from the vanishing densities in the unrestricted and balanced families. The value rests on the complete restricted-language statistic and limit, not a recomputation of the kernel by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
