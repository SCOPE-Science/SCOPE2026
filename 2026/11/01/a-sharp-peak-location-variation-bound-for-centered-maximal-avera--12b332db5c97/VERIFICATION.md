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

The argument uses only finite real averages and inequalities, with no unproved numerical assumption. The key nonstandard step is proved in `RESULT.md`: shifting a center one step toward a unimodal peak while shrinking the radius by one removes only values no larger than the previously maximal average. This gives unimodality of the centered maximal output even with endpoint-truncated balls. The variation identity and the two endpoint lower bounds then prove both estimates for arbitrary real nonnegative unimodal inputs.

Run `python3 unimodal_verify.py` using the standard Python library. Exact rational tests executed successfully: 4,332 exhaustive unimodal sequences (lengths 3--8, values 0--3), 4,800 deterministic longer sequences (lengths 9, 12, 20, and 35), and 5,047 single-spike boundary tests (orders 3--100). They test identities, inequalities, strict interior peaks, and simultaneously sharp endpoint examples. These finite computations are not a proof for arbitrary lengths or real inputs.

The factor \(1-1/n\) is sharp in the unimodal class because of endpoint single spikes; the stronger location-bound is attained by a single spike at **each** location. The results do not settle the arbitrary-input path conjecture, quantify other modes of oscillation, or constitute independent validation.
