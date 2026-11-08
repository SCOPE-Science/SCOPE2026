---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The displayed 30-edge icosahedron has 125 perfect matchings; independent face generation recovers f=(30,315,1260,1575,750,125), Euler characteristic 25, agreeing with 43 S2 and 19 S3. Full verifier source constructs 1975 acyclic face-poset pairs, 65 critical 2-cells, 41 critical 3-cells, and 65x41 signed boundary with rank22 and unit 22x22 minor -1; the code explicitly computes acyclic Hasse sort and a Bareiss minor rather than reading a log. Under the proved acyclicity, integral Morse cancellation gives ranks 43 and 19 with no torsion; since pi_2 of the wedge of 65 spheres is free on their generators, Smith unit pivots identify the full 3-dimensional CW homotopy type. The pure 5-dimensional complex is not shellable due to lower homology. The independent bounded check reproduces face counts, not the full signed Morse reduction.

## originality

PASS

The extension-restricted perfect-matching complex differs from the ordinary matching complex of the same icosahedron: the ordinary complex includes nonextendable matchings, has 5887 nonempty faces and Z/3 torsion in H3, whereas this complex has 4055 nonempty faces and torsion-free H2,H3. Bayer et al. and Chandrakar–Singh treat honeycomb/polygonal families, neither giving this finite icosahedral computation.

## value

PASS

The standard highly symmetric planar icosahedron is a motivated benchmark for extension-restricted matchings; the mixed-dimensional, torsion-free wedge and non-shellability distinguish its topology from the known torsion ordinary matching complex. Exact computation of a natural finite complex is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
