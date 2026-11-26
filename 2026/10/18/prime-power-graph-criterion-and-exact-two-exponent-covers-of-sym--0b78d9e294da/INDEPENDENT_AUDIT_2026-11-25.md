# Independent mathematical audit

## correctness

PASS

Assign each maximal prime power in an order to one cycle length that it divides. The powers assigned to one cycle are coprime, and their sum is at most their product for a nonempty assignment, hence at most that cycle length. The converse uses disjoint cycles. Thus a support of an actual order is a clique, all singleton vertices and edges are realized, and compatibility of all edges and singleton divisibilities is necessary. It is sufficient because pairwise intersecting nonempty subsets of the two covering indices must have a common index; the order 1 is automatic. Intersecting the exponents with E_k by gcd preserves coverage; for each resulting divisor d the least second exponent in divisibility order is the lcm of orders missing from d. This proves the minimax formula; the graph formula for the residual follows by the same iff test. Independent reproduction enumerates integer partitions rather than iterating the order-set recurrence and computes missing-order lcms by incidence bitsets. All 38 rows, including witness pairs and every tabulated count, match. In particular k=40 gives 53,542,288,800, with other witness member 35,959,964,040, over 495 distinct orders and 36,864 candidate divisors.

## originality

PASS

Two-integer covers of symmetric-group orders are already a hypothesis of Bulatov–Karpova–Shur–Startsev Proposition 15, not introduced by the reviewed record or by Xu–Regan. The supported distinct contribution is the iff local test for arbitrary proposed pairs and the exact minimax invariant and certified finite segment, not the cover concept, prime-power segmentation constructions, or cover-to-identity translation.

## value

PASS

The invariant is motivated by an existing two-exponent positive-identity construction, and the iff theorem reduces a coverage condition on every symmetric-group order to explicit compatibility of prime powers. The exact optimization distinguishes sharp achievable bounds from merely feasible input pairs across a substantial range with many competing orders and candidate exponents. The structural result, not just the degree-40 number, makes the finite evidence useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
