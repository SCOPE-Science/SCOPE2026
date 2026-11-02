# Divisibility rigidity and exact embedding census for cyclic evolution algebras

## Finding

For a field \(k\) and an integer \(s\ge 1\), let \(C_s(k)\) be the commutative, generally nonassociative \(k\)-algebra with natural basis \(e_0,\ldots,e_{s-1}\) and multiplication \(e_i e_j=0\) for \(i\ne j\), \(e_i^2=e_{i+1}\), with indices modulo \(s\). Let \(\mu_N(k)=\{c\in k^\times:c^N=1\}\).

**Classification theorem.** For any positive integers \(n,m\), every algebra homomorphism \(C_n(k)\to C_m(k)\) is either zero or injective. A nonzero homomorphism exists if and only if \(n\mid m\). When \(n\mid m\), all nonzero homomorphisms are parametrized without repetition by \(r\in\{0,\ldots,n-1\}\) and \(c\in\mu_{2^m-1}(k)\). Writing \(f_0,\ldots,f_{m-1}\) for the target basis, the corresponding homomorphism is uniquely specified by
\[
\Phi_{r,c}(e_0)=\sum_{j=0}^{m/n-1}c^{2^{nj}}f_{r+nj},\qquad
\Phi_{r,c}(e_{i+1})=\Phi_{r,c}(e_i)^2\quad(0\le i<n-1).
\]
The zero map is the only map when \(n\nmid m\). Hence the number of homomorphisms is \(1\) or \(1+n|\mu_{2^m-1}(k)|\), respectively.

**Embedded-subalgebra census.** If \(n\mid m\), the number of distinct subalgebras of \(C_m(k)\) that are isomorphic as algebras to \(C_n(k)\) is
\[
\frac{|\mu_{2^m-1}(k)|}{|\mu_{2^n-1}(k)|}.
\]
They form one orbit under \(\operatorname{Aut}_k(C_m(k))\). In particular, over \(\mathbb F_q\), the numbers of nonzero embeddings and distinct embedded copies are, respectively,
\[
 n\gcd(q-1,2^m-1),\qquad
 \frac{\gcd(q-1,2^m-1)}{\gcd(q-1,2^n-1)}.
\]
For example, \(C_4(\mathbb F_{16})\) has exactly five subalgebras isomorphic to \(C_2(\mathbb F_{16})\), although it has thirty embeddings of that algebra. The \(n=m\) automorphism count is known from existing perfect-evolution-algebra theory, and the \(n=1\) idempotent case is elementary. Both are included as boundaries of the uniform formula, **not** as independent novelty claims. The principal new scope is the strict case \(2\le n<m\).

## Assumptions and scope

All maps are \(k\)-linear multiplication-preserving algebra maps, with no unit requirement because these algebras need not be unital. Integers \(m,n\) are positive, including \(1\), and the field has arbitrary characteristic. The stated classification concerns field-valued points and actual subalgebras, not possibly nonreduced homomorphism schemes. When counting over \(\mathbb F_q\), \(q\) is any prime power. No algebraic-closedness or perfectness hypothesis on \(k\) is used. The strict-embedding assertion is the case \(n<m\).

## Proof

1. Write \(Q(x)=x^2\) for the squaring map of \(C_m(k)\). For any target vector \(x=\sum_{j\in\mathbb Z/m}a_j f_j\), one has \(Q(x)=\sum_j a_j^2 f_{j+1}\). The equality holds in every characteristic because the mixed products of distinct basis vectors vanish. Thus \(\operatorname{supp}(Q(x))=\operatorname{supp}(x)+1\), and \(\operatorname{supp}(Q^t(x))=\operatorname{supp}(x)+t\).

2. Let \(\Phi:C_n(k)\to C_m(k)\) be a homomorphism and put \(v_i=\Phi(e_i)\). The relations force \(v_i=Q^i(v_0)\) and \(Q^n(v_0)=v_0\). If \(v_0=0\), the whole map vanishes. Otherwise the support \(S\) of \(v_0\) is nonempty, is invariant under addition by \(n\) modulo \(m\), and is a union of residue classes modulo \(g=\gcd(m,n)\). Since distinct source basis elements have zero product, the vectors \(v_0,\ldots,v_{n-1}\) have pairwise disjoint supports: indeed, in \(C_m(k)\), \(xy=0\) if and only if the supports of \(x,y\) are disjoint, because the squares \(f_j^2=f_{j+1}\) form a basis.

3. If \(g<n\), the nonempty set \(S\), being invariant under addition by \(g\), meets \(S+g\). This contradicts the disjointness of the supports of \(v_0\) and \(v_g\). Hence \(g=n\), equivalently \(n\mid m\). In this case \(S\) is a union of complete classes modulo \(n\). Disjointness of its first \(n\) shifts forces it to be **exactly one** class \(r+n\mathbb Z\) modulo \(m\) for a unique \(0\le r<n\).

4. Let \(c\ne0\) be the coefficient of \(f_r\) in \(v_0\). From \(Q^n(v_0)=v_0\), the coefficient at \(f_{r+nj}\) is \(c^{2^{nj}}\), for \(j=0,\ldots,m/n-1\), and going once around the target cycle forces \(c^{2^m}=c\). Thus \(c^{2^m-1}=1\). Conversely any such \((r,c)\) gives a vector fixed by \(Q^n\); its first \(n\) shifts have disjoint supports, so extending by \(v_i=Q^i(v_0)\) respects **all** multiplication relations. Uniqueness follows from the support class and coefficient at \(f_r\). All \(v_i\) are nonzero and have disjoint supports, hence they are linearly independent and \(\Phi\) is injective.

5. For \(n=m\), the same classification gives \(|\operatorname{Aut}(C_n(k))|=n|\mu_{2^n-1}(k)|\): all nonzero maps are bijective. For \(n\mid m\), the automorphism group of the source acts freely by precomposition on the embeddings, and two embeddings have the same image exactly when they differ by such a precomposition. The embedding count therefore yields the subalgebra count above. The integer quotient is valid because \(2^n-1\mid 2^m-1\).

6. Rotations \(f_j\mapsto f_{j+t}\) and diagonal automorphisms \(f_j\mapsto d^{2^j}f_j\) with \(d^{2^m-1}=1\) preserve the target multiplication. Rotations move the support residue \(r\) to any other residue; fixing \(r\), the diagonal maps multiply its distinguished coefficient by \(d^{2^r}\). Raising to the \(2^r\)th power permutes \(\mu_{2^m-1}(k)\), since \(2^m-1\) is odd. Consequently the target automorphism group acts transitively on all embeddings, and therefore also on their images.

7. The multiplicative group \(\mathbb F_q^\times\) is cyclic of order \(q-1\), so \(|\mu_N(\mathbb F_q)|=\gcd(q-1,N)\). Substitution gives the finite-field formulas.

## Verification

The standalone \(verify.py\) enumerates **all linear maps** in 17 small finite-field source/target configurations, independently tests their defining multiplication relations, and compares the resulting sets of solutions to the parametrized maps, not merely their cardinalities. The tested fields include \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_8,\mathbb F_{16}\). It also enumerates the explicitly parametrized images and reduces their natural bases to canonical subspace signatures in five configurations, including the five-subalgebra example over \(\mathbb F_{16}\). Execute with `python3 verify.py`; the final success marker is `CYCLIC_EVOLUTION_EMBEDDINGS_OK`.

These finite checks independently test the formulas at the stated small parameters; the all-field theorem is established by the argument above rather than by the enumeration.

## Relationship to prior work

Elduque and Labra (arXiv:1312.4685v1, §§2–4) develop evolution-algebra graphs, a disjoint-support lemma for perfect targets, and finiteness/monomial structure of **automorphisms**. Those results support the present argument but concern natural-basis changes and same-dimensional automorphisms, not proper embeddings between cyclic algebras of different dimensions. The known \(n=m\) case is explicitly acknowledged.

Camacho, Khudoyberdiyev and Omirov (arXiv:1405.7126, §§2–3) distinguish ordinary subalgebras, evolution-algebra subalgebras and subalgebras with an extendable natural basis. In particular, their condition-P analysis of permutation-type evolution algebras does not enumerate the non-extendable cyclic subalgebras or their finite-field arithmetic.

Cadavid, Rodiño Montoya and Rodríguez (arXiv:1710.10516v1, Definition 2.1 and Theorem 2.4) compare two **same-graph, same-dimensional** evolution algebras arising from adjacency and random-walk matrices, using a stronger notion of evolution homomorphism. Their zero-or-isomorphism statement for that context does not cover ordinary proper algebra embeddings of the present directed-cycle algebras.

The 2026 survey by Kaygorodov, Martín González and Viruel (arXiv:2610.22248v1, §2.1.6 and discussion of cyclic algebras) records the diagonal-root and automorphism theory. The new statement here is the strict-divisor embedding criterion, full parameter census and orbit count for \(n<m\), not the already-known automorphism boundary.

## Limitations

No claim is made about homomorphisms of arbitrary weighted/permutation evolution algebras, non-field coefficient rings, or scheme-theoretic nilpotent structure. The claim classifies **embedded copies isomorphic to** the specified cycle algebra, not all subalgebras of the target. Standard full-text comparisons and semantic record searches give a best-knowledge priority assessment, not exhaustive priority certification. Independent mathematical review has not been performed.

## References

- A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (first public 2013-12-17), especially Lemma 4.3 and Theorem 4.8. https://arxiv.org/abs/1312.4685
- L. M. Camacho, A. Kh. Khudoyberdiyev and B. A. Omirov, *On the property of subalgebras of Evolution algebras*, arXiv:1405.7126 (2014-05-28), §§2–3. https://arxiv.org/abs/1405.7126
- P. Cadavid, M. L. Rodiño Montoya and P. M. Rodríguez, *On the isomorphisms between evolution algebras of graphs and random walks*, arXiv:1710.10516v1 (2017-10-28), Theorem 2.4. https://arxiv.org/abs/1710.10516
- I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (2026-10-15), §2.1.6. https://arxiv.org/abs/2610.22248
