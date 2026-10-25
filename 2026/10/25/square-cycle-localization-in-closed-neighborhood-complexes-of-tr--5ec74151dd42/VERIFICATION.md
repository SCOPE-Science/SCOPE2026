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

# Reproducibility checks

The included standalone Python 3 file `verify.py` has no external dependencies. Executing `python verify.py` produced:

```text
PASS: 16 independent vertex-sum collapse certificates, 384 elementary pairs
PASS: 10 cactus-with-pendant-tree homology computations over GF(101)
PASS: 8 cycle base cases (lengths 3 through 10)
```

For the 16 vertex sums, the script reconstructs all faces and checks every elementary-collapse pair and freeness. For the separate cactus cases it computes finite-field ranks. The finite tests do not establish universal or integral statements; the gluing proof and standard integral homology of wedges supply those results. No external independent scientific review has been performed.
