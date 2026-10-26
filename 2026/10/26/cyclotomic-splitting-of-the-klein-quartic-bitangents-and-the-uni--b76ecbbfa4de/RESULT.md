# Cyclotomic splitting of the Klein quartic bitangents and the uniform Frobenius law

## Finding

For the smooth plane Klein quartic
\[
C:\quad X^3Y+Y^3Z+Z^3X=0
\]
over \(\mathbb Q\), the splitting field of the 28 geometric bitangent **lines** is precisely \(K=\mathbb Q(\zeta_7)\), the cyclotomic field of degree six.

For an odd prime power \(q\) with characteristic different from seven, the Frobenius action on the 28 geometric bitangents has the following complete cycle profiles:

| \(q\bmod7\) | Cycle lengths | Number rational over \(\mathbb F_q\) |
|---|---|---:|
| \(1\) | \(1^{28}\) | 28 |
| \(2,4\) | \(1,3^9\) | 1 |
| \(3,5\) | \(1,3,6^4\) | 1 |
| \(6\) | \(1^4,2^{12}\) | 4 |

Equivalently, for all integers \(n\ge1\),
\[
\#\{\text{bitangent lines over }\mathbb F_{q^n}\}=
\begin{cases}
28,&q^n\equiv 1\pmod7,\\
4,&q^n\equiv 6\pmod7,\\
1,&q^n\not\equiv\pm1\pmod7.
\end{cases}
\]
This is a classification of Frobenius on the *entire finite étale bitangent scheme*, not a statement about rationality of tangency points.

## Assumptions and scope

The equation is the specific Klein model written above, over \(\mathbb Z[1/14]\). The count applies to any prime power \(q\) of odd characteristic not seven. This excludes the characteristic-two theta-characteristic pathology and the singular characteristic-seven fiber. All bitangents count as distinct geometric line classes in the dual plane, including hyperflex lines.

## Proof

**1. Smoothness in the permitted characteristics.** The three partial derivatives are \(3X^2Y+Z^3\), \(X^3+3Y^2Z\), and \(Y^3+3Z^2X\). In characteristic three they become \(Z^3,X^3,Y^3\), with no projective common zero. Otherwise, multiplying the equations at a hypothetical singular point gives \(28(XYZ)^3=0\). Outside characteristics two and seven this forces one coordinate to vanish, and then all three vanish, impossible. Hence the plane quartic is smooth over \(\mathbb Z[1/14]\).

**2. Cyclotomic upper bound.** Set \(\zeta=\zeta_7\) and define
\[
a=\zeta-\zeta^6,\qquad b=\zeta^2-\zeta^5,\qquad c=\zeta^4-\zeta^3.
\]
Use Elkies' explicit Klein-model projective automorphisms represented over \(K\) by
\[
G=\operatorname{diag}(\zeta^4,\zeta^2,\zeta),\qquad
H=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},\qquad
S=\begin{pmatrix}a&b&c\\b&c&a\\c&a&b\end{pmatrix}.
\]
The actual involution is a scalar multiple of \(S\), which is sufficient projectively; \(S^2=-7I\). These generate the order-168 automorphism group projectively and preserve \(C\). The line \(L_0:X+Y+Z=0\) is a bitangent because the quartic restriction is \(-(X^2+XY+Y^2)^2\). Its orbit under this group consists of all 28 geometric bitangents, since its stabilizer has order six (Elkies, Section 1.5); alternatively, the exact 28-element reduction in step 3 below provides a lower bound of 28, while a smooth plane quartic in characteristic zero has only 28. Every line in the orbit has coefficients in \(K\). Thus the splitting field \(L\) is a subfield of \(K\).

**3. A complete characteristic-five cyclotomic permutation certificate.** Work in
\[
R=\mathbb F_5[z]/(z^6+z^5+z^4+z^3+z^2+z+1).
\]
The polynomial is irreducible because the order of five modulo seven is six. Reduce \(G,H,S\) with \(\zeta\mapsto z\), act on normalized dual-line row vectors starting at \((1,1,1)\), and take the closure under the three generators. The supplied standalone exact verifier constructs **28 distinct vectors**. For each \(r\in(\mathbb Z/7\mathbb Z)^\times\), replace \(z\) by \(z^r\) in every coordinate and compute the resulting permutation of the 28 vectors. Its cycle profiles are exactly the four rows in the table. All computations use explicit modular polynomial multiplication, reduction, exponentiation for inverses, and exact tuple equality; there are no floating-point operations. In particular, \(r=5\) acts with four cycles of length six, so the cyclotomic Galois action has order six. Because \(K/\mathbb Q\) has degree six, the kernel is trivial; therefore \(L=K\).

**4. Passage to all good odd finite characteristics.** On the smooth genus-three family over \(\mathbb Z[1/14]\), two-torsion of the Jacobian is finite étale, and the odd theta characteristics form a finite étale degree-28 scheme. For a smooth plane quartic, an odd theta characteristic has exactly one section: its effective divisor of degree two uniquely determines a bitangent line. Thus the bitangent scheme is this finite étale scheme, and its specializations remain geometrically distinct and preserve unramified Frobenius permutations. The extension \(K/\mathbb Q\) ramifies only at seven; for any odd \(p\ne7\), Frobenius acts on \(\zeta\) by \(\zeta\mapsto\zeta^p\). For \(q=p^e\), arithmetic Frobenius acts by \(\sigma_{q\bmod7}\), proving all cycle profiles and rational counts, including the characteristic-three fiber.

## Verification

Run \(\texttt{python3 verify_klein_bitangents.py}\) with Python 3 and no nonstandard dependencies. The verifier constructs the 28-orbit inside the explicit 15,625-element residue field, checks \(z^7=1\), checks \(S^2=-7I\), establishes projective normalization, and computes the complete six-element cyclotomic Galois action. Expected final line: \(\texttt{VERIFIED: 28 distinct projective bitangent duals generated by Klein group over 5^6}\). Its output includes every residue class and cycle count. This finite computation certifies the Galois permutation, not the infinite-characteristic specialization theorem, which follows from step 4.

## Relationship to prior work

Elkies gives the explicit order-168 projective automorphism generators, the rational bitangent \(X+Y+Z=0\), and the transitive 28-line orbit. Plaumann–Sturmfels–Vinzant develop exact algorithms for quartic bitangents, but do not state the full cyclotomic splitting and finite-field Frobenius classification for the specific Klein model. Bethea–Brazelton independently recover the transitive geometric automorphism orbit and note four real bitangents; their theorem concerns geometric symmetry rather than the congruence-based arithmetic Frobenius action. The four real bitangents are consistent with the four fixed lines of complex conjugation \(\sigma_6\). The additional result here is the **complete arithmetic cyclotomic action**, its exact minimal field, and the uniform classification for all permitted finite fields.

## Limitations

The claim is specific to this plane Klein model and its odd-characteristic good reductions; it does not extend automatically to twists. It does not classify tangency-point residue fields or any characteristic-two bitangent scheme. The group matrices and classical degree-28 fact are established inputs, and the explicit congruence table may be implicit in nineteenth-century descriptions; an equivalent earlier arithmetic table under other terminology cannot be ruled out. The computational certificate alone would not prove finite-étale specialization; that step uses the standard theory of odd theta characteristics over bases with two invertible.

## References

1. N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1999), especially equations (1.2), (1.3) and the bitangent discussion in Section 1.5. https://library.slmath.org/books/Book35/files/elkies.pdf
2. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104, first posted 2010-08-24; *Journal of Symbolic Computation* 46 (2011), 712–733. https://arxiv.org/abs/1008.4104
3. C. Bethea and T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242, Section 4.1 (2024). https://arxiv.org/html/2410.09242v1

