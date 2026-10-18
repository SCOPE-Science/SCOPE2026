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

The standalone `verify.py` is Python 3 standard-library code and runs with `python3 verify.py` without packages or network access. It is included with the six main documents in the same artifact bundle.

For \(p=3,5,7,11,13,17,19,31,127\), the program constructs the operator \(I-T_{-1}-T_2\) on the basis \(u,u^2,\ldots,u^{p-1}\) and checks the exact kernel dimension \(d_p\). For \(p\le31\), it verifies the \(-1\) and \(2\) eigenrelations, constructs truncated exponentials, and tests their idempotence directly using the original quandle product. In multi-weight cases it checks a mixed parameter point and one quandle multiplication relation in the coordinates. It enumerates every coefficient vector in \(\mathbb F_3[R_3]\) and \(\mathbb F_5[R_5]\), obtaining \(4\) and \(6\) idempotents respectively.

Expected final output line: `VERIFY_OK`.

The general proof rests on the explicit group-ring identity, the filtration argument, truncated logarithm and the semisimple character decomposition. The finite checks are independent corroboration only. The scheme-theoretic statement follows from the same polynomial identities over arbitrary commutative coefficient algebras, not from finite-field point counts. Literature comparisons are not an independent scholarly certification.
