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

The checker `verify.py` uses only the Python standard library. It verifies the following claims independently of the displayed decimal approximations:

1. the Sylvester determinant of \(F(\theta,y)\) and \(K(\theta,y)\) is exactly \(16P(\theta)\);
2. an exact rational Sturm sequence gives exactly two positive roots of \(P\), one in \((0.1666993,0.1666994)\) and one in \((9.706301,9.706302)\);
3. the source eigenvalue equation collapses algebraically because its constant coefficient is zero at \(r=\theta^2\);
4. the reported decimal values lie inside the exact isolating intervals and high-precision numerical evaluation agrees with them.

The factorization over \(\mathbb{Q}(\sqrt2)\) and the common-root formulas are also checked by exact coefficient arithmetic in the construction of the result. The numerical root printout is a readability aid and is not used to certify uniqueness or root count.
