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

The theorem's direct reduction is (MK) \(\iff\) isotonicity; (Pos) \(\iff\) the least positive input is sent to a positive value; and (Con) \(\iff\) every positively mapped input among the allowed lower indices forces a constant prefix. Counting the two disjoint monotone classes by multiset coefficients establishes the formulas without relying on computation.

The independent finite enumerator `checker.py` executes directly against the three displayed axioms for every increasing map at sizes \(2\)–\(9\), compares its truth value with the structural criterion, and checks both unrestricted and top-preserving counts. Expected output pairs are \((2,2),(5,3),(13,9),(40,21),(115,70),(415,210),(1281,735),(4956,2485)\).

Run from the directory containing the files: `python checker.py`. No third-party packages or external files are required. Finite enumeration does not certify the infinite theorem or novelty. The primary full text could not be retrieved for an exhaustive literature comparison; this remains a documented priority risk.
