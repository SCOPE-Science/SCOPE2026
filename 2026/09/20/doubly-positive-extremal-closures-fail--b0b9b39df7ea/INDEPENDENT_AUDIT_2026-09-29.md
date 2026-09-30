# Independent audit — Product and convolution can destroy extremality in the doubly-positive cone

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/doubly-positive-extremal-closures-fail--b0b9b39df7ea`  
**Assigned and audited tree:** `6a1372bdc0412d0e2d5191b29d73038e5575e240`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The claim survives independent review without a substantive research-file edit.

## Correctness

PASS. The 2009 Jaming–Matolcsi–Révész source was inspected directly: Proposition 4.3 gives the degree-four ellipse and extremality on its boundary, Lemma 4.2 gives the required real-zero obstruction for nonconstant Hermite extremals, Corollary 4.4 records restricted positive closure results, and Question 1 asks the unrestricted product/convolution question. For a=(2-√6)/8, b=1/8 the ellipse expression is exactly 1/8. The spatial polynomial Q has discriminant 32(2-√6)<0 and positive leading coefficient, so F>0; Fourier sign-flip of the H2 coefficient gives R(X)=(X-(1+√6))^2 and H≥0. Since H has only two zeros, H*H is strictly positive everywhere, while F² is strictly positive; Lemma 4.2 therefore rules out extremality of F², and Fourier cone automorphism transfers the conclusion to H*H.

## Originality

PASS with a meaningful residual-risk note. The source paper explicitly asks the unrestricted closure question and proves only special type-restricted positive cases. Targeted searches of the citation chain and exact construction did not locate a published negative answer, and no obvious duplicate appears in the current SCOPE repository. Because the counterexample is a short combination of ingredients already present in the 2009 paper, an unpublished observation or poorly indexed remark remains a nontrivial priority risk.

## Scientific value

PASS. A concrete one-dimensional Schwartz/Hermite self-product and self-convolution counterexample answers an explicit structural question about extremal rays negatively, while also exposing a general mechanism from strict positivity of a nonconstant Hermite extremal or its Fourier transform.

## Independent checks

- Inspected the primary source's Lemma 4.2, Proposition 4.3, Corollary 4.4, and Question 1 in full text.
- Symbolically verified the chosen point lies exactly on the extremal ellipse and that disc(Q)=32(2-√6)<0.
- Symbolically verified the Fourier-side polynomial equals (X-(1+√6))^2 under the source's Hermite Fourier rule.
- Checked the convolution positivity argument: for fixed ξ the product H(η)H(ξ-η) vanishes only at finitely many η and is otherwise positive.
- Checked current main-path tree identity against the assignment snapshot.

## Literature and evidence

- https://arxiv.org/abs/0801.0941 — Jaming, Matolcsi and Révész, primary full text containing the extremal Hermite criteria and the open closure question.
- https://doi.org/10.1007/s00041-008-9057-6 — Published version of the primary 2009 extremal-rays paper.
- https://doi.org/10.1016/j.jco.2011.01.002 — Hinrichs and Vybíral (2011), later positive-positive-definite work; concerns different Bochner/matrix questions rather than extremal-ray closure.

## Limitations

- The counterexample disproves universal preservation but does not classify which pairs of extremals have extremal products or convolutions.
- The mechanism is presented in the one-dimensional Hermite class, which is sufficient for the universal question but not a dimension-free classification.
- Because the proof is short and source-local, unindexed or unpublished prior awareness remains a stronger originality caveat than usual.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `6a1372bdc0412d0e2d5191b29d73038e5575e240`. This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels remain byte-for-byte semantically identical to the pre-audit file.
