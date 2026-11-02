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
# Reproduction and scope of checks

The complete algebraic proof is contained in `RESULT.md`. The attached `checker.py` is the independently implemented finite-table check for the new assertions. Execute `python3 checker.py` with Python 3 and no additional dependencies. Observed successful output:

```
all-unital-bands 1 count 1 Y-spectrum [1]
all-unital-bands 2 count 2 Y-spectrum [2]
all-unital-bands 3 count 9 Y-spectrum [1, 3]
all-unital-bands 4 count 84 Y-spectrum [1, 2, 4]
RRB-representation 1 bases 1
RRB-representation 2 bases 2
RRB-representation 3 bases 8
RRB-representation 4 bases 68
ALL_CHECKS_OK
```

The unital band census covers all multiplication tables with element zero a prescribed left identity, but only through size four. The larger construction test checks every prescribed locus size through order thirteen. The right-regular representation test covers every unital right-regular band through four points. These finite tests do not establish the universal statements alone; the proof in `RESULT.md` establishes them by quantified associative identities. The program does not test infinite nonassociative BMI models or universal syntactic fixed-point combinators. Independent audit has not been performed.
