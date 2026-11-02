---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For q>=4 every vertex degree is 2q. Reconstructed the root-neighbor incidence count: for S with minimum internal degree q and v in S, coordinate-clique populations a<=2,b,c<=q-1, k=a+b+c>=q, B=S\({v}U A), and 2|B|>=qk-a^2-b^2-c^2. Convexity maximizes the square sum at (q-1,r,0), r=k-q+1, forcing |S|>=2q and equality only r=1 with full q-coordinate and one cross-direction, hence q-by-2-by-1 rectangles. Their count is 3q(q+1). Pairing the 3-by-q base grid, with an odd-q final three-cell column, yields floor(3q/2) full-coordinate colour classes and matches the size bound. Independent integer exhaustive checks over local (a,b,c) combinations, the complete rectangle census, and explicit majority partitions for q=4..14 passed; the proof supplies all q.

## originality

PASS

Lu balanced Hamming lemma implies 2q lower bound and hence upper on colours, so those components are covered. Previously published Cartesian-product work leaves unequal (3,q,q) case open and does not provide the explicit sharp partition or equality census. Actual primary full texts not obtainable in this execution; best-of-knowledge judgment qualified.

## value

PASS

Solves a natural imbalanced three-factor Hamming majority-partition extremum and completely classifies minimal dense cores with a nontrivial exact census. Lower core-size inequality is a known consequence of balanced Hamming isoperimetry, but new attaining unequal-factor partitions and equality rigidity are substantive and address a published parameter question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
