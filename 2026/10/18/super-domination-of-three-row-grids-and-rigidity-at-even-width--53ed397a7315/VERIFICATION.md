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

# Reproducibility and scope of checks

`python3 verify.py` is a complete, standalone Python standard-library exact check of the mathematical finite-state certificate. The predicate `local_ok` tests all omitted-vertex witness possibilities and excludes both imaginary endpoint witnesses. The four-mask max-plus transfer stores *all* reachable states and exact integer maxima. The program asserts that at width \(9\) and width \(11\), and likewise at width \(10\) and width \(12\), supports are identical and every entry rises by exactly \(3\). It verifies \(1543\) reachable states in each compared vector. Since subsequent transfer steps are identical and max-plus homogeneous, this is the induction certificate, not an experiment assuming periodicity.

The program then closes both boundaries for every width \(1\) through \(12\) and asserts the exact optimum table \((2,3,5,6,9,9,12,12,15,15,18,18)\). An independently coded neighborhood-bitset exhaustive search of all possible omitted subsets for widths \(1\) through \(6\) validates the super domination predicate and produces the minimum-set counts \((3,2,4,2,60,2)\) for these widths; these finite sample counts are not asserted for general odd widths. The infinite minimum-set *count at even widths* is proved separately via graph cuts and four-cycle propagation in `RESULT.md`.

The proof does not verify other grid heights. Reproducibility checks were performed successfully on the exact embedded `verify.py` bytes. No external proof checker or independent human review has been carried out.
