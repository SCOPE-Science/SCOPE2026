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

# Verification details

From a directory containing the two verification files, execute `python prism_parity_verify.py`. The program uses only Python's standard library and prints the exact terminating line `PRISM_PARITY_VERIFY_OK` if every assertion passes. `prism_parity_verify.out` is the recorded output from the packaged script executed in its delivered directory.

The finite enumeration covers every labelled configuration for cyclic lengths \(n=3,4,5,6,7,8\), totalling \(87{,}360\) states. Each is iterated to an exactly detected finite cycle; the resulting first-entry distributions and cycle lengths are compared with the formulas.

A separate implementation builds the binary linear map by applying the update to basis vectors. Its Gaussian-elimination ranks verify the expected kernel dimensions for selected even and odd multiples of three and reversible lengths, including the larger values \(n=9,10,12,15,18,24\). Finally, ranks of \(F^{2^j}-I\) and derived primitive-orbit counts are checked for powers-of-two rim sizes through \(n=128\).

The verifier enumerates finitely many instances and does not certify the infinite theorem on its own. The complete proof uses Chinese-remainder decomposition, the primary local Smith invariants, and the nilpotence of the cyclic adjacency polynomial at dyadic lengths. No external or independent audit has been performed.
