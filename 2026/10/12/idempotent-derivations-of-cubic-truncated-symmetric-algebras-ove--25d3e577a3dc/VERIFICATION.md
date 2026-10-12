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

# Reproducibility and proof limits

The accompanying standalone `verify.py` uses only the Python standard library and constructs derivation matrices on the basis consisting of the unit, degree-one monomials, and unordered degree-two monomials. Every candidate checked is tested for \(D^2=D\) by matrix multiplication, then its full linear rank is obtained by Gaussian elimination in the corresponding finite field.

Run `python3 verify.py` from the directory containing this file. It ends with `VERIFY_OK` only after assertions pass. Exhaustive checks are made for \((n,q)=(1,2),(1,3),(1,5),(2,2),(2,3)\), including all quadratic coefficients of degree-one generator images. A separate full scalar-image check handles \(n=1\), characteristic three, where cubics can admit derivations with nonzero scalar images before imposing idempotence. A direct \(\mathbb F_4\) check handles \(n=1\). Deterministically seeded random cases \((n,q)=(3,2),(2,5)\) and explicit quadratic-shear constructions in \(n=2,3,4\) are additional checks, not exhaustive verifications of those dimensions.

For \(\mathbb F_2\), the theorem predicts \(1+112t^2\) at \(n=2\) and \(1+269312t^3+28672t^4\) at \(n=3\); the former is exhaustively recovered, and the latter is checked by the symbolic proof and sampled matrix calculations, not exhaustive enumeration. The algebraic proof (particularly the characteristic boundary, quadratic-shear conjugacy, and projection-complement count) is needed for arbitrary fields and all dimensions. No independent external audit is claimed.
