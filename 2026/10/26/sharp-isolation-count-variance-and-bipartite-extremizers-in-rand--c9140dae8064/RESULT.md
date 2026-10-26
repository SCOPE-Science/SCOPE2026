# Sharp isolation-count variance and bipartite extremizers in random irregular subgraphs

## Finding
Let \(G\) be any finite simple triangle-free \(d\)-regular graph on \(n\) vertices, for \(d\ge1\). Independently assign each vertex \(v\) a uniform \([0,1]\) mark \(U_v\); retain an edge \(uv\) iff \(U_u+U_v\ge1\). Let \(X\) count isolated vertices in the retained graph and put \(C_d=\binom{2d}{d}\). The **sharp finite-degree bound** is
\[
\operatorname{Var}(X)\le\frac{n}{d+1}R_d,\qquad
R_d=\frac{d+1}{d}\left(1-\frac1{C_d}\right)
+\frac{d(d-1)}{(d+1)(d+2)}<2.
\]
Equality in the first inequality holds precisely when every connected component of \(G\) is \(K_{d,d}\) (with \(K_{1,1}\) understood as a single edge). Thus the finite-\(d\) constant cannot be decreased whenever the order is a multiple of \(2d\). Moreover \(R_d\to2\), so the universal constant \(2\) in \(\operatorname{Var}(X)<2n/(d+1)\) is optimal. The theorem includes both connected and disconnected hosts.

More precisely, for distinct nonadjacent vertices \(u,v\) with \(t=|N(u)\cap N(v)|\),
\[
\operatorname{Cov}(\mathbf1_{\{u\text{ isolated}\}},\mathbf1_{\{v\text{ isolated}\}})
=\frac{t}{(d+1)^2(2d-t+2)}.
\]
For adjacent vertices, triangle-freeness gives the exact constant
\[
\operatorname{Cov}(\mathbf1_{\{u\text{ isolated}\}},\mathbf1_{\{v\text{ isolated}\}})
=\frac{1-C_d^{-1}}{d^2}-\frac1{(d+1)^2}.
\]

## Assumptions and scope
The host is finite, loopless, simple, triangle-free and exactly regular, with positive integer \(d\), and all marks are independent continuous uniforms. There are no size-asymptotic or connectedness assumptions. The random graph is a spanning subgraph of the specified fixed host; \(X\) counts degree-zero vertices only, not counts of other degrees. Equality uses the finite-degree constant \(R_d\), not the strict universal bound \(2\).

## Proof
For each vertex define \(Y_v=1-U_v\), and let \(I_v\) indicate isolation. Given \(Y_v=y\), each of its \(d\) neighbor marks must be below \(y\), hence \(\mathbb E I_v=\int_0^1y^d\,dy=1/(d+1)\), and \(\operatorname{Var}(I_v)=d/(d+1)^2\).

For nonadjacent \(u,v\), write \(t=|N(u)\cap N(v)|\). Conditional on \(Y_u=y,Y_v=z\), the joint isolation probability equals \(y^{d-t}z^{d-t}\min(y,z)^t\). Integrating the two symmetric triangles yields
\[
\mathbb E[I_uI_v]
=2\int_0^1z^{d-t}\int_0^z y^d\,dy\,dz
=\frac{2}{(d+1)(2d-t+2)}.
\]
Subtracting \(1/(d+1)^2\) gives the first claimed covariance.

For adjacent \(u,v\), triangle-freeness makes their remaining \(d-1\) neighbor sets disjoint. Their common edge is absent precisely when \(Y_u+Y_v>1\). Therefore
\[
\mathbb E[I_uI_v]
=\int_0^1\!\int_{1-y}^1 y^{d-1}z^{d-1}\,dz\,dy
=\frac1{d^2}-\frac{(d-1)!^2}{(2d)!}
=\frac{1-C_d^{-1}}{d^2}=:J_d.
\]
Let \(t_{uv}=|N(u)\cap N(v)|\). Every ordered adjacent pair has covariance \(J_d-(d+1)^{-2}\), and there are \(nd\) such pairs. Also \(\sum_{u\ne v}t_{uv}=nd(d-1)\), counting ordered pairs of neighbors of each common neighbor; triangle-freeness makes every positive term correspond to a nonadjacent pair. It follows that
\[
\operatorname{Var}(X)=\frac{nd}{(d+1)^2}
+nd\left(J_d-\frac1{(d+1)^2}\right)
+\frac1{(d+1)^2}\sum_{\substack{u\ne v\\uv\notin E(G)}}
\frac{t_{uv}}{2d-t_{uv}+2}.
\]
Since \(0\le t_{uv}\le d\), the last summand is at most \(t_{uv}/(d+2)\), with equality iff \(t_{uv}=0\) or \(t_{uv}=d\). Thus
\[
\operatorname{Var}(X)\le
\frac{nd}{(d+1)^2}+nd\left(J_d-\frac1{(d+1)^2}\right)
+\frac{nd(d-1)}{(d+1)^2(d+2)}
=\frac{n}{d+1}\left[d(d+1)J_d+\frac{d(d-1)}{(d+1)(d+2)}\right].
\]
Inserting \(J_d=(1-C_d^{-1})/d^2\) proves the stated \(R_d\).

If \(d\ge2\), equality forces any two distinct neighbors of any vertex to have all \(d\) neighbors in common. Fix vertex \(v\) in a connected component and let \(U=N(v)\); then the members of \(U\) have the same neighborhood \(W\), containing \(v\), with \(|U|=|W|=d\). Every vertex in \(U\) is adjacent to every vertex in \(W\), filling the degree of every vertex of \(U\cup W\). Connectivity forces this component to be exactly \(K_{d,d}\). Conversely every \(K_{d,d}\) has \(t_{uv}=d\) for nonadjacent distinct vertices, so attains equality. For \(d=1\), every regular graph is already a disjoint union of \(K_{1,1}\), and equality holds automatically.

Finally, direct algebra gives
\[
2-\left(\frac{d+1}{d}+\frac{d(d-1)}{(d+1)(d+2)}\right)
=\frac{(d-1)(3d+2)}{d(d+1)(d+2)}\ge0.
\]
Because \((d+1)/(dC_d)>0\), we have \(R_d<2\). The binomial coefficient \(C_d\) diverges rapidly, and each rational summand in \(R_d\) tends to one, so \(R_d\to2\). Taking \(G=K_{d,d}\) for increasing \(d\) proves optimality of the universal constant.

## Verification
The standalone file `verify_isolation_variance.py` uses exact rational arithmetic. It exhausts the ranks of all independent marks for nonadjacent pairs with \(1\le d\le3\) and all admissible codegrees, independently evaluates adjacent-pair triangular integrals by binomial expansion for \(1\le d\le29\), and checks the finite-degree bound and matching exact variance on \(K_{d,d}\). It completed 125 exact assertions (`VERIFY_OK`). These are checks of the finite computations; the preceding integrals and counting establish all integer degrees.

## Relationship to prior work
Fox, Luo and Pham introduce this random irregular subgraph model and give \(\operatorname{Var}(m(H,k))\le17n/(d+1)\) for every degree \(k\) in any regular host (Theorem 2.1 and Lemma 2.2). Their theorem applies here but has a larger constant and does not state the triangle-free isolation-count sharp extremal formula or equality structure. Alon and Wei study irregular spanning subgraph degree multiplicities and the same model's marginal uniformity. The present result is a specialized, substantially sharper, extremal second-moment theorem, not a refinement for all \(k\) or arbitrary hosts.

## Limitations
The statement only concerns isolation (\(k=0\)) and triangle-free regular hosts. It does not imply high-probability concentration at scales where \(n/(d+1)\) stays bounded, or a sharp bound for other degrees. Priority beyond the directly inspected literature has not been independently certified.

## References
- J. Fox, S. Luo, H. T. Pham, *On random irregular subgraphs*, arXiv:2207.13651v1 (2022-07-27), Section 2, https://arxiv.org/abs/2207.13651 ; published DOI:10.1002/rsa.21204.
- N. Alon, F. Wei, *Irregular subgraphs*, arXiv:2108.02685 (2021), https://arxiv.org/abs/2108.02685.
