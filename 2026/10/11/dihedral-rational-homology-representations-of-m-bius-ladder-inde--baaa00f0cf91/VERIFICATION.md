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

# Reproducible mathematical checks

Use Python 3.10 or later; no external packages are required. From a directory containing the included program, run `python verify_dihedral.py --extended`. The script constructs modular graph adjacency, enumerates independent faces and exact orientation signs for fixed faces, and separately constructs orbit-conflict graphs and their signed independence polynomials. The direct and orbit methods verify all 308 dihedral elements for \(2\le n\le12\). It independently reduces mod-two boundary matrices for \(2\le n\le9\) and obtains the degree and rank stated in the theorem. The optional extended check treats all 1,548 additional elements for \(13\le n\le30\) by orbit counts. Successful actual execution displayed `VERIFY_OK` and `EXTENDED_ORBIT_OK`. The implementation uses integer-only arithmetic.

These tests are finite and neither establish the infinite-family statement alone nor certify integral homology, equivariant homotopy, or homology at arbitrary primes. The all-width argument uses explicit transfer matrices, a fixed-simplex Lefschetz formula, and published nonequivariant concentration. A separate independent audit has not been performed.
