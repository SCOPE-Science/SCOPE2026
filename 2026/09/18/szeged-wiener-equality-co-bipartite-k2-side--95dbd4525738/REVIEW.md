# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The exact formula was re-derived from the defining distance counts. Under the 2-connectivity conditions, the graph has diameter at most two, so for every edge \(uv\),
\[
n_{uv}(u)=\deg(u)-|N(u)\cap N(v)|.
\]
Applying this identity separately to the four \(Q\)-vertex types \(A,B,C,D\), to \(xy\), and to all cross-edges reproduces
\[
\eta(G)=8ab+2c(a+b)+3d(a+b)+4cd-4d.
\]
The Wiener-index count was also checked directly from the complete list of nonedges.

The equality classification reduces to the integer equation
\[
8ab+2c(s-1)+d(3s+4c-6)-2s-4=0,\qquad s=a+b,
\]
together with
\[
a+c\ge1,\quad b+c\ge1,\quad a+b+c\ge2.
\]
The case split in `RESULT.md` exhausts \(c=0\) and \(c\ge1\), and in the latter case first forces \(ab=0\). The remaining one-variable divisibility cases leave only the stated \(q\ge8\) solutions.

As a supplementary check, `artifacts/verify_small_side.py` constructs the graphs from the four parameters, computes all-pairs distances, evaluates \(W\) and \(Sz\) from their definitions, and verifies both the formula and the equality classification throughout the stated finite test range. This computation is not used as a substitute for the general proof.

No hidden hypothesis was found in the 2-connectivity reduction: for \(q\ge2\), the three displayed attachment conditions are sufficient because deleting \(x\) or \(y\) leaves the other attached to \(Q\), while deleting a vertex of \(Q\) leaves at least one attachment from the adjacent pair \(\{x,y\}\) to the remaining clique.

## Originality

Originality assessment: **PASS, to the best of our knowledge.**

Zhang--Li (arXiv:2609.20025) proves the \(2n\) lower bound, poses the equality classification as Problem 7, gives the family corresponding to
\[
(a,b,c,d)=(1,1,0,q-2),
\]
and explicitly states that their displayed sufficient condition is not necessary. The source does not provide an exact formula for the co-bipartite two-vertex-side class or a classification within it. The present result therefore addresses a concrete portion of their newly posed equality problem without claiming to solve the global problem or to identify the unspecified counterexamples they mention.

Bonamy--Knor--Lužar--Pinlou--Škrekovski (2017) was checked at its full accessible text around the relevant bounds and conjecture. It proves the \(2n-6\) theorem, characterizes equality there, and conjectures the later \(2n\) bound; it does not state this co-bipartite equality classification. Klavžar--Nadjafi-Arani (2014) was checked through its accessible text for the closest terminology and structural themes; its bounds are organized around bipartite/isometric-cycle and girth regimes, not the present dense two-clique parameterization.

Exact and synonymous searches included Szeged-Wiener equality at \(2n\), co-bipartite graphs, two-clique formulations, and equivalent cross-neighborhood descriptions. No stronger or equivalent theorem was found. No inaccessible paper was identified as specifically likely to contain this exact classification. The main residual risk is very recent or unindexed parallel work, especially because the equality problem appeared only in the 2026 preprint.

## Value

Value assessment: **PASS.**

The result gives both an exact invariant formula on a natural infinite dense graph class and a sharp equality classification inside a newly posed open problem. It shows rigidity from \(n\ge11\) in this class and isolates a unique additional ten-vertex equality type. The statement is substantially stronger than evaluating one numerical example or one parameter choice.

## Limitations

- The global classification in Zhang--Li Problem 7 remains open.
- The theorem assumes a co-bipartition with one clique of size two.
- The finite computation is supporting evidence only; correctness rests on the general counting proof.
- Originality is to the best of our knowledge.
- Independent audit has not been performed.
