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

The exact verifier implements the divisor formula with integer arithmetic and checks it in three independent ways.

First, for small \(q\) and \(n\), it directly enumerates the source alphabet, decomposes all words into cyclic rotation orbits, determines each least period and product weight in \(\mathbb F_p^\times\), and compares the resulting weighted orbit sum with the divisor formula.

Second, it evaluates the formula at every one of the forty \((q,n)\) entries displayed in the motivating paper's rank table and checks exact equality.

Third, for eight prime powers \(q\), it verifies four successive \(p\)-power lengths against the published corollary
\[
r_{q,n}=\frac{(q-q/p)^n}{p-1}.
\]

The replay output is stored in `verification_output.txt`. These finite checks corroborate implementation and normalization only. The theorem for all \(n\) rests on the character-orthogonality and Möbius-inversion proof in `RESULT.md`; the underlying Carlitz \(L\)-function orbit theorem is a cited premise rather than something re-certified by the verifier.
