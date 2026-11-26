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

The rank-one midpoint factor is the stated convex two-site update at finite h. Positive diagonal entries and a positive sweep transition for each original oriented tree edge imply irreducibility and aperiodicity, so the zero-sum radius is strictly below one. Starting with singleton cycles, every edge joins different components of a growing forest, and the transposition merges their cycles; the limiting P is one n-cycle. Writing s=1/h gives P⁻¹M=I−sH+O(s²) with H the sum of the transported incidence outer products divided by rates. Differentiating each simple eigenvalue of P gives −ζ_k u_k*Hu_k, and the normalized cycle Fourier vectors give the displayed sine-square formula. If any nonconstant mode had zero first-order attenuation, it would be fixed by all the transported transpositions and therefore by P, a contradiction. As a check on the path and star simplifications, omitting edge j from P multiplies it on the right by its transported transposition; this splits P into cycles of lengths d_j and n−d_j. The two cycles are the components after deleting the original edge. Thus a path has split sizes j and n−j (the sine-square sum is n/2), whereas all star splits are 1 and n−1. For small h the scaled matrix (I−M)/h is L_T+O(h); since the baseline L_T is symmetric, its eigenvalues cluster within O(h) of those of L_T, with the appropriate multiplicities, giving the stated spectral-radius expansions even for the repeated star eigenvalue. For n≥4 the connectivity ordering is opposite to the ordering of the stiff deficits. Continuity on the fixed zero-sum space gives at least one crossover, not uniqueness.

## originality

PASS

Best-of-knowledge pass for the explicit weighted-tree stiff Fourier coefficient and the parameter-driven equal-rate path/star reversal. The finite-h pair update is exactly a convex gossip update of neighbor weight q=ha/(1+ha); neither periodic gossip, its tree edge-order invariance, nor path/star benchmarking is new. The closest periodic-gossip full text could not be obtained lawfully in the attempted routes; its actual abstract and the other accessible passages do not establish coverage of the stiff coefficient or reversal.

## value

PASS

The result quantifies how a strictly mixing algorithm approaches a nonmixing permutation in the stiff regime; the coefficient explains precisely why an ordering suggested by continuous-time connectivity can reverse for the completed discrete sweep. The formula treats arbitrary positive rates on every finite tree, not just an isolated numerical crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
