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

On each strict sorting chamber the map is a permutation. Splitting a generic segment at coordinate crossings and using the triangle inequality gives the upper maximum over permutation norms; continuity handles segments lying in ties. A small arbitrary perturbation inside each chamber gives the reverse inequality. On the mean-zero subspace, the nearest-neighbor path Laplacian with degree-one ends has eigenmodes cos((j-1/2)k pi/N) by the second-difference equation (with equal ghost and endpoint values). The extreme nonzero eigenvalues are 4 sin^2(theta) and 4 cos^2(theta), theta=pi/(2N). Their eigenspaces are simple. For even N, reflection pairs opposite signs in both modes and sine/cosine complementation matches magnitudes, so a permutation attains the spectral ratio. For odd N the lowest mode has a zero coordinate while the highest has none; compactness and the finite permutation family make the inequality strict. For the odd lower bound, write v_(h+l)=(-1)^(h+l-1) cos(l pi/N), h=(N+1)/2. In increasing rank, expressing v as -cos of angles yields the even-angle grid when N=3 mod 4 (0 once and other angles twice) and the odd-angle grid when N=1 mod 4 (pi once and others twice). This matches the low-mode midpoints within theta in every rank. The positive semidefinite defect lambda_max I-L annihilates v, so the energy deficit of the permuted low mode is at most lambda_max N theta^2, giving the stated odd lower bound and asymptotic. Each sorted-value gap is crossed by at least one original path edge, whose square dominates the sum of its crossed gap squares, proving the separate one-point bound. A different-coordinate SVD enumeration (python /workspace/independent_checks.py 2) checked 872 permutations over N=2–6; this is finite numerical corroboration only.

## originality

PASS

The supported distinct contribution is the parity-resolved two-input path-gradient stability result and quantitative odd-N enclosure, not the spectral condition-number bound in isolation or one-input contraction. The closest checked two-input works concern different norms or the star graph; they give no all-path saturation result. The exact odd optimum is not claimed.

## value

PASS

The path-gradient norm of differences is a natural conditioning invariant for monotone sorting. The anti-contractive growth despite one-point contraction and the exact saturation parity are whole-family structure, while the uniform odd error shows that the strict obstruction does not change leading amplification. This is not a claim to the exact odd optimum or another graph's modulus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
