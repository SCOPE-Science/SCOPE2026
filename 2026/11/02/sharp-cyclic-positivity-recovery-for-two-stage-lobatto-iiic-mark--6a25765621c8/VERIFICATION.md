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

Direct Butcher tableau elimination gives R(z)=1/(1−z+z²/2). On n-cycle Q=P−I, factorization of R(h(P−I)) gives a convergent complex-pole pair α=ρe^{iθ}, θ=atan(1/(1+h)), ρ=cosθ−sinθ<1. Summing powers by residues P^n=I produces c_{n,j}=2ρ^(j+1)/(h|1−α^n|²)[sin((j+1)θ)+ρ^n sin((n−j−1)θ)]. If nθ≤π all coefficients are nonnegative, and at equality only j=n−1 vanishes. For π<nθ<2π that last coefficient is negative; for nθ≥2π, k=ceil(3π/(2θ)) yields sin(kθ)≤−1/√2 while ρ^n≤e^(−2π), forcing a negative coefficient. Thus n≤4 positive for all h>0; for n≥5 h=0 or h≥cot(π/n)−1 exactly, with large-step positivity recovery. Independent exact matrix inversions at 45 n/h cases checked signs and formula, plus n=5,10 numerical boundaries; finite tests supplement all-n proof.

## originality

PASS

Lóczi–Ketcheson arXiv:1303.6651 treats absolute monotonicity of rational Runge–Kutta stability functions, which gives general sufficient constraints but not this exact directed-cycle late-step positivity recovery. Bharali–Holtz arXiv:math/0511325 develops entire functions preserving nonnegativity of all nonnegative circulant matrices and a Fourier characterization, not this fixed rational function on shifted cycle generators. Published Gauss Padé and SSP-SDIRK Markov results use different rational R and do not imply the cotangent Lobatto threshold. Specialist cyclic resolvent work remains a priority risk.

## value

PASS

A standard implicit Runge–Kutta method can have invalid transition weights at small positive steps but recover valid stochastic matrices at a computable graph-size-dependent large-step threshold. The all-n sharp boundary, zero pattern and n/π scale are natural method/graph interaction facts useful for diagnosing Markov discretization; not a cosmetic numerical root.

The dated certificate retains the supplied scientific assessment, sources and limitations.
