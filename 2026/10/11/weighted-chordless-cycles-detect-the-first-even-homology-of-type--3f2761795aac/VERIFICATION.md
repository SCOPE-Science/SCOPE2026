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
# Reproducibility and limits

Run `python3 verify.py` in a directory containing that standalone script. The checker uses only Python's standard library. It exactly enumerates permutations, computes minimum inversion lengths for every descent mask on 2 through 7 vertices, checks four explicitly labeled cycle examples against reduced clique homology shifts, and compares the first even degree and rank against independent chordless-cycle enumeration for 15 selected graphs. It prints `VERIFY_OK` and `INDEPENDENT_CYCLE_MINIMUM_AND_RANK_VERIFIED` on success.

The computations test instances and cannot prove all-parameter claims. The proof uses the published integral descent–Hochster theorem plus the descent-run inversion lemma and chordal clique homology. The result is not an independent validation or formal certification.
