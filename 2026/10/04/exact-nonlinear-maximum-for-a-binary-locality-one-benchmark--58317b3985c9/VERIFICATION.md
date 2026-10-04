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

Run `python3 verify.py` with a standard Python 3 interpreter.

The script performs two independent finite checks. First, it constructs the eight-word code
\[
\{(a,a,b,b,c,c,d,d,d):c=a+b\}
\]
and verifies cardinality \(8\), global minimum distance \(3\), and for every coordinate the existence of a one-helper recovery view whose two-coordinate projection has minimum distance \(2\).

Second, after the proved reduction to coordinate equivalence classes, it enumerates every integer partition of \(9\) into parts at least \(2\). For each partition it enumerates every subset of the corresponding binary quotient cube and computes the largest subset with weighted minimum distance at least \(3\). The exact maxima are printed, with overall maximum \(8\), followed by `VERIFY_OK`.

The exhaustive search is finite because at most four equivalence classes are possible, so the largest quotient has only \(16\) vertices and only \(2^{16}\) subsets. The script does not use its finite enumeration to justify the infinite/logical reduction from locality to equivalence classes; that reduction is proved in `RESULT.md`.
