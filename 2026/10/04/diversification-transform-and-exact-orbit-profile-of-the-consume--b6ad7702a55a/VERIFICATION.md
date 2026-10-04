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

The bundled `verify.py` uses only the Python standard library.

For each \(n\leq6\), it explicitly constructs every labeled consumer-product structure: it chooses the product subset, lists every permutation of that subset as a possible consumer preference order, and enumerates every independent tuple of such preference orders for the consumers. The number of distinct encodings is compared with
\[
\sum_{p=0}^n {n\choose p}(p!)^{n-p}.
\]
The resulting injective counts are
\[
1,2,4,11,54,567,13928
\]
for \(n=0,\ldots,6\), and the formula is separately evaluated through \(n=8\), giving \(837321\) and \(134985098\) at the next two arities.

The script also checks the general transform on the empty-signature base class, where \(f_p=1\) and the diversification is just a two-sorted set, so the expected injective profile is \(2^n\). Finally it computes Stirling numbers recursively and verifies the repeated-coordinate profile through arity seven.

The program ends with `VERIFY_OK`. The finite replay checks the combinatorial encoding and the displayed values; the all-arity theorem is supplied by the symbolic proof in `RESULT.md`. No independent audit has been performed.
