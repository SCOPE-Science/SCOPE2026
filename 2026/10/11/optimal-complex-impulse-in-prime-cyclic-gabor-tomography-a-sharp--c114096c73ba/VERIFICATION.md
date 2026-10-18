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

For prime p≥5 and complex z, directly expand the ambiguity of normalized g=1+zδ_0 into (0,0), (u=0,v≠0), (u≠0,v=0), and mixed uv≠0 branches. Weyl matrices form an orthonormal Hilbert–Schmidt basis and its columns after lifting are orthogonal p²-Fourier characters, producing exactly the claimed p² singular values, mixed j multiplicity p−1. The trivial ambiguity 1 gives s_max=√p. For z=re^{i phi}, mixed branches give s_min/√p≤2r mu_p(phi)/(p+r²+2r cosphi)≤mu_p(phi)/(√p+cosphi), equality in radial AM–GM only when r=√p. Angular zero phases form the p-grid with one missing node; case splitting for cosphi≥0, the outer two intervals, and the middle interval proves the sharp unique phase ±π/2. At z=±i√p unmixed normalized branches equal 1/2 and the mixed minimum sin(pi/p)/√p is smaller, so s_min=sin(pi/p)>0 and κ=√p/sin(pi/p), with exactly two optimizers. Finite actual SVD/angle-grid independent checks p=5,7 corroborated the theorem but do not replace the global angular proof.

## originality

PASS

A sharp phase-radius minimax for the two-level flat-plus-one-complex-impulse family and rigid optimizers ±i√p survive; the general Weyl-ambiguity singular formula was already known and is explicitly excluded from novelty.

## value

PASS

Conditioning of a natural minimal-perturbation flat Gabor window is a meaningful restricted signal-design problem. The theorem identifies both globally sharp stability loss of order p^{3/2} and the uniquely optimal imaginary perturbations, a nontrivial phase effect missed by positive-real spikes. The restricted family is explicitly motivated and the claim does not conflate it with unrestricted Gabor-window optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
