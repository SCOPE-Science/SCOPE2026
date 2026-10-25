# Heisenberg commuting graphs over finite chain rings recover exactly residue size and length

## Finding

Let \(R\) be a finite commutative chain ring with maximal ideal \((\pi)\), nilpotency length \(m\geq 1\), and residue-field order \(q\). Write \(H(R)=\operatorname{UT}_3(R)\) for the group of upper unitriangular three-by-three matrices, and let \(\Gamma(H(R))\) be its **full** commuting graph: all elements are vertices, and two distinct vertices are adjacent exactly when the matrices commute.

**Classification theorem.** For any two finite commutative chain rings \(R,S\),
\[
\Gamma(H(R))\cong\Gamma(H(S))
\quad\Longleftrightarrow\quad
(q_R,m_R)=(q_S,m_S).
\]
In particular the abstract commuting graph does **not** determine the isomorphism type or characteristic of the coefficient ring. The isomorphism is constructive: normalize every nonzero vector of \(R^2\) by its common \(\pi\)-valuation, use the uniform tree of successive projective-line reductions, and freely match the unit-multiplier labels and central coordinates.

The graph has \(q^{3m}\) vertices and \(q^m\) universal vertices. For each \(v=0,\ldots,m-1\), the nonuniversal degree
\[
q^{2m+v}-1
\]
occurs precisely
\[
(q^2-1)q^{3m-2v-2}
\]
times. No other degrees occur. In particular, the number of distinct nonuniversal degrees equals \(m\), after which the number of universal vertices recovers \(q\).

**Uniform nonisoclinic collision.** For every prime \(p\) and every \(m\geq2\), put
\[
R=\mathbb Z/p^m\mathbb Z,\qquad
S=\mathbb F_p[t]/(t^m).
\]
Then their Heisenberg groups have isomorphic full commuting graphs and both have nilpotency class exactly two, but they are **not isoclinic**: their derived subgroups have exponents \(p^m\) and \(p\), respectively. This illustrates the same explicit nonisoclinic family already derivable from earlier all-arity commuting-tuple comparisons, now with the **stronger** conclusion that one bijection preserves all commuting pairs. The original contribution here is the complete graph-isomorphism classification and its converse, not the existence of this family.

The existence of *some* nonisoclinic class-two groups with the same commuting graph was previously reported by Arvind, Cameron, Ma and Maslova, crediting Eamonn O'Brien for an example at order \(64\) and further examples. No priority is claimed for the first counterexample to the 2022 Arvind–Cameron conjecture. The assessed contribution is the explicit all-chain-ring graph classification and the uniform infinite family with exact recoverable parameters.

## Assumptions and scope

A finite commutative chain ring is a finite commutative local ring whose ideals are linearly ordered by inclusion. It has a generator \(\pi\) of its maximal ideal, a unique integer \(m\ge1\) with \(\pi^m=0\) and \(\pi^{m-1}\ne0\), and a residue field \(R/(\pi)\) of order \(q\ge2\). Put \(R_j=R/(\pi^j)\) for \(1\le j\le m\). In particular \(|R_j|=q^j\) and \(|R_j^\times|=(q-1)q^{j-1}\). If \(m=1\), \(R\) is a finite field.

The group \(H(R)\) consists of triples \((a,b,c)\in R^3\), representing the matrix with upper off-diagonal entries \(a,b,c\) in positions \((1,2),(2,3),(1,3)\) respectively. Its multiplication is
\[
(a,b,c)(u,v,w)=(a+u,b+v,c+w+av).
\]
Commutation is therefore exactly the equation \(av-ub=0\). Its center and derived subgroup are both \(\{(0,0,c):c\in R\}\). This is a nonabelian class-two group even when \(q=2\).

The graph includes the center. As usual an isoclinism is an isomorphism between the two central quotients together with an isomorphism of derived subgroups, both compatible with commutators. Field order \(q\), characteristic, and ring length \(m\) are allowed to vary freely between rings. No ring isomorphism is assumed.

## Proof

**1. Valuation and projective direction.** Define \(\operatorname{val}(0)=m\), and \(\operatorname{val}(a)=v\) when \(a\in(\pi^v)\setminus(\pi^{v+1})\). For a vector \(x=(a,b)\in R^2\), set \(\operatorname{val}(x)=\min(\operatorname{val}(a),\operatorname{val}(b))\). If \(x\ne0\) and its valuation is \(v<m\), then multiplication by \(\pi^v\) induces an additive-module bijection \(R_{m-v}\longrightarrow(\pi^v)\). Thus \(x\) determines a **unique** primitive vector \(u_x\in R_{m-v}^2\) whose multiplication by \(\pi^v\) gives \(x\). Primitive means at least one coordinate is a unit. Define the associated projective point \(P_x=R_{m-v}u_x\in\mathbb P^1(R_{m-v})\). Two primitive vectors define the same point if and only if they differ by multiplication by a unit.

**2. Exact determinant criterion.** For nonzero vectors \(x,y\) with valuations \(v,w\), if \(v+w\ge m\) then \(\det(x,y)=0\) automatically. If \(v+w<m\), put \(k=m-v-w\). Dividing by the common uniformizer power gives
\[
\det(x,y)=0\quad\Longleftrightarrow\quad
\det(u_x,u_y)\equiv0\pmod{\pi^k}.
\]
All reductions are well-defined because \(k\le m-v\) and \(k\le m-w\). Over the local ring \(R_k\), any primitive \(u\) can be completed to an invertible two-by-two matrix. In the resulting coordinates \(u=(1,0)\), the determinant with a second primitive vector \(z\) vanishes exactly when \(z\) is a unit multiple of \(u\). Consequently,
\[
\boxed{\ \det(x,y)=0\iff
\bigl(v+w\ge m\bigr)\text{ or }
\bigl(v+w<m\ \text{and}\ P_x|_k=P_y|_k\bigr).\ }
\]
Here \(P|_k\) denotes the image of the projective point under reduction to \(R_k\). If either vector is zero, its determinant with every other vector is zero.

**3. The uniform projective-direction tree.** The projective line \(\mathbb P^1(R_1)\) has \(q+1\) points. For every \(j\ge2\), every projective point of \(\mathbb P^1(R_{j-1})\) has exactly \(q\) lifts in \(\mathbb P^1(R_j)\): in a chart with the first coordinate a unit, points are \((1,z)\) and lift by the \(q\) elements of the additive fiber \((\pi^{j-1})/(\pi^j)\); the other chart works identically. Thus the system of projective lines at levels \(1,\ldots,m\), linked by reductions, is an abstract rooted forest consisting of \(q+1\) uniform \(q\)-ary trees of depth \(m-1\). Its isomorphism type depends only on \(q,m\), regardless of the ring.

For each valuation \(v\), fixing a projective direction \(P\in\mathbb P^1(R_{m-v})\), the primitive representatives form a torsor for \(R_{m-v}^\times\), of cardinality \((q-1)q^{m-v-1}\). These representatives give distinct vectors of valuation \(v\), and their unit labels do not affect determinant vanishing. Any isomorphism of the projective-direction forests for two rings with the same \(q,m\), together with arbitrary bijections between the corresponding unit-label torsors, therefore induces a bijection \(R^2\to S^2\) preserving the **entire** zero-determinant relation by Step 2. Map the zero vector to zero. Choose any bijection between the two central-coordinate sets, each of size \(q^m\). The induced bijection \(H(R)\to H(S)\) preserves commuting pairs and hence is an isomorphism of full simple commuting graphs. This proves the forward construction.

**4. Graph degrees and parameter recovery.** Since the commutator is the determinant, the universal vertices are exactly \(Z(H(R))\), of cardinality \(q^m\), and the total number of vertices is \(q^{3m}\). For nonzero \(x=\pi^v u\in R^2\) with primitive \(u\) and valuation \(v<m\), the linear map
\[
R^2\to R_{m-v},\qquad y\mapsto\det(u,y)\bmod\pi^{m-v}
\]
is surjective, since at least one coordinate of \(u\) is a unit. Hence its kernel has cardinality \(q^{2m-(m-v)}=q^{m+v}\). Adjoining an arbitrary central coordinate gives centralizer size \(q^{2m+v}\), so the full-graph degree is \(q^{2m+v}-1\). The number of coefficient vectors of valuation exactly \(v\) is
\[
q^{2(m-v)}-q^{2(m-v-1)}=(q^2-1)q^{2(m-v-1)}.
\]
Multiplying by the \(q^m\) central labels gives the stated degree multiplicity. The nonuniversal degree values are distinct for \(v=0,\ldots,m-1\). Thus the number of such distinct values recovers \(m\); then \(|Z(H(R))|=q^m\) recovers \(q\) uniquely. Therefore graph isomorphism forces the same \((q,m)\), proving the converse.

**5. Derived-subgroup obstruction.** The commutator of \((1,0,0)\) and \((0,r,0)\) is the central element \((0,0,r)\), so \(H(R)'\) is exactly the additive group of \(R\). If \(R=\mathbb Z/p^m\mathbb Z\), this additive group has exponent \(p^m\); if \(S=\mathbb F_p[t]/(t^m)\), its additive group has exponent \(p\). For \(m\ge2\) they cannot be isomorphic. As isoclinism requires an isomorphism of derived subgroups, the groups are not isoclinic. Both rings have \((q,m)=(p,m)\), so by Step 3 their full commuting graphs are isomorphic. This completes the proof.

## Verification

The standalone program `verify_chain_commuting.py` implements ring addition and multiplication independently for integer residue rings \(\mathbb Z/p^m\mathbb Z\) and truncated polynomial rings \(\mathbb F_p[t]/(t^m)\). For the four test pairs \((p,m)=(2,2),(2,3),(3,2),(5,2)\), it constructs an explicit digitwise valuation-and-projective-direction bijection of all coefficient vectors and compares zero determinants **for every pair**. It checks injectivity, surjectivity, centralizer cardinalities, and valuation histograms. For the \((2,2)\) pair it additionally checks all \(64^2\) ordered pairs of three-coordinate group elements through **independently implemented group multiplication**, verifying that equality of opposite products matches the determinant rule.

The run returned `VERIFY_OK all direct commuting-graph comparisons and group-product checks` and two `GROUP_PRODUCTS_OK` messages for the actual group-multiplication tests. These finite checks are corroboration. The general theorem, including extension to nonprime residue fields and all lengths, follows from the proof, not the computation.

## Relationship to prior work

Arvind and Cameron (2022, Section 8) explicitly asked whether a nilpotency-class-two finite group is determined up to isoclinism by its full commuting graph. This was subsequently **answered negatively** in Arvind, Cameron, Ma and Maslova (2023 preprint, revised 2025, Section 9), crediting O'Brien for nonisoclinic order-\(64\) examples and other finite pairs. Accordingly the existence of class-two counterexamples is prior art, not a new assertion of priority here. The later paper also asks about existence for each order \(p^6\); the displayed uniform family supplies one such pair for every prime \(p\), a consequence already available in weaker invariant form from earlier enumeration. The new assertion is the simultaneous graph isomorphism across **all** chain rings.

Bartnicka and Matras (2017, Sections 2–3) establish the projective-line distant-graph theory over finite local rings and relate it to residue-field quotients. Their distant graph concerns **primitive projective points at one ring level**; it does not, in the inspected discussion, classify the full element-commuting graph across **all** valuations and its nested projective-direction reductions. The tree argument above combines all these levels.

A separate established result for **two-generated** class-two groups models their commuting graphs by a cyclic-module determinant relation and proves isoclinism for graph-isomorphic groups within that restricted class. The displayed examples here are outside that restriction for \(m\ge2\): their central quotients are additive \(R^2\), which cannot be generated by only two group elements in general, and the polynomial-ring examples require \(2m\) generators as elementary abelian quotients.

Earlier all-arity commuting-tuple counts for the same chain-ring Heisenberg family already establish equality of those numerical invariants across rings with fixed \(q,m\) and yield the same nonisoclinic examples. Those consequences are explicitly **excluded from the new contribution**. Equality of clique counts of every arity alone cannot certify graph isomorphism. The present proof supplies a simultaneous adjacency-preserving bijection for every pair of such rings, the complete graph-degree spectrum, and a converse graph recognition theorem.

## Limitations

The theorem is restricted to **commutative chain rings** and to the size-three unitriangular Heisenberg group. No claim is made for nonchain local rings, larger Heisenberg groups, or arbitrary class-two groups. Although the graph determines \((q,m)\), it need not distinguish coefficient rings with those parameters; conversely two rings with different parameters cannot have isomorphic graphs **within this family**. The construction is noncanonical because it chooses projective-tree isomorphisms and unit-label bijections. Computations cover prime residue fields and small lengths only.

The existence of nonisoclinic class-two groups with identical commuting graphs and the displayed nonisoclinic Heisenberg pair already have prior support; neither is new here. The complete **graph-isomorphism** classification across all finite commutative chain rings has not been identified in the inspected references; an equivalent classification under chain-geometry or graph-theoretic terminology remains a residual originality risk. No assertion of exhaustive publication priority or independent verification is made.

## References

1. V. Arvind and P. J. Cameron, “Recognizing the Commuting Graph of a Finite Group,” arXiv:2206.01059v1, first publicly submitted 2 June 2022; especially Section 8 (the original class-two isoclinism conjecture). Listed primary mathematical subject 20D60, secondary 05C60.
2. V. Arvind, P. J. Cameron, X. Ma, and N. V. Maslova, “Aspects of the commuting graph,” arXiv:2305.07301 (first submitted 12 May 2023; version 5 of 27 July 2025), Section 9 and Question 4. This expressly credits E. O'Brien with earlier class-two nonisoclinic examples of isomorphic commuting graphs.
3. E. Bartnicka and A. Matras, “The distant graph of the projective line over a finite ring with unity,” arXiv:1701.01263 (first submitted 5 January 2017), Sections 2–3, projective lines of local rings and residue-field reductions.
4. “Two-generated class-two commuting graphs are determinant blow-ups,” publicly available mathematical research record, October 2026, exact hypothesis two-generated class-two groups; repository identifier `2026/10/4/SCOPE-two-generated-class-two-commuting-graphs-are-determinant-blow-up--414532e5643a`.
