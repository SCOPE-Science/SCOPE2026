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

# Reproducibility and scope

The theorem is proved analytically in `RESULT.md`. Run `python3 verify.py` using Python's standard library. In the checked package this returned `CHECK_OK 148`, which counts 144 off-diagonal asymmetry derivative comparisons and four full-redistribution optimality tests. The script also checks the quadratic coefficient near balance. The test points cover reproduction means \(\lambda\in\{1.2,1.5,2,4\}\), fixed exchange totals \(s\in\{0.15,0.6,1,1.5\}\), and nine positive asymmetry choices for each pair. Tests evaluate the two-dimensional fixed point, the exact analytic sensitivity formula, type-exchange symmetry, and centered finite differences.

A separate symbolic differentiation of the \(2\times2\) implicit-function system simplifies \(\bar q'\det(I-\lambda DM)\) to \(\lambda(q_1+q_2)(q_2-q_1)/4\); the same identity is also derived without computer algebra in `RESULT.md`. The numerical root for \(\lambda=2\), \(s=1\) is \(d_\ast\approx0.4944804708703976\).

Finite-precision calculations do not prove all-parameter assertions. Proof obligations are discharged by the inequality \(-t\log t<1-t\), Perron–Frobenius comparison, symmetry and continuation of the unique positive fixed point, direct matrix inversion, and monotone crossing of the type-2 survival threshold. The result is exact for the stated Poisson branching process, not for finite-population fixation; no independent scientific audit has been performed.
