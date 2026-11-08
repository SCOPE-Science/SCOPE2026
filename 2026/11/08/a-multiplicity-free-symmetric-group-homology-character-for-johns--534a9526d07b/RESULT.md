# A multiplicity-free symmetric-group homology character for Johnson-graph clique complexes

## Finding

Let integers \(n\ge 6\), \(3\le k\le n-3\) be given. Write \(J(n,k)\) for the Johnson graph on the \(k\)-element subsets of \([n]\), joining distinct subsets with intersection of size \(k-1\). Let \(K_{n,k}\) be its clique (flag) complex, equivalently the inclusive scale-one graph-metric Vietoris–Rips complex. Permuting the ground-set labels makes its second reduced rational homology into a natural representation of \(S_n\). Put \(s=\min(k,n-k)\), and let \(S^\lambda\) denote the rational Specht representation indexed by a partition \(\lambda\) of \(n\). Then

\[
\boxed{\widetilde H_2(K_{n,k};\mathbb Q)\cong
\bigoplus_{j=1}^{s-1}S^{(n-j-2,j,1,1)}.}
\]

Every summand occurs with multiplicity one, and there are no other irreducible constituents. In particular, this homology representation has no invariant vector under the full \(S_n\)-action. The previously established integral homotopy classification gives \(K_{n,k}\simeq\bigvee^{\beta(n,k)}S^2\), where the new formula refines its number of spheres by determining the full symmetry representation.

An equivalent explicit character is as follows. If \(g\in S_n\) has \(c_\ell\) cycles of length \(\ell\), put \(a=c_1\), \(b=c_2\) and \(F_g(t)=\prod_{\ell\ge1}(1+t^\ell)^{c_\ell}\). For a formal power series \(P\), write \([t^r]P\) for the coefficient of \(t^r\). Then

\[
\begin{aligned}
\operatorname{tr}(g\mid\widetilde H_2(K_{n,k};\mathbb Q))
={}&[t^{k-1}]F_g+[t^k]F_g+[t^{k+1}]F_g-1\\
&-a\left([t^{k-1}]\frac{F_g}{1+t}+[t^k]\frac{F_g}{1+t}\right)\\
&+\binom a2[t^{k-1}]\frac{F_g}{(1+t)^2}
-b[t^{k-1}]\frac{F_g}{1+t^2}.
\end{aligned}
\]

The quotient expressions mean removal of the indicated individual fixed one-cycles or two-cycle factors before coefficient extraction. All terms are defined even if \(a=0\) or \(b=0\), since the corresponding coefficient is multiplied by zero. In the smallest case, \((n,k)=(6,3)\), the summands have shapes \((3,1,1,1)\) and \((2,2,1,1)\), of dimensions ten and nine respectively.

## Assumptions and scope

Ground-set permutations act simplicially on \(K_{n,k}\); their action on oriented simplices carries the usual sign from rearranging the vertex order. Homology has rational coefficients in the representation assertion; the connectivity and collapse statements below are integral topological statements. The range \(3\le k\le n-3\) guarantees that both maximal clique types are nondegenerate and excludes the line-graph boundary cases. The result concerns the graph-metric Rips complex at inclusive scale one only, not higher scales. The theorem asserts an isomorphism of rational representations, not a preferred equivariant basis, integral Specht-lattice splitting, or equivariant homotopy wedge.

## Proof

**1. Clique geometry and homology concentration.** An adjacent pair of \(k\)-subsets can be written \(A\cup\{x\}\), \(A\cup\{y\}\), where \(|A|=k-1\) and \(x\ne y\). Every further common neighbor either contains \(A\), or is a \(k\)-subset of \(A\cup\{x,y\}\). A common neighbor of the first type outside the original edge and one of the second type are nonadjacent. Thus every clique with at least three vertices belongs to precisely one of the maximal cliques

\[
F_A=\{A\cup\{z\}:z\in[n]\setminus A\},\qquad |A|=k-1,
\]
\[
T_B=\{B\setminus\{z\}:z\in B\},\qquad |B|=k+1.
\]

Distinct star cliques or distinct top cliques meet in at most one graph vertex; a star and a top meet in at most two. In each \(F_A\) and \(T_B\), choose any vertex as an apex. For each subset \(\tau\) of the other vertices of that facet with \(|\tau|\ge3\), in decreasing order of size remove \((\tau,\tau\cup\{\mathrm{apex}\})\). Uniqueness of containing maximal clique for every face with at least three vertices ensures these are elementary free-face collapses. The remaining simplicial complex is connected and two-dimensional, with the same full graph one-skeleton.

The graph \(J(n,k)\) is the one-skeleton of the \((n-1)\)-dimensional hypersimplex \(P_{n,k}=\{x\in[0,1]^n:\sum_i x_i=k\}\). Every two-dimensional face of this convex polytope is a triangle, obtained by leaving three coordinates variable with sum one or two. These triangles belong to \(K_{n,k}\). The two-skeleton of the boundary of \(P_{n,k}\), which is homeomorphic to \(S^{n-2}\), is simply connected because \(n\ge6\). It contains the entire one-skeleton of \(K_{n,k}\), so the additional simplices of \(K_{n,k}\) cannot create fundamental-group generators. Consequently \(K_{n,k}\) and its collapsed two-dimensional core are simply connected. They have reduced homology only in degree two, where it is a free abelian group. All subsequent equivariant Euler-character calculations therefore represent the actual rational \(\widetilde H_2\), with positive sign; no higher homology term is omitted.

**2. Equivariant Euler class.** Work in the rational representation ring of \(S_n\). Denote by \(X_r\) the permutation module on \(r\)-subsets; by \(I_{r,r+1}\) the permutation module on flags \(A\subset B\), \(|A|=r\), \(|B|=r+1\); and by \(E^{\mathrm{or}}\) the oriented edge module of \(J(n,k)\), on which reversing an edge changes its sign.

Let \(K^F\) be the union of all simplex stars \(F_A\), and \(K^T\) the union of all simplex tops \(T_B\). The stars intersect one another only at vertices, and analogously for tops. Counting a simplex's equivariant Euler class as the one-dimensional trivial representation on its stabilizer gives

\[
[\chi(K^F)]=[X_{k-1}]-[I_{k-1,k}]+[X_k],
\qquad
[\chi(K^T)]=[X_{k+1}]-[I_{k,k+1}]+[X_k].
\]

Indeed, the incidence module counts each graph vertex once for every star/top containing it; add \(X_k\) to restore every vertex once. Every edge belongs to exactly one star and one top. By the uniqueness above, the intersection \(K^F\cap K^T\) is precisely the one-dimensional Johnson graph and hence has Euler class \([X_k]-[E^{\mathrm{or}}]\). The equivariant inclusion–exclusion identity and removal of the degree-zero trivial class now give

\[
\boxed{[\widetilde H_2(K_{n,k};\mathbb Q)]
=[X_{k-1}]+[X_k]+[X_{k+1}]
-[I_{k-1,k}]-[I_{k,k+1}]+[E^{\mathrm{or}}]-[\mathbf1].}
\tag{1}
\]

This is an equality of actual and virtual representations because homology is concentrated in degree two by Step 1.

**3. Character formula.** A fixed subset of size \(r\) is a union of cycles of \(g\), so \(\chi_{X_r}(g)=[t^r]F_g(t)\). A fixed adjacent-rank flag is specified by a fixed singleton and a fixed subset of size \(r\) disjoint from it; hence \(\chi_{I_{r,r+1}}(g)=a[t^r]F_g/(1+t)\). An oriented edge of \(J(n,k)\) consists of a common \((k-1)\)-subset and two exchanged elements. The only edges fixed setwise by \(g\) arise from two individually fixed elements, with orientation sign \(+1\), or from one transposition, with orientation sign \(-1\). Therefore

\[
\chi_{E^{\mathrm{or}}}(g)
=\binom a2[t^{k-1}]\frac{F_g}{(1+t)^2}
-b[t^{k-1}]\frac{F_g}{1+t^2}.
\]

Substitution into (1) proves the displayed full-cycle-type character expression.

**4. Specht decomposition.** The Frobenius characteristic sends \(X_r\) to \(h_rh_{n-r}\), sends \(I_{r,r+1}\) to \(h_rh_1h_{n-r-1}\), and sends \(E^{\mathrm{or}}\) to \(h_{k-1}h_{n-k-1}e_2\). Here \(h_r\) and \(e_2\) are the complete and degree-two elementary symmetric functions; \(e_2=h_1^2-h_2\). Formula (1) thus becomes

\[
\begin{aligned}
\mathcal F_{n,k}={}&h_{k-1}h_{n-k+1}+h_kh_{n-k}+h_{k+1}h_{n-k-1}
-h_{k-1}h_1h_{n-k}\\
&-h_kh_1h_{n-k-1}+h_{k-1}h_{n-k-1}e_2-h_n.
\end{aligned}
\tag{2}
\]

Complementing all \(k\)-subsets identifies \(K_{n,k}\) equivariantly with \(K_{n,n-k}\), so suppose \(k\le n/2\). For any \(1\le j\le k-1\), set \(p=n-j-2\), \(q=j\). The partition \((p,q,1,1)\) is valid because \(p\ge q\) throughout this range. Its four-by-four Jacobi–Trudi determinant expands to

\[
\begin{aligned}
s_{(p,q,1,1)}={}&(h_ph_q-h_{p+1}h_{q-1})e_2
-h_1(h_ph_{q+1}-h_{p+2}h_{q-1})\\
&+(h_ph_{q+2}-h_{p+3}h_{q-1}).
\end{aligned}
\tag{3}
\]

Summing the first parenthesis over \(j=1,\ldots,k-1\) telescopes to \(h_{n-k-1}h_{k-1}-h_{n-2}\); summing the second bracket telescopes to \(h_{n-k}h_{k-1}+h_{n-k-1}h_k-h_{n-1}-h_{n-2}h_1\); and summing the third bracket telescopes to \(h_{n-k+1}h_{k-1}+h_{n-k}h_k+h_{n-k-1}h_{k+1}-h_n-h_{n-1}h_1-h_{n-2}h_2\). Using \(e_2=h_1^2-h_2\) cancels the remaining boundary terms and gives

\[
\sum_{j=1}^{k-1}s_{(n-j-2,j,1,1)}=\mathcal F_{n,k}.
\]

Under the Frobenius characteristic, Schur functions correspond bijectively to irreducible rational Specht characters. Their partitions are distinct and each appears once. This proves the decomposition and the absence of the trivial constituent \(S^{(n)}\). The complement symmetry completes the case \(k>n/2\).

## Verification

The independent standard-library program `verify_johnson_equivariant.py` enumerates the simplices of \(K_{n,k}\) directly from all star/top cliques, calculates signed Lefschetz traces by testing fixed oriented simplices, separately evaluates the fixed-subset/fixed-edge expression, and independently obtains the proposed Specht characters through Murnaghan–Nakayama border-strip recursion. It compares all three integer traces on every conjugacy class for all \(6\le n\le9\), \(3\le k\le\lfloor n/2\rfloor\): six parameter cases and 130 class comparisons. For \(n\le8\), it additionally computes complete mod-two boundary ranks for four cases and checks concentration in degree two. The checker's exact output is in `VERIFIER_OUTPUT.txt`. An additional character-only test of every class for \(10\le n\le12\) was performed, with no mismatches; it is not required by the program and does not establish the general quantifier. The proof above, not finite tests, establishes the all-parameter result.

## Relationship to prior work

Shuldiner and Oldford (2022, arXiv:2208.12710) characterize the maximal star/top cliques and their combinatorial incidences. They do not compute their clique-complex homology representation. Goyal, Shukla and Singh (2020, arXiv:2009.12130) study clique complexes of line graphs; the present range is not covered, since every \(J(n,k)\) here has an induced claw (three disjoint coordinate exchanges from a chosen vertex) and a line graph is claw-free. Iglesias and Natale (2019, arXiv:1912.09243) compute the \(S_n\)-representation of functions **on the vertices** of Johnson graphs, which consists of two-row Specht modules, whereas the present second homology consists of four-row Specht modules. The published sphere-wedge classification *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes* (2026) supplies the same domain and previously known nonequivariant homotopy type, but makes no claim about the symmetry action. The present theorem refines precisely that known homology by determining its full equivariant decomposition. Indexed searches for equivalently phrased flag complexes of hypersimplex graphs, Specht modules, and symmetric-group homology characters identified no implication of this representation statement; this is a bounded literature comparison rather than a guarantee of global novelty.

## Limitations

The calculation is rational representation theory. It does not provide a canonical integral Specht-lattice decomposition or an equivariant homotopy splitting of the sphere wedge. It concerns only scale one and central Johnson ranks, and it relies on the standard Jacobi–Trudi and Frobenius-characteristic theorems for its irreducible identification. Equivalent statements in unindexed or inaccessible literature remain a residual originality risk. The explicit finite checker is not a proof for unbounded \(n\); that proof is the uniform argument in the preceding section.

## References

1. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710, first public version 2022-08-26. See Sections 3–4 on maximal cliques and unique containing cliques.
2. S. Goyal, S. Shukla and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first public version 2020-09-25. See the introduction and Section 3.
3. R. Iglesias and M. Natale, *A Fast Fourier Transform for the Johnson graph*, arXiv:1912.09243, first public version 2019-12-18. See Section 3, Theorem 1, on vertex-function representations.
4. *Sphere-wedge collapse of scale-one Johnson-graph Rips complexes*, 2026, public research record https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sphere-wedge-collapse-of-scale-one-johnson-graph-rips-complexes--c10287ed1518 ; see the theorem and proof of the nonequivariant homotopy type.
5. The Jacobi–Trudi identity, Frobenius characteristic, and Murnaghan–Nakayama character rule (standard symmetric-function and representation-theoretic identities).
