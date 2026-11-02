---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For q_epsilon=(s^4-t^4,s^2t^2+epsilon s^4,t^2,s^2-st,st), the two Cox coprimeness conditions hold for every parameter because v2=t^2 and v3=s(s-t) never vanish simultaneously and u0 is nonzero when w=st=0. The selected epsilon-independent 3x3 minors of the 5x3 Cox differential are -4t^2(3s^4+t^4), -4s(s-t)^2(s^3-st^2-2t^3), and 4st^2(2s-t); independently reconstructed symbolically. If s=0 or t=0 one of the first two minors is nonzero; if st != 0 and all minors vanished the third forces t=2s, contradicting the first (-304s^6). Therefore the differential rank is three globally in characteristic zero. Using Iwasaki Appendix A.1, an independently reconstructed full 16x16 relative cohomology matrix has exact determinant 4096 epsilon(1-4epsilon), rank 15 at epsilon=0 and 1/4, and rank 16 away from those roots. For rank-two degree-12 normal N=O(a)+O(12-a), a<=6, h0(N(-7))=6-a equals the matrix corank. Consequently N=O(5)+O(7) at both roots, balanced O(6)^2 elsewhere; simple determinant roots define reduced pullback divisor V(epsilon(1-4epsilon)). The source Cox resolution/determinantal scheme interpretation supplies the nonstandard geometric identification; computations verify its actual special matrix, not merely a prerecorded VERIFY_OK log.

## originality

PASS

Best-of-knowledge PASS restricted to the global geometric classification of this canonical affine deformation. Iwasaki Proposition 6.7 supplies q0, the local deformation and general determinantal framework, and its Appendix A.1 already factors the entire determinant, but it establishes U-membership only near 0. The missing global rank premise is necessary to assert the second determinant root is a genuine unramified jumping curve, and the independent case split verifies it. Cela--Lian is about general curves, not this explicit special one-parameter family. Published-record and exact-formula searches returned no separate coverage. This is close to primary prior mathematics and priority risk is material and recorded.

## value

PASS

The one-parameter slice is the original paper’s distinguished explicit deformation through its jumping-divisor smooth point, so it is a motivated geometric object rather than an arbitrary numeric slice. Globalizing its membership in the unramified map locus turns the already-known factored determinant into a genuine complete two-point reduced intersection classification, including the second exact unbalanced map and no other jumps on that line. The result is narrow and technically close to the source but is a complete natural parameter-line splitting classification useful for testing the geometry of the determinant/jumping stratum; it does not claim the whole divisor or a new general technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
