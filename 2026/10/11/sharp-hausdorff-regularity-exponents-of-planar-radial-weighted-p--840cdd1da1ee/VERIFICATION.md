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

PASS: Local boundary mass M_K(r)≤2πr for full planar convex bodies follows from convex intersection/perimeter monotonicity, and for segments double length ≤4r<2πr. Support parametrization x=h n+h'τ, ds=(h+h'')dθ, integration by parts gives exact shape derivative ∫v(f+ρ∇f·n) and no tangential v' remainder. For p<0 flat truncation f_eps=min(|x|^p,eps^p) bounds gradient ∫|∇f_eps|≤2π(1−p)eps^p, singular remainder ≤2π(-p)/(p+1)eps^(p+1), choose eps=δ. For p≥0 use bound ∫p|x|^(p−1) and radius R, yielding stated Lipschitz coefficients. Weak boundary measure limit and uniform cutoff extend to segments/points. Point vs small disk makes exponent p+1 optimal, concentric disks fixed radius force exponent≤1 for p>0. Finite CHECKS.py verifies selected disks/segments/triangles but cannot prove universal statement.

## originality

PASS

PASS best of knowledge with real access risk. Csató–Giovagnoli–Roy 2026 same functional has qualitative Hausdorff continuity with degenerate factor-two; companion Csató–Giovagnoli arxiv:2610.11677v1 Oct8 announces qualitative continuity, but primary full text inaccessible after OA attempts and authorized Oxford returned vpn_disconnected, so cannot infer whole-document absence of quantitative sharp exponents. Hug–Schneider support-measure 1/2 Hölder theorem has bounded-Lipschitz tests not singular |x|^p; Saracco–Stefani examines inclusion monotonicity rather than this two-body modulus. The explicit p-dependent full phase diagram and optimal witnesses not found in read accessible sources.

## value

PASS

PASS: Natural power-weighted geometric perimeter in shape optimization admits robust explicit Hausdorff error control even through collapse to segments/points. Singular/zero/positive parameter transition with optimal exponents distinguishes integrability barrier and is independently useful for stability estimates. Constants p≠0 not asserted optimal, and no higher dimensional scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
