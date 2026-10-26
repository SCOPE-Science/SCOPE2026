# Maximal square-zero subalgebras in free anticommutative antiassociative algebras

## Finding
Let \(K\) be a field of characteristic different from \(2\), let \(V\) be an \(r\)-dimensional vector space with \(r\geq3\), and let \(F(V)\) be the free anticommutative antiassociative algebra on \(V\). Put \(Z=\bigwedge^3 V\) and \(W=\bigwedge^2 V\). Every inclusion-maximal square-zero subalgebra of \(F(V)\) is an ideal and belongs to exactly one of the following families:

1. The characteristic ideal \(W\oplus Z\), of dimension \(\binom r2+\binom r3\).
2. For a line \(\ell=Kv\subset V\) and \(w\in W\), the ideal
   \[
   I(\ell,w)=Z\oplus(\ell\wedge V)\oplus K(v+w),
   \]
   of dimension \(r+\binom r3\). The ideal depends only on \(\ell\) and the class of \(w\) modulo \(\ell\wedge V\), after the generator \(v\ne0\) of \(\ell\) has been fixed.

These are two orbits under \(\operatorname{Aut}(F(V))\): the singleton \(W\oplus Z\) and the family of the \(I(\ell,w)\). For \(K=\mathbb F_q\) with odd prime-power \(q\), the exact number of inclusion-maximal square-zero subalgebras, equivalently maximal abelian subalgebras, is
\[
\boxed{1+\frac{q^r-1}{q-1}\,q^{\binom{r-1}{2}}.}
\]
In the first non-Zinbiel rank \(r=3\), all maximal abelian subalgebras have dimension \(4\), and there are \(q^3+q^2+q+1\) of them. For \(r\geq4\), the distinguished ideal has strictly greater dimension than the other maximal abelian ideals.

Their pairwise intersections are also fixed: distinct \(I(\ell,w)\) with the same line, and \(I(\ell,w)\) with \(W\oplus Z\), intersect in dimension \(r-1+\binom r3\); those associated with different lines intersect in dimension \(1+\binom r3\).

## Assumptions and scope
Algebras are nonunital and have a bilinear product. *Anticommutative antiassociative* means \(ab=-ba\) and \(a(bc)=-(ab)c\) for all elements. In characteristic different from \(2\), these are exactly the anticommutative binary Zinbiel algebras; in particular, the triple product is alternating. A subalgebra is *square-zero* when every product of two of its elements is zero. Because the product is anticommutative, these are also precisely the commutative (abelian) subalgebras. *Maximal* always means maximal by inclusion, not merely maximum dimension.

The underlying vector space and multiplication of the free algebra are
\[
F(V)=V\oplus W\oplus Z,\quad
v\cdot u=v\wedge u,\quad
v\cdot \alpha=v\wedge\alpha,\quad
\alpha\cdot v=-v\wedge\alpha,
\]
for \(v,u\in V\), \(\alpha\in W\); products of two elements of \(W\oplus Z\), and all products involving \(Z\), are zero. Thus \(F(V)^2=W\oplus Z\), \(F(V)^3=Z\), and all products of length four vanish. The free-algebra description itself is known; it is used as input, not claimed as a new result.

## Proof
**1. Projection obstruction.** Let \(U\subseteq F(V)\) be square-zero and let \(P\subseteq V\) be its image under the projection \(F(V)\to V\). If \(\dim P\geq2\), lift independent \(v,u\in P\) to elements \(a,b\in U\). The degree-two component of \(ab\) is \(v\wedge u\ne0\), a contradiction. Hence \(\dim P\leq1\).

**2. Zero projection.** If \(P=0\), then \(U\subseteq W\oplus Z\). The latter is square-zero, so the only maximal possibility with zero projection is \(W\oplus Z\).

**3. Line projection.** Suppose \(P=\ell=Kv\) and choose a lift \(a=v+w+z\in U\), with \(w\in W\) and \(z\in Z\). For \(b=\alpha+\zeta\in U\cap(W\oplus Z)\), the product \(ab=v\wedge\alpha\) vanishes. The kernel of the wedge map \(W\to Z\), \(\alpha\mapsto v\wedge\alpha\), is precisely \(v\wedge V\). Thus
\[
U\subseteq Z\oplus(v\wedge V)\oplus K(v+w).
\]
The right-hand space \(I(\ell,w)\) has zero product: the only potentially nonzero new products are \((v+w)(v\wedge u)=v\wedge v\wedge u=0\) and \((v+w)^2=0\). It follows that every square-zero \(U\) with line projection extends to one of the stated \(I(\ell,w)\).

**4. Maximality and ideal property.** For each \(I(\ell,w)\), multiplication by any \(a\in V\) maps \(v+w\) into \((v\wedge V)\oplus Z\), and maps \(v\wedge V\) into \(Z\). Multiplication by \(W\) also maps \(v+w\) into \(Z\), and multiplication by \(Z\) vanishes. Thus \(I(\ell,w)\) is an ideal. The ideal \(W\oplus Z\) is also an ideal. No square-zero space strictly containing \(I(\ell,w)\) can have a larger projection than \(\ell\), and step 3 rules out enlargement with the same projection. No square-zero space containing \(W\oplus Z\) can project nontrivially to \(V\): for nonzero \(v\), some \(\alpha\in W\) has \(v\wedge\alpha\ne0\) when \(r\geq3\). This proves the classification and maximality.

**5. Parameter and dimension counts.** Fixing \(\ell=Kv\) and one representative \(v\ne0\), two choices \(w,w'\in W\) define the same ideal exactly when \(w-w'\in v\wedge V\). This subspace has dimension \(r-1\). Hence each line has \(\dim(W/(v\wedge V))=\binom{r-1}{2}\) affine parameters, or \(q^{\binom{r-1}{2}}\) choices over \(\mathbb F_q\). There are \((q^r-1)/(q-1)\) lines. Since the direct sums have dimensions \(\binom r2+\binom r3\) and \(1+(r-1)+\binom r3\), the dimension and counting formulas follow.

**6. Orbits and intersections.** Each automorphism preserves \(F(V)^2=W\oplus Z\), so the distinguished ideal is fixed. Linear changes of generators act transitively on lines, while the triangular generator substitutions \(v\mapsto v+\alpha\), with \(\alpha\in W\), extend to invertible algebra maps and act transitively on the affine parameters for each line; therefore all other maximal square-zero ideals form one orbit. Two distinct ideals with the same line share exactly \((\ell\wedge V)\oplus Z\). The distinguished ideal meets every \(I(\ell,w)\) in that same subspace. For distinct lines \(\ell,m\), their projections do not meet, and \((\ell\wedge V)\cap(m\wedge V)=\ell\wedge m\) is one-dimensional; their intersection is \((\ell\wedge m)\oplus Z\). This proves the intersection assertions.

## Verification
The accompanying standalone files `checker.cpp` and `check_rank4.py` independently construct multiplication and test the classification in finite fields. Compiling and running the first checks **all 925,771 four-dimensional subspaces** of the seven-dimensional algebra over \(\mathbb F_3\), finding exactly \(40\) square-zero subspaces and verifying that each is an ideal. It also tests 93,556 sampled four-dimensional subspaces over \(\mathbb F_5\), including 156 square-zero ideals; the \(\mathbb F_5\) test is not exhaustive. The second checks all \(1,081\) *predicted* rank-four maximal square-zero ideals over \(\mathbb F_3\), including their ideal and zero-product properties; it does not enumerate all subspaces of the larger algebra. Neither finite computation is a substitute for the arbitrary-rank proof.

Reproduce using `g++ -O3 -std=c++17 checker.cpp -o checker && ./checker` and `python check_rank4.py` with standard Python 3. The tests require no third-party packages.

## Relationship to prior work
Remm, *Anti-commutative anti-associative algebras. Acaa-algebras* (2025), explicitly identifies the exterior-degree-one-through-three model of the free algebra and gives its multiplication in rank three; neither the free model nor the seven-dimensional example is claimed as new. Ismailov–Mashurov–Smadyarov (2023) previously constructed the seven-dimensional non-Zinbiel binary Zinbiel example, and Smadyarov (2026) studies nilpotency and nil subvarieties of binary Zinbiel algebras. Kunze–Scheinberg (1986) gives an earlier related antiassociative construction. The finding here is the **all-rank maximal square-zero subalgebra/ideal classification, its finite-field counts, orbit partition, and intersection spectrum**, rather than the construction or low-rank identification of these algebras.

## Limitations
The theorem concerns the free algebras, not arbitrary quotients or arbitrary binary Zinbiel algebras. Finite-field enumeration assumes odd characteristic, although the structural classification holds over any field of characteristic different from two. The literature comparison found no explicit equivalent maximal-square-zero classification in the inspected sources; an implicit consequence in broader work on dual mock-Lie or antiassociative algebras remains possible. No independent mathematical audit has been performed.

## References
1. E. Remm, *Anti-commutative anti-associative algebras. Acaa-algebras*, arXiv:2504.04092v1, first posted 2025-04-05, https://arxiv.org/html/2504.04092.
2. N. Smadyarov, *Nilpotency and nil subvarieties of binary Zinbiel algebras*, arXiv:2610.02852v1, first posted 2026-10-02, https://arxiv.org/html/2610.02852v1.
3. N. Ismailov, F. Mashurov and N. Smadyarov, *Defining identities for mono and binary Zinbiel algebras*, Journal of Algebra and Its Applications 22 (2023), article 2350165, DOI:10.1142/S0219498823501657.
4. R. A. Kunze and S. Scheinberg, *Alternative algebras having scalar involutions*, Pacific Journal of Mathematics 124 (1986), https://msp.org/pjm/1986/124-1/pjm-v124-n1-p10-s.pdf.
