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

PASS. Directly reconstructed spectral majorization reduction to the scalar simplex and strict-convex KKT (μ_i=(λ_i−τ)_+, trace 1), making the nearest-state map independent of 1<p<∞. On traceless 2×2 and 3×3 Hermitians the S_p norms at every p (n=2), respectively S4 alone (n=3), are proportional to S2; Hilbert projection gives constant 1, fixed distinct states make it sharp. For n≥4 derivative of ||diag(1,1,−2,0)+t diag(1,1,1,−3)||_p^p is p(2−2^(p−1)), vanishing only at 2; the three-active-coordinate threshold map removes the Z direction and produces strict expansion. For n=3 independently differentiated the noncommuting Y=[[1,0,1],[0,−1,0],[1,0,0]], Z=diag(1,1,−2): (1/p) derivative of ||Y+tZ||_p^p equals (φ^(p−3)+φ^(3−p))/√5−1 and vanishes only at 2,4. At the simple-spectrum Aδ the divided-difference derivative converges to Y. Independent numerical derivatives agree at nine exponents; 80 random-projection checks and six finite expansive witnesses corroborate but do not prove the universal bounds. The theorem proves only qualitative strict expansion; no exact expansive constants or endpoints.

## originality

PASS

PASS. Matrix spectral clipping and water filling are known, but the exact ambient-trace-one nonexpansivity phase diagram, especially the exceptional noncommuting qutrit (3,4), is not implied by the inspected published Frobenius quantum-channel feasibility work or universal unitarily invariant low-rank approximation theorem. The latter starts from positive input density matrices and a nonconvex rank cap; for k=n the projection is the identity, so it cannot encode expansion of trace-one indefinite Hermitian inputs. Distinguishing Schatten4 on the traceless affine difference subspace from globally Hilbertian norms matters. Mathematically stronger coverage was sought in Resultary and web aliases, not found; this is not a novelty guarantee.

## value

PASS

PASS. A full dimension/exponent nonexpansivity classification for a canonical convex quantum-state projection, with an exceptional non-Hilbert Schatten exponent and sharp local expansion mechanisms, answers a motivated stability question for spectral thresholding, not merely a change of notation or routine numerical calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
