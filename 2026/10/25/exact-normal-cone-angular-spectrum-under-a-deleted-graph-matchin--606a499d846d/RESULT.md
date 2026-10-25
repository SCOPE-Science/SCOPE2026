# Exact normal-cone angular spectrum under a deleted graph matching

## Finding
Let \(n\ge4\) be an integer, and delete an arbitrary matching \(M\) of size \(m\) from the complete graph \(K_n\). The symmetric edge (type-A root) polytope \(P_{n,M}\) has a **complete explicit spherical normal-cone angle spectrum**. At an oriented root vertex \(v_{ij}=e_i-e_j\), with \(\{i,j\}\notin M\), its normalized exterior solid angle is
\[
\omega(v_{ij})=\frac{2(n-2)+\sigma_i+\sigma_j}{2n(n-1)(n-2)},\qquad \sigma_k=\mathbf 1\{k\text{ belongs to an edge of }M\}.
\]
Thus the spherical measure depends only on the number of endpoints incident with deleted edges. For \(s=0,1,2\), the possible angle value is \(\omega_s=(2(n-2)+s)/(2n(n-1)(n-2))\), with **oriented-vertex multiplicity**
\[
2N_0=2\binom{n-2m}{2},\quad 2N_1=4m(n-2m),\quad 2N_2=4m(m-1).
\]
Zero multiplicities are omitted. When two or more levels occur, their values are strictly ordered \(\omega_0<\omega_1<\omega_2\). In particular, deleting a nonempty matching redistributes normal-cone solid angle toward retained roots incident to its endpoints. All angle masses sum to one.

## Assumptions and scope
For integers \(n\ge4\) and \(0\le m\le\lfloor n/2\rfloor\), fix any matching \(M\) with \(m\) pairwise disjoint undirected edges on vertex set \(\{1,\ldots,n\}\). Write \(G=K_n\setminus M\), \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), and
\[
P_{n,M}=\operatorname{conv}\{e_i-e_j:\{i,j\}\in E(G),\ i\ne j\}\subset H.
\]
For a vertex \(v\), its outward normal cone is \(N_P(v)=\{u\in H:\langle u,v\rangle\ge\langle u,x\rangle\ \forall x\in P\}\). Let \(U\) be Haar-uniform on the unit sphere of the \((n-1)\)-dimensional Euclidean space \(H\). The normalized angle is \(\omega(v)=\Pr(U\in N_P(v))\). Boundary ties have spherical probability zero. All listed roots are distinct points of common Euclidean norm \(\sqrt2\), so each is an exposed vertex: its inner product with itself is uniquely largest among the roots.

## Proof
Choose independent standard Gaussian variables \(Z_1,\ldots,Z_n\), let \(\overline Z=n^{-1}\sum_i Z_i\), and represent \(U=(Z-\overline Z\mathbf 1)/\|Z-\overline Z\mathbf1\|\). The projection and common positive denominator do not change the ordering of linear scores on roots. Hence the undirected maximizing edge is the allowed \(\{i,j\}\) that maximizes \(|Z_i-Z_j|\).

Almost surely all coordinates are distinct. Let \(a\) and \(b\) be the indices of the largest and smallest, and let \(a'\) and \(b'\) be those of the second-largest and second-smallest coordinates. If \(\{a,b\}\notin M\), this unique complete-graph diameter is an allowed edge and wins. Each fixed allowed undirected edge occurs as the unordered extreme pair with probability \(2/[n(n-1)]\).

Suppose instead that \(\{a,b\}\in M\). Since \(M\) is a matching, the edges \(\{a,b'\}\) and \(\{a',b\}\) are both allowed. Every other allowed edge has score no larger than at least one of their two scores: the largest possible difference using neither extreme is at most \(Z_{a'}-Z_{b'}\), and differences using just one extreme are bounded by the corresponding second-extreme choice. The two candidate scores differ only through the upper and lower extreme gaps
\[
A=Z_{a}-Z_{a'},\qquad B=Z_{b'}-Z_{b};
\]
the edge \(\{a',b\}\) wins if \(A<B\), and \(\{a,b'\}\) wins if \(B<A\). Conditional on any prescribed assignment of labels to the Gaussian order ranks, the sorted values retain their unconditional distribution and are invariant under reversal with sign change. Thus \(\Pr(A<B)=\Pr(B<A)=1/2\), and equality has probability zero.

Fix an allowed undirected edge \(e=\{i,j\}\). Beyond its direct extreme-pair probability, it can win only when the extreme pair is a deleted edge incident to either \(i\) or \(j\). If \(i\) is a deleted-pair endpoint, its unique partner is the other extreme; conditional on that extremal event, the other endpoint \(j\) of \(e\) is the appropriate second-extreme label with probability \(1/(n-2)\), and its gap wins with probability \(1/2\). The contribution is
\[
\frac{2}{n(n-1)}\,\frac1{n-2}\,\frac12=\frac1{n(n-1)(n-2)}.
\]
There is one such contribution for each matched endpoint of \(e\). Summing gives
\[
\Pr(e\text{ wins})=\frac{2(n-2)+\sigma_i+\sigma_j}{n(n-1)(n-2)}.
\]
Central symmetry and the antipodal symmetry of \(U\) give equal probability to the two orientations of each winning edge. Division by two establishes the claimed normalized cone angle.

There are \(n-2m\) unmatched and \(2m\) matched graph vertices. Allowed edges having zero, one and two matched endpoints number \(N_0=\binom{n-2m}{2}\), \(N_1=2m(n-2m)\), and \(N_2=\binom{2m}{2}-m=2m(m-1)\), respectively. Every edge gives two oriented roots, establishing the multiplicities. The probabilities partition the unit sphere, and the three candidate values differ by \(1/[2n(n-1)(n-2)]>0\).

## Verification
The independent executable `VERIFY.py`, included with this result, computes exact rational exposure probabilities by enumerating every Gaussian rank assignment for each \(4\le n\le8\) and all possible matching sizes. It treats the two potential winners after a forbidden extreme pair as equally likely, justified analytically by exchangeability of the two extreme spacings. It also checks normalization and vertex-level multiplicities for \(4\le n\le300\). Its output is `EXACT_ANGLE_PASS cases=19 permutations=225072 edge_checks=304 symbolic_n_max=300`. The numerical checks are finite confirmations; the proof above establishes all integer dimensions.

## Relationship to prior work
D'Alì, Delucchi and Michałek introduced broad face-theoretic and algebraic-combinatorial tools for symmetric edge polytopes and explicitly relate them to Kantorovich–Rubinstein polytopes. Braun, Bruegge and Kahle study facets of symmetric edge polytopes for random graphs. Neither accessible primary text gives this fixed-matching, vertex-by-vertex spherical normal-cone spectrum. General Gaussian normal-cone interpretations and Gaussian extreme-rank symmetry are classical principles; the asserted contribution is the exact closed angular classification in this graph-polytope family, not those principles themselves.

## Limitations
The theorem concerns uniform spherical normal-cone measures in the Euclidean zero-sum realization, and only graph deletions forming a matching. It does not classify full normal-cone shapes or cover arbitrary deleted-edge subgraphs. The result has had only self-review, not independent validation. Related results may exist under Gaussian argmax probability, graph Lipschitz-ball polar, root-polytope, or exterior-angle terminology and warrant further bibliographic comparison.

## References
1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (2019-10-11); primary MSC 52B20. https://arxiv.org/abs/1910.05193
2. B. Braun, K. Bruegge and M. Kahle, *Facets of Random Symmetric Edge Polytopes, Degree Sequences, and Clustering*, arXiv:2204.07239v1 (2022-04-14). https://arxiv.org/abs/2204.07239
