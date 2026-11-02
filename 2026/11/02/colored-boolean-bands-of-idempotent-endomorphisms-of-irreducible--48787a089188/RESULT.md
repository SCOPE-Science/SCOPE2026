# Colored Boolean bands of idempotent endomorphisms of irreducible scalar Frobenius groups

## Finding

Let \(q=p^f\) be a prime power and let \(m>1\) divide \(q-1\). Choose \(a\in\mathbb F_q^\times\) of order \(m\) with \(\mathbb F_p(a)=\mathbb F_q\). Write \(r=\omega(m)\) for the number of distinct prime divisors of \(m\). The main counting and separation phenomenon concerns \(r\ge2\); all structural formulas below also hold when \(r=1\).

For the nonabelian irreducible scalar Frobenius group
\[
G=(\mathbb F_q,+)\rtimes\langle t\rangle,\qquad |t|=m,\qquad txt^{-1}=ax,
\]
let \(E\) denote the idempotents of its group-endomorphism monoid, with multiplication by composition \(ef=e\circ f\).

**Structure theorem.** The set \(E\) is a submonoid consisting of \(0\), the identity \(I\), and elements \(e_{c,S}\) indexed by \(c\in\mathbb F_q\) and nonempty subsets \(S\subseteq[r]\). Its multiplication is exactly
\[
e_{c,S}e_{d,T}=e_{c,S\cap T},\qquad e_{c,\varnothing}=0,
\]
with \(I\) acting as identity and \(0\) as zero. In particular,
\[
|E|=2+q(2^r-1),\qquad xyx=xy\quad(x,y\in E).
\]
Here the middle assertion records composition, not an additional defining identity.

**Commuting criterion and maximal-family classification.** For nonempty supports,
\[
e_{c,S}e_{d,T}=e_{d,T}e_{c,S}\quad\Longleftrightarrow\quad c=d\ \text{or}\ S\cap T=\varnothing.
\]
Every inclusion-maximal pairwise commuting family of idempotents is a subsemigroup. These families are in canonical bijection with functions \(\kappa:[r]\to\mathbb F_q\). The family associated with \(\kappa\) is
\[
\mathcal C_\kappa=\{0,I\}\cup\bigcup_{c\in\operatorname{im}\kappa}\bigl\{e_{c,S}:\varnothing\ne S\subseteq\kappa^{-1}(c)\bigr\}.
\]
Consequently their exact number is
\[
\boxed{\#\{\text{maximal commuting idempotent families}\}=q^r.}
\]
Their sizes are \(2+\sum_{c\in\operatorname{im}\kappa}(2^{|\kappa^{-1}(c)|}-1)\). The largest size is \(2^r+1\), attained by exactly \(q\) families; the smallest size is \(r+2\), attained by exactly \((q)_{\underline r}\) families.

If \(\lambda\vdash r\) is a partition with \(m_s(\lambda)\) parts of size \(s\) and \(b=\sum_s m_s(\lambda)\), the **complete maximal-family-size polynomial** is
\[
\boxed{\mathcal P_{r,q}(z)=\sum_{\lambda\vdash r}\frac{r!(q)_{\underline b}}{\prod_{s\ge1}(s!)^{m_s(\lambda)}m_s(\lambda)!}\,z^{\,2+\sum_{s\ge1}m_s(\lambda)(2^s-1)}.}
\]
Here \((q)_{\underline b}=q(q-1)\cdots(q-b+1)\), with the empty product equal to one. In particular, \(\mathcal P_{r,q}(1)=q^r\).

**Centralizers.** If \(|S|=s\ge1\), then
\[
\boxed{|C_E(e_{c,S})|=2^r+1+(q-1)(2^{r-s}-1).}
\]
There are exactly \(q\binom rs\) elements in this stratum. Both \(0\) and \(I\) commute with every idempotent.

## Assumptions and scope

The scalar complement has order \(m>1\) and acts irreducibly over \(\mathbb F_p\): equivalently \(f=\operatorname{ord}_m(p)\). No claim is made for reducible actions on the kernel, noncyclic complements, or arbitrary Frobenius kernels. All counts concern distinct endomorphisms of the fixed group, not conjugacy classes. A commuting family is maximal by inclusion, not only maximal cardinality. The monoid zero is the trivial homomorphism. The notation \(S\subseteq[r]\) uses any fixed ordering of the distinct prime-power factors of \(m\), and relabeling induces the natural permutation of coordinates.

## Proof

**1. All group endomorphisms.** Write \(V=(\mathbb F_q,+)\). Since \(V\) is the unique Sylow \(p\)-subgroup of \(G\), every group endomorphism \(\phi\) maps \(V\) into itself. Its restriction \(A:V\to V\) is \(\mathbb F_p\)-linear, and \(\phi(t)=v t^j\) for a unique \(v\in V\) and \(j\in\mathbb Z/m\mathbb Z\). The conjugation relation forces
\[
A(ax)=a^jA(x)\quad(x\in V).
\]
Its kernel is \(a\)-invariant. Irreducibility therefore forces either \(A=0\) or \(A\) injective, hence bijective. In the latter case, \(a\) and \(a^j\) define isomorphic simple \(\mathbb F_p[C_m]\)-modules; thus \(j\equiv p^s\pmod m\) for exactly one \(0\le s<f\), and \(A(x)=u x^{p^s}\) for some \(u\in\mathbb F_q^\times\). These endomorphisms are automorphisms, and all \(u,s\) and all \(v\) occur. If \(A=0\), the condition \(\phi(t)^m=1\) permits all \(v\in V\) when \(j\ne0\), whereas \(j=0\) forces \(v=0\). Consequently
\[
|\operatorname{End}(G)|=fq(q-1)+q(m-1)+1.
\]
The only idempotent automorphism is \(I\).

**2. Singular retraction multiplication.** For \(c\in V\) let \(t_c=c t c^{-1}\), so its affine coordinates are \(((1-a)c,t)\). For \(j\in\mathbb Z/m\mathbb Z\), define \(\rho_{c,j}\) by \(\rho_{c,j}|_V=0\) and \(\rho_{c,j}(t)=t_c^j\). If \(j\ne0\), the coefficient \(1-a^j\) is nonzero, so distinct \(c\)'s give distinct endomorphisms; \(\rho_{c,0}=0\) for every \(c\). Since \(\rho_{c,j}\) kills the kernel, composition on generators gives
\[
\rho_{c,j}\circ\rho_{d,k}=\rho_{c,jk}.
\]
Thus \(\rho_{c,j}\) is idempotent exactly when \(j^2\equiv j\pmod m\). Write the prime-power factorization \(m=\prod_{i=1}^r\ell_i^{h_i}\). By the Chinese remainder theorem, all such residues are the \(2^r\) Boolean choices \(j=1\) or \(0\) modulo each \(\ell_i^{h_i}\). Let \(j_S\) be the idempotent corresponding to the set of factors where the residue is \(1\), and put \(e_{c,S}=\rho_{c,j_S}\). Then \(j_S j_T=j_{S\cap T}\), proving the structure theorem, including \(xyx=xy\).

**3. Commutation and maximality.** The product law implies that two nonzero singular idempotents commute when they share their label \(c\), or when their support intersection is empty; the remaining cases produce distinct nonzero elements with different labels. The elements \(0,I\) commute with all of \(E\).

Let \(F\) be any inclusion-maximal pairwise commuting subset. It contains \(0,I\), and at least one nonzero singular idempotent. For each label \(c\) used in \(F\), let \(B_c\) be the union of the supports of all its members with that label. Different nonempty \(B_c\)'s are disjoint by the commuting criterion. Maximality forces all nonempty subsets of \(B_c\) to be represented: any omitted subset commutes with every member and can be added. It also forces \(\bigcup_cB_c=[r]\): an unused coordinate could be added with any existing label. The sets \(B_c\) consequently partition \([r]\), and their labels are distinct. Conversely, given a function \(\kappa:[r]\to\mathbb F_q\), every set \(\mathcal C_\kappa\) is commuting, closed under products, and maximal: a new support overlapping a differently colored occupied coordinate fails commutation, while one contained in its own color-block is already present. This proves the canonical bijection and the count \(q^r\).

**4. Sizes, distribution, and centralizers.** Each nonempty fiber of \(\kappa\) with cardinality \(s\) contributes precisely \(2^s-1\) nonzero idempotents. The inequality \(2^s-1\ge s\) is strict for \(s>1\), giving the minimum for injective colorings, while \(\sum_i(2^{s_i}-1)\le2^{\sum_i s_i}-1\) is strict with more than one nonempty fiber, giving the maximum for constant colorings. Such injective colorings exist because \(m\mid q-1\) implies \(q\ge r\). A set partition of block-size profile \(\lambda\) has cardinality \(r!/\prod_s(s!)^{m_s}m_s!\); assigning distinct field colors to its blocks gives \((q)_{\underline b}\) choices. Summing yields \(\mathcal P_{r,q}(z)\).

Finally, the nonzero elements commuting with \(e_{c,S}\) consist of all \(2^r-1\) supports at color \(c\), and for each of the \(q-1\) other colors all \(2^{r-s}-1\) nonempty supports disjoint from \(S\). Adding \(0,I\) gives the displayed centralizer formula.

## Verification

Run `python3 artifacts/verify.py` with Python 3; the script uses only the Python standard library. For \((q,m)=(7,6)\) and \((4,3)\), it independently enumerates all group endomorphisms through their images on generators, tests the relations and idempotence, and checks every band product, every commuting adjacency, every centralizer, and every inclusion-maximal commuting family. For \((q,m)=(16,15)\), it checks the explicitly parameterized idempotents and all their pairwise products and maximal commuting families, without claiming a complete enumeration of every group endomorphism in that case. All cases print `CASE_OK`, followed by `VERIFY_OK`.

## Relationship to prior work

Gould, Grau, and Johnson study the *endomorphism monoid of the full transformation semigroup* and prove that its idempotents form a special band. Their object is not the group-endomorphism monoid of a scalar Frobenius group; their multiplication classification therefore neither states nor implies the Boolean-color commutation criterion or maximal-family census here. Their work motivates a structural rather than purely cardinality-based investigation of endomorphism bands.

Wang gives the automorphism group of finite Frobenius groups with elementary-abelian kernel and cyclic complement. His result covers the automorphism part of the endomorphism classification here, which is therefore not claimed as a new automorphism-group theorem; the missing singular retractions and their commuting structure are the subject of this result.

Edmunds develops connections between pairs of commuting idempotent endomorphisms and associative interchange rings, with detailed classifications over *abelian* finite groups. The present group is nonabelian, and the problem here is the complete system of maximal commuting idempotent families, not the classification of interchange operations. His foundational observations about commuting idempotents are acknowledged.

Related results on scalar affine Frobenius groups determine their character-codegree pseudo-algebra; other results determine the invariable-generating graph or relative subgroup commutativity degree. Those quantities do not encode the group-endomorphism composition table, its idempotent band, or the coloring of prime-power factors. The distinct family of irreducible generalized dihedral groups has only one prime divisor in the complement and is excluded from the new multi-prime counting phenomenon.

## Limitations

The irreducibility condition is essential to the classification of nonzero kernel maps as automorphisms. Reducible actions can admit proper nonzero endomorphisms on \(V\), producing additional idempotents. The theorem does not identify maximal commuting subsets of the *entire* endomorphism monoid; only its idempotents are considered. The study establishes exact formulas and verified mathematical implications, not exclusive publication priority. More general descriptions of retractions of Frobenius groups or of semilattice-indexed bands could imply parts of these calculations under other terminology.

## References

1. V. Gould, A. Grau, and M. Johnson, "The structure of End(\(\mathcal T_n\))," arXiv:2307.11596v1, first public 21 July 2023, primary MSC2020 20M05, 20M10, 20M20. https://arxiv.org/abs/2307.11596
2. C. C. Edmunds, "Interchange Rings," *Journal of the Australian Mathematical Society* 101 (2016), 310–334, first public 12 May 2016, DOI 10.1017/S1446788716000112. https://doi.org/10.1017/S1446788716000112
3. L. Wang, "On the automorphism groups of Frobenius Groups," arXiv:1610.05914v1, first public 19 October 2016; Theorem 1.1 determines automorphism groups for elementary-abelian cyclic-complement Frobenius groups. https://arxiv.org/abs/1610.05914
4. "Scalar affine Frobenius groups are rigid under the group pseudo-algebra," publicly available mathematical research record (2026); applies to character codegrees, not endomorphism composition.
5. "Complete bipartite invariable-generation graphs of elementary-abelian cyclic Frobenius groups," publicly available mathematical research record (2026); applies to generation from conjugacy classes, not endomorphism idempotents.
