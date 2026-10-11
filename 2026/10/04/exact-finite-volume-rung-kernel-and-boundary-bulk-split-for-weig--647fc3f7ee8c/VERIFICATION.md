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

The rung-current reduction was reconstructed from electrical antisymmetry: one unit injected across rung \(j\) gives the difference-mode system \(B_nd=2e_j\), hence the rung kernel is \(2cB_n^{-1}\). Solving the endpoint-modified tridiagonal recurrence gives the stated leading minors and determinant; the standard inverse formula then simplifies to the displayed \(\alpha\)-kernel. Independent direct matrix inversion for sizes through ten and multiple positive weights matched every entry. Transfer-current principal minors give the joint law, and the covariance and boundary/bulk limits follow directly. The finite checks supplement, rather than replace, the all-size recurrence proof.

## originality

PASS

The closest ladder source was inspected at its finite weighted counting and infinite stationary determinantal results. Klenke gives the infinite rung kernel \(\rho\alpha^{|i-j|}\) and finite total tree-weight recurrences, while Lyons--Peres give the unweighted endpoint sequence and limit. Burton--Pemantle supplies the general transfer-current theorem. None of the inspected sources states an algebraically equivalent finite non-Toeplitz rung kernel with both endpoint factors, all finite joint rung probabilities, or the simultaneous endpoint-versus-bulk limits. Fresh Resultary and web searches did not locate such a statement.

## value

PASS

This is a natural complete finite-volume invariant of a canonical weighted spanning-tree model: one formula gives every rung marginal, covariance and higher inclusion determinant for every size and common positive rung weight. The nonstationary boundary factors explain why the classical endpoint limit \(\sqrt3-1\) differs from the infinite bulk density \(1/\sqrt3\). That complete finite joint law is more than a single textbook effective-resistance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
