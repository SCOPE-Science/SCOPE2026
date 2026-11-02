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
# Verification of the flat Möbius–cylinder distance theorem

The proof in `RESULT.md` applies to every positive horizontal period and vertical half-width. For reproducible finite corroboration, extract `verify_geometry.py` beside this file and run:

```sh
python3 verify_geometry.py
```

The Python 3 standard-library checker uses rational arithmetic for all enumerated lift comparisons, and a deterministic random seed plus Simpson integration for selected distributional comparisons. The completed extraction-and-execution reported 7,203 exact lift comparisons, 750,009 seeded checks, 12 endpoint scaling checks, and 4 derivative-transition checks, totaling 757,228 passes.

The crucial infinite-domain statements require the analytic deck-minimization, diamond-domain integration, positivity and asymptotic arguments in `RESULT.md`. A finite run cannot establish them; it also does not prove worldwide novelty. In particular, Sabitov's 2007 full text could not be inspected in this review, and no independent audit is claimed.
