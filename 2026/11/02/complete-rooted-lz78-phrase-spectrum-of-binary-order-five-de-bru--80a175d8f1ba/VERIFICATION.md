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

Run `python3 verify.py` alongside this document. The verifier exhausts all \(2^{16}\) five-bit shift-permutation feedback functions, retains the single \(32\)-cycle maps, independently enumerates rooted directed Euler tours, and compares the resulting \(2048\) canonical words. It then agrees two independent LZ78 parsing implementations at all \(65536\) rooted words and asserts every displayed histogram.

The standalone verifier was executed successfully and printed `VERIFY_OK`. Its table of exact outcomes is reproducible from the code and does not require external inputs, unpublished software, or a random seed. The proof of completeness is the feedback-function bijection and the Euler-tour bijection, not an extrapolation from experiments. The result has not received independent mathematical auditing. Earlier publications may contain an unindexed equivalent enumeration; historical priority is not certified.
