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

The finding uses analytical conjugacy, graph incidence, and parity arguments for all dimensions. Run the standalone checker with `python3 verify.py`; it relies solely on the standard library.

The checker implemented the original XOR shift-register transition directly in binary arithmetic, not by importing the cyclic graph rank formula into the transition routine. For all \(1\le n\le80\), each injection site, and each time \(0\le t\le n+3\), it compared the computed binary span rank with the theorem: **186840 rank checks passed**. For \(n\le8\), from up to three starting states, it enumerated exact integer-multiplicity distributions of the random-bit strings and checked the support and equal masses: **1039 distribution checks passed**. It enumerated even binary necklaces for \(1\le g\le12\) and independently checked the Burnside formula: **12 class-count checks passed**.

Finite checks cannot establish an all-dimension theorem; the proof in `RESULT.md` establishes the infinite-range statement. Independent audit status is not performed.
