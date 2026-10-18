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

# Reproduction procedure

The program `enumerate_cayley.py` requires Python 3 and NetworkX and generates `cayley_certificates.json`. Its output covers all inverse-closed connection sets of every finite abelian group of order less than sixteen. An automorphism permutation for every cell member is included.

The program `check_certificates.py` requires only the Python standard library. It recomputes inversion orbits, enumerates all connection sets, evaluates counting colour refinement, and validates each supplied permutation using every ordered vertex pair. Successful reproduction prints `PASS 821 exhaustive cases 4936 checked root-fixing automorphisms` followed by counts by group order.

The independent `check_exception16.py` constructs the classical sixteen-vertex Cayley graph and verifies the adjacency matrix, degree, common-neighbour counts, rooted colour partition, and a finer rooted-automorphism invariant. Its output starts with `PASS:`. No published paper is embedded; references are bibliographic only.

The enumeration is a finite exhaustive classification, and completeness depends on the finite abelian group classification and the elementary inverse-closure fact proved in the main text. Program output without its checked source and certificate does not itself establish the theorem. Verification here is reproducibility checking and self-review, not independent scientific audit.
