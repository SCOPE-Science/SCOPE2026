# Self-review

## Correctness

**PASS.** A total idempotent function decomposes into disjoint rooted fibres. A star's root colour and non-root colour multiplicities are complete invariants. Its internal leaf permutations and permutations of isomorphic fibres supply all automorphisms, yielding the exact rigidity criterion. Choosing each permissible rigid star type at most once proves the product polynomial; a contiguous subset-sum lemma proves every carrier size up to the sharp maximum is possible. The unrestricted multiset generating function and coefficient recurrence follow from the same type count. For fixed \(q\), an exact expression for the logarithm of the generating function yields the stated regular power asymptotics of the log partition function, mean, and variance; exponential tilting gives matching coefficient growth bounds. The supplied checker independently enumerates the claimed finite parameter ranges and returns `ALL_CHECKS_OK`. The infinite assertions do not depend on exhaustive testing.

## Originality

**PASS within the checked primary-literature and mathematical-database evidence.** Kuželka's arXiv:2608.30580 treats general unary functions and automorphism-aware model counting but not the constrained idempotent rooted-star rigidity ceiling. OEIS A161870 already contains the two-colour **unrestricted** series, which is expressly credited and not claimed new. published-finding corpus searches for coloured idempotent unary rigidity, star-type automorphism groups, exact finite ceiling, and equivalent generating polynomials did not identify a result covering the rigid classification. The closest identified published work concerns generic unary functions or polymorphism-homogeneous monounary algebras and lacks the exact same object/constraints. Historical priority remains a caveat: older work on finite unary algebras or coloured star forests might imply the criterion without matching terminology.

## Value

**PASS.** Finite model counting with automorphisms raises the natural question of which coloured unary models admit no nontrivial symmetry. The theorem completely classifies that locus, provides a sharp finite size obstruction and an exact labelled/unlabelled conversion for rigid models, and contrasts it with unbounded general counts and their growth. The cutoff is structural rather than an arbitrary small example or recomputation of a known unrestricted sequence.

## Evidence and limits

The proof, explicit coefficient methods and standard-library exhaustive checker are self-contained. Exhaustive finite checks cover \(q=1,2,4\) on small carriers, not all parameters. The original paper was materially inspected in its publicly accessible version, including its automorphism treatment; the absence of a matched theorem in inspected material does not establish publication priority. The asymptotic is for fixed colour count. The result does not extend automatically to unrestricted unary maps or multiple operations.

Self-review: passed. Independent audit: not yet performed.
