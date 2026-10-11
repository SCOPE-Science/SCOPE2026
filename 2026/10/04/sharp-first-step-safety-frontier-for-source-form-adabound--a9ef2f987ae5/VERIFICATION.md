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

At \(t=1\), the source recurrence gives \(m_1=(1-\beta_1)h x_1\), \(v_1=(1-\beta_2)h^2x_1^2\), and \(x_2=x_1[1-(1-\beta_1)h\widehat\eta_1]\). The raw rate ranges over all positive values as \(|x_1|\) varies, so its attainable supremum after clipping is exactly \(u_1\). Thus the sharp condition follows from \(|1-z|\le1\) iff \(0\le z\le2\). The unsafe neighborhood is obtained by solving the upper-clip inequality. The inspected verifier independently checks the recurrence, safe/unsafe sides and all stated default numbers. One nonessential sentence in RESULT.md says the clipped rate attains the entire closed interval even when \(\ell_1=0\); in that boundary case the attainable set is \((0,u_1]\), but the supremum and every theorem statement are unchanged.

## originality

PASS

The defining AdaBound paper gives the source recurrence, the dynamic clipping mechanism, the recommended upper-bound schedule and the default parameters, but its theorem is a regret bound and does not compare the first upper clip with the exact scalar-quadratic descent interval. Savarese's direct correction treats global regret and arbitrarily slow convergence rather than this one-step curvature boundary. Fresh Resultary and web searches returned related quadratic stability frontiers for other algorithms but no theorem implying the exact AdaBound condition or upper-clipping plateau.

## value

PASS

AdaBound's defining mechanism is intended to suppress extreme adaptive rates. The theorem identifies an exact pointwise safety requirement on that upper bound, quantifies the source defaults on the canonical scalar-curvature test, and separates mere finiteness of a clipped rate from curvature-compatible descent. The narrow scope is mathematically motivated by the algorithm's central design feature rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
