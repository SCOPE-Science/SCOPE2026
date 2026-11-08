---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Independently reconstructed the unit-normalized Szegő Cauchy double-alternant; within-ring discrete Fourier eigenvalues yield C_m(r)C_n(s), and root-of-unity resultants yield a cross factor with g=gcd(m,n), L=lcm(m,n), a=r^L, b=s^L. Its cos(Lθ) derivative is strictly negative since (1−a²)(1−b²)>0; equality occurs uniquely cos=-1 modulo 2π/L. The exact quotient (1−αt)/(1−βt) has log derivative ≥α−β and tends to that coefficient as t→0, proving globally sharp deficit; coincident equal-radius nodes are correctly singular. The model-space Wold decomposition supports the infinite orbit interpretation but no infinite determinant is claimed. Independent numerical Gram determinants match in 72 mixed-radius cases; they are not an infinite proof.

## originality

PASS

Qualified PASS: closest inspected Resultary theorem determines all-angle same-radius one-ring determinant and stability, explicitly excluding two radii. Aguilera–Carando gives Riesz orbit-frame existence, not mixed-radius raw-seed D-optimality. Cross-ring exact resultant plus strict phase optimum and sharp logarithmic defect are not implied by these inspected results. General D-optimal sampling and classical Fekete work remain risk; failed search is not novelty proof.

## value

PASS

PASS: two concentric individually regular Hardy sampling orbits are the natural next interpolation design after the known single circle. An exact globally optimal radius-independent stagger with arithmetic gcd/lcm behavior and sharp determinant sensitivity bounds has independent design relevance, not merely the Cauchy identity. Distinguishes determinant from condition-number objectives and does not pretend unrestricted two-circle optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
