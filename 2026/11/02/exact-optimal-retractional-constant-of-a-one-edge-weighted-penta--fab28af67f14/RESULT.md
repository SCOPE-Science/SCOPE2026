# Exact optimal retractional constant of a one-edge weighted pentagon

## Finding
For every real \(t>0\), let \(M_t=\{0,1,2,3,4\}\) have the shortest-path metric of the graph with edges \(0\!\! -\!\!1\), \(1\!\! -\!\!2\), \(2\!\! -\!\!3\), \(3\!\! -\!\!4\) of length one and closing edge \(4\!\! -\!\!0\) of length \(t\). Fix basepoint \(0\). The optimal commuting retractional basis constant is
\[
\kappa(M_t)=\begin{cases}
1+t,&0<t\le1,\\
2/t,&1\le t\le2,\\
1,&t\ge2.
\end{cases}
\]
This is the infimum of the maximal Lipschitz constant over **every** ordering beginning at the basepoint and **every** compatible system of commuting prefix retractions. The value is attained by explicit retractions. In particular \(\kappa(M_1)=2\), whereas \(\kappa(M_t)=1\) from \(t=2\) onward, although the closing edge remains strictly shorter than the alternative path for \(2\le t<4\).

## Assumptions and scope
For an ordering \((v_0,v_1,v_2,v_3,v_4)\) of \(M_t\) with \(v_0=0\), write \(A_k=\{v_0,\ldots,v_k\}\). A commuting retractional system consists of maps \(r_k:M_t\to A_k\), for \(0\le k\le4\), each fixing \(A_k\) pointwise and satisfying \(r_j\circ r_k=r_{\min\{j,k\}}\) for all indices. Define
\[
\kappa(M_t)=\min_{(v_i),\,(r_k)}\max_{0\le k\le4}\operatorname{Lip}(r_k),
\qquad \operatorname{Lip}(r)=\max_{u\ne v}\frac{d_t(r(u),r(v))}{d_t(u,v)}.
\]
The finite minimization includes every allowed ordering and every compatible system, not just a prescribed retraction. The induced linear maps on the real Lipschitz-free space \(\mathcal F(M_t)\) form the corresponding partial-sum projections, with equal operator norms. No optimization over arbitrary linear bases is claimed.

## Proof
**Distance table in the nontrivial range.** For \(0<t\le2\), the distances on unit edges are one and the closing distance is \(t\). The remaining unordered distances are
\[
d_t(0,2)=d_t(1,3)=d_t(2,4)=2,
\qquad d_t(0,3)=d_t(1,4)=1+t.
\]
This follows by comparing the two arcs between each pair. The identities include the endpoints \(t=1,2\).

**Universal lower bound for \(0<t\le2\).** Consider the last proper prefix retraction \(r_3\), which fixes four vertices and sends the single omitted vertex \(v\in\{1,2,3,4\}\) to some different retained vertex \(w\). For each possible ordered pair \((v,w)\), the table below gives one retained vertex \(u\ne v\), followed by the ratio \(d_t(w,u)/d_t(v,u)\). Consequently that ratio is a lower bound for \(\operatorname{Lip}(r_3)\).

| Omitted \(v\) | Chosen target \(w\) | Witness \(u\) | Lower ratio |
| --- | --- | --- | --- |
| 1 | 0 | 2 | \(2\) |
| 1 | 2 | 0 | \(2\) |
| 1 | 3 | 0 | \(1+t\) |
| 1 | 4 | 2 | \(2\) |
| 2 | 0 | 3 | \(1+t\) |
| 2 | 1 | 3 | \(2\) |
| 2 | 3 | 1 | \(2\) |
| 2 | 4 | 1 | \(1+t\) |
| 3 | 0 | 2 | \(2\) |
| 3 | 1 | 4 | \(1+t\) |
| 3 | 2 | 4 | \(2\) |
| 3 | 4 | 2 | \(2\) |
| 4 | 0 | 3 | \(1+t\) |
| 4 | 1 | 3 | \(2\) |
| 4 | 2 | 0 | \(2/t\) |
| 4 | 3 | 0 | \((1+t)/t\) |

If \(0<t\le1\), every listed ratio is at least \(1+t\): in particular \(2/t\ge1+t\) and \((1+t)/t\ge1+t\). If \(1\le t\le2\), each ratio is at least \(2/t\), since \(2\ge 2/t\), \(1+t\ge2/t\), and \((1+t)/t\ge2/t\). Therefore every ordering and commuting system has constant at least the asserted value. The lower bound in fact does not need commutativity.

**Explicit optimal system.** Choose the ordering \((0,1,2,3,4)\). Encode each map by the images of vertices \((0,1,2,3,4)\). Define in both regimes
\[
r_0=(0,0,0,0,0),\qquad r_1=(0,1,0,1,0),\qquad r_4=(0,1,2,3,4).
\]
For \(0<t\le1\), set
\[
r_2=(0,1,2,1,0),\qquad r_3=(0,1,2,3,0).
\]
For \(t\ge1\), set
\[
r_2=(0,1,2,1,2),\qquad r_3=(0,1,2,3,2).
\]
Each map fixes precisely the required initial vertices, and direct substitution shows \(r_jr_k=r_{\min\{j,k\}}\). In the first regime, \(r_0,r_1,r_2\) are nonexpansive and the only enlarged edge image of \(r_3\) is \(3\!\! -\!\!4\mapsto3\!\! -\!\!0\), of length \(1+t\). Thus the maximum Lipschitz constant is \(1+t\). In the second regime, every unit edge is mapped to a pair at distance at most one, and the closing edge is mapped by \(r_2,r_3\) to \(0\!\! -\!\!2\) at distance at most two. Hence each map is \(\max\{1,2/t\}\)-Lipschitz. To justify testing only graph edges, map an arbitrary shortest path through its edge sequence and apply the triangle inequality to its image. This argument also applies when \(t\ge4\), when the direct closing edge no longer realizes the shortest endpoint distance. For \(t\ge2\), the system is nonexpansive, and a nonconstant retraction fixing two distinct vertices necessarily has Lipschitz constant at least one. This proves all three phases and the sharp boundaries.

## Verification
The accompanying standalone `verify_pentagon.py` uses exact rational arithmetic to reconstruct all distances, test each of the sixteen lower-bound witnesses, and check the asserted retraction identities and Lipschitz ratios at rational parameters on both sides of the two transition points. It also exhaustively enumerates all vertex orderings and all compatible retractions for selected rational values as an independent **finite** consistency test. Run `python verify_pentagon.py`; successful output is `PENTAGON_RATIONAL_CHECK_OK`. The proof above, not this finite collection of tests, establishes the result for all real \(t>0\).

## Relationship to prior work
Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces* (arXiv:1905.13188, first public 2019-05-30), constructs retractional-basis obstructions for particular finite samples of a circle **with an added center vertex**, notably a theorem requiring at least ten peripheral vertices. Those results do not determine this five-vertex weighted graph invariant. Hájek and Medina (arXiv:2112.03095) formalize compatible retractional bases and prove broad existence results for nets in Banach spaces without computing this sharp pentagon constant.

The exact coordinate-projection formulas for *spanning-tree edge-molecule bases* of weighted cactus transportation spaces (published-finding corpus record `b98930fbc1cd`) calculate norms of different linear projections; those need not arise from point retractions, and the calculation does not optimize commuting prefix point-map systems. Results on numerical index and Euclidean distortion of weighted cycles likewise concern different invariants. The present phase law optimizes over all allowed retractional systems, rather than over edge-coordinate bases. The cutoff at \(t=2\) is distinct from the metric redundancy cutoff \(t=4\).

## Limitations
The exact classification concerns only the five-vertex one-edge weighted cycle, a fixed basepoint, and retraction-induced partial-sum bases; it does not classify arbitrary weighted pentagons or arbitrary linear bases of the associated free space. Its proof does not extend without further work to longer cycles. A finite search cannot establish originality, and unindexed older treatments of retractional constants may exist. No independent mathematical audit has been performed.

## References
1. M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188, https://arxiv.org/abs/1905.13188 (first publicly posted 2019-05-30), especially Section 3 and Theorem 5.
2. P. Hájek and R. Medina, *Schauder bases in Lipschitz free spaces over nets in Banach spaces*, arXiv:2112.03095, https://arxiv.org/abs/2112.03095 (especially Definition 1.2).
3. *Sharp coordinate-projection norms for edge bases of cactus transportation spaces*, published-finding corpus record `2026/10/11/SCOPE-sharp-coordinate-projection-norms-for-edge-bases-of-cactus-trans--b98930fbc1cd`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-coordinate-projection-norms-for-edge-bases-of-cactus-trans--b98930fbc1cd.
