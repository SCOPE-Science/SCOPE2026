# Full hyperoctahedral homology character of scale-two hypercube Čech complexes

## Finding

For every integer \(n\ge2\), let \(Q_n\) be the graph on \(\mathbb F_2^n\) whose edges join vectors differing in one coordinate. Let \(K_n\) be the intrinsic graph Čech complex at scale \(2\): its simplices are exactly the nonempty subsets of a closed graph neighborhood
\[N[v]=\{v,v+e_1,\ldots,v+e_n\}.\]
Every automorphism of \(Q_n\) acts on \(K_n\). Write
\[G_n=\operatorname{Aut}(Q_n)=\mathbb F_2^n\rtimes S_n,\qquad g(x)=\sigma x+b.\]

For the coordinate permutation \(\sigma\), let \(r\) be its number of cycles, \(a_1\) its number of fixed coordinates, and \(a_2\) its number of two-cycles. Define
\[D=a_1+\binom{a_1}{2}+a_2.\]
For each coordinate cycle \(C\), write \(s_C(u)=\sum_{i\in C}u_i\pmod2\). Define
\[F(g)=\begin{cases}2^r,&s_C(b)=0\ \text{for every cycle }C,\\0,&\text{otherwise,}\end{cases}\]
and
\[\tau(g)=\#\left\{z\in\mathbb F_2^n:\ \operatorname{wt}(z)\in\{1,2\},\ \sigma z=z,\ s_C(b+z)=0\ \text{for every }C\right\}.\]
These quantities depend only on the affine coordinate action and are computable from its disjoint cycles without constructing the simplicial complex. **The complete rational second-homology character** is
\[\boxed{\operatorname{tr}\!\left(g\mid H_2(K_n;\mathbb Q)\right)=F(g)\left(1-\frac D2+\binom{a_1}{2}-a_2\right)+2^{r-1}\tau(g)-1.}\]
The only positive-degree rational homology is in degree \(2\). The translation-fixed part has the following stronger structure as a module for coordinate permutations:
\[\boxed{H_2(K_n;\mathbb Q)^{\mathbb F_2^n}\cong\bigwedge\nolimits^2\mathbb Q^n.}\]
Here the right-hand side is the second exterior power of the natural permutation representation of \(S_n\). Its dimension is \(\binom n2\), but it has **no** nonzero \(S_n\)-invariant vector. Therefore \(H_2(K_n;\mathbb Q)^{G_n}=0\).

## Assumptions and scope

The space is the **intrinsic graph Čech complex**, not the Euclidean Čech complex and not a Vietoris–Rips clique complex. Scale \(2\) corresponds to closed radius-one balls in the edge-length-one geometric realization of the graph, so the description by closed vertex neighborhoods is exact. The group \(G_n\) acts on the simplicial vertices by affine coordinate permutations. Hamming weight is the number of nonzero binary coordinates. All homology representations and traces are over \(\mathbb Q\). All assertions hold for every integer \(n\ge2\).

The number \(\tau(g)\) can be found by considering only the following \(D\) candidate vectors \(z\): one coordinate belonging to a one-cycle; a pair of distinct one-cycle coordinates; or the two coordinates of a two-cycle. Keep just those candidates for which \(s_C(b+z)=0\) on every cycle. No search over all binary vectors is required.

## Proof

**1. Homological concentration.** Theorem 4.1 of Adams–Shukla–Singh proves
\[K_n\simeq\bigvee^{\beta_n}S^2,\qquad \beta_n=2^{n-2}(n^2-3n+4)-1.\]
This supplies the independent topological premise: \(H_0(K_n;\mathbb Q)=\mathbb Q\), \(H_2(K_n;\mathbb Q)=\mathbb Q^{\beta_n}\), and all other rational homology vanishes. The known homotopy equivalence is **not** assumed equivariant. Instead the trace is calculated from the genuine simplicial automorphism \(g\) using the Hopf trace formula. Its simplicial Lefschetz number \(L(g)\) equals \(1+\operatorname{tr}(g\mid H_2)\).

**2. Fixed vertices and edges.** Let \(V_g\) be the number of fixed cube vertices. Solving \(\sigma x+b=x\) one cycle at a time shows \(V_g=F(g)\): the necessary and sufficient consistency condition is \(s_C(b)=0\) on each coordinate cycle, and every consistent cycle has exactly two binary choices. The one-skeleton of \(K_n\) has an edge for each pair of vertices at Hamming distance \(1\) or \(2\). Among the fixed cube vertices, difference vectors must be invariant under \(\sigma\). The \(\sigma\)-invariant difference vectors of weight \(1\) or \(2\) are precisely the \(D=a_1+\binom{a_1}{2}+a_2\) vectors listed in the assumptions. Hence the number of edges with both endpoints fixed is \(F(g)D/2\), and each contributes \(+1\) to the signed trace in degree one.

A remaining setwise-fixed edge has its endpoints exchanged by \(g\). Writing its endpoints as \(x,x+z\), this requires \(\sigma z=z\), \(1\le\operatorname{wt}(z)\le2\), and \((I-\sigma)x=b+z\). The latter has solutions exactly when \(s_C(b+z)=0\) on every cycle, and in that case there are \(2^r\) ordered starting vertices. Dividing by two for the unordered edge gives exactly \(2^{r-1}\tau(g)\) exchanged edges. Each reverses the orientation of its one-chain. Therefore
\[\operatorname{tr}(g\mid C_0)=F(g),\qquad \operatorname{tr}(g\mid C_1)=\frac{F(g)D}{2}-2^{r-1}\tau(g).\]

**3. Every higher face has a unique center.** Two distinct closed neighborhoods of vertices of a hypercube intersect in at most two vertices: centers at distance one share their two endpoints, centers at distance two share exactly their two common neighbors, and more distant centers have empty intersection. Thus every face with at least three vertices belongs to a *unique* maximal simplex \(N[v]\). A face of dimension at least two can therefore be preserved setwise by \(g\) only if its center \(v\) is fixed by \(g\). At each fixed center, \(g\) fixes the center vertex and permutes the other \(n\) vertices of \(N[v]\) by the coordinate permutation \(\sigma\). This induced permutation has \(1+a_1\) fixed vertices and \(a_2\) transposed two-cycles. The full simplex on \(N[v]\), being contractible, has simplicial Lefschetz number one. Its trace in degree zero is \(1+a_1\), and its degree-one signed trace is \(\binom{1+a_1}{2}-a_2\). Subtracting these low-degree contributions, the alternating trace from its faces of dimension at least two equals
\[1-(1+a_1)+\binom{1+a_1}{2}-a_2=\binom{a_1}{2}-a_2.\]
The uniqueness of centers prevents any higher-dimensional face from being counted twice. Summing over the \(F(g)\) fixed centers gives the total higher-dimensional contribution \(F(g)(\binom{a_1}{2}-a_2)\). Combining with the degree-zero and degree-one traces yields
\[L(g)=F(g)-\frac{F(g)D}{2}+2^{r-1}\tau(g)+F(g)\left(\binom{a_1}{2}-a_2\right).\]
Subtracting the trivial trace of \(H_0\) proves the displayed homology character for **every** affine cube symmetry.

**4. The exterior-square invariant module.** Set \(T_n=\mathbb F_2^n\). Since \(T_n\) is normal in \(G_n\), the fixed subspace \(W_n=H_2(K_n;\mathbb Q)^{T_n}\) is an \(S_n\)-module. Its character is obtained by averaging over translations:
\[\chi_{W_n}(\sigma)=2^{-n}\sum_{b\in\mathbb F_2^n}\operatorname{tr}((\sigma,b)\mid H_2).\]
For each \(\sigma\), exactly \(2^{n-r}\) translations satisfy the fixed-point consistency conditions, so \(\sum_bF(\sigma,b)=2^n\). For each of the \(D\) invariant small difference vectors \(z\), exactly \(2^{n-r}\) translations satisfy the consistency conditions for \(b+z\). Consequently \(\sum_b2^{r-1}\tau(\sigma,b)=2^{n-1}D\). Substitution gives
\[\chi_{W_n}(\sigma)=\binom{a_1}{2}-a_2.\]
For the natural permutation representation \(P_n=\mathbb Q^n\), the trace of \(\sigma\) on \(\bigwedge^2P_n\) is also \(\binom{a_1}{2}-a_2\): fixed unordered pairs contribute \(+1\), while transposed pairs contribute \(-1\). Equality of characters over \(\mathbb Q\), together with semisimplicity for finite groups, establishes \(W_n\cong\bigwedge^2P_n\). Finally \(\bigwedge^2P_n\) has no trivial \(S_n\)-subrepresentation: an invariant alternating coefficient on a pair must be its own negative after the transposition of that pair. Hence \(H_2(K_n;\mathbb Q)^{G_n}=0\).

For clarity, the prior translation-only character follows by putting \(\sigma=\operatorname{id}\). In contrast a pure transposition of two coordinates in the three-cube has character \(-3\), not determined by the dimensions or translation traces alone.

## Verification

The companion, standard-library Python script `verify.py` independently enumerates **all** nonempty simplices of \(K_n\) as subsets of closed graph neighborhoods and, for every automorphism in dimensions \(2\) through \(5\), directly computes the oriented simplicial Lefschetz number with no use of the closed character formula. It compares every resulting trace with the cycle formula. It also averages over all translations for every coordinate permutation and compares against the exterior-square character. In dimension \(6\) it checks thirty-five specified affine symmetries. Run `python3 verify.py`; the expected concluding line is `VERIFY_OK`.

The verified full-automorphism counts for dimensions \(2,3,4,5\) are \(8,48,384,3840\), respectively, and the corresponding face counts are \(14,72,352,1616\). All complete checks passed. These bounded computations are corroboration, not proof of the statement for arbitrary dimension: the latter follows from the uniform fixed-face argument and the published homology-concentration theorem.

## Relationship to prior work

Adams–Shukla–Singh (arXiv:2212.05871, Theorem 4.1) established the nonequivariant wedge-of-two-spheres homotopy type and the Betti-number formula used here. Those results do not determine the group representation and are not presented as discoveries. A previously derived translation-only calculation determines the restriction to \(T_n\), including each one-dimensional translation constituent; this does not determine how nonidentity elements of \(S_n\) act, even on the translation-invariant summand. The **new result here is the character for the entire semidirect product** and identification of the \(S_n\)-module of translation invariants as \(\bigwedge^2\mathbb Q^n\).

Matsushita's general closed-neighborhood-complex equivalences and fundamental-group results do not calculate this hypercube homology character. Galetto–Montaño–Wellner compute equivariant homology for *Vietoris–Rips*, not intrinsic Čech, complexes on hypercubes; the two simplicial constructions have distinct face conditions and homology degrees at the indicated scales. A publication-independent comparison cannot exclude all equivalent unpublished or unindexed formulas.

## Limitations

The representation is **rational**, the underlying graph is the binary hypercube, and the Čech scale is exactly \(2\). The formula specifies the character of the full hyperoctahedral group, which determines its rational representation up to isomorphism; it does not list a separate irreducible decomposition for that nonabelian group. No claim is made about higher Čech scales, integral equivariant decompositions, or equivariance of the published sphere-wedge homotopy equivalence. The verification script is exhaustive only in the indicated finite dimensions. A literature search and internal overlap comparison are not a proof of worldwide novelty.

## References

1. H. Adams, S. Shukla, and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871v1 (first public 2022-12-12), revised v2 (2023), subsequently *Homology, Homotopy and Applications* 27(1) (2025), 83–105. In particular Lemma 2.2 and Theorem 4.1. https://arxiv.org/abs/2212.05871v1 and https://arxiv.org/html/2212.05871v2.
2. T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (2025), Theorems 1.2, 1.4 and 1.5. https://arxiv.org/html/2511.12608v2.
3. F. Galetto, J. Montaño, and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (2026), for the contrasting Vietoris–Rips setting. https://arxiv.org/abs/2606.20784.
