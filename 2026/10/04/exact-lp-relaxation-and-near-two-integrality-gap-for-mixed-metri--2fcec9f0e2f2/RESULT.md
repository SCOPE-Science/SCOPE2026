# Exact LP relaxation and near-two integrality gap for mixed metric dimension of double fans
## Finding
Let \(F_{2,n}=\overline{K_2}\vee P_n\) be the double fan with apex vertices \(u_1,u_2\) and path vertices \(v_1,\ldots,v_n\), \(n\ge2\). Let \(\lambda_M(G)\) be the optimum of the continuous relaxation of the standard mixed-metric integer program: assign \(0\le y_s\le1\) to vertices and require \(\sum_{s:d(s,a)\ne d(s,b)}y_s\ge1\) for every two distinct elements \(a,b\in V(G)\cup E(G)\). Then \(\lambda_M(F_{2,2})=4\), \(\lambda_M(F_{2,3})=4\), and for every \(n\ge4\), \[\lambda_M(F_{2,n})=\frac{n+4}{2}.\] The optimum is unique. For \(n=2\) all four coordinates equal \(1\); for \(n=3\), \(y_{u_1}=y_{u_2}=y_{v_1}=y_{v_3}=1\) and \(y_{v_2}=0\); for \(n\ge4\), \(y_{v_1}=y_{v_n}=1\) and every other coordinate equals \(1/2\). Since the known integer mixed metric dimension is \(n+1\) for \(n\ge3\), the natural LP has additive gap \(\frac{n-2}{2}\) and ratio \(\frac{2(n+1)}{n+4}\), which tends to \(2\). The \(n=2\) graph is \(K_4-e\) and its integer value \(4\) is prior-covered by the max-mixed-dimension literature; no novelty is claimed for that integer endpoint.

## Assumptions and scope
All graphs are finite, simple, and connected. For \(n\ge2\), the double fan is
\[
F_{2,n}=\overline{K_2}\vee P_n,
\]
with nonadjacent apex vertices \(u_1,u_2\) and path vertices \(v_1,\ldots,v_n\).

For graph elements \(a,b\in V(G)\cup E(G)\), define the resolving neighborhood
\[
R(a,b)=\{s\in V(G):d(s,a)\ne d(s,b)\}.
\]
Kelenc, Kuziak, Taranenko, and Yero formulate mixed metric dimension as a binary covering program with one variable per vertex and one constraint for every pair of graph elements. Here \(\lambda_M(G)\) denotes its canonical continuous relaxation obtained by replacing the binary restrictions by \(0\le y_s\le1\):
\[
\lambda_M(G)=\min \sum_{s\in V(G)}y_s
\quad\text{subject to}\quad
\sum_{s\in R(a,b)}y_s\ge1
\quad(a\ne b).
\]
This notation is used only for the relaxation studied here; the published mixed metric dimension itself remains the integer optimum.

## Proof
The key point is that the full mixed-resolving system of the double fan has an exact small-neighborhood description.

First, every two-element subset of \(V(F_{2,n})\) occurs as an exact resolving neighborhood. Indeed:

- \(R(u_1,u_2)=\{u_1,u_2\}\).
- \(R(u_2,u_2v_i)=\{u_1,v_i\}\) and symmetrically \(R(u_1,u_1v_i)=\{u_2,v_i\}\).
- For \(i\ne j\), \(R(u_1v_i,u_1v_j)=\{v_i,v_j\}\).

Hence every feasible fractional solution satisfies
\[
y_p+y_q\ge1
\qquad\text{for all distinct vertices }p,q.
\]

We next classify singleton resolving neighborhoods. Two distinct vertices have at least themselves in their resolving neighborhood. Two distinct edges have at least two distinguishing endpoints, and a vertex not incident with an edge is distinguished from that edge by both endpoints. Thus a singleton resolving neighborhood can only arise from a vertex \(x\) and an incident edge \(xy\). In that case
\[
R(x,xy)=\{s:d(s,y)<d(s,x)\}.
\]

For a spoke, with \(x=v_i\) and \(y=u_a\), this set is
\[
\{u_a\}\cup\{v_j:|j-i|\ge2\}.
\]
The opposite orientation of a spoke is never singleton because it contains both \(v_i\) and the other apex. For a path edge, the two orientations give
\[
R(v_i,v_iv_{i+1})=\{v_{i+1}\}\cup
\begin{cases}\{v_{i+2}\},&i+2\le n,\\\varnothing,&i=n-1,\end{cases}
\]
and the left-right symmetric formula.

Consequently the vertices supporting singleton constraints are exactly
\[
\begin{cases}
\{u_1,u_2,v_1,v_2\},&n=2,\\
\{u_1,u_2,v_1,v_3\},&n=3,\\
\{v_1,v_n\},&n\ge4.
\end{cases}
\]
Every remaining resolving neighborhood has at least two vertices. Therefore the singleton constraints together with all pair constraints are not merely necessary but sufficient for the entire LP: any set of at least two vertices contains a pair whose weights already sum to at least one.

For \(n=2\), every coordinate is forced to one, giving \(\lambda_M=4\). For \(n=3\), four coordinates are forced to one and the only remaining coordinate can be zero, again giving \(\lambda_M=4\).

Now let \(n\ge4\). The two endpoint coordinates \(y_{v_1},y_{v_n}\) are forced to one. There remain exactly \(n\) unforced vertices, and on them the reduced program is the fractional vertex-cover program of the complete graph:
\[
x_i+x_j\ge1\quad(i\ne j),\qquad 0\le x_i\le1.
\]
Summing all \(\binom n2\) pair inequalities gives
\[
(n-1)\sum_i x_i\ge\binom n2,
\]
so \(\sum_i x_i\ge n/2\). Equality is attained by \(x_i=1/2\) for every unforced vertex. If equality holds, the sum of all pair inequalities is also equality, so every individual pair inequality is tight; because \(n\ge3\), this forces all \(x_i=1/2\). Thus the optimizer is unique and
\[
\lambda_M(F_{2,n})=2+\frac n2=\frac{n+4}2.
\]

For \(n\ge3\), the published integer value is \(\operatorname{mdim}(F_{2,n})=n+1\). Hence for \(n\ge4\) the additive and multiplicative gaps are
\[
(n+1)-\frac{n+4}2=\frac{n-2}2,
\qquad
\frac{n+1}{(n+4)/2}=\frac{2(n+1)}{n+4}\longrightarrow2.
\]
The \(n=2\) graph is \(K_4-e\), which earlier work already identifies as max-mixed-dimensional, so its integer optimum is \(4\).

## Verification
The included checker independently constructs each double fan for \(2\le n\le20\), computes all vertex distances by breadth-first search, forms every original resolving neighborhood \(R(a,b)\), and solves the unreduced continuous program with all element-pair constraints.

It verifies every exact two-vertex resolving neighborhood, the complete singleton classification, the closed-form optimum, and uniqueness by minimizing and maximizing every coordinate over the optimum face of the original LP. The finite computation is corroborative only; the arbitrary-parameter theorem follows from the proof above.

## Relationship to prior work
The foundational paper of Kelenc, Kuziak, Taranenko, and Yero introduces mixed metric dimension and explicitly gives the binary integer-programming formulation whose continuous relaxation is studied here. Its first public arXiv version is dated 14 November 2016, and the manuscript lists AMS/MSC \(05C12\), \(05C76\), and \(05C90\). The paper studies the integer invariant, not the continuous relaxation or its integrality gap.

Ghalavand, Klavžar, and Tavakoli later study graphs whose mixed metric dimension equals their order. In particular, their general results imply that \(K_4-e\), which is \(F_{2,2}\), has integer mixed metric dimension four. This prior result is used only to state the integer comparison at the small endpoint.

Rahmadi studies the integer mixed metric dimension of double fans and states the value \(n+1\) for \(n\ge2\). The displayed upper-bound set in that proof contains all \(n+2\) vertices, while the earlier max-mixed-dimension result already settles \(n=2\) as four. For \(n\ge3\), the integer value \(n+1\) is consistent with direct verification and is used here only as the denominator of the integrality-gap comparison. The new claim is the exact continuous relaxation, its unique optimizer, and its asymptotically factor-two gap.

Targeted searches for “fractional mixed metric dimension,” “mixed metric dimension LP relaxation,” “mixed resolving set fractional,” and “mixed metric dimension integrality gap,” including database searches for double fans, did not locate an equivalent theorem or a stronger result that implies this relaxation formula.

## Limitations
The result concerns the canonical continuous relaxation of the published binary mixed-metric formulation; it does not assert that \(\lambda_M\) is established standard notation. The exact formula is proved only for double fans. The finite LP replay through \(n=20\) does not replace the proof. Literature searches cannot exclude an unindexed treatment using different optimization terminology.

## References
1. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” arXiv:1611.04292v1, 14 November 2016; Applied Mathematics and Computation 314 (2017), 429–438, DOI 10.1016/j.amc.2017.07.027.
2. A. Ghalavand, S. Klavžar, M. Tavakoli, “Graphs whose mixed metric dimension is equal to their order,” arXiv:2305.19620, 31 May 2023; Computational and Applied Mathematics 42 (2023), 210, DOI 10.1007/s40314-023-02351-5.
3. D. Rahmadi, “Mixed Metric Dimension of Double Fan Graph,” Jurnal Diferensial 6(1) (2024), 52–56, published 9 February 2024, DOI 10.35508/jd.v6i1.12526.
