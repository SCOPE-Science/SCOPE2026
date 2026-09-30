# Independent audit — Exact constants and concentration centers for block-product anti-concentration

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/exact-block-product-small-ball-constants--cf3421945354`  
**Assigned and audited tree:** `97d501b57c9e93d47f3880a131a39a6a629f763d`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review.

## Correctness

PASS. The block factor is exactly the average of m iid Uniform[-1,1] variables. Each factor density is even and unimodal, and the product-density integral preserves monotonicity on (0,infinity), so the all-center concentration maximum is indeed at zero. Under T_m=-log|A_m|, q_m(u)=e^{-u}H_m(e^{-u}); convolution gives the stated polynomial-in-u asymptotics. Expanding the incomplete-gamma tail at x=log(1/s)+log M yields the coefficient 1+log M+sum delta_m in the second logarithmic term. The density singularity and L^p constant follow from the same convolution and Stirling asymptotics. The m1=m2=2 check was independently integrated and exactly reproduces epsilon[5epsilon-2(epsilon+2)log epsilon-4]. The large-m correction -3/(20m) follows from log(sin x/x)=-x^2/6-x^4/180+... and the Gaussian fourth moment.

## Originality

PASS on the stated refinement boundary. Abakumov–Friedland–Yomdin (2026) explicitly establish the product profile and full block-size scaling only up to constants depending on degree, with matching p-growth up to constants on block-product models. The assigned record supplies exact central Bates-density coefficients, the exact concentration center, a second logarithmic term, and an exact high-p limiting constant. The September 19 SCOPE record on Schur concavity optimizes the structural block scale w_d across partitions; it does not derive these distributional constants. Classical Irwin–Hall/Bates and Mellin-product formulas are prior art, so novelty is only their sharp synthesis for these new extremizers.

## Scientific value

PASS. Replacing degree-only comparability by explicit block-size-dependent constants, identifying the next logarithmic term, and tying the same coefficient to both small-ball and high-p density asymptotics materially sharpens the extremizer analysis in the motivating preprint. The result is focused but quantitatively informative.

## Independent checks

- Re-derived the logarithmic-convolution asymptotics and the origin of the 1+log M+sum(delta_m) coefficient.
- Integrated the (m1,m2)=(2,2) case independently and obtained the exact formula printed in the record.
- Checked the Edgeworth/Laplace first correction beta_m=sqrt(6/pi)(1-3/(20m)+O(m^-2)).
- Compared with the source preprint abstract, which claims optimality only up to degree-dependent constants, and with the September 19 SCOPE Schur-concavity record, which addresses a distinct block-scale optimization question.

## Literature and evidence

- https://arxiv.org/abs/2609.19473 — Abakumov, Friedland and Yomdin (2026): motivating product-profile theorem; block-product sharpness and density growth are stated up to degree-dependent constants.
- https://doi.org/10.1137/0118065 — Springer and Thompson (1970), classical distributions of products of random variables.
- https://doi.org/10.1155/2017/3571419 — Marengo, Farnsworth and Stefanic (2017), Irwin–Hall distribution background.

## Limitations

- The exact constants concern the canonical centered block-product models, not arbitrary multi-affine polynomials.
- The second-order expansion fixes the block sizes as s tends to zero; no uniform remainder over growing block sizes is proved.
- Older product-distribution literature is broad, so the originality conclusion is limited to the specific sharp synthesis and motivating extremizer setting.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `97d501b57c9e93d47f3880a131a39a6a629f763d`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
