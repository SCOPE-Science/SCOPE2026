# Independent audit — Point-mass Walsh square-function correction

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/point-mass-walsh-square-function-correction--db30226ad0bb`  
**Audited tree:** `bd6ec5e58f662e779b1fd65fb258927d4e941001`

## Disposition

**PASSED.** Correctness, originality on the stated boundary, and scientific value all pass. The record may remain in the validated set.

## Correctness

**PASS.** The correction and exact profile are correct. For the point mass F_n=prod_j(1+x_j)/2 and distinct J, direct finite differences give D_J F_n=2^{-k}(prod_{j in J}x_j) prod_{i notin J}(1+x_i)/2. Hence at Hamming radius r the square function is 2^{-k} binom(n-r,k-r)^{1/2} for r<=k and zero otherwise, yielding the stated exact norm-ratio sum. Maximizing the power of n across r gives the three fixed-p regimes; at p=2 the binomial identity sum_r binom(n,r)binom(n-r,k-r)=2^k binom(n,k) gives the exact Hilbert formula. Re-expanding with p_n=2+lambda/log n gives the stated critical-window limit. A fresh brute-force computation over cubes n<=6 matched the closed formula to 1.8e-15. The source preprint itself is now directly readable in public arXiv HTML: Lemma 6.3 evaluates (D_J F_n)(x_J) as (-2)^k and deduces a 2^k lower bound, whereas the displayed Walsh expansion has the global 2^{-n} factor; the audited correction identifies exactly this normalization error.

## Originality

**PASS.** The assigned result does more than note a typo: it gives the exact pointwise Hamming-layer profile, exact finite-n L_p ratio, the p<2/p=2/p>2 asymptotic phase split, and the logarithmic critical window while showing that the exponent-optimality conclusion can still be recovered from the correctly normalized r=k layer. The public arXiv record remains v1 from 2026-09-08, and repository searches around the source identifier and Walsh square-function terminology found no earlier SCOPE record containing this correction/profile package. I found no public erratum or indexed correction predating the record.

## Scientific value

**PASS.** The correction removes a concrete false quantitative bound from a very recent higher-order sharpness argument while preserving the intended exponent-optimality conclusion by a valid route. The exact layer formula and critical-window asymptotics also clarify how the singleton test transitions at p=2, so the contribution is scientifically useful beyond merely flagging the normalization mistake.

## Independent checks

- Read arXiv:2609.09040v1 Section 6.3 in public HTML and verified that Lemma 6.3 explicitly writes (-2)^k and a 2^k point-mass lower bound.
- Re-derived D_J F_n directly from D_j=(I-flip_j)/2 and counted Hamming layers.
- Recomputed all fixed-p leading powers and constants, the exact p=2 identity, and the p=2+lambda/log n limit.
- Ran an independent brute-force cube calculation for n=2,...,6 and k<=3; the exact closed formula matched within 1.8e-15, and the n=2,k=1,p=3/2 case contradicts the source lower bound.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.09040 — Jiao–Luo–Zanin–Zhou, Sharp Fractional Riesz Estimates on the Hypercube, arXiv:2609.09040v1.
- https://rt.http3.lol/index.php?q=aHR0cHM6Ly9hcnhpdi5vcmcvaHRtbC8yNjA5LjA5MDQwdjE — Public HTML mirror used to inspect Section 6.3 directly; Lemma 6.3 lines display the erroneous (-2)^k normalization and resulting 2^k lower bound.

## Limitations

- This audit corrects the singleton sharpness test; it does not re-audit every argument in the source paper.
- The source is a very recent v1 preprint, so a future revision could independently repair the same normalization issue.

## Repository identity

The assigned source-tree SHA `bd6ec5e58f662e779b1fd65fb258927d4e941001` matched the current tree at the audited path after comparison at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`, source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`, and current `main`. GitHub was read only during this audit.
