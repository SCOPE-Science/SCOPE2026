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

# Computational verification and limits

Run `python3 verify.py` in the folder containing this file. The script is standalone and uses only Python's standard library.

It exhaustively enumerates all \(3\times3\) matrices with trace \(1\) over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), checking the conditions \(\det B\ne0\) and \(\det(I_3-B)\ne0\) against the polynomial: respectively \(24\), \(1998\), \(30528\), \(224000\). It builds the full exterior multiplication table, calculates the linear derivation equations, verifies dimensions \(24\) for unrestricted derivations in characteristic two and \(15\) in odd characteristic, and tests \(180\) independently sampled radical-preserving derivations in each of characteristics \(2\), \(3\), \(5\) against all basis Leibniz identities and the radical-rank criterion. The characteristic-two radical-preserving subspace has dimension \(21\) because its generator images have zero scalar coefficients.

Passing output ends `EXTERIOR_RANK_CENSUS_OK`. Enumeration is exhaustive only for the stated finite leading-matrix fields; samples are not exhaustive for full derivation spaces. The proof in RESULT.md establishes the theorem for all finite fields. No independent mathematical audit has been performed.
