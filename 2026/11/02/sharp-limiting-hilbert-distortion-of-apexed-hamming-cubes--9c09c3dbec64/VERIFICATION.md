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

The graph metric is one on original edges and apex edges, two on every other distinct pair. Unit tensors with coordinate inner product 1/2 have scaled squared norm 8/3 and squared separation (16/3)(1−2^(−k)) at Hamming distance k; equality at k=2 fixes the noncontracting normalization and the unit edges realize the stated expansion. In an arbitrary Hilbert embedding based at the apex, with t=C², Parseval gives R≤t and the one-flip energy gives U≤dt/4. A degree-j Walsh character changes sign on j(d−j) unordered two-flips, giving mean squared separation 8(dU−V)/(d(d−1))≥4. Weighted Cauchy–Schwarz gives V≥U²/t, and dU−U²/t increases on [0,dt/4], proving t≥8(d−1)/(3d) for all d≥2. This suffices for the exact limit. For the finite LP, Gram averaging preserves every affine squared-distance bound and PSD. Translation invariance diagonalizes the Gram matrix on Walsh characters, and permutation invariance groups the nonnegative masses by degree. At Hamming shell k the corresponding character average is the stated Krawtchouk sum. The degree-zero mass can be removed without violating the apex lower bound because 4≤a₂≤4 times the remaining mass. Conversely every feasible mixture is a real PSD Gram matrix with precisely the required distances. There is a compact feasible sublevel using the tensor upper bound, so the LP has a minimum. At d=2, a₂=4w₁ forces w₁≥1 and a₁=2w₁+4w₂≥2; w₁=1,w₂=0 attains t=2. An independent rational LP reproduction found t=2,2,2,20/9 for d=2,3,4,5, with numerical checks through d=12, not a proof of the infinite claim. Replay: /workspace/branches/f47ae752-0661-44d5-875e-7e5dc01330c2/lp_repro.py. The frozen VERIFY.py was inspected, not executed, and does not itself solve the LP.

## originality

PASS

Bounded best-of-knowledge pass for the sharp asymptotic constant and the exact orbit LP for this particular metric. Ordinary Hamming and Johnson graph theorems do not retain the cone's metric; same-day clique-join and tree records have different families, even where a finite special case or a limiting number coincides. The generic Gram SDP, Walsh diagonalization and symmetry reduction are established methods, not claimed as original. The shell estimate with its matching tensor map supplies distinct mathematical content beyond a change of notation in those methods.

## value

PASS

A universal hub changes the usual cube's diverging distortion into a bounded diameter-two problem. The exact limiting obstruction is not set by the diameter alone: the one- and two-coordinate shells compete with the common apex radius, and the feature map meets the resulting constant. This supplies a precise benchmark for one-point extensions of product metrics. The orbit-sized LP additionally makes the exact finite invariant accessible without a Gram matrix of exponential order, without claiming a finite closed form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
