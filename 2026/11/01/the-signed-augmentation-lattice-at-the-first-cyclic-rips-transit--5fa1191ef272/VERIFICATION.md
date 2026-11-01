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

# Verification and limits

The all-parameter proof in `RESULT.md` classifies the cliques, identifies the circular-arc nerve core, and calculates the primitive integral attaching degrees with the exact dihedral orientation signs. This argument establishes the infinite-family theorem without extrapolation from finite data.

Run `python3 verify_cycle_power.py` from the same directory as this file. The script uses only Python's standard library. The output in `verify_cycle_power_output.txt` records the finite checks for every integer \(2\le k\le8\). It constructs the interval-core simplices, checks exceptional triangles and boundaries, calculates their Euler characteristic, and calculates the signed simplicial Lefschetz number for every rotation and reflection at every tested parameter. For \(2\le k\le4\), independent brute-force enumeration of all vertex subsets confirms that the classified faces are exactly the cliques of the corresponding graph power.

The exact signed simplicial Lefschetz values agree with the claimed homological character for all tested symmetries. The checks do not prove a universal statement by enumeration; that proof comes from the covering-and-attachment argument. The finite checker does not establish novelty or an equivariant homotopy equivalence. Independent audit: not performed.
