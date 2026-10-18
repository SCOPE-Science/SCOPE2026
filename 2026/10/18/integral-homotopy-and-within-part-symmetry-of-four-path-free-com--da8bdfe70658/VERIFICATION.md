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

# Reproducibility and proof limits

- Independent enumeration of forbidden four-vertex simple paths, and direct vertex-subset face inclusion comparison on 64 finite multipartite graphs.
- Independent boundary-rank computation modulo two on each such complex; sample \(K_{3,3,3}\) gives 38 two-spheres by the formula and \(K_{2,2,2,2}\) gives 35.
- Exact signed augmented Lefschetz enumeration on 123 within-part permutation cycle-type classes across nine graph size patterns.
- Formal proof using a Mayer–Vietoris induction, relative 2-cell attachments, Euler evaluation, the Hurewicz map and homology Whitehead.

The scripts use the Python 3 standard library only. Run `python3 verify_pathfree4.py` and `python3 verify_equivariant.py`; compare their output to the corresponding included `.txt` artifacts. Finite tests cannot prove an infinite-parameter theorem; the mathematical proof is in `RESULT.md`. No independent scientific audit has been performed.
