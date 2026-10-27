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

# Reproducibility
Run the included standalone Python script `verify.py` using Python 3 with only the standard library. It constructs a reachable complete capped-counter DFA for \(N_{01}\ge k\), refines its behavioral partition until stable, and compares the number of equivalence classes with \(\lfloor k^2/4\rfloor+3\) for every \(1\le k\le40\). It also verifies agreement between these minimized classes and the claimed symbolic class labels.

Direct finite word checks enumerate every prefix of length at most nine and every suffix of length at most six for \(1\le k\le12\), independently calculating scattered index pairs in concatenated words and comparing them to the concatenation formula.

Expected exact output:

`VERIFY_OK minimized_thresholds=40 bounded_automaton_states=22220 direct_prefix_suffix_tests=1559052`

These tests are intentionally finite. The universal formula rests on the separate Myhill–Nerode proof in `RESULT.md`; neither these checks nor the self-review are independent external auditing.
