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
Run `python3 verify.py` with Python 3 standard library. This reconstructs the complement of each cyclic host on the designated selected vertices for all \(2\le r\le100\), checks \(P_4\dot\cup(r-2)K_2\), and checks the inequality excluding a smaller regular host. The stdout is preserved in `verification_output.txt`.

The proof for all \(r\ge2\) is the algebraic crossing-edge bound and the explicit cycle-block description in RESULT.md; the finite checker does not establish the infinite theorem on its own. The code does not enumerate all abelian groups or all vertex-transitive graphs. Independent audit has not been performed.
