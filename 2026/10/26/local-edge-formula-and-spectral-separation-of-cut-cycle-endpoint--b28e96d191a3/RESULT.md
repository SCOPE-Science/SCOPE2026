# Local-edge formula and spectral separation of cut–cycle endpoint norms in strongly regular graphs

## Finding
Let \(G\) be a finite, connected, noncomplete, simple, unweighted strongly regular graph with parameters \((n,d,\lambda,\mu)\). Thus every vertex has degree \(d\), adjacent vertices have \(\lambda\) common neighbors, and nonadjacent vertices have \(\mu\) common neighbors; in particular, \(\mu>0\). Fix any orientation of the edges, let \(B\) be its vertex-by-edge incidence matrix, and let
\[
Q=B^{\mathsf T}(BB^{\mathsf T})^{+}B,\qquad P=I-Q.
\]
These are the Euclidean-orthogonal cut-space and cycle-space projections, considered as operators on the real edge-coordinate spaces \(\ell_1(E(G))\) and \(\ell_\infty(E(G))\).

Put \(m=d-\lambda-1\). For every unoriented edge \(e=uv\), define its *exclusive-neighbor sets*
\[
U_e=N(u)\setminus(N(v)\cup\{v\}),\qquad
V_e=N(v)\setminus(N(u)\cup\{u\}),
\]
and its local induced-edge statistic
\[
\tau_e=|E(G[U_e])|+|E(G[V_e])|,\qquad
\tau_*=\min_{e\in E(G)}\tau_e.
\]
Then the exact induced endpoint norms are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=
\frac{2}{\mu n}\bigl[d(2m+\mu)-2m-\tau_*\bigr],}
\]
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=
\frac{2}{\mu n}\bigl[d(2m+\mu)-2m-\tau_*\bigr]
+1-\frac{4(m+\mu)}{\mu n}.}
\]
More precisely, each edge \(e\) has a cut-projection column of absolute sum \(\frac{2}{\mu n}[d(2m+\mu)-2m-\tau_e]\); hence the norm-maximizing columns are exactly the edges with \(\tau_e=\tau_*\).

The norms are **not adjacency-spectrum invariants**, even within the class of strongly regular graphs. The \(4\times4\) rook graph \(R=K_4\mathbin\square K_4\) and the Shrikhande graph \(S\) both have parameters \((16,6,2,2)\) and adjacency spectrum \(\{6^1,2^6,(-2)^9\}\), but
\[
\boxed{\|Q_R\|=\frac94,\quad\|P_R\|=\frac{21}{8},\qquad
\|Q_S\|=\frac{19}{8},\quad\|P_S\|=\frac{11}{4}.}
\]
All displayed projection norms use either endpoint space, as above. In both graphs every edge attains the maximum. Thus each of the two endpoint norms distinguishes this cospectral pair, with difference \(1/8\).

## Assumptions and scope
The theorem concerns every existing connected noncomplete strongly regular graph with \(\mu>0\), including complete multipartite examples where the parameters are admissible. The graph is unweighted and its edge coordinates have the ordinary counting-measure \(\ell_1\) and \(\ell_\infty\) norms. The result concerns the *canonical Euclidean-orthogonal projections* only, not the infimum over all nonorthogonal projections. Vertex and edge orientations do not affect the values.

## Proof
**1. Exact electrical potential.** Let \(A\) be the adjacency matrix and \(L=dI-A=BB^{\mathsf T}\) the graph Laplacian. Strong regularity gives
\[
A^2=(d-\mu)I+(\lambda-\mu)A+\mu J,
\quad (n-d-1)\mu=d(d-\lambda-1)=dm.
\]
Consequently,
\[
(dI-A)\bigl[(d-\lambda+\mu)I+A\bigr]=\mu(nI-J).
\]
Fix an oriented edge with endpoints \(u,v\), and let \(b=\mathbf e_u-\mathbf e_v\). As \(Jb=0\), the vector
\[
\phi=\frac{[(d-\lambda+\mu)I+A]b}{\mu n}
\]
solves \(L\phi=b\). The cut-projection column for this edge is the vector of potential differences \(B^{\mathsf T}\phi\), up to an irrelevant orientation sign. Set \(c=1/(\mu n)\) and \(h=m+\mu=d-\lambda+\mu-1\ge1\). Since \(|U_e|=|V_e|=m\), the potential has values \(+hc\) at \(u\), \(-hc\) at \(v\), \(+c\) on \(U_e\), \(-c\) on \(V_e\), and \(0\) elsewhere.

**2. Exact total variation.** Define \(W_+=\{u\}\cup U_e\) and \(W_-=\{v\}\cup V_e\). These sets are disjoint and each has \(m+1\) vertices. With vertex-set indicators,
\[
\phi=c(\mathbf1_{W_+}-\mathbf1_{W_-})+(h-1)c(\mathbf1_{\{u\}}-\mathbf1_{\{v\}}).
\]
The two displayed vertex functions have consistently ordered values. Therefore, for *each* edge the two gradient contributions have the same sign or one vanishes; their absolute values add.

For any disjoint vertex sets \(W_+,W_-\), the edge total variation of \(\mathbf1_{W_+}-\mathbf1_{W_-}\) equals
\[
d(|W_+|+|W_-|)-2|E(G[W_+])|-2|E(G[W_-])|.
\]
Indeed, an edge joining the two sets contributes \(2\), an edge joining exactly one set to their complement contributes \(1\), and an edge internal to either set contributes \(0\); summing vertex degrees proves the identity. Here \(|E(G[W_+])|=m+|E(G[U_e])|\) and similarly for \(W_-\). The total variation is therefore \(2d(m+1)-4m-2\tau_e\). Also, because \(u\) and \(v\) are adjacent and have degree \(d\), the total variation of \(\mathbf1_{\{u\}}-\mathbf1_{\{v\}}\) is \(2d\). Thus
\[
\sum_{f\in E(G)}|Q_{f,e}|=
\frac{2d(m+1)-4m-2\tau_e+2d(h-1)}{\mu n}
=\frac{2}{\mu n}\bigl[d(2m+\mu)-2m-\tau_e\bigr].
\]
Taking the maximum over edges proves the formula for \(Q\).

**3. Complementary projection.** The diagonal entry at any edge is the effective resistance across that edge:
\[
Q_{e,e}=\phi(u)-\phi(v)=\frac{2(m+\mu)}{\mu n}.
\]
Because \(Q\) is an orthogonal projection on Euclidean edge space, \(0\le Q_{e,e}\le1\). For any projection matrix column,
\[
\sum_f|P_{f,e}|=
|1-Q_{e,e}|+\sum_{f\ne e}|Q_{f,e}|
=\sum_f|Q_{f,e}|+1-2Q_{e,e}.
\]
The correction is independent of \(e\), yielding the cycle-space formula. Both matrices are symmetric, so their maximum absolute row sums (induced \(\ell_\infty\) norms) equal their maximum absolute column sums (induced \(\ell_1\) norms).

**4. Cospectral witness.** In \(R=K_4\mathbin\square K_4\), every vertex neighborhood is the disjoint union of two triangles. Fixing an edge \(uv\) leaves \(U_e\) and \(V_e\) each spanning a triangle, so \(\tau_e=3+3=6\). In the Shrikhande graph, defined as the Cayley graph on \(\mathbb Z_4^2\) with generators \(\pm(1,0),\pm(0,1),\pm(1,1)\), every neighborhood induces a six-cycle. Deleting the vertex \(v\) and its two neighbors inside \(N(u)\) leaves a three-vertex path; hence each exclusive-neighbor set spans two edges, and \(\tau_e=2+2=4\). Both graphs are strongly regular with \((n,d,\lambda,\mu)=(16,6,2,2)\), so \(m=3\). Substituting gives the four stated norms. Their common adjacency spectrum follows directly from their common strongly regular parameters: the nontrivial eigenvalues satisfy \(\theta^2-4=0\), and trace plus dimension give multiplicities \(6\) and \(9\). This completes the proof.

## Verification
An independent standard-library exact-rational program, `check_srg.py`, constructs grounded graph Laplacians, inverts them over \(\mathbb Q\), reconstructs all cut and cycle projection columns, and compares the resulting absolute column sums with the local formula. Its eight test graphs are the five-cycle, Petersen graph, \(3\times3\) and \(4\times4\) rook graphs, Paley graph on thirteen vertices, Shrikhande graph, triangular graph on six labels, and \(5\times5\) rook graph. These contain \(333\) total edge columns. The program checks each graph's strongly regular parameters from its adjacency relation; it reports `SRG_HODGE_EXACT_OK cases=8 columns=333`. These finite checks are corroboration, not a substitute for the all-graph proof.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2018) identify finite graph Lipschitz-free spaces as quotients of real edge \(\ell_1\) by cycle spaces, providing Banach-space motivation. Their 2023 article studies invariant and minimum-norm projections, concentrating on discrete tori and Hamming graphs, and explicitly calculates a canonical endpoint cut-projection norm for the Hamming cube. It does not give the present local-edge characterization for strongly regular graphs. Godsil, Guo, Kempton and Lippner (2017) analyze adjacency spectra under two-vertex perturbations of strongly regular graphs; their spectral uniformity statements concern different invariants and do not imply equality of the absolute edge-current sums here. Brouwer and Van Maldeghem's monograph records the cospectral Shrikhande/rook pair and the local six-cycle distinction; those combinatorial facts are background, not the new norm calculation.

The standard identity relating complementary projection columns via the diagonal effective resistance is not claimed as new. Existing special-family endpoint formulas, for example for the rank-two Johnson/Kneser graphs or complete multipartite graphs, do not determine \(\tau_e\) for arbitrary strongly regular graphs and do not supply the Shrikhande/rook spectral separation. The claim is neither that these graphs are new nor that their nonisomorphism is new; it is the exact endpoint norm formula and the resulting new Banach-operator separation.

## Limitations
The statistic \(\tau_*\) still requires inspecting local induced subgraphs; the theorem does not reduce the norms to the strongly regular parameters alone. This is essential, as the cospectral witness demonstrates. The theorem neither classifies possible values of \(\tau_*\) over all strongly regular graphs nor proves minimum norms among arbitrary nonorthogonal projections. Nothing is asserted for weighted graphs, graph-directed (non-selfadjoint) Laplacians, or intermediate \(\ell_p\) operator norms. Literature overlap remains possible in less-indexed electrical-current or finite-graph projection sources; absence from targeted searches is not a proof of novelty.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, first arXiv version 10 July 2018, arXiv:1807.03814v1, https://arxiv.org/pdf/1807.03814 .
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, first arXiv version 21 May 2023, arXiv:2305.12582v1, https://arxiv.org/pdf/2305.12582 .
3. C. Godsil, K. Guo, M. Kempton, G. Lippner, *State transfer in strongly regular graphs with an edge perturbation*, first arXiv version 5 October 2017, arXiv:1710.02181v1, https://arxiv.org/pdf/1710.02181 .
4. A. E. Brouwer, H. Van Maldeghem, *Strongly Regular Graphs*, §10.6, https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf .
