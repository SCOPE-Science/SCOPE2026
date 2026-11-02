# Colored complementary-retraction graph of the two-generator exterior algebra

## Finding
Let \(K=\mathbb F_q\) be any finite field, \(q\ge2\), of arbitrary characteristic, and let \(A=\bigwedge_K(Kx\oplus Ky)\) be the four-dimensional unital associative exterior algebra, with \(z=xy=-yx\) and \(x^2=y^2=0\). The unital \(K\)-algebra endomorphism monoid has exactly \(q^6\) elements. Its set \(E\) of idempotent endomorphisms has size
\[
|E|=q^2(q+1)+2.
\]
Deleting the augmentation and identity maps from the simple graph whose vertices are \(E\) and whose distinct vertices are joined precisely when they commute gives exactly
\[
\bigsqcup_{j=1}^{q(q+1)/2}K_{q,q}.
\]
Consequently every inclusion-maximal pairwise commuting family of idempotent endomorphisms contains exactly four maps (augmentation, identity, and a complementary pair), is a four-element Boolean monoid under composition, and the number of such families is
\[
\frac{q^3(q+1)}{2}.
\]
The number of ordered commuting pairs in \(E^2\), allowing repetitions, and the probability of commutation for independent uniform idempotents are respectively
\[
q^2(q+1)(q+5)+4,\qquad
\frac{q^2(q+1)(q+5)+4}{\bigl(q^2(q+1)+2\bigr)^2}.
\]
In particular this probability is asymptotic to \(q^{-2}\) as \(q\) grows along prime powers. These are *algebra* endomorphisms; no claim is made about arbitrary linear maps, pre-endomorphisms, or endomorphisms of higher-rank exterior algebras.

## Assumptions and scope
The algebra has basis \(1,x,y,z\), relations \(x^2=y^2=z^2=xz=zx=yz=zy=0\), and \(yx=-z\). In characteristic two the relation \(-z=z\) holds, but the proofs below remain valid. All homomorphisms are \(K\)-linear, unital, and multiplicative. The augmentation \(\varepsilon\) is the homomorphism fixing \(1\) and sending \(x,y,z\) to zero. An idempotent endomorphism means \(f\circ f=f\); pairwise commuting refers to composition, not commutativity of algebra elements.

## Proof
**Endomorphism coordinates.** The ideal \(J=(x,y,z)\) is the set of nilpotent elements (the scalar part of every nilpotent is zero). Every element of \(J\) has square zero, and every two elements of \(J\) anticommute, also in characteristic two. Thus the images of the two generators may be *any* elements of \(J\). An endomorphism is uniquely described by \((P,\ell)\), where \(P\in M_2(K)\) specifies the degree-one coefficients and \(\ell\in K^{1\times2}\) specifies the coefficients of \(z\) in the generator images. Because \(f(z)=f(x)f(y)=(\det P)z\), composition obeys
\[
(P,\ell)\circ(Q,m)=(PQ,\ell Q+(\det P)m).
\]
There are \(q^4 q^2=q^6\) endomorphisms.

**All idempotents.** The idempotence equations are
\[
P^2=P,\qquad \ell P+(\det P)\ell=\ell.
\]
If \(\operatorname{rank}P=0\), then \(P=0\) and \(\ell=0\); this is \(\varepsilon\). If \(\operatorname{rank}P=2\), then \(P=I\), \(\det P=1\), and the second equation implies \(\ell=0\); this is the identity. If \(\operatorname{rank}P=1\), \(\det P=0\), and the equation becomes \(\ell P=\ell\), so \(\ell\) is a functional vanishing on \(\ker P\), with exactly \(q\) choices. An idempotent rank-one operator \(P\) is uniquely determined by the ordered distinct pair \((L,M)=(\operatorname{im}P,\ker P)\) of projective lines in \(K^2\). There are \((q+1)q\) such pairs and therefore \(q^2(q+1)\) nontrivial idempotent algebra maps.

**Commuting criterion.** Let \((P,\ell)\) and \((Q,m)\) be nontrivial idempotents. Their degree-one projections commute precisely when they are equal or complementary. To see this, commuting rank-one idempotents preserve the image and kernel of each other; in the eigenline decomposition of \(P\), the rank-one idempotent \(Q\) must be either \(P\) or \(I-P\). In the equal case, the two compositions have central rows \(\ell P=\ell\) and \(mP=m\); they agree if and only if \(\ell=m\), that is, the endomorphisms are the same. In the complementary case \(Q=I-P\), the row \(\ell\) vanishes on \(\operatorname{im}Q=\ker P\) and \(m\) vanishes on \(\operatorname{im}P=\ker Q\). Hence \(\ell Q=mP=0\). Both compositions are \((0,0)=\varepsilon\), independently of the two labels. Thus distinct nontrivial maps commute exactly when their degree-one projections are complementary.

**Graph and maximal families.** Complementation \(P\mapsto I-P\) is a fixed-point-free involution on the \(q(q+1)\) rank-one projections, yielding \(q(q+1)/2\) unordered complementary pairs. For each such pair, the \(q\) maps above \(P\) are joined to all \(q\) maps above \(I-P\) and have no other nontrivial commuting neighbors. Therefore the graph is the claimed union of complete bipartite graphs. Augmentation commutes with everything because every algebra endomorphism preserves the unique nilpotent ideal and \(\varepsilon\circ f=f\circ\varepsilon=\varepsilon\); identity likewise commutes with everything. An inclusion-maximal commuting family contains both, together with precisely one edge of one component. Its multiplication is the Boolean four-element meet semilattice: the two rank-one maps are incomparable and their product is \(\varepsilon\). There are \(q^2\) edges per bipartite component, hence \(q^3(q+1)/2\) maximal families.

**Commuting-pair census.** Put \(N=q^2(q+1)\), so \(|E|=N+2\). The distinct nontrivial commuting ordered pairs are twice the number of graph edges, namely \(q(q+1)q^2=q^3(q+1)=qN\). The diagonal contributes \(N+2\) ordered pairs; ordered pairs involving at least one of the two universal elements contribute another \(4N+2\) after removing their four diagonal/universal overlaps appropriately. Equivalently, a direct count is \(N+2+qN+4N+2=(q+5)N+4\), proving the formula. Dividing by \((N+2)^2\) gives the probability, whose leading term is \(q^{-2}\).

## Verification
The independent enumerator in `verify_exterior.py` explicitly generates all \(q^6\) algebra endomorphisms from images of generators, computes their compositions via multiplication in the exterior algebra, selects idempotents, and constructs the commuting graph without using the claimed formulas as selection criteria. It exhaustively verifies the idempotent count, connected components, bipartite graph types, maximal-family count and ordered-pair count over fields of orders \(2,3,4,5,8\), including both prime and genuine extension fields. The results are
\[
\begin{array}{c|ccccc}
q&2&3&4&5&8\\
|E|&14&38&82&152&578\\
\text{graph components}&3&6&10&15&36\\
\text{maximal families}&12&54&160&375&2304\\
\text{ordered commuting pairs}&88&292&724&1504&7492
\end{array}
\]
The final program output is `VERIFY_OK exterior retraction commutation census`. These finite checks corroborate but do not replace the unrestricted proof.

## Relationship to prior work
Guimarães and Koshlukov study automorphisms of infinite-dimensional Grassmann algebras and associated superalgebra gradings [1], and Behzad and Gatto study linear endomorphism *operators* on exterior-algebra representation spaces [2]. Neither framework directly supplies this count of multiplicative idempotent maps on the four-dimensional exterior algebra or their commuting-pair graph. Ebrahim and Facchini classify idempotent *pre-endomorphisms* through complementary submodules and pre-ideals [3]. Their structural splitting principle provides important conceptual context, but does not state the explicit finite-field labeled-endomorphism commuting graph or its maximal-family and probability formulas. The rank-one projection argument used here is elementary linear algebra and is not claimed as novel. The contribution is the complete algebra-specific compatibility classification and census.

## Limitations
The result concerns unital \(K\)-algebra homomorphisms of precisely the rank-two exterior algebra, including characteristic two. It does not classify endomorphisms of general finite-dimensional Grassmann algebras, arbitrary linear operators, or the nonunital homomorphism monoid. The strongest literature overlap risk is an equivalent statement buried in semigroup literature on retractions of local algebras or under a different description of complementary projections. The referenced literature comparisons establish novelty only relative to inspected material, not absolute priority. No independent external mathematical audit has been performed.

## References
[1] A. de Araújo Guimarães and P. Koshlukov, *Automorphisms and superalgebra structures on the Grassmann algebra*, arXiv:2009.00175v1 (public September 1, 2020), https://arxiv.org/abs/2009.00175.

[2] A. Behzad and L. Gatto, *Bosonic and Fermionic Representations of Endomorphisms of Exterior Algebras*, arXiv:2009.00479v1 (public September 1, 2020), https://arxiv.org/abs/2009.00479.

[3] F. A. Ebrahim and A. Facchini, *Idempotent Pre-Endomorphisms of Algebras*, arXiv:2304.05079v1 (public April 11, 2023), https://arxiv.org/abs/2304.05079.
