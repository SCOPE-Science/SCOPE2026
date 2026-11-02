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

# Verification and reproducibility

Run `python3 verify.py` in a directory containing the bundled standalone script. It uses Python 3 and the standard library only. It constructs matrices for \(1-T\) on explicit finite prime-field vector spaces, generates binary-operation terms via finite coefficient closure, and computes all equational codimensions for the tested arities by exact finite-field linear algebra. It also evaluates the polynomial and orbit-count formula for four small cardinalities. Its completed output was:

```
F2 quadratic irreducible: |R|=4, Latin=True, arity=2, terms=4, equation ranks=(0, 2)
F2 two identical irreducible blocks: |R|=4, Latin=True, arity=3, terms=16, equation ranks=(0, 4)
F3 scalar -1: |R|=3, Latin=True, arity=3, terms=9, equation ranks=(0, 2)
F3 nonlatin nonprojection: |R|=9, Latin=False, arity=3, terms=27, equation ranks=(0, 1, 2)
F3 nonsemisimple latin: |R|=9, Latin=True, arity=3, terms=81, equation ranks=(0, 1, 2)
F5 split semisimple latin: |R|=25, Latin=True, arity=2, terms=25, equation ranks=(0, 1, 2)
F2 projection: |R|=2, Latin=False, arity=3, terms=3, equation ranks=(0, 2)
order=2: types=1, labeled=1
order=4: types=2, labeled=3
order=3: types=2, labeled=2
order=9: types=5, labeled=15961
VERIFY_OK
```

The pair `equation ranks=(0, 2)` over \(\mathbb F_2\) indicates probabilities \(1\) and \(1/4\); ranks \((0,1,2)\) over \(\mathbb F_3\) indicate an intermediate \(1/3\) between \(1\) and \(1/9\). The verifier is a finite consistency check, not an infinite proof or independent certification. The general sufficiency, necessity, representation-theoretic and counting arguments are given in RESULT.md. Historical novelty cannot be certified by running this script.
