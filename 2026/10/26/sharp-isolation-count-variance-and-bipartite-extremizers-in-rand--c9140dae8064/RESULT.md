# Sharp isolation-count variance and bipartite extremizers in random irregular subgraphs

## Finding

Let \(G\) be a nonempty finite simple triangle-free \(d\)-regular graph on \(n\) vertices, where \(d\ge1\). Independently assign each vertex \(v\) a uniform \([0,1]\) mark \(U_v\), and retain an edge \(uv\) exactly when \(U_u+U_v\ge1\). If \(X\) counts vertices isolated in this spanning subgraph and \(C_d=\binom{2d}{d}\), then
\[
\operatorname{Var}(X)\le\frac n{d+1}R_d,\qquad
R_d=\frac{d+1}d(1-C_d^{-1})+\frac{d(d-1)}{(d+1)(d+2)}<2.
\]
Equality in the finite-degree bound holds exactly for disjoint unions of \(K_{d,d}\), including unions of single edges when \(d=1\). Thus for orders divisible by \(2d\) the bound is attained. Also \(R_d\to2\), so the universal constant in \(\operatorname{Var}(X)<2n/(d+1)\) cannot be decreased. There is no connectedness assumption.

Let \(I_v\) denote the isolation indicator. For distinct nonadjacent \(u,v\) with codegree \(t=|N(u)\cap N(v)|\),
\[
\operatorname{Cov}(I_u,I_v)=\frac{t}{(d+1)^2(2d-t+2)}.
\]
For adjacent \(u,v\) the covariance is \(d^{-2}(1-C_d^{-1})-(d+1)^{-2}\). These claims use independent continuous marks and concern isolation only; they give no sharp bound for other degree counts or hosts with triangles.

## Proof

Set \(Y_v=1-U_v\). Conditional on \(Y_v=y\), isolation requires each neighbor mark to be below \(y\), so \(\mathbb E I_v=\int_0^1y^d\,dy=1/(d+1)\) and \(\operatorname{Var}(I_v)=d/(d+1)^2\). Ties have probability zero.

For nonadjacent vertices, conditional on \(Y_u=y,Y_v=z\), the joint probability is \(y^{d-t}z^{d-t}\min(y,z)^t\). Its integral is
\[
2\int_0^1 z^{d-t}\int_0^z y^d\,dy\,dz=\frac{2}{(d+1)(2d-t+2)}.
\]
For adjacent vertices the other neighbor sets are disjoint by triangle-freeness, and the common edge is absent if \(Y_u+Y_v>1\). Their joint probability is
\[
J_d=\int_0^1\int_{1-y}^1y^{d-1}z^{d-1}\,dz\,dy
=\frac1{d^2}-\frac{(d-1)!^2}{(2d)!}
=\frac{1-C_d^{-1}}{d^2},
\]
using the beta integral. Subtract the product of the means in both cases to obtain the stated covariances.

There are \(nd\) ordered adjacent pairs. The sum of \(t_{uv}=|N(u)\cap N(v)|\) over ordered pairs of distinct vertices is \(nd(d-1)\) by counting ordered pairs of neighbors of each vertex; under triangle-freeness only nonedges contribute. The individual variances cancel the subtracted products in the adjacent-pair sum. Hence
\[
\operatorname{Var}(X)=ndJ_d+\frac1{(d+1)^2}\sum_{u\ne v,\,uv\notin E(G)}\frac{t_{uv}}{2d-t_{uv}+2}
\le ndJ_d+\frac{nd(d-1)}{(d+1)^2(d+2)}=\frac n{d+1}R_d.
\]
The summand comparison is \(t/(2d-t+2)\le t/(d+2)\), with equality exactly for \(t=0\) or \(t=d\). For \(d\ge2\), equality forces the neighbors of each vertex \(v\) to have a common neighborhood \(W\) of size \(d\), containing \(v\). The sets \(N(v)\) and \(W\) are disjoint by triangle-freeness. All edges between these sets are present, filling all their degrees, so the component of \(v\) is \(K_{d,d}\). Conversely such components have all codegrees in \(\{0,d\}\) for distinct nonadjacent pairs. At \(d=1\) the variance bound is attained and the components are necessarily single edges.

Finally,
\[
2-\left(\frac{d+1}d+\frac{d(d-1)}{(d+1)(d+2)}\right)=\frac{(d-1)(3d+2)}{d(d+1)(d+2)}\ge0.
\]
The positive subtraction \((d+1)/(dC_d)\) gives \(R_d<2\) even at \(d=1\). Both summands in \(R_d\) tend to 1, so the sequence of hosts \(K_{d,d}\) proves optimality of 2.

## Verification and limitations

The accompanying `verify_isolation_variance.py` has a recorded run with 125 finite exact rational comparisons. It checks nonadjacent pairs by rank enumeration for degrees through 3, and the adjacent integral and variance expressions on \(K_{d,d}\) for degrees through 29. The analytic proof gives the theorem for all positive degrees and nonempty hosts; the finite tests are supporting evidence. A fixed host order not divisible by \(2d\) does not attain the displayed bound. No new concentration theorem beyond a variance estimate is asserted.

## Relationship to prior work

Frieze, Gould, Karoński and Pfender, *On Graph Irregularity Strength*, J. Graph Theory 41 (2002), 120–137, [doi:10.1002/jgt.10056](https://doi.org/10.1002/jgt.10056), use the uniform vertex-mark construction in their proofs of Lemmas 7 and 9: retaining the edges assigned weight 2 gives the spanning subgraph studied here. Their Eq. (1) gives the uniform degree marginal in the regular case. Alon and Wei, *Irregular subgraphs*, [arXiv:2108.02685](https://arxiv.org/abs/2108.02685), give this same marginal law and investigate degree multiplicities. Fox, Luo and Pham, *On random irregular subgraphs*, [arXiv:2207.13651](https://arxiv.org/abs/2207.13651), Theorem 2.1, state a variance bound \(17n/(d+1)\) for each degree count in arbitrary regular hosts. The present claim is the sharp finite-degree constant and equality structure for isolation in triangle-free hosts, together with the two exact indicator covariances. In particular, the shared edge for adjacent vertices is treated separately from nonadjacent pairs with common neighbors. Historical priority beyond the inspected statements is not claimed.
