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

# Verification notes

The complete proof is in `RESULT.md`. A finite experimental check cannot establish equivalence for all degrees; here that step uses the algebraic classification of eight pointed extension profiles and the classical permutation square-root condition.

Run under Python 3 (standard library only):

```
python exact_symmetric.py --n9
python verify_symbolic.py
python verify_sentences.py
```

`exact_symmetric.py` enumerates every first move up to conjugation and every possible second move for degrees one through eight, then repeats for degree nine to check the first stabilized example. It compares complete atomic two-variable diagrams in the language with a named identity and ternary product relation; no stronger language is used. It writes `exact_output.json` next to itself.

`verify_symbolic.py` independently enumerates cycle partitions and implements the parity criterion for permutation square roots, checking the asserted seven- versus eight-profile cutoff through degree forty. `verify_sentences.py` independently evaluates the exact five distinguishing sentences through degree eight. `verification.log` records the actual successful runs; each of `EXACT_VERIFY_OK`, `EXACT_NINE_OK`, `SYMBOLIC_VERIFY_OK`, and `SENTENCES_VERIFY_OK` was obtained. These finite checks do not independently validate the infinite logical argument or establish originality.

Remaining limits: The mathematical argument assumes the ordinary Ehrenfeucht–Fraïssé theorem for relational structures, and the square-root criterion is a previously published theorem cited in the result. Formal mechanized proof and external independent scientific audit were not performed.
