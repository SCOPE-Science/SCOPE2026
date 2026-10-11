---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Scaling the momentum by \(\lambda\) gives the stated two-state matrix with trace \(T=1+\beta-s(1-\nu\beta)\) and determinant \(D=\beta(1-s(1-\nu))\). The second-order Jury conditions reduce exactly to the claimed stability interval. For \(0<\nu<1\), the discriminant has the two positive zeros \((1-\beta)/(1\pm\sqrt{\beta\nu})^2\). Between them the complex-pair modulus \(\sqrt D\) decreases with \(s\), while the scaled disk Jury inequalities exclude any improvement beyond the upper coalescence point. This yields the unique interior optimum and its closed rate. The endpoint cases reduce respectively to eigenvalues \(1-s,\beta\) and constant determinant \(\beta\), giving the two plateaus. The minimum vanishes exactly at \(\nu=\beta\); then trace and determinant both vanish at \(s=1/(1-\beta)\), so Cayley--Hamilton gives \(M^2=0\). Independent numerical/symbolic checks reproduced the optimum and exact nilpotence.

## originality

PASS

Ma and Yarats define QHM and identify \(\nu=\beta\) with Nesterov momentum, but their inspected paper does not solve the exact scalar quadratic learning-rate spectral-radius minimization. Krivovichev and Sergeeva analyze a two-step method whose characteristic polynomial maps to QHM, derive stability and a general spectral-radius formula, and pose parameter optimization over a spectral interval; their Section 2.3 solves that broader tuning problem numerically for an external second momentum parameter rather than giving the audited fixed-\((\beta,\nu)\) closed-form scalar landscape. Thus the stability clause is covered background, but the unique upper-discriminant optimum, endpoint plateaus and nilpotent slice are not stated or mechanically supplied by the inspected optimization theorem. Current Resultary searches found no equivalent closed QHM formula.

## value

PASS

QHM is a standard optimizer family and exact quadratic modes are the canonical tuning benchmark. The theorem gives the complete fixed-\((\beta,\nu)\) rate landscape rather than a single tuned example, including both endpoint plateaus and a unique two-step deadbeat Nesterov slice. That supplies a precise structural interpretation of the immediate-discount parameter and a reusable calibration benchmark, even though it does not solve the multi-curvature minimax problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
