---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For the broadcast-voter model on T_d, d>=3, the two-ancestral-particle dual of Astoquillca–González Casanova–dos Santos has ordinary inward/outward jump rates 2 and 2(d-1) for distance>=3; at distance 2 the one midpoint simultaneously broadcasts to both occupied neighbors at rate q=∫uΛ(du)/Λ[0,1], while individual inward jumps total 2(1-q); at distance 1 direct coalescence has rate 2. The k>=3 gambler-ruin hitting probability of level2 is (d-1)^-(k-2). Solving 2d h1=2+2(d-1)h2 and (2d-q)h2=q+2(1-q)h1+2(d-1)h3, h3=h2/(d-1), gives h1=[2(d-1)+(d-2)q]/H, hk=[2+(d-2)q]/H (d-1)^-(k-2), H=2(d-1)^2+(d-2)q. I independently simplified both generator equations to zero symbolically; derived d(h1)/dq=2(d-2)^2(d-1)/H²>0 and d(h2)/dq=2d(d-2)^2/H²>0; checked q=0 gives classical (d-1)^-k. Duality under Bernoulli(p) initial data converts coalescence probability to covariance p(1-p)h_k; algebraic inversion follows from h1<1. The proof relies on full primary graphical subset rates; these were inspected in arXiv:2610.04530 Sections 3.2-3.4 and their pair specialization.

## originality

PASS

Original broadcast-voter paper proves stationary existence, duality and full moment-profile identifiability for trees; this adds the exact homogeneous-tree two-point covariance, sharp distance decay, q-monotonicity, and inversion from one measured pair, none stated in its theorem. Classical ordinary voter model supplies only q=0.

## value

PASS

An exact all-distance covariance profile and one-pair identification formula are natural observables for this new interacting-particle process, quantify how first moments alter local clustering but not distant decay, and can be used to calibrate the broadcast parameter. Neither immediate generic duality nor q=0 collision probability gives the result automatically.

The dated certificate retains the supplied scientific assessment, sources and limitations.
