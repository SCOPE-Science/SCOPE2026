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

Run `python3 check_full.py` and compare with `output_full.txt`; run `python3 check_translation.py` and compare with `output_translation.txt`. Both commands were executed from the supplied standalone source files, and exact stdout matched the records.

The first algorithm enumerates all \(\binom{64}{3}=41664\) unordered anchor triples and all eight extension patterns, for \(333312\) total cases. None has zero witnesses. The second uses translation transitivity, fixes one anchor at zero, enumerates all \(63\cdot62=3906\) ordered pairs of remaining relative anchors, and directly checks every adjacency pattern. It does not use precomputed bitsets or output from the first algorithm.

The classification for all orders reduces algebraically to the order-eight finite case, using the rectangle law and regular elementary abelian permutation group argument. For larger powers of two a four-vector linear-independence obstruction is explicit. Finite checks do not serve as evidence for arbitrary Latin squares except through this reduction. The two checks are ordinary reproducibility checks, not an independent audit or a formally verified proof.
