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

# Reproduction and limits

Execute `python3 verify_oddprime_pair.py` with Python 3 and no third-party packages. The checker compares coefficient dictionaries obtained by symbolic convolution of the formula with independently enumerated cyclic zero-zero pairs over every affine codeword. It checks all \(p\in\{3,5,7\}\) with dimensions \(1\le m\le6,3,3\), respectively, and binary \(p=2\) through dimension five as an external contrast. It also asserts total codeword count, maximal proper zero-pair count, and the top multiplicity, and terminates with `VERIFY_OK` on success.

All computations are exact integers. The polynomial identity, support recurrence, and multiplicities for all dimensions and odd primes are established by the mathematical proof in `RESULT.md`; successful finite checks alone would not prove this infinite claim. No independent audit has been performed.
