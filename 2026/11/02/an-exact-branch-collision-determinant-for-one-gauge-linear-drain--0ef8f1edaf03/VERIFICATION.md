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

# Verification of the rooted drainage-tree determinant

The main proof is the monic-denominator numerator transformation followed by synthetic division at a deleted leaf; it proves the identity over the polynomial ring in the depletion and transfer parameters. The exact output is a Laplace transform of initial states for a zero-input linear ODE. Differentiation and Cayley–Hamilton translate the determinant criterion into full-trace identifiability and positive-state nonidentifiability.

`check_observability.py` was run with Python 3 and SymPy. Its result was:

```
PASS: symbolic rooted trees: 34
PASS: exact rational routed networks: 665
PASS: singular instances among these: 105
PASS: repeated-rate chain/sibling boundary cases: 4
```

The independent variable is continuous time, but the program tests only finite exact instances and does not independently prove the general theorem. The theorem is about known linear network coefficients and exact initial states, not estimation under unknown inputs or sampling noise. Independent audit has not been performed.
