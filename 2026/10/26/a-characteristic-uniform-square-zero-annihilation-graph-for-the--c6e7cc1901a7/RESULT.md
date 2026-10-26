# A characteristic-uniform square-zero annihilation graph for the bivariate cubic truncation

## Finding
Let \(k=\mathbb F_q\) be any finite field, of arbitrary characteristic, and put
\[
A=k[x,y]/(x^3,y^3).
\]
Define \(S(A)=\{a\in A:a^2=0\}\). The *square-zero annihilation graph* \(\Gamma_2(A)\) has vertex set \(S(A)\setminus\{0\}\), and distinct vertices \(a,b\) are adjacent exactly when \(ab=0\). It is the induced subgraph of the usual zero-divisor graph on nonzero square-zero elements.

**Theorem.** For every prime power \(q\),
\[
\boxed{\Gamma_2(A)\cong K_{q^3-1}\vee\left(\bigsqcup_{j=1}^{q+1}K_{(q-1)q^3}\right).}
\]
Here \(K_m\) denotes a complete graph of order \(m\); \(\bigsqcup\) is disjoint union, and \(\vee\) adds every edge between the two displayed parts. In particular the graph has \(q^5-1\) vertices. Its \(q^3-1\) universal vertices have degree \(q^5-2\), and each of the remaining \(q^5-q^3\) vertices has degree \(q^4-2\). Its clique number and chromatic number both equal \(q^4-1\), and its independence number is \(q+1\). Furthermore,
\[
\#\{(a,b)\in S(A)^2:ab=0\}=q^9+q^8-q^7.
\]
These formulas hold unchanged in characteristic two and odd characteristic, although the parametrizations of the square-zero elements are different. When \(\operatorname{char}k=3\), the substitutions \(x=g-1\), \(y=h-1\) identify \(A\) with the modular group algebra \(k[C_3\times C_3]\).

## Assumptions and scope
The field is finite of cardinality \(q\ge2\); no restriction on characteristic. Work in the nine-element monomial basis \(\{x^iy^j:0\le i,j\le2\}\), with both cubic relations imposed. The graph is simple: loops are excluded even though every vertex squares to zero. The theorem concerns the *induced subgraph* on square-zero elements, not the full zero-divisor graph, and counts ordered pairs with zeros explicitly where indicated.

## Proof
**1. Square-zero locus in odd characteristic.** Every nilpotent has constant term zero, so write
\[
a=\ell+a_2+a_3+a_4,
\]
where \(a_d\) is homogeneous of total degree \(d\). Since \(x^2,xy,y^2\) are linearly independent and \(\ell^2=0\) forces \(\ell=0\) over a field of characteristic different from two, every square-zero element has the form
\[
a=ux^2+vxy+wy^2+sx^2y+txy^2+zx^2y^2
\]
with \(u,v,w,s,t,z\in k\). The terms of total degree at least three do not contribute to \(a^2\), since every monomial of total degree five vanishes. Consequently
\[
a^2=(v^2+2uw)x^2y^2,
\qquad a^2=0\iff v^2+2uw=0.
\]
The projective conic \(v^2+2uw=0\) has exactly \(q+1\) rational directions. Explicitly, there are \(q\) points with \(u=1\), \(v\in k\), \(w=-v^2/2\), and one point \([0:0:1]\). The affine cone therefore has \(1+(q+1)(q-1)=q^2\) vectors, each admitting an arbitrary three-coordinate higher-degree tail.

For two such square-zero elements with quadratic vectors \(c=(u,v,w)\), \(c'=(u',v',w')\), their product is
\[
ab=(uw'+wu'+vv')x^2y^2.
\]
Write \(B(c,c')=uw'+wu'+vv'\). If \(c\ne0\) and both vectors lie on the conic, then \(B(c,c')=0\) *if and only if* \(c'\in kc\). Indeed when \(u=0\) one has \(v=0\), \(w\ne0\), and \(B=0\) forces \(u'=0\), hence \(v'=0\). When \(u\ne0\), the equation \(B=0\) determines \(w'\), and substitution in \(v'^2+2u'w'=0\) gives \((v'-(v/u)u')^2=0\). Thus \(c'=\lambda c\), including \(\lambda=0\), over every field. Conversely \(B(c,\lambda c)=\lambda(v^2+2uw)=0\). This establishes that two nonzero quadratic directions annihilate exactly when they coincide projectively.

**2. Square-zero locus in characteristic two.** Frobenius squaring acts termwise. Writing the same monomial coefficients for \(a\), its square is
\[
a^2=a_{00}^2+a_{10}^2x^2+a_{01}^2y^2+a_{11}^2x^2y^2.
\]
These four monomials are independent. Hence square-zero elements are exactly
\[
a=ux^2+wy^2+sx^2y+txy^2+zx^2y^2,
\]
with five free coefficients. Their pairwise product is
\[
ab=(uw'+wu')x^2y^2.
\]
If \((u,w)\ne(0,0)\), the bilinear equation \(uw'+wu'=0\) is exactly the determinant-zero condition in two dimensions, and so holds precisely when \((u',w')\) is proportional to \((u,w)\). Again there are \(q+1\) projective directions. Thus the same annihilation geometry holds even though the odd-characteristic conic has become the full characteristic-two two-dimensional space.

**3. Graph reconstruction.** In either characteristic the leading coefficient vector ranges over a cone with \(q^2\) vectors, partitioned into zero and \(q+1\) lines of \(q-1\) nonzero vectors. In every case there are \(q^3\) unrestricted higher-degree tails. Nonzero elements with zero leading vector form a clique of \(q^3-1\) universal vertices, since their products with all square-zero elements vanish. Each of the \(q+1\) nonzero leading directions contributes a clique of \((q-1)q^3\) vertices. Vertices from distinct such cliques never annihilate one another. This is precisely the asserted join of disjoint cliques.

The graph parameters follow immediately. There are \(q^3-1\) universal vertices and \((q+1)(q-1)q^3=q^5-q^3\) others. A peripheral vertex has \((q^3-1)+((q-1)q^3-1)=q^4-2\) neighbors. Every maximal clique contains the universal clique and one peripheral clique, giving size \(q^4-1\). Choosing one vertex in each peripheral clique produces an independent set of size \(q+1\), which is maximal. The clique coloring is optimal by assigning one palette of \(q^3-1\) colors to the universal part and a shared palette of \((q-1)q^3\) colors to every peripheral clique.

For the ordered-pair count, the \(q^3\) square-zero elements with zero leading vector each annihilate all \(q^5\) square-zero elements, whereas each of the \(q^5-q^3\) elements with nonzero leading vector annihilates exactly \(q^4\) of them. Therefore
\[
q^3q^5+(q^5-q^3)q^4=q^9+q^8-q^7.
\]
Finally, if \(k\) has characteristic three and \(g,h\) generate \(C_3\times C_3\), then \((g-1)^3=(h-1)^3=0\). The resulting surjection from \(k[x,y]/(x^3,y^3)\) to \(k[C_3\times C_3]\) is an isomorphism because both have dimension nine. This completes the proof.

## Verification
A standalone standard-library checker accompanies this result. It enumerates every element of the nine-dimensional algebra over the prime fields of orders two and three, identifies the square-zero set by multiplication in the full monomial basis, and independently compares every ordered product within that set with the asserted leading-coefficient criterion. It found \(32\) square-zero elements and \(640\) ordered zero-product pairs over \(\mathbb F_2\), and \(243\) square-zero elements and \(24057\) ordered zero-product pairs over \(\mathbb F_3\). Both passed all pairwise checks. The proof, not the finite tests, establishes the formula for every prime power.

## Relationship to prior work
Aliniaeifard and Li, *Zero-Divisor Graphs for Group Rings* (2014), study zero-divisor graphs of modular group algebras, including structural recognition of finite abelian groups and global graph parameters. Their accessible full text does not give the graph induced by square-zero elements of \(k[C_3\times C_3]\), nor the characteristic-uniform clique-join decomposition above. Arunkumar, Cameron, Kavaskar and Chelvam, *Induced subgraphs of zero-divisor graphs* (2022 preprint, 2023 journal article), prove general universality and structural results for zero-divisor graphs; universality of *some* induced graph in *some* ring does not determine this canonical induced graph in this particular ring. A single-element Jordan-form census for the same truncated algebra may detect its square-zero locus in some characteristics, but cannot on its own determine the required two-element annihilation relation. These are mathematical implication comparisons, not assertions of absolute novelty.

## Limitations
The theorem determines only the square-zero induced subgraph; it does not classify the entire zero-divisor graph, full ring automorphisms, or higher nilpotency-index strata. No claim is made for truncations with other exponents or numbers of variables. Finite exhaustive checks do not certify the general result. The literature search is bounded and does not establish publication priority; independent review has not been performed.

## References
1. F. Aliniaeifard and Y. Li, *Zero-Divisor Graphs for Group Rings*, Communications in Algebra **42** (2014), 4790–4800. DOI: https://doi.org/10.1080/00927872.2013.827689 . Public online date: 2014-05-23.
2. G. Arunkumar, P. J. Cameron, T. Kavaskar and T. Tamizh Chelvam, *Induced subgraphs of zero-divisor graphs*, Discrete Mathematics **346** (2023), 113580; first arXiv version 2022-07-24, https://arxiv.org/abs/2207.11741 .
