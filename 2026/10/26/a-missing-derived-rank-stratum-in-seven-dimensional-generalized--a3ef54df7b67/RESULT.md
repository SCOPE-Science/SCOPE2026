# A missing derived-rank stratum in seven-dimensional generalized mock-Poisson algebras

## Finding

For the canonical seven-dimensional free anticommutative antiassociative algebra \(F\) on three generators, consider all derivation-induced generalized mock-Poisson brackets
\[
\{x,y\}_D=D(x)*y+D(y)*x.
\]
Among those not satisfying the ordinary mock-Poisson compatibility identity, the dimension of the derived mock-Lie space \(W_D=\operatorname{span}_K\{\{x,y\}_D:x,y\in F\}\) is **exactly one of \(1,3,4\)**. Dimension \(2\) is impossible. The two exceptional strata are characterized by scalar and rank-one-perturbed scalar actions of \(D\) on the generator quotient; all other actions yield dimension \(4\). An exact finite-field census of all derivations in the three strata is given below.

## Assumptions and scope

Take a field \(K\) of characteristic zero. All the algebraic statements and formulas also hold over any finite field \(K=\mathbb F_q\) with characteristic greater than \(3\). Let \(V\) have dimension \(3\), and put
\[
F=V\oplus \bigwedge^2V\oplus\bigwedge^3V.
\]
Define the anticommutative product \(*\) by \(v*w=v\wedge w\), \((v\wedge w)*t=v\wedge w\wedge t\), \(t*(v\wedge w)=-v\wedge w\wedge t\) for degree-one vectors \(v,w,t\), and zero whenever total degree exceeds \(3\). This product is antiassociative. For any derivation \(D:F\to F\), let \(A:V\to V\) be its induced map on \(F/F^2=V\). The derivation is uniquely determined by an arbitrary linear choice of its three generator images \(D|_V:V\to F\); in particular, every \(3\)-by-\(3\) matrix \(A\) occurs and has exactly \(q^{12}\) lifts to a derivation over \(\mathbb F_q\).

Write \(W_D\) for the image span of \(\{\cdot,\cdot\}_D\); this is a subspace of \(F\), not an assertion about the abstract isomorphism classes of all generalized mock-Poisson structures. The central parameter is the generator map \(A\), not the higher-degree part of \(D\).

## Proof

**1. The construction and the genuinely generalized condition.** The cited construction of Normatov (Theorem 2.6) proves that \((F,*,\{\cdot,\cdot\}_D,D)\) is a generalized mock-Poisson algebra in characteristic zero. Its proof is an expansion using anticommutativity, antiassociativity and the derivation law, and applies without change in the stated characteristics above \(3\). This theorem is used as a foundation, not claimed as new. In the generalized compatibility identity the correction is \((x*y)*D(z)\). For degree-one generators \(x,y,z\), it is precisely \(x\wedge y\wedge Az\), and it vanishes for all inputs iff \(A=0\), since decomposable two-vectors can wedge nontrivially with any nonzero \(Az\). Thus the generalized algebra is not an ordinary mock-Poisson algebra iff \(A\ne0\).

**2. Reduction to a three-dimensional symmetric-square map.** Decompose the generator values as \(D(v)=Av+Bv+Cv\), with \(B:V\to\bigwedge^2V\) and \(C:V\to\bigwedge^3V\). For \(v,w\in V\), the degree-two component of \(\{v,w\}_D\) is
\[
b_A(v,w)=Av\wedge w+Aw\wedge v,
\]
a symmetric bilinear map factoring through \(S^2V\). The degree-three component depends on \(B\), while \(C\) contributes nothing. On \(\bigwedge^2V\), the degree-two component of the derivation is \(\Lambda^2(A)\) in the derivation-action sense, and for \(v\in V\) and \(\omega\in\bigwedge^2V\) one obtains
\[
\{v,\omega\}_D=((\operatorname{tr}A) v-2Av)\wedge\omega\in\bigwedge^3V.
\]
All brackets with two factors of degree at least two vanish. If \(A\ne0\), the displayed map to \(\bigwedge^3V\) cannot be identically zero: otherwise \((\operatorname{tr}A)I-2A=0\), and taking traces in dimension three yields \(\operatorname{tr}A=0\), hence \(A=0\) in characteristic different from \(2\). The mixed brackets therefore generate the entire one-dimensional top degree. Subtracting top-degree components from brackets on \(V\) shows
\[
\dim_K W_D=1+\operatorname{rank}(b_A)\qquad(A\ne0).
\]
This equality is independent of all twelve higher-degree generator coefficients.

**3. Rank classification of \(b_A\).** In characteristic different from two, \(b_A=0\) iff \(A\) is scalar. Indeed, \(b_A(v,v)=2Av\wedge v\), so if \(b_A=0\), every line of \(V\) is \(A\)-stable; comparing \(e_i\) and \(e_i+e_j\) forces all diagonal eigenvalues equal. Scalars conversely give zero because wedge products cancel.

Suppose \(0<\operatorname{rank}b_A<3\). The annihilator of its image in \((\bigwedge^2V)^*\) contains a nonzero alternating form \(\omega\). For all \(x,y\), its vanishing on \(b_A(x,y)\) says
\[
\omega(Ax,y)=\omega(x,Ay).
\]
A nonzero alternating form on a three-space has a one-dimensional radical \(L\). The displayed relation shows \(A(L)\subseteq L\). On the symplectic two-space \(V/L\), a self-adjoint endomorphism with respect to a nondegenerate alternating form must be scalar, say \(\lambda I\). To verify this without any splitting-field assumption, write the alternating form as \(\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\); the equation \(T^T J=JT\) forces both off-diagonal entries of \(T\) to vanish and the two diagonal entries to agree. Hence \((A-\lambda I)(V)\subseteq L\), so \(\operatorname{rank}(A-\lambda I)\le1\). Since \(A\) is not scalar, this rank is one.

Conversely, let \(A=\lambda I+u\otimes f\) with \(u\ne0\) and \(f\ne0\). Then
\[
b_A(x,y)=u\wedge(f(x)y+f(y)x).
\]
Choose \(a\) with \(f(a)=1\). The values on \((a,a)\) and on \((a,w)\) for \(w\in\ker f\) span \(u\wedge V\), which is a two-dimensional space. Thus \(\operatorname{rank}b_A=2\). These arguments show \(\operatorname{rank}b_A\in\{0,2,3\}\), with exact indicated criteria, and prove the bracket dimensions \(1,3,4\).

For explicit examples, choose generator matrix \(A=I_3\), \(A=\operatorname{diag}(2,1,1)\), and \(A=\operatorname{diag}(1,2,3)\), respectively, and set \(B=C=0\). Each is nonzero in the assumed characteristics and has the required type.

**4. Exact finite-field enumeration.** Over \(\mathbb F_q\), each \(A\) has exactly \(q^{12}\) derivation lifts. The rank-zero \(b_A\) locus comprises the \(q\) scalar matrices, of which one is excluded by \(A=0\). The rank-two locus is the disjoint union, as \(\lambda\) varies over \(\mathbb F_q\), of the rank-one matrices \(A-\lambda I\). This union is disjoint because \((\lambda-\mu)I\) has rank three for distinct scalars, while the difference of two rank-one matrices has rank at most two. The number of rank-one \(3\)-by-\(3\) matrices is \((q^3-1)^2/(q-1)\), by counting outer products of nonzero column and row vectors modulo simultaneous rescaling. The remaining \(q^9-q-q(q^3-1)^2/(q-1)\) matrices are rank-three for \(b_A\). Multiplying each count by \(q^{12}\) gives, in order of bracket dimensions \(1,3,4\),
\[
q^{12}(q-1),\qquad
q^{13}\frac{(q^3-1)^2}{q-1},\qquad
q^{12}\left(q^9-q-q\frac{(q^3-1)^2}{q-1}\right).
\]
They sum to \(q^{12}(q^9-1)\), exactly the number of derivations with \(A\ne0\). This is a count of **labelled derivations on the fixed algebra**, not a count of isomorphism classes of generalized mock-Poisson structures.

## Verification

Run `python3 verify.py` from the package. The checker builds the seven basis vectors, multiplication table and derivation extension directly, then verifies the Leibniz rule for all \(49\) basis pairs on each sampled derivation, calculates the full symmetric-bracket rank, and checks the correction-term witness. It exhaustively counts the \(3^9=19683\) generator matrices over \(\mathbb F_3\) purely as a check of the linear rank lemma; the result is \(3,1014,18666\) for ranks \(0,2,3\) of \(b_A\). The characteristic-three calculation is **not** used to certify the theorem's generalized mock-Poisson assertion in that characteristic. Separate checks test \(2250\) arbitrary or structured derivations over \(\mathbb F_5,\mathbb F_7,\mathbb F_{11}\) including arbitrary higher-degree components, and the three explicit strata in each field. Output terminates with `VERIFY_OK`.

## Relationship to prior work

Normatov, *Generalized Mock-Poisson Algebras: Constructions and Structural Properties*, arXiv:2610.23143v1 (first available 16 October 2026), introduced the definition and derivation construction (Theorem 2.6), established dimension seven as the smallest possible for genuinely generalized examples (Propositions 2.2–2.3), and provided a seven-dimensional example (Example 2.8). Those results are foundational and **not** claimed as new. The present statement instead determines the entire derived-bracket rank spectrum and a precise rank-one matrix boundary for **every derivation** of that minimal algebra, together with exact finite-field multiplicities. Remm's prior deformation-quantization study concerns antiassociative structures and symmetric polarizations; no equivalent derivation-induced bracket-rank enumeration is found in its sections on antiassociativity and polarization. A previously indexed classification of maximal square-zero ideals on the same free algebra concerns the other, anticommutative product and does not imply these bracket ranks.

## Limitations

The theorem is restricted to the canonical minimal seven-dimensional algebra and to brackets induced by derivations. It does not classify all generalized mock-Poisson structures on that algebra up to isomorphism or all non-derivation-induced generalized brackets. The finite-field census counts derivations, not orbit classes. The computation is corroborative and not an infinite-field proof. The possibility that an equivalent rank-stratification theorem follows implicitly from a broader earlier derivation/cohomology classification remains a literature risk.

## References

1. Z. Normatov, *Generalized Mock-Poisson Algebras: Constructions and Structural Properties*, arXiv:2610.23143v1 (2026), Theorem 2.6, Propositions 2.2–2.3 and Example 2.8. https://arxiv.org/abs/2610.23143
2. E. Remm, *Deformation quantization of nonassociative algebras*, arXiv:2201.06627v3 (2023), especially Section 4.2 and Section 6.1; published in *Mathematics* 13 (2025), article 58. https://arxiv.org/abs/2201.06627
