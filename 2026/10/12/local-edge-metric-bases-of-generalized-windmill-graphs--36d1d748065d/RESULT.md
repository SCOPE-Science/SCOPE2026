# Local edge metric bases of generalized windmill graphs
## Finding
For all integers \(r\ge2\) and \(m\ge2\), let
\[
W_{r,m}=K_1\vee rK_m
\]
be the generalized windmill formed from \(r\) copies of \(K_{m+1}\) sharing exactly one common center \(c\). Then
\[
\operatorname{edim}_{\ell}(W_{r,m})=rm-1.
\]

More strongly, every local edge metric basis is exactly
\[
V(W_{r,m})\setminus\{c,u\},
\]
where \(u\) is any one of the \(rm\) noncentral vertices. Hence \(W_{r,m}\) has exactly
\[
rm
\]
local edge metric bases.

The specialization \(m=2\) gives the friendship graphs.

## Assumptions and scope
All graphs are finite, simple, and connected. For a vertex \(s\) and edge \(e=xy\), define
\[
d(s,e)=\min\{d(s,x),d(s,y)\}.
\]
A set \(S\subseteq V(G)\) is a local edge metric generator if every pair of adjacent edges \(e,f\) is distinguished by some \(s\in S\), meaning
\[
d(s,e)\ne d(s,f).
\]
The minimum cardinality of such a set is the local edge metric dimension \(\operatorname{edim}_{\ell}(G)\).

Write the \(r\) noncentral blades as pairwise disjoint sets
\[
B_1,\ldots,B_r,
\qquad |B_i|=m,
\]
with every \(B_i\cup\{c\}\) inducing \(K_{m+1}\). There are no edges between distinct blades.

## Proof
For each noncentral vertex \(u\), call the edge \(cu\) its spoke.

Take two distinct noncentral vertices \(u,v\). The two spokes \(cu\) and \(cv\) are adjacent at \(c\). A vertex \(s\notin\{u,v\}\) cannot distinguish them. Indeed, if \(s=c\), both edge distances are \(0\). If \(s\) is noncentral, then
\[
d(s,cu)=d(s,cv)=1,
\]
because each spoke contains the center \(c\), which is adjacent to every noncentral vertex. In contrast, \(u\) distinguishes the two spokes, since
\[
d(u,cu)=0,\qquad d(u,cv)=1,
\]
and similarly for \(v\).

Therefore a local edge metric generator must meet every two-element subset of the \(rm\) noncentral vertices. Equivalently, it contains all but at most one noncentral vertex. Hence
\[
|S|\ge rm-1.
\]

For the upper bound, fix any noncentral vertex \(w\) and set
\[
S=V(W_{r,m})\setminus\{c,w\}.
\]
We prove that \(S\) distinguishes every pair of adjacent edges.

Let adjacent edges \(e=pq\) and \(f=pr\) share the vertex \(p\), with distinct noncommon endpoints \(q\) and \(r\).

If at least one of \(q,r\) belongs to \(S\), say \(q\in S\), then
\[
d(q,e)=0.
\]
If \(q\) is noncentral and \(q\notin f\), then \(q\) is adjacent to \(p\) whenever the two edges lie in one blade, and if \(p=c\) then \(q\) is itself adjacent to \(c\). Thus
\[
d(q,f)=1,
\]
so \(q\) distinguishes \(e\) and \(f\).

The only remaining possibility is that one noncommon endpoint is \(c\) and the other is the unique omitted vertex \(w\). Then the two adjacent edges have the form
\[
pu \quad\text{and}\quad pc
\]
with \(u=w\) and \(p,u\) in the same blade. Because \(r\ge2\), choose any \(s\in S\) from a different blade. Then
\[
d(s,pc)=1,
\qquad
d(s,pu)=2,
\]
so \(s\) distinguishes the pair.

Thus \(S\) is a local edge metric generator, proving
\[
\operatorname{edim}_{\ell}(W_{r,m})=rm-1.
\]

Finally, equality in the lower bound forces a minimum generator to contain exactly \(rm-1\) noncentral vertices and therefore to contain no center. Hence every basis is precisely \(V(W_{r,m})\setminus\{c,w\}\) for one noncentral vertex \(w\). There are exactly \(rm\) choices.

## Verification
The included checker constructs \(W_{r,m}\), computes all-pairs vertex distances, forms every adjacent edge pair, and tests the local edge metric definition directly.

It fully enumerates every vertex subset for
\[
2\le r\le5,\qquad 2\le m\le3,
\]
rejects every set smaller than \(rm-1\), enumerates every minimum set, and compares the complete basis family with the theorem. It also checks all predicted bases at the larger parameter pairs
\[
(2,4),\ (2,5),\ (3,4),\ (4,4),\ (6,2).
\]

## Relationship to prior work
The parameter was introduced in 2020. That source determines exact values for paths, ladders, cycles, stars, and wheels, and explicitly leaves further special graph families open. Its complete searchable text contains no occurrence of “friendship” or “windmill.”

A 2022 follow-up on wheel-related graphs states in its abstract that it treats fan graphs, semi-Jahangir graphs, and Jahangir graphs. It does not list friendship or generalized windmill graphs among the families analyzed.

A 2024 structural paper studies local edge metric dimension for corona products and edge-corona products and gives an integer-linear-programming formulation. Its indexed metadata assigns MSC \(05C12\) and \(05C76\). Neither its stated product theorems nor the earlier star and wheel formulas imply the present result: generalized windmills are vertex amalgamations of cliques, and local edge metric dimension is not monotone under adding the intra-blade edges to a star. The proof above shows that, despite those additional local constraints, the entire minimum-set family is stable.

## Limitations
The theorem requires at least two blades and blade size at least two. The one-blade case is a complete graph and behaves differently. No claim is made here for Dutch windmills with cycle blades, noncomplete blade graphs, or arbitrary vertex-amalgamations. Exhaustive computation is corroborative only; the all-parameter conclusion follows from the proof.

The 2022 wheel-related article was available through indexed text and abstract-level material, while its repository PDF endpoint was not retrievable during comparison. Its stated family list excludes generalized windmills, but inaccessible body text leaves a small residual terminology risk.

## References
1. R. Adawiyah, Dafik, R. Alfarisi, R. M. Prihandini, I. H. Agustin, M. Venkatachalam, “The local edge metric dimension of graph,” Journal of Physics: Conference Series 1543 (2020), 012009, DOI 10.1088/1742-6596/1543/1/012009.
2. R. Adawiyah, R. M. Prihandini, “Some Wheel Related Graph and It's Local Edge Metric Dimension,” Pancaran Pendidikan 11(3) (2022), 65–76, DOI 10.25037/pancaran.v11i3.426.
3. F. Amini, M. A. Henning, M. Tavakoli, “Local edge metric dimensions via corona products and integer linear programming,” Computational and Applied Mathematics 43(6) (2024), Article 358, DOI 10.1007/s40314-024-02879-0.
