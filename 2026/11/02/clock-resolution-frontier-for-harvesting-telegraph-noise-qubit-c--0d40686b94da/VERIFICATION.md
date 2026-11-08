---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The stationary telegraph coherence solves Gʺ+2ξGʹ+4ν²G=0 with G(0)=1,Gʹ(0)=0, giving e^{−ξt}[cos δt+(ξ/δ)sin δt], δ=sqrt(4ν²−ξ²). An x-pulse converts the pre-pulse Bloch y component G(t)sin ωt to conserved z, while conditional transverse modes decay, giving terminal ensemble capacity 2ε|E[G(T)sin(ωT)sin2θ(T)]|. Fixed θ optimizes outside expectation; informed θ(T) can select the sign inside, not the telegraph state. A globally Lipschitz slow envelope h(t)=e^{−ξt}sin ωt1_{t>=0}, maximized at t_H, and Gaussian characteristic filtering yield uniformly B/(2ε)=H e^{−(δσ)²/2}+O(σ+δ^−2) for σ→0; analogous F/(2ε)=H b(δσ)+O(σ+δ^−2). Fourier |cos| gives b(s)→2/π as s→∞, while uniform integration-by-parts for fixed σ yields blind zero and informed positive smoothed-envelope limit. Independently checked exact slow envelope and nearest rapid-phase peaks for ν=10,30,100 at ξ=ω=1; deterministic tests only corroborate analytic bounds.

## originality

PASS

Jiang et al. 2026 already give the deterministic one-pulse retained capacity expression. Classical RTN coherence and Gaussian Fourier suppression are prior. The assessed result adds independent clipped Gaussian pulse-time jitter with capacity calculated after ensemble mixing, and compares blind fixed-angle versus time-informed sign feedback under sharp high-coupling precision scaling; these comparative limits were absent from inspected close literature.

## value

PASS

The sharp δσ resolution transition quantifies when a physically motivated decoherence-mitigation protocol survives timing uncertainty. The strict informed-vs-blind split, including survival 2H/π where blind capacity vanishes, is a nontrivial information-constraint boundary, not merely another deterministic pulse optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
