# Half-turn Lefschetz characters and full symmetry quotients of \(3\times n\) grid matching complexes

## Finding
For every integer \(n\ge2\), let \(G_n=P_3\mathbin{\square}P_n\) be the simple three-row, \(n\)-column nearest-neighbor rectangular grid. Let \(X_n=\mathcal M(G_n)\) be its ordinary matching complex, and let \(R\) reverse the rows and \(C\) reverse the columns. Put \(J=RC\), the half-turn. The reduced Lefschetz number is
\[
\widetilde\Lambda(g;X_n)=\sum_{i\ge0}(-1)^i\operatorname{tr}(g\mid\widetilde H_i(X_n;\mathbb Q)).
\]
Define \(D(z)=1+2z+2z^3+4z^4-2z^5+z^6\) and integer sequences \(b_m^{\mathrm{o}}\), \(b_m^{\mathrm{e}}\) by
\[
\sum_{m\ge0}b_m^{\mathrm{o}}z^m=\frac{1+z+3z^3-z^4}{D(z)},\qquad
\sum_{m\ge0}b_m^{\mathrm{e}}z^m=\frac{1-z^2+3z^3+z^5}{D(z)}.
\]
Then the half-turn's complete alternating rational homology character is
\[
\boxed{\widetilde\Lambda(J;X_{2m+1})=-b_m^{\mathrm{o}}\ (m\ge1),\qquad
\widetilde\Lambda(J;X_{2m})=-b_m^{\mathrm{e}}\ (m\ge1).}
\]
In particular this character, combined with the two coordinate-reflection characters, determines the reduced rational Euler characteristic of the quotient by the whole natural Klein-four group \(K=\langle R,C\rangle\). For an explicit fully numerical instance,
\[
\boxed{\widetilde\chi(X_{17}/K)=-51.}
\]
The displayed half-turn formula and resulting quotient invariant are the single finding; no degreewise homology classification is asserted.

## Assumptions and scope
A graph matching is a set of edges with no shared endpoint; a matching of size \(k\) is a \((k-1)\)-simplex of \(X_n\). The action is the **actual simplicial action on matching edges**, including orientation signs in chains, not merely a permutation of unoriented facets. All calculations use integral signed counting and therefore determine rational alternating homology traces via the Hopf trace formula. The quotient means the geometric-realization quotient \(|X_n|/K\), whose rational Euler characteristic can be obtained by averaging characters after barycentric subdivision. The two generating functions are formal power series about \(z=0\).

## Proof
**1. Fixed-orbit Lefschetz identity.** Suppose a graph automorphism \(g\) preserves a matching \(M\) of \(k\ge1\) graph edges, comprising \(s\) edge orbits. Its permutation on the oriented \((k-1)\)-simplex has sign \((-1)^{k-s}\), and the alternating chain sign is \((-1)^{k-1}\). Their product is \((-1)^{s+1}\). The augmented empty simplex contributes \(-1\), so the finite-chain Hopf trace formula gives
\[
\widetilde\Lambda(g;\mathcal M(G))=-\sum_{M:gM=M}(-1)^{\#(M/g)}.\tag{1}
\]
Here the sum includes the empty matching, with zero orbits. This includes the essential sign of a two-edge orbit.

**2. An explicit eight-state signed matching transfer.** Index masks \(A,B\subseteq\{0,1,2\}\) by bit masks \(0,\ldots,7\). A left column has vertices already occupied from preceding-column horizontal edges in \(A\), and selects outgoing horizontal edges in \(B\); overlapping masks are impossible. Within the three-vertex vertical path, one may choose no vertical edge or one of the upper/lower edges. Thus define the integer matrix
\[
T_{A,B}=\begin{cases}
(-1)^{|B|}\left(1-\mathbf1_{\{0,1\}\cap(A\cup B)=\varnothing}-\mathbf1_{\{1,2\}\cap(A\cup B)=\varnothing}\right),&A\cap B=\varnothing,\\
0,&A\cap B\ne\varnothing.
\end{cases}\tag{2}
\]
Each left-half matching is counted once, with sign \((-1)\) per selected edge-orbit, except that an incoming/outgoing seam orbit may need the adjustment in step 3. Denote the standard row and column basis vectors by \(e_A^\mathsf T\) and \(e_A\), and regard the following arrays as column vectors indexed by masks \(0,\ldots,7\):
\[
u_{\mathrm{o}}=(1,1,0,0,1,0,0,0)^\mathsf T,\qquad
u_{\mathrm{e}}=(1,0,1,0,0,-1,0,-1)^\mathsf T.\tag{3}
\]

**3. Folding by the half-turn.** For \(n=2m+1\), fold the graph about the center column. Every edge orbit wholly outside that column is a left-half edge paired with a disjoint right-half image. Every center-column vertical edge belongs to a two-edge orbit whose two members share the middle vertex, so neither can appear. The two orbits made from upper and lower horizontal edges incident to the center each use **both** outer center-column vertices; they conflict with each other. The orbit involving the middle center vertex contains two edges sharing that vertex, so it too is forbidden. Consequently exactly three outgoing boundary masks are allowed: empty, top alone, or bottom alone. The orbit sign of each allowed outgoing edge is already represented by its single left-half edge. Formula (1) therefore yields
\[
\widetilde\Lambda(J;X_{2m+1})=-e_0^\mathsf T T^m u_{\mathrm{o}}.\tag{4}
\]
For \(n=2m\), the fold lies between the two central columns. The middle-row seam edge is a singleton orbit. The upper and lower seam edges form one orbit and must be selected together or not at all. The four permitted outgoing masks are empty, middle, top-plus-bottom, and all three. Since an upper/lower pair is *one* edge orbit rather than two independent left-half edges, its sign is the negative of the sign already assigned by \((-1)^{|B|}\); this explains the negative entries at masks \(5\) and \(7\) of \(u_{\mathrm{e}}\). Thus
\[
\widetilde\Lambda(J;X_{2m})=-e_0^\mathsf T T^m u_{\mathrm{e}}.\tag{5}
\]
No unseen symmetry-fixed edge orbit can occur: every edge either lies strictly on one side of the fold, crosses the fold, or is contained in the central column.

**4. Exact rational generating functions, for all widths.** Let \(s_m(u)=e_0^\mathsf T T^m u\), and write \(d=(1,2,0,2,4,-2,1)\) for the coefficients of \(D\). Direct eight-state integer multiplication gives, for each \(u\in\{u_{\mathrm{o}},u_{\mathrm{e}}\}\),
\[
\sum_{j=0}^{6}d_j s_{m+6-j}(u)=0\qquad(0\le m\le7).\tag{6}
\]
Indeed these are the eight scalar identities \(e_0^\mathsf T T^m p(T)u=0\), where
\[
p(T)=T^6+2T^5+2T^3+4T^2-2T+I.
\]
By Cayley--Hamilton for this explicit \(8\times8\) matrix, any sequence \(e_0^\mathsf T T^m w\) satisfies a monic linear recurrence of order eight. Its first eight zero terms in (6) force *all* subsequent terms to be zero. The initial six values are, respectively,
\[
(s_m(u_{\mathrm{o}}))_{m=0}^{5}=(1,-1,2,-3,3,-4),\quad
(s_m(u_{\mathrm{e}}))_{m=0}^{5}=(1,-2,3,-5,10,-15).
\]
Multiplication by \(D(z)\) gives numerator coefficient lists \((1,1,0,3,-1,0)\) and \((1,0,-1,3,0,1)\), proving exactly the two stated rational generating functions. This is an algebraic proof, not recurrence fitting or inference from finitely many graph computations.

**5. Full symmetry quotient.** For completeness set \(F_j=e_0^\mathsf T T^j e_0\), and \(Q_m=e_0^\mathsf T T^{m-1}(e_7-e_1-e_4)\) for \(m\ge1\). Also set \(a_0=a_1=1\) and \(a_j=a_{j-1}-a_{j-2}\). Counting all matchings in the transfer gives \(\widetilde\Lambda(1;X_n)=-F_n\). Row reflection splits invariant edge orbits into two independent copies of path matchings, with signed count \(a_n^2\), so \(\widetilde\Lambda(R;X_n)=-a_n^2\). Under column reflection of odd width, the central column has signed factor \(1-2=-1\), and the paired off-axis edges contribute \(F_m\), so \(\widetilde\Lambda(C;X_{2m+1})=F_m\). For even width, three singleton seam edges cancel unless every last-column vertex of the folded half-grid is occupied; the remaining signed matching sum is \(Q_m\), whence \(\widetilde\Lambda(C;X_{2m})=-Q_m\). Combining these elementary fixed-orbit calculations with (4)--(5), rational character averaging gives the exact quotient formulas
\[
\widetilde\chi(X_{2m}/K)=-\frac{F_{2m}+a_{2m}^2+Q_m+b_m^{\mathrm{e}}}{4}\quad(m\ge1),\tag{7}
\]
\[
\widetilde\chi(X_{2m+1}/K)=\frac{-F_{2m+1}-a_{2m+1}^2+F_m-b_m^{\mathrm{o}}}{4}\quad(m\ge1).\tag{8}
\]
For \(n=17\), the exact transfer evaluations give \(F_{17}=320\), \(a_{17}=0\), \(F_8=94\) and \(b_8^{\mathrm{o}}=-22\). Formula (8) is therefore \((-320+94+22)/4=-51\). The quarter averages are integers because they are Euler characteristics of finite quotient CW complexes. This completes the proof.

## Verification
The accompanying executable `verify.py` uses only Python's standard library. It constructs the exact matrix (2), verifies the two rational-function identities by their initial coefficients and the eight exact scalar identities (6), and independently constructs graph edge orbits under a literal half-turn. The independent orbit-conflict matching enumerator agrees with both transfer formulas for every \(2\le n\le17\), sixteen widths, including the different odd/even center configurations. It additionally reproduces \(F_{17}=320\), \(F_8=94\), \(b_8^{\mathrm{o}}=-22\), and \(\widetilde\chi(X_{17}/K)=-51\). Run `python3 verify.py` from this package and expect `VERIFY_OK`. Finite orbit enumeration is a cross-check, not the all-width proof; steps 1--5 are the proof.

## Relationship to prior work
Chauhan, Sharma, and Shukla, arXiv:2609.27366 (first public September 23, 2026), prove nonequivariant vanishing ranges, first nonzero integral homology, and connectivity for the **same** family of graph matching complexes. Their Conjecture 4.1 posits an all-width wedge of spheres of dimension \(n-1\), and their published table covers widths at most nine. The present theorem neither assumes nor attempts to establish that conjecture. The two individual coordinate-reflection Lefschetz numbers and the ordinary signed matching generating function may be computed by separate orbit counts; those scalar invariants *do not determine* the missing product-character value for a Klein-four action. The new analysis is the half-turn fold with its nontrivial central seam sign constraints and the resulting complete quotient Euler invariants. The earlier Goyal--Shukla--Singh (2021) attempted homotopy classification was subsequently retracted and is not used as mathematical input. Width-two results of Braun--Hough and Matsushita do not cover the present family.

## Limitations
The theorem determines alternating rational homology characters, not the individual degreewise representations, torsion, or homotopy type of the quotient. A finite test up to width seventeen does not prove the all-width formulas; their proof depends on the exact transfer and Cayley--Hamilton calculation. Equivalence to an unindexed formula in earlier matching-polynomial or monomer--dimer literature remains possible, and no independent audit has occurred. The contribution concerns the missing half-turn action, not previously known generic Hopf-trace or group-averaging principles.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1, first posted 2026-09-23, https://arxiv.org/abs/2609.27366 (full 23-page manuscript, especially Theorem 1.2, Proposition 3.8 and Conjecture 4.1).
2. S. Goyal, S. Shukla, A. Singh, *Matching Complexes of \(3\times n\) Grid Graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), DOI:10.37236/10496. Retracted; consulted for topic comparison only.
3. B. Braun, W. K. Hough, *Matching and Independence Complexes Related to Small Grids*, Electronic Journal of Combinatorics 24(4), P4.18 (2017), DOI:10.37236/6212 (width-two family).
4. T. Matsushita, *Matching Complexes of Small Grids*, Electronic Journal of Combinatorics 26(3), P3.1 (2019), DOI:10.37236/8480 (width-two family).
