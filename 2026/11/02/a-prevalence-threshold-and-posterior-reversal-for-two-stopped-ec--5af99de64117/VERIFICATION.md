---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every state h, conditional survival integration yields mean stopped cost c_i(1-exp(-lambda_hi*t_i))/lambda_hi. Subtracting AB and BA factors precisely as (1-u_hA)(1-u_hB)(c_A/lambda_hA-c_B/lambda_hB), and mixing by the occupancy prior gives a single affine crossing iff signs oppose. A no-alarm prefix independently weights each state by S_h; Bayes posterior is the same interchange criterion times a strictly positive reach probability. All zero and boundary D_h cases follow from the exact affine identity. Independent rational substitutions reproduced D0=3/16, D1=-35/512, pi*=96/131, no-alarm posterior 9/13, and prefix interchange difference 69/40960; inspected checker_ordering.py tests direct stopped labor rather than assuming the formula. Domain: two prescribed positive-duration, positive-rate, positive-cost blocks, fixed latent state, immediate alarm stop and no sequence-dependent terminal charges. No general adaptive-policy optimality asserted.

## originality

PASS

Best-of-knowledge distinct stopped-time labor interchange and posterior switch, not a new general two-job sequencing principle. Explicit continuous survival weighting and exact informative false-alarm reversal distinguish fixed per-inspection sequencing results. Close older abstract-level general scheduling results remain a genuine risk.

## value

PASS

The exact sharp prevalence threshold and an informative-block posterior reversal produce a reproducible qualitative scheduling boundary: the same two informative sensors reverse order solely after a negative alarm history, while consumed labor is measured continuously. This motivated two-state stochastic inspection specialization is useful for diagnosing why a fixed static sensor order can be suboptimal. It does not claim a new generic adjacent-interchange theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
