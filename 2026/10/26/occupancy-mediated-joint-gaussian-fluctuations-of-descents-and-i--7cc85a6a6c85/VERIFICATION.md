---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Clay’s exact ordered-selected-prefix/sorted-unselected-tail representation was read in primary Proposition 4.5. Coupling it with one iid uniform sample gives both statistics jointly. For deterministic k≈a n, descents as a 1-dependent sum have variance ≈a n/12; the inversion Hoeffding first-order projection has weights n-2t+1 for t≤k and -k otherwise, with canonical remainder variance O(n²), negligible on n^(3/2) scale. Direct algebra yields inversion variance coefficient (a-a²+a³/3)/12 and conditional cross covariance (k-1)/6=o(n²) on normalized scales. Lindeberg blocking proves the joint Gaussian noise. Independent occupancy CLT gives variance tau²=e^-c-(1+c)e^-2c, and random-index replacement contributes Z/2 and (1-a)Z/2, hence the claimed Sigma cross covariance. Independent finite exact conditional enumeration checked identities; no proof rests on finitely many sample n.

## originality

PASS

Clay 2026 provides separate marginal critical-regime CLTs and the common prefix coupling but does not state or calculate the mixed joint weak limit; marginal Gaussianity alone cannot determine correlation. Dörr–Heiny 2024 prove joint uniform-permutation normal/extreme asymptotics (zero asymptotic cross noise after these scales) and do not treat intermediate random-to-top with fluctuating distinct coupon occupancy. Related Resultary uniform permutation covariance results are different statistics/distributions. The new positive occupancy-mediated covariance is therefore a best-of-knowledge genuine addition.

## value

PASS

A positive time-density cross-covariance, despite asymptotically independent permutation-order noise conditional on occupancy, is a structural joint-mixing insight. It separates exactly two canonical shuffle statistics’ common noise, and gives a natural occupancy-canceling contrast. The result is a fixed-density intermediate-time joint limit not determined by either published one-dimensional marginal theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
