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

Run `python3 verify.py` from this package with Python 3.9 or later. The script uses the standard library only and prints `VERIFY_OK 308 independent exact rational and polynomial comparisons` after finishing. It checks complete independent union-find enumerations of all acyclic subsets for four small bipartite graphs, all three edge-pair orbits, and four rational fugacities. It additionally uses polynomial-degree bounds and interpolation across 55 integer pairs to verify the identities behind the positive certificate for **all** formal parameter values. This verifies the algebraic identities rather than inferring the theorem from numerical data.

The all-size argument also depends on the independently stated graph-theoretic classification of allowed right-column patterns and on elementary positivity of the displayed factors. No external proof assistant, independent reviewer, or certification channel was used. The model requires equal edge fugacities; arbitrary edge-dependent activity, full negative association, and the general forest conjecture are unproved here. Historical priority remains subject to further independent checking.
