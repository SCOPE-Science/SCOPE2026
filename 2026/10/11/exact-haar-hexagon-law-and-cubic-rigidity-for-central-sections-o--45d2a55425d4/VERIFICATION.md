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

A generic centered plane intersects both opposite faces x_i=±a_i in edges iff each weighted absolute normal X=a|u1|,Y=b|u2|,Z=c|u3| satisfies the strict triangle inequality against the other two. Thus six-sided sections occur exactly in the spherical cone spanned by (b,a,0),(c,0,a),(0,c,b) in the positive octant; otherwise centered symmetry and polygon geometry give four edges, with equality sets measure zero. An independent SymPy determinant gives -2abc and exact scalar products bc,ab,ac, yielding p6=4/pi arctan[2abc/(alpha beta gamma+bc gamma+ac beta+ab alpha)] by the classical solid-angle identity. AM-GM proves Q/(abc)>=5sqrt2 with equality only a=b=c; continuity along (t,1,1), t>=1, and limit0 proves every probability in (0,4/pi atan(sqrt2/5)]. The known cube equality 1-6/pi asin(1/3) is algebraically consistent. The actual verify_probability.py was read; its Monte Carlo trials cannot prove the general all-positive-a,b,c theorem, which the cone/AM-GM proof establishes.

## originality

PASS

Lonke's full 1998 work explicitly treats Haar central sections of a cube and its expected vertex count; in dimension three that computes the already-known equal-edge probability and is credited, not new. The exact unequal a,b,c law cannot be obtained by affinely stretching a Haar plane because the plane distribution changes; Lonke's equal-cube statement is not a broader-aspect-ratio result. Abas's orthotope width distribution is a different invariant, and the van Oosterom–Strackee spherical triangle identity is a standard calculation method. No covering unequal-box shape law or sharp all-aspect-ratio rigidity theorem found in actual inspected statements; inaccessible/hidden historical stereology remains a residual risk.

## value

PASS

Random Haar central-plane section combinatorics of three-dimensional boxes is a canonical stochastic-convex-geometry model. The explicit two-dimensional aspect-ratio dependence, uniqueness of cubic maximizer and exact full positive range are mathematically meaningful classifications, not an arbitrary slice or a restatement of the cube-only value. A researcher comparing anisotropic sections can use the exact law without seeking a broad higher-dimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
