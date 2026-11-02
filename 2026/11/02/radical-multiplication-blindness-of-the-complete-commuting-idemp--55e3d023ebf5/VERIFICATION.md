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

# Reproducibility and scope

The included `verify.py` uses only the Python standard library. Execute `python verify.py` from the directory containing the extracted file. It independently constructs the multiplication of the path algebra and the three-arrow radical-square-zero algebra on six basis elements, enumerates all elements for fields of prime orders two and three, finds all idempotents, computes commutation, counts ordered pairwise-commuting triples with repetitions, and enumerates maximal cliques by backtracking.

Observed:

```
CHECK_OK field=2 algebra=square_zero tuples=[1, 26, 340, 3368] maximal={8: 8}
CHECK_OK field=2 algebra=path_algebra tuples=[1, 26, 340, 3368] maximal={8: 8}
CHECK_OK field=3 algebra=square_zero tuples=[1, 56, 976, 10592] maximal={8: 27}
CHECK_OK field=3 algebra=path_algebra tuples=[1, 56, 976, 10592] maximal={8: 27}
VERIFY_OK
```

The tuple predictions are evaluated from the color sum, rather than from multiplication in the same algebra. Graph maximal-clique sizes and multiplicities are computed independently of the orbit-stabilizer proof. Exhaustive testing was performed only in these four small finite examples; no computation proves the infinite parametric theorem. For general finite fields, dimensions, and tuple arities, verification rests on the explicit conjugation, stabilizer and Stirling-inversion proof in RESULT.md. Independent mathematical audit has not been performed.
