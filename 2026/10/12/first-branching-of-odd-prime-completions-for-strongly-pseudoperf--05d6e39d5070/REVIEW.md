# Self-review: first odd-prime completion branching

## Correctness

**PASS.** Reciprocal divisor closure gives a bijection between admissible subsets and binary masks. The exact equation \(x+p\operatorname{rev}_{a+1}(x)=2^{a+1}p\) yields the fraction criterion and bounds the prime search to \(p<2^{a+1}\). Full mask enumeration and a logically distinct direct subset-sum DP over every potential prime agree for \(1\le a\le9\). Each winning prime has an explicit divisibility, primality, sum, and reciprocal-closure check. The computation proves the entire stated finite domain; no extrapolation beyond exponent \(9\) is made.

## Originality

**PASS.** Aryan and colleagues' Section 4 classifies the narrower strongly \(2\)-near-perfect one-pair omission and records \(p=179\) at exponent \(9\). The OEIS A334405 table includes the other number \(11776=2^9\cdot23\) as an individual example. Neither coverage certifies first branching across all prime completions and all lesser exponents. Searches of exact values, equivalent prime-fiber formulations, earlier family descriptions and research records yielded no dominating claim.

A substantial access risk remains: the recent Wang–Zelinsky preprint itself was available at abstract level, but full text could not be inspected; no claim that the unseen text is not covering is made.

## Value

**PASS.** The first parameter where one exponent supports two distinct odd-prime completions is a natural invariant for the two-prime subfamily of a problem being actively investigated. The two solutions instantiate inequivalent omission mechanisms—one reciprocal pair and two reciprocal pairs—marking the first point where the previously classified one-pair mechanism coexists with a genuinely broader one. The conclusion is finite and structural; it does not rebrand the previously listed numbers as discoveries.

## Closest literature and limitations

The 2024 complete theorem about strongly \(2\)-near-perfect numbers is hypothesis-restricted, while the 2026 paper treats the broader notion but remains an access risk. The OEIS sequence is a table of instances, not an exhaustive fiber classification through the necessary numeric range. The full later-exponent behavior is open here.

Self-review: passed. Independent audit: not yet performed.
