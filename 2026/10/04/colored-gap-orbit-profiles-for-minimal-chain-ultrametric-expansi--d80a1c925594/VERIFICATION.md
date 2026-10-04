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

The bundled `verify.py` uses only the Python standard library. It independently constructs finite members of the chain minimal expansion as recursively ordered nested set partitions with singleton leaves.

Checks performed:

- every \(1\le d\le3\) and \(1\le n\le5\): the recursively generated structures have cardinality \(n!d^{n-1}\);
- every generated hierarchy encodes to a permutation plus a length-\(n-1\) word over \(\{1,\ldots,d\}\), decoding returns the original hierarchy, and the code set equals the full Cartesian product of all such permutations and words;
- every \(1\le d\le5\) and \(1\le n\le8\): the repeated-tuple Stirling transform satisfies \(d\,b_d(n)=\mathcal F_n(d)\);
- the displayed initial injective and all-tuple profiles are reproduced exactly.

The finite replay does not substitute for the general proof. The infinite statement follows from the explicit colored-gap bijection in `RESULT.md`; the verifier checks that the bijection and formulas behave exactly as claimed on nontrivial finite ranges. A successful replay ends with `VERIFY_OK`.
