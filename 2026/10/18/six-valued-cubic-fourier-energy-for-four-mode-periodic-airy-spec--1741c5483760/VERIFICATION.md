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

The standalone standard-library program `verify_energy.py` uses integer arithmetic exclusively. On execution it checks the six explicit witnesses and all \(\binom{31}{4}=31465\) four-element integer supports inside \([-15,15]\), checking cubic/linear triple fibers and their multiplicity types. In a completed run it printed:

`VERIFY_OK six attainable levels; 31 choose 4 = 31465 exact supports; counts=256:30758, 262:168, 274:14, 340:420, 400:105`

The less common level \(268\) has an explicitly verified witness outside the enumerated interval. The analytic proof, not the finite census, establishes the universal six-valued classification and strict-positive dichotomy. The work has not received independent audit.
