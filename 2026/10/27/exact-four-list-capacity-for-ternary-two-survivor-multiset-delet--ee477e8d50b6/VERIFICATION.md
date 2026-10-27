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

# Reproduction and limits

Run `python3 verify.py` from the directory containing this file. The script uses only the Python standard library. It constructs all ternary source compositions at the tested lengths, all six unordered two-symbol received compositions, and the explicit eleven-source construction. It checks every list occupancy, the low-degree classification, and enumerates all twelve-element potential codes at lengths \(4\) and \(5\). The captured standard output of an actual run is `CHECKS.txt`.

Observed checks: \(127\) distinct construction lengths \(4\) through \(128\); degree classifications for \(29\) lengths \(4\) through \(32\); \(455\) twelve-codeword subsets at length \(4\); \(293930\) at length \(5\); and exact \(6\)- and \(10\)-word small-length upper bounds. An independent mixed-integer programming formulation with six received-output rows verified optimum \(11\) for \(n=4,5,6,8,12\). The code does not enumerate all lengths. General correctness follows from the printed degree/incidence argument in `RESULT.md`.

No independent external audit, formal-proof certification, or universal literature-priority determination has been performed.
