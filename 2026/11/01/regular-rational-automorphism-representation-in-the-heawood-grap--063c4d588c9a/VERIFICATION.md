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

# Verification of the Heawood magnitude regular-character theorem

Run `python3 verify_fano_magnitude_regular.py` with Python 3.10 or later, using only the standard library. The expected terminal marker is `FANO_MAGNITUDE_REGULAR_CHARACTER_OK`; the complete recorded output is in `verify_fano_magnitude_regular.out`.

The program enumerates seven points, seven lines, 21 edges, all 14×14 shortest-path distances and the length-four chain bases. It checks chain sizes (840, 2268, 1134), signs and boundary composition, the 42 distinct zero four-boundary columns, disjoint primitive supports and binary rank 840 of the three-boundary. The integral-surjectivity proof in `RESULT.md` establishes the needed stronger integral statement; mod-two rank by itself is not an integral certificate. The checker enumerates 168 invertible binary matrices and 168 correlations and verifies the identity trace 336 and zero for the other 335 group elements. Summary counts of every tested fixed-chain class are recorded in the output file.

The finite exhaustive computation is a direct check of this graph only. The proof gives the mathematical bridge from the finite boundary matrices to the rational module using group-character semisimplicity. No integral regular-lattice equivalence or independent external certification is asserted.
