# Independent audit — 2026-09-29

**Record:** `2026/09/17/the-sharp-one-third-bound-for-3-kernels-at-minimum-indegree-two--fb623dc79236`  
**Audited source tree:** `9af02221f4d868065b2b829f0bd6f5f2d9cdbed8`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** **PASSED**

## Correctness — PASS

PASS. The reduction from Boyer et al.'s Algorithm 1 with (ell,k)=(1,2) is valid: the final A has A-outdegree at most one, R is acyclic, 2|R|<=|B|, every b in B is reached from R in one step, and no arc runs from R to final A. For x with no B-in-neighbor, minimum indegree two therefore gives at least two A-in-neighbors, so C_x={x}∪N_A^-(x) has size at least three. Because an A-vertex has at most one A-outneighbor, it occurs in at most two C_x sets; the shared-element incidence multigraph is consequently a pseudoforest. I independently rechecked the pseudoforest edge/private-token covering lemma by component pruning and exhaustively enumerated every simple pseudoforest through seven vertices with the extremal token allocation p(v)=max(0,3-d(v)); the two-parallel-edge unicyclic base case was checked separately. The resulting hitting set P has |P|<=|A|/3. Inclusion-minimality makes D[P] acyclic: on a directed cycle each possible C_x hit by a cycle vertex is also hit by its predecessor or by the center x itself. Thus R∪P is a 2-prekernel, Boyer et al.'s Lemma 4.2 supplies a contained 3-kernel, and |R|+|A|/3<=|V|/3 follows from 2|R|<=|B|. The bidirected triangle gives equality.

## Originality — PASS

PASS, qualified to the best of current indexed evidence. Boyer et al. prove only the general q>=3 upper bound c_{δ,q}<=1/(floor(sqrt(δ+1))+1), which gives c_{2,3}<=1/2, while their universal lower bound is 1/(δ+1)=1/3. Their paper explicitly treats sharper constants as open territory. Targeted current searches found no subsequent indexed theorem establishing c_{2,3}=1/3. The record therefore appears to resolve the first nontrivial δ=2,q=3 case rather than restating the June 2026 result. Priority remains qualified because this is a very recent problem and an unindexed contemporaneous note could exist.

## Scientific value — PASS

PASS. Exact determination of c_{2,3} closes the first unresolved case of the conjectural formula c_{δ,q}=1/(δ+1) for q>=3. The proof is structural, not merely finite computation: the new ingredient is a pseudoforest-incidence covering mechanism that converts the residual outdegree-one geometry into the sharp one-third bound, so it has plausible reuse beyond this single parameter pair.

## Sources checked

- https://arxiv.org/abs/2606.16971 — Boyer et al., Small q-kernels in digraphs with minimum in-degree δ; definitions, Algorithm 1/Lemma 4.4, prekernel conversion Lemma 4.2, general upper bound, and lower bound.
- https://arxiv.org/abs/2608.00825 — Penev, Stein and Trujillo-Negrete, nearby 2026 q-kernel work; no located statement covering the exact minimum-indegree constant c_{2,3}.

## Limitations

- The pseudoforest covering argument was independently reconstructed and stress-tested but is not formally verified.
- Originality is necessarily qualified against unindexed or private work on a problem posed only months earlier.

No GitHub content was modified during this audit. This file records an independent evidence review; it is not a peer-review or priority guarantee.
