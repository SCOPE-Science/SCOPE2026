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

The included `verify.cpp` was compiled with a C++17 compiler and run from this package directory. It uses exact \(\mathbb F_2\) bit-mask arithmetic, not floating-point calculations. The published \(p=5,q=2\) Massey representatives pass. The homeomorphic control \((L(19,2),L(19,9))\) yields \(19\) surviving candidates for each allowed scalar, while the published distinguishing controls \((L(7,1),L(7,2))\) and \((L(11,2),L(11,3))\) yield none.

For \(p=19\), the program checks all \(32\) normalized nonhomeomorphic pairs and both allowed scalar values for each pair. It enumerates every nonzero vector \(c\) in the \(18\)-dimensional algebra and checks all \(19^2\) ordered input pairs in the naturality condition. The exact output is preserved in `verification-output.txt`; the program exits with status zero only when the formula controls pass and all \(32\) target pairs have zero survivors.

This verifies the finite obstruction calculation and its stated scope. It does not provide an independent audit or extend the result to other prime orders.
