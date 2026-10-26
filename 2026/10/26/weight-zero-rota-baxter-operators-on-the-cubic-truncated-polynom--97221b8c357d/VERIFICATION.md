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

The self-contained `verify.py` enumerates all linear operators over GF(2), GF(3), and GF(4) and directly tests every unordered pair in the basis (1,t,t²). For GF(5), it verifies every operator permitted by the closed normal form. It independently forms the automorphism orbits using all changes of generator t ↦ ut + vt².

Expected and observed counts: q=2 (4 operators, 4 orbits), q=3 (15, 7), q=4 (16, 6), q=5 (45, 9). Exact arithmetic includes GF(4) realized by a quadratic irreducible polynomial over GF(2). The output is `VERIFY_OK`.

The finite checks do not certify the infinitely many field sizes. That statement is supported by the basis-pair algebraic proof in `RESULT.md`. Independent external audit and validation are not performed.
