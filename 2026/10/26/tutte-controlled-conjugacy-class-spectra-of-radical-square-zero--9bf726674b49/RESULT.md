# Tutte-controlled conjugacy-class spectra of radical-square-zero quiver unit groups

## Finding

Let \(Q=(V,E)\) be any finite quiver with \(n=|V|\geq1\) vertices and \(m=|E|\) labelled arrows, allowing loops and parallel arrows, and let \(q\) be any prime power. Let \(J\) denote the arrow ideal, set \(A=\mathbb F_qQ/J^2\), and write \(U=A^\times\). Let \(G\) be the undirected multigraph obtained by forgetting arrow orientations. Define \(t=q-1\). For every spanning edge set \(S\subseteq E\), set \(c(S)\) equal to the number of components of \((V,S)\), \(r(S)=n-c(S)\), and \(\beta(S)=|S|-r(S)\). Loops count as edges but do not change components.

Define the two-variable class-spectrum polynomial \(\Phi_{G,q}(X,Y)\) by assigning a monomial \(X^aY^b\) to each conjugacy class in \(U\) whose size admits the canonical group-action factorization \(q^a t^b\), as specified in the proof. Its coefficients count classes; if \(q=2\), factors \(t^b=1\) should be combined to recover the ordinary class-size histogram. Then

\[
\boxed{\displaystyle
\Phi_{G,q}(X,Y)=
\sum_{S\subseteq E}t^{\beta(S)}Y^{r(S)}
\sum_{R\subseteq E\setminus S}
X^{m-|S|-|R|}(1-X)^{|R|}t^{c(S\cup R)}.}
\]

In particular, the entire class-size spectrum depends only on the cycle matroid of \(G\) and \(c(G)\), not on the orientation of any arrow. More precisely, \(t^{-c(G)}\Phi_{G,q}(X,Y)\) is an invariant of that matroid (as a polynomial identity after the indicated normalization). Specializing to the total number \(k(U)\) of conjugacy classes gives

\[
\boxed{\displaystyle k(U)=\Phi_{G,q}(1,1)=t^{c(G)}T_G(q,q),}
\]

where \(T_G\) is the ordinary Tutte polynomial of the multigraph. This also counts ordinary irreducible complex characters of the finite group \(U\).

For any forest with \(m\) edges and \(c\) components, the **entire** spectrum has the closed form

\[
\boxed{\Phi_{G,q}(X,Y)=t^c\bigl(1+Y+(t-1)X\bigr)^m.}
\]

For a cycle \(C_\ell\), allowing the loop case \(\ell=1\) and two parallel edges when \(\ell=2\), set \(\lambda_+=1+(t-1)X\) and \(\lambda_-=1-X\). Then

\[
\boxed{\displaystyle
\Phi_{C_\ell,q}(X,Y)
=(\lambda_++Y)^\ell+(t-1)(\lambda_-+Y)^\ell
-tY^\ell+t^2Y^{\ell-1}.}
\]

A connected unicyclic graph whose unique cycle has length \(\ell\) and whose remaining \(b\) edges are bridges has spectrum \((1+Y+(t-1)X)^b\Phi_{C_\ell,q}(X,Y)\). Disjoint components multiply their spectrum polynomials.

## Assumptions and scope

The field \(\mathbb F_q\) is arbitrary, including characteristic two. The algebra uses the quotient by all paths of length two or more, not the unrestricted path algebra when directed paths of length two exist. The term *conjugacy* means conjugation inside the finite unit group \(A^\times\), not primary conjugacy in a semigroup, and not commutation of arbitrary additive algebra elements. The group has order \(|U|=t^nq^m\). The spectrum variables \(X,Y\) are formal class-size markers, not field elements.

A graph with isolated vertices or loops is included. If a class size is \(q^a t^b\), the canonical exponents are \(a=m-|E_0(d)|\) and \(b=r(S)\), where \(E_0(d)\) and \(S\) are defined below. At \(q>2\) these factors are multiplicatively independent because \(q\) and \(q-1\) are coprime, so different exponent pairs give different class sizes; at \(q=2\), all \(b\)-markers correspond to a factor of one.

## Proof

Every unit has a unique expression \(D(d)+N(u)\), where \(d\in(\mathbb F_q^\times)^V\), \(u\in\mathbb F_q^E\), and \(D\) and \(N\) are the vertex and arrow coordinates. For an arrow \(e:i\to j\), the arrow coordinate of a product is \(d_i v_e+u_e s_j\). The square-zero property of the arrow ideal makes the multiplication complete.

Fix the diagonal vector \(d\). Conjugation preserves it because the diagonal torus is abelian. Write

\[
E_0(d)=\{e:i\to j\mid d_i=d_j\}.
\]

Conjugation by \(1+N(v)\) changes the \(e\)-coordinate by a nonzero scalar multiple of \((d_j-d_i)v_e\). Consequently it eliminates every coordinate with \(e\notin E_0(d)\), while leaving the coordinates of \(E_0(d)\) unchanged. Those eliminated coordinates contribute exactly \(q^{m-|E_0(d)|}\) to each resulting conjugacy-class size.

On the surviving coordinates, diagonal conjugation sends \(u_e\) to \((s_i/s_j)u_e\), with \(s\in(\mathbb F_q^\times)^V\). For a fixed **exact nonzero support** \(S\subseteq E_0(d)\), there are \(t^{|S|}\) vectors. The diagonal elements fixing one such vector are precisely those satisfying \(s_i=s_j\) on every edge of \(S\), hence exactly \(t^{c(S)}\) stabilizers. Thus each diagonal orbit has size \(t^{n-c(S)}=t^{r(S)}\), and the number of distinct orbits with support \(S\) is \(t^{|S|-r(S)}=t^{\beta(S)}\). Multiplying by the eliminated-coordinate contribution, a class indexed by \((d,S)\) has size

\[
q^{m-|E_0(d)|}t^{r(S)}.
\]

This proves the manifestly nonnegative expression

\[
\Phi_{G,q}(X,Y)=
\sum_{d\in(\mathbb F_q^\times)^V}
X^{m-|E_0(d)|}
\sum_{S\subseteq E_0(d)}t^{\beta(S)}Y^{r(S)}.
\]

To obtain the subset formula in the finding, interchange the sum over \(d\) and \(S\). With the equality indicator \(\epsilon_e(d)=\mathbf 1_{\{d_i=d_j\}}\), use

\[
X^{m-|E_0(d)|}
=\prod_{e\in E}\bigl(X+(1-X)\epsilon_e(d)\bigr).
\]

For \(S\subseteq E_0(d)\), factors from \(S\) equal one. Expanding the product over remaining edges selects a further disjoint set \(R\subseteq E\setminus S\). The condition that \(d\) is constant on every edge of \(S\cup R\) leaves exactly \(t^{c(S\cup R)}\) diagonal vectors, proving the displayed two-subset expression. Every exponent depends only on \(|S|,|R|,r(S),r(S\cup R),n,m\), proving matroid dependence up to the factor for isolated components.

At \(X=Y=1\), only \(R=\varnothing\) survives (using \(0^0=1\) for the empty selection), so

\[
k(U)=\sum_{S\subseteq E}t^{\beta(S)+c(S)}.
\]

By the spanning-subset definition

\[
T_G(x,y)=\sum_{S\subseteq E}(x-1)^{r(E)-r(S)}(y-1)^{|S|-r(S)},
\]

and since \(r(E)=n-c(G)\), substitution \(x=y=q=t+1\) gives exactly \(k(U)=t^{c(G)}T_G(q,q)\).

For a forest, choose an endpoint leaf of a pendant edge. Once the old diagonal labels are fixed, its new vertex label is equal to the incident old label in one way, contributing \(1+Y\) for the new edge's absent/present support, or unequal in \(t-1\) ways, contributing \(X\). Each new tree edge therefore multiplies the spectrum by \(1+Y+(t-1)X\). Every isolated root contributes \(t\), yielding the forest formula. The same argument gives the bridge factor and disjoint-component multiplication.

For the cycle formula, separate supports \(S\) which are proper subsets of the \(\ell\) cyclic edges, from the full support. A proper \(S\) of cardinality \(s\) is a forest with \(r(S)=s\) and \(\beta(S)=0\). Contracting it produces a cyclic edge system with \(L=\ell-s\) edges. The sum of \(X^{\#\text{unequal adjacent labels}}\) over all \(t\)-colorings of this cycle is the trace of the \(t\)-by-\(t\) transfer matrix with diagonal entries one and off-diagonal entries \(X\), namely

\[
\lambda_+^L+(t-1)\lambda_-^L.
\]

The formula also holds for \(L=1\), where the remaining edge is a loop after contraction. Summing \(\binom{\ell}{s}Y^s\) times these contributions for \(0\le s<\ell\) gives the two binomial expressions with \(-tY^\ell\). The full support contributes \(t^{\beta(E)}t^{c(E)}Y^{r(E)}=t^2Y^{\ell-1}\), completing the formula, including cycles of length one or two.

## Verification

A standalone Python checker independently enumerates the finite unit group using the diagonal-and-arrow multiplication law, computes every conjugacy orbit directly by all group conjugators, and compares its class-size histogram against a separately implemented graph-support formula. It verifies 17 graph/field configurations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); among them are loops, parallel edges, directed cycles, forests, and a four-cycle. It also independently checks the closed forest formula in three instances and the closed cycle formula for eight cycle/field pairs. Running `python3 verify.py` prints `ALL_QUIVER_UNIT_TUTTE_CLASS_AND_SPECTRUM_CHECKS_PASSED 17 forest_3 cycle_8`. The embedded `verify_output.txt` records the full small-case class-size histograms. Computations are finite checks, not the proof for arbitrary parameters.

## Relationship to prior work

Can, Casimiro, and Malheiro investigate incidence monoids and conjugacy relations for bipartite posets, including torus/unipotent decompositions and twisted group conjugacy, in arXiv:2208.01073 (first posted 2022-08-01). These results motivate the finite-field unit-group class-counting question, but their checked conjugacy theorems are not a formula for the complete finite-field class-size distribution of arbitrary radical-square-zero quivers.

Rossmann's 2022 article studies **different** graph-indexed nilpotent groups, defined through graph-associated class-two Lie structures. In particular, its edgeless-graph group is additive of order \(q^n\), while the present edgeless-quiver unit group is \((\mathbb F_q^\times)^n\). Its conjugacy polynomials therefore do not specialize to the present spectrum.

Existing additive algebra commutator-fiber and centralizer calculations, including calculations for Kronecker path algebras, concern commutation in the entire additive algebra, not conjugacy-class sizes of its unit group. The scalar class-number formula alone is a simple specialization of the subset method; the main result here is the **complete** two-variable class-size spectrum, its graph-matroid invariance, and the closed forest/unicyclic classifications. The Tutte and transfer-matrix identities used in the proof are classical and are not claimed as new methods.

## Limitations

No classification of irreducible character **degrees** is supplied: equality of the numbers of characters does not determine their degrees. The polynomial is not asserted to distinguish quivers or groups up to isomorphism. For \(q=2\), formally distinct \(Y\)-exponents represent the same integer factor one and must be combined for actual size multiplicities. No formula for the unrestricted path algebra, without the radical-square-zero quotient, is claimed. An equivalent formula in the broader literature on torus-by-vector finite groups or toric graph actions may predate this result; the documented source search is not a proof of historical uniqueness.

## References

1. M. B. Can, A. Casimiro, and A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets*, arXiv:2208.01073 (initial submission 2022-08-01), sections 2 and 7, especially Theorem 7.2 and Corollary 7.3.
2. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bulletin of the London Mathematical Society 54 (2022), 1923–1943, DOI:10.1112/blms.12665, sections 1–4.
3. D. Kaur, U. B. Sharma, and A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493 (2020), background for finite-field triangular group conjugacy enumeration.
4. Classical Tutte-polynomial spanning-subset definition and the elementary Potts-model transfer-matrix identity, used as standard tools rather than priority claims.
