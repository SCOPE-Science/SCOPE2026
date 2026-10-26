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

# Reproducibility and verification

`verify.py` runs an exact finite Markov-chain absorbing-probability calculation, including the current vertex and full visited-set mask. It checks the resulting cover-terminal distribution against the direct weighted-path formula (1) in `RESULT.md` for three deterministic positive resistance profiles, all starting sites and targets, and all cycle sizes from three through six. It additionally checks the nonconstant fair four-cycle profile and uses symbolic differentiation to check the exact Jacobian and rank formula through ten vertices.

Run with Python 3 and SymPy:

```
python verify.py
```

Expected exact output:

```
PASS exact finite-chain, analytic derivatives and rank checks: 551
```

The calculation passed 551 exact rational or symbolic equalities with the file provided here. It is not an exhaustive test of all real resistance vectors or all cycle lengths; the infinite-length statements are proved analytically using weighted harmonic hitting probabilities and the analytic submersion theorem.

Scientific limits: only finite positive fixed reversible edge weights; local inverse theorem near the homogeneous profile, except a global classification on the four-cycle. Potential implicit overlap with earlier nonuniform cycle termination literature is explicitly disclosed in the scientific review. No independent audit was performed.
