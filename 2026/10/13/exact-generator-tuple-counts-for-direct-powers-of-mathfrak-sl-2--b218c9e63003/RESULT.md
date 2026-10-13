# Exact generator-tuple counts for direct powers of \(\mathfrak{sl}_2(\mathbb F_q)\)

## Finding

For every prime power \(q\), every integer \(k\ge1\), and every integer \(r\ge1\), let \(L_q=\mathfrak{sl}_2(\mathbb F_q)\), and let \(N_{q,k}(r)\) be the number of ordered \(r\)-tuples of elements of the direct-product Lie algebra \(L_q^{\oplus k}\) whose generated \(\mathbb F_q\)-Lie subalgebra equals the whole direct product. Put
\[
G=q^r(q^r-1)(q^r-q),\qquad A=q(q^2-1).
\]
Then the **complete direct-power generation count** is
\[
\boxed{N_{q,k}(r)=
\begin{cases}
\displaystyle\prod_{j=0}^{k-1}(G-jA),&q\text{ odd and }k\le G/A,\\[2mm]
0,&q\text{ odd and }k>G/A,\\[1mm]
\displaystyle q^{kr}\prod_{j=0}^{2k-1}(q^r-q^j),&q\text{ even and }r\ge2k,\\[2mm]
0,&q\text{ even and }r<2k.
\end{cases}}
\]
In odd characteristic \(G/A\) is a nonnegative integer. Consequently, the maximum number of direct factors which an ordered \(r\)-tuple can generate is exactly \(G/A\) when \(q\) is odd, whereas it is exactly \(\lfloor r/2\rfloor\) when \(q\) is even. For \(r=2\), the odd-characteristic maximum is \(q^2(q-1)\), while the even-characteristic maximum is one. Despite this discontinuity, the one-factor count \(N_{q,1}(r)=G\) holds in **every** characteristic.

## Assumptions and scope

The base field is the finite field \(\mathbb F_q\), with \(q\) any prime power, including nonprime fields and fields of characteristic two or three. The Lie bracket on \(\mathfrak{sl}_2\) is the ordinary matrix commutator, and direct products have componentwise bracket. All generation, linear spans, Lie subalgebras, and automorphisms in the theorem are taken over the full field \(\mathbb F_q\), not merely its prime subfield. Repetitions and zero elements in the ordered tuple are allowed. For \(r=1\) both formulas give zero as required. For \(k=1\) the formulas coincide in both characteristics.

## Proof

**1. The one-factor count.** Let \(L\) be any three-dimensional Lie algebra over \(\mathbb F_q\), and let \(t\) be the number of its two-dimensional Lie subalgebras. An ordered \(r\)-tuple generates \(L\) precisely when its linear span is either all of \(L\), or a two-dimensional plane which is not a Lie subalgebra: two linearly independent vectors spanning a nonclosed plane already generate all of the three-dimensional algebra, while a tuple contained in a proper Lie subalgebra cannot generate \(L\).

The number of ordered \(r\)-tuples spanning the three-dimensional vector space is
\[
(q^r-1)(q^r-q)(q^r-q^2).
\]
For each fixed plane, the number with linear span equal to that plane is \((q^r-1)(q^r-q)\). There are \(q^2+q+1-t\) non-subalgebra planes. Thus the exact count of Lie-generating tuples is
\[
(q^r-1)(q^r-q)(q^r+q+1-t).
\]
We show \(t=q+1\) for \(L_q\) in all characteristics. When \(q\) is odd, the nondegenerate invariant trace form \(\langle X,Y\rangle=\operatorname{tr}(XY)\) on the traceless matrices makes the bracket of any basis of a plane \(W\) orthogonal to \(W\). Since \(L_q=[L_q,L_q]\) and \(\dim L_q=3\), the linear bracket map \(\bigwedge^2L_q\longrightarrow L_q\) is an isomorphism; in particular, the bracket of a basis of \(W\) is nonzero. The plane is bracket-closed exactly when its trace-orthogonal line \(\mathbb F_q Z\) lies in \(W=Z^\perp\), equivalently \(\operatorname{tr}(Z^2)=0\). Writing
\[
Z=\begin{pmatrix}a&b\\c&-a\end{pmatrix}
\]
this is the nonsingular projective conic \(a^2+bc=0\), with exactly \(q+1\) rational points. When \(q\) is even, the scalar identity matrix lies in \(L_q\) and is central, and the ordinary upper- and lower-triangular matrix units bracket to this identity. Hence \(L_q\) is a three-dimensional Heisenberg Lie algebra. A plane is bracket-closed exactly when it contains the one-dimensional center, giving \(q+1\) planes. Substituting \(t=q+1\) yields \(G=q^r(q^r-1)(q^r-q)\), with no characteristic exception.

**2. Odd characteristic: direct powers of a simple algebra.** For odd \(q\), \(L_q\) is a perfect simple \(\mathbb F_q\)-Lie algebra. Its full \(\mathbb F_q\)-linear automorphism group is \(\operatorname{PGL}_2(q)\) acting by matrix conjugation, of order \(A=q(q^2-1)\). One way to verify fullness is that automorphisms preserve the nondegenerate Killing form and the bracket tensor, so embed in the corresponding three-dimensional special orthogonal group, which has order \(q(q^2-1)\); the conjugation action of \(\operatorname{PGL}_2(q)\) is faithful and attains that order.

The automorphism group acts freely on the set of generating ordered \(r\)-tuples: an automorphism fixing every generator fixes the entire Lie algebra. Thus those tuples form exactly \(G/A\) automorphism orbits.

A subdirect product of copies of a nonabelian simple perfect Lie algebra is a direct product of diagonally embedded blocks of factors. This follows inductively from the Lie-algebra Goursat lemma: a subdirect product in \(L^{\oplus s}\oplus L\) is either the entire product or the graph of an isomorphism between the new factor and one simple factor of the already classified subdirect product. Consequently, if \(r\) generators project onto every factor, they generate the full direct product **if and only if** their \(k\) projected generating \(r\)-tuples lie in pairwise distinct \(\operatorname{Aut}(L_q)\)-orbits. Given a generating tuple in the first factor, exactly \(G-A\) generating tuples avoid its orbit in the second, then \(G-2A\) avoid the first two orbits, and so on. This proves the falling-product formula and the sharp capacity \(G/A\).

**3. Even characteristic: a Heisenberg direct product.** For even \(q\), each \(L_q\) is the three-dimensional Heisenberg Lie algebra, with derived algebra equal to its one-dimensional center. Therefore \(L_q^{\oplus k}\) has \(2k\)-dimensional abelianization and \(k\)-dimensional center. An ordered tuple generates the direct product **if and only if** its images span the entire abelianization. Necessity is immediate. For sufficiency, let \(S\) be the Lie subalgebra generated by a tuple surjecting onto the abelianization. The bracket of arbitrary cosets in the abelianization is well-defined (because the center brackets trivially), and its values span the entire derived algebra: in each factor, the two standard quotient basis vectors bracket to the central basis element. All those bracket values therefore lie in \([S,S]\subseteq S\), and since \(S\) also surjects onto the quotient, \(S=L_q^{\oplus k}\).

The number of ordered \(r\)-tuples spanning a \(2k\)-dimensional \(\mathbb F_q\)-space is
\[
\prod_{j=0}^{2k-1}(q^r-q^j)
\]
when \(r\ge2k\), and is zero otherwise. Each quotient tuple has exactly \(q^{kr}\) independent choices of its central coordinates. This gives the even-characteristic formula. Setting \(k=1\) simplifies to \(q^r(q^r-1)(q^r-q)=G\), completing the compatibility check and the theorem.

## Verification

The supplied `verify.py` uses standard-library finite-field arithmetic for fields of orders \(2,3,4,5\) (including a polynomial basis for \(\mathbb F_4\)), constructs Lie subalgebra closures by repeated brackets and row reduction, and verifies the one-factor generating-pair counts by exhaustive enumeration. It independently enumerates all projective planes, finding exactly \(q+1\) closed planes in every tested field. For odd \(q\in\{3,5\}\), it enumerates the full projective conjugation group acting on generating pairs, verifies free orbits, and checks the two-factor falling-product count. For even \(q\in\{2,4\}\), it independently enumerates full-rank quotient tuples for the specified \((k,r)\) cases. It additionally checks one-factor generating triples for \(q=2,3\). Execute with `python verify.py`; the final output line is `VERIFY_OK`.

The finite checks test the proof but do not prove the unrestricted prime-power, factor-count, or word-length quantifiers; those follow from the preceding linear-algebra and Goursat arguments.

## Relationship to prior work

Bois studied Lie-generator varieties and minimal generator numbers over algebraically closed fields, including direct sums of classical simple Lie algebras (arXiv:0708.1711, Section 2.2.5). This gives a strong existence antecedent but neither finite-field generator-tuple multiplicities nor the finite-field characteristic-two change from a simple to a Heisenberg factor. Ionescu's earlier semisimple-generation study concerns existence and remains an additional bibliographic priority risk because full text was not obtainable. The published three-dimensional plane-count result of Towers and collaborators gives \(t=q+1\) for perfect three-dimensional algebras and the three-dimensional Heisenberg algebra; the one-factor plane count is therefore credited as known, not presented as a separate novel theorem. Classical subdirect-product/Goursat and automorphism-orbit methods also precede this result; the claimed additional content is their explicit finite-field synthesis into the **all-arity, all-direct-power enumeration and sharp characteristic-dependent capacity**.

Allcock–Santha–Yuan–Zhang (arXiv:2506.05733) investigate constructive direct-power generation in dynamical Lie algebras and quantum circuits, rather than counts over finite fields. The analogous generating-graph theory for direct powers of finite simple **groups** (Burness–Crestani, 2012) is an important conceptual precedent but is not a statement about Lie brackets or the characteristic-two degeneration here.

## Limitations

The theorem concerns full-field Lie generation by unrestricted ordered elements; it does not count tuples subject to restrictions such as nilpotency, conjugacy class, or choice from a designated subspace. The general formula does not assert an unproved classification of Lie generating varieties beyond this family. The formulas were internally proof-reviewed and computationally tested; independent mathematical audit is not claimed. An inaccessible historical semisimple-generation paper and possible equivalent general Hall-type statements leave a residual bibliographic-priority uncertainty. The reported originality refers to the combined exact finite-field characteristic dichotomy, not to the separately classical tools.

## References

1. J.-M. Bois, *Generators of simple Lie algebras in arbitrary characteristics*, arXiv:0708.1711 (first submitted 13 August 2007), especially Sections 1 and 2.2.5. https://arxiv.org/abs/0708.1711.
2. T. Ionescu, *On the generators of semisimple Lie algebras*, Linear Algebra Appl. 15 (1976), 271–292. DOI 10.1016/0024-3795(76)90033-1.
3. Published 2026 result, *Plane counts control subalgebra commutativity in dimension three*, identifier 2026/9/18/SCOPE-plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c (its plane counts and perfect-case conic are credited).
4. J. Allcock, M. Santha, P. Yuan and S. Zhang, *On generating direct powers of dynamical Lie algebras*, arXiv:2506.05733 (2025). https://arxiv.org/abs/2506.05733.
5. T. C. Burness and E. Crestani, *On the generating graph of direct powers of a simple group*, J. Algebraic Combin. 38 (2013), 329–350 (online 26 October 2012), DOI 10.1007/s10801-012-0405-x.
