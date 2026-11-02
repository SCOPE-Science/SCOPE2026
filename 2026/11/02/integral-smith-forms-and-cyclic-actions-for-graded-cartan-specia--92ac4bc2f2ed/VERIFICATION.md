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

# Reproduction

The original integer Cartan matrices are constructed from sums of weighted cyclic shifts. Run `python check_smith.py` with SymPy available. The complete observed output is in `check_output.txt`:

```
CYCLIC_NAKAYAMA_WEIGHTED_SMITH_OK 406_INTEGER_SNF 1458_DIRECT_MODULAR_RANK
EXAMPLE n=6 L=4 a=2: [1, 1, 1, 1, 65, 4095]
EXAMPLE n=6 L=4 a=1: [1, 1, 1, 1, 2, 0]
```

The integer checker uses an exact-integer Smith routine; the modular checks use a separate finite-field row-reduction implementation. They assess 406 matrices and 1458 independently computed mod-prime ranks; neither is an exhaustive verification of unbounded parameters. The theorem depends on the exact ring-presentation proof in `RESULT.md`. The cyclic action is verified algebraically in the proof, not by a complete computer-generated conjugacy certificate. The status front matter does not assert an independent audit.
