# Scientific review

**Correctness — PASS.** The smallest nonzero affine digit gives a partition into big blocks with one zero interval each. A zero interval can join only its next neighbor, so the only run lengths are \(p^j\) and \(2p^j\). Counting base-\(p\) carry transitions gives an explicit join statistic, while an invertible prefix-sum map on higher affine coefficients yields the exact product polynomial \(F_s\). Counting the remaining affine parameters proves every coefficient of the all-window enumerator. Direct exhaustive codeword comparisons validated 117 complete enumerators; they supplement rather than replace the infinite-family proof.

**Originality — PASS, with bibliographic qualification.** The most relevant comparison is Ma–Luo's symbol-pair distributions of simplex and variation-simplex codes (arXiv:1911.02184v1), a different code geometry and length. Shi–Zhu–Helleseth (arXiv:2109.13764v1) give the general zero-run identity used in the proof, not its carry-counted affine zero-run census. Pan–Ling–Liu (arXiv:2309.08920v1) determine all **minimum** \(b\)-symbol distances of Reed–Muller codes, which does not imply this full spectrum. A prior complete **binary** affine code spectrum is acknowledged and excluded from the claim. Searches found no matching odd-prime all-window distribution, but an unindexed equivalent remains possible.

**Mathematical value — PASS.** The natural, coordinate-sensitive overlapping-symbol weight has a complete classification across all odd primes and dimensions, including exact multiplicities and a superincreasing carry polynomial. This resolves far more than the extremal distance and isolates a meaningful nonbinary structural phenomenon.

**Limitations and risks.** Coordinate permutations or extension-field digit conventions can change the question. Finite tests do not prove the infinite theorem, and bibliographic noncoverage cannot guarantee first discovery. No independent expert audit was performed.

Self-review: passed. Independent audit: not yet performed.
