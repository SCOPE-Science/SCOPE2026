# Centralizer-rank polynomials of toric and complexity-one incidence monoids

## Finding

Let \(P\) be a finite poset whose strict chains have at most two elements, let \(G=(V,E)\) be its undirected Hasse graph, and let \(A=I(P,\mathbb F_q)\) be its incidence algebra over an arbitrary finite field of order \(q\). Put \(n=|V|\), \(m=|E|\), and \(c=k_G(E)\), the number of connected components (including isolated vertices). For \(a\in A\), define \(C_A(a)=\{b\in A:ab=ba\}\) and \(\rho(a)=\dim_{\mathbb F_q}A-\dim_{\mathbb F_q}C_A(a)\). The centralizer-rank polynomial is
\[
\mathcal C_{G,q}(z)=\sum_{a\in A}z^{\rho(a)}.
\]

**General graphic-matroid theorem.** For an edge set \(F\subseteq E\), write \(r(F)=n-k_G(F)\), the rank of \(F\) in the graphic matroid. Then
\[
\boxed{\displaystyle
\mathcal C_{G,q}(z)=
\sum_{\substack{S,T\subseteq E\\S\cap T=\varnothing}}
(q-1)^{|S|}\,z^{r(S)}(qz)^{m-|S|-|T|}
(1-qz)^{|T|}\,q^{n-r(S\cup T)}.}
\]
In particular, the normalized polynomial \(q^{-c}\mathcal C_{G,q}(z)\) depends **only** on the cycle matroid of \(G\) and on \(q\), not on the particular incidence poset or edge orientation.

**Forest law.** If \(G\) is a forest (allowing isolated vertices), then
\[
\boxed{\mathcal C_{G,q}(z)=q^c\bigl(1+(q^2-1)z\bigr)^m.}
\]
Consequently, for each \(0\le j\le m\), exactly \(q^c\binom mj(q^2-1)^j\) algebra elements have centralizer dimension \(n+m-j\).

**Single-cycle law.** If \(G\) is connected and has exactly one cycle, necessarily of even length \(\ell\ge4\), set \(P_q(z)=1+(q^2-1)z\). Then
\[
\boxed{\displaystyle
\mathcal C_{G,q}(z)=P_q(z)^{m-\ell}
\left[P_q(z)^\ell+(q-1)(1-z)^\ell
+q(q-1)^\ell\bigl(z^{\ell-1}-z^\ell\bigr)\right].}
\]
Thus every centralizer size and multiplicity in a connected height-two unicyclic incidence algebra is determined by the number of cover relations, the unique cycle length, and the field order. In both cases the formulas are valid in all finite characteristics.

## Assumptions and scope

A strict chain means a sequence of distinct comparable vertices. The two-element-chain condition ensures that products of off-diagonal incidence-basis elements vanish; this excludes comparability paths of length two. The Hasse graph is bipartite between minimal and maximal elements, except for isolated vertices, so its cycles are even. No restriction on \(q\) beyond being a prime power is required. The polynomial counts all elements of the associative algebra, not only its units. The centralizer is a vector subspace, so its cardinality is \(q^{n+m-\rho(a)}\).

The forest formula includes \(m=0\), when the incidence algebra is commutative and \(\mathcal C_{G,q}=q^n\). The single-cycle formula requires connectedness; for disconnected height-two graphs the general formula applies, and componentwise products may be used.

## Proof

**1. Commutator matrix and its rank.** Write the canonical incidence-algebra basis as \(e_v\) for \(v\in V\) and \(e_{uv}\) for cover relations \(u<v\). Every element is uniquely
\[
a=\sum_{v\in V}a_ve_v+\sum_{e\in E}\beta_e e_e.
\]
For \(b\) with vertex coefficients \(b_v\) and edge coefficients \(\gamma_e\), the \(e=u<v\) coefficient of \([a,b]\) equals
\[
(a_u-a_v)\gamma_e+\beta_e(b_v-b_u).
\]
All vertex coefficients of \([a,b]\) vanish, and there are no edge-edge products. Let \(D=\{e=uv:a_u\ne a_v\}\). In the commutator matrix, every row indexed by \(D\) has a unique nonzero pivot in its own edge-coordinate column \(\gamma_e\); these pivots are pairwise distinct. Rows indexed by \(E\setminus D\) have no entries in edge-coordinate columns. Their nonzero rows correspond exactly to \(S=\{e\in E\setminus D:\beta_e\ne0\}\) and are nonzero scalar multiples of the oriented vertex-edge incidence matrix of \((V,S)\). Its rank over any field is \(n-k_G(S)=r(S)\), because a spanning forest supplies independent rows and every other row is a signed path sum. Hence
\[
\boxed{\rho(a)=|D|+r(S).}
\]
This identity handles zero coefficients, disconnected graphs and characteristic two without exceptions.

**2. General polynomial and matroid invariance.** Fix the vertex labels \((a_v)\). For an equal-labelled edge \(e\), choosing \(\beta_e=0\) contributes weight \(1\), while choosing a nonzero value contributes one of \(q-1\) choices. Record the set \(S\) of nonzero equal-labelled edges. For a differently labelled edge, all \(q\) choices of \(\beta_e\) are permitted and the edge contributes one rank. By Step 1,
\[
\mathcal C_{G,q}(z)=\sum_{S\subseteq E}(q-1)^{|S|}z^{r(S)}
\sum_{\substack{(a_v)\in\mathbb F_q^V\\a_u=a_v\ (uv\in S)}}
\prod_{e=uv\in E\setminus S}
\left({\bf1}_{a_u=a_v}+qz\,{\bf1}_{a_u\ne a_v}\right).
\]
For edges outside \(S\), rewrite each factor as \(qz+(1-qz){\bf1}_{a_u=a_v}\) and expand, selecting a subset \(T\subseteq E\setminus S\) of equality factors. A vertex-label assignment constant along every edge in \(S\cup T\) has exactly \(q^{k_G(S\cup T)}=q^{n-r(S\cup T)}\) choices. This yields the boxed double sum. Since \(n=c+r(E)\), dividing by \(q^c\) leaves an expression in \(m\), \(q\), \(|S|\), \(|T|\), \(r(S)\), \(r(S\cup T)\) and \(r(E)\) alone. All these data are preserved under isomorphism of graphic matroids, proving invariance.

**3. Forest factorization.** If \(G\) is a forest, select one vertex label per component and independent differences along its edges. This linear change of coordinates is bijective, giving \(q^c\) choices of root labels. For one edge with fixed parent label, equal labels contribute \(1+(q-1)z\), while different labels contribute \((q-1)qz\). The local sum is therefore \(1+(q^2-1)z\), independently on every edge, proving the forest law.

**4. Unique cycle and its correction.** Remove pendant trees from the connected unicyclic graph, leaving an even cycle of length \(\ell\). The same leaf calculation as in Step 3 multiplies the rank polynomial by \(P_q(z)\) for every removed edge, regardless of the cycle labels. On the bare cycle, pretend temporarily that every active equal-labelled edge increases rank by one. Summing over its \(q\) vertex labels with the edge weights
\[
W_{aa}=1+(q-1)z,\qquad W_{ab}=qz\quad(a\ne b)
\]
gives the trace of an \(\ell\)-th power of the \(q\)-by-\(q\) transfer matrix. Its eigenvalues are \(P_q(z)\) once and \(1-z\) with multiplicity \(q-1\), so the provisional polynomial is \(P_q(z)^\ell+(q-1)(1-z)^\ell\).

A set of cycle edges has independent graphic incidence rows unless **every** cycle edge is active. That exceptional configuration occurs exactly when all cycle vertex labels coincide (\(q\) choices) and every cycle edge coefficient is nonzero (\((q-1)^\ell\) choices). Its true rank is \(\ell-1\), rather than the provisional \(\ell\); replacing its contribution gives the correction \(q(q-1)^\ell(z^{\ell-1}-z^\ell)\). Restoring all pendant edges proves the stated formula.

**5. Nonisomorphic-poset consequence.** For a connected forest with \(m\) edges, the polynomial is always \(qP_q(z)^m\), even when the underlying Hasse trees are nonisomorphic. For example, a five-element star and an alternating five-element fence have different Hasse-graph degree sequences but exactly the same centralizer-dimension multiplicities over every finite field. Their incidence algebras are not isomorphic, by the standard incidence-algebra reconstruction theorem for finite posets. The polynomial is therefore a genuinely coarser invariant than algebra isomorphism.

## Verification

Run `python3 check_incidence_centralizers.py` with Python 3 and its standard library. The checker independently builds the incidence-algebra multiplication table, forms every full adjoint matrix \(b\mapsto ab-ba\) and computes its rank by finite-field row reduction. For each tested field and graph, it compares the resulting histogram with both a separate graphic-matroid subset expansion and the stated closed forest/single-cycle polynomial when applicable.

Twelve cases were exhaustively checked, spanning \(26{,}587\) algebra elements over the prime fields of orders two and three. The cases include connected and disconnected forests, distinct trees with the same rank distribution, a four-cycle in both characteristics, a six-cycle, nonisomorphic single-cycle graphs with the same cycle length, and the multicyclic graph \(K_{2,3}\) for the general matroid formula. The final output is `ALL_INCIDENCE_CENTRALIZER_CHECKS_PASSED 12 26587`. Finite tests do not prove the all-graph theorem; the proof is given above. For the four-cycle over \(\mathbb F_2\), the computed rank histogram is \((2,8,60,106,80)\).

## Relationship to prior work

Mahir Bilen Can's *Incidence Monoids: Automorphisms and Complexity* (2021), especially Theorems 1.1–1.4, studies automorphisms, torus-action complexity, and adherence orders. Its complexity-zero connected height-two graphs are trees, and its complexity-one height-two graphs are unicyclic. Those results motivate exactly the two explicit cases here but do not provide centralizer-rank enumerators. Gargate and Gargate (2020) count \((k+1)\)-potent elements in incidence algebras; this is a different constraint on individual elements.

The standard Fortuin–Kasteleyn/Potts expansion and graphic-matroid rank theory underlie the counting method and are not claimed as inventions. In particular, existing chromatic-fiber formulas for additive commutators of radical-square-zero quiver algebras already give total commuting-pair counts. A total commuting-pair count is one weighted evaluation of the present rank polynomial, not a complete centralizer-dimension distribution. The contribution assessed here is the full elementwise rank polynomial, its graphic-matroid invariance, and the universal tree/unique-cycle laws. No originality claim is made for the known total commuting-pair specialization or the standard transfer-matrix eigenvalue calculation in isolation.

## Limitations

For general multicyclic graphs the double subset sum is an exact expression but not a compact closed form. The two closed formulas apply only to the stated forest and connected unicyclic cases. The poset must have no strict chain of three elements; deeper incidence algebras have nonzero off-diagonal products, so the proof does not extend directly. The classification by torus-action complexity is borrowed from Can and is not re-proved here. The formula's mathematical correctness does not establish publication priority; an equivalent derivation might exist under a matroid, Potts-model, or finite-algebra formulation. No independent audit or external mathematical validation has been performed.

## References

1. Mahir Bilen Can, *Incidence Monoids: Automorphisms and Complexity*, arXiv:2105.09826v1 (public 20 May 2021), https://arxiv.org/abs/2105.09826; MSC2020 20M32 among the listed classifications.
2. Ivan Gargate and Michael Gargate, *\((k+1)\)-potent Matrices in Triangular Matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243 (public 30 August 2020), https://arxiv.org/abs/2009.04243.
3. Alan D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607 (2005), https://arxiv.org/abs/math/0503607.
