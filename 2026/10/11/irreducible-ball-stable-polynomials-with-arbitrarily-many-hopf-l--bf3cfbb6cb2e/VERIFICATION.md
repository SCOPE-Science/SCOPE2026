---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Reproducible verification

## Exact analytic checks

1. Set \(S=z_1^2+z_2^2\), \(r=|z_3|\). Verify \(|S|\le1-r^2\) and \((1-r^2)^m\le1-r^2\) for every integer \(m\ge1\) when \(0\le r\le1\). The resulting bound \(|S^m+\varepsilon z_3^2|\le1-(1-\varepsilon)r^2\) is strictly below \(1\) for positive \(r\) and \(\varepsilon<1\). At \(r=0\), any interior point has \(|S|<1\).
2. On the boundary set \(r=0\), solve \(S^m=1\) and apply the equality case \(|z_1^2+z_2^2|=|z_1|^2+|z_2|^2\). This yields the listed real circles and no others; their phases differ modulo \(\pi\).
3. In \(\mathbb C[z_1,z_2]\), rewrite the irreducible prime \(q=1-S\) as \(1-uv\) with \(u=z_1+iz_2\), \(v=z_1-iz_2\). Divide \(1-S^m\) by \(q\); the complementary sum is \(m\bmod q\), hence not divisible by \(q\). Eisenstein on the quadratic polynomial in \(z_3\) proves irreducibility over the full complex polynomial ring.
4. Compute the nonzero gradient on the circles, verify \(\langle\gamma_j'(t),\gamma_j(t)\rangle=0\), and observe \(J'(z_1,z_2)=(-z_2,z_1)\) preserves all distinct real two-planes \(e^{\pi i j/m}\mathbb R^2\). Distinct fibers of this Hopf fibration in \(S^3\) have absolute linking number one.

These steps form an all-parameters proof; no finite sampling is used to infer an infinite assertion. No computational program or external certificate is necessary. Literature comparisons and originality risks are recorded in the scientific review, not claimed to be independently certified.
