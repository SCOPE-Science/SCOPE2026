# Weighted Tutte character spectra of radical-square-zero quiver unit groups

## Finding
Let \(Q\) be any finite quiver with \(n\ge1\) vertices, including possible loops, parallel arrows, oppositely oriented pairs, and oriented cycles. Let \(q\) be a prime power, and let \(U_Q=(\mathbb F_qQ/J^2)^\times\), where \(J\) is the arrow ideal. Let \(L\) be the number of loops, counting multiplicity. For each unordered pair \(e=\{u,v\}\) of distinct vertices, let \(a_e\) be the total number of arrows in both directions. Form a simple undirected graph \(\Gamma\) whose edges \(E\) are exactly the pairs with \(a_e>0\). Put \(R=q-1\), and for \(S\subseteq E\) define the spanning graphic rank \(r(S)=n-c(S)\), where \(c(S)\) counts connected components, including isolated vertices, and the cycle nullity \(\beta(S)=|S|-r(S)\). Set \(B_a(q)=1+q+\cdots+q^{a-1}\) for positive integers \(a\).

**Theorem.** For \(q>2\), the generating polynomial for the multiplicities of the irreducible complex character degrees of \(U_Q\) is
\[
\boxed{\mathcal C_{Q,q}(z)=\sum_{j\ge0} |\{\chi\in\operatorname{Irr}(U_Q):\chi(1)=R^j\}|z^j
=q^L\sum_{S\subseteq E}R^{c(S)+\beta(S)}\left(\prod_{e\in S}B_{a_e}(q)\right)z^{r(S)}.}
\]
Every irreducible degree is a power of \(q-1\), and the degrees \(1,R,\ldots,R^{r(E)}\) all occur. The formula determines the complete degree distribution, not merely the number of conjugacy classes. It depends on arrow multiplicities only through \(L\) and the unordered totals \(a_e\); changing arrow orientations does not change it. Equivalently it holds for any finite-dimensional split basic unital associative algebra whose Jacobson radical squares to zero, with \(a_e=\dim(e_uJe_v)+\dim(e_vJe_u)\) and \(L=\sum_u\dim(e_uJe_u)\).

For \(q=2\), the diagonal torus is trivial, so \(U_Q\) is abelian and has exactly \(2^{L+\sum_{e\in E}a_e}\) irreducible characters, all of degree one. Evaluating the displayed polynomial at \(z=1\) gives the same total, but its formal powers of \(R=1\) no longer distinguish degrees.

Define the multivariate random-cluster polynomial \(Z_\Gamma(t,\{w_e\})=\sum_{S\subseteq E}t^{c(S)}\prod_{e\in S}w_e\). Then the precise graph-theoretic specialization is
\[
\boxed{\mathcal C_{Q,q}(z)=q^L R^{-n}z^n Z_\Gamma\left(\frac{R^2}{z},\{q^{a_e}-1\}_{e\in E}\right),}
\]
understood as a polynomial identity after cancellation of Laurent factors. In particular, for a loopless quiver with at most one arrow between each unordered vertex pair, with ordinary Tutte polynomial \(T_\Gamma\),
\[
\boxed{\mathcal C_{Q,q}(z)=R^{n-r(E)}z^{r(E)}T_\Gamma(1+R/z,q).}
\]
For a loopless underlying forest with \(m\) edges of multiplicity one, this reduces to \(R^{n-m}(R+z)^m\). In this family the distribution depends only on \(n\) and \(m\), not on the forest shape.

## Assumptions and scope
All groups and algebras are finite. A quiver has a finite set of labeled vertices and finitely many arrows. The quotient \(\mathbb F_qQ/J^2\) has vector-space dimension \(n+L+\sum_ea_e\), regardless of any directed cycles. Irreducible characters are ordinary complex characters, not modular characters. The graph \(\Gamma\) has no graph-theoretic loops and records positive unordered arrow-class dimensions; algebra loops contribute the separate scalar factor \(q^L\). For an edge-free graph, sums and products over edges have their usual empty-set values. The theorem applies also to one vertex and to disconnected graphs.

## Proof
Write \(A=\mathbb F_qQ/J^2\). The vertex idempotents split \(A=D\oplus J\), with \(D\cong\mathbb F_q^n\) and \(J^2=0\). Thus its unit group is the semidirect product \(U_Q=N\rtimes T\), where \(N=1+J\) is isomorphic to the additive group of \(J\), and \(T=D^\times\cong(\mathbb F_q^\times)^n\). Both \(N\) and \(T\) are abelian. Fix a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\). Using a chosen basis of arrows, every \(\lambda\in J^*\) parametrizes exactly one linear character \(\chi_\lambda(1+x)=\psi(\lambda(x))\) of \(N\). The fixed nontrivial additive character gives a perfect pairing over \(\mathbb F_q\); no choice of basis changes the counting.

Conjugation by \(t=(t_v)_{v\in V}\in T\) scales the arrow space from \(u\) to \(v\) by \(t_u/t_v\). Consequently \(t\) fixes \(\chi_\lambda\) if and only if \(t_u=t_v\) for every unordered edge class \(e=\{u,v\}\) on which \(\lambda\) is nonzero. Loops impose no stabilizer condition. Let \(S(\lambda)\subseteq E\) be the set of nonzero unordered arrow classes. Its torus stabilizer is precisely the subtorus constant on the connected components of \((V,S(\lambda))\), so
\[
|T_\lambda|=R^{c(S(\lambda))},\qquad |T:T_\lambda|=R^{r(S(\lambda))}.
\]
There are exactly \(q^L\prod_{e\in S}(q^{a_e}-1)\) dual vectors \(\lambda\) having \(S(\lambda)=S\); each of the \(a_e\)-dimensional off-diagonal dual blocks must be nonzero exactly on \(S\), while the \(L\) loop coordinates are free. The number of \(T\)-orbits of such characters is this cardinality divided by \(R^{r(S)}\).

Because \(T_\lambda\) fixes \(\chi_\lambda\), that character extends to the inertia group \(N\rtimes T_\lambda\) by \(\widetilde\chi_\lambda(nt)=\chi_\lambda(n)\). Every irreducible complex representation of the abelian group \(T_\lambda\) is one-dimensional, and there are exactly \(R^{c(S)}\) of them. The finite-group little-group/Clifford correspondence for an abelian normal subgroup states that induction of these extensions (twisted by linear characters of \(T_\lambda\)) produces every irreducible representation of \(U_Q\), without duplication when one dual orbit representative is chosen. Each induced character has degree \(R^{r(S)}\). Hence the number of irreducible characters arising from supports \(S\) is
\[
\frac{q^L\prod_{e\in S}(q^{a_e}-1)}{R^{r(S)}}\,R^{c(S)}
=q^L R^{c(S)+|S|-r(S)}\prod_{e\in S} B_{a_e}(q)
=q^L R^{c(S)+\beta(S)}\prod_{e\in S} B_{a_e}(q).
\]
Summing over all supports proves the displayed polynomial. For \(q>2\), distinct exponents give distinct character degrees. For every rank between zero and \(r(E)\), a subset of a spanning forest realizes that rank, so each listed degree occurs.

The random-cluster form follows from \(c(S)=n-r(S)\) and \(R B_{a_e}(q)=q^{a_e}-1\). For a simple support graph with all \(a_e=1\), apply the subset expansion \(T_\Gamma(x,y)=\sum_{S\subseteq E}(x-1)^{r(E)-r(S)}(y-1)^{|S|-r(S)}\) with \(x=1+R/z\) and \(y=q=1+R\). For a forest, \(r(S)=|S|\) and the binomial theorem gives \(R^{n-m}(R+z)^m\). If \(q=2\), then \(T=1\) and \(N\) is abelian, giving the separate assertion.

A second global consistency check is the character-degree-squares identity. With \(d=L+\sum_ea_e\), the formula yields
\[
\sum_{\chi\in\operatorname{Irr}(U_Q)}\chi(1)^2
=q^L\sum_{S\subseteq E}R^{n+|S|}\prod_{e\in S}B_{a_e}(q)
=R^n q^L\prod_{e\in E}(1+R B_{a_e}(q))
=R^nq^d=|U_Q|.
\]
This also handles empty edge sets.

## Verification
The supplied standalone `verify.py` enumerates the group law directly, constructs its conjugacy classes from finite generators, separately enumerates the torus action on radical-dual vectors, and compares the resulting class count and character-degree distribution against the theorem. It verifies 19 finite-field configurations, including \(\mathbb F_4\), loop arrows, repeated arrows, opposite arrows, connected and disconnected quivers, a directed triangle, and a four-vertex cycle support. All tested cases satisfy the character-degree-squares identity. Execute `python verify.py` with standard Python; output ends with `VERIFY_OK 19 direct conjugacy censuses, diagonal-dual orbit censuses, degree-sum checks`.

For a directed three-cycle over \(\mathbb F_3\), the multiplicities at degrees \(1,2,4\) are respectively \(8,12,10\). Their degree-squared sum is \(8+12\cdot4+10\cdot16=216=|U_Q|\), and direct enumeration gives 30 conjugacy classes. For a pair of vertices with one arrow in each direction over \(\mathbb F_4\), the counts are nine degree-one and fifteen degree-three characters; the group has order 144. These finite checks corroborate but do not replace the general proof.

## Relationship to prior work
The argument uses the classical little-group method for a finite abelian normal subgroup and the standard subset expansion of the Tutte polynomial; neither foundational tool is claimed as new. Halasi (2006) proves that irreducible characters of unit groups of general finite DN-algebras are induced from linear characters of subalgebra unit groups, extending Szegedy's earlier monomiality theorem; he proves the possible degrees have the form \(q^r(q-1)^s\), but does not enumerate the multiplicity at each degree for the square-zero quiver family. The present formula evaluates the multiplicities rather than just proving monomiality or identifying the possible degree shape. André and Dias (arXiv:1910.14639v1, 2019) study induction of smooth representations of unit groups of split basic algebras over non-Archimedean local fields; their field and their representation-theoretic conclusion differ from the explicit character-degree enumeration here. Bilen Can (arXiv:2105.09826v1, 2021) studies automorphisms and torus-action complexity of incidence monoids, not ordinary complex character multiplicities of the associated finite unit groups. Khrypchenko and Siciliano (arXiv:2302.01868v1, 2023) determine identities and derived lengths of incidence-algebra unit groups, a different invariant.

The precise asserted contribution is an explicit weighted-graphic/Tutte character-multiplicity formula, covering arbitrary finite quivers including loops and opposing arrows, and its exact orientation-invariance consequence. The overlap assessment is relative to inspected literature and accessible prior records; no claim of global publication priority or independent certification is made.

## Limitations
The theorem requires a split basic algebra with square-zero radical. If the radical has nonzero products, the unipotent subgroup need not be abelian, and the present proof and formula do not extend unchanged. It gives degree multiplicities, not explicit character values or tensor-product decompositions. The random-cluster expression is an exact evaluation, not an algorithm polynomial in arbitrary graph size. A more general published theorem on characters of torus-by-abelian groups might imply the formula after specializing to these weights; that priority risk remains. Szegedy's 1996 original article was not fully available for inspection, although its stated character-degree shape and monomiality result were compared via the inspected Halasi paper. The computations cover only the stated finite cases. Independent mathematical audit has not been performed.

## References
1. C. A. M. André and J. Dias, *Smooth representations of unit groups of split basic algebras over non-Archimedean local fields*, arXiv:1910.14639v1 (first public 2019-10-31), https://arxiv.org/abs/1910.14639.
2. M. Bilen Can, *Incidence Monoids: Automorphisms and Complexity*, arXiv:2105.09826v1 (first public 2021-05-20), https://arxiv.org/abs/2105.09826.
3. M. Khrypchenko and S. Siciliano, *Identities and derived lengths of finitary incidence algebras and their group of units*, arXiv:2302.01868v1 (first public 2023-02-03), https://arxiv.org/abs/2302.01868.
4. Z. Halasi, *On the characters of the unit group of DN-algebras*, Journal of Algebra 302 (2006), 678–685; author-open PDF https://zhalasi.web.elte.hu/papers/02.dn.pdf. The paper cites the earlier monomiality theorem of B. Szegedy.
5. Standard finite-group Clifford/little-group correspondence for an abelian normal subgroup; standard graphic-matroid subset expansion of the Tutte polynomial (used as established tools, not new claims).
