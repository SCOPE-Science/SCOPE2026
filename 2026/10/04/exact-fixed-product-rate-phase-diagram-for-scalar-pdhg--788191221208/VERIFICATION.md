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

For the stated scalar strongly convex--concave quadratic, direct proximal substitution gives the displayed two-by-two iteration matrix. With \(p=\tau\sigma\) and \(s=\tau+\sigma\), exact algebra yields \(T=(s+2-2p)/(1+s+p)\), \(D=(1-p)/(1+s+p)\), and discriminant \((s^2-8p(1-p))/(1+s+p)^2\), while positive steps of fixed product realize exactly \(s\ge2\sqrt p\). In the complex-root regime the spectral radius is \(\sqrt D\), strictly decreasing in \(s\); on the real-root branch implicit differentiation gives the strictly positive derivative proved in the record. Hence the fixed-product optimum is the feasible point nearest the double-root boundary \(s_c=\sqrt{8p(1-p)}\). This boundary lies strictly above the arithmetic-geometric lower bound exactly for \(p<1/2\), producing the two asymmetric minimizers and \(\rho_p^*=\sqrt{1-p}/(\sqrt{1-p}+\sqrt{2p})\); for \(p\ge1/2\) the unique optimum is \(\tau=\sigma=\sqrt p\). The separate derivative calculation on the balanced branch proves the global unique minimum at \(p=1/2\), \(\tau=\sigma=1/\sqrt2\), with rate \(\sqrt2-1\). Goldstein's adaptive update indeed preserves \(\tau_k\sigma_k\) exactly, so the stated reachability limitation follows. The verifier checks the matrix identities and polynomial sign identity exactly and probes the phase diagram numerically; the continuum classification rests on the analytic monotonicity proof.

## originality

PASS

Goldstein et al. give the same basic PDHG ordering, the standard product condition and an adaptive residual-balancing scheme whose proof explicitly states that \(\tau_k\sigma_k\) remains unchanged. They do not solve the exact fixed-product rate optimization. Fercoq gives the closest broader modern framework: for quadratic saddle problems PDHG is a linear fixed-point iteration, its convergence speed is governed by the spectral radius, and step selection can be formulated as minimizing that radius. The full inspected Section 4 develops estimation and adaptive search, including conjugate principal eigenvalues, but does not state the scalar closed-form boundary \(p=1/2\), the two asymmetric minimizers below it, or the global pair \(1/\sqrt2\). Current Resultary searches for scalar PDHG, fixed product, spectral radius and the one-half phase transition did not return an equivalent theorem.

## value

PASS

Step-size tuning is a central practical issue for PDHG, and current work explicitly uses spectral-radius monitoring on quadratic models. The scalar benchmark exposes a nontrivial phase transition: below product one half the fastest pair is asymmetric and lies at eigenvalue coalescence, while above it balance is optimal; globally the best product is exactly one half. Coupling this with the prior product-preserving adaptive rule gives a precise parameterization limitation. This is a motivated exact benchmark with reusable tuning insight, not an arbitrary two-by-two exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
