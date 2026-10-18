---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For centered affine-regular hexagons H=conv{±u,±v,±(v−u)} with nonsingular u,v, area=3|det(u,v)|. Regular unit octagon has eight facets n_j·z≤1 over Q(√2), n_j=(±1,±(√2−1)) or swapped. Dihedral symmetry fixes u on first edge. The boundary conditions for v and v−u reduce via facet enumeration to three positive determinant edge chambers (and reflected negative partners), with quadratic D_i(s) and parameter intervals in frozen RESULT.md. Independently symbolically differentiated all three D_i and verified their endpoint maximum (3−√2)/2, unique interior minimum (2+3√2)/8 at s=1/2−√2/4, 1/2, 1/2+√2/4, with middle chamber spanning the full range. The area spectrum is 3 times determinant interval, divided by octagon area 2√2 for normalized interval. Independently enumerated 8^5 possible active facet assignments for general translated center c (using linear solves and linear-program feasibility): 3392 rank-deficient facet systems, 29 feasible polyhedra and no detected noncentral nondegenerate sampled vertex-pair solutions; this computational exploration does not by itself formally prove centrality or exhaustive positive-dimensional interior cases. Lassak 2003 explicitly treats the same center o of K and inscribed H in its extremal theorem, consistent with the centered reduction. Bundled verify.py has complete symbolic chamber enumeration but uses high-precision float comparisons for signs, so call it exact symbolic formulas with numerically classified signs, not fully certified sign arithmetic.

## originality

PASS

Lassak 2003 addresses the exact extremal geometric object in every centrally symmetric planar body but gives structural necessary extremal conditions rather than the numerical octagon spectrum. Its reference to the regular octagon concerns packing ratio, not area extremizers. The specialized facet enumeration and complete attainable interval are a new natural exact case on the inspected evidence.

## value

PASS

The regular octagon is a canonical symmetric test body for the general extremal-area affine-regular hexagon problem, contrasted with the constant-area ellipse/parallelogram cases. Exact min/max together with attainment of *every* intermediate area give a complete meaningful finite classification and benchmark for centrally symmetric convex geometry, not an arbitrary coefficient trick or small gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
