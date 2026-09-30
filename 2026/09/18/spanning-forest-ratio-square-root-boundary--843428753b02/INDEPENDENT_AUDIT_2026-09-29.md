# Independent audit — 2026-09-29

Record: `2026/09/18/spanning-forest-ratio-square-root-boundary--843428753b02`  
Assigned and audited source tree: `e12bf909c65d149b049da537d9fea23fc66e1005`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `35831ab2d9c56c3e5c11eb1cc5971517f0385cf3`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The extension-deficit proof checks. For a k-edge forest H in K_n, exactly q(H)=sum_C binom(|E(C)|,2) unchosen edges are internally blocked, yielding the exact consecutive-level identity. For a noncomplete G, the crude extension bound reduces the comparison to bar q_k<1. The line-graph path overcount and cycle union bound have the correct directions; under n>=3k^2 they give E Q<3/4 and forest probability >9/10, hence bar q_k<5/6. I independently checked the product inequality used in the cycle bound throughout the stated range. For k=3, direct enumeration independently reproduces bar q_3=12(n+4)/(n^2+3n+4), and independently recomputes all six n=5,6 two-missing-edge entries in the record's table.

## Originality

**qualified_recent_conjecture_progress**. Bencs--Csikvari's 16 September 2026 preprint proves the total forest/tree ratio inequality and poses the stronger consecutive-level problem. Current searches did not locate the square-root-width boundary theorem or the all-order k=3 resolution in later public work. The result is therefore supported as nonconstant progress on that very recent conjecture, with a correspondingly high risk of concurrent unindexed work.

## Scientific value

**meaningful_growing_range**. The theorem proves a growing O(sqrt(n)) band of consecutive forest-ratio cases rather than finitely many small ranks, and settles the first rank where four-edge cycle effects enter for every admissible n. The constant 3 is only sufficient, and the central/deeper ranks remain open.

## Literature and evidence checked

- https://arxiv.org/abs/2609.18611
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/spanning-forest-ratio-square-root-boundary--843428753b02
## Limitations

- The argument does not reach k larger than a constant multiple of sqrt(n).
- The numerical constant 3 is not optimized.
- The normalized-matching/LYM conjecture itself is not proved.
- The motivating conjecture was posted only days before the record, so concurrency risk is substantial.
