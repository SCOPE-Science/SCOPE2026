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

# Verification record

The proof is in `RESULT.md`. The standalone checker `verify.py` uses dependencies specified in `requirements.txt`; execute `python verify.py` from this directory. Its actual recorded stdout is in `verification_output.txt`.

The executable verifies exact symbolic convolution and asymptotic identities, nine direct split-integral evaluations of the original ambiguity function, and nine roots obtained by solving both real equations to high precision. It checks the positive limiting delay and a positive transversality derivative for each parameter pair. The three tested pairs are \((a,b)=(1,1/2),(2,1),(1,4/5)\). The found roots verify the stated convergence trends and are not used as substitutes for the analytic implicit-function theorem.

The mathematical argument covers every fixed real \(a>b>0\) and all sufficiently large integer indices. Neither finitely many numerical roots nor symbolic simplification alone proves that unrestricted claim; the proof needs the derivative-nondegenerate limiting equation and analytic continuation in reciprocal index. Published-source priority and independent validation remain unverified.
