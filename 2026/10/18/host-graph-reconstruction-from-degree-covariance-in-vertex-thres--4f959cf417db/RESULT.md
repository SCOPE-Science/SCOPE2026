# Host-graph reconstruction from degree covariance in vertex-threshold subgraphs

## Finding

**Theorem (exact degree-covariance inversion).** Let \(G=(V,E)\) be any finite, labeled, simple, undirected graph with \(n\ge1\) vertices, without restrictions on connectedness or regularity. Assign independent uniform \([0,1]\) random variables \(U_v\) to its vertices and retain a host edge \(uv\in E\) precisely when \(U_u+U_v\ge1\). Write \(Z_v\) for the degree of vertex \(v\) in the resulting random spanning subgraph, \(Z=(Z_v)_{v\in V}\), and \(\Sigma=\operatorname{Cov}(Z)\). Let \(A\) and \(D\) be the host adjacency and degree-diagonal matrices and set \(Q=D+A\), the signless Laplacian. Then

\[
\boxed{12\Sigma=Q+Q^2,\qquad Q=\tfrac12\big((I+48\Sigma)^{1/2}-I\big).}
\]

Here the square root is the unique positive-definite symmetric square root. In particular, the labeled host graph is uniquely determined by the joint covariance of its random degrees alone: for distinct vertices \(u,v\), the recovered \(Q_{uv}\) equals \(1\) if \(uv\in E\) and \(0\) otherwise. The result includes empty graphs and isolated vertices.

More explicitly, with \(d_v\) the host degree and \(c_{uv}=|N_G(u)\cap N_G(v)|\),

\[
\Sigma_{vv}=\frac{d_v(d_v+2)}{12},\qquad
\Sigma_{uv}=\frac{(d_u+d_v+1)A_{uv}+c_{uv}}{12}\quad(u\ne v).
\]

The covariance and signless Laplacian have identical eigenspaces, with the spectral transformation \(q\mapsto q(q+1)/12\). Their common nullity is exactly the number of bipartite connected components of \(G\), counting isolated vertices as bipartite components.

**Stable reconstruction.** If \(\widehat\Sigma\) is any symmetric positive-semidefinite matrix, set \(\widehat Q=\frac12((I+48\widehat\Sigma)^{1/2}-I)\). Then

\[
\|\widehat Q-Q\|_F\le12\|\widehat\Sigma-\Sigma\|_F.
\]

Consequently, \(\|\widehat\Sigma-\Sigma\|_F<1/24\) guarantees exact recovery of every host edge by rounding each off-diagonal entry of \(\widehat Q\) to \(0\) or \(1\) at threshold \(1/2\). In particular, the sample covariance from independently repeated vertex-threshold subgraphs reconstructs \(G\) eventually almost surely, as the number of repetitions tends to infinity.

## Assumptions and scope

Vertex labels are known and consistently aligned across repeated experiments, and a fresh independent uniform vertex-weight vector is drawn for each experiment. The underlying host graph is fixed, finite, simple, and undirected. The theorem concerns **the covariance of labeled vertex degrees**, not a covariance matrix of degree *frequencies* or a distribution of an unlabeled random graph. Both the model definition and all recovered quantities are exact finite-graph statements; there is no sparse-graph or large-degree assumption.

## Proof

Enumerate the host edges and let \(B\) be the unsigned vertex-edge incidence matrix, so \(Q=BB^{\mathsf T}\). If \(Y_e\) is the retained-edge indicator, then \(Z=BY\). A single edge is retained with probability \(1/2\), and hence \(\operatorname{Var}(Y_e)=1/4\). If distinct edges \(e=uv\) and \(f=uw\) meet at \(u\), their conditional retention probabilities given \(U_u=t\) both equal \(t\), and the remaining labels are conditionally independent. Therefore

\[
\mathbb E[Y_eY_f]=\int_0^1 t^2\,dt=\frac13,
\qquad \operatorname{Cov}(Y_e,Y_f)=\frac1{12}.
\]

If \(e\) and \(f\) are disjoint, their indicator variables are independent. Because the diagonal entries of \(B^{\mathsf T}B\) equal \(2\), and its off-diagonal entries equal \(1\) precisely for incident pairs of edges, these three cases yield

\[
\operatorname{Cov}(Y)=\frac{I+B^{\mathsf T}B}{12}.
\]

Multiplying by \(B\) and \(B^{\mathsf T}\) gives

\[
12\operatorname{Cov}(Z)=B(I+B^{\mathsf T}B)B^{\mathsf T}=BB^{\mathsf T}+(BB^{\mathsf T})^2=Q+Q^2.
\]

This formula is valid when \(E\) is empty: the incidence matrix then has zero columns. Since \(Q\) is positive semidefinite,

\[
I+48\Sigma=I+4Q+4Q^2=(I+2Q)^2,
\]

and \(I+2Q\) is positive definite. The principal square root is therefore exactly \(I+2Q\), proving the inversion formula. Expanding the diagonal and off-diagonal entries of \(Q+Q^2\) yields the stated entrywise formulas. Spectral mapping gives the eigenvalue correspondence. Finally,

\[
x^{\mathsf T}Qx=\sum_{uv\in E}(x_u+x_v)^2;
\]

on each connected component a vector in the kernel must alternate signs along edges. Such a nonzero alternating vector exists precisely for a bipartite component; an isolated vertex contributes one dimension. This proves the nullity statement.

To prove stability, write \(S=(I+48\Sigma)^{1/2}\), \(T=(I+48\widehat\Sigma)^{1/2}\), and \(X=T-S\). Both \(S\) and \(T\) are symmetric with eigenvalues at least \(1\). The identity

\[
TX+XS=T^2-S^2=48(\widehat\Sigma-\Sigma)
\]

is a Sylvester equation. In an orthonormal eigenbasis of \(T\) on the left and of \(S\) on the right, each entry of \(X\) is the corresponding right-hand-side entry divided by a sum of two eigenvalues, at least \(2\). Frobenius-norm invariance under orthogonal changes of bases therefore gives \(\|X\|_F\le24\|\widehat\Sigma-\Sigma\|_F\). As \(\widehat Q-Q=X/2\), the stated bound follows. Errors smaller than \(1/2\) in each off-diagonal entry preserve the binary host adjacency after rounding. Repeated independent degree observations are bounded, so the strong law of large numbers applies to their coordinate means and second products. Their empirical covariance tends entrywise (hence in Frobenius norm, for fixed \(n\)) to \(\Sigma\), which proves eventual almost-sure exact recovery.

## Verification

The accompanying standard-library script `verify.py` enumerates **all 1,099 labeled simple graphs on one through five vertices**. For each host, it calculates the degree covariance directly by summing the exact joint probabilities of pairs of retained edges, independently evaluates \((Q+Q^2)/12\), and tests entrywise equality in rational arithmetic. It also verifies the matrix-square identity and that covariance nullity equals the number of bipartite connected components. Running `python verify.py` produced `VERIFY_OK 1099 host graphs, exact edge-pair sums, rank, square-root inverse`. These finite checks supplement, but do not replace, the all-graph proof.

## Relationship to prior work

Fox, Luo and Pham study precisely this **vertex-threshold random spanning-subgraph model** for regular host graphs. Their first and second moments concern *counts of vertices of each degree*: in particular, their Theorem 2.1 proves a variance bound for each degree-frequency count. The inspected article does not provide the covariance matrix of the **labeled vector of degree magnitudes**, its graph-independent polynomial relationship with the signless Laplacian, or inversion recovering the host graph. The present statement applies to arbitrary, including irregular, hosts, and addresses a different inverse question.

Reilly and Scheinerman give the random threshold graph model when the host is complete, and their broad results concern the whole distribution of that special family. They therefore cover the complete-host distribution from which a specialized covariance could be calculated, but do not provide the all-host inverse covariance theorem stated here. Pal and Makowski study asymptotic empirical degree distributions of random threshold networks rather than the finite labeled-degree covariance and its inverse. The unsigned-incidence representation and the nullspace characterization of the signless Laplacian are standard graph spectral facts, not separately claimed as new.

The new assertion is the **exact covariance-to-host inversion and stability for the correlated, vertex-threshold subgraph mechanism**, not the creation of that mechanism or a new general spectral theory. A general pair-moment decomposition makes the identity accessible, and possible implicit appearances in older moment or graph-inference literature remain an originality risk.

## Limitations

The identification is of a **labeled** host, and requires population covariance or sufficiently accurate replicated-degree observations. The formula is specific to the stated independent, continuously uniform latent weights and threshold \(1\); unknown thresholds, dependent latent labels, edge noise, or missing vertex alignment need different analyses. This does not assert good finite-sample estimation rates for arbitrary growing graphs; the almost-sure consistency statement fixes \(n\). The originality review covers accessible relevant papers and search records, not every historical publication. Independent validation of mathematical and historical claims has not been performed.

## References

1. J. Fox, S. Luo, and H. T. Pham, *On random irregular subgraphs*, arXiv:2207.13651v1 (first posted 2022-07-27), Section 1 and Section 2, https://arxiv.org/html/2207.13651v1.
2. E. P. Reilly and E. R. Scheinerman, *Random Threshold Graphs*, Electronic Journal of Combinatorics 16 (2009), R130, DOI:10.37236/219, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v16i1r130.
3. S. Pal and A. M. Makowski, *Asymptotic degree distributions in large (homogeneous) random networks: A little theory and a counterexample*, arXiv:1710.11064 (2017), https://arxiv.org/abs/1710.11064.
