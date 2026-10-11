---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Independent elimination gives determinant \(u^2(1-\alpha)^2\) and trace \(u^2\alpha^2-2w\alpha+1+u^2\). Under the penalty-between-curvatures assumption, \(F(\alpha)=T(\alpha)+2u(1-\alpha)\) decreases strictly from positive to negative, so it has exactly one root. At that root the discriminant vanishes with a negative repeated eigenvalue. For smaller alpha, the root-product lower bound exceeds the critical radius; for larger alpha, the trace-magnitude lower bound does. The independent witness \((a,b,\beta)=(1,4,2)\) reproduces \(\alpha_*=0.9462158829301036\) and \(\rho_*=0.0253540759335033\).

## originality

PASS

The primary SC-PRSM literature supplies the common relaxation and convergence domains, and the 2016 full text explicitly frames large values near one as empirical acceleration guidance. It does not state the exact problem-dependent scalar minimizer found here. Resultary returned no implication-equivalent finding.

## value

PASS

The result replaces empirical 'close to one' relaxation guidance by an exact problem-dependent calibration and explains the optimum through critical damping on the smallest nontrivial strongly convex equality model. It provides a sharp benchmark for symmetric-ADMM/PRSM parameter-selection theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
