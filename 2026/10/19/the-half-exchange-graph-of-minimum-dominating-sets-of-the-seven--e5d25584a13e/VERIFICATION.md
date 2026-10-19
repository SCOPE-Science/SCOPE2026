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

The graph and all 240 code sets are built using only Python standard-library modules. Invoke `python3 verify_steiner.py certificate.json`, then `python3 verify_permutation.py certificate.json` from the directory holding the files. The first script enumerates 30 Steiner triple systems on seven points with a pair-exact-cover recursion and constructs their eight Hamming-code cosets; the second independently generates the same sets by 5040 parity-check-column permutations and all translations. Both validate exact pair intersections and every breadth-first distance sphere of the 240-vertex exchange graph.

Observed output files: `steiner.log` and `permutation.log`. The certificate digest is `c781514e90db3505a668f3b39a284e8072605fb2d9967fa9504a7b913b21d89d`. The reconstructed certificate consists of 240 sorted sets of 16 integer-encoded seven-bit vertices and 1680 pairs of set indices. The generated profile at every start is 1, 14, 63, 106, 56, hence connected and diameter four. The complete 28,680-pair intersection table has frequencies 12,600 (zero), 7,680 (two), 6,720 (four), and 1,680 (eight).

Finite exact checks prove only the enumerated Q7 assertion once completeness of the Steiner reduction is established in the written proof. The programs do not establish priority over all published or unpublished literature, do not extend to other hypercube dimensions, and do not constitute independent external validation.
