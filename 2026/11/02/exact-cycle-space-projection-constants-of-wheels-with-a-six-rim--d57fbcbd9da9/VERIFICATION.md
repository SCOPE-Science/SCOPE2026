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

# Reproducibility and verification

Run `python3 wheel_projection_verify.py` with Python 3 and no external dependencies.

The checker uses exact rational arithmetic for every displayed primal vector and finite dual certificate. It constructs each projection from the proposed cyclic columns, checks all facial cycles are fixed, checks the full edge-column norm, and validates the cancellation constraints. It checks the Laurent identity algebraically as a finite integer-polynomial identity, which is the core of the all-size proof, and checks its cyclic representatives for rim sizes from 7 to 200. The observed output was:

`CHECK_OK 109531 exact rational and Laurent identities n=3..200`

No sampling over a finite range by itself establishes the theorem for arbitrarily large graphs. The separate proof in `RESULT.md` uses a formal Laurent identity valid for all positive rim lengths and verifies the only possible support overlap at rim size seven. The cyclic symmetrization lemma is a direct finite-group averaging argument. No external independent review, third-party certification, or formal proof assistant verification has been performed.
