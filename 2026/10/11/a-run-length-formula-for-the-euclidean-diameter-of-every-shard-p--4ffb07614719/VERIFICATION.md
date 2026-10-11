---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The theorem is proved symbolically in `RESULT.md`; finite enumeration is corroborative only.

Verified source premises:
- an \(\alpha\)-alternating matching may be empty;
- its characteristic vector has \(+1\) coordinates only on \(\{a\}\cup A\) and \(-1\) coordinates only on \(B\cup\{b\}\);
- the vertices of the shard polytope are exactly these characteristic vectors.

Verified proof reductions:
- squared Euclidean distance of two vertices equals the Hamming size of their support symmetric difference;
- each matching uses at most one coordinate per maximal run;
- pairwise distance optimization therefore reduces to three open-matching states;
- a singleton run differs from a longer run only when both matchings try to use it, producing the four transition matrices displayed in `RESULT.md`;
- the max-plus invariant after every complete \(U_iD_i\) run pair yields the closed formula \(2(f+g)\);
- maximum distance from the zero vertex is \(2f\) in squared units, with exactly \(\prod_i p_iq_i\) maximizing vertices.

`verify.py` exhaustively enumerates every arc word of lengths \(2\) through \(10\), every alternating matching for each word, and every vertex pair. It compares direct Euclidean squared diameters and zero-vertex data against the formulas. This finite replay is not used as proof for arbitrary arc length.
