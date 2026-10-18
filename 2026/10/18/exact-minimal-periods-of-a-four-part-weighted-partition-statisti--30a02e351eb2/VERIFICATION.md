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

# Reproduction and boundaries

Execute `python3 verify.py` from this directory. The script uses only the Python standard library and prints `VERIFIED` after checking its assertions.

The exact symbolic check constructs the rational generating numerator by integer polynomial operations on the four slack-variable geometric sums, then confirms its reduction to the stated factored denominator. An independent enumeration of all four-part partitions of sizes zero through 74 checks the initial coefficients. The script checks periodicity and the absence of proper-divisor periods over two full candidate periods for moduli 5, 7, 11, 13, 17, 25, 35, 49, 77, and 125. The finite tests cannot establish the asserted universal periods; the proof uses cyclotomic coprimality, binomial valuation, and CRT. No external certificate or independent audit is asserted.
