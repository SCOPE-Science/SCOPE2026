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

# Reproducibility and limits

Run `python3 verify.py` from the extracted complete package. This checks exact integer identities and the nonzero determinant for the binary Jacobian problem, not a finite experimental extrapolation. The proof of smoothability uses base-locus analysis and Bertini; preservation of the Milnor number uses the classical semiquasihomogeneous theorem. The six points, exceptional del Pezzo surfaces, and resolved Euler number are independent inputs explicitly identified in Burek, arXiv:2610.01276v1, §§3–4 and Remark 8.4. No independent audit has been performed. The exact Hodge pair is not determined; the stated lower bound is proved.
