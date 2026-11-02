# A rank-jumping divisor and cuspidal boundary in a characteristic-three net of genus-four bielliptic curves

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). In \(\mathbf P^3_k\), with homogeneous coordinates \([X:Y:Z:W]\), consider the complete intersections
\[
C_{s,t}:\qquad Y^2Z=X^3+XZ^2+Z^3,\qquad W^2=XY+sXZ+tZ^2,
\]
where \(s,t\in k\). Define
\[
\Delta(s,t)=-(s^2-1)^2+s^3(t^3+t)+s^2(t^2-t^4)-t^6.
\]
Then the following assertions hold.

1. **Exact smooth locus.** The curve \(C_{s,t}\) is smooth if and only if \(\Delta(s,t)\ne0\). Every smooth member is a connected, nonhyperelliptic canonical curve of genus \(4\), equipped with a degree-two map onto the fixed supersingular elliptic curve \(E:Y^2Z=X^3+XZ^2+Z^3\). The map branches simply at exactly six geometric points.
2. **Complete arithmetic stratification.** On the smooth parameter locus the geometric \(3\)-rank \(f\) and the \(a\)-number are
\[
(f(\operatorname{Jac} C_{s,t}),a(\operatorname{Jac} C_{s,t}))=
\begin{cases}(3,1),&s\ne0,\\(2,2),&s=0.\end{cases}
\]
The associated Newton polygons have slopes \((0,0,0,\tfrac12,\tfrac12,1,1,1)\) for \(s\ne0\), and \((0,0,\tfrac12,\tfrac12,\tfrac12,\tfrac12,1,1)\) for \(s=0\). The \(3\)-rank-drop divisor in this two-dimensional smooth net is **reduced**, cut out by the single equation \(s=0\).
3. **Rank-drop boundary.** The scheme-theoretic intersection of the discriminant curve \(V(\Delta)\) with \(s=0\) consists of the two distinct points \((0,t_+)\), \((0,t_-)\) satisfying \(t_\pm^2=-1\), each of intersection multiplicity exactly \(3\). Each corresponding complete intersection is irreducible with exactly one unibranch cusp analytically equivalent to \(w^2=u^3\), with \(\delta=1\) and normalization of genus \(3\).
4. **Genuine variation.** The smooth curves form a two-dimensional family in the moduli space of genus-four curves; in particular the rank-drop divisor is not an isotrivial artifact.

## Assumptions and scope

All statements are geometric over \(k=\overline{k}\) of characteristic \(3\); there is no restriction that \(s,t\) lie in a finite field. The polynomial \(\Delta\) is the explicitly displayed discriminant equation, with its stated scheme structure. The \(3\)-rank is the dimension of the maximal étale quotient of the Jacobian's \(3\)-torsion group scheme; the \(a\)-number is the dimension of the kernel of the Cartier operator on regular differentials. The Newton polygon conventions list all eight slopes with multiplicities. The polynomial calculations below are interpreted in \(k\), not over characteristic zero.

## Proof

**1. The fixed elliptic base and branch sections.** In the affine chart \(Z=1\), the cubic is \(y^2=x^3+x+1\). Its derivative with respect to \(x\) is \(1\), and at infinity \(O=[0:1:0]\) the projective partial derivative with respect to \(Z\) is nonzero, so it is nonsingular. Its coefficient of \(x^2\) vanishes, hence its Hasse invariant in characteristic \(3\) is zero, and \(E\) is supersingular. The involution \(W\mapsto-W\) on \(C_{s,t}\) has quotient \(E\). Its branch section is \(q=XY+sXZ+tZ^2\), a section of \(\mathcal O_E(2)\simeq\mathcal O_E(6O)\). At \(O\), put \(u=X/Y\), \(v=Z/Y\); the cubic yields \(v=u^3+O(u^4)\), so \(q/Y^2=u+su v+tv^2\) has a simple zero for every \((s,t)\). This already guarantees that the double cover is geometrically connected.

**2. The exact discriminant.** Away from \(O\), for \(t\ne0\), a zero of \(q=x(y+s)+t\) has \(x\ne0\) and \(y=-s-t/x\). Substitution into \(y^2=x^3+x+1\) gives the monic quintic
\[
F_{s,t}(x)=x^5+x^3+(1-s^2)x^2+stx-t^2.
\]
Its five roots give the five finite branch points, with their intersection multiplicities. A direct Sylvester resultant over \(\mathbb F_3[s,t]\) is
\[
\operatorname{Res}_x(F_{s,t},\partial_xF_{s,t})=t^2\Delta(s,t).
\]
Thus for \(t\ne0\) the section has six simple zeros exactly when \(\Delta\ne0\). For \(t=0\), the section factors as \(q=x(y+s)\) on the affine elliptic curve: it has two simple roots over \(x=0\) and three simple roots over \(y=-s\) precisely when \(s^2\ne1\). This agrees with \(\Delta(s,0)=-(s^2-1)^2\ne0\). In characteristic different from two, the local quadratic cover \(W^2=q\) is nonsingular precisely at simple zeros of \(q\), and is étale and nonsingular elsewhere. Therefore the complete intersection is smooth exactly on \(U=\mathbf A^2_k\setminus V(\Delta)\). By Riemann–Hurwitz for the six simply branched points, \(2g(C)-2=6\), so \(g(C)=4\). Since a smooth \((2,3)\) complete intersection in \(\mathbf P^3\) has \(\omega_C\simeq\mathcal O_C(1)\), this is the canonical, nonhyperelliptic embedding.

**3. The Hasse–Witt calculation.** For a smooth complete intersection of degrees \(3\) and \(2\) in \(\mathbf P^3\), the Koszul-residue basis of \(H^1(C,\mathcal O_C)\) corresponds to the four monomials with positive exponent vectors of sum \(5\):
\[
e_1=(1,1,1,2),\quad e_2=(1,1,2,1),\quad e_3=(1,2,1,1),\quad e_4=(2,1,1,1).
\]
The matrix entry in row \(i\), column \(j\) of the **transpose** of the absolute-Frobenius Hasse–Witt matrix is the coefficient of the monomial of exponent vector \(3e_i-e_j\) in \((PQ)^{3-1}\), where
\[
P=Y^2Z-X^3-XZ^2-Z^3,\qquad Q=W^2-XY-sXZ-tZ^2.
\]
Expanding and reducing modulo three gives the **entire transposed Hasse–Witt coefficient matrix**
\[
H(s,t)=\begin{pmatrix}
0&0&0&0\\
0&s&-1&s+t\\
0&0&0&1\\
0&0&-1&s
\end{pmatrix}.
\]
The lower-right \(3\times3\) block \(B\) has determinant \(s\). For \(s\ne0\), the semilinear action is invertible on a three-dimensional block and zero on the remaining line, giving stable rank \(3\) and ordinary rank \(3\). For \(s=0\), the first coordinate of \(B\) maps to zero, and the induced semilinear map on the quotient by that coordinate has invertible matrix \(\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\). Every semilinear iterate of \(B\) therefore has rank at least \(2\), and the first iterate already has rank \(2\); thus stable rank is \(2\). The full matrix has one additional zero coordinate, so its stable and ordinary ranks are also \(2\). The one-step matrix ranks are respectively \(3\) and \(2\). Transposition identifies this matrix with the dual Cartier presentation of Frobenius; duality preserves the ranks of the iterates (with the appropriate Frobenius coefficient twists). Thus its stable rank computes the geometric \(3\)-rank and its one-step corank computes the \(a\)-number, proving the asserted pairs. The Newton polygons then follow: after removing the ordinary slopes and their duals, the remaining factor has dimension one or two and \(3\)-rank zero, so its slopes are all \(1/2\). The scalar determinant \(s\) proves the rank-drop divisor has multiplicity one in the smooth parameter surface.

**4. The two cuspidal boundary members.** Restricting the discriminant polynomial yields
\[
\Delta(0,t)=-(t^2+1)^3.
\]
The two roots of \(t^2+1\) are distinct in characteristic three, and each appears with multiplicity three. At \(s=0\), \(t^2=-1\), the branch quintic factors as
\[
F_{0,t}(x)=(x+1)^3(x^2+1).
\]
The triple zero \(x=-1\) lies on the nonsingular affine part of \(E\) with \(y=t\ne0\), so \(x+1\) is a local parameter. The quadratic cover consequently has completed local equation \(w^2=u^3\) after multiplying by a unit and changing the local parameter. The other two finite roots and \(O\) remain simply branched, and there are no further singularities. Since the quadratic function is not a square on \(E\) (it has a simple zero at \(O\)), this fiber is irreducible. Normalizing replaces the cusp by one smooth point, and decreases the arithmetic genus \(4\) by its \(\delta\)-invariant \(1\), giving genus \(3\).

**5. Moduli variation.** The branch sections \(XY\), \(XZ\), and \(Z^2\), restricted to \(E\), are linearly independent. Thus the branch divisors of \(q_{s,t}\) are distinct as \(s,t\) vary: two sections of the same degree-six line bundle with equal divisors are scalar multiples, and the coefficient of \(XY\) is fixed as one. An automorphism of \(E\) carrying one such branch divisor to another must preserve the line bundle class \(\mathcal O_E(6O)\), so its translation component belongs to the finite group scheme of six-torsion; origin-preserving automorphisms are also finite. Therefore any given marked elliptic double cover occurs at finitely many parameters. Finally, a smooth genus-four curve has finitely many involutions, so forgetting its distinguished elliptic quotient remains finite-to-one. This proves that the image of the net in \(\mathcal M_4\) has dimension two.

## Verification

A standalone exact certificate, `verify_net.py`, requires Python 3 and SymPy. Executing `python verify_net.py` reconstructs the sixteen coefficient entries of the Hasse–Witt matrix, checks the \(3\times3\) determinant and invariant \(2\times2\) minor, computes the Sylvester resultant, checks both boundary factorizations, and verifies the affine smoothness derivative of the elliptic base. The expected terminal line is `CHAR3_BIELLIPTIC_NET_RESULTANT_HASSE_RANK_CUSP_EXACT_PASS`. The argument for arbitrary algebraically closed characteristic-three fields and the moduli dimension is mathematical, not a finite-field extrapolation.

## Relationship to prior work

Ogasawara–Ohashi–Sakata–Harashita [1] developed genus-four double covers of elliptic curves and nonsingularity criteria, while explicitly restricting their general discriminant treatment to characteristic different from two and three. Kudo–Harashita [2] give the general Koszul cohomology method for Hasse–Witt matrices of complete-intersection curves. Chang–Dragutinović–Groen–Lin–Pacheco-Tallaj–Singhal [3] prove general dimension and existence results for \(p\)-rank strata in moduli of double covers of a fixed elliptic curve. Those broad results allow such strata but do not specify this two-parameter characteristic-three net, its explicit Hasse–Witt matrix, reduced jumping divisor, or its two triple-intersection cuspidal boundary members. In particular, the explicit one-parameter construction in [3, Proposition 5.4] assumes \(p\nmid(g-1)\), which excludes \((p,g)=(3,4)\); its other explicit examples use different branch configurations. The assertion here is this **explicit complete stratification and boundary calculation**, not the first existence of genus-four double covers or \(3\)-rank strata. Earlier unindexed equivalent examples cannot be excluded.

## Limitations

No assertion is made about all genus-four bielliptic curves in characteristic three, about global irreducibility or reducedness of the entire curve \(V(\Delta)\), or about stable reduction across its boundary. The cuspidal statement applies only to the two points on \(s=0\). The full Newton polygon result uses the standard dimension-one and dimension-two classification of \(p\)-rank-zero factors. The exact computations independently establish the displayed polynomial identities; they do not by themselves certify the general geometric arguments or priority. No independent mathematical audit has been conducted.

## References

[1] T. Ogasawara, R. Ohashi, K. Sakata, S. Harashita, *Superspecial genus-4 double covers of elliptic curves*, arXiv:2403.08139, first posted 2024-03-12. https://arxiv.org/abs/2403.08139

[2] M. Kudo, S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114, first posted 2016-07-05, especially Appendix B. https://arxiv.org/abs/1607.01114

[3] K. Chang, D. Dragutinović, S. R. Groen, Y. Lin, N. Pacheco-Tallaj, D. Singhal, *The p-rank stratification of the moduli space of double covers of a fixed elliptic curve*, arXiv:2502.09540, first posted 2025-02-13. https://arxiv.org/abs/2502.09540
