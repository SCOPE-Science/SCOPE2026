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

Discrete Fourier transform splits the 2d normalized kernel Gram matrix into d Hermitian 2x2 blocks with A_k=d r^(2k)F_k(r^(2d)), B_k=d s^(2k)F_k(s^(2d)), mixed modulus |C_k|=d(rs)^k|F_k((rs)^d e^(-id theta))|. Their strictly positive determinants multiply with (1-r²)^(pd)(1-s²)^(pd). The Veronese numerator recurrence gives positive coefficients, correct degree and simple negative real roots by Sturm-style sign interlacing; Jochemko establishes broader real-rootedness prior, so no novelty claimed for it. Numerator |w+a|² increases and |1-w| denominator decreases strictly with u=1+cos(d theta), forcing each block determinant and product to decrease strictly in u including duplicate-point endpoint. Independent direct determinant/phase checks verified 64 cases across p=2..5,d=2..5; proof applies all p,d≥2 and 0<r,s<1.

## originality

PASS

The real-rootedness ingredient is known through Jochemko 2016, and kernel Fekete point optimization has broad prior literature. The inspected exact statements do not prove global pairwise phase ordering of two concentric regular same-cardinality weighted Bergman kernel orbits for all integer powers p≥2 and arbitrary radii, nor the finite optimum determinant product. Similar published Resultary Szegő orbit frames concern one orbit and Blaschke zeros rather than this 2-orbit p≥2 determinant.

## value

PASS

This gives an all-parameter, unique global staggered optimal relative design and a closed product for a widely used analytic reproducing kernel, with strict comparison of every pair of phases rather than a local extremum. The restriction to two already-regular rings is geometrically motivated, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
