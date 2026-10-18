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

# Verification of the circular-ladder double total domination enumerator

Run `python3 verification/verify.py` with the standard Python 3 library and no external packages. The committed output is `verification/output.txt`.

The verifier independently constructs every prism open neighborhood and tests the original double total domination condition by exhaustive enumeration for \(3\le n\le9\). This includes exactly \(349{,}440\) binary subsets over the seven tested graph orders. It next performs full backtracking enumeration of common-neighbor-independent subsets for \(3\le n\le13\), which is a separate finite method from the direct domination checker. Next it directly compares each common-neighbor conflict edge set against the square of the parity-twisted auxiliary graph for \(3\le n\le100\), including component lengths. Finally it checks analytic maximum sizes and six-residue coefficients through \(n=400\).

These finite checks do not establish the infinite family. The mathematical proof proceeds by a general bijection, exact auxiliary graph identification and a cyclic gap composition count, valid for every \(n\ge3\). This is scientific corroboration without any independent audit or external certification.
