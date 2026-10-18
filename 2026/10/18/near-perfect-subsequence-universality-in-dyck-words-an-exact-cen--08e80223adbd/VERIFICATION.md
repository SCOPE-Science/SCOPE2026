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

# Verification and scope

Execute the self-contained Python 3 file using `python3 verify.py`. The program generates all Dyck words of semilength 2–12 without consulting the closed-form classification, and calculates each shortest-absent count with a suffix next-occurrence automaton. It compares the full qualifying set against a second independent generator, compares each count with pair-absence matrix products, directly lists candidate absent binary words at semilengths 2–8, and checks the explicit Fibonacci-maximizing constructions for semilengths 4–79.

Actual successful output:

```text
VERIFY_OK dyck_semilength_2_to_12=290510 near_perfect=4083 exact_family_and_extremizers=11 direct_SAS_levels_2_to_8=7 symbolic_witness_levels_4_to_79=76
```

The program uses only the Python standard library and performs finite tests. All-size completeness, exact cardinalities, and equality cases are established by the arch classification and transfer-matrix proof. No external or independent validation has been performed.
