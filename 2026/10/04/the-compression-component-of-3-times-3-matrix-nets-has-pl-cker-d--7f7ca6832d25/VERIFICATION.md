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
# Verification

Run `python3 verify.py` from the directory containing the bundled files. The script uses only Python's standard library and exact integer arithmetic.

It verifies the Chern and Segre class coefficients in the truncated Chow ring, then computes the degree in two ways: projective-bundle pushforward and direct reduction by the projective-bundle relation. The recorded output is:

```text
CHERN_F_OK [{(0, 0): 1}, {(0, 1): 2, (1, 0): 2}, {(0, 2): 3, (1, 1): 3, (2, 0): 3}, {(1, 2): 3, (2, 1): 3}, {}]
SEGRE_F_OK [{(0, 0): 1}, {(0, 1): -2, (1, 0): -2}, {(0, 2): 1, (1, 1): 5, (2, 0): 1}, {(1, 2): -3, (2, 1): -3}, {(2, 2): 3}]
PUSHFORWARD_TERMS [3360, -3360, 1008, -84, 3]
ROUTE_A_DEGREE 927
ROUTE_B_DEGREE 927
VERIFY_OK
```

The verifier checks the intersection arithmetic conditional on the projective-bundle identification from arXiv:2609.09675v1. It does not independently re-prove that source theorem or perform an exhaustive literature search.
