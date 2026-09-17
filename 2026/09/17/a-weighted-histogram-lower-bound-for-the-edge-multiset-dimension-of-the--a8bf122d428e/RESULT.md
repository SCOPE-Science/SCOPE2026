# A weighted-histogram lower bound for the edge multiset dimension of the 6-cube

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult `REVIEW.md` for limitations. Publication is not peer review or a guarantee of priority.

## Claim

Let `Q_6` be the 6-dimensional hypercube and `edim_m(Q_6)` its edge multiset dimension. Then

`edim_m(Q_6) >= 8`.

Combined with the explicit 15-landmark certificate in Allikvere's August 2026 preprint, the source report reports the bracket

`8 <= edim_m(Q_6) <= 15`.

## Definitions

For an edge `e=uv` and a vertex `s`, let

`d(e,s)=min(d(u,s),d(v,s))`.

For a landmark set `S`, define the edge histogram

`H_e^S(r)=|{s in S : d(e,s)=r}|`, for `r=0,...,5`.

The set `S` is edge-multiset resolving when these six-component histograms are pairwise distinct over all 192 edges of `Q_6`.

## Proof

For any fixed landmark `s` and shell `r`, exactly

`6*C(5,r)`

edges have edge-distance `r` from `s`: fix one coordinate direction, project the 32 parallel edges to `Q_5`, and count Hamming-distance-`r` vertices there, then sum over six directions.

Thus for `|S|=m`,

`sum_e H_e^S(r)=6m*C(5,r)`.

Assign a histogram `h=(h_0,...,h_5)` the weight

`W(h)=2(h_0+h_5)+(h_1+h_4)`.

Double counting gives the forced total

`sum_e W(H_e^S)=84m`.

For an individual edge, the distance shells contain `2*C(5,r)` vertices, so for `m<=7` the only active histogram-capacity restrictions are `h_0,h_5<=2`.

For `m=6`, the numbers of admissible histograms of weights `0,1,2,3,4,5` are

`7,12,27,36,54,60`.

Any 192 distinct admissible histograms therefore have total weight at least

`0*7 + 1*12 + 2*27 + 3*36 + 4*54 + 5*56 = 670`,

while the global identity forces total weight `84*6=504`. Contradiction.

For `m=7`, the corresponding low-weight counts are

`8,14,32,44,68,80`.

There are 166 admissible histograms of weight at most four, so 192 distinct histograms have total weight at least

`0*8 + 1*14 + 2*32 + 3*44 + 4*68 + 5*26 = 612`,

whereas the global total is `84*7=588`. Contradiction.

The previously published lower bound excludes landmark sets of size below six; the two contradictions exclude sizes six and seven. Hence `edim_m(Q_6)>=8`.

## Reproducibility

The source report states an independent verifier that reproduced the low-weight counts and the contradictions `670>504` and `612>588`, and separately checked Allikvere's 15-vertex certificate. The source report states that its locally generated `RESULT.md`, `REVIEW.md`, and `verify_q6_bound.py` could not be attached because those files were not available in the supplied package. Those unavailable local files are therefore not fabricated or republished here.

## Prior work and scope

The closest source is Jaan Allikvere, *The edge multiset dimension of hypercubes*, arXiv:2608.09983 (5 Aug 2026), which gives an explicit 15-vertex resolving set for `Q_6` and reports only `edim_m(Q_6)>=6`. The source report also checked Farhan--Klavžar--Kuziak--Yero, arXiv:2607.10311, and Ikhlaq--Ismail--Siddiqui--Nadeem, *Symmetry* 15 (2023), 762.

## Limitations

The exact value remains unknown. the same-model review classified originality as a qualified PASS only; unpublished or very recent unindexed work may overlap. No consequential inaccessible source was identified in the source report, and no independent review is claimed.
