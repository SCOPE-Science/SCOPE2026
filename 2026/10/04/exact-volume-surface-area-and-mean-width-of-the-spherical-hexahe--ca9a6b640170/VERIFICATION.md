---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The intersection inequality reduces exactly to \(\|x\|^2+\sqrt2\|x\|_\infty\le1/2\), giving vertices \((\pm1/(3\sqrt2),\pm1/(3\sqrt2),\pm1/(3\sqrt2))\) and adjacent distance \(\sqrt2/3\). The three active unit-sphere normals along an edge give \(\cos\alpha=23/27\). Gauss-Bonnet on one congruent spherical face, followed by symmetry, yields \(S=4\pi-20\alpha\). The divergence-theorem/vector-area calculation gives \(V=4\pi/3+2/(3\sqrt2)-49\alpha/6\), while the standard face-curvature plus edge contribution gives the stated Finch-normalized mean width. Fresh numerical evaluation reproduces \(V=0.158029005045087\), \(S=1.540658645708557\), \(W=0.722630772064860\), and an independent spherical radial quadrature gave \(V=0.1580223742\), consistent at the expected grid error.

## originality

PASS

Finch explicitly ends his 2013 paper by asking for exact \(V\), surface area, and mean width of this spherical hexahedron and supplies only a numerical normalized volume. Dodd and Theodorou give a general analytical algorithm for volume and exposed surface area of arbitrary intersecting spheres, so the volume and area components are in principle covered by a broader computational framework and should not be treated as conceptually new by themselves. That framework does not address mean width, and Finch's later explicit open question, after citing the sphere-intersection literature, confirms the missing same-object exact evaluation. Current exact-formula searches for the \(23/27\) angle and the displayed mean width found no prior source.

## value

PASS

The record answers a named exact-evaluation question for a canonical six-sphere intersection and supplies all three intrinsic measures in one normalization, including mean width, which is not covered by the general volume/surface algorithms. The correction of the adjacent-vertex scale and the consistency of the three measures make this a useful convex-geometry reference result rather than a gratuitous symbolic simplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
