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

The proof is a twelve-state deterministic finite automaton obtained by subset determinization of the binary-triple transducer for path-neighborhood modal truth values. An explicit vector of twelve generating-function numerators satisfies all exact integer-polynomial transfer equations, proving the rational generating function for every word length.

Run `python verify.py` in the same directory. It constructs the transducer independently of the displayed transition constants; checks the complete transition table and accepting vector; verifies the twelve polynomial identities; and directly enumerates the distinct approximation pairs for path sizes 1 through 15. Expected output starts with `VERIFY_OK` and contains the exact counts 1, 2, 3, 7, 13, 23, 43, 79, 145, 267, 491, 903, 1661, 3055, 5619, 10335 (including the auxiliary size-zero convention).

The enumeration is finite corroboration only; the transfer certificate gives the infinite proof. No assertion is made about arbitrary tolerance graphs or about multiplicities of preimages. Independent external review or certification has not been performed.
