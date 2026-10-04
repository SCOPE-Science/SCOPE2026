# Feasible polytope and all optimizers for fractional edge dimension of complete multipartite graphs
## Finding
Let \(G=K_{a_1,\ldots,a_k}\) be a connected complete multipartite graph of order \(N\ge3\). If \(k\ge3\), an edge resolving function \(g:V(G)\to[0,1]\) is feasible if and only if \(g(x)+g(y)\ge1\) for every two distinct vertices, so the unique optimum is \(g\equiv1/2\) and \(\operatorname{edim}_f(G)=N/2\). If \(k=2\), with parts \(A,B\), feasibility is equivalent to the same inequalities only for pairs lying within \(A\) or within \(B\). Hence the optimum face is the Cartesian product of the partwise fractional clique-cover optima: a singleton part has weight \(0\); a part of size \(2\) has arbitrary nonnegative weights summing to \(1\); and a part of size at least \(3\) has every vertex at weight \(1/2\). This recovers the published scalar values while classifying the entire feasible polytope and every optimizer.

## Assumptions and scope
All graphs are finite, simple, and connected. For distinct edges \(e,f\), let
\[
R_e\{e,f\}=\{z:d(z,e)\ne d(z,f)\},
\]
where \(d(z,uv)=\min\{d(z,u),d(z,v)\}\). An edge resolving function \(g:V(G)\to[0,1]\) satisfies \(g(R_e\{e,f\})\ge1\) for every distinct edge pair.

## Proof
Assume first \(k\ge3\). For any distinct vertices \(x,y\) in the same part, choose \(z\) in another part; then direct distance comparison gives
\[
R_e\{zx,zy\}=\{x,y\}.
\]
If \(x,y\) lie in distinct parts, choose \(z\) in a third part and the same identity holds. Thus every feasible \(g\) obeys \(g(x)+g(y)\ge1\) for every distinct vertex pair.

Conversely, every resolving neighborhood of two distinct edges contains at least two vertices: for adjacent edges their noncommon endpoints resolve them, and for disjoint edges endpoints of either edge have distance zero to that edge and positive distance to the other. Therefore the all-pairs inequalities are sufficient. Summing them yields
\[
(N-1)\sum_v g(v)\ge\binom N2,
\]
so the minimum is at least \(N/2\), attained by \(g\equiv1/2\). Equality makes every pair inequality tight; since \(N\ge3\), this forces \(g(v)=1/2\) for all \(v\).

Now let \(k=2\), with parts \(A,B\). For distinct \(x,y\) in one part, choosing \(z\) in the other gives \(R_e\{zx,zy\}=\{x,y\}\), so all same-part pair inequalities are necessary. They are sufficient: adjacent edges have their two noncommon endpoints in one part, while disjoint edges \(ab,a'b'\) have
\[
R_e\{ab,a'b'\}=\{a,a',b,b'\},
\]
which contains a same-part pair. The optimization therefore separates over the two parts. A part of size \(1\) has optimum total \(0\); size \(2\) has the segment of nonnegative weights summing to \(1\); and size \(m\ge3\) has unique optimum \(1/2\) on every vertex, by summing all \(\binom m2\) pair inequalities.

Consequently \(\operatorname{edim}_f(K_{1,N-1})=(N-1)/2\), while every other connected complete multipartite graph of order at least three has value \(N/2\), recovering the published scalar formula. The new claim is the exact feasible system and full optimizer classification.

## Verification
The included checker reconstructs every connected complete multipartite isomorphism type of orders \(3\) through \(10\), computes all-pairs distances by breadth-first search, and builds every edge resolving neighborhood directly. It verifies the claimed exact size-two neighborhoods, solves the original vertex-level linear program, and at the optimum separately minimizes and maximizes every coordinate.

## Relationship to prior work
Yi introduced fractional edge dimension and Proposition 3.7 of the foundational paper gives the complete-multipartite scalar values above. The same paper records twin-pair resolving-neighborhood constraints. A 2021 follow-up defines minimal edge resolving functions and gives a general combinatorial method, while citing Yi's complete multipartite scalar calculation. Neither inspected source states the full complete-multipartite feasible polytope or all optimizer faces.

## Limitations
The scalar minimum values are prior results and are not the originality claim. The theorem concerns fractional edge dimension, not ordinary edge metric dimension or fractional local edge dimension. The computation through order ten is corroborative only. Literature searches cannot exclude a differently phrased or non-indexed optimizer classification.

## References
1. E. Yi, “On the edge dimension and fractional edge dimension of graphs,” arXiv:2103.07375v1, 12 March 2021; Discrete Applied Mathematics 319 (2022), 38–49, DOI 10.1016/j.dam.2022.07.014.
2. N. Goshi, S. Zafar, T. Rashid, J. L. G. Guirao, “A Combinatorial Approach to the Computation of the Fractional Edge Dimension of Graphs,” Mathematics 9 (2021), 2364, DOI 10.3390/math9192364.
