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

# Reproducibility and limits
Execute `python3 verify.py` in the package directory with Python 3.10 or later. The checker uses only the Python standard library and obtains its tables from direct enumeration. It cross-checks T0–T6 axioms with the pointwise normal form for every candidate on chains through six elements, enumerates partitions and checks basic operation compatibility for all admissible algebras through five elements, and validates every prescribed-cut count and renewal coefficient through chains of seven elements.

Expected final log line: `VERIFY_OK all_axiom_cases_m_le_4 1335 direct_congruence_algebras 300 cut_subset_checks 63`.

These are finite independent implementations of the identities and counting predicates, not a formal infinite proof or independent human audit. The unrestricted result is justified by the four mathematical proof steps in RESULT.md. The original paper's tense-filter correspondence is an external mathematical premise and is explicitly referenced. No formal proof-assistant certification or independent validation is claimed.
