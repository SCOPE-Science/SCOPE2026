---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

Read source reduced Riccati map and reconstructed w_{n+1}=exp(−iχ_n)(w_n+s)/(1+s w_n), with s=sinθ∈(0,1). The disk-automorphism identity 1−|f_s(w)|²=(1−s²)(1−|w|²)/|1+sw|² gives exact log defect telescope. Fresh independent numerical identity/Jensen checks at 9 complex configurations plus Haar quadratures succeeded. Since each χ_n is fresh uniform and independent, postrotation angle is Haar and independent of new radius except at f_s(w)=0; w=−s maps to 0 then next step nonzero and Haar. Angular uniformity yields E[log|1+s w_n| conditional on radius]=0, bounded increment in [log(1−s),log(1+s)]; martingale strong law gives almost-sure 2log cosθ and Hoeffding–Azuma gives displayed two-sided n−1 tail bound with L=log[(1+s)/(1−s)]. Simulations do not prove the infinite limit.

## originality

PASS

Quantitative finite-step angular isotropy, exact almost-sure radial defect exponent and martingale concentration extend the same published circle-stationarity observation; no examined broader theorem explicitly gives this full-disorder map-specific rate.

## value

PASS

The exact radial boundary burn-in exponent and finite-horizon concentration replace an arbitrary discarded simulation transient for a naturally occurring lattice quantum-walk transfer map; the quantity is important for interpreting its invariant Riccati circle, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
