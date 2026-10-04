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

The symbolic checker `verify.py` independently reconstructs the algebra from the published vector field. It checks the stationary elimination, substitutes the nonzero relation \(u^2=2ab/e\), recomputes \(\det(\lambda I-J)\), specializes the result to \((a,b,c,d,e,m,k)=(15,43,1,16,5,5,2)\), and verifies the exact Routh first-column entries.

Running `python3 verify.py` in the package directory returns `VERIFY_OK` using exact symbolic and rational arithmetic. No floating-point computation is needed for the proof. The checker does not address global attractors, numerical Lyapunov exponents, or any independent literature certification.
