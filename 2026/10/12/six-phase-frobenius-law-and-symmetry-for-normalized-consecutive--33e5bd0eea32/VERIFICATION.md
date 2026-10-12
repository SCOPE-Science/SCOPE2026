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
# Reproducible checks and limits

The symbolic proof in RESULT.md establishes the full infinite claim. In each of six residue classes, direct substitution gives the normalized values and a nonnegative witness in the reduced pair. Coprimality of the second-stage gluing and the rectangular Apéry description are checked algebraically. Expansion yields all six Frobenius polynomials; the Apéry-sum identity proves genus and symmetry.

The bundled `verify.py` needs standard Python 3.9+ only. Run `python3 verify.py`; observed output was:

```
EXACT_REGRESSION_OK normalized_triplets=139 n=2..140; six phases; symmetry, Frobenius, genus, and witness checks
```

The check uses an independent shortest-residue-path Apéry calculation to determine \(F\) and genus for each of 139 test indices, compares every exact phase formula, checks all gcd normalization and gluing witnesses, and checks a small named sample. It is not exhaustive over all \(n\); no unbounded claim is justified only by those computations.

The classification is for gcd-normalized consecutive triples only. Broader literature and direct unindexed equivalents remain residual originality risks. External independent audit has not been performed.
