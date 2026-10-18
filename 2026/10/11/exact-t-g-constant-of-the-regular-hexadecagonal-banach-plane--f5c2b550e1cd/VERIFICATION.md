---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The actual RESULT.md supplies the 8 facet-functionals norm and dihedral reduction x=v0+a(v1-v0), a in [0,1]. With z=x-y, x=y+z and y,z on polygonal edges, the complete admissible y,z edge-pair solutions reduce to six nondegenerate oriented branches: (E2,E13),(E3,E13),(E3,E14) and their swaps. Their exact a intervals are [0,q],[q,1-q],[1-q,1], q=2-sqrt2-(3/2)sqrt(2-sqrt2)+(1/2)sqrt(2+sqrt2). Explicit norm branch table yields factors T and T-kappa1*a, middle T-kappa2*(a-q) and T-kappa2*(1-q-a), and endpoint swap; both kappas positive. Simultaneous equality at x=(1,0), y=(1/2,h) with h the stated exact facet intersection. Source verify.py was read: it enumerates 256 edge pairs but uses floating tolerance and a dense 1001-point replay of branch formulas, not a rigorous exact-computer algebra certificate. Its feasible branch structure and equality values were corroborated; the mathematical argument relies on exact edge equations and algebra in RESULT.md, not the floating samples. This is a specific 16-gon theorem, not all 4n-gons.

## originality

PASS

Bounded best-of-knowledge originality: the exact stated invariant and quantified result were compared by implication to the closest primary and published SCOPE sources; no decisive covering result found. Unread material and alternative nomenclature remain explicit, and source search is not proof of absolute novelty.

## value

PASS

T_G is a motivated geometric invariant and the first sharp hexadecagon computation here gives not only a number but a stronger simultaneous-factor envelope with exact extremizer. Polygonal facet transitions are genuinely more involved than Hilbert-space or octagonal cases and illuminate the geometric-mean functional.

The dated certificate retains the supplied scientific assessment, sources and limitations.
