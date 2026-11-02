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

The exact finite stage law was independently recomputed with `fractions.Fraction` in `verify.py` for \(2\le d\le12\) and \(2\le q\le6\). The script checks that all mixed-event probabilities sum with the all-synchronized terminal atom to one, verifies the binomial/bridge boundary law, and exhaustively counts random-walk bridges for \(d\le7\). It also evaluates fixed-\(q\) large-\(d\) mean and two-laggard constants as supplementary diagnostics. Full execution returned `PASS 3278 exact finite and supplementary numerical checks`.

The infinite asymptotics rest on the displayed product, its uniform local expansion, a Gaussian tail estimate, and controlled Euler--Maclaurin sums; the finite checker does not establish the infinite claim. No independent mathematical audit has been performed.
