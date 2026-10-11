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

Coupling the two conditional trees by changing only P_j leaves the eventual descendant set of j unchanged and gives T^(0)-T^(1)=S_{j,n}D(Q_j)>0 almost surely. Future subtree growth has mean n/j and is independent of Q_j; averaging the standard depth mean H_{q-1} over q=2,...,j-1 gives the conditional mean gap and Bernoulli covariance. Harmonic telescoping gives the global covariance. Independent root-attachment indicators give Var(R_n), and the classical L2 path-length limit gives the correlation asymptotic.

## originality

PASS

Best-of-knowledge originality passes. Classical recursive-tree work supplies path-length and root-degree marginal theory, but no inspected source or Resultary hit gives the arrival-indexed root-attachment covariance, conditional stochastic order, or exact root-degree/path-length covariance.

## value

PASS

Root degree and total path length are canonical recursive-tree statistics. The theorem quantifies the path-shortening effect at every arrival, strengthens it to stochastic order and monotone-transform covariance, and explains linear covariance with only logarithmically vanishing correlation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
