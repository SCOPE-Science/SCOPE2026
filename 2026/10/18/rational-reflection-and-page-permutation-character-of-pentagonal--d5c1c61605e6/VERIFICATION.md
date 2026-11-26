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

Independent equivariant filtration proof: let Y consist of the cone with apex F on the join of the n middle-edge choices {B_i,C_i}, together with all matchings with exactly one endpoint edge A_i or D_j. Each such one-endpoint cone attaches along a cone in the middle-edge complex: at its own page only C_i, respectively B_j, remains available. Their intersections are contained in the base, so Y has zero reduced homology. The relative chains split over the ordered endpoint pairs A_i,D_j, joined to their compatible middle-edge complexes, with degree shifted up by two. For i≠j the middle complex is a cone (C_i and B_j are each the sole choice on their respective pages), so that pair contributes no homology. For i=j both middle edges on page i are forbidden; the other n−1 choices form a join of 0-spheres, so each diagonal pair contributes one line in degree n. The reduced long exact sequence identifies these relative groups equivariantly with the claimed reduced homology. A permutation sends each diagonal line to the line indexed by the image of its page. For a fixed page the orientation sign is sgn(π), coming from permuting the remaining ordered join factors. Global reversal swaps the two endpoint edges and independently reverses the 0-sphere generators on the other n−1 pages, giving (−1)^n on every diagonal line. Thus the traces hold including permutations with no fixed pages. The character determines the rational module; the Specht hook follows from sign-twisting the standard summand of the page module. The frozen blocker matching is also consistent: the two second-stage types of upward steps preserve the blocker pattern, and the unmatched residual arrows form paths V_i→T_i→U_i→C→C∪{F}.

## originality

PASS

The nonequivariant homotopy conclusion is not new and is not credited as the originality claim. The compared primary passages and closest indexed findings did not cover the exact rational module for common-edge pentagons, in particular the global reflection sign and its combination with the page action. This is a bounded best-of-knowledge comparison, not a priority guarantee.

## value

PASS

The book is a natural edge-glued counterpart to vertex-glued windmills and linear tilings, with page permutations and one shared reversal. The exact module distinguishes this gluing at the representation level and specifies how reversal acts, information ordinary contractions cannot supply. In particular the result uniformly explains why only same-page endpoint pairs support homology lines and why global reversal has parity n. It gives useful exact traces for every symmetry of this natural family rather than a small sample or isolated numerical Betti number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
