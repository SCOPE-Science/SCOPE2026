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

Run `python3 verify.py` using standard Python 3. The script constructs the exact \(\operatorname{GP}(12,5)\) adjacency graph from its vertex formulas. It recursively enumerates every face of the induced-maximum-degree-one complex, checks each face by a separate degree-based predicate, then constructs every matching pair using a specified vertex order. The complete reversed-matched Hasse digraph is topologically sorted, establishing acyclicity rather than relying on a toggle heuristic.

The script then recursively eliminates exact signed matched 7/8-cell incidences and compares the full eleven-by-five boundary with the stated matrix. It verifies that two columns form a primitive rank-two integer image and that all five columns are combinations of those two, so its Smith invariant factors are \(1,1\). Standard discrete Morse and cellular homotopy arguments described in `RESULT.md` convert these checks into the wedge-of-spheres conclusion.

The provided `verification_output.txt` is the recorded stdout from executing this very script. The output terminates in `ALL_CHECKS_PASS`.

Limitations: the script verifies a particular finite 24-vertex object and its full finite incidence relations. It is not a general solver for generalized Petersen families. It does not provide external independent mathematical review, and searches do not establish uniqueness or publication priority.
