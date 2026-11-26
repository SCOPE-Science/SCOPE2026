---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Anchor the Gram matrix at the attachment vertex. The mean-zero unmarked-clique and leaf sectors have eigenvalues 1/2 and q/2. On the remaining sector, using total load on each class, the Gram form has diagonal U_m and 1−β_n q and off-diagonal 1−q/2. Its determinant times four is F(q)=4U_m(1−β_n q)−(q−2)^2. It is positive at q=1,2 and negative at 1/β_n; strict concavity and its negative leading coefficient give one crossing for q≥1 and no later return. The positive pivot gives a one-dimensional kernel there, with class totals ((Q−2)/(2U_m),1) and their negative sum at the hub; rank gives the claimed affine dimensions. At a root 1−β_n Q>0, so decreasing U_m or increasing β_n decreases the upper crossing strictly. For ε=1/n and δ=Q−2 the equation is δ²+2U_m(1−ε)δ−4U_m ε=0. Its δ derivative at ε=δ=0 is bounded away from zero on U_m∈[1/2,3/4]; expansion gives δ=2ε+(−2+4/m)ε²+O(ε³) uniformly, and the logarithm gives the asserted second coefficient. The frozen script and notes were inspected, not executed. The separately written `python /workspace/branches/independent_reproduction.py 1` passed below/at/above full anchored Gram signs and nullity for 12 independently reconstructed shortest-path instances; the formulas, not the finite sample, prove the family theorem.

## originality

PASS

The general finite-metric and diameter-two methods are prior, as is an unpowered special-case QEC. The supported distinct contribution is the explicit two-parameter pineapple evaluation with equality loads, strict decreases and the clique-sensitive uniform second term. No inspected source states or mechanically supplies this whole package. The ordinary QEC and powered endpoint are not independent invariants for diameter-two graphs; exact prior QEC coverage is credited wherever found.

## value

PASS

Pineapples are natural one-point metric gluings. The exact root quantifies the loss relative to an isolated star, shows how each size affects the loss, and resolves which terms of the large-leaf exponent are universal or detect the clique. Together with the equality load this is more than computing an isolated ordinary QEC by a standard criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
