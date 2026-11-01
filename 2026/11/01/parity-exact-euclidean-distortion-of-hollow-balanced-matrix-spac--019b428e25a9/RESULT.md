# Parity-exact Euclidean distortion of hollow balanced matrix spaces

## Finding
For every integer \(n\ge4\), let \(E_n\) denote the set of unordered pairs of distinct vertices of \([n]\), and let
\[
X_n=\left\{x\in\mathbb R^{E_n}:\sum_{e\ni i}x_e=0\ \text{for each }i\in[n]\right\},\qquad
\|x\|_\infty=\max_{e\in E_n}|x_e|.
\]
Equivalently, these are real symmetric hollow \(n\)-by-\(n\) matrices with zero row sums, with the maximum absolute off-diagonal entry norm. This space has dimension \(d_n=n(n-3)/2\). With multiplicative Banach--Mazur distance, put
\[
\delta_n=\begin{cases}
n/2,&n\text{ even},\\
0,&n\equiv1\pmod4,\\
3,&n\equiv3\pmod4.
\end{cases}
\]
Then
\[
\boxed{d_{\rm BM}(X_n,\ell_2^{d_n})^2=\frac{n-3}{n-1}\left(\binom n2-\delta_n\right).}
\]
The intrinsic Euclidean form \(\sum_{e\in E_n}x_e^2\) is optimal among *all* Hilbertian equivalent norms. In particular, the dimension-maximal distortion \(\sqrt{d_n}\) occurs if and only if \(n\equiv1\pmod4\).

Both Euclidean contact radii and all outer equality cases are explicit. For \(\|x\|_\infty=1\),
\[
\min_{x\in X_n}\sum_ex_e^2=\frac{n-1}{n-3},\qquad
\max_{x\in X_n}\sum_ex_e^2=\binom n2-\delta_n.
\]
Every outer maximizer has entries in \(\{-1,0,1\}\). Its zero edges are exactly a perfect matching when \(n\) is even, the empty set when \(n\equiv1\pmod4\), and a triangle when \(n\equiv3\pmod4\); in every case the remaining signs have equally many plus and minus incidences at each vertex. Conversely every such balanced signing attains the maximum. Inner minimizers are precisely the normalized coordinate projection vectors described below, up to a global sign.

## Assumptions and scope
The scalar field is \(\mathbb R\), the number of vertices is any integer \(n\ge4\), every off-diagonal edge coordinate has the same maximum-norm weight, and the constraint is **unsigned** incidence: each row sum, not an oriented divergence, vanishes. The Euclidean norm \(\|x\|_2=(\sum_{i<j}x_{ij}^2)^{1/2}\) counts each undirected edge once. For \(d\)-dimensional normed spaces the multiplicative Banach--Mazur distance is the infimum of \(\|T\|\|T^{-1}\|\) over all linear isomorphisms to \(\ell_2^d\); it is not the logarithmic convention. In particular the formula does not concern arbitrary centered symmetric matrices with nonzero diagonal, skew-symmetric flows, or a graph with missing edges.

## Proof
**1. Dimension and the inner radius.** Let \(B\) be the \(n\)-by-\(\binom n2\) unsigned vertex-edge incidence matrix of the complete graph: column \(e=\{i,j\}\) has ones in rows \(i,j\). Since \(BB^{\mathsf T}=(n-2)I+\mathbf1\mathbf1^{\mathsf T}\) is invertible, \(X_n=\ker B\) has dimension \(\binom n2-n=d_n\). The orthogonal projector from the edge Euclidean space onto \(X_n\) is
\[
Q=I-B^{\mathsf T}(BB^{\mathsf T})^{-1}B,
\quad (BB^{\mathsf T})^{-1}=\frac1{n-2}\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}{2(n-1)}\right).
\]
All diagonal entries \(Q_{ee}\) equal \(q=(n-3)/(n-1)>0\). Hence, for \(x\in X_n\), \(|x_e|=|\langle x,Q\mathbf e_e\rangle|\le\sqrt q\,\|x\|_2\). This gives \(\|x\|_2^2\ge 1/q\) when \(\|x\|_\infty=1\). Equality is realized by \(x=Q\mathbf e_e/q\), because \((Q\mathbf e_e/q)_e=1\) and \(|(Q\mathbf e_e/q)_f|\le1\) by the equal-diagonal projection Cauchy--Schwarz inequality. Explicitly its entries are \(1\) at \(e\), \(-1/(n-2)\) on each edge sharing exactly one endpoint with \(e\), and \(2/((n-2)(n-3))\) on each disjoint edge. Cauchy--Schwarz equality also shows that every inner minimizer has this form, with an arbitrary overall sign.

**2. Upper radius for even \(n\).** If \(n\) is even, each row contains an odd number \(n-1\) of numbers in \([-1,1]\) summing to zero. Maximizing the convex sum of their squares over that cube slice forces all but one entries to be saturated, with the remaining entry zero. Thus each row's square sum is at most \(n-2\), giving \(\|x\|_2^2\le n(n-2)/2=\binom n2-n/2\). To attain it, delete a perfect matching from \(K_n\); the remaining graph is connected, has even degree \(n-2\), and has an even number of edges. Follow an Eulerian circuit and assign alternating signs \(+1,-1\) along its edges, with zeros on the deleted matching. At each vertex, incident signs cancel in entrance/exit pairs. Equality forces exactly one zero at every vertex, so the zeros form a perfect matching.

**3. Integral extreme points for odd \(n\).** Consider the compact polytope \(C=\{x:Bx=0,\ |x_e|\le1\}\). Strict convexity of \(\sum_ex_e^2\) implies that every maximizer is an extreme point of \(C\). At an extreme point, the columns of \(B\) indexed by unsaturated edges \(F=\{e:|x_e|<1\}\) must be linearly independent, or a small nonzero perturbation supported on \(F\) would preserve the constraints. Each connected component of \(F\) is therefore a tree or an odd unicyclic graph: an even cycle gives an alternating kernel, and two cycles in one component also give dependent columns. For odd \(n\), at a vertex \(v\) incident to \(r_v\) edges of \(F\), the required sum of its free-edge entries is an integer of parity \(r_v\), since \(n-1\) is even and all fixed entries are signs. A tree, or any tree branch attached to an odd cycle, has a leaf where the single free edge is forced to be an odd integer and hence cannot lie strictly between \(-1\) and \(1\). Thus every nonempty free component is an odd cycle. At each cycle vertex the free-edge sum is even, and the unique solution around an odd cycle consists of integers (solve consecutive equations and divide their alternating total by \(2\)). Because those edges are unsaturated, each must be zero. Therefore **every extreme point** of \(C\) has only \(-1,0,1\) coordinates; the zero-edge subgraph has even degree everywhere (zero row sums require as many positive as negative edges at each vertex).

**4. Odd \(n\), split by residue class.** The universal bound is \(\|x\|_2^2\le\binom n2\). When \(n\equiv1\pmod4\), the graph \(K_n\) has even vertex degrees and an even number of edges, so alternating signs around an Eulerian circuit attain equality with no zeros. When \(n\equiv3\pmod4\), \(K_n\) has an odd number of edges, making a zero-free balanced signing impossible: summing all vertex constraints would require equally many positive and negative edges. A nonempty even-degree zero subgraph has at least three edges, hence \(\|x\|_2^2\le\binom n2-3\). This is attained by deleting a triangle; the remainder is connected (as \(n\ge7\)), has even degrees and an even number of edges, so Eulerian alternating signs give a balanced signing. Equality forces precisely the three edges of one triangle to vanish.

**5. Optimization over all Hilbertian norms.** Let \(H(x)=\langle Ax,x\rangle\) be any positive definite quadratic form defining a linear Euclidean comparison. Its squared distortion is the ratio of the maximum and minimum of \(H(x)\) on \(\|x\|_\infty=1\). After scaling, the inequalities \(\|x\|_\infty^2\le H(x)\le D^2\|x\|_\infty^2\) hold for all \(x\) if its distortion is at most \(D\). Averaging \(H\) over permutations of the vertices preserves these inequalities. Extend the averaged form from \(X_n\) to all edge vectors by first applying the Euclidean orthogonal projector \(Q\) in both slots; because \(Q\) commutes with vertex permutations, the extension is invariant. Every permutation-invariant symmetric bilinear form on the edge-coordinate space is a linear combination of the three relations 'same edge', 'shares one vertex', and 'disjoint'. On \(X_n\), for \(x,y\in X_n\), the ordered sum over shared-vertex distinct edge pairs equals \(-2\sum_ex_ey_e\) by expanding the zero row sums. The disjoint-pair sum equals \(\sum_ex_ey_e\), since \(\sum_ex_e=\sum_ey_e=0\). Therefore the restriction of any invariant form to \(X_n\) is a scalar multiple of \(\sum_ex_ey_e\). Consequently the ambient edge-Euclidean form minimizes distortion over *all* linear Euclidean comparisons. Combining steps 1--4 yields the claimed exact Banach--Mazur distance and complete equality classifications.

## Verification
The standalone `verification/check.py` uses rational arithmetic for the orthogonal projection, checks its idempotence at small orders, constructs an Eulerian-signing extremizer for every order from \(4\) through \(19\), and compares the resulting exact rational squared distortions to the formulas. It also solves \(160\) randomized linear programs on the cube section as independent finite sanity checks. The command is `python verification/check.py`; dependencies are Python 3, NumPy, SciPy, and NetworkX. These finite computations do not establish universal validity; that follows from the five proof steps above.

## Relationship to prior work
The Banach--Mazur problem for cube sections is motivated by the finite-dimensional geometry studied by Youssef, *Restricted invertibility and the Banach--Mazur distance to the cube* (first arXiv version 2012-06-04). That work gives general factorization and comparison bounds, not this exact signless-incidence kernel. Kurata and Bapat, *Moore-Penrose inverse of a hollow symmetric matrix and a predistance matrix* (2016), treat the larger hollow and centered matrix spaces and their Moore--Penrose inverses, not sharp cube-section Euclidean distortion of their intersection. Previous formulas for the bipartite row-and-column-zero rectangular matrix space also do not imply this result: they use a bipartite incidence kernel and a different symmetry representation. Here the unsigned complete-graph constraints are nonbipartite and the exact \(n\bmod4\) behavior arises from odd-cycle integrality.

## Limitations
This is a real finite-dimensional theorem with equal coordinate weights and all complete-graph edges present. It does not determine the Banach--Mazur distance for arbitrary graphs, weighted edge sup norms, complex scalars, nonzero diagonal, or other target spaces. The originality comparison is based on inspected sources and searchable records; an unindexed older exact treatment of this specific cube section is not ruled out. All equalities in the result are analytic, not inferred from the finite verifier.

## References
1. P. Youssef, *Restricted invertibility and the Banach--Mazur distance to the cube*, arXiv:1206.0654, first submitted 2012-06-04, https://arxiv.org/abs/1206.0654.
2. H. Kurata and R. B. Bapat, *Moore-Penrose inverse of a hollow symmetric matrix and a predistance matrix*, Special Matrices 4 (2016), 270--282, DOI:10.1515/spma-2016-0028, published 2016-07-07.
3. F. Grundbacher and T. Kobos, *On certain extremal Banach--Mazur distances in small dimensions*, arXiv:2407.08829 (2024), https://arxiv.org/abs/2407.08829; background on the dimension-maximal Euclidean distortion question only.
