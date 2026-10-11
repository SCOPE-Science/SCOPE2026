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

# Reproducible checks and limits

The provided `verify.py` was executed using Python with SymPy against the exact vector field defined in the finding. It printed `PASS: exact Lie derivative, equilibrium plane, endpoint and extremal identities`. It checks the Lie derivative of \(\Phi=w-bxy\), parameter specializations at \(b=-1\) and \(b=-2\), the equilibrium plane, and the restrictions \(\dot z=wy\), \(\dot w=-y^2\) when \(z=0\).

Run `python verify.py` from the directory containing this document and script. The script performs symbolic identity checks only: it does **not** certify invariant-set arguments, invariant-measure support, or the periodic Wirtinger inequality and its equality case. Those statements are proved analytically in `RESULT.md`. No numerical trajectory integration or finite parameter enumeration is used as a substitute for a global proof.

The original 2016 six-page published PDF was inspected in full at https://sprott.physics.wisc.edu/pubs/paper443.pdf; equation (6) is the source for the original vector field. A related 2019 article by Bayani and collaborators was reviewed at abstract/bibliographic level only, and possible coverage in its unavailable full text remains an explicit originality risk. No independent audit has been performed.
