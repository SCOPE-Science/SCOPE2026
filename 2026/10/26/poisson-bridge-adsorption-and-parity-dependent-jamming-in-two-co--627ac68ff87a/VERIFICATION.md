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

# Reproducible verification

Run `python verify.py` with Python 3.9 or later. The code uses only the standard library. Its observed output included `PASS 1923 exact transition, full-graph comparison, and Lyapunov assertions`.

The code checks exact conditional transition probabilities of the reduced process against an independently enumerated labeled-graph process for sizes two through five and three exact rational rate ratios; verifies the key potential drift bound for all reachable-form count triples with both class sizes up to eleven; and reports exact-rational cross-count and defect probabilities for larger finite instances. The displayed numerical trends are examples, not a proof of the Poisson limit.

The infinite-size proof requires (i) the explicit normalized Markov drifts, quadratic-variation estimates, and deterministic ODE, (ii) the Poisson random-time-change representation, (iii) the superharmonic potential uniform tail bound, and (iv) the exact parity identity. The verification program does not certify those infinite arguments independently.

The source comparison is limited by inaccessible historical full text. Neither historical priority nor independent certification is claimed.
