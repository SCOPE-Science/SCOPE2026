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

# Verification

The universal statements follow from the direct support-and-mean proof in `RESULT.md`. The core closure lemma for an integer \(b\ge2\) is exact and needs no numerical approximation. A strict three-atom counterexample proves the converse for every other contraction in \((0,1)\). The inequality \((Z-m)(Z-m-1)\ge0\) for integer \(Z\) proves the universal sharp variance floor. The geometric survival-tail sum proves the extinction expectation.

The standalone `verify.py` uses Python's `fractions.Fraction` for exact arithmetic and is runnable with `python3 verify.py`, without installed third-party packages. A completed run returned:

```
VERIFY_OK exact_fixed 7100 variable 208 nonreciprocal_witness 130 variance_example 124/625
```

These are bounded diagnostic checks of exact identities. They do not prove the all-parameter statements, which rest on the written reasoning. No independent audit or external formal certification has been performed. Numerical-lattice modeling limitations and the searched-but-not-exhaustive novelty evidence are stated in `RESULT.md` and `REVIEW.md`.
