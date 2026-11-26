---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a half-length h=tn+r, r=0 gives identical halves and is excluded. Conjugacy requires equal multiplicities; after deleting t full periods in counts, the adjacent cyclic r-arcs must therefore agree on every singleton position. Their symmetric difference has cardinality 2 min(r,n-r) (the arcs are disjoint when r<=n/2, and their complements otherwise). It is nonempty and contained in the two positions of the repeated letter. Hence r=1 or n-1 and these positions are cyclic neighbors in either case. This excludes factors of all lengths when the repeat is nonadjacent. For an adjacent repeat, rotating to aaC yields (Ca)(aC), distinct conjugate halves of length n-1. The only possible smaller residue is 1, which cannot give distinct conjugates for half-length 1. A singleton forces the period to be primitive; dividing the multinomial linear count by n gives q!/2 for fixed repeated label a. Fusing the adjacent aa gives (q-1)! circular arrangements, and subtraction gives the avoiding classes, including zero for q=2. Independent replay (`python3 independent_check.py`) directly tested all rotation classes for q=2 through 7, at all cyclic starts and half-lengths through 2(q+1), finding exactly the predicted table (at q=7: 2520/720/1800). The finite window does not prove infinite avoidance; the residue argument does. The supplied checker was inspected rather than run.

## originality

PASS

The supported distinct claim is the multialphabet periodic one-repeat dichotomy across arbitrarily many period boundaries, including exact shortest length and rotation-class counts. The binary boundary is covered by prior classification; neither the inspected bounded circular classification nor the alphabet-permutation results supply the multialphabet statement. This is a bounded best-of-knowledge assessment.

## value

PASS

This is a complete classification of the first natural repeated-letter extension of permutation periods. It isolates cyclic adjacency as the only obstruction, permits true infinite periodic avoidance despite repetition, and gives exact first witness length when avoidance fails. Applying a position-residue argument to all half-lengths is the useful content; the necklace counts are secondary consequences. It does not address several repeated labels or arbitrary periodic words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
