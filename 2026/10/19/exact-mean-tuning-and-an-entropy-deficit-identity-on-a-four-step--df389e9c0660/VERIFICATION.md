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

# Verification of the mean-tuning and entropy-deficit identity

The analytical proof in `RESULT.md` establishes the statements for every real \(s>1\). `verify.py` uses only the Python standard library and verifies exact rational consequences at 190 parameters, including all four postcritical boundary equalities, interval lengths, normalized step-density and Frobenius--Perron equations, invariant masses, exact mean integral, and sign of its derivative. It additionally evaluates the Perron polynomial and the KL entropy-deficit equality numerically at nine parameters. An exact rational test over finitely many parameters is not a proof of the universal identities; those follow from the explicit algebra in `RESULT.md`.

Reproduce from the package directory with `python verify.py`. Verified output:

```
PASS: 190 exact-rational Markov, density, mean, and derivative tests;
      unique ternary-root check and entropy--KL identity at 9 parameters.
```

The Markov-to-topological-entropy equality and acip physicality invoke standard primitive piecewise-expanding Markov results, for which explicit hypotheses are verified in `RESULT.md`. The entropy formula also follows from the generating Markov partition. No finite experiment is used to certify almost-everywhere behavior or uniqueness of an arbitrary invariant measure. No independent validation has occurred.
