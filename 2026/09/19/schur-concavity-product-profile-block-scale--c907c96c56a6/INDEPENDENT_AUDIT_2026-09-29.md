# Independent audit — 2026-09-30

Record: `2026/09/19/schur-concavity-product-profile-block-scale--c907c96c56a6`  
Assigned and audited source tree: `399ba790ebeb4e00183f74f1994e61807bd952d4`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `a76703f6ff9d089971ff15d44fc88212d0e81de9`  
Disposition: **passed**

## Correctness

**independently_supported**. The majorization and envelope argument is correct. At fixed x+y, terms containing both variables increase with sqrt(xy), while each pair of terms containing exactly one has squared bracket R(x+y)+2xy+2sqrt(xy(R^2+R(x+y)+xy)), strictly increasing in xy; Robin-Hood transfers therefore strictly increase W_d and prove strict Schur concavity. Genuine block splitting is also strictly improving, so the integer maximum with at most q blocks is the balanced q-block partition, and grouping subsets by how many size-(m+1) blocks they contain yields the displayed exact envelope. Cauchy–Schwarz gives W_d^2<=binom(q,d-1) d e_d, Maclaurin gives the sharp continuous envelope, and applying Maclaurin from e_2 to e_d with e_2=(n^2-sum b_i^2)/2 yields exactly the stated global variance-stability factor. The d=2 and q=d boundary cases remain strict for unequal positive blocks.

## Originality

**qualified_recent_refinement**. Abakumov–Friedland–Yomdin introduced the product-profile scale only in September 2026, explicitly evaluate equal d-block profiles, and prove the coarse at-most-q scale q^{(d-1)/2}n^{d/2}. The inspected source description does not give the exact optimization for q>d, majorization theorem, elementary-symmetric compression, or quantitative stability. Searches did not locate an equivalent statement. The contribution is therefore supported as an exact extremal analysis of a very new structural invariant, with high concurrency risk and no claim to novelty for classical majorization or Maclaurin inequalities.

## Scientific value

**meaningful_exact_extremal_refinement**. The record upgrades the source's block-count estimate to an exact integer envelope, proves uniqueness of the balanced optimizer, and quantifies how near-optimal scale forces near-balanced blocks. This is useful for every source theorem using w_d, although it does not prove that the resulting q-dependence is information-theoretically optimal for the actual concentration function.

## Literature and evidence checked

- https://arxiv.org/abs/2609.19473
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/schur-concavity-product-profile-block-scale--c907c96c56a6

## Limitations

- The theorem optimizes the source's structural scale w_d, not the true concentration function over all polynomials with at most q blocks.
- The broader optimal dimensional exponent problem for arbitrary multi-affine polynomials remains open.
- The d=1 case is excluded because W_1 is partition-independent.
- The source invariant is extremely recent, so unindexed contemporaneous refinements are a substantial priority risk.
