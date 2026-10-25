# The full vertex-permutation and particle-exchange homology of two configurations on the Kuratowski graph

## Finding
Let \(K_5\) denote the topological graph with one edge between each pair of five labeled vertices, and let \(X=\operatorname{Conf}_2(K_5)=\{(x,y)\in K_5\times K_5:x\ne y\}\). The symmetric group \(S_5\) permutes the five labels, and \(\tau(x,y)=(y,x)\) is particle exchange. These operations commute. Let \(V\) denote the four-dimensional standard rational representation of \(S_5\), and let \(\varepsilon\) denote the nontrivial one-dimensional representation of \(\langle\tau\rangle\cong C_2\). Then

\[\begin{aligned}
H_0(X;\mathbb Q)&\cong\mathbf1,\\
H_1(X;\mathbb Q)&\cong (\bigwedge^2 V)\boxtimes(\mathbf1\oplus\varepsilon),\\
H_2(X;\mathbb Q)&\cong\operatorname{sgn}_{S_5}\boxtimes\varepsilon,
\end{aligned}\]
with all higher groups zero. The irreducible \(\bigwedge^2 V\cong S^{(3,1,1)}\) is six-dimensional. The integral homology is free, of ranks \(1,12,1\); its ranks and the orientable genus-six surface type were established previously [1], and are not claimed as new.

Equivalently, for a permutation \(\sigma\in S_5\) having \(f\) fixed labels and \(t\) two-cycles, and \(e\in\{0,1\}\), the first-homology character is
\[
\operatorname{tr}((\sigma,\tau^e)|H_1)=
(1+(-1)^e)\frac{(f-1)(f-2)-2t}{2},
\]
and the second-homology character is \(\operatorname{sgn}(\sigma)(-1)^e\).

Because particle exchange reverses the fundamental orientation, the \(\tau\)-eigenlattices in rational first homology are each six-dimensional, invariant under every vertex permutation, and Lagrangian for the intersection form; its restriction to either eigenspace vanishes, and it pairs the two nondegenerately. The unordered two-particle quotient has first rational homology \(\bigwedge^2 V\) and is a nonorientable surface of genus seven.

## Assumptions and scope
The graph is the *topological* graph \(K_5\), with edges modeled by closed intervals and distinct particles forbidden to meet even at vertices. This is not the sink-configuration model that allows collisions at designated vertices. All homology-module statements are over \(\mathbb Q\), except for the stated ordinary integral homology groups. The group \(S_5\times C_2\) acts by genuine homeomorphisms; \(S_5\) acts on both coordinates and \(C_2\) interchanges them.

## Proof
The two-particle cubical deleted-product model \(D\) has a zero-cell for every ordered pair of distinct vertices, a one-cell for every choice of which particle traverses an edge while the other occupies a disjoint vertex, and a square for every ordered pair of disjoint graph edges. Its cell numbers are \(20,60,30\). The standard equivariant deformation-retraction criterion for two particles holds on the unsubdivided complete graph: paths between essential vertices have at least one edge and every simple cycle has length at least three. Hence \(D\simeq X\) equivariantly for all stated symmetries [1].

Each edge of \(D\) lies in exactly two squares. At any vertex \((a,b)\), the three possible departures of the first particle and the three departures of the second are linked by a six-cycle: the allowed squares are those whose two newly occupied endpoints are different. Thus every vertex link is a circle. Its one-skeleton is connected, so \(D\) is a connected closed surface. The cellular boundary matrix in the stated canonical oriented bases has \(\operatorname{rank}\partial_1=19\), \(\operatorname{rank}\partial_2=29\), and every nonzero Smith factor of \(\partial_2\) is one. The primitive generator of \(\ker\partial_2\) has all thirty square coordinates equal to \(\pm1\), verifying orientability. Euler characteristic \(20-60+30=-10\) gives genus six and \(b_1=12\), \(b_2=1\); these nonequivariant facts also follow from [1].

To establish the *action*, orient each graph edge from its smaller vertex to its larger vertex; orient a cell by the moving-particle coordinate in dimension one and by first-then-second particle order in dimension two. A label permutation acts on an edge by its image orientation sign; particle exchange interchanges the two coordinate directions and contributes a minus sign on squares. In these bases, compute for every \((\sigma,\tau^e)\) the signed traces \(T_i\) of its cellular maps on \(C_i(D;\mathbb Q)\), \(i=0,1,2\). Apply each square permutation to the primitive fundamental cycle to obtain the degree \(\operatorname{sgn}(\sigma)(-1)^e\), as is checked on every one of the 240 group elements. The Hopf trace formula gives
\[
\operatorname{tr}((\sigma,\tau^e)|H_1)
=1+\operatorname{sgn}(\sigma)(-1)^e-T_0+T_1-T_2.
\]
Direct counting of the fixed oriented cells for all seven conjugacy classes of \(S_5\), with either particle-exchange choice, yields precisely the formula in the Finding. The exhaustive standalone checker verifies this identity independently for every one of the 240 elements, using the actual signed cellular matrices, not numerical approximations. Finally, the standard representation has character \(f-1\), so its exterior square has character \(((f-1)(f-2)-2t)/2\); complete reducibility and character uniqueness over \(\mathbb Q\) identify the two \(S_5\)-irreducible exchange eigenspaces as \(\bigwedge^2V\). For any degree-one classes \(u,v\) in the same exchange eigenspace, the intersection form obeys \(\langle\tau u,\tau v\rangle=-\langle u,v\rangle\), forcing \(\langle u,v\rangle=0\). Their equal half-dimensions prove the Lagrangian assertion. Since \(\tau\) acts freely and reverses orientation, the quotient surface has Euler characteristic \(-5\), hence nonorientable genus seven.

## Verification
The included `verify.py` constructs the 20-by-60 and 60-by-30 signed integral boundary matrices from graph incidences. It verifies \(\partial_1\partial_2=0\), ranks \(19,29\), the 29 unit Smith factors, and a 30-square primitive generator with coefficients \(\pm1\). Independently the program implements every vertex permutation and both particle-exchange choices and confirms both homology character formulas for all 240 group elements. It requires Python 3 and SymPy (`sympy`), with entirely integral or rational arithmetic; execute `python verify.py` after installing SymPy. No floating-point computation or extrapolation occurs.

## Relationship to prior work
Barnett and Farber [1], specifically their discussion of the Kuratowski graphs in the first sections, establish that the two-point cubical configuration space of \(K_5\) is an orientable genus-six surface. Their general homology and intersection-form methods imply its ordinary ranks, not the complete \(S_5\times C_2\) homology representation asserted here. An and Knudsen [2] examine second graph braid-group homology, show generation results for planar graphs, and distinguish nonplanar phenomena; their results are not a character computation for the ordered two-point configuration of \(K_5\). Other results for sink configurations or different graphs concern different spaces. The precise additional data are the irreducible symmetric-group constituents, the exchange character, and the resulting invariant Lagrangian splitting.

## Limitations
This is a rational equivariant homology identification for this specific graph and two ordered particles, not an integral isomorphism of \(\mathbb Z[S_5\times C_2]\)-modules. The proof does not claim new genus or ordinary Betti ranks, nor a general classification for other complete graphs. The search and full-text checks described in the accompanying scientific review cannot exclude an unindexed equivalent equivariant calculation. No independent mathematical audit has been performed.

## References
[1] K. Barnett and M. Farber, *Topology of configuration space of two particles on a graph, I*, Algebraic & Geometric Topology **9** (2009), 593–624; arXiv:0903.2180, https://arxiv.org/abs/0903.2180.

[2] B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371, first posted 2020-08-24; Journal of Topology **15** (2022), 666–691, https://arxiv.org/abs/2008.10371. The 2020 preprint motivates the new nonplanar two-point case; the 2009 source is supporting background, not claimed as a newer discovery.
