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

A unit vector in ker N satisfies all three bands strictly for every admissible t>0 in the singular case. Otherwise the transit event is S²∩tA[-1,1]³. Strict convexity of ||Az||² restricts all maximizers on the unit cube to vertices. It follows that there are no directions below t_c, only finitely many at equality, and a spherical neighborhood around a maximizing direction above t_c. The right-hand limit is admissible: H² is at least the average squared signed-corner norm ∑||A_i||², at least ∑h_i² since n_i·A_i=h_i, and thus strictly larger than max h_i². Compactness excludes patches other than the disjoint neighborhoods of maximizing corners. At each corner let y be its inward offsets, d_i=s_i u_s·A_i. Flipping the ith sign gives d_i≥||A_i||²/H>0. In the local equation write y_i=ρ θ_i/d_i with θ_i≥0 and ∑θ_i=1. The derivative in ρ of the squared-norm equation at (ρ,δ)=(0,0) is −2 independently of θ, and its δ derivative is 2H. Its unique local solution on this fixed compact simplex is ρ=Hδ+O(δ²) with one θ derivative. The leading physical area Jacobian in θ_1,θ_2 is δ² H²|det A|/(d_1 d_2 d_3), by the cross-product transform with (A diag(s))^T u_s=d. The simplex has coordinate area 1/2, and the Jacobian error is O(δ³); summing and dividing by 4π gives exactly the stated formula, including all ties. At A=I/√3 there are eight corners, d_i=1/3, and C=3√3/π. VERIFICATION.md and verify.py were inspected, not executed. The proof is for each fixed geometry and common scale, not a uniform error bound as geometry tends to singularity or a new tie.

## originality

PASS

The band model, general numerical spherical-area problem, and the elementary farthest-vertex criterion are not the substantive originality. The supported addition is the sharp analytic surface-area onset for arbitrary invertible triple geometry and relative widths, including all ties and an explicit positive coefficient. Neither the directly competing CORBITS method nor the closest polytope-contact results state or mechanically yield that coefficient for this event in the inspected passages.

## value

PASS

For a natural joint-selection model, knowing whether visibility is positive does not quantify how rapidly it first becomes detectable. An explicit, strictly positive coefficient gives the leading small probability directly, even when multiple contacts tie, without resolving tiny areas numerically. It is useful across all fixed nonsingular triple geometries and arbitrary relative widths, not just the orthogonal benchmark; it does not model survey completeness or eccentric-orbit effects.

The dated certificate retains the supplied scientific assessment, sources and limitations.
