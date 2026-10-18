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
# Computational verification

The primary finite proof is `census.cpp`. Compile using `g++ -O3 -std=c++17 census.cpp -o census`, then execute `./census`. It reproduces the exact minimum and the number of restricted-growth minimizing words at every length through 16, and checks each canonical-word total against hardcoded exact expectations. The run must terminate with `CENSUS_VERIFY_OK range=1..16`.

The independent checker `verify_independent.py` does not implement the recurrence. It enumerates selected position masks and groups them by the spelled scattered subsequence; it repeats the full minimum and minimizer census for all restricted-growth words through length nine and checks every listed optimizer at larger lengths. Execute with `python3 verify_independent.py`; the ending marker is `VERIFY_OK ternary_minimal_maxocc_length_1_to_16`.

The full canonical word census is `data/census.json`. Entries use base-zero symbols, and `canonical_minimizers` lists each minimizer exactly once up to bijective renaming. The exact domain is the full ternary alphabet with words allowed to omit letters. The work is a finite proof, not a proof of any uniform formula beyond length 16. The source enumeration is required to establish the lower bounds; checking optimal witnesses alone gives only upper bounds. No separate independent audit has been performed.
