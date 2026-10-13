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

`artifacts/verify.py` is a standalone Python standard-library replay. It checks the two six-line lists exactly over the integers, reconstructs projective concurrency classes by cross products, evaluates the common conic, and tests transversality using the dual-conic condition \(25a^2+25b^2-c^2\neq0\). It then uses Bézout to count residual conic-line nodes and verifies:

- both global weak multiplicity vectors are \(t_2=6,t_3=3,t_4=2\);
- the conic profiles are \((4,1,2)\) and \((2,2,2)\);
- the line singular-point counts are \((4,3,3,5,4,3)\) and \((3,6,3,4,4,3)\);
- the conic contains \(7\) and \(6\) singular points, respectively;
- the resulting \(r_j\) sequences differ exactly as stated.

The verifier is finite and exact; it does not recompute the source’s Jacobian syzygy resolutions or prove any statement about other realizations. Successful replay ends with `VERIFY_OK`.
