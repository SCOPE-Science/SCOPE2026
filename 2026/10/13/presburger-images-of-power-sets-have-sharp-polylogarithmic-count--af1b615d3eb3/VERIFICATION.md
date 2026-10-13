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

The proof has two logically separate checks.

1. **Quantitative induction.** For a fixed \(n\)-term power sum, Schulz's \(S_2\) calculation gives directly
   \[
   |\pi(S_2)\cap[-H,H]|\le O(1)+(5n^2\log_2(bH))^n.
   \]
   On every one of the finitely many \(S_1\) subspaces, equations (2)--(5) of Lemma 3.2 rewrite the same output \(c\) as a fixed rational linear combination of at most \(n-1\) powers. Thus a quantitative induction hypothesis gives \(O((1+\log H)^{n-1})\) there. Finite union closes the induction.

2. **Presburger reduction.** Schulz's proof of Theorem B invokes Presburger cell decomposition to partition a definable function into finitely many rational affine pieces. Choosing one of finitely many bases for each input coordinate reduces every image piece to the preceding power-sum case with at most \(M\) terms.

3. **Sharpness.** If \(B>M\), the sum of \(M\) powers of \(B\) has base-\(B\) digits equal to exponent multiplicities, so no carry occurs. Restricting exponents to \(0,\ldots,L\) therefore yields exactly \(\binom{L+M}{M}\) distinct sums, all at most \(MB^L\).

The bundled exact replay tests this last combinatorial identity for \(1\le M\le7\) and \(0\le L\le8\) and reports:

`VERIFY_OK 126 exact assertions`

The computational replay is a sanity check for sharpness; the upper bound is source-backed and proved symbolically above. No independent audit has been performed.
