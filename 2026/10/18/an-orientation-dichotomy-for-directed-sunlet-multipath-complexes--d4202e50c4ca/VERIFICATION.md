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

# Reproducibility and limitations

Run `python3 verify_sunlet.py` from the directory containing this file. The Python script uses only the standard library. It enumerates every pendant orientation for cycle sizes 3, 4, 5 and 6, constructs all directed arcs, tests every possible subset for the indegree/outdegree and no-directed-cycle definition, and compares it to the separate forbidden-pair model. It also checks every coefficient of the exact all-parameter face polynomial, calculates the reduced mod-two Betti numbers by explicit boundary-matrix reduction, and replays each asserted mixed-case elementary collapse while checking that every lower face is free.

Observed counts: eight, sixteen, thirty-two and sixty-four orientation words respectively; sixty-six, five hundred twenty-eight, three thousand seven hundred twenty and twenty-four thousand six hundred sixty-six elementary collapse pairs checked respectively, with no failures. Expected reduced Betti vectors: zero for both uniform words and one rank-one group in degree \(n-2\) for each mixed word. The script prints `all finite checks passed` on success.

Finite verification does not prove the formula for untested values of \(n\). The proof in `RESULT.md` supplies an all-parameter elementary-collapse argument and a crosspolytope identification. It certifies an ordinary/simple homotopy statement, not equivariant deformation retraction, and does not assert that independent mathematical review has occurred.
