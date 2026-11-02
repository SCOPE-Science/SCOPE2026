# The exceptional characteristic-seven bicanonical Wronskian of a genus-three hyperelliptic pencil

## Finding
Let \(k\) be algebraically closed of characteristic \(7\). In the smooth genus-three pencil
\[
C_t:\ y^2=x^8+t x^4+1,\qquad t^2\ne4,
\]
the generic Hasse order sequence of the complete bicanonical linear series \(|2K_{C_t}|\) is \((0,1,2,3,4,5)\) for every \(t\ne0\), whereas the single smooth exceptional member \(C_0\) has sequence \((0,1,2,3,4,7)\). The scheme of nonclassical parameters, cut out by the ordinary bicanonical Hasse-Wronskian in this pencil, is the **reduced** point \(t=0\).

On \(C_0:y^2=x^8+1\), let \(R_\alpha\) denote the ramification point with \(x=\alpha\) for each \(\alpha^8=-1\), and let the other fiber notation count geometric points individually. The complete higher Hasse-Wronskian divisor for the generic orders \((0,1,2,3,4,7)\) is
\[
\operatorname{div}(\mathcal W_{0})
=4\sum_{\alpha^8=-1}R_\alpha
+\sum_{P\mid x=0}P
+\sum_{P\mid x=\infty}P
+\sum_{\substack{\alpha^{48}=1\\\alpha^8\ne-1}}\ \sum_{P\mid x=\alpha}P.
\]
It consists of eight points of multiplicity four and eighty-four simple points (the latter: two above zero, two above infinity, and eighty above the remaining forty roots). Its degree is \(116\).

## Assumptions and scope
The parameter runs through \(\mathbb A^1_k\setminus\{2,-2\}\). These are exactly the smooth members, since \(x^8+t x^4+1\) has a repeated root precisely when \(t^2=4\) in characteristic \(7\). The curve is the smooth projective completion of the displayed affine equation. Hasse derivatives \(D_x^{(j)}\) are defined by the expansion \(f(x+u)=\sum_{j\ge0}D_x^{(j)}(f)u^j\) on the separable function-field extension \(k(C_t)/k(x)\). An order sequence is the lexicographically first six-tuple of nonnegative integers having a nonzero determinant of their Hasse derivatives on a basis of \(H^0(C_t,2K_{C_t})\). The higher Wronskian uses the actual generic order sequence on the exceptional member, not the characteristic-zero sequence.

## Proof
**Basis and determinants.** The regular differential \(\omega=dx/y\) has divisor \(2P_\infty^++2P_\infty^-\). Thus
\[
\omega^2,\ x\omega^2,\ x^2\omega^2,\ x^3\omega^2,\ x^4\omega^2,\ y\omega^2
\]
are six independent regular bicanonical sections; by Riemann--Roch \(h^0(2K)=6\), so they form a basis. The first five Hasse-derivative columns for \(1,x,x^2,x^3,x^4\) form a triangular matrix with determinant one in rows \(0,1,2,3,4\). Any row \(j>4\) annihilates those five monomials. Therefore the determinant with rows \(0,1,2,3,4,j\) equals \(D_x^{(j)}y\).

**Exact characteristic-seven identities.** Write \(F=x^8+t x^4+1\). In the polynomial ring \(\mathbb F_7[x,t]\), define \(B_j=y^{2j-1}D_x^{(j)}y\) for \(j\ge1\). Expanding \(y(x+u)^2=F(x+u)\) gives the fully polynomial recursion
\[
2B_j=D_x^{(j)}F\,F^{j-1}-\sum_{i=1}^{j-1}B_iB_{j-i}.
\]
Exact evaluation for \(j\le7\) gives
\[
B_5=3t(t^2-4)x^7(x^8-1)F,\qquad B_5|_{t=0}=B_6|_{t=0}=0,
\]
and
\[
B_7|_{t=0}=\frac{x(1-x^{48})}{2(x^8+1)}
=4x\bigl(1-x^8+x^{16}-x^{24}+x^{32}-x^{40}\bigr).
\]
The rational expression on the left is a polynomial because the denominator divides its numerator; this displayed equality is in \(\mathbb F_7[x]\). Therefore, for \(t\ne0\), the first nonzero determinant uses rows \((0,1,2,3,4,5)\). At \(t=0\), the row-5 and row-6 determinants vanish identically but row 7 does not, proving the two order sequences. The coefficient of \(x^7\) in the polynomial \(B_5\) is \(-3t(t^2-4)\), a unit multiple of \(t\) on the smooth parameter line. Hence the ideal of coefficients of the ordinary Wronskian is exactly \((t)\), proving that the nonclassicality locus is reduced, not merely set-theoretically a singleton.

**Higher Wronskian.** The order-sum of \((0,1,2,3,4,7)\) is \(17\). Multiplying the determinant by six bicanonical trivializations and the associated differential power yields the globally defined section of \(K_{C_0}^{\otimes29}\):
\[
\mathcal W_0=D_x^{(7)}y\,\frac{(dx)^{29}}{y^{12}}
=\frac{x(1-x^{48})}{2y^{27}}(dx)^{29}.
\]
At every root of \(x^8+1\), \(x-\alpha\) has local order two, \(y\) and \(dx\) order one; \(1-x^{48}\) has local order two. Thus the Wronskian has local order \(2-27+29=4\). The 48 roots of \(x^{48}=1\) are simple and include the eight branch roots; at each of the other forty abscissae there are two points and the Wronskian has simple zeros. Above \(x=0\) lie two unramified simple zeros. At either of the two points at infinity, \(\operatorname{ord}(x)=-1\), \(\operatorname{ord}(y)=-4\), and \(\operatorname{ord}(dx)=-2\); the Wronskian order is \(-49+108-58=1\). These are all zeros, and their total multiplicity \(8\cdot4+80+2+2=116\) equals \(29\deg K=29\cdot4\), independently excluding any unlisted zero or pole.

## Verification
The standalone `verify.py` performs arithmetic with exact sparse polynomials over \(\mathbb F_7[x,t]\), reconstructs \(B_j\) by the recursion through \(j=7\), proves the displayed identities by coefficient comparison, checks the Hasse--Witt matrix for context, and verifies the complete divisor degree. Run `python3 verify.py`; the recorded standard output in `verify_output.txt` ends in `VERIFY_OK`. Local valuations and the Wronskian transformation formula are established in the proof, not extrapolated from finite-field sampling.

## Relationship to prior work
Shaska and Shor (arXiv:1307.8177, first publicly posted July 31, 2013) study bicanonical Weierstrass points of genus-three hyperelliptic curves with extra automorphisms. Their explicit ordinary-characteristic Wronskian for a related one-parameter octavic family covers the general method and the classical generic calculations; **those formulas are not claimed as original here**. Their stated normalized nonzero parameter regime does not evaluate the characteristic-seven exceptional Hasse order jump or the higher-Hasse-Wronskian divisor displayed above. Stöhr and Voloch give general positive-characteristic order-sequence/Wronskian theory; the claim here is an evaluated exceptional case, not a new formalism.

## Limitations
This is a theorem over algebraically closed fields of characteristic seven about the marked smooth pencil and the complete bicanonical linear series. It does not assert a new formula for the characteristic-zero 2-Weierstrass divisor, distinguish geometric isomorphism classes of all parameters, or establish historical priority against every older article on positive-characteristic special curves. The higher Hasse-Wronskian multiplicities are taken relative to the true generic order sequence \((0,1,2,3,4,7)\); they must not be identified with characteristic-zero classical 2-Weierstrass weights. The superspecial nature of \(C_0\) is known independently and is not the novelty claim.

## References
- T. Shaska and C. Shor, *The 2-Weierstrass points of genus 3 hyperelliptic curves with extra automorphisms*, arXiv:1307.8177 (initial submission July 31, 2013), especially the octavic family and ordinary Wronskian calculations.
- K.-O. Stöhr and J. F. Voloch, *Weierstrass points and curves over finite fields*, Proceedings of the London Mathematical Society, series 3, 52 (1986), 1–19; general Hasse-order and Wronskian formalism.
