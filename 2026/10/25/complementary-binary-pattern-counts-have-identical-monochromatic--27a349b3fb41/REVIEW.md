# Review of complementary binary-pattern progression symmetry

## Correctness — PASS
The integer identity is reconstructed from zero padding and digitwise complementation. The proof identifies the sole possible new occurrence at the left boundary of the reflected word and shows its count is the constant \(\varepsilon_v\), independently of the integer and padding width. Reversing any finite increasing progression preserves its difference and produces a uniform color shift modulo every \(q\ge2\); exchanging \(v\) with \(\bar v\) gives both inequalities between maximal progression lengths. The argument covers \(n=0\), every mixed word, and possibly infinite supremal lengths. A separate verifier confirms \(61{,}440\) integer identities and \(4{,}800\) finite progressions; finite checks are not claimed to prove the infinite result.

## Originality — PASS within inspected evidence
The principal comparison is B. Sobolewski, *On monochromatic arithmetic progressions in binary words associated with pattern sequences*, arXiv:2204.05287 (posted 11 April 2022), Section 6 Problem 4, which states the equality between a mixed word and its bit complement only as a conjectural pattern after computations for words through length three. Its separate length bounds and dilation identities do not imply the new exact integer reflection. Searches for equivalent formulations, broad bounds, potential tabulations, and implication by prior work in mathematical literature and accessible mathematical research records did not identify a covering result. The accessible journal index is not a substitute for a reading of the full 2024 journal text, which is an explicit originality risk; an unindexed independent proof remains possible.

## Mathematical value — PASS
The result settles a specifically posed published problem for every mixed binary pattern and every positive step, and it strengthens the original parity conjecture to all moduli through a structural identity on complete finite color words. It supplies a reusable involutive mapping rather than an isolated numerical extension. The result does not treat constant patterns, does not compute the shared values, and does not handle nonbinary bases.

## References and limitations
Sobolewski, arXiv:2204.05287, especially Sections 1, 6, and 7, provides the exact normalization and motivating open problem; journal version *Theoretical Computer Science* 1018 (2024), article 114815, DOI:10.1016/j.tcs.2024.114815 (indexed metadata and abstract only). Priority has not been independently established, and the verifier tests finitely many cases.

Self-review: passed. Independent audit: not yet performed.
