# Sharp fourth moments and phase rigidity for the three fundamental characters of \(SU(4)\)

## Finding
Let \(V=\mathbb C^4\) be the defining representation of \(SU(4)\), let \(W=\bigwedge^2V\), and write \(\chi_V,\chi_{V^*},\chi_W\) for the ordinary (unnormalized) irreducible trace characters. With Haar probability measure \(dg\), define
\[
F(g)=a\chi_V(g)+b\chi_{V^*}(g)+c\chi_W(g),\qquad a,b,c\in\mathbb C.
\]
For every coefficient triple,
\[
\boxed{\int_{SU(4)}|F(g)|^4\,dg\leq\frac{51}{11}\left(\int_{SU(4)}|F(g)|^2\,dg\right)^2.}
\]
The constant is best possible. All nonzero equality cases are exactly
\[
(a,b,c)=\lambda(1,1,\sqrt{5/3}),\quad
\lambda(1,1,-\sqrt{5/3}),\quad
\lambda(1,-1,i\sqrt{5/3}),\quad
\lambda(1,-1,-i\sqrt{5/3}),\qquad \lambda\in\mathbb C\setminus\{0\}.
\]
Thus there are exactly four maximizing projective phase classes, and their coefficient energies divide as \(3:3:5\).

A quantitative strengthening is the following exact nonnegative deficit identity. With \(x=|a|\), \(y=|b|\), \(z=|c|\), and \(N=x^2+y^2+z^2\),
\[
\begin{aligned}
\frac{51}{11}N^2-\int|F|^4\,dg
={}&\frac{11}{2}\left(z^2-\frac{5N}{11}\right)^2
+\frac32(x^2-y^2)^2+4z^2(x-y)^2\\
&+2\left(x^2y^2-\operatorname{Re}(a^2\overline{b}^{\,2})\right)
+8\left(z^2xy-\operatorname{Re}(c^2\overline{ab})\right).
\end{aligned}
\]
Every term on the right is nonnegative.

## Assumptions and scope
The group is the compact simply connected group \(SU(4)\); the three characters are exactly its three fundamental representations, of dimensions \(4,4,6\). In particular \(W\cong W^*\) but \(V\not\cong V^*\). The measure is Haar probability, the characters are trace characters (not divided by dimensions), and coefficient scalars are unrestricted complex numbers. Character orthogonality yields \(\int|F|^2\,dg=N\). The claim covers every complex coefficient triple, including zero coefficients and all phase choices. Equality classification excludes the zero function.

## Proof
Character multiplication is tensor-product decomposition. The required irreducible rules (with distinct summands represented by their dimensions and familiar names) are
\[
\begin{array}{lll}
V\otimes V\cong\operatorname{Sym}^2V\oplus W,&
V^*\otimes V^*\cong\operatorname{Sym}^2V^*\oplus W,&
V\otimes V^*\cong\mathbf1\oplus\mathrm{Ad},\\
V\otimes W\cong\mathbf{20}\oplus V^*,&
V^*\otimes W\cong\overline{\mathbf{20}}\oplus V,&
W\otimes W\cong\mathbf1\oplus\mathrm{Ad}\oplus\mathbf{20'}.
\end{array}
\]
Here \(\mathrm{Ad}\) has dimension \(15\); the \(\mathbf{20}\), \(\overline{\mathbf{20}}\), and \(\mathbf{20'}\) summands are pairwise inequivalent, as are the other representation labels displayed. The two symmetric squares (dimension \(10\) each) are inequivalent. These rules can alternatively be verified by Weyl integration, without relying on the names of summands, as in the accompanying checker.

Grouping the characters in \(F^2\) by inequivalent irreducible types and using their orthonormality gives the exact identity
\[
\begin{aligned}
M:=\int|F|^4\,dg
={}&|a|^4+|b|^4+|a^2+b^2|^2
+2|c^2+2ab|^2+|c|^4\\
&+8|c|^2\bigl(|a|^2+|b|^2\bigr).
\end{aligned}
\]
Equivalently,
\[
\begin{aligned}
M={}&2x^4+2y^4+3z^4+8x^2y^2+8z^2(x^2+y^2)\\
&+2\operatorname{Re}(a^2\overline{b}^{\,2})
+8\operatorname{Re}(c^2\overline{ab}).
\end{aligned}
\]
Put \(S=x^2+y^2\), \(p=xy\). Since the real part of a complex number is at most its modulus,
\[
M\leq2S^2+6p^2+3z^4+8z^2(S+p).
\]
Since \(0\leq p\leq S/2\) and the right side is increasing in \(p\),
\[
M\leq\frac72S^2+12Sz^2+3z^4
=\frac{51}{11}N^2-\frac{11}{2}\left(z^2-\frac{5N}{11}\right)^2.
\]
Subtracting the exact moment from the square-completion expression, using \(S^2-4p^2=(x^2-y^2)^2\) and \(S-2p=(x-y)^2\), proves the stated deficit identity without omitted terms.

If \(N>0\), equality in the first square enforces \(z^2=5N/11>0\). Equality in the other amplitude squares forces \(x=y>0\), hence \(x^2=y^2=3N/11\). The two phase deficits vanish exactly when \(a^2\overline{b}^{\,2}\) and \(c^2\overline{ab}\) are positive real numbers. Thus \(b/a\in\{1,-1\}\) and \(c^2/(ab)>0\), which, after dividing by \(a\ne0\), yields the four displayed coefficient classes. Substitution attains \(M=51N^2/11\), proving sharpness and exhaustion of equality cases.

## Verification
The standalone script `check_su4.py` performs exact Weyl integration over the maximal torus using Laurent polynomials in three torus variables and the \(SU(4)\) squared Weyl denominator. In the ordered six terms \(\chi_V^2,\chi_{V^*}^2,\chi_W^2,2\chi_V\chi_{V^*},2\chi_V\chi_W,2\chi_{V^*}\chi_W\), its exact integer Gram matrix is
\[
\begin{pmatrix}
2&1&0&0&0&0\\
1&2&0&0&0&0\\
0&0&3&4&0&0\\
0&0&4&8&0&0\\
0&0&0&0&8&0\\
0&0&0&0&0&8
\end{pmatrix}.
\]
The script checks all entries independently, reconstructs \(M\) on 216 coefficient triples of small Gaussian integers, checks the inequality there, and verifies the rational extremal energy identity. The all-coefficient theorem follows from the preceding exact proof; finite checks do not certify an infinite assertion by themselves.

## Relationship to prior work
Fernández Núñez, García Fuertes and Perelomov [1] develop the three fundamental \(A_3\) character generating functions, identifying exactly the natural characters used here. Their character and weight-multiplicity formulas provide representation-theoretic background, but their sections on character generating functions, weight multiplicities and appendices do not state the sharp three-character fourth-moment bound, its phase classification, or the deficit. Cardona and Ruzhansky [2] prove Fourier multiplier boundedness theorems for compact Lie groups, without this finite central-character extremal constant.

The established character product rules determine the quartic moment polynomial, but its global sharp optimization and the exact phase-sensitive deficit are additional statements. Character packets for other compact groups obey different representation fusion rules, and no such estimate establishes the present \(SU(4)\) theorem. The equivalent \(\operatorname{Spin}(6)\) description uses two half-spin and one vector character. No claiming of priority over unindexed literature is made.

## Limitations
This theorem concerns the central three-dimensional span of the fundamental characters of \(SU(4)\), not arbitrary matrix coefficients, general character packets, or an all-rank \(SU(n)\) statement. The verification program is a finite exact cross-check of tensor multiplicities and selected coefficients; it is not an external or independent audit. An equivalent exact inequality may appear in unindexed character optimization literature.

## References
[1] J. Fernández Núñez, W. García Fuertes and A. M. Perelomov, *Some results on generating functions for characters and weight multiplicities of the Lie algebra A3*, arXiv:1705.03711, first posted 2017-05-10. https://arxiv.org/abs/1705.03711

[2] D. Cardona and M. Ruzhansky, *Fourier multipliers for Triebel–Lizorkin spaces on compact Lie groups*, Collectanea Mathematica 73 (2022), 477–504, first online 2021-10-06. https://doi.org/10.1007/s13348-021-00330-9
