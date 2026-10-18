# Star-sphere retractions and signed permutation homology of triangular-graph neighborhood complexes

## Finding
For each integer \(n\ge7\), let \(T_n=L(K_n)=J(n,2)\) be the triangular graph: its vertices are the two-subsets of \([n]\), with distinct vertices adjacent when their two-subsets intersect. Write \(X_n=\mathcal N(T_n)\) for the ordinary **open** Lovász neighborhood complex. For every \(i\in[n]\), the \(n-1\) vertices of \(T_n\) corresponding to pairs containing \(i\) span an induced subcomplex \(S_i\cong\partial\Delta^{n-2}\cong S^{n-3}\).

The inclusion of these \(n\) spheres yields an injective \(S_n\)-equivariant homomorphism
\[
\operatorname{sgn}\otimes_{\mathbb Z}\mathbb Z^{[n]}
\ \longhookrightarrow\
\widetilde H_{n-3}(X_n;\mathbb Z).
\]
The image is a direct summand of the **underlying abelian group**. The permutation representation here is the free integral permutation lattice on the \(n\) labels; no \(\mathbb Z[S_n]\)-equivariant splitting is claimed. Thus \(\widetilde H_{n-3}(X_n;\mathbb Z)\) contains at least \(n\) independent, primitive infinite-order classes, even though the ambient complex has simplices of higher dimension.

For \(n=7\), these seven classes exhaust the rational fourth homology:
\[
\widetilde H_4(X_7;\mathbb Q)
\cong \operatorname{sgn}\otimes_{\mathbb Q}\mathbb Q^{[7]}
\cong S^{(1^7)}\oplus S^{(2,1^5)}.
\]
The last equality uses the standard notation for rational Specht modules; it asserts a one-dimensional sign summand and a six-dimensional sign-twisted standard summand. No integral torsion-freeness assertion for \(X_7\) follows from this statement.

## Assumptions and scope
All graphs are finite, loopless, and undirected. A finite set \(F\subseteq V(G)\) is a simplex of \(\mathcal N(G)\) precisely when there exists a vertex \(v\in V(G)\) **distinct from every vertex of \(F\)** and adjacent to all its elements; in a loopless graph the distinctness is automatic. Coefficients are integral except in the explicit rational corollary. The symmetric group \(S_n\) permutes \([n]\), hence the two-subsets and the complex \(X_n\). All assertions about retractions and split injections apply to **every integer \(n\ge7\)**, without an upper bound. The exhaustiveness assertion concerns \(n=7\) only.

For \(i\in[n]\), define its spoke set \(A_i=\{\{i,j\}:j\in[n]\setminus\{i\}\}\). The complex \(S_i\) is the collection of proper subsets of \(A_i\). We orient its fundamental cycle \(z_i\) as the alternating boundary of the formal \((n-2)\)-simplex whose vertices are the \(n-1\) spokes listed by increasing value of their other endpoint.

## Proof
**1. The embedded spheres.** Each proper subset \(F\subsetneq A_i\) omits at least one spoke \(\{i,j\}\). This omitted spoke is adjacent in \(T_n\) to every element of \(F\), so \(F\in X_n\). By contrast, the entire set \(A_i\) has no common neighbor. A proposed neighbor \(\{i,j\}\) is not adjacent to itself, while a pair avoiding \(i\) intersects at most two of the \(n-1\ge6\) spokes. Hence the induced complex on \(A_i\) is exactly \(\partial\Delta^{n-2}\), and \(z_i\) defines a reduced integral homology class in dimension \(n-3\).

**2. Explicit retractions.** Fix \(i\) and choose any three distinct labels \(B_i=\{b_1,b_2,b_3\}\subset[n]\setminus\{i\}\), in a fixed order. Define a map on vertices of \(X_n\), which are edges \(e\) of \(K_n\), by
\[
r_i(e)=\begin{cases}
e,&i\in e,\\
\{i,b(e)\},&i\notin e,
\end{cases}
\qquad
b(e)=\text{the first label of }(b_1,b_2,b_3)\text{ not in }e.
\]
Such a label exists because \(e\) has only two endpoints. It remains to prove that \(r_i\) is simplicial with target the **boundary** \(S_i\), not the full simplex.

Each simplex of \(X_n\) lies in the open neighborhood \(N_{T_n}(\{u,v\})\) of some \(\{u,v\}\). If \(i\in\{u,v\}\), say \(u=i\), all the spokes in this neighborhood omit \(\{i,v\}\), and every other vertex there has the form \(\{v,a\}\) with \(i\notin\{v,a\}\). Its image under \(r_i\) also omits \(\{i,v\}\), since \(b(\{v,a\})\ne v\). Thus the entire image omits one spoke. If instead \(i\notin\{u,v\}\), the neighborhood contains precisely the two spokes \(\{i,u\},\{i,v\}\), together with pairs avoiding \(i\). All image spokes therefore have other endpoint in \(\{u,v\}\cup B_i\), a set of at most five labels. As \(n-1\ge6\), the image again omits a spoke. Hence \(r_i:X_n\to S_i\) is a simplicial map. It fixes every vertex of \(S_i\), so it is a simplicial retraction.

**3. Pairwise annihilation.** If \(j\ne i\), the spoke set \(A_j\) contains just one vertex containing \(i\), namely \(\{i,j\}\). It maps to itself; all other spokes in \(A_j\) map into the three spokes with other endpoint in \(B_i\). Thus \(r_i(S_j)\) lies in a simplex on at most four vertices of \(S_i\). Since \(S_i\) is a sphere of dimension \(n-3\ge4\), the induced map on its reduced \((n-3)\)-homology is zero. Together with \(r_i\vert_{S_i}=\mathrm{id}\), this gives
\[
(r_i)_*[z_j]=\delta_{ij}[z_i].
\]
Consequently the composite of the inclusion \(\mathbb Z^n\to\widetilde H_{n-3}(X_n;\mathbb Z)\) and the combined retraction map back to \(\mathbb Z^n\) is the identity. This proves integral linear independence, infinite order, primitivity, and splitting as abelian groups without a computational or rationality assumption.

**4. The permutation action.** The group \(S_n\) sends \(S_i\) to \(S_{\sigma(i)}\). Reordering the \(n-1\) spokes induces orientation degree
\[
\deg(\sigma:S_i\to S_{\sigma(i)})
=\operatorname{sgn}(\sigma)(-1)^{i+\sigma(i)}.
\]
Indeed, deleting one position from an ordered permutation changes its sign by the displayed parity. Upon replacing \([z_i]\) with \(w_i=(-1)^i[z_i]\), one obtains \(\sigma w_i=\operatorname{sgn}(\sigma)w_{\sigma(i)}\). The embedded integral lattice is therefore precisely the sign twist of the natural permutation lattice. The individual retractions depended on the auxiliary ordered triples \(B_i\), so this does **not** prove a group-equivariant retraction.

**5. Exactness over \(\mathbb Q\) at seven labels.** The 21 vertices of \(T_7\) are the two-subsets of \([7]\). Its 21 neighborhoods each have 10 vertices. Enumerating every nonempty subset of these neighborhoods, with duplicate faces identified, gives 18,494 distinct nonempty simplices and the face counts in dimensions zero through nine
\[
(21,210,1190,3780,5187,4410,2520,945,210,21).
\]
Exact binary elimination on the full simplicial boundary matrices gives \(\operatorname{rank}_{\mathbb F_2}(\partial_4)=2534\) and \(\operatorname{rank}_{\mathbb F_2}(\partial_5)=2646\). Therefore
\[
\dim_{\mathbb F_2}H_4(X_7;\mathbb F_2)
=5187-2534-2646=7.
\]
The reproducible code below reconstructs all these faces from the graph and verifies the ranks with two opposite pivot conventions. By the universal coefficient theorem, \(\dim_{\mathbb Q}H_4(X_7;\mathbb Q)\le7\). The integral retractions already embed \(\mathbb Z^7\), so rational dimension is at least seven. Equality follows, and the displayed rational \(S_7\)-character is the full one. The decomposition into the sign line and sign-twisted standard representation follows from \(\mathbb Q^{[7]}=\mathbf1\oplus S^{(6,1)}\) and \(S^{(6,1)}\otimes\operatorname{sgn}\cong S^{(2,1^5)}\).

## Verification
The accompanying standalone `VERIFY.py` uses only the Python standard library. Execute `python3 VERIFY.py` in the extracted package directory. It independently generates graph neighborhoods, tests the explicit simplicial retractions and off-diagonal null maps for \(7\le n\le11\), checks the signed orientation formula on a generating set of \(S_7\), and exhaustively constructs the 18,494 simplices of \(X_7\). It computes both mod-two boundary ranks using two pivot conventions and independently confirms that the seven star cycles are linearly independent modulo boundaries over \(\mathbb F_2\). The infinitely many cases are proved by the combinatorial two-case argument above, not inferred from finite testing. The rational equality uses exact mod-two ranks and the universal coefficient inequality; it does not use approximate linear algebra.

## Relationship to prior work
The original neighborhood-complex theory introduced by Lovász, and Matsushita's study of their fundamental groups, motivate the objects but do not calculate the star-sphere summand for triangular graphs. General clique-inclusion methods, including the dimension bound in Matsushita–Wakatsuki, give nonvanishing in a suitable degree from an individual large clique, but do not show \(n\) independent integral sphere classes, a simultaneous abelian-group splitting, or their full signed permutation action. Fröberg's work on Stanley–Reisner rings of neighborhood complexes treats specific graph families rather than triangular graphs.

A publicly posted finite homology calculation, *Mixed-dimensional mod-two neighborhood homology first appears at* \(T_7\), establishes \(\dim_{\mathbb F_2}H_4(X_7;\mathbb F_2)=7\) but explicitly does not determine integral splittings, symmetric-group representations, or any case beyond seven labels. Our independent computation agrees with that rank. The present result instead constructs an integral infinite-family split subgroup and identifies the **entire rational homology representation in that degree at seven labels**. These are not consequences of the published finite Betti vector alone.

## Limitations
For \(n>7\) no claim is made that the displayed \(n\)-dimensional subgroup exhausts the homology, nor that its splitting can be chosen \(S_n\)-equivariantly over \(\mathbb Z\). At \(n=7\), only the rational fourth-homology representation is completely identified: odd-primary torsion in integral homology, homology in other degrees, attaching maps, and the full homotopy type are outside the claim. The threshold \(n\ge7\) is sufficient for the explicit three-anchor retractions and is **not** asserted to be optimal. Exhaustive computations do not certify unsearched mathematical literature; general duality and clique-inclusion theorems remain important overlap comparators.

## References
1. L. Lovász, *Kneser's conjecture, chromatic number, and homotopy*, Journal of Combinatorial Theory, Series A 25 (1978), 319–324, DOI 10.1016/0097-3165(78)90022-5.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1, first publicly posted 2012-10-10; Journal of Mathematical Sciences, University of Tokyo 24 (2017), 321–353. The paper's listed primary MSC is 55Q05.
3. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639v1 (2023); Journal of Combinatorial Theory, Series A 211 (2025), article 105978.
4. R. Fröberg, *Stanley–Reisner rings of neighborhood complexes and linear resolutions*, Journal of Algebraic Combinatorics 63 (2026), article 56, DOI 10.1007/s10801-026-01530-x.
5. *Mixed-dimensional mod-two neighborhood homology first appears at* \(T_7\), publicly posted research record, 2026-10-11, published-finding corpus/2026, identifier `5026f3f1e8ec`, `RESULT.md` (the earlier mod-two finding; no integral symmetry or general-family claim).
