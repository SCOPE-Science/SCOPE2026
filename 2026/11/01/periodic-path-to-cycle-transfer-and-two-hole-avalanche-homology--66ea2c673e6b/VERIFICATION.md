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

Binary supports translate right by one per round and truncate at the sink. Replacing a predecessor i by i+d shows F_t⊆F_{t-d} for t≥d. A common residue a for any intersection of the first d supports lifts to the physical vertex a+d (0≤a<d), so no intersections are lost at the sink for k≥2. The nerve has the claimed translates of -R and inversion identifies the cycle complex; nonempty intersections are simplices. Independently, residue reduction has a simplicial section a↦a+d, with the composite contiguous to the identity because original and section vertices share the same first-period firing simplex. For two holes the complements of the facets are edges of g disjoint C_L (K2 for L=2), so the nerve is the Alexander dual of their independence complex. Cone deletion of the second path vertex gives the three-step suspension recurrence; in the cycle cofibre one side of the map is contractible or the source sphere has strictly smaller dimension. L=3,4,5 give three points, two contractible components and a circle, respectively, and K2 gives S⁰. The join therefore has integral reduced cohomology of rank b in degree gs-1, and duality shifts it to degree d-gs-2 as claimed, including degree-zero cases. The frozen mod-two checker was inspected, not run, and is not evidence of integral torsion-freeness; the integral argument is decisive.

## originality

PASS

Credit the known cyclic and particular path cases and standard topology. The distinct content supported by the comparison is arbitrary binary repeated sink-path transfer with the first-period nerve, and its uniform two-hole application including noncoprime separations. The nearest periodic lifting result concerns cycles on both sides; the nearest two-hole classification concerns coprime shifts. Neither supplies the requisite no-boundary-loss equivalence for all motifs on terminating paths.

## value

PASS

One common second-block witness turns a terminating dynamical system into a finite-period homotopy calculation for every binary motif and every k≥2. This is useful beyond the previously classified small motifs. The two-hole case converts the arithmetic of separation into explicit integral ranks, including exponentially many classes in growing degree, without a size-dependent path computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
