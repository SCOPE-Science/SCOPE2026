# Scientific review

## Correctness — PASS
The proof reduces all mutual-inverse entries to products of interval-transversal incidence entries. Induction on the final variable proves the required full row rank without genericity assumptions. A real singular-value decomposition then gives every positive, negative and zero eigenvalue count; Vandermonde identities sum the image-rank blocks. Direct exact enumeration (`verify.py`) and a separate numerical eigensign check (`verify_eigensigns.py`) agree for chain sizes through five. Finite checks are supporting evidence only.

## Originality — PASS, qualified
The closest recent source is Higgins's 2026 balanced-weighting theorem for permutation matchings of order-preserving transformation monoids; its abstract does not report real inertia, but the full text was inaccessible. Higgins's accessible 2024 paper and relevant 2019/2015 material address matching and inverse-subsemigroup structures rather than the precise spectral signature. Existing inverse-degree formulas are prior work and are not presented here as novel. No exact rank/inertia formula was found in the bounded scientific searches. An unindexed or inaccessible equivalent source remains a risk.

## Mathematical value — PASS
The mutual-inverse adjacency matrix is the natural finite matrix underlying matching questions. The theorem computes the complete sign signature of its spectrum in every image-rank stratum and yields a central-binomial global rank; neither property is fixed by known vertex-degree statistics or a perfect-matching theorem.

## Limits and prior comparison
The theorem concerns real inertia, not individual nonzero eigenvalues or existence of involution matchings. The directly relevant 2026 full primary text could not be inspected; its abstract and public bibliographic data were read. The general proof and standalone verification instructions are in `RESULT.md` and `verify.py`.

Self-review: passed. Independent audit: not yet performed.
