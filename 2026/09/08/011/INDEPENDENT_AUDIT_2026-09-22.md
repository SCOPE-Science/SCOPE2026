# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `f9bf099ac572e01adfe11ccbe2da5419a9b9660f`, verified unchanged on current `main`.

## Correctness

I wrote a fresh include/exclude search for intersecting 3-uniform families after the standard WLOG normalization `{0,1,2} in F`. Disjoint-pair propagation is independent of the committed solver. For every `n=9,...,13`, the search proves UNSAT for diversity target `gamma >= n-2`; node counts were `13093,26447,48753,83559,135841`. A separate two-target implementation proves UNSAT for a non-star family with both `delta >= 4` and at least one edge missing each vertex; node counts were `7825,20391,46439,89885,171835`. The triangle family has `|T_n|=3n-8`, maximum degree `2n-5`, diversity `n-3`, and minimum degree 3. Thus the independent computations establish exactly `D(n)=n-3` and `d(n)=3` throughout the stated window.

## Originality

I searched the intersecting-family diversity and minimum-degree literature under diversity, covering number, degree stability, triangle/two-out-of-three family, and `k=3,n=9..13`. Kupavskii and Frankl–Wang establish large-`n` diversity results/conjectures, while Pátkós studies a broader asymptotic degree/diversity program. I found no source giving this exact five-value small-window diversity table together with the exact non-star minimum-degree threshold. The record also avoids claiming uniqueness of extremal type.

## Scientific value

These exact small-parameter thresholds close a concrete finite window immediately above the classical small configurations and test the transition between Hilton–Milner/triangle-style competitors and large-`n` stability theory. Both quantities are pinned by exhaustive certificates and a simple extremal family, making the result useful as benchmark data for future general statements.

## Disposition

**PASSED unchanged.**
