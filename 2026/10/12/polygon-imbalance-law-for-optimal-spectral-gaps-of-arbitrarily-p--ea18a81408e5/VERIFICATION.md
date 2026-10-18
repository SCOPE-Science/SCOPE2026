---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For star Laplacian and positive costs c_i=d_i², the Rayleigh/PSD inequality evaluated on a minimum-resultant polygon embedding bounds λ2 by Λ=[S−δ²/(m+1)]^{-1}, S=Σc_i, δ=(2 max d_i−Σd_i)_+. The min resultant in R² is zero exactly at the polygon inequality, and otherwise δ with unique largest side. If δ=0 all rates 1/S attain the bound; saturation of the centered embedding equality forces each leaf rate. For δ>0, prescribed w_j=Λ(1−δ/(n d_j)) and w_i=Λ(1+δ/(n d_i)) are positive and satisfy exact cost one. The proof does not merely find an eigenvector: it gives a full PSD certificate L−ΛP as Λ/n times δ[Σ_{i≠j} z_i²/d_i−T²/B]+(B/d_j)(z_j+d_jT/B)². Both terms nonnegative, and nullity gives a simple λ2. The saturated eigenvector forces uniqueness for any optimal allocation. The two-leaf case and equality polygon boundary are included. Independently checked exact example (25,4,1) with Λ=1/29, rates (9/290,5/116,3/58), budget one and symbolic PSD identity.

## originality

PASS

The primary Sun–Boyd–Xiao–Diaconis paper establishes the general arbitrary-price SDP/max-variance duality, but its worked exact families are paths/cycles rather than the proposed all-price star formula. Göring–Helmberg–Wappler analyze a symmetric/uniform-cost star embedding and cannot settle the strict price-imbalance transition. The later Farhadi–Louis–Singh–Tetali treatment of tree variance embedding and an alternate star infinity functional does not state the same exact spectral-cost rates. There is a best-of-knowledge possibility of an equivalent formula in older tree connectivity literature, notably Fiedler 1990 not read in full.

## value

PASS

Exact optimization of algebraic connectivity under heterogeneous linear edge prices is a natural rate-allocation question. The closed polygon-inequality bifurcation, unique optimizer, spectral multiplicity change, and a sharp semidefinite sum-of-squares certificate replace a generic convex-program solver for an entire continuous family. This is a motivated structural theorem, not just the known equal-price star instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
