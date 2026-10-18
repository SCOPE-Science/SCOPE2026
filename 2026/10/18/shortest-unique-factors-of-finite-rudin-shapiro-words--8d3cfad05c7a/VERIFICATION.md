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

# Verification

The accompanying `rs_unique_check.py` is a standalone Python 3 program with no third-party dependencies. Run `python3 rs_unique_check.py`. Its output is preserved in `rs_unique_output.txt`. The program checks each finite frequency table through dyadic order 12, all 128 possible length-8 windows of paired aligned blocks, and all 104 length-14 windows permitted by parity-alternating block triples, which are each repeated at least six times within the first 1024 bits.

The general quantified theorem is established by mathematical induction using the proved decoding correspondence, not by extrapolating the finite checks. No external formal certification or independent audit is asserted.
