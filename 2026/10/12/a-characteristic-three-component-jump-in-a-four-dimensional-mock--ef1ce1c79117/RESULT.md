# A characteristic-three component jump in a four-dimensional mock-Lie Yang–Baxter locus

## Finding

Let \(K\) be a field with \(\operatorname{char}K\ne2\). On the four-dimensional vector space \(A=Ke_1\oplus\cdots\oplus Ke_4\), define the commutative multiplication
\[
e_1\bullet e_1=e_2,\qquad e_1\bullet e_3=e_3\bullet e_1=e_4,
\]
with all remaining basis products zero. This is exactly the mock-Lie algebra printed in Example 2.1 of Benali, Chtioui, Hajjaji, and Mabrouk. The annihilator contains \(Ke_2+Ke_4\), which contains all products, so triple products vanish and the Jacobi identity holds in every characteristic.

A general skew tensor has the unique expression
\[
\begin{aligned}
r={}&a(e_1\wedge e_2)+b(e_1\wedge e_3)+c(e_1\wedge e_4)\\
&+d(e_2\wedge e_3)+e(e_2\wedge e_4)+f(e_3\wedge e_4),
\end{aligned}
\]
where \(u\wedge v=u\otimes v-v\otimes u\) and the six coefficients belong to \(K\). For the mock-Lie Yang–Baxter polynomial
\[
[[r,r]]=r_{12}\bullet r_{13}+r_{13}\bullet r_{23}-r_{12}\bullet r_{23},
\]
the following criterion is **necessary and sufficient over every field of characteristic different from two**:
\[
\boxed{
 b=0,\quad 3a^2=0,\quad a(c-d)=0,\quad
 2af+c^2-2cd=0,\quad 3cf=0.
}
\]

If \(\operatorname{char}K\ne2,3\), the reduced field-valued solution locus is the union of the affine \(3\)-space
\[
\{a=b=c=0\}
\]
and affine \(2\)-space
\[
\{a=b=f=0,\ c=2d\},
\]
meeting in the affine line \(\{a=b=c=d=f=0\}\), with free coordinate \(e\).

If \(\operatorname{char}K=3\), the reduced solution locus instead has **three irreducible three-dimensional components**:
\[
\{a=b=c=0\},\quad
\{a=b=0,\ c=-d\},\quad
\{b=0,\ c=d,\ af=-c^2\}.
\]
The first two components are affine \(3\)-spaces; the third is the quadric cone \(af+c^2=0\) times an affine \(e\)-line. All pairwise intersections, and their triple intersection, are exactly the affine plane
\[
\{a=b=c=d=0\}
\]
with free coordinates \(e,f\).

For every odd prime power \(q\), the number of skew Yang–Baxter solutions is
\[
\boxed{
N_q=\begin{cases}
q^3+q^2-q,&\operatorname{char}\mathbf F_q\ne3,\\
3q^3-2q^2,&\operatorname{char}\mathbf F_q=3.
\end{cases}}
\]
The respective numbers of nondegenerate skew solutions (rank \(4\)) are
\[
\boxed{q(q-1)\quad\text{and}\quad q^2(q-1).}
\]
The remaining solutions have rank \(0\) (one solution) or rank \(2\).

Moreover, the associated coboundary linear maps
\[
\Delta_r(x)=(L_x\otimes I-I\otimes L_x)r
\]
forget exactly the coefficient \(e\). They therefore have exactly \(q\) solution tensors each, and the numbers of distinct such maps are
\[
\boxed{q^2+q-1\quad\text{and}\quad 3q^2-2q,}
\]
respectively. Here we claim only the displayed polynomial solutions and coboundary maps in characteristic \(3\); no characteristic-zero bialgebra theorem is imported into characteristic \(3\) without separate proof.

## Assumptions and scope

The earliest public version of the source, arXiv:2301.12928v1, was posted on 27 December 2022, in the middle date window. The source lists primary MSC2020 \(16W10\), and assumes characteristic zero for its general theoretical development. Its Example 2.1 and tensor equation (4.9), however, have integral structure constants. The results here interpret those explicitly specified algebraic equations over every field with \(2\ne0\), including characteristic \(3\).

The term *reduced locus* refers to the ordinary geometric set of field-valued skew tensors, not the potentially nonreduced representing tensor-equation scheme. The statement is not an isomorphism classification under algebra automorphisms and does not concern arbitrary nonskew tensors.

## Proof

Write the skew tensor as the skew matrix
\[
R=\begin{pmatrix}
0&a&b&c\\
-a&0&d&e\\
-b&-d&0&f\\
-c&-e&-f&0
\end{pmatrix}.
\]
By the defining multiplication, the only nonzero products of basis vectors are \(e_1\bullet e_1=e_2\) and \(e_1\bullet e_3=e_3\bullet e_1=e_4\). For each \(i,j,k\in\{1,2,3,4\}\), the \(e_i\otimes e_j\otimes e_k\) coefficient of the Yang–Baxter tensor is
\[
\sum_{u,v}m^i_{uv}R_{uj}R_{vk}
+\sum_{u,v}R_{iu}R_{jv}m^k_{uv}
-\sum_{u,v}R_{iu}m^j_{uv}R_{vk},
\]
where \(m^i_{uv}\) are the multiplication constants. Among the \(64\) coefficients, the nonzero polynomials, up to repeated occurrence, are
\[
\begin{gathered}
-ab,\ -b^2,\ -2bc,\ 3a^2,\ 2ab,\ 2a(c-d),\\
b^2,\ b(c-d),\ 2af+c^2-2cd,\ 2bf,\ 6cf.
\end{gathered}
\]
Because \(K\) is a field, \(b^2=0\) implies \(b=0\). Because \(2\ne0\), the remaining conditions are exactly those stated in the finding. This proves the complete necessary-and-sufficient criterion without restricting the tensor ansatz.

When \(3\ne0\), \(3a^2=0\) gives \(a=0\), and the other nontrivial equations reduce to \(c(c-2d)=0\), \(cf=0\). If \(c=0\), \(d,e,f\) are arbitrary; if \(c\ne0\), then \(c=2d\) and \(f=0\). The union of the two stated linear spaces and their intersection follows.

When \(\operatorname{char}K=3\), the equations become
\[
b=0,\qquad a(c-d)=0,\qquad af=c(c+d).
\]
If \(a=0\), then \(c(c+d)=0\), yielding the two affine components \(c=0\) and \(c=-d\). If \(a\ne0\), then \(c=d\) and \(f=-c^2/a\); the Zariski closure of these points is the irreducible quadratic hypersurface \(c=d\), \(af+c^2=0\), with \(e\) free. Irreducibility follows because the polynomial \(af+c^2\) is primitive and linear in \(a\) over \(K[c,f]\) with coprime coefficient polynomials \(f,c^2\). All pairwise intersections are \(a=c=d=0\), with arbitrary \(e,f\).

For finite fields of order \(q\) with characteristic different from \(3\), the two components have \(q^3\) and \(q^2\) points and meet in \(q\) points. The count is \(q^3+q^2-q\). In characteristic \(3\), the two linear components contribute \(2q^3-q^2\) points. The solutions with \(a\ne0\) contribute \((q-1)q^2\), producing \(3q^3-2q^2\).

The Pfaffian of the skew matrix is \(af-be+cd\), so its determinant is \((af-be+cd)^2\). All solutions satisfy \(b=0\). In characteristic different from \(3\), rank \(4\) occurs only on \(a=f=0,c=2d\) with \(d\ne0\): there are \(q(q-1)\) choices of \((d,e)\). In characteristic \(3\), solutions with \(a\ne0\) have \(c=d\) and \(af=-c^2\), so the Pfaffian vanishes. On the linear component \(a=0,c=-d\), the Pfaffian is \(-d^2\), nonzero exactly when \(d\ne0\); \((d,e,f)\) then give \(q^2(q-1)\) choices.

Finally, let \(u\odot v=u\otimes v+v\otimes u\). Directly expanding the coboundary formula, using \(b=0\), gives
\[
\begin{aligned}
\Delta_r(e_1)={}&2a(e_2\otimes e_2)+(c-d)(e_2\odot e_4)
                  +2f(e_4\otimes e_4),\\
\Delta_r(e_3)={}&a(e_2\odot e_4)+2c(e_4\otimes e_4),\\
\Delta_r(e_2)={}&\Delta_r(e_4)=0.
\end{aligned}
\]
The two displayed tensors recover \(a,c,d,f\) uniquely because \(2\ne0\), but contain no \(e\). Thus the coboundary map has exactly one freely variable skew coefficient \(e\) on every solution fiber, proving the final counts.

For each finite extension \(\mathbf F_{q^m}\), replace \(q\) by \(q^m\). In particular, the Hasse–Weil exponential zeta functions of these reduced solution loci are
\[
Z(T)=\begin{cases}
\dfrac{1-qT}{(1-q^2T)(1-q^3T)},&\operatorname{char}\mathbf F_q\ne3,\\
\dfrac{(1-q^2T)^2}{(1-q^3T)^3},&\operatorname{char}\mathbf F_q=3.
\end{cases}
\]

## Verification

Run `python3 artifacts/verify.py` in a Python environment with SymPy installed. The included `artifacts/requirements.txt` specifies the sole nonstandard dependency.

The checker directly reconstructs the mock-Lie multiplication, all \(64\) tensor coefficients of the Yang–Baxter equation, and independently the coadjoint \(\mathcal O\)-operator identity of the primary paper. It verifies the coefficient identities, symbolic branch formulas, and exact Pfaffian and coboundary formulas.

Exhaustive field checks enumerate all \(q^6\) skew matrices for \(\mathbf F_3\), \(\mathbf F_5\), and \(\mathbf F_7\), rather than only enumerating a candidate set. They produce the respective tuples (solutions, rank-four solutions, distinct coboundary maps)
\[
(63,18,21),\quad (145,20,29),\quad (385,42,55).
\]
An additional independent extension-field check in \(\mathbf F_9\) verifies \(2025\) solutions and \(648\) nondegenerate ones using explicit finite-field arithmetic. The checker prints `VERIFY_OK`.

The finite checks are not proofs for arbitrary fields; the preceding tensor-coordinate calculation and algebraic case division establish the theorem.

## Relationship to prior work

Benali–Chtioui–Hajjaji–Mabrouk introduce the mock-Lie Yang–Baxter tensor and its coadjoint \(\mathcal O\)-operator characterization, and use the exact four-dimensional multiplication as Example 2.1. Their complete accessible preprint develops abstract theory; it does not classify all skew solutions of that example or determine the characteristic-three components, rank-four counts, or coboundary fibers. Its characteristic-zero standing assumption is explicit.

Assiry studies symplectic forms and Yang–Baxter structures on Jacobi–Jordan algebras more broadly, but its full text does not provide these four-dimensional tensor equations or arithmetic formulas. Other literature uses “Jacobi–Jordan,” “mock-Lie,” and “Lie–Jordan” for the same class of commutative Jacobi algebras; searches under all three terminology variants and exact products found no covering computation.

The literature comparison is statement-level: general symplectic correspondences and a displayed example do not themselves imply the explicit reduced-locus decomposition, its exceptional characteristic-three component, or the finite-field formulas. A 2023 meeting abstract on mock-Lie Yang–Baxter solutions was identified but not fully inspected; it remains an originality risk rather than being declared non-covering.

## Limitations

Characteristic \(2\) is excluded because skew symmetry, the Pfaffian rank test, and the recovery of coboundary parameters rely on \(2\ne0\). The classification is of skew tensor solutions in the printed basis, not of orbits modulo automorphisms. No scheme-theoretic reducedness of the unradicalized defining polynomial ideal is asserted.

The original paper's general triangular-bialgebra results assume characteristic zero; the characteristic-three result here proves the explicit polynomial identities and counts of their associated linear coboundary maps, not an unverified extension of every theoretical proposition.

A meeting abstract and later mock-Lie literature may hide an equivalent low-dimensional calculation; absence from search results is not a proof of historical uniqueness.

## References

1. K. Benali, T. Chtioui, A. Hajjaji, and S. Mabrouk, “Mock-Lie bialgebras and mock-Lie analogue of the classical Yang-Baxter equation,” arXiv:2301.12928v1, first public version 27 December 2022; full accessible postprint arXiv:2301.12928v2 (2023), especially Example 2.1, Eq. (4.9), and Proposition 5.1.
2. T. Chtioui, K. Benali, A. Hajjaji, and S. Mabrouk, “Bialgebras, the Yang–Baxter equation and Manin triples for mock-Lie algebras,” *Acta et Commentationes Universitatis Tartuensis de Mathematica* 27 (2023), DOI `10.12697/ACUTM.2023.27.16` (published version of the originating work).
3. A. Assiry, “Symplectic Forms and the Yang-Baxter Equation in Jacobi-Jordan Algebras,” *International Journal of Mathematics and Computer Science* 19 (2024), 23–36 (published 23 August 2023), publicly readable PDF at `https://future-in-tech.net/19.1/R-Assiri.pdf`.
