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

# Reproduction

Compile and execute `census.cpp` with `g++ -std=c++17 -O3 census.cpp -o census && ./census`; the program enumerates the full labeled space and prints its subset-image diameters and complete-reachability totals. Independently run `python3 verify_canonical.py`; the script uses frontier sets rather than the C++ array queue, enumerates all normalized defect-one maps, checks the expected histogram and free rotation orbits, and prints `VERIFY_OK` on success.

The five-state Černý representative is `a=(1,2,3,4,0)` and `b=(0,1,2,3,0)`. The word `baaaabaaaabaaaabaaaa` has length \(20\) and maps the full state set to \(\{4\}\). The normalized search gives no word of length below \(20\) with this image.

The two programs' exhaustive input spaces differ: `census.cpp` examines all \(9,765,625\) ordered pairs, whereas `verify_canonical.py` checks \(1200\) normalized rank-four maps and their quotient under five cyclic relabelings. Their cross-check relies on the mathematical normal-form reduction. Verification is not an independent audit or a claim of beyond-scope results.
