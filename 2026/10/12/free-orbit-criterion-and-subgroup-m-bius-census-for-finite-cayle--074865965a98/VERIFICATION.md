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
# Reproducible finite verification

Use Python 3 standard library with `python3 verify.py`. The exact command was executed against the attached source and returned:

```
VERIFY_OK single_modal_partition_checks 7992 multi_component_checks 9193 direct_boolean_closures 352 subgroup_mobius_and_dihedral_cases 12 symmetric4_random_checks 600 symmetric4_subgroups 30
EXAMPLES D2 q2 free 8 D3 q2 free 42 S4 q2 free 16740024
```

The program implements finite groups from multiplication tables, constructs all subgroups and their Möbius coefficients, checks the primitive-word dihedral formula, evaluates partition refinement for colored named-agent S5 frames, compares the orbit criterion for all enumerated small component colorings, and directly builds Boolean modal closures for 352 examples. Its test corpus includes \(D_1\), \(D_2\), \(D_3\), \(D_4\) and \(S_4\), including 600 seeded random checks for the non-dihedral group \(S_4\). It also verifies the 30-subgroup count of \(S_4\).

All examples are finite and the random tests are not exhaustive on \(S_4\). The general proof is supplied independently in `RESULT.md`, including modal-equivalence propagation, inversion on every subgroup of \(G\), and rotation/reflection inclusion-exclusion in \(D_m\). Neither code nor mathematical prose asserts external independent certification.
