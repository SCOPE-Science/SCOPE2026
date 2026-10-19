# Higher commuting-tuple conjugacy for finite graphical groups

## Finding

For every finite simple graph \(\Gamma=(V,E)\), finite field \(\mathbf F_q\), and integer \(k\ge 1\), the polynomial recording the simultaneous-conjugacy orbit sizes of ordered, pairwise commuting \(k\)-tuples in the graphical group \(G_\Gamma(\mathbf F_q)\) is

\[
B_{\Gamma,k}(q;t)=\sum_{U\subseteq V}(q-1)^{|U|}\left(\frac{q^k-1}{q-1}\right)^{c(U)}q^{k|E|-r(U)}t^{r(U)},
\qquad r(U)=|N[U]|-c(U).
\]

Here \(c(U)\) is the number of connected components of the induced graph \(\Gamma[U]\), with \(c(\varnothing)=0\), and \(N[U]\) is the closed neighborhood of \(U\), with \(N[\varnothing]=\varnothing\). An orbit counted by the coefficient of \(t^j\) has exactly \(q^j\) members. At \(t=1\) this is an exact formula for the number of simultaneous-conjugacy classes of commuting ordered tuples. The \(k=1\) specialization is an ordinary conjugacy-class enumeration already considered in the literature; the uniform higher-arity orbit-size formula is the result here.

The formula distinguishes higher conjugacy information for groups whose ordinary numbers of conjugacy classes agree. Let \(\Gamma_1=K_{1,3}\) and \(\Gamma_2=K_3\sqcup K_1\). Their group orders are both \(q^7\), and their ordinary conjugacy-class counts are both \(q^2(q^3+q^2-1)\); however,

\[
B_{\Gamma_1,2}(q;1)=q^5(q^6+q^3-1),\qquad
B_{\Gamma_2,2}(q;1)=q^6(q^4+q^3+q^2-q-1),
\]

whose difference is \(q^5(q-1)^3(q+1)(q^2+q+1)>0\) for every finite field. The distinction is not a claim that ordinary-class-number equivalence with unequal higher profiles was previously unknown; the contribution is its explicit realization and computation within graphical groups.

## Assumptions and scope

Fix an arbitrary total ordering of \(V\). Write each edge \(e=\{u,v\}\) with \(u<v\). Define \(G_\Gamma(\mathbf F_q)\) as the set of pairs \((x,z)\in\mathbf F_q^V\times\mathbf F_q^E\), with multiplication

\[
(x,z)(x',z')=\bigl(x+x',\,z+z'+(x_ux'_v)_{e=\{u,v\},\,u<v}\bigr).
\]

The identity is \((0,0)\), and inverses are obtained by negating \(x\) and adjusting each central edge coordinate. This is a class-at-most-two group of order \(q^{|V|+|E|}\). No restriction on graph connectivity, isolates, field characteristic, or vertex count is required. The parameter \(k\) is a positive integer. A commuting tuple is an ordered list \((g_1,\ldots,g_k)\) with all commutators trivial; simultaneous conjugation acts by the same group element on all entries. The exponent of \(t\) is the base-\(q\) logarithm of the orbit size, which is an integer by the proof.

## Proof

**Step 1: commutation and the common support.** The commutator of \((x,z)\) and \((x',z')\) has central coordinate \(x_ux'_v-x'_ux_v\) at edge \(\{u,v\}\). For a tuple of elements write its vertex coordinates as column vectors \(X_v=(x_v^{(1)},\ldots,x_v^{(k)})\in\mathbf F_q^k\). The tuple is pairwise commuting if and only if \(X_u\wedge X_v=0\) for every edge. Let \(U=\{v:X_v\ne0\}\). Adjacent nonzero columns are proportional; hence all nonzero columns within each connected component of \(\Gamma[U]\) belong to one common one-dimensional subspace of \(\mathbf F_q^k\). Conversely, this condition ensures commutation on all edges, including those crossing to zero columns. The number of possible column arrays with support exactly \(U\) is therefore

\[
(q-1)^{|U|}\bigl((q^k-1)/(q-1)\bigr)^{c(U)}.
\]

For each connected component one chooses a projective line (there are \((q^k-1)/(q-1)\) choices), then one of its \(q-1\) nonzero vectors independently at every vertex.

**Step 2: rank of the conjugation action.** For fixed vertex columns \(X=(X_v)\), conjugation by any group element with vertex coordinate \(y\in\mathbf F_q^V\) translates the \(k|E|\) central coordinates by the image of the linear map

\[
T_X:\mathbf F_q^V\longrightarrow (\mathbf F_q^k)^E,\qquad
(T_X y)_{\{u,v\}}=y_uX_v-y_vX_u
\]

(up to an irrelevant global sign). Consider the edges lying wholly in \(U\). In a component \(C\) of \(\Gamma[U]\), write \(X_v=a_vv_C\) with \(a_v\ne0\) and a fixed nonzero vector \(v_C\). Restricting \(T_X\) to the internal edges, its kernel on \(C\) consists precisely of \(y_v=\lambda_Ca_v\), one scalar per component; this follows by propagating the edge equations along paths. Thus the internal-edge block has rank \(|U|-c(U)\).

For each vertex \(w\notin U\) adjacent to \(U\), the column of \(T_X\) indexed by \(w\) is nonzero and supported on crossing edges incident to \(w\); columns corresponding to different outside vertices have disjoint edge supports. These columns are independent of each other and independent of all internal-edge outputs, because internal and crossing edge sets are disjoint. Outside vertices without neighbors in \(U\) give zero columns. It follows that

\[
\operatorname{rank}(T_X)=|U|-c(U)+|N[U]\setminus U|=|N[U]|-c(U)=r(U).
\]

This argument also covers empty support, isolated vertices, and single-vertex components.

**Step 3: orbit counting.** Simultaneous conjugation leaves every vertex column fixed, while translating central-coordinate tuples along the additive subspace \(\operatorname{im}(T_X)\). For each fixed admissible \(X\), all orbits have size \(q^{r(U)}\) and the number of distinct orbits is \(q^{k|E|-r(U)}\). Multiplication by the number of possible \(X\) from Step 1 and summation over all \(U\subseteq V\) gives the stated polynomial, with no missing conjugacy identifications.

**Step 4: explicit separation.** Substituting the four-vertex edge sets \(\{01,02,03\}\) and \(\{01,12,02\}\) into the support formula gives identical total coefficients for \(k=1\), equal to \(q^2(q^3+q^2-1)\), but the displayed distinct formulas for \(k=2\). Their difference factors as shown. Both graphical groups have four vertex and three edge coordinates, so their common order is \(q^7\).

## Verification

The accompanying standalone programs `check_graphical.py` and `check_group_orbits.py` contain independent, executable finite verifications. The first enumerates admissible vertex arrays from the pairwise exterior-product equations, computes ranks of their conjugation matrices by Gaussian elimination, and compares the results with the support formula for all \(75\) labeled graphs with at most four vertices over \(\mathbf F_2\) at \(k=2\); it also checks selected examples over \(\mathbf F_3\), a three-tuple example, and a five-vertex path. The second constructs the group multiplication directly for the two four-vertex witness graphs over \(\mathbf F_2\), exhausts all \(5632\) commuting ordered pairs in each group, and partitions them into actual conjugacy orbits. It finds \(2272\) and \(1600\) orbits respectively. All finite checks passed. The proof, not the finite experiments, establishes the theorem uniformly for arbitrary \(q\), \(k\), and \(\Gamma\).

To reproduce, run `python check_graphical.py` and `python check_group_orbits.py` with Python 3.10 or later; neither program uses external packages.

## Relationship to prior work

Rossmann (2021) defines graphical groups and studies their ordinary conjugacy-class size enumerators, corresponding to the specialization \(k=1\). Kaur, Prajapati, and Prasad (2019) introduce and analyze higher simultaneous-conjugacy invariants of finite groups, including recursive methods and examples showing that ordinary class-count equality need not persist to higher arity. Sharma and Singh (2020) develop commuting probabilities and higher simultaneous conjugacy through centralizer branching. These prior frameworks motivate the combination of graph-dependent vertex-support geometry with a complete orbit-size calculation for every arity. The present formula does not assert that these general notions or the ordinary \(k=1\) specialization are new.

## Limitations

The assertion concerns simultaneous conjugacy of pairwise commuting tuples, not arbitrary tuples or automorphism-group orbits. The formula is finite but can require summing over exponentially many vertex subsets, and does not itself yield an efficient algorithm for unrestricted large graphs. The construction presupposes the standard finite-field graphical-group model. The stated originality is assessed against the specifically identified literature; differently formulated or unindexed prior formulas remain a possible overlap risk. Independent external validation has not been performed.

## References

1. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (first public 2021-07-12); published in *Bulletin of the London Mathematical Society*, DOI:10.1112/blms.12665.
2. G. Kaur, S. Prajapati, and A. Prasad, *Simultaneous Conjugacy Classes as Combinatorial Invariants of Finite Groups*, arXiv:1905.07957 (first public 2019-05-20).
3. A. Sharma and A. Singh, *Commuting probability and simultaneous conjugacy classes of commuting tuples in a group*, arXiv:2002.01253 (first public 2020-02-04).
