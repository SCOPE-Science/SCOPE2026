# Independent audit — 2026/09/09/032

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I used a separate Catalan-sized generation: starting with the empty permutation, insert the new maximum (n) at every position that creates no 123 pattern (the entries to its left must contain no increasing pair), or no 132 pattern (each left entry must exceed each right entry). This constructs all avoiders, since deleting the maximum reverses the step. I counted fixed points, excedances and descents directly for every object through (n=10). Every cell of the stored 123 trivariate tables for (n=0,ldots,10) agrees, as does every one of the 572 stored 123-versus-132 divergence entries. The (n=10) table has 39 cells and total 16,796; its descent marginal is (42,1770,7515,6455,1013,1) at descents 4–9. The (n=3) divergence witnesses also follow directly. This checks the joint census independently of the candidate's incremental pattern-pruning code. The claimed Dyck descent correspondence and general Eulerian generating function are established prior facts, not newly proved by the finite table.

## Originality — PASS, narrow

Elizalde's earlier work supplies partial single-pattern fixed-point/excedance results, while Barnabei–Bonetti–Silimbani supply the descent generating function for 123 avoiders. The exact ((fp,exc,des)) cross-tabulation through ten and the matched comparison with 132 are absent from the checked papers. The (n=8,9,10) Eulerian rows are consequences of the already published descent generating function and should not be presented as independent new mathematics. The result is a finite joint data set, with no all-(n) trivariate formula.

## Scientific value — PASS, bounded

The 39-cell (n=10) joint row and explicit earliest 123/132 divergence provide benchmarks for proposed refined bijections and generating functions. The value is as reproducible small-parameter data, not a resolution of the open general joint distribution.

## Sources

- Elizalde, *Multiple pattern avoidance with respect to fixed points and excedances*, arXiv:math/0311211: https://arxiv.org/abs/math/0311211
- Barnabei, Bonetti, Silimbani, *The descent statistic over 123-avoiding permutations*, arXiv:0910.0963: https://arxiv.org/abs/0910.0963
- Candidate `artifacts/tri_123_n10.json`, `artifacts/divergence_123_vs_132.json`; independent maximum-insertion replay described above.
