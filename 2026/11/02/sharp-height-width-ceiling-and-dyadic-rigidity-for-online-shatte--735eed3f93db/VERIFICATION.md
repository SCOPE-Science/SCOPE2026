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

Run `python3 verify.py` with standard Python 3. The verifier enumerates every naturally labeled partial-order relation on one through six points, applies transitive closure, deduplicates exact relation matrices, enumerates all downsets and computes the exact complete-binary-tree rank by recursive query splitting. It separately determines height and width by full subset enumeration. The observed distinct relation counts are 1, 2, 7, 40, 357 and 4,824, totaling 5,231. The printed success marker is:

`HEIGHT_WIDTH_SHATTERING_ALL_CHECKS_PASS 5231`

Every enumerated case satisfies the universal upper bound; every case of height one or two has online dimension equal to width. Every rank-maximal height-three case is exactly a disjoint union of three-element chains, and the converse is checked. Additional tests construct disjoint chain unions for chain lengths two, three and seven, verifying their ideal counts and online ranks. The recursion is exhaustive on these *finite* examples and is not an infinite proof. The universal theorem, dyadic rigidity and exact extremal claim rest on the structural argument in `RESULT.md`.
