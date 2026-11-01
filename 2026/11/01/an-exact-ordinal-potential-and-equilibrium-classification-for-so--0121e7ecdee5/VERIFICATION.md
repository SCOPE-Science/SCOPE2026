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

# Reproducible checks

Run `python3 verification/cactus_check.py` using Python 3.10 or later, without third-party dependencies. The deterministic script constructs cactus hosts, enumerates their cycle-deletion states, and compares all legal unilateral deletions and bilateral additions against exact threshold calculations. It also checks the welfare additivity identity, optimal welfare, stable-state counts, strict potential increase for every profitable move, and connected-subgraph completeness for small hosts.

Recorded run: `PASS: 1093 cactus/parameter instances, 26710 states, exact pairwise moves, welfare and potential`; `Connected-state exhaustive equality: 1526 states checked via every edge subset`; `Eleven-vertex example: host welfare 450, optimum 480`.

All model payoffs and comparisons in this script are evaluated using integers or exact rational fractions. This is finite reproducibility, not a proof for all finite cactus graphs. The universal proof is in RESULT.md, Sections 1–5. No external independent validation has been performed.
