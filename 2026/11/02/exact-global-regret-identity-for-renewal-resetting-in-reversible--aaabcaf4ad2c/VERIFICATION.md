---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For D,L>0, V∈C²([0,L]), killed at 0/reflected at L, and iid positive finite-mean renewal clocks q, independent fixed-location attempts yield T_q(x)=a_q(x)/f_q(x), f_q=P(H_x<τ_q)>0. Killed semigroup identity gives -ℒa_q=f_q with a_q(0)=0 and a_q'(L)=0; inversion yields a_q(x)=∫K_V(x,y)m(y)f_q(y)dy, m=e^(-V/D), K_V=(1/D)∫_0^min(x,y) e^(V(z)/D) dz. Under w_p=m f_p²/Z, swap x,y in symmetric kernel: half the pair sum of h(y)/h(x)+h(x)/h(y)-2 is (h(x)-h(y))²/(h(x)h(y)); hence nonnegative exact regret, equality precisely h constant and f_q(0)=f_p(0)=1 forces f_q=f_p. Inequality 2(cosh log hdiff−1)≥(log hdiff)² gives stability. Separate inward-drift half-line formula is obtained by explicit hitting transforms and Green kernels, with finite-mean-risk qualifications. Read the complete pinned symbolic/rational/numerical checker; its finite checks are corroboration, not the analytical proof.

## originality

PASS

The conjugate-launch distribution and even a free-diffusion special-case global optimality assertion are established prior work and are expressly credited. The mathematically distinct arbitrary-potential reversible speed weighting and exact nonnegative regret identity with equality/stability are not implied by the source stationarity calculation or selected-family comparisons. Classical symmetric Green-kernel inequality antecedents remain a precise residual risk.

## value

PASS

An exact all-competitor positive loss certificate upgrades an explicitly motivated stationary conjugate-launch construction to a verifiable global theorem on arbitrary smooth one-dimensional reversible potentials, with uniqueness at profile level and logarithmic stability. This closes a genuine analytical gap left by local variational calculus and includes explicit drift-dependent benchmarks, not a routine alternate notation for a Poisson-rate optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
