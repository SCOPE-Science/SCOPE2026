---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For every k>=1 and admissible r_i,a_i,p with r1*r2=q<1<rbar, repeated migration has exact P^k=(1/2)[[1+s,1-s],[1-s,1+s]], s=(1-2p)^k=(-μ)^k. Linearization D P^k has trace rbar(1+s), determinant q s; Perron root Λ(s) is strictly increasing because its differentiated numerator rbar Λ-q stays positive. The unique Λ=1 crossing s=-τ=-(rbar-1)/(rbar-q) lies in (-1,0). Thus all even k endemic and odd k extinct exactly if μ^k>=τ (including equality). For Λ<=1, positive left PF vector yields strict Lyapunov descent (critical case included); for Λ>1 small right-PF subsolution and 1 supersolution with strict subhomogeneity ensure unique positive globally attracting fixed point. Independent 78 exact rational P^k/characteristic/parity tests corroborate; global conclusion proved analytically, not by finite trajectories. Example r1=2,r2=1/5,p=9/10: extinct k=1,3,5,7.

## originality

PASS

Best-of-knowledge originality of the sharp repeated strong-migration parity phase boundary and all-integer nonlinear global classification in mixed source-sink two-patch rational model. Classic monotone map/Perron theorems are acknowledged prior, and paper with k-fast movement has a different disease map and eventual rather than finite-k result.

## value

PASS

Shows a dynamical reversal: additional fast mixing can destroy a globally eradicating odd-k effect and restore endemicity, with exact k cutoff and critical behavior. This is a mathematically motivated epidemiological two-time-scale boundary rather than routine local stability linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
