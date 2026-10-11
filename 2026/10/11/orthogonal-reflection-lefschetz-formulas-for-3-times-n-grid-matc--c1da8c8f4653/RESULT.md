# Orthogonal-reflection Lefschetz formulas for \(3\times n\) grid matching complexes

## Finding
For every integer \(n\ge 2\), let \(G_n=P_3\mathbin{\square}P_n\) be the rectangular grid with vertices \((r,c)\), \(r\in\{0,1,2\}\), \(0\le c<n\), and edges at Manhattan distance one. Let \(X_n=\mathcal M(G_n)\) be the matching complex, whose simplices are sets of pairwise vertex-disjoint graph edges. Let \(R(r,c)=(2-r,c)\) and \(C(r,c)=(r,n-1-c)\), acting simplicially on \(X_n\). Define the reduced rational Lefschetz number
\[
\widetilde\Lambda(g;X_n)=\sum_{i\ge0}(-1)^i\operatorname{tr}(g\mid\widetilde H_i(X_n;\mathbb Q)).
\]
(The reduced augmented-chain convention is used to evaluate this number.) Define \(a_0=a_1=1\) and \(a_j=a_{j-1}-a_{j-2}\) for \(j\ge2\). Define integer sequences \((F_m)_{m\ge0}\) and \((Q_m)_{m\ge0}\) by their ordinary generating functions
\[
\sum_{m\ge0}F_mz^m=\frac{(1+z)^2(1-z+z^2)}{1+2z+2z^3+4z^4-2z^5+z^6},
\]
\[
\sum_{m\ge0}Q_mz^m=\frac{-z^2(1+z+2z^2-z^3+z^4)}{1+2z+2z^3+4z^4-2z^5+z^6}.
\]
Then the two orthogonal reflections have the exact reduced Lefschetz numbers
\[
\boxed{\widetilde\Lambda(R;X_n)=-a_n^2,
\qquad
\widetilde\Lambda(C;X_n)=\begin{cases}-Q_{n/2},&n\text{ even},\\F_{(n-1)/2},&n\text{ odd}.\end{cases}}
\]
In particular, the first trace is \(0\) precisely for \(n\equiv2\pmod3\) and is \(-1\) otherwise; the second is governed by a degree-six rational recurrence and can have magnitude greater than one. For \(n=7\), the two reduced Lefschetz numbers are respectively \(-1\) and \(-5\).

## Assumptions and scope
The graph is the simple, unweighted rectangular \(3\times n\) nearest-neighbor grid, with the two coordinate reflections acting on **edges** and hence on oriented simplices of the ordinary matching complex. These are *reduced, alternating* traces on rational homology, not traces in a specified degree. No assumption that homology is concentrated in one degree is made. All indices are nonnegative integers, the case \(n=2\) is included, and the rational functions are expanded formally at \(z=0\).

## Proof
**Signed fixed-face identity.** Let \(g\) be any automorphism of a finite graph. An invariant nonempty matching with \(k\) edges splits into \(s\) orbits under \(g\). The edge permutation on the oriented \((k-1)\)-simplex has sign \((-1)^{k-s}\); multiplying by its alternating-chain sign \((-1)^{k-1}\) gives \((-1)^{s+1}\). The augmented empty simplex contributes \(-1\). Consequently the Hopf trace formula gives
\[
\widetilde\Lambda(g;\mathcal M(G))=-\sum_{M:gM=M}(-1)^{\#(M/g)}.
\tag{1}
\]
This argument includes the orientation signs, rather than merely counting invariant faces.

**Reflection \(R\).** The two vertical graph edges in a column are exchanged by \(R\), share the center-row vertex, and therefore cannot both belong to an invariant matching. Each top-row horizontal edge and its bottom-row mate form a valid orbit. Every center-row horizontal edge is fixed. These two classes of edge orbits independently form matchings in two copies of the path on \(n\) vertices. Their signed orbit sum is \(a_n^2\), where the signed matching count of a path satisfies the displayed recurrence by deleting its last edge. Equation (1) proves the first formula and the period-six consequence.

**Reflection \(C\), odd width.** Write \(n=2m+1\). A pair of horizontal edges meeting the central column is interchanged by \(C\) and has a common central endpoint, so cannot be selected. Every remaining off-axis orbit corresponds to one matching edge in the left \(3\times m\) half-grid. The central column has two fixed vertical edges, of which at most one can be chosen, giving signed factor \(1-2=-1\). Thus the signed invariant-orbit sum equals \(-F_m\), where \(F_m\) is the signed matching count of the half-grid. Equation (1) yields \(\widetilde\Lambda(C;X_{2m+1})=F_m\).

**Reflection \(C\), even width.** Write \(n=2m\). Off-axis matching-edge orbits correspond to a matching in the left \(3\times m\) half-grid. There are precisely three fixed seam edges, one for each row. For a fixed half-grid matching, every free vertex in its last column permits an independent choice of its seam edge; summing with signs gives \((1-1)^b\), where \(b\) is the number of such free vertices. Only half-grid matchings saturating all three boundary-column vertices survive. Define \(Q_m\) as their signed sum. Equation (1) gives \(\widetilde\Lambda(C;X_{2m})=-Q_m\).

**Closed generating functions.** Index all subsets \(A,B\subseteq\{0,1,2\}\) by bit masks from \(0\) to \(7\), and put
\[
T_{A,B}=\begin{cases}(-1)^{|B|}\bigl(1-\mathbf1_{\{0,1\}\cap(A\cup B)=\varnothing}-\mathbf1_{\{1,2\}\cap(A\cup B)=\varnothing}\bigr),&A\cap B=\varnothing,\0,&A\cap B\ne\varnothing.\end{cases}
\]
This is the transfer matrix for signed matchings: \(A\) are vertices occupied from the preceding column, \(B\) are vertices selected for horizontal edges to the next column (each weighted \(-1\)), and the remaining vertices admit either no vertical edge or one of the two adjacent vertical edges (each weighted \(-1\)). Let \(e_A\) denote the standard basis vector. Then \(F_m=e_0^TT^me_0\) and, for \(m\ge1\),
\[
Q_m=e_0^TT^{m-1}(e_7-e_1-e_4),\qquad Q_0=0.
\]
The latter identity follows because a final column is fully covered with no outgoing edges exactly when all three vertices are incoming, or one extreme vertex is incoming and the complementary vertical edge is chosen. Taking matrix resolvents gives
\[
\sum_{m\ge0}F_mz^m=e_0^T(I-zT)^{-1}e_0,
\qquad\sum_{m\ge0}Q_mz^m=z e_0^T(I-zT)^{-1}(e_7-e_1-e_4).
\]
Exact symbolic evaluation of these explicit eight-by-eight matrices yields the two rational functions stated above. The accompanying standalone program evaluates the matrix identities over \(\mathbb Q(z)\), so no numerical interpolation is needed for the generating-function step. This completes the proof for every \(n\ge2\).

## Verification
Run `python verify_grid_reflection.py` with Python 3 and SymPy. It constructs the eight-state matrix and verifies both rational-function identities symbolically. Separately, it enumerates all matchings of \(G_n\) for each \(2\le n\le7\), tests invariance under each edge permutation, computes edge-orbit signs and compares the signed sums with the formulas. It prints `VERIFY_OK` after all tests. These finite enumerations support the result; they do not establish the all-width statement, which follows from the combinatorial proof and symbolic transfer identity.

## Relationship to prior work
Chauhan–Sharma–Shukla (first publicly posted September 23, 2026) study nonequivariant connectivity and homology of the same width-three grid matching complexes. Their publicly accessible abstract establishes vanishing ranges and nonvanishing in the first possible degree, without stating reflection-character formulas. Goyal–Shukla–Singh (2021) treated matching complexes of the same graphs, but the published paper was retracted; its homotopy conclusion is not used. The present theorem concerns the two specific reflection actions and their **alternating homology characters**, which do not follow from nonequivariant connectivity or Betti numbers. The generating functions count signed matchings only as an intermediate device for computing these equivariant topological invariants.

## Limitations
The formulas do not determine separate rational homology representations in every degree, the product of the two reflections, or integral torsion. The recent width-three-grid preprint could not be comprehensively inspected in full text; an unindexed or incidental equivalent equivariant calculation therefore remains a literature-overlap risk. The retracted 2021 work is not relied on for any theorem. This is not an independent audit or a claim of absolute uniqueness.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366 (first posted 2026-09-23), https://arxiv.org/abs/2609.27366.
2. S. Goyal, S. Shukla, A. Singh, *Matching Complexes of \(3\times n\) Grid Graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), https://doi.org/10.37236/10496. **Retracted**; consulted only to compare topics and terminology.
3. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics 26(3), P3.1 (2019), https://doi.org/10.37236/8480.
