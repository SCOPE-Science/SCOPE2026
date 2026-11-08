---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Since A commutes with dI, binomial rearrangement yields T_s(h)=Σ_{j=0}^s h^j A^j E_{s-j}(-dh)/j!. Alternating Taylor sums E_m(-x)≥0 for 0≤x≤1, all A^j≥0, and T_s 1=1, proving sufficient stochasticity. For witness (u,v), A^j_uv=0 j<s-1, A^{s-1}_uv>0, A^s_uv=0, so exact entry h^{s-1}A^{s-1}_uv(1-dh)/(s-1)! <0 at every h>1/d. A bipartite geodesic of length s-1 gives shorter walk absence and opposite-parity s-walk absence. Applies to directed bipartite strongly connected constant-exit-rate chains too. Independently checked 5 C8 RK4 rational step transition signs and stochastic rows, including explicit h³(1-2h)/6 witness.

## originality

PASS

General SSP positive coefficient-one sufficiency and classwise sharpness are prior results. The nontrivial surviving contribution is fixed-network, all-order necessity under a structural walk-parity certificate, producing an exact negative transition entry for every h>1/d. Closest Horváth text was materially read in full and did not state this graph-certificate result.

## value

PASS

Positivity preservation of graph diffusion is an exact numerical admissibility property, distinct from norm/spectral stability. The graph-theoretic walk-parity certificate yields a sharp network-specific all-timesteps obstruction in broad regular bipartite families and a concrete entry crossing, a useful cutoff despite higher Taylor accuracy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
