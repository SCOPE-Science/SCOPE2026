# Discriminant completion makes reduced double-section plane curves free

## Finding

**Theorem.** Fix an integer \(d\ge3\) and nonzero \(L\in\mathbb C[y,z]_{d-2}\), together with \(Q\in\mathbb C[y,z]_{d-1}\) and \(R\in\mathbb C[y,z]_d\). Define
\[
F=x^2L+xQ+R,\qquad D=Q^2-4LR,\qquad f=FD.
\]
If \(f\) is nonzero and reduced in \(\mathbb C[x,y,z]\), then \(V(f)\subset\mathbb P^2_{\mathbb C}\) is a free plane curve of degree \(3d-2\), with exponents \(\boxed{(d,2d-3)}\). In particular, the two syzygies displayed below are a free homogeneous basis of its Jacobian-syzygy module.

**Geometric specialization.** For a smooth complex plane cubic \(E\) and **any** point \(p\in E\), the central projection \(E\to\mathbb P^1\) from \(p\) has degree two and four distinct ramification directions. Adjoining to \(E\) the four lines through \(p\) corresponding to those directions yields a free septic with exponents \((3,3)\). This includes nonflex and flex centers. The theorem does not assert that the result is supersolvable at every center.

## Assumptions and scope

All statements are over \(\mathbb C\) and use the ordinary projective grading. The polynomial \(L\) has exact degree \(d-2\), and the indicated degrees of \(Q,R\) allow zero forms. The reducedness condition means that \(F\) is reduced, \(D\) is squarefree, and \(F,D\) have no common irreducible factor. The homogeneous binary form \(D\) has degree \(2d-2\) and, if reduced, gives that number of distinct lines through \(p=[1:0:0]\). For each direction, the residual intersection after removing the fixed multiplicity \(d-2\) at \(p\) is described by a quadratic, with discriminant \(D\). No smoothness or irreducibility assumption is imposed on \(F\) beyond reducedness of \(f\).

The hypothesis is nonempty in every degree: take \(Q=0\), take \(L\) to be the product of \(d-2\) distinct binary linear forms, and \(R\) to be the product of \(d\) further, all distinct, binary linear forms. Then \(D=-4LR\) is squarefree. Since \(-R/L\) is not a square in \(\mathbb C(y,z)\), the polynomial \(x^2L+R\) is irreducible in \(\mathbb C[x,y,z]\) by Gauss's lemma. Its restriction to no factor line of \(LR\) is identically zero, so \(f\) is reduced.

## Proof

Write \(N=3d-2\), \(A=F_x=2xL+Q\), and introduce the homogeneous polynomials
\[
H=L_zF_y-L_yF_z,\qquad
T=2(F_{xz}F_y-F_{xy}F_z).
\]
They have respective degrees \(2d-4\) and \(2d-3\). Define coefficient triples
\[
S_1=(xA-NF,\ yA,\ zA),
\]
\[
S_2=(4xH-NT,\ ND_z+4yH,\ -ND_y+4zH).
\]
Each entry of \(S_1\) has degree \(d\) and each entry of \(S_2\) has degree \(2d-3\).

**First syzygy.** Because \(D\) depends only on \(y,z\), one has \(f_x=A D\). Euler's identity gives \((x,y,z)\cdot\nabla f=Nf\), so
\[
S_1\cdot\nabla f=A(Nf)-NF(AD)=0.
\]

**Second syzygy.** The exact polynomial identities
\[
D=A^2-4LF,
\qquad D_zF_y-D_yF_z=AT-4FH
\]
follow by differentiation of the first identity and cancellation of terms involving \(L F_y,L F_z\). Consequently,
\[
D_zf_y-D_yf_z=D(D_zF_y-D_yF_z)=D(AT-4FH).
\]
Using Euler's identity again yields
\[
\begin{aligned}
S_2\cdot\nabla f
&=4H(Nf)-N\bigl(Tf_x-D_zf_y+D_yf_z\bigr)\\
&=4H(NFD)-N\bigl(TAD-D(AT-4FH)\bigr)=0.
\end{aligned}
\]

**Nonzero Saito determinant.** Row operations using the displayed definitions reduce the determinant to
\[
\begin{aligned}
\det\!\begin{pmatrix}
x&y&z\\
xA-NF&yA&zA\\
4xH-NT&ND_z+4yH&-ND_y+4zH
\end{pmatrix}
&=-N^2F(yD_y+zD_z)\\
&=-N^2(2d-2)FD,
\end{aligned}
\]
where the last equality uses the degree \(2d-2\) of \(D\). The scalar \(-N^2(2d-2)\) is nonzero in characteristic zero. Since \(f\) is reduced, Saito's determinant criterion applies to the Euler derivation and these two annihilating derivations. It proves freeness and identifies \(S_1,S_2\) as a basis, with exactly the claimed degrees.

For the cubic specialization, choose coordinates placing \(p\) at \([1:0:0]\). Since \(p\in E\) and \(E\) is smooth there, its equation has the displayed form with \(d=3\) and \(L\ne0\). The residual quadratic after subtraction of the fixed intersection at \(p\) defines the degree-two map to the pencil of lines. In characteristic zero, each ramification index of a degree-two map is two; Riemann–Hurwitz gives total ramification \(2g(E)-2+2\cdot 2=4\), hence four *distinct* ramification points and four distinct branch directions. Thus \(D\) is squarefree, and the irreducible cubic \(F\) does not divide the binary form \(D\). The free-divisor theorem applies.

## Verification

The supplementary script `verify.py` performs exact symbolic expansion for \(d=3,4,5\), checking \(D=A^2-4LF\), the differentiated identity, both Jacobian syzygies, and the precise determinant scalar. It uses SymPy and prints `VERIFY_OK` if all tests succeed. Those finite tests corroborate but do not replace the all-degree derivation above. The determinant identity is valid for every choice of the input forms and does not rely on genericity.

## Relationship to prior work

Dimca, Ilardi, Pokora and Sticlaru (2023), *Construction of free curves by adding lines to a given curve*, construct other families by adding special tangent lines and propose that supersolvable plane curves are free. Their Theorem 1.11 treats projection centers outside the starting curve under additional assumptions; their Thom–Sebastiani construction concerns a different input family. The present theorem treats centers of multiplicity \(d-2\) on the initial curve and is proved directly without a supersolvability assumption.

Di Gennaro, Ilardi, Miró-Roig, Schenck and Vallès (2023), *Free curves, Eigenschemes and Pencils of curves*, give broad eigenscheme and pencil criteria. Their Theorems 2.5 and 3.6 impose a finite eigenscheme or a pencil-factor hypothesis; the displayed first syzygy here has a positive-dimensional eigenscheme, as its minors with the Euler row have the common factor \(F\). Their results therefore do not directly imply the stated universal discriminant-completion theorem. Vallès (2015) concerns unions of members of a same-degree pencil with smooth base locus, again a different construction. Bannai and Tokunaga (2019) study cubic–tangent-line arrangements from a topological perspective. These comparisons do not establish absolute priority against all possible literature.

## Limitations

Reducedness is essential to invoke the freeness criterion: repeated discriminant directions are not covered. The theorem is over characteristic zero; a characteristic-\(p\) extension would need to reconsider the determinant scalar and inseparable ramification. The proof does **not** classify all singularity types, fundamental groups, or modular centers. In particular, a nonflex point on a smooth cubic need not be modular, so the cubic specialization is a freeness claim, not an assertion of supersolvability for every center. 
## References

1. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117 (first posted 2023-01-03), especially Theorems 1.5, 1.11 and Conjecture 1.10.
2. R. Di Gennaro, G. Ilardi, R. M. Miró-Roig, H. Schenck, J. Vallès, *Free curves, Eigenschemes and Pencils of curves*, arXiv:2306.09443 (first posted 2023-06-15), especially Theorems 2.5 and 3.6.
3. J. Vallès, *Free divisors in a pencil of curves*, arXiv:1502.02416 (first posted 2015-02-09), Theorem 2.7.
4. S. Bannai, H. Tokunaga, *Zariski \(N\)-ples for a smooth cubic and its tangent lines*, arXiv:1903.04098 (first posted 2019-03-11).
5. K. Saito, *Theory of logarithmic differential forms and logarithmic vector fields*, J. Fac. Sci. Univ. Tokyo 27 (1980), 265–291; determinant criterion as recalled in reference 2.
