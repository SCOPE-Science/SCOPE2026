# Exact conjugacy classes of anisotropic Leibniz-algebra automorphisms over finite fields

## Finding

Let \(q\) be any **odd prime power**, let \(k=\mathbb F_q\), and choose a nonsquare \(d\in k^\times\). Define the three-dimensional left Leibniz algebra \(L_d\) with basis \(e_1,e_2,z\) and bracket
\[
[e_1,e_1]=z,\qquad [e_2,e_2]=-d z,\qquad
[e_1,e_2]=[e_2,e_1]=[z,L_d]=[L_d,z]=0.
\]
This algebra has two-step nilpotency, one-dimensional centre, and anisotropic quadratic bracket on \(L_d/kz\). Its automorphism group \(G_q=\operatorname{Aut}_k(L_d)\) has order \(2q^2(q^2-1)\), and its **complete conjugacy-class size distribution** is the following. Put \(Q=q^2\).

| Class description | Number of classes | Size of each class |
| --- | ---: | ---: |
| Identity | \(1\) | \(1\) |
| Nonidentity translations | \(1\) | \(Q-1\) |
| Nontrivial scalar slopes from \(k^\times\) | \(q-2\) | \(Q\) |
| Non-scalar slopes, paired by field conjugation | \((Q-q)/2\) | \(2Q\) |
| Semilinear slopes of norm other than \(1\) | \(q-2\) | \(Q(q+1)\) |
| Norm-one semilinear slopes, zero trace obstruction | \(1\) | \(q(q+1)\) |
| Norm-one semilinear slopes, nonzero trace obstruction | \(1\) | \(q(Q-1)\) |

Consequently the exact class number, commuting probability, number of ordered commuting pairs, and number of nonidentity involutions are
\[
\boxed{k(G_q)=\frac{q^2+3q}{2}},\qquad
\boxed{\operatorname{cp}(G_q)=\frac{q^2+3q}{4q^2(q^2-1)}},
\]
\[
\boxed{\#\{(g,h)\in G_q^2:gh=hg\}
       =q^2(q^2-1)(q^2+3q)},\qquad
\boxed{\#\{g\in G_q:g^2=1,\ g\ne1\}=2q^2+q}.
\]
The nonidentity involutions form **exactly two conjugacy classes**, of sizes \(q^2\) and \(q(q+1)\). These formulas depend only on \(q\), not on the chosen nonsquare \(d\).

## Assumptions and scope

The characteristic must be odd; the anisotropic two-dimensional norm form underlying this specific family does not occur over a finite field of characteristic two. The asserted conjugacy classes are ordinary inner-conjugacy classes in the full group of \(k\)-linear bracket-preserving automorphisms, not classes under all abstract group automorphisms. Involution means an element of order exactly two; the identity is not counted. All formulas hold for every odd prime power, including nonprime fields.

## Proof

**1. Identification of the automorphism group.** Let \(K=k(\sqrt d)=\mathbb F_{q^2}\), with \(\sigma(u)=u^q\) and \(N(u)=u\sigma(u)\). Identify \(L_d/kz\) with \(K\) by \(e_1\mapsto1\) and \(e_2\mapsto\sqrt d\). The bracket is \([u,v]=B(u,v)z\) for
\[
B(u,v)=\tfrac12\operatorname{Tr}_{K/k}(u\sigma(v)),
\qquad B(u,u)=N(u).
\]
Since \(B\) is nondegenerate, the centre is exactly \(kz\). Thus every automorphism has a unique form
\[
(u,\tau z)\longmapsto
(Au,\,[\ell(u)+\mu\tau]z),
\]
where \(A\in\operatorname{GL}_k(K)\), \(\ell\in\operatorname{Hom}_k(K,k)\), \(\mu\in k^\times\), and \(B(Au,Av)=\mu B(u,v)\). Conversely each such triple is an automorphism.

All similitudes of this anisotropic binary form are exactly
\[
A(u)=a\sigma^\epsilon(u),
\qquad a\in K^\times,\quad \epsilon\in\{0,1\},
\quad\mu=N(a).
\]
Indeed, given a similitude, divide its value \(a=A(1)\) out of its action. The resulting isometry fixes \(1\), hence preserves the orthogonal line \(k\sqrt d\), and maps \(\sqrt d\) to one of \(\pm\sqrt d\). These two isometries are the identity and \(\sigma\), respectively. The converse follows immediately from multiplicativity of the norm. Because \(B\) is nondegenerate, uniquely write \(\ell(u)=B(v,Au)\) for \(v\in K\). In these coordinates, composition is
\[
(v,A)(w,C)=(v+A(w),AC).
\]
Therefore \(G_q\cong K^+\rtimes(K^\times\rtimes\langle\sigma\rangle)\), acting on \(K\) by \(u\mapsto v+a\sigma^\epsilon(u)\). In particular, \(|G_q|=2Q(Q-1)\).

**2. Classes with \(\epsilon=0\).** Write an affine element as \(f(u)=a u+b\). When \(a=1\), all nonzero \(b\) are conjugate under multiplications by \(K^\times\); these form one class of size \(Q-1\), besides the identity. When \(a\ne1\), conjugation by a translation removes \(b\) because \(1-a\) is invertible. Multiplicative conjugation leaves \(a\) unchanged, whereas \(\sigma\) replaces \(a\) by \(a^q\). The singleton Frobenius orbits are the \(q-2\) elements \(a\in k^\times\setminus\{1\}\), giving classes of size \(Q\); the remaining \(Q-q\) elements lie in \((Q-q)/2\) two-element orbits, giving class size \(2Q\).

**3. Classes with \(\epsilon=1\).** Write an element as \(f(u)=a\sigma(u)+b\). Conjugating by multiplication by \(c\in K^\times\) changes the slope to \(c a/\sigma(c)\); hence the norm \(t=N(a)\in k^\times\) is invariant. The map \(c\mapsto c/\sigma(c)\) has image the entire norm-one subgroup, of size \(q+1\). Consequently all slopes with the same norm are multiplicatively conjugate. For \(t\ne1\), the \(k\)-linear map \(1-a\sigma\) is invertible: a nonzero fixed vector would imply \(N(a)=1\). Thus translations remove \(b\). Each of the \(q-2\) nonunit norm values gives one class containing \(Q(q+1)\) elements.

For \(t=1\), multiplicative conjugation normalizes the slope to \(1\), leaving \(f(u)=\sigma(u)+b\). Translation conjugation changes \(b\) by an element of \((1-\sigma)K\), which equals the trace-zero \(k\)-line because \(q\) is odd. The stabilizer of the normalized slope among multiplications is \(k^\times\), which scales the trace of \(b\). Thus there are exactly two classes according as \(\operatorname{Tr}_{K/k}(b)\) is zero or nonzero. For each of the \(q+1\) norm-one slopes, there are \(q\) admissible translation parameters in the first class and \(Q-q\) in the second, giving \(q(q+1)\) and \(q(Q-1)\) elements respectively. This proves every row of the table; their sizes add to \(2Q(Q-1)\), so none are omitted.

**4. Corollaries and involutions.** Adding the number of classes gives \((Q+3q)/2\). The standard identity \(\#\{(g,h):gh=hg\}=|G_q|k(G_q)\) gives the commuting formulas. An ordinary affine map \(u\mapsto au+b\) is a nonidentity involution exactly when \(a=-1\), yielding \(Q\) elements. A semilinear map squares to \(u\mapsto N(a)u+b+a\sigma(b)\); it is an involution exactly when \(N(a)=1\) and \(b+a\sigma(b)=0\). For each of the \(q+1\) norm-one slopes, the latter equation has exactly \(q\) solutions (the operator is conjugate to \(1+\sigma\)). These are precisely the zero-trace semilinear class, so the two involution classes have sizes \(Q\) and \(q(q+1)\), totaling \(2Q+q\).

## Verification

The accompanying self-contained `check_semiaffine.py` independently enumerates bilinear similitudes, affine-semilinear group elements, exact conjugacy classes by inner conjugation, and all order-two elements. It tests \(q=3,5,7,9\). The \(q=9\) test uses \(\mathbb F_3[u]/(u^2+1)\) to verify a nonprime field. In all four fields every predicted class-size multiplicity, the group order, the class number, and the involution count were checked exhaustively. Execute with `python3 check_semiaffine.py`; expected terminator: `ALL_EXACT_CHECKS_PASSED`. Finite checks are corroboration, not a substitute for the argument covering all odd prime powers.

For \(q=3\) the class-size frequency distribution is \(1:1,8:1,9:1,12:1,18:3,24:1,36:1\), giving nine classes in a group of order \(144\). For \(q=9\) there are \(54\) classes in a group of order \(12{,}960\).

## Relationship to prior work

Kurdachenko, Pypka and Semko identify the automorphism-group structure of three-dimensional nilpotent Leibniz algebras of the relevant anisotropic type in the 2023 preprint (Theorem 3.7), including the 2024 journal treatment (Theorem 3.1). Their 2026 full classification explicitly incorporates this anisotropic type as previously known. The automorphism-group structure is **not** asserted to be new here. Fulman and Guralnick develop a general class-counting orbit method for classical affine groups, including affine general-linear, unitary, symplectic and orthogonal groups; their Lemma 2.1 is relevant methodology but does not state the present class-size table for the affine binary **similitude** subgroup. The semilinear group \(\operatorname{A\Gamma L}_1(\mathbb F_9)\) is known in small-group databases, so its \(q=3\) specialization is not itself an originality claim.

The assessed refinement is the **uniform, exact norm/trace-stratified inner-conjugacy distribution for the full automorphism group of this Leibniz family**, together with the two involution classes and the derived commuting probability for every odd prime power. Equivalent formulas might exist under affine semilinear group or general orthogonal-similitude nomenclature.

## Limitations

Only the anisotropic three-dimensional family and odd characteristics are treated. The assertion is about conjugacy within the full \(k\)-linear algebra automorphism group, not the automorphisms of the abstract group. The result does not determine irreducible character degrees or conjugacy behavior in isotropic forms. An equivalent general semilinear-group conjugacy enumeration in older or unindexed literature remains a priority risk. The finite computations check four fields, while the stated infinite family relies on the proof.

## References

1. L. A. Kurdachenko, O. O. Pypka and M. M. Semko, *On the automorphism groups of some nilpotent 3-dimensional Leibniz algebras*, arXiv:2310.11180v1, posted 2023-10-17, especially Section 3 and Theorem 3.7. https://arxiv.org/abs/2310.11180
2. J. Fulman and R. Guralnick, *Enumeration of conjugacy classes in affine groups*, arXiv:2112.15219v1, posted 2021-12-30, especially Lemma 2.1 and Sections 3–4. https://arxiv.org/abs/2112.15219
3. D. J. S. Robinson, standard finite-group identity relating conjugacy-class count and commuting pairs; also follows by summing centralizer orders over classes. The identity is reproved in the preceding counting argument.
4. L. Kurdachenko, O. Pypka and M. Semko, *On the structure of automorphism groups of some low-dimensional Leibniz algebras*, Ukrainian Mathematical Journal 76 (2024), 864–876 (Ukrainian edition), especially Theorem 3.1. https://umj.imath.kiev.ua/index.php/umj/article/download/7868/10033/23362
5. L. Kurdachenko, O. Pypka and M. Semko, *Automorphism Groups of Three-Dimensional Leibniz Algebras: A Complete Description*, arXiv:2609.24320v1, Section 2 and final classification table. https://arxiv.org/abs/2609.24320
