# A complete null-polynomial module and right-stabilizer for a 128-element matrix ring

## Finding

Let \(K=\mathbb F_2\), let \(T\subset M_2(K)\) be the upper-triangular algebra, and let
\[
R=\left\{(A,B)=\begin{pmatrix}A&B\\0&A\end{pmatrix}:A\in T,\ B\in M_2(K)\right\}.
\]
This is a unital ring with \(128\) elements. In \(R[x]\) the variable \(x\) is central and evaluation is on the right: \(\bigl(\sum_i a_ix^i\bigr)(r)=\sum_i a_ir^i\). Let \(\mathcal N(R)\) denote the null polynomials, and put \(t=x+x^2\in K[x]\). Write \(E_{ij}\) for the usual two-by-two matrix units and set \(U_{ij}=(E_{ij},0)\) for \((i,j)\in\{(1,1),(1,2),(2,2)\}\), and \(V_{ij}=(0,E_{ij})\) for all four index pairs.

**Complete presentation.** As a \(K[x]\)-submodule of \(R[x]\), \(\mathcal N(R)\) is free on precisely the following seven explicit polynomials:
\[
\begin{aligned}
&V_{12}t,\quad V_{22}t,\quad V_{11}t^2,\quad V_{21}t^2,\\
&U_{12}t^3,\quad U_{22}t^3,\quad U_{12}t^2+U_{11}t^3.
\end{aligned}
\]
The additive group of polynomial functions induced by \(R[x]\) has \(2^{30}\) elements. More precisely, for the natural \(K[x]\)-module structure on the evaluation image,
\[
R[x]/\mathcal N(R)\cong
\bigl(K[x]/(t)\bigr)^2\oplus
\bigl(K[x]/(t^2)\bigr)^3\oplus
K[x]/(t^3)\oplus K[x]/(t^4).
\]
This is an isomorphism of \(K[x]\)-modules, **not** an assertion that evaluation is a ring homomorphism.

**Exact obstruction to right multiplication.** The ring of constants preserving all null polynomials under right multiplication is
\[
\left\{b\in R:\mathcal N(R)b\subseteq\mathcal N(R)\right\}
=\left\{\left(\begin{pmatrix}a&c\\0&a\end{pmatrix},D\right): a,c\in K,\ D\in M_2(K)\right\}.
\]
It is an index-two subring of \(R\), containing exactly \(64\) elements. Moreover, every null polynomial of degree at most five remains null after right multiplication by **every** polynomial in \(R[x]\); degree six is the least degree at which right-ideal closure fails.

## Assumptions and scope

All operations in this result are over \(K=\mathbb F_2\). There is no generalization claimed to other fields or other finite rings. The pair notation uses the multiplication
\[
(A,B)(C,D)=(AC,AD+BC).
\]
The ring has dimension seven over \(K\), with ordered basis
\[
(U_{11},U_{12},U_{22},V_{11},V_{12},V_{21},V_{22}).
\]
For a polynomial \(f\), the symbol \(\deg f\) is the ordinary degree in the central variable \(x\), with \(\deg0=-\infty\). The natural \(K[x]\)-action on the image of evaluation is \((x\cdot h)(r)=h(r)r\); this makes sense because \((xf)(r)=f(r)r\) even though general polynomial products do not evaluate multiplicatively.

## Proof

**1. Seven explicit null polynomials.** For \(r=(A,B)\), let \(G=E_{12}\) and write
\[
A=\begin{pmatrix}a&b\\0&c\end{pmatrix},\qquad
T_r=t(r)=r+r^2=(\delta G,C),
\quad\delta=b(1+a+c),\quad C=B+AB+BA.
\]
Because \(G^2=0\), block multiplication yields
\[
T_r^2=(0,\delta(GC+CG)),\qquad
T_r^3=(0,\delta GCG),\qquad T_r^4=0.
\]
If \(\delta=0\), both powers of degree at least two vanish. If \(\delta=1\), the diagonal entries of \(A\) coincide and its upper-right entry is one. The identities \(E_{12}G=E_{22}G=0\) show that \(V_{12}t\) and \(V_{22}t\) vanish. Every \(V_{ij}t^2\) vanishes because the first component of \(T_r^2\) is zero. Likewise \(U_{12}t^3\) and \(U_{22}t^3\) vanish, since \(T_r^3\) has upper-right block proportional to \(G\), which both \(G\) and \(E_{22}\) annihilate on the left. Finally,
\[
U_{12}T_r^2+U_{11}T_r^3
=(0,\delta GCG+\delta E_{11}GCG)=0
\]
in characteristic two. Thus all seven displayed polynomials belong to \(\mathcal N(R)\).

**2. The seven polynomials generate every null polynomial.** The leading coefficients of the seven generators are, respectively,
\[
V_{12},V_{22},V_{11},V_{21},U_{12},U_{22},U_{11},
\]
which form a basis of \(R\) over \(K\). Their degrees are \(2,2,4,4,6,6,6\). Repeated cancellation of the leading coefficient therefore reduces every element of \(R[x]\), modulo the submodule they generate, to a linear combination of the following **thirty normal monomials**:
\[
\begin{array}{c|c}
\text{coefficient} &\text{allowed exponents }j\text{ in }\text{coefficient}\cdot x^j\\\hline
U_{11},U_{12},U_{22}&0,1,2,3,4,5\\
V_{11}&0,1,2,3\\
V_{12}&0,1\\
V_{21}&0,1,2,3\\
V_{22}&0,1.
\end{array}
\]
To prove uniqueness it suffices to prove that these thirty polynomial functions are linearly independent. The next paragraph gives a small, exact finite certificate rather than assuming numerical sampling.

Encode an element of \(R\) by
\[
\rho(A,B)=a_{11}+2a_{12}+4a_{22}+8b_{11}+16b_{12}+32b_{21}+64b_{22},
\]
and encode output coordinates in the above ordered seven-element basis by indices \(0,1,\ldots,6\). Use the thirty normal monomials in the order of the table (ordered by coefficient, then increasing exponent, with the coefficient order as in the basis above). For each pair \((r,k)\), form the row of the evaluation matrix recording output coordinate \(k\) of all thirty monomials at the element encoded by \(r\). Take the thirty rows
\[
\begin{gathered}
(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),\\
(1,0),(1,3),(1,5),(2,1),(2,4),(2,6),\\
(4,1),(4,2),(4,4),(4,6),(7,1),(7,4),(7,6),\\
(10,4),(15,4),(32,3),(32,5),(34,4),(34,6),\\
(37,3),(37,5),(39,4),(39,6).
\end{gathered}
\]
Direct exact elimination over \(K\) gives determinant \(1\) for this fully specified \(30\times30\) matrix. The independent standalone verifier evaluates these entries from the block multiplication law and checks its rank, without reading precomputed matrix entries. Hence the normal monomials are independent as polynomial functions. Every null polynomial reduces to the zero normal form, proving the seven-generator statement. Distinct leading coefficients also make the seven generators linearly independent over \(K[x]\), so the module is free.

**3. Module decomposition and function count.** The four generators with coefficients in the square-zero ideal \(\{(0,B)\}\) contribute two direct summands killed by \(t\) and two killed by \(t^2\). The generator \(U_{22}t^3\) contributes a summand killed by \(t^3\). On the \(U_{11},U_{12}\) coordinates, the two relations have presentation matrix
\[
\begin{pmatrix}t^3&0\\t^2&t^3\end{pmatrix}.
\]
Over the PID \(K[x]\), its Smith invariant factors are \(t^2\) and \(t^4\) (the entries have gcd \(t^2\), and the determinant is \(t^6\)). Combining factors yields the displayed module decomposition. Since \(\deg t=2\), its dimension is \(2\cdot2+3\cdot4+6+8=30\), and the number of induced polynomial functions is \(2^{30}\).

**4. The constant right-stabilizer.** Let \(b=(C,D)\in R\) with
\[
C=\begin{pmatrix}a&c\\0&d\end{pmatrix}.
\]
The products of the first six generators with \(b\) are null: the two \(V_{12},V_{22}\)-coefficient generators remain multiples of themselves, \(V\)-coefficient multiples of \(t^2\) always vanish, and the \(U_{12},U_{22}\)-coefficient multiples of \(t^3\) gain only null \(V\)-terms. For the seventh generator \(g=U_{12}t^2+U_{11}t^3\), direct coefficient multiplication gives, modulo \(\mathcal N(R)\),
\[
gb\equiv(a+d)U_{11}t^3.
\]
Indeed the full expression differs by \(d g+c U_{12}t^3\) and terms \(V_{ij}t^2\) or \(V_{ij}t^3\), all null. The class of \(U_{11}t^3\) is nonzero: using \(g=0\) in the quotient, it equals the nonzero class of \(U_{12}t^2\), a sum of two distinct normal monomials. Thus \(gb\) is null exactly when \(a=d\). This also proves the displayed right-stabilizer criterion for all null polynomials because the seven generators span \(\mathcal N(R)\) over \(K[x]\), and right multiplication by constants commutes with multiplication by \(K[x]\).

**5. Sharp minimum degree.** The generators of degrees \(2\) and \(4\) are right-stable under arbitrary constants. Every null polynomial of degree at most five is a \(K[x]\)-linear combination of only these four generators: a nonzero coefficient of a degree-six generator cannot be canceled by other generators because their leading coefficient directions are independent. Thus such a polynomial remains null after multiplication by any polynomial in \(R[x]\). In degree six, \(g\) above is null, whereas \(gU_{11}\equiv U_{11}t^3\notin\mathcal N(R)\). This establishes the sharp threshold.

## Verification

The accompanying `verify.py` implements all \(128\) ring elements as seven-bit vectors and multiplies them by the exact block law. It independently checks the seven null generators on every ring element, reconstructs the indicated \(30\times30\) evaluation minor and verifies determinant one over \(\mathbb F_2\), checks the stabilizer criterion for all \(128\) constants, and tests the asserted degree-six witness. Run `python3 verify.py` in the same directory. A successful run prints a `VERIFY_OK` line. The universal module statement for all polynomial degrees follows from the proved leading-coefficient reduction, not from a bounded-degree search.

## Relationship to prior work

V. Havlovec, *Null polynomials over a finite ring need not form a two-sided ideal*, arXiv:2608.13251 (first publicly submitted August 13, 2026), constructs **this same ring** and gives the displayed degree-six non-right-stable null polynomial (with equivalent notation). The existence of that witness is therefore **prior work**, not a novelty claim. The additions here are the full seven-generator null-polynomial module, its Smith invariant factors and exact function count, the complete constant right-stabilizer, and proof that degree six is optimal.

The related work by Havlovec on structural matrix rings (arXiv:2608.13242) proves positive ideal results for rings defined by allowed matrix positions. The present ring has an equality constraint between two diagonal blocks, so that result does not apply to its null-polynomial module. Werner's general finite-ring null-polynomial study (2014) establishes positive families and posed the conjecture disproved in Havlovec's example; its positive results do not determine the seven relations here. Searches for equivalent formulations under the terms null polynomials, polynomial-function modules, degree bounds, and right idealizers found no covering description; an equivalent result in unindexed literature remains possible.

## Limitations

This is a complete computation for one specifically motivated \(128\)-element ring, not a theorem about all noncommutative finite rings. The thirty-row determinant is an exact finite certificate, not a general symbolic rank formula for larger families. The result classifies constant right multipliers that preserve all null polynomials, not the entire polynomial right idealizer. The additive quotient is a \(K[x]\)-module, not naturally a quotient ring. Independent external validation has not been performed.

## References

1. Valentin Havlovec, *Null polynomials over a finite ring need not form a two-sided ideal*, arXiv:2608.13251, first submitted 2026-08-13, revised 2026-09-15. https://arxiv.org/abs/2608.13251
2. Valentin Havlovec, *Integer-valued polynomials over structural matrix rings*, arXiv:2608.13242, first submitted 2026-08-13. https://arxiv.org/abs/2608.13242
3. Nicholas J. Werner, *Polynomials that kill each element of a finite ring*, Journal of Algebra and Its Applications **13** (2014), 1350111, DOI:10.1142/S0219498813501119.
