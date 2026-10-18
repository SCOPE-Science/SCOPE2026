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

`checker.py` constructs each strict-incidence matrix directly, computes its \(h\)th matrix power by finite-field multiplication, and compares whether it vanishes with the independent Hasse-path event. Its finite runs are independent of the proof's branching recurrence except for the final comparison of counts.

Exhaustively counted (\(b,h,q\); successes/total): \((1,3,2):8/64\), \((2,1,2):3/4\), \((2,2,2):624/1024\), \((2,1,3):8/9\), \((2,2,3):49248/59049\). A nonbalanced six-vertex tree gives \(64/512\) maximal-power successes. Additionally, four full-tree cases received 256 independent random matrix checks each, and 300 random matrices were checked using arithmetic in \(\mathbb F_4\). The critical two-branch binary recurrence was evaluated to height 20,000.

Run from the package directory with `python3 checker.py`. The final printed line is `ALL_TREE_INCIDENCE_TOP_JORDAN_CHECKS_PASSED` if all direct tests pass.

Proof limitations: the direct finite checks are not exhaustive in arbitrary height, arbitrary branching or all finite fields, and do not establish the asymptotic theorem independently. The proof of the general statement uses unique root paths, elementary finite-field counting, and the exact scalar recurrence. No external independent audit has been performed.
