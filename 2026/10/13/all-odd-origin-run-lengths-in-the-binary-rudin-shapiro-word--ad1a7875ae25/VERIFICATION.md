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

# Verification instructions and limitations

The entire mathematical assertion is proved symbolically in `RESULT.md`. The standalone Python 3 script `verify.py` verifies finite consequences using direct binary-digit counting, independently of the key concatenation formula. It has no third-party dependencies.

Run `python3 verify.py` in the directory containing `verify.py`. Its observed output was:

`VERIFY_OK double_checks=20001 concatenation_checks=16382 constructed_odd_k=200 small_d=1024 second_witness_k=25`

The script checks \(r(2n)=r(n)\) for 20,001 inputs; the exact concatenation identity for 16,382 input-width pairs; the explicit first-change construction for all 200 positive odd lengths through 399; first-change parity for 1,024 differences; and further distinct witnesses for 25 prescribed lengths. None of these finite checks is an exhaustive test of the infinite theorem. The proof of the binary duplication identity, multiplier inequalities, complete absence of even indices, and bound \(d<32k^3\) must be read as the infinite certificate.

All source dates and comparisons are documented in the accompanying proof and review. No independent audit or independent validation has been performed.
