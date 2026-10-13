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

The proof in `RESULT.md` is universal and does not infer an infinite claim from computation.

The attached checker factors every integer
\[
4\le n\le2{,}000{,}000,
\]
retains composite integers with \(\omega(n)\le2\), computes \(\beta(n)\) exactly from the prime-power formula, and tests
\[
\beta(n)\mid n-1.
\]
It tests \(554175\) low-support composites and finds exactly
\[
\{4\}.
\]

The checker separately verifies, over thousands of prime powers, the inequalities
\[
0<\beta(p^a)<p^a
\]
and
\[
\beta(p^a)\ge p^{a-1}(p-1),
\]
including the equality condition and parity facts used in the proof.

The unbounded theorem rests on the symbolic congruence, ratio, parity, and exhaustive factorization arguments in `RESULT.md`; the finite replay is corroborative only.
