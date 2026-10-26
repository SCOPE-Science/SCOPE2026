# Scientific review

**Correctness — PASS.** The base-arithmetic carry lemma exactly characterizes every adjacent pair, including both periodic and aperiodic branches. Each length-four window crosses at most one substitution boundary, ensuring two increments \(+1\); the reversal would require two increments \(-1\), impossible for any modulus at least three. The full short-factor family decompositions are exact by the constructive adjacency lemma. Inclusion–exclusion gives the short counts, and reversal-orbit counting gives the gcd trichotomy. Finite symbolic and direct-prefix verifications independently support the proof; prefix data are not the infinite proof.

**Originality — PASS, with residual risk.** Allouche et al. (arXiv:2406.09302, Question 62) discuss generalizing reflection complexity and give only an illustrative binary-base, modulus-three case. Starosta (arXiv:1104.2476) gives full factor complexity and short factor languages but does not give the claimed ordinary reversal-orbit census for every base. Allouche–Shallit (2000) supplies palindrome information that cannot alone exclude distinct reversed factor pairs. The current claim covers all bases at least three, the gcd-determined exact length-two/three behavior, and the universal length-four threshold. Published-record and mathematical research-record searches found no stronger directly covering statement. Unindexed equivalent results remain a possibility.

**Value — PASS.** A short local combinatorial obstruction solves a natural all-base variant of a published reflection-complexity question for a classical family, with a substantive number-theoretic dichotomy arising from the carry modulus. The classification is sharp and encompasses infinite aperiodic and periodic families; it is not merely an isolated finite table or a restatement of palindromic avoidance.

**Limits.** The focus is the ordinary reversal relation for base at least three and modulus at least three. Starosta's exact factor-complexity formula is prior work. No human or independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
