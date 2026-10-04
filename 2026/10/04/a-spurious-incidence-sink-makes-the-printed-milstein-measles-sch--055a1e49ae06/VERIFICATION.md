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

The bundled `verifier.py` reconstructs the deterministic drift terms from the stated six-compartment model and from the printed Milstein scheme. It checks symbolically that the inserted deterministic term is \(-\beta SI/N\) in the infected update, that the target total drift is \(\Lambda-\mu N-\phi_1I\), and that the printed Milstein total drift is smaller by exactly \(\beta SI/N\).

It also checks the exact witness \(\beta=1/20\), \(S=I=1\), \(E=V_1=V_2=R=0\), for which \(N=2\) and the spurious drift equals \(-1/40\).

Run with a standard Python interpreter with SymPy available. Expected terminal output is exactly `VERIFY_OK`.

The checker verifies algebraic consistency, not article implementation history. No source code for the published figures was available, so the claim does not assert which formula was executed by the authors.
