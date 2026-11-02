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

# Reproducibility checks and limits

Run `python3 verify.py` using only the Python standard library. The direct verifier was executed from its source and reported:

`VERIFY_OK states=17 triples=37 tight_arcs=24 slack_one_arcs=13 A8_eq_A2=True exact_trace_classes=6 direct_brute_n=3..8`

It constructs the prism graph and all third-edge incompatibilities, tests the three-offset forbidden-pair table, constructs all 37 valid triples and 17 pair states, verifies the four-state potential and all 37 transition inequalities, proves the integer matrix identity \(A^8=A^2\) by exhaustive entry comparison, and computes exact integer traces for the six relevant residue cases. It separately brute-forces **all** edge subsets on each prism circumference 3 through 8 and checks each predicted maximum size and multiplicity.

The all-length conclusion is derived from the finite integer identity, the telescoping-potential proof and the bijection from labelled edge sets to cyclic words, not from an experimental sequence. No full external independent assessment or complete historical priority certification was performed.
