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

# Verification and reproducibility

Run `python verify.py` with Python 3, SymPy and NumPy. It checks the following from first principles:

- Exact characteristic polynomials for all tested \(4\le n\le10\) and all allowed exceptional-edge separations.
- Exact Chebyshev product-difference identities for all tested consecutive separations.
- Independent exact characteristic determinants retaining the symbolic cycle flux for \(4\le n\le8\), with two rational parameter pairs.
- Hermitian support-function order at 49 angles for six positive-weight pairs (both enhanced, both weakened, and mixed), for dimensions \(4\le n\le12\).

Observed replay: `PASSED: 39 exact zero-flux identities; 28 exact flux identities; 7350 numerical support comparisons`.

The exact symbolic checks establish only the stated finite cases; the sampled floating-point support inequalities are not interval certificates. The general proof instead relies on the matching-polynomial identity, the Chebyshev recurrence, eigenvalue interlacing, and support-function compactness. Bibliographic originality has not received independent peer assessment.
