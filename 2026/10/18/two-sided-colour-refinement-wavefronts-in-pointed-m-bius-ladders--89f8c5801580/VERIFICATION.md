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
# Reproducible verification

From the same folder, execute `python verify_direct.py` and `python verify_quotient.py`. The first script uses a direct \(2m\)-vertex graph implementation and predicts/refutes equality of every pair of colour classes at every round for \(4\le m\le120\). The second separately implements the multiplicity-weighted reflection quotient for \(4\le m\le150\), and enumerates full graph automorphisms for \(4\le m\le10\). It requires the `networkx` Python package. Recorded outputs are in `direct_output.txt` and `quotient_output.txt`.

The checks are finite, not a proof of the universal integer quantifier. The proof in `RESULT.md` independently derives the quotient, establishes the round-three base case, proves the wavefront induction, and handles the finite boundary and automorphism arguments. No external or independent scientific audit has been performed.
