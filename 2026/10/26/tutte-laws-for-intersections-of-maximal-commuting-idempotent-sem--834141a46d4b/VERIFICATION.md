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
# Verification of the incidence-semigroup intersection theorem

Run `python3 verify.py` with the standard library. The checker constructs all incidence-algebra elements over small prime fields, checks the convolution multiplication directly, enumerates all idempotents and unipotent units, independently constructs maximal commuting idempotent subsets, and compares the sizes of their intersections with independent spanning-subgraph counts. For sufficiently small idempotent sets it additionally performs exhaustive Bron–Kerbosch maximal-clique enumeration. The program prints `VERIFY_OK` exactly when all assertions pass.

Verified configurations: a two-point chain over \(\mathbb F_2\) and \(\mathbb F_3\); a three-point V and a three-point chain over \(\mathbb F_2\); and a four-point complete height-two poset and four-point diamond over \(\mathbb F_2\). The corresponding numbers of maximal semilattices are \(2,3,4,8,16,32\). Calculations are exhaustive only for the stated small instances. General maximality, the all-poset histogram, polynomial reconstruction, and the limit law require the proofs in `RESULT.md`.
