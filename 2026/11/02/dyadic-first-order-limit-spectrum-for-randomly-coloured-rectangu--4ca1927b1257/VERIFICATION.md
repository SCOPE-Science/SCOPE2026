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
# Verification

`python3 checker.py` requires only standard Python 3. The script performs:

- exact orbit-denomination totals and gap-free subset-sum coverage for alphabets of cardinalities \(4,8,16\);
- direct breadth-first computation of shortest-path multiplicities from each corner in \(5\times6\), \(8\times11\), and \(10\times10\) grids, verifying unique diagonal maximizers at fixed tested distances;
- independent enumeration of all \(256\) four-code tuples on a four-letter alphabet, yielding the multiplicity-pattern counts \(4,48,36,144,24\).

Observed final line: `ALL_CHECKS_OK`. These finite checks support the path-count and orbit formulas. They do not establish Hanf locality or asymptotic concentration; those statements are supplied by the mathematical proof and the cited locality theorem. The exact formula construction is for each fixed dyadic rational with a sufficiently large grid, not a bound uniform across all formulas.
