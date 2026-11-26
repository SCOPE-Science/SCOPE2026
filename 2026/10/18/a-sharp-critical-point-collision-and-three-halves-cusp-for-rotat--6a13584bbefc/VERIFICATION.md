---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For q=r² the derivative numerator is N=q(w⁴+1)−4rc(w³+w)+(3+4qc²−q²)w²; the denominator V² is zero-free on the closed disk. Dividing N by w² gives the quadratic in u=w+w⁻¹ with discriminant 4q(1−q)(4c²−3−q). The boundary Poisson formula excludes u∈[−2,2] for either root; every other u has exactly one inverse in the disk, with nonzero local coordinate derivative. The conjugation relation and continuity of the real roots from the double root give precisely the stated nonreal-conjugate and real-sign regimes. At c=c₀, u₀=2c₀/r>2 and N=q(w²−u₀w+1)², with inner root t=(√(3+r²)−√(3(1−r²)))/(2r). Each base zero of C is simple because c∈(−1,1), so no critical value is zero; a shared value of two simple cubic critical points would require a fiber of degree at least four. Since C′(0)=q, the lift gives just the origin multiplicity n−1 and n copies of every nonzero ramification point with unchanged multiplicity (total 3n−1). For δ=c−c₀, N_{ww}=2q(u₀²−4)=6(1−q) and N_c=−8c₀(1−q)t² at the double root. Consequently F_w(c,t+x)=a(x²−bδ)+O_r(|x|³+|δx|+δ²), with a=3(1−q)/D₀² and b=8c₀t²/3. The reciprocal quadratic gives branch endpoints x=±√(bδ)+O_r(|δ|) on both sides. Integrating F_w between them gives −(4/3)a(bδ)^(3/2)+O_r(|δ|²) with a consistent square root; its absolute leading coefficient is exactly the stated K(r). Sign symmetry gives the other collision. This is local at fixed r, excludes the prescribed-zero collisions at c=±1, and applies also at n=1 where the origin is not critical. checker.py was inspected, not executed; the proof replaces finite splitting probes.

## originality

PASS

Standard finite-Blaschke ramification theory, generic cubic splitting, and the elementary cyclic lift are not independently new. The distinct verified output is the exact bifurcation in the prescribed-zero coordinates and its sharp positive K(r), including the complete critical-point and critical-value consequences for the lifted family. The strongest inspected cubic normal-form passage does not give this parameter boundary or splitting constant; indexed collisions concern other maps or other predicates. The targeted comparison is not an exhaustive priority determination.

## value

PASS

Specifying an origin and a pair of rotated regular zero polygons is a natural geometric normalization, and the exact boundary resolves when the lifted interior ramification changes from two simple orbits to a single doubly ramified one. The nonzero explicit splitting constant controls actual image separation as the prescribed zero angle changes; it is information not furnished by a generic exponent or degree count. The result is local at fixed radius and does not purport to characterize general cubic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
