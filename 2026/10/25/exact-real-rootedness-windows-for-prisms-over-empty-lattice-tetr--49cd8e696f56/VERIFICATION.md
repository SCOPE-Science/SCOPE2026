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

# Exact verification and reproducibility

Run `python check.py` from a directory containing the accompanying `check.py`; the script requires Python 3 and SymPy. It checks the numerator transform in two algebraically independent ways (including exact Ehrhart finite differences), the full cubic discriminant identity, its ordered transition factors and root-factorization boundaries. It also counts lattice points in Reeve tetrahedra directly by geometric integer loops for 105 parameter pairs and checks the entire claimed integer phase classification for 22,500 volume–height pairs. The observed terminal output is:

```text
EMPTY_TETRA_PRISM_OK symbolic_identities=5 independent_lattice_counts= 105 parameter_pairs= 22500
```

The general validity comes from the proof in `RESULT.md`, notably the Ehrhart coefficient identities, product differential operator, elementary discriminant rule, and rational monotonicity argument. These finite enumerations are supplementary tests, not substitutes for the proof and not a claim to exhaustive testing of an infinite domain. The external literature comparisons support only the stated accessible-evidence originality assessment. No independent scientific audit or certification has been performed.
