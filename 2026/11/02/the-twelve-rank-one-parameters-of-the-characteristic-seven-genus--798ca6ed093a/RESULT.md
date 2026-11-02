# The twelve rank-one parameters of the characteristic-seven genus-three Howe family

## Finding
Let \(k=\overline{\mathbb F}_7\) and, for \(a,b\in k\) with \((a-b)(a^2-4)(b^2-4)\ne0\), let \(C_{a,b}\) be the smooth projective model of
\[
y^2=(x^4-ax^2+1)(x^4-bx^2+1).
\]
These genus-three curves possess three commuting non-hyperelliptic involutions and elliptic quotients. Put \(s=a+b\), \(q=ab\), and define all polynomials over \(\mathbb F_7\):
\[
\begin{aligned}
H_0&=q^3-q^2-qs^2-3q-3s^2-1,\\
H_+&=-(a+b+4)(a-2b-2)(a-4b-6),\\
H_-&=-(a+b-4)(a-2b+2)(a-4b+6).
\end{aligned}
\]
For every such geometric parameter, the Jacobian \(7\)-rank and \(a\)-number are exactly
\[
f_7(C_{a,b})=\mathbf1_{H_0\ne0}+\mathbf1_{H_+\ne0}+\mathbf1_{H_-\ne0},\qquad a(C_{a,b})=3-f_7(C_{a,b}).
\]
The complete rank-at-most-one locus, as a set of geometric points, consists exclusively of fourteen \(\mathbb F_7\)-rational **ordered marked parameters**: precisely two rank-zero parameters \((3,4),(4,3)\), and the twelve rank-one parameters
\[
(0,3),(0,4),(1,3),(1,4),(3,0),(3,1),(3,6),
(4,0),(4,1),(4,6),(6,3),(6,4).
\]
All twenty smooth ordered \(\mathbb F_7\)-parameters have nonordinary Jacobians: two have rank zero, twelve rank one, and six rank two.

## Assumptions and scope
Work over the algebraic closure of \(\mathbb F_7\). Parameter pairs are ordered and distinguish the two quartic factors; no assertion about the number of geometric isomorphism classes is made. The smoothness condition is necessary, since each quartic has repeated roots for \(a=\pm2\) or \(b=\pm2\), and the two factors share roots when \(a=b\). As the branch polynomial is squarefree of degree eight, the smooth projective model has genus three. The symbol \(a(C)\) denotes the Jacobian's \(a\)-number and should not be confused with the coefficient \(a\).

## Proof
Write \(f(x)=(x^4-ax^2+1)(x^4-bx^2+1)\) and \(c_j=[x^j]f(x)^3\). The standard hyperelliptic Cartier–Manin coefficient formula in characteristic seven, using differentials \(dx/y,x\,dx/y,x^2\,dx/y\), gives the matrix
\[
M=(c_{7i-j})_{1\le i,j\le3}=
\begin{pmatrix}c_6&0&c_4\\0&c_{12}&0\\c_4&0&c_6\end{pmatrix}.
\]
The same coefficient identities give
\[
c_{12}=H_0,\qquad c_6-c_4=H_+,\qquad c_6+c_4=H_-.
\]
Indeed, explicit expansion modulo seven yields the displayed polynomial \(H_0\), and factors the other two as the products of three affine linear forms. Conjugating \(M\) by the constant matrix whose columns are \((1,0,1),(0,1,0),(1,0,-1)\) yields \(\operatorname{diag}(H_-,H_0,H_+)\). Because this change-of-basis matrix lies in \(\mathrm{GL}_3(\mathbb F_7)\), it also diagonalizes all Frobenius-semilinear products: every nonzero diagonal entry stays nonzero under Frobenius powers. Consequently, the stable Cartier rank is the number of nonzero \(H\)-values, proving the \(7\)-rank formula. The ordinary Cartier rank equals the same number; the standard relation \(a(C)=3-\operatorname{rank}(M)\) proves the \(a\)-number formula.

For completeness over the *entire algebraic closure*, a rank-at-most-one point must lie on two of the three divisors \(H_0=0\), \(H_+=0\), \(H_-=0\). Intersections of a linear factor of \(H_+\) with a linear factor of \(H_-\) are rational over \(\mathbb F_7\) whenever unique; parallel factors do not meet in the affine plane. For the intersections involving \(H_0\), substituting the three \(H_+\)-line equations \(b=-a-4,\ b=4(a-2),\ b=2(a-6)\) produces, respectively,
\[
-a(a-3)(a+2)^4,\quad (a-3)(a+2)^4(a+3),\quad (a-1)(a+2)^4(a+3).
\]
Substituting the three \(H_-\)-line equations \(b=-a+4,\ b=4(a+2),\ b=2(a+6)\) produces
\[
-a(a-2)^4(a+3),\quad (a-3)(a-2)^4(a+3),\quad (a-3)(a-2)^4(a+1).
\]
Thus each intersection of distinct \(H\)-divisors, including intersections over \(\overline{\mathbb F}_7\), has coordinates in \(\mathbb F_7\). Directly evaluating their zeros at the twenty smooth \(\mathbb F_7\)-pairs leaves exactly the two rank-zero pairs, twelve listed rank-one pairs, and six rank-two pairs. No other geometric rank-at-most-one points exist. As a separate finite-field check, the \(\mathbb F_{49}\) smooth parameter census gives counts \((2,12,384,1764)\) by ranks \((0,1,2,3)\). This last census corroborates rather than establishes the algebraic-closure exhaustiveness.

## Verification
Run `python3 verify_symbolic.py` with SymPy and `python3 verify_fields.py` with standard Python. The first independently expands the degree-eight branch polynomial, reconstructs the Hasse matrix, verifies its diagonalization, tests all six line restrictions and the complete rational list. The second implements arithmetic in \(\mathbb F_7\) and \(\mathbb F_{49}\) without a symbolic algebra library, reconstructs Hasse coefficient matrices and elliptic quotient Hasse invariants, and compares results. Successful outputs are `HOWE_7_SYMBOLIC_OK` and `HOWE_7_FIELD_OK`, respectively. The algebraic proof above, not the bounded field census, establishes exhaustiveness over \(k\).

## Relationship to prior work
Ohashi's 2021 description of genus-three Howe curves gives this family, its smoothness hypotheses, and the degree-eight product isogeny from three elliptic quotients, as well as superspecial criteria; it does not state the characteristic-seven complete rank-one parameter list or these factored three-invariant rank strata. Achter–Howe establishes conventions for Cartier versus Hasse–Witt semilinearity; Frei treats general hyperelliptic \(a\)-numbers and coefficient matrices. The rank-zero members here include the familiar Fermat-type curve, so the two rank-zero points themselves are not advanced as a new existence construction. The new scope is the exhaustive, algebraic-closure-valid characteristic-seven rank-one and nonordinary parameter classification in this symmetric family.

## Limitations
This is a classification of ordered coefficients for one two-dimensional family in characteristic seven, not a classification of all genus-three curves or their isomorphism classes. Prior unindexed calculations using elliptic quotients could contain this specialization; searches cannot establish absolute priority. The factorization of \(H_0\) into irreducible geometric components and scheme-theoretic multiplicities of intersections are not asserted. No independent external audit has been performed.

## References
1. R. Ohashi, *On the maximality of genus-3 Howe curves*, arXiv:2112.11152, first version December 21, 2021.
2. J. Achter and E. Howe, *Hasse–Witt and Cartier–Manin matrices: a warning and a request*, 2018.
3. S. Frei, *The a-number of hyperelliptic curves*, arXiv:1703.03516, 2017.
