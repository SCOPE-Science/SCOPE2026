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

# Verification and limits

Run `python3 verify_parking_shapes.py` in the extracted package directory with Python 3.10 or newer. It depends only on the standard library. The checker constructs the successful-parking probability from the sequential protocol itself, including every failed-direction branch with exact rational probability. It then checks the derived conditional probability law, ratio identities, sharp finite adjacent thresholds, reflection, and normalizations, and checks large-size trough location against the analytically proved scaling curve.

Observed reproducibility: **6,849 passed assertions**, including **350,476 directly enumerated preference vectors** counted across seven direction probabilities and \(2\le n\le6\). The direct process is independent of the closed-form mass formula, whereas the later algebraic assertions use that formula. The unrestricted results follow from the proof in RESULT.md, not the enumeration. The asymptotic test is a numerical sanity check, not a proof. No independent mathematical validation was performed.
