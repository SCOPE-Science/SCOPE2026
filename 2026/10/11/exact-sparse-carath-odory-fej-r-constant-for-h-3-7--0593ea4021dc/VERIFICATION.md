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
# Verification

The proof is analytic. `artifacts/verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt5)\) implemented with Python's standard-library `fractions.Fraction`. It verifies the upper-certificate identity, candidate contacts, Chebyshev factorization, Bernstein representation and positivity, derivative identities, and uniqueness determinant.

Run:

`python3 artifacts/verify.py`

Expected terminal line:

`VERIFY_OK exact_upper=1 factorization=1 bernstein_positive=6 uniqueness=1`

No finite sample or floating-point scan is used to infer nonnegativity on the continuum. The checker verifies algebraic identities only; the mathematical proof explains why the positive Bernstein representation implies \(R(x)>0\) for every \(x\in[-1,1]\).
