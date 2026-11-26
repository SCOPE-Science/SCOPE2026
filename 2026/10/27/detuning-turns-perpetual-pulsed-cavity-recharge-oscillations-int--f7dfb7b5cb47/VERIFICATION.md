---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Under the passive linear Lindblad dynamics a coherent pulse evolves with the dissipative two-mode amplitude matrix; the normally ordered number covariance starts at zero and remains zero under vacuum loss. Subtracting the scalar mean frequency minus iγ/4 gives a traceless matrix with square Z²I; its exponential gives B=−Fg sin(Zt)exp(−γt/4−iω̄t)/Z. The modulus squared is the stated damped cosh-minus-cos expression, with no positive-time zeros when β=2|Im Z|>0. Off resonance Im(Z²)=−γΔ/4, so β>0. Taking the Hermitian part of the amplitude generator gives nonpositive real eigenvalue parts; equality would force the charger's eigenvector component to vanish, inconsistent with g>0. Consequently β<α. The derivative is a positive factor times R cos(ϖt−φ)−L(t), where L=α cosh(βt)−β sinh(βt)>0 and φ=atan2(ϖ,α). L starts below R, decreases then grows strictly to infinity; writing it as a shifted cosh gives the exact unique positive envelope crossing T_env. Beyond it the energy strictly decreases. An independent lobe count controls the residual: roots that can yield a maximum lie in positive cosine lobes; there the derivative sign function is strictly concave, since its second derivative is −ϖ²R cos(ϖt−φ)−β²L<0. Every full lobe with center before T_env starts and ends negative and is positive at the center, hence contributes exactly one strict maximum. There is at most one per lobe and none starting after T_env. Only a bounded number of initial or terminal lobes can differ from the center count, even at envelope equality or tangency. Thus N=ϖ T_env/(2π)+O(1). Expanding at fixed g,γ gives ϖ=2G+O(Δ²), β=γ|Δ|/(4G)+O(|Δ|³), and R/α→4g/γ with O(Δ²) error. The artanh term divided by β stays bounded, yielding the claimed coefficient and additive error. At resonance, the derivative of exp(−γt/2) sin²(Gt) gives one strict maximum per period and the displayed zero nodes. A separately written numerical lobe replay gives N=26,50,124,247 at Δ=0.1,0.05,0.02,0.01 with g=γ=1, matching the frozen report; this is supplementary. The uploaded script was not executed.

## originality

PASS

The contribution supported is the all-time classification for the charger-pulsed, amplitude-damped, initially empty battery, including the closed detuned cutoff and an additive O(1) count with the explicit model normalization. The resonant baseline, two-mode spectrum and the general cosine-versus-growing-envelope mechanism are not novel. The strongest indexed telegraph analogue shares both the counting idea and the functional form of the leading coefficient under spectral identification, but its published assertion fixes stationary initial data for a different observable and supplies a scaled limit, not this cutoff or bounded-error cavity count.

## value

PASS

The sharp count and closed final-turning bound distinguish a singular resonance idealization from free decay under any fixed nonzero detuning in a canonical pulsed model. The explicit envelope yields an all-time stopping bound without arbitrarily truncating a transient simulation, and the error bound quantifies how many exact peaks are lost as detuning changes. This is not merely diagonalization, a new name for the telegraph law, or a fit to a finite peak count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
