# Self-review

**Correctness — PASS.** The exact linear-greedy-arch equivalence, its cyclic matching translation, and the parity of the path components are proved for every integer \(k\geq1\). The counting proof handles all boundary cases, distinguishes labeled words from primitive necklaces, and uses a direct reflection-axis fixed-point count for the bracelet formula. `verify.py` independently tests the criterion against direct scattered-subsequence enumeration and greedy arch recognition, and confirms all orbit totals through \(k=8\). Finite checks do not prove the infinite claim.

**Originality — PASS, qualified.** The closest primary texts concern the definition and algorithms for circular universality (Barker et al. 2020; Fleischmann et al. 2021; Schnoebelen–Veron 2023), and fixed-balance noncircular spectra (Day et al. 2019). They do not state the specific unique-even-component criterion or the combined labeled, necklace and bracelet formulas in the inspected material. The numerical sequence \((2k+1)2^k\) already occurs in OEIS A014480 and is not itself claimed new. A differently phrased preexisting result remains possible.

**Mathematical value — PASS.** This is a complete natural classification at the first length beyond the minimum, with sharp formulas for words modulo two symmetries and a linear-time test. The cycle-matching and parity derivation accounts for the enumeration rather than merely reproducing a known number sequence.

**Closest literature and limitations.** The 2020/2021 circular-universality works and 2023 arch-index algorithm give essential context but no directly identified sharp enumeration. Applicability is restricted to labeled binary words of length \(2k+1\); higher surplus length and larger alphabets are not covered. The search cannot exclude unlocated formulations. The proof has not undergone independent scientific evaluation.

Self-review: passed. Independent audit: not yet performed.
