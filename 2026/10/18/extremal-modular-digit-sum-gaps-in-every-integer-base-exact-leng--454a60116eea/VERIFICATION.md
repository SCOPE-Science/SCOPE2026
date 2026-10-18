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

# Reproducibility

The symbolic argument in `RESULT.md` proves the theorem for every integer base \(b\ge2\). Finite enumeration is not used in place of proof. The standalone `verify.py` file requires only Python 3 and the standard library. Run it with `python3 verify.py` in the extracted directory.

It compares every admissible interval of the claimed maximal length with the independently implemented classification for bases \(2\) through \(12\), totaling \(2,492,834\) starting points. It also rejects all intervals of one larger length in the same tested ranges, constructs maximal-length witnesses in bases \(2\) through \(30\), and checks their digit sums and endpoints. The expected final line begins with `PASS:`.

The limiting density proof is theoretical. The finite checks do not certify infinite equidistribution or completeness beyond their tested ranges. The mathematical assumptions and all normalization choices are given in `RESULT.md`.
