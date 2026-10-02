# Independent scientific audit — SCOPE-20260919-329faea3aeba

Audited at: 2026-10-01T12:12:53.903497Z

Disposition: **passed**

## Correctness — PASS

For every even modulus, reduction modulo that modulus preserves integer parity, so applying the binary Laplacian after one modular insertion gives exactly the second binary update. For binary input and odd modulus exceeding the mask degree, each raw Laplacian value lies in the bounded interval determined by the mask degree, and modular reduction wraps exactly once precisely at negative values. Negativity is exactly the active inner boundary indicator, yielding the claimed binary boundary correction. Linearity over the two-element field and locality then give the iterated boundary pulse, finite-speed support, and schedule-parity consequences. The inspected repository verifier checks the identities across representative masks, states, even moduli, large odd moduli, and schedules; it is consistent evidence rather than the general proof.

## Originality — PASS

The motivating paper already proves the common parity class for sufficiently large odd inserted moduli and reports even moduli as binary-like, but it does not state the exact erasure identity for all even moduli, the active-boundary correction, or the all-time schedule quotient. Semantic search returned this record as the exact hit; the nearby prime-power digit-factorization record concerns constant-modulus renormalization rather than time-dependent insertion parity.

### Equivalent formulations

The final theorem is not a mere renaming of the source's odd-modulus parity observation.

### Broader coverage

Neither broader result supplies the exact time-dependent parity-word quotient claimed here.

### Exact database or table

No database/table coverage was found; novelty rests on implication comparison, not search failure.

### Claim versus prior implication

Although the algebra is elementary, the all-time schedule equivalence and localized boundary mechanism are not already contained in the inspected source.

## Value — PASS

The theorem turns a computational even/odd dichotomy into an exact operator statement, identifies the geometric forcing as a finite-speed boundary pulse, and gives schedule equivalence classes valid for all subsequent binary phases. That is a motivated structural explanation of the source phenomenon, despite the elementary algebra.

## Sources inspected

- Long-Lived Carpet-Like Transients in Time-Dependent Modular Discrete Laplacian Dynamics — https://arxiv.org/abs/2609.20416. INACCESSIBLE_PLAUSIBLE_SOURCE: The accessible material confirms the source's higher-odd synchronization and finite-horizon scope. The full text was not available for inspection, so whole-document noncoverage is not asserted.

## Checked sources

- https://arxiv.org/abs/2609.20416
- https://arxiv.org/abs/2509.05815
- semantic research-index search

## Residual risks

- The source full text was not independently obtained in this run, so an unindexed stronger lemma elsewhere in the paper remains a concrete originality risk.
- The core parity reductions are elementary; the value lies in the exact operator/schedule consequences for the active model rather than in difficult algebra.

## Limitations

- The odd boundary formula requires binary input and modulus larger than the mask degree.
- The theorem does not settle smaller odd moduli or long-time persistence of carpet-like regimes.
- The accessible primary source was incomplete in this audit, and that access risk is recorded explicitly.
