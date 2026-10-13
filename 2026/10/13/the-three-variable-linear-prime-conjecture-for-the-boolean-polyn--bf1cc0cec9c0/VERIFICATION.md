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
The replay is `verify.py`, with certificate data in `witnesses.json`.

It reconstructs all \(15\) nonzero linear supports in \(\mathbb B[x,y,z]\), enumerates all \(32768\) generating subsets, recomputes \(1748\) distinct linear closures, isolates the \(1721\) non-variable-generated proper closures that omit at least one variable, and verifies one explicit factor witness for every such closure.

The exact membership predicate used by the replay is justified in `RESULT.md`: a support \(F\) belongs to a linear-generated ideal exactly when every monomial of \(F\) lies in a monomial shift of some generator whose whole shifted support remains inside \(F\). This is an equivalence because Boolean addition is union and has no cancellation.

The recorded replay output ends with `CHECK_OK`. The largest factor degree in the certificate is \(3\), and the largest product degree is \(6\).

The computation does not test primeness only up to a degree cutoff. It exhausts all possible linear generating sets and supplies a concrete finite non-primality witness for every negative closure class. The prime variable-generated cases are proved symbolically.

Independent audit has not been performed.
