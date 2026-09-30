# Independent audit — 2026-09-28

Record: `2026/09/10/044`  
Audited tree: `26d3e48d4e6c9badf0e6328f2141344b9fa92123`  
Disposition: **repaired**

## Correctness
The finite enumeration itself is correct: a fresh independent implementation reproduced the standard ASM/DSASM/OSASM totals through order 5 and the order-5 distribution `3,7,9,9,4`. The original prose, however, mixed two incompatible definitions. It defined palindromicity by `c_k=c_(d-k)` with `d` the true degree, yet called `t+2t^2+t^3` palindromic only after the reciprocal shift `4`. Under the written degree-based definition that order-3 polynomial is not palindromic because its constant coefficient is zero.

The repair uses the normalization actually compatible with the known even-order theorem: `P(t)` is reciprocal up to monomial shift when `P(t)=t^m P(1/t)`. For finite support `[a,b]`, `m=a+b` is forced. Order 3 has support `[1,3]` and shift `4`, so it is reciprocal. Order 5 has support `[1,5]`, forcing shift `6`, but `c1=3 != c5=4` (and `c2=7 != c4=9`), so it is not reciprocal under any shift. Thus the core counterexample survives, but the statement and certificate need the coordinated repair supplied in this plan.

## Originality
The closest sources I located are BFK and Kumari: they provide refined DSASM machinery, the even-order OSASM symmetry, and the odd-order unrefined product. I did not locate the order-5 refined row or its odd reciprocal-symmetry failure. This supports the specific finite contribution, not an exhaustive novelty claim.

## Scientific value
The repaired result is a precise obstruction to a natural odd analogue of the even reciprocal identity, with an exact, independently reproduced counterexample.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/044
- https://arxiv.org/abs/2309.08446
- https://arxiv.org/abs/2503.18685
- https://arxiv.org/abs/math/0008184
