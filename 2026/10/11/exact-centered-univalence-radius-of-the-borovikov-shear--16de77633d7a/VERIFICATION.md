---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

From the actual Git RESULT.md blob b26f24e194e2cfa019ce15b39e938b50223adc07, reconstruct W(z)=log((1−z²)/(1+z²)), which is analytic because the quotient maps the disk into the right half-plane. W′(z)=−4z/(1−z⁴); CR gives u_y=−8/π Re[z/(1−z⁴)], whence the claimed Jacobian. For |z|≤r, Re[z/(1−z⁴)]≤|z|/(1−|z|^4)≤r/(1−r⁴), and equality for r>0 forces |z|=r,z^4=r^4 and positive-real quotient, hence unique z=r. Strict radial increase yields J>0 inside r_M and J=0 at positive real r_M. F_M(x+iy)=x+iY_x(y) fixes x and each vertical disk slice is connected; ∂_yY_x=J>0 gives global injectivity. For r>r_M the larger disk contains a Jacobian zero, contradicting Lewy’s necessary nonzero-Jacobian theorem for injective harmonic maps. No finite grid is needed. Independently differentiated the rational kernel and checked the equality/radial monotonicity argument; separate Resultary fiber-valence analysis confirms the same explicit shear, without substituting for this full-disk proof.

## originality

PASS

Best-of-knowledge: the source fold equation and published derivative-optimality result are not enough to prove the fold is the first point anywhere in every centered disk, nor global injectivity before it; the full-disk Jacobian extremum and vertical-fiber monotonicity supply genuinely additional conclusions. Original recent preprint full text was unavailable; residual risk is stated rather than an automatic failure.

## value

PASS

It is a genuinely motivated exact boundary for a newly important explicit harmonic counterexample: distinguishing a single known axial fold from the first collapse anywhere plus global no-collision on the entire centered disk settles a meaningful geometry question. The exact Jacobian-minimum identity itself can be reused, and does not purport to solve the universal Landau problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
