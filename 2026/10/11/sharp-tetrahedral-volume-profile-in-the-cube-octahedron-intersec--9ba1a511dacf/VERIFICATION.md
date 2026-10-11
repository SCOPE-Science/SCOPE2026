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

# Reproduction and verification

Run `python3 verify.py` with Python 3 (standard library only). The script generates, rather than loads, all 24 formal vertices on each side of \(c=2\); the vertex set may specialize to fewer distinct points at endpoints. It enumerates all \(\binom{24}{4}=10{,}626\) quadruples on each side, derives every signed cubic determinant polynomial in exact integer arithmetic, and checks the nonnegativity of both differences against the proposed envelope in the degree-three rational Bernstein basis. It evaluates 63,756 polynomial inequalities, covering the entire parameter intervals, and derives an explicit equality witness for each branch.

A separate symbolic-algebra diagnostic in a different code path found 109 distinct signed determinant polynomials for the first vertex family and 97 for the second. The supplied replay performs the proof-critical checks from its own generated data and does not depend on that independent diagnostic or its logs.

The step from vertex quadruples to arbitrary contained tetrahedra follows analytically by separate affinity of the signed determinant. The cap-volume identities and sign factorizations for the normalized ratio are analytic arguments in `RESULT.md`; the checker is not a substitute for reconstructing those arguments. Scientific novelty has only same-model review; independent source/prior-art verification remains open.
