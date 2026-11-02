---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For each strictly convex polygon at small radius the exact difference of Euclidean-close and boundary-close probabilities is r²/p² sum_j[β_j/sinβ_j−1], with the radius limit first. Centered equal-arclength chord direction is φ(c)+δ²κ′(c)/24+O_C1(δ⁴); adjacent chord subtraction gives β_j=δκ(s_j)+δ³κ″(s_j)/12+O(δ⁵) uniformly for C8 curves. Expansion of z/sin z−1 =z²/6+7z⁴/360+O(z⁶), periodic quadrature and ∫κκ″=−∫(κ′)² produce mΛ_m=L/6∫κ² + (L³/m²)[7/360∫κ⁴−1/36∫(κ′)²]+Oγ(m^-4). Fresh independent adaptive quadrature of support-function ovals h_p=1+cos(pθ)/[2(1−p²)], p=2,3 confirms identical ∫f(κ)ds via periodic substitution but distinct gradient energy and exact secondary 4√3π^4(378−85p²)/3645, with p2 positive and p3 negative. This verifies the key nonstandard coefficient. The finite numerical samples are not substitutes for analytic remainder control.

## originality

PASS

The exact fixed-polygon small-radius corner law is known earlier and explicitly credited. Discrete elastica/curvature Gamma-convergence sources study convergence of curve energies or their minimizers, whereas the claim concerns an exact O(m^-2) signed correction to an arclength-uniform random-pair boundary-shortcut observable and an equal-curvature-histogram counterexample. The most plausible Iglesias–Bruckstein article full text was inaccessible even through authorized connection; its abstract alone cannot prove whole-document noncoverage. Best-of-knowledge PASS with a named material risk.

## value

PASS

The r→0 boundary shortcut coefficient has a natural geometric probabilistic meaning, and its first continuum term is bending energy. The exact next term detects (κ′)^2 and distinguishes strictly convex ovals sharing every arclength curvature moment, proving the correction contains geometric frequency information invisible to curvature histograms. This is a nontrivial structural refinement rather than a routine leading-limit discretization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
