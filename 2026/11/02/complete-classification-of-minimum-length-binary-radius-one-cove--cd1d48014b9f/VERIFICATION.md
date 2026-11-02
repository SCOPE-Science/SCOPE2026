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

# Verification procedure and limits

`cover_census.c` is a deterministic complete enumeration in C11; it builds two 64-bit halves of each of the 128 Hamming-neighborhood masks and checks all binary indexed cycles at every length from 1 through 22. This directly certifies the zero counts through 21 and the 132 accepted cycles at 22. Its exact orbit canonicalization and weight histogram verify the group-action and forced-balance assertions.

`verify.py` independently recomputes the masks with arbitrary-precision integers, checks the complete census through length 22, computes all extended dihedral-complement orbits, and checks window distinctness and the target multiplicity histogram of every accepted cycle. It reads `optimal_cycles.txt` only as an optional inventory cross-check, never as a source of accepted candidates. `VERIFY_OK` denotes successful execution of these exact checks.

Run `gcc -O2 -std=c11 -Wall -Wextra -pedantic cover_census.c -o cover_census`, then `./cover_census`, then `python3 verify.py` in the extracted package directory. All three input files are enclosed. No external libraries, network access, stochastic computations, or solver certificates are needed. The reproducibility envelope contains the exact source bytes and their hashes.

The enumeration is finite, not an all-length theorem; historical priority and independent audit are not verified by these scripts.
