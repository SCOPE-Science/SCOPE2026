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

# Reproduction and limits

Run `python verify_leaf_wiener.py` with Python 3 and no third-party modules. The program enumerates all 46,233 parent lists for 2 through 9 vertices. For every tree it constructs shortest-path distances by a direct breadth-first traversal, independently of the recurrence proof. It checks exact rational leaf count, Wiener index, the sum of leaf distance centralities, and the covariance identity. Every individual parent choice is further tested for the three conditional-expectation identities for sizes 2 through 7, totaling 5,912 parent transitions. A separate moment recurrence is checked through 200 vertices (198 increments).

Verified local output: `PASS: 46233 recursive trees enumerated (n=2..9); 5912 conditional parent transitions; 198 exact moment-recursion steps`.

Finite checking neither establishes the theorem outside these sizes nor certifies the historical novelty of the formula. The general result has an independent symbolic proof in RESULT.md. The optional asymptotic correlation uses the published Wiener variance asymptotic from Neininger (2002) and is not independently re-established here. No independent audit has been performed.
