# Unit-conjugacy profiles and commutant counts for idempotents of the finite magma monoid

## Finding
Fix an integer \(n\ge1\) and a set \(X\) of size \(n\). Let \(\mathcal M(X)\) be the monoid of all binary operations on \(X\) with the product
\[
(\star\triangleleft\circ)(x,y)=\circ(\star(x,y),\star(y,x)).
\]
The idempotents of this monoid admit a complete classification under conjugation by its units; each class has a closed orbit-size formula, and each idempotent has a closed formula for the number of elements of the *entire monoid* commuting with it.

Write \(N=\binom n2\). Every idempotent has the following profile: an unordered multiset of \(d\ge1\) pairs of nonnegative integers \((b_i,c_i)\), and an unordered multiset of \(a\ge0\) nonnegative integers \(h_j\), subject exactly to
\[
d+\sum_{i=1}^{d}b_i=n,\qquad
 a+\sum_{i=1}^{d}c_i+\sum_{j=1}^{a}h_j=N.
\]
Every such profile occurs; two idempotents are conjugate under the unit group if and only if their profiles agree. Let \(m_{b,c}\) be the multiplicity of a pair \((b,c)\) and \(m_t\) the multiplicity of an integer \(t\) in these multisets. The size of the corresponding unit-conjugacy orbit is
\[
\frac{n!\,2^N N!}{
 \bigl(\prod_{i=1}^{d} b_i!\,2^{c_i}c_i!\bigr)
 \bigl(\prod_{j=1}^{a}2\,h_j!\bigr)
 \bigl(\prod_{(b,c)}m_{b,c}!\bigr)
 \bigl(\prod_t m_t!\bigr)}.
\]
Here \(2\,h_j!\) means twice the factorial of \(h_j\), not the factorial of twice \(h_j\). With \(B_i=1+b_i\), \(H_i=1+b_i+2c_i\), and \(L_j=1+h_j\), the *full-monoid commutant* of any idempotent with this profile has cardinality
\[
\boxed{\displaystyle
 |\{g\in\mathcal M(X):g\triangleleft e=e\triangleleft g\}|=
 \prod_{i=1}^{d}\left(\sum_{k=1}^{d}B_k^{b_i}H_k^{c_i}\right)
 \prod_{j=1}^{a}\left(\sum_{k=1}^{d}H_k^{h_j}
       +2\sum_{t=1}^{a}L_t^{h_j}\right).}
\]
Empty products are \(1\); the displayed formulas also apply at \(n=1\).

## Assumptions and scope
The set \(X\) is nonempty and finite; no associative, commutative, or identity axiom is assumed of its individual binary operations. A unit means an invertible element of \((\mathcal M(X),\triangleleft)\), not necessarily a permutation of \(X\). Conjugacy is by those units, whereas the commutant counts *all* (potentially noninvertible) elements. The parameters \(b_i,c_i,h_j\) describe **source-orbit fibers of the retraction**, not values in the original multiplication table.

Let \(Y=X\times X\), and let \(\iota(x,y)=(y,x)\). The flip has \(n\) fixed singleton orbits \((x,x)\) and \(N\) free two-point orbits \(\{(x,y),(y,x)\}\) with \(x\ne y\). The map
\[
 T_\star(x,y)=(\star(x,y),\star(y,x))
\]
is a bijection from binary operations to equivariant maps \(Y\to Y\). It takes \(\star\triangleleft\circ\) to \(T_\circ\circ T_\star\), which is sufficient to preserve idempotency, conjugacy and commutation. Thus the problem is equivalent to that of idempotent equivariant self-maps of this fixed \(C_2\)-set.

For an idempotent equivariant map \(e\), its image \(A=e(Y)\) is an equivariant subset and \(e\) fixes \(A\) pointwise. List the fixed singleton orbits of \(A\) as \(F_1,\ldots,F_d\), and the free orbits of \(A\) as \(Q_1,\ldots,Q_a\). Define \(b_i\) as the number of fixed singleton orbits outside \(A\) mapped to \(F_i\), and \(c_i\) as the number of free orbits outside \(A\) collapsed into \(F_i\). Define \(h_j\) as the number of other free orbits mapped bijectively onto \(Q_j\). A fixed singleton cannot map to a free orbit. These observations give precisely the two conservation equations above.

## Proof
**1. Equivariant-retraction normal form.** An equivariant map \(T:Y\to Y\) is determined by the images of representatives of the \(n\) singleton orbits and \(N\) free orbits. A singleton representative must map to one of the \(n\) singleton points; a free representative may map to any of the \(n^2\) points. This gives \(n^n(n^2)^N=n^{n^2}\) maps, equal to the number of all binary operations, and proves the asserted bijection. The rule for \(\triangleleft\) gives the stated reversed composition identity. An endomap is idempotent exactly when it restricts to the identity on its image, proving the retraction form. A fixed orbit in the image must have a fixed preimage equal to itself, so \(d\ge1\), and the stated conservation equations follow. Conversely, take any profile satisfying these equations, choose the indicated root orbits and disjoint sets of leaf orbits, and map each leaf equivariantly to its assigned root. This constructs an idempotent realizing the profile.

**2. Classification by the unit group.** An equivariant automorphism of \(Y\) permutes its singleton orbits arbitrarily, permutes its free orbits arbitrarily, and independently flips the two points inside each free orbit. Thus its group has order \(n!\,2^N N!\). Conjugation by such a unit carries an equivariant retraction to an isomorphic retraction, preserving root types and the numbers of leaf orbits assigned to every root. Conversely, when the two profile multisets coincide, match like-typed rooted fiber clusters, permute each type of leaf orbit, and use the independent free-orbit flips to match all orientations of maps to free root orbits. These choices define an equivariant automorphism carrying one retraction to the other. This proves that the two multisets give a complete, and nonredundant, classification.

**3. Stabilizer and orbit size.** A unit commuting with \(e\) must act on the image \(A\) as a type-preserving permutation and carry each fiber of \(e\) to the fiber of its new root. For a fixed root of type \((b_i,c_i)\), with its root held fixed, there are \(b_i!\) permutations of its extra singleton orbits, and \(2^{c_i}c_i!\) signed permutations of its free leaf orbits. For a free root of type \(h_j\), with that root orbit held as a set, there are \(h_j!\) permutations of its free leaves, and exactly two coherent choices of orientation for the root and all its leaves. Finally, root clusters with identical profiles can be permuted, contributing \(m_{b,c}!\) and \(m_t!\). Multiplication gives the denominator in the orbit formula. Dividing \(n!2^N N!\) by the stabilizer size proves the formula.

**4. Full commutant.** For any two endomaps \(e,g\), \(eg=ge\) with \(e^2=e\) is equivalent to: (i) \(g(A)\subseteq A\); and (ii) for every \(y\in Y\), the point \(g(y)\) belongs to \(e^{-1}(g(e(y)))\). Indeed, if they commute, apply the equation at a point of \(A\) and at each \(y\); conversely these conditions give the equation pointwise. Require also equivariance of \(g\).

For a fixed root \(F_k\), the fiber \(e^{-1}(F_k)\) contains exactly \(B_k=1+b_k\) fixed singleton points and \(2c_k\) points from free orbits, so its total size is \(H_k=B_k+2c_k\). For a free root \(Q_t\), each specified point of the orbit has exactly \(L_t=1+h_t\) preimages. A source fixed-root cluster \(F_i\) can be sent to a target fixed root \(F_k\) only. After that choice, each of its \(b_i\) singleton leaves has \(B_k\) choices and each of its \(c_i\) free leaves has \(H_k\) equivariant choices, giving \(B_k^{b_i}H_k^{c_i}\); sum over \(k\). A source free-root cluster \(Q_j\) can target a fixed root \(F_k\), with \(H_k^{h_j}\) choices, or a free root \(Q_t\), with two orientations for the image of its root and \(L_t^{h_j}\) choices for its free leaves. Sum these alternatives and multiply over all independent root clusters. This yields exactly the full-monoid commutant formula. There is no hidden requirement that \(g\) be injective on either root set or source fibers.

## Verification
The standalone `verify.py` enumerates all equivariant self-maps on \(X^2\), tests idempotency by literal composition, extracts profiles from actual fibers, enumerates all unit conjugations, and counts commutants by literal pairwise composition. For \(n=2\), it examines all \(16\) maps and all \(7\) idempotents, finding \(4\) unit orbits; it checks the commutant formula for all \(7\) idempotents. For \(n=3\), it examines all \(19{,}683\) maps and all \(706\) idempotents, finding \(31\) unit orbits; it checks every predicted unit orbit and the commutant count on one representative from each orbit. The script prints `VERIFY_OK` for both sizes. These are finite spot checks; the unrestricted-\(n\) theorem follows from the structural proof above, not from enumeration. An additional independent direct check used multiplication tables and the literal operation \(\star\triangleleft\star\) to recover \(7\) and \(706\) at \(n=2,3\).

## Relationship to prior work
López-Permouth, Owusu-Mensah and Rafieipour introduced and investigated the magma monoid, including its group of units (2022). López-Permouth's 2026 open-access article characterizes and counts idempotents and describes kernel-cokernel decompositions. Baiduk and Kozerenko's July 2026 work supplies a general transformation-semigroup treatment, including idempotency and enumerations. Ruiz-Medina's 2025 open-access paper counts equivariant endomaps and units for general finite group actions. These results supply important background but the accessible inspected text does not give the simultaneous unit-conjugacy profile classification, the explicit orbit sizes, or the *full-monoid* commutant formula above. Unlike the known global totals, the formulas here distinguish individual idempotent types and quantify their symmetries and commuting partners. The Baiduk–Kozerenko full text was not accessible for a complete theorem-by-theorem comparison; the originality assessment therefore remains subject to that specific risk.

## Limitations
The formulas concern conjugation by units, not a broader semigroup notion of conjugacy, and count centralizers inside the full binary-operation monoid, not its unit group alone. They do not enumerate semigroup Green classes, classify non-idempotents, or establish distinct conjugacy properties of the underlying individual magmas. The finite computations cover only \(n=2,3\) and cannot substitute for the proof. The absence of an identified equivalent theorem is not proof of unique priority; the closely related July 2026 preprint and any inaccessible historical treatments could contain equivalent statements. Source figures for global idempotent totals are not used as proof here, since the small cases are verified independently.

## References
1. Y. Baiduk and S. Kozerenko, “Transformation Semigroup Perspective on the Magma Monoid,” arXiv:2607.13746v1 (first public 2026-07-15), https://arxiv.org/abs/2607.13746; journal version DOI 10.1007/s00233-026-10659-x.
2. S. R. López-Permouth, “Idempotent elements in binary and s-ary magma monoids,” São Paulo Journal of Mathematical Sciences (2026), DOI 10.1007/s40863-025-00519-x, https://link.springer.com/article/10.1007/s40863-025-00519-x.
3. S. R. López-Permouth, I. Owusu-Mensah, and A. Rafieipour, “A monoid structure on the set of all binary operations over a fixed set,” Semigroup Forum 104 (2022), 667–688, DOI 10.1007/s00233-022-10280-8.
4. R. H. Ruiz-Medina, “Cardinalities in finite monoids of \(G\)-equivariant functions,” arXiv:2503.03772v1 (2025), https://arxiv.org/html/2503.03772v1.
