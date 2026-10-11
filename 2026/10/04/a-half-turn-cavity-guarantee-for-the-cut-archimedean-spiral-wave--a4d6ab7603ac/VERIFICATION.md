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

After scaling to \(a=1/2\), the essential threshold is \(1\). For the proposed disk center \(c=(73/100,73/100)\) and radius \(R=481/200\), direct recomputation of the spiral-distance function gives a minimum near \(\theta=\pi\) with squared distance about \(5.82656\), safely above \(R^2=5.784025\); the package's outward interval argument covers the entire continuum \([3.1415,7]\), and the reverse triangle inequality covers \(\theta\ge7\). The exact alternating Bessel series has the order-six partial sum negative and a decreasing alternating tail beginning negative, so \(J_0(R)<0\), hence \(j_{0,1}<R\). A disk-supported Dirichlet ground-state trial function therefore has Rayleigh quotient below the known essential threshold, forcing discrete spectrum. Inclusion of cut spirals extends the same disk from \(\beta=\pi\) to all \(\beta>\pi\).

## originality

PASS

Exner–Tater prove the centered-disk threshold \(\beta>2j_{0,1}\) and explicitly remark that shifting the disk center could improve the bound, but they do not provide a shifted-disk certificate or the half-turn threshold. The later Barseghyan–Exner paper studies Lieb–Thirring estimates for shrinking spirals rather than this cut-cavity optimization. Resultary returned no earlier implication-equivalent half-turn theorem.

## value

PASS

The theorem gives a substantial rigorous improvement of a published sufficient bound by an explicit reproducible geometric mechanism. It does not claim the true threshold, but it closes a concrete gap explicitly identified by the source and is not merely a finite numerical experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
