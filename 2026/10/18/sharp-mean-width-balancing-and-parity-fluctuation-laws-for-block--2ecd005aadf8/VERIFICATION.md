---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Disjoint checks give a Cartesian product of one-block hulls. Every admissible sign vector remains exposed as a cube vertex. For m_j≥3, fixing one or two signs leaves respectively 2^(m_j−2) or 2^(m_j−3) completions, so the vertex mean is zero and covariance is I_N. Averaging enclosing ellipsoid inequalities gives tr(A^(−1))+z^T A^(−1)z≤1, yielding det(A)≥N^N with equality only for the centered ball. A negative sign product requires at least one reversal and the cheapest costs exactly 2M_j. Gaussian sign parity is fair and independent of magnitudes, and radial independence divides the expected Gaussian support width by E R=a_N. This gives the stated width and, because p_(r−1)−2p_r+p_(r+1) is the integral of q^(r−1)(1−q)²>0, the two strict extremal partition rules (trivial for k=1). Opposite directions flip the sign product precisely in odd blocks, establishing the exact loss and its zero atom. For the minimum limit, independently obtained the global dominance q(t)≤exp(−ct): if f(t)=c exp(−t²/2), then q(t)/f(t)=integral_0^infinity exp(−tu−u²/2)du≤1/c. Thus q(s/m)^m≤exp(−cs), justifying all fixed moments by dominated convergence as the tails tend to exp(−cs). The per-block limiting odd/even variances are respectively 4/c² and 12/c²; uniformly bounded third moments give Lyapunov's CLT when k,m both grow. The uncentered sum of scaled block losses is O_P(k); dividing the radial normalization error by sqrt(k) costs O_P(sqrt(k/N))=o_P(1), with no need for independence of that error. The fixed-k laws follow by joint independent block convergence and Slutsky. Finally 2kp_m/a_N is asymptotic to sqrt(2 pi) k²/N^(3/2). The frozen checker was inspected, not run; its integer directions and finite quadrature are supplementary.

## originality

PASS

The demihypercube, even-check formulation, support optimization, reflection symmetries and related single-block enclosing ellipsoid facts are not credited as new. The supported distinction is exact strict balancing and maximal imbalance of intrinsic widths for product block profiles, together with the parity-dependent multi-block fluctuation and scaling laws. The closest indexed type-B/type-D width result has substantial one-block overlap, but its stated class and conclusions do not cover these product and growing-block assertions; it is also dated later than the frozen record.

## value

PASS

The exact volume-free-width comparison shows that Euclidean mean width distinguishes independent-check arrangements not distinguished by vertex count, vertex radius, covariance, or the enclosing ball. It gives both optimizing profiles and a concrete k versus N scale on which the deficit stays observable, and explains why parity shows up in width fluctuations despite identical first-order block means. The intrinsic comparison is useful on its stated family without claiming a general coding-theoretic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
