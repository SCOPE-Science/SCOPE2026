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

# Reproducibility and scope

Run `python verify.py` with SymPy installed. The script uses exact symbolic differentiation and rational arithmetic to establish the displayed quartic Lie-derivative identity, the Gram determinant identity, and the quartic SOS identity, as well as exact rational data for a locked-angle example. A suite of 120 rational substitutions is diagnostic only, not an infinite-domain proof. The proof in `RESULT.md` supplies the all-parameter strict inequalities, invariant-ray necessity, and symmetrization degree lower bound. No external independent audit or formal proof certification has been performed.
