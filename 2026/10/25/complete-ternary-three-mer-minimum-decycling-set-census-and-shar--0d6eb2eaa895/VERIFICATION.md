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
# Reproducing the finite proof

Run `python3 verify.py` beside this file. No command-line arguments, downloads, packages, or external datasets are required. The program constructs the directed order-three ternary de Bruijn graph, enumerates all rotation-class transversals, independently compares short-cycle masks with Kahn cycle detection, computes longest residual paths, and determines orbit representatives under alphabet permutations and reversal. A separate direct ternary-word enumeration independently verifies the sharp absence/presence of each pattern set at lengths 8, 9, and 10.

Observed standard output begins with:

`TERNARY_3MER_MDS_PASS candidates=6561 optimum=11 minima=84 latency9=60 latency10=24 symmetry_orbits=7 short_cycles=3+18`

The verifier rewrites two CSV catalogs deterministically: `min_decycling_sets.csv` with the full 84-set classification, and `short_cycles.csv` with all 21 critical short directed cycles. The proof explains why 6561 is a complete candidate search: 11 pairwise-disjoint rotation cycles make 11 a sharp lower bound, so every 11-element decycling set has precisely one representative from each class. The finite checks alone do not establish corresponding assertions for larger de Bruijn graphs or other alphabets. Independent audit has not been performed.
