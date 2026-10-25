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

## Checks performed
`python3 check_cylinder_fourcut.py` reproduced all three local relative boundary ranks: 34 of 37 columns, 66 of 69 columns, and 70 of 73 columns for two, three, and four layers. All three explicit signed integral cube 3-cycles had exactly zero boundary and were independent modulo two. Direct five-subset enumeration excluded dual four-simplices in these cases. Additional direct relative boundary checks for five, six, and seven layers each yielded rank 70 of 73 columns.

## Logical scope
The all-length theorem uses a proven four-layer locality reduction; finite enumeration alone does not establish infinitely many cases. Alexander duality and a long exact sequence identify only the stated homology degree over the rational and binary fields. The result does not claim the complete integral homology or homotopy type of the cut complex. External independent validation has not been performed.
