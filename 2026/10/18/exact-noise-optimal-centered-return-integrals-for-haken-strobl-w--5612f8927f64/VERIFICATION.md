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

Run `python verify.py` after installing `requirements.txt`. It directly constructs the full \(n^2\)-dimensional complex Lindblad generator for each finite \(K_{a,b}\), solves the trace-zero steady-state resolvent rather than reusing the reduced analytic equations, and compares the return integral against the theorem. It separately checks the reduced integrated equations with exact rational arithmetic, including \(a=1\) and \(b=1\), and evaluates the proposed optimum against nearby dephasing strengths. See the verifier's printed count. The proof of exponential relaxation and the formula for arbitrary positive integers are analytical; finite checks cannot certify them universally. No independent audit or human validation has been performed.
