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

The standalone verifier `artifacts/verify_q7_frameproof.py` rebuilds the forbidden-triple relation directly from the binary Hamming-geodesic definition. It exhaustively enumerates all valid nine-word and ten-word codes after translating one codeword to `0000000`; the former count is 7,560 and the latter is zero. It then checks every enumerated maximum directly, reconstructs all coordinate permutations and translations, partitions the maxima into the two claimed Hamming-isometry orbits, and recomputes stabilizers, pair-distance profiles, and coordinate multiplicities.

The verifier uses no timeout, randomized search, external solver, cached certificate, or unproved pruning rule. Its only pruning step removes a future word exactly when that word and two already chosen words form a forbidden triple. The exhaustive search is finite over all 128 binary words of length seven. The result does not assert any classification in other lengths or alphabets.

Expected successful replay begins with:

```text
VERIFY_OK vertices=128 maximum=9 origin_maxima=7560 target10=0 labeled_maxima=107520 natural_group=645120 orbits=2 orbit_sizes=80640,26880 stabilizers=8,24
```
