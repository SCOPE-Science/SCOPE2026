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

# Verification and limits

The universal proof is in `RESULT.md`. It uses exact polynomial reduction in characteristic three, the trace exact sequence for the additive map \(t\mapsto t^3-t\), Frobenius on conjugate square roots, and fixed two-element subsets of six branch points. No finite experiment is used to prove a statement for all extension degrees.

Run `python3 verify_wild_d6.py` with the standard library. The script constructs exact finite fields of orders \(3,9,27,81\), tests every nonzero parameter in each (\(2+8+26+80=116\) cases), checks the original characteristic-three polynomial identity, directly enumerates rational branch points, and independently computes \(\deg\gcd(f(X),X^{q^d}-X)\) at extension degrees \(d=1,2,3,6\). It also checks the exact three-way parameter frequencies.

Observed terminal success marker: `WILD_D6_CHAR3_FROBENIUS_2TORSION_ALL_CHECKS_PASS`.

Scientific limits: the previously published characteristic-three model, ordinarity, and complete-splitting criterion are not new. The newly classified non-split Frobenius types, exact parameter distribution, and rational two-torsion orders have no independent external validation. The published reference's full characteristic-three subsection was inspected, but not every possible older equivalent treatment.
