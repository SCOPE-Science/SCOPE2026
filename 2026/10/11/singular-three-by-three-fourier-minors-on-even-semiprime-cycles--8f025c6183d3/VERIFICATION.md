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

# Reproducibility and evidence limits

Execute `python3 verify_minors.py` with Python 3.9 or later. The program requires only the Python standard library and enumerates every row/column three-point pair for \(p\in\{3,5,7\}\) in exact integer arithmetic. It evaluates the determinant in the quotient \(\mathbb Q[X]/\langle\Phi_p(X)\rangle\), not by floating-point cancellation. The expected singular counts are \(48/400\), \(1600/14400\), and \(11760/132496\). All passed on the package source artifact.

The infinite theorem uses Loukaki's published fiber-matching Fourier minor theorem and classical Chebotarev prime-order nonsingularity, followed by a complete parity/collision case analysis. The finite verifier checks only three specified primes. This verifies arithmetic consistency but not the whole theorem and is not external or independent review. Unrestricted literature completeness has not been proved.
