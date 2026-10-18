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

# Reproducibility

`verify_dodeca_total3.py` requires only the Python 3 standard library. From this directory, execute:

```sh
python3 verify_dodeca_total3.py
```

The expected deterministic result is `verification_output.txt`.

The program independently constructs the thirty graph edges and all independent triples; enumerates the entire Alexander dual using the six-vertex Ramsey bound; reduces all four integral signed boundary matrices using unit-only unimodular operations; cross-checks the ranks over four small fields; enumerates all graph automorphisms; and computes full signed Lefschetz characters directly on both the original total cut complex and its Alexander dual. It checks all one hundred twenty elements rather than sampling classes.

The exact unimodular pivots, not the finite-field checks, establish integral torsion-freeness. The topological implications use combinatorial Alexander duality and standard Hurewicz and homology Whitehead theorems; no computational output by itself replaces those deductions. The calculation is specific to the supplied dodecahedral graph, total three-cut convention and rational symmetry character. No independent external audit has been performed.
