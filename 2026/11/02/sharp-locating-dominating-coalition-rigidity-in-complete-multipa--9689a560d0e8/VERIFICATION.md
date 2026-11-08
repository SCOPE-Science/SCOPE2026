---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The final claim quantifies all finite complete multipartite graphs with r>=2 labelled parts each ni>=2, with open-neighborhood locating domination and distinct non-LD coalition blocks. For any D, LD is equivalent to |Pi\D|<=1 for each part, since unselected twins obstruct location and each Pi contributes a selected vertex for distinct external signatures and domination. Within-part pairs induce an auxiliary multigraph with loops, whose vertex covers encode unions of blocks. No one-cover plus every block in a two-cover forces <=4 cover-participating vertices. Four blocks cannot coexist with any loop or triangle, so every part size=2. Explicit 3- and 4-block constructions prove sharpness; at 4 classes auxiliary support must be 2K2, P4, or C4. Surjective labelled edge-type maps with 2^r within-part orientations divided by 4! yield A_r=2^(r-3)(4^r-5*2^r+6). Independent enumeration directly checked all unordered partitions for (2,2),(2,3),(2,2,2),(2,2,2,2), giving four-class counts 1,30,364 as required; finite checks supplement the structural proof. r=2 boundary and labelled vertices/unlabelled blocks correctly normalized.

## originality

PASS

Best-of-knowledge PASS for the all-part-size dichotomy, exact equality support and A_r enumerator; the known four-cycle r=2 boundary is acknowledged prior art, not separately claimed as new.

## value

PASS

Locating–dominating coalition number is a natural recently introduced domination parameter. A uniform bound of 3 or 4 independent of part count sharpens the general r+2 bound; equality rigidity and exact enumerator for the infinite cocktail-party family distinguish genuinely different coalitional decompositions. The two-cover obstruction is substantive and the complete classification can be used without redoing search for each graph; not a trivial substitution of a known LD number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
