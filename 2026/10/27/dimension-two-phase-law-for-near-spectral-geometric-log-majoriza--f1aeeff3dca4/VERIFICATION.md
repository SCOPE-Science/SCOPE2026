---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the dimension-two spectral-curve comparison

## Analytical reconstruction

The verification concerns the stated universal theorem for complex Hermitian positive-definite \(2\times2\) matrices. Independently reconstructing the proof shows: (i) both curves have identical scalar homogeneity and determinants, allowing determinant-one normalization; (ii) the exact square-root formula gives \(M=(A^{-1}+B)/K\) and \(N=(A^{-1}+D)/K\); (iii) the weighted commutator square establishes \(\operatorname{tr}N\ge\operatorname{tr}M\) with equality exactly at commutativity; (iv) the two-eigenvalue power identity and the derivative of \(s\coth s\) establish the strict sign for every real parameter; and (v) trace ordering at common determinant is exactly log-majorization in two dimensions. The proof treats repeated eigenvalues by continuous extension at the zero hyperbolic parameter.

## Reproducible exact tests

Execute `python3 check_near_spectral.py` using a standard Python 3 interpreter, with no external packages. Actual observed output:

```
PASS: 896 exact rational identities and inequalities
```

The included checker tests only finite rational cases, including matrix dimensions 2–4 for the commutator identity and determinant-one \(2\times2\) examples for the spectral-curve normalizations. No extrapolation from finite checks is used to prove a universal statement.

## Open limits

The main result is limited to \(2\times2\) matrices, and no Loewner comparison is asserted. The 2025 foundational near-geometric source could not be fully inspected; this is a priority risk, not a mathematical proof gap. No independent audit has been performed or is represented as completed.
