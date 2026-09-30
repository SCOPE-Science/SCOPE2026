# Independent audit — 2026-09-29

Record: `2026/09/14/003`  
Audited source tree: `a8d7c8ee4f4bd724421342c4005184b9fab136a3`  
Disposition: **passed**

## Correctness

The graph and symbolic-power calculations reproduce exactly. M8 has eight maximal independent sets, hence eight minimal vertex covers, each of size five; every vertex occurs in five covers. Summing the eight cover inequalities gives 5 deg(a)>=8m, while the diagonal vector k(1,...,1) lies in I^(5k) with degree 8k, proving the Waldschmidt constant 8/5. Independent exhaustive enumeration of the box {0,...,4}^8 gives 358134 vectors satisfying the I^(4) cover inequalities. The 364 multisets of three edges yield 316 distinct load vectors, and every one of those 358134 symbolic vectors dominates a three-edge load, proving I^(4) subset I^3. The stated initial-degree witnesses and the lower bound rho(I)>=5/4 are also correct; equality of resurgence and asymptotic resurgence remains explicitly conjectural.

## Originality

Recent literature studies ordinary and symbolic powers of cubic circulant edge ideals, including this graph family, but the closest accessible source does not state the audited Waldschmidt/containment census. The exact M8 invariant package is therefore a useful special-case computation, with no priority claim inferred from the search.

## Scientific value

The record provides an exact Waldschmidt constant, low symbolic initial degrees, and a finite exhaustive containment certificate for a canonical non-bipartite cubic graph. It is a strong benchmark computation, though it stops short of the full resurgence theorem requested by the original target.

## Limitations

- The exact equalities rho(I)=rho_a(I)=5/4 are not proved and remain conjectural in the record.
- The containment I^(4) subset I^3 is certified by exhaustive finite enumeration rather than a short structural proof.
- RESULT.md and METADATA.json refer to output/artifacts/*.py, while the audited scripts are stored under artifacts/*.py; this packaging path mismatch does not change the verified counts.
- The closest literature comparison does not establish priority or novelty for these exact M8 values.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/003
- https://arxiv.org/abs/2409.20161
- https://arxiv.org/abs/1805.03428
- https://arxiv.org/abs/2203.01268
