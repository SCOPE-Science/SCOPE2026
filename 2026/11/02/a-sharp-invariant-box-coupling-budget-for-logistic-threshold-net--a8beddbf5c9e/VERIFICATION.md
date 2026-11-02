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

The independent audit channel is not performed. The scientific claim has a same mathematical model proof review only.

Run `python3 verification.py` from the extracted research package; no third-party Python dependencies are required. Actual replay produced `PASS: row sums, 4 non-equitable cross weights, 9 beta ranges, contraction, four numerical fixed points, sharpness and cusp checks`. In the four-node example at beta=8, leakage 0.15 is below epsilon*=0.15606521549378 and the contraction-rate bound is 0.029066962173548.

The source of the infinite-dimensional quantified conclusion is the inward-face and contraction argument written in RESULT.md, not numerical iteration. The program checks a representative non-equitable example and scalar identities but does not independently establish source priority, exhaustive equilibrium counts, or convergence of every trajectory outside the specified boxes.
