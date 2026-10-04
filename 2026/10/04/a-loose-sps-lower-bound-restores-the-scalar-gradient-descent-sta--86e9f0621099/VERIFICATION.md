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

The proof in `RESULT.md` is self-contained and analytic. `verify.py` replays the SPS update directly from its defining formula on representative parameter choices. It checks the exact two-cycle numerically for several values with \(q\ge2\), verifies the stability-index formula on that cycle, checks agreement of the normalized piecewise map with the original update, and stress-tests representative \(q<2\) trajectories.

The finite numerical tests do not certify the universal statements. Those statements rely on the branch inequalities and limiting contradiction in the proof. No claim is made beyond the deterministic scalar quadratic with a constant cap and a constant valid strict lower-bound error.
