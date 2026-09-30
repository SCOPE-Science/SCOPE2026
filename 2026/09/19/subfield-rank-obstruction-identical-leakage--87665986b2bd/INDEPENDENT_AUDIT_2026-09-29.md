# Independent Audit — 2026-09-30

**Record:** `2026/09/19/subfield-rank-obstruction-identical-leakage--87665986b2bd`  
**Title:** Subfield-rank obstruction for identical leakage under linear computations  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `77a9c500e36791748ded7c1b31bd103cdd038531`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. Restricting the product-code attack to inputs (u_1 c,...,u_K c) for a fixed nonzero computation-code word a=uG is legitimate because the base code is F-linear. If the coordinates of a have B-span basis alpha_1,...,alpha_r, every identical leakage g_j(a_i c_j) is a B-linear combination of the r base-share leakages g_j(alpha_l c_j). A product decoder therefore gives a base repair using at most r B-symbols per share. For the systematic one-output code, a rank-one codeword is equivalent exactly to a nontrivial B-relation sum b_i mu_i in B, i.e. dependence of the classes mu_i+B in F/B; if independent, a generator row has rank two, so the minimum is exactly two. The K≥m and quadratic-extension corollaries follow from dim_B(F/B)=m-1. The supplied exhaustive verifier matches the criterion in all listed small binary extensions.
- **Originality — PASS:** PASS, while recognizing its close relationship to the companion column-rank record. Aoutouf–Augot publicly establish the computation-code leakage framework and report identical-leakage behavior, but the accessible source description does not state a minimum rank-weight obstruction or the quotient-space classification for a systematic single output. Standard rank-weight notions and older secure-network-coding leakage results are prior art. This record adds a different invariant from the companion column-rank law: the minimum B-rank of a codeword controls restrictions to one-dimensional input families, whereas the companion record measures the full local transcript rank of the generator columns.
- **Scientific value — PASS:** PASS. The obstruction supplies a sharp necessary test for whether computation can create a genuinely new one-subsymbol attack, completely resolves the systematic single-output rank-one question, and explains the otherwise counterintuitive quadratic-extension collapse. It is complementary rather than redundant with the companion exact local column-rank law.

## Independent findings
- The restriction argument needs only one nonzero component of u to recover c_0 after the product decoder returns the K input secrets.
- For K≥m, dependence in the (m-1)-dimensional quotient F/B forces minimum rank one for every single-output coefficient vector.
- For two inputs over a quadratic extension, all coefficient pairs are quotient-dependent, so no genuine one-subsymbol gain can be certified through this model.
- The exhaustive verifier reports all 16 quadratic two-input tuples dependent and matches the rank criterion in the m=3 and m=4 test families.

## Independent checks
- Re-derived the one-dimensional restriction/repair reduction.
- Proved the quotient-space criterion directly in both directions.
- Checked the dimension and LFSR corollaries.
- Inspected the repository exhaustive verification script and recorded output.

## Literature evidence
- https://arxiv.org/abs/2609.19929 — Aoutouf–Augot motivating computation-code and identical-leakage framework.
- https://wcc2026.inria.fr/ — Earlier subfield-subcode LERS context.
- https://arxiv.org/abs/1509.04764 — Guruswami–Wootters exact repair background.
- https://arxiv.org/abs/1301.5482 — Relative generalized rank weights and information leakage in network coding; different model.

## Limitations
- The rank condition is necessary, not sufficient, when the minimum rank exceeds one.
- The theorem covers linear leakage and linear computations over finite fields only.
- The result is close in spirit to the companion exact local column-rank law but controls a different object (minimum codeword rank); near-simultaneous priority risk is material because the motivating preprint is very recent.

The assigned source-tree SHA still matches the current record tree inspected on `main`. GitHub was used only as read-only evidence; no repository writes were made.
