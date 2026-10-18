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

Read `RESULT.md` for the exact definitions and the analytical all-dimensional argument. Run `python3 check_spherical_sector.py` with Python 3, NumPy and SciPy installed. The checker uses rational arithmetic for the cone and ball identities at ten selected rational values of \(\sin^2\theta\), validates weighted John first/second moments numerically, and compares against SLSQP maximization of \(\log a+(d-1)\log b\) for the full three-parameter axial ansatz. It prints `All checks passed.` on success; this output was observed for the embedded file. None of these numerical checks are offered as proof outside the tested cases.

For the universal proof, independently verify that \(c^2=a^2+\cot^2\theta\,b^2\), maximize the displayed quadratic \(q(u)\) on \([-1,1]\), and check the four scalar John-moment identities for each branch. A valid certificate needs only the displayed finitely many contacts, and yields global optimality for ellipsoids of arbitrary center and orientation. The derivative statement follows from direct differentiation of the exact volume formula. No external audit or additional certification has been performed.
