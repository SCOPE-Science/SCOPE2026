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

# Reproduction and scope

Use Python 3, with no third-party dependencies, to execute `python verify.py` in the directory containing the standalone script. Compare its output with `verification_output.txt`; a successful run ends in `VERIFY_OK`.

The code enumerates the hexad orbit from three explicit permutations and tests the five-design and seven-set coverage, the full group of order \(95\,040\), signed characters on each element and direct simplicial Lefschetz characters on all distinct cycle structures. It compares the result with the three indicated published character-table rows. The proof that the rank-six basis complex is shellable depends on the established Björner matroid-shellability theorem, not solely on enumeration. The representation decomposition is over the complex numbers. No separate integral direct-sum splitting or equivariant sphere-wedge equivalence is tested or claimed.
