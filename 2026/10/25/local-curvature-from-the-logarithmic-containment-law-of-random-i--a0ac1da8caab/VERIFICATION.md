---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The exact semicircle-anchoring identity P(p outside hull)=n∫ f(s)Q_p(s)^{n-1} ds counts the unique anchor for continuously sampled cyclic directions. For boundary local arclength s>0, the opposite-ray chord endpoint is tδ(s)=−2δ/(κ(z)s)+O(δ+δ²/s²); its arc mass changes by −2f(z)δ/(κ(z)s). Expanding (n−1)th power over Cδ≤s≤η yields coefficient 2n(n−1)f(z)^2/κ(z) times δlog(1/δ). Other parts, including the returning endpoint near the opposite side of z, are O(δ) for n>=3. The circle n=3 dilogarithm formula independently yields the same log coefficient, though convergence of numerical ratios is slow at moderate δ. The n-fixed scope and uniform Oδ error are correctly stated.

## originality

PASS

Best-of-knowledge statement-and-implication comparison after querying Resultary and checking relevant primary literature: the actual full claim, not just title, is not entailed by an inspected stronger theorem. Any acknowledged known special cases are explicitly excluded from novelty. Residual risks are itemized below.

## value

PASS

The local rare-event inclusion law gives a curvature estimator from pointwise fixed-sample random inscribed hulls and makes the squared boundary sampling density explicit; it distinguishes the δ→0 boundary-layer regime from traditional n→∞ random-polytope asymptotics. The classical circle n=3 specialization is excluded from novelty and appropriately credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
