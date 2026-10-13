# Scientific review

## Correctness — PASS

Legendre's factorial valuation formula gives the exact digit-sum reduction after stripping the power of three from \(n+1\). The endpoint/primitive-unit partition is disjoint and exhaustive. The explicit two-state matrix tracks carries from low to high ternary digits, including the final carry. Its trace, determinant and two initial polynomials imply the recurrence and the claimed rational generating function. Singularity extraction at the unique pole \(z=1\), performed after extracting a fixed power of the formal variable \(q\), proves the fixed-valuation asymptotics. The polynomial-degree recurrence proves the maximal-valuation count for \(m\ge2\); smaller scales are correctly excepted. A standalone verifier corroborates these identities for the stated finite ranges.

## Originality — PASS, with remaining risk

The closest manuscript, Eu–Huang–Kao (2026), explicitly supplies a pointwise ternary valuation lemma and the valuation-zero cardinality; these are acknowledged as prior art and are not claimed as new. Its zero-run spectra count consecutive zeros modulo primes, not complete histograms of the valuation of each term. The present bivariate rational frequency generating function is a strictly different aggregate invariant; its higher-valuation coefficients and arbitrary-fixed-prime-power asymptotics are not consequences of the source's stated zero-run enumerations alone. Full-text review of Bobrowski–He–Shiue (2019), Krattenthaler–Müller (2025), and the OEIS A006013 entry found no stronger covering frequency formula. The digit-valuation lemma could admit an unpublished or independently known transfer-matrix summation, and finite published-finding corpus/web searches cannot establish uniqueness; this remains a real risk.

## Value — PASS

This supplies exact frequencies for every three-adic valuation, rather than just nondivisibility modulo the prime. On prefixes of natural size \(3^m\), it identifies the degree \(2r\) and the exact leading coefficient of the surviving count for each prime-power modulus \(3^r\), and determines the rare maximal-valuation class. The invariant is naturally motivated by the prime-modulus census and its pointwise carry lemma, not by an arbitrary isolated index or ad hoc residue slice. The two-state proof explains the entire collection simultaneously.

## Scope and validation limitations

Finite computations are corroborative only. The result is not a residue-class formula modulo prime powers and does not include other Raney parameters. The prior paper's prime-level nondivisibility formula is reproduced as a specialization and excluded from novelty. Review of unindexed mathematical literature and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
