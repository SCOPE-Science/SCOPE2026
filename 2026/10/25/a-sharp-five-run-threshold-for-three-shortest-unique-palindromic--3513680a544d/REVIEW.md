# Review of the five-run SUPS theorem

## Correctness

**PASS.** Every palindrome has a center in one maximal run; for a fixed length, there is at most one eligible palindrome per run center. The proof establishes the pairwise-disjoint-center exclusions, the stronger impossibility of simultaneous shortest answers centered at internal runs two and four, and the exact inequalities forcing length at least fourteen for a three-answer query. It then constructs infinitely many equality-witness families and rules out all shorter unique palindromes by center. A direct all-substring standalone verifier checked \(6944\) low-run words at lengths at most fourteen with every nonempty interval, plus \(48\) parameter-family instances and \(2400\) additional larger interval tests. Finite checks are corroboration, not the proof for unbounded parameters.

## Originality

**PASS relative to inspected evidence, with residual historical uncertainty.** Watanabe et al., arXiv:1903.06290, exploit run-centered minimal unique palindromes and study fast SUPS queries on run-length-encoded strings. Mieno and Funakoshi, arXiv:2204.07327, prove at most four SUPSs for arbitrary words and describe a three-answer binary example without a five-run classification. Nakashima et al., arXiv:1608.05550, develop general query algorithms. None of their inspected primary statements entails the stronger sharp bounds by run count, the length-fourteen minimum, or the two-parameter witness family. Targeted searches compared equivalent formulations, possible stronger theorems, exact tables and claim-versus-prior logical implication. Coverage beyond indexed and accessible sources remains unproved.

## Mathematical value

**PASS.** The SUPS answer count is a natural output parameter in stringology, and the number of constant runs is a standard compressed representation. The result identifies the first structural regime with three simultaneous optimal answers, an exact minimal-length boundary and an unbounded witness family. These are precise infinite-family, tight-threshold statements rather than a numerical census detached from an invariant.

## Limits and closest literature

The theorem does not settle existence of four simultaneous SUPSs in unrestricted binary strings or classify all longer five-run triples. The finite verifier cannot replace the analytic proof. Historical priority can change if unindexed equivalent work is found. The closest primary texts are arXiv:1903.06290 (2019-03-14), arXiv:2204.07327 (2022-04-15), and arXiv:1608.05550 (2016-08-19).

Self-review: passed. Independent audit: not yet performed.
