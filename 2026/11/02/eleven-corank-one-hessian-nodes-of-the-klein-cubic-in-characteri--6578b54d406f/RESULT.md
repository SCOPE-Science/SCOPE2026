# Eleven corank-one Hessian nodes of the Klein cubic in characteristic three

## Finding
Let \(k=\overline{\mathbb F}_3\), with cyclic indices in \(\mathbb Z/5\mathbb Z\), and let
\[
F(x_0,\ldots,x_4)=\sum_{i=0}^{4}x_i^2x_{i+1},\qquad
\mathcal K=V(F)\subset\mathbb P^4_k.
\]
Write \(M(x)=(\partial_i\partial_j F)(x)\) and \(\mathcal H=V(\det M)\subset\mathbb P^4_k\) for the Hessian quintic. Among points of \(\mathcal H\) where \(M\) has **rank exactly four**, the singular points of \(\mathcal H\) are precisely
\[
P_t=[1:t:t^{-1}:t^3:t^{-5}],\qquad t^{11}=1.
\]
There are exactly eleven such points. Each is an ordinary double point of the hypersurface \(\mathcal H\), and none belongs to \(\mathcal K\). The eleven-point reduced subscheme is defined over \(\mathbb F_3\); Frobenius acts with orbit lengths \((1,5,5)\). In particular exactly one of these nodes is \(\mathbb F_3\)-rational, and all are defined over \(\mathbb F_{3^5}\).

## Assumptions and scope
All geometric statements concern an algebraically closed field of characteristic exactly three. The rank condition means rank four of the *five-by-five Hessian matrix of the original cubic*, not rank of the tangent quadratic form of the Hessian quintic. The assertion **classifies only the corank-one part of the singular locus**; no claim is made that these eleven points exhaust singularities where \(\operatorname{rank}M\le3\). The displayed points carry the reduced structure for the stated arithmetic splitting.

## Proof
Set \(D=\det M\). At any point \(x\) where \(M(x)\) has rank four, choose a nonzero kernel vector \(v\). Since \(M\) is symmetric, its adjugate is \(c vv^{\mathsf T}\) for a nonzero scalar \(c\). The determinantal derivative formula therefore gives
\[
\frac{\partial D}{\partial x_j}(x)
=c\,v^{\mathsf T}\bigl(\partial_{x_j}M\bigr)v
=c\bigl(2v_{j-1}^{2}+4v_jv_{j+1}\bigr).
\]
In characteristic three, these five derivatives vanish exactly when
\[
v_{j-1}^{2}=v_jv_{j+1}\quad(j\in\mathbb Z/5\mathbb Z).\tag{1}
\]
If any coordinate of a nonzero solution of (1) vanishes, repeated use of (1) forces every coordinate to vanish, a contradiction. Scale to \(v_0=1\), write \(v_1=t\), and solve (1) successively to get
\[
v=(1,t,t^{-1},t^3,t^{-5}),\qquad t^{11}=1.
\]
Conversely these eleven vectors solve (1); they are distinct because the eleventh roots of unity are simple in characteristic three.

The trilinear third derivatives of the cubic are symmetric, so \(M(x)v=M(v)x\). For the above \(v\), equations (1) are also precisely \(\nabla F(v)=0\). Differentiated Euler's identity gives \(M(v)v=2\nabla F(v)=0\).

At \(v=(1,1,1,1,1)\), the matrix \(M(v)\) has diagonal entries \(2\), entries \(2\) on the two cyclic adjacent diagonals, and zeros elsewhere. Its row sums vanish in characteristic three, while its leading four-by-four determinant is \(-16\), nonzero modulo three. Hence its kernel is exactly \(kv\). For any \(t^{11}=1\), the diagonal map
\[
A_t=\operatorname{diag}(1,t,t^{-1},t^3,t^{-5})
\]
satisfies \(F(A_tx)=tF(x)\); consequently the ranks of \(M(P_t)\) are all four and \(\ker M(P_t)=kP_t\). Thus \(M(x)v=0\) forces \(x=P_t\), proving completeness of the rank-four singular set, as well as the converse existence claim by the adjugate derivative formula.

In the affine chart \(x_0=1\), put \(x_i=1+u_i\) for \(1\le i\le4\). Direct expansion of \(D\) modulo three has zero constant and linear terms, and homogeneous quadratic part
\[
Q(u)=-u_1^2-u_2^2-u_3^2-u_4^2+u_1u_2+u_2u_3+u_3u_4.
\]
Its symmetric Hessian matrix is tridiagonal with diagonal \(-2\) and neighboring entries \(1\), and has determinant \(5\equiv2\pmod3\). Hence \(P_1\) is an ordinary quadratic double point. The projective automorphisms \(A_t\) transport this germ to each \(P_t\), so all eleven are ordinary double points.

Because every monomial of \(F(P_t)\) equals \(t\), one has \(F(P_t)=5t=2t\ne0\), so these nodes lie off the cubic. Finally, geometric Frobenius sends \(P_t\) to \(P_{t^3}\). The order of \(3\) modulo \(11\) is \(5\), giving the orbit structure \((1,5,5)\); equivalently \(T^{11}-1\) over \(\mathbb F_3\) has one linear and two irreducible quintic factors.

## Verification
The included standalone `verify.py` recomputes the five-by-five Hessian determinant modulo three, tests the diagonal critical point and Hessian rank, extracts the exact quadratic tangent cone and its nonzero determinant, and verifies the factor degrees \((1,5,5)\) of \(T^{11}-1\). It prints `VERIFY_OK`. The completeness argument is the symbolic adjugate-and-kernel proof above; finite-field sampling is not substituted for geometric completeness.

## Relationship to prior work
The Klein cubic and its characteristic-zero Hessian singular curve are classical. In particular Fisher's treatment identifies the modular curve \(X(11)\) as the singular locus of the Hessian of this cubic in characteristic zero (a statement about the classical fiber). The present claim concerns a different, explicitly delimited feature of the characteristic-three Hessian: its complete **rank-four** singular stratum, which comprises isolated ordinary nodes lying outside the original cubic. The established characteristic-zero description and general Hessian rank-drop statements do not imply this exceptional-characteristic stratum.

## Limitations
No classification, multiplicity, or resolution is asserted for the corank-at-least-two Hessian locus, nor is a complete resolution of the Hessian quintic constructed. The arithmetic claim concerns the eleven-node reduced subscheme only. An unindexed treatment of the characteristic-three specialization could affect historical priority. These calculations have not undergone independent verification.

## References
- T. Fisher, *On families of 7- and 11-congruent elliptic curves*, LMS J. Comput. Math. 17 (2014), 536–564; DOI: 10.1112/S1461157014000059, especially the characteristic-zero Hessian construction. An earlier related publicly dated version is arXiv:1105.1706 (9 May 2011).
- X. Roulleau, *The Fano surface of the Klein cubic threefold*, arXiv:1001.4853 (2010); background on the classical cubic and its automorphisms.
- A. Adler, *Invariants of \(\mathrm{PSL}_2(\mathbb F_{11})\) acting on \(\mathbb C^5\)*, Comm. Algebra 20 (1992), 2837–2862; historical source cited by Fisher, not used for a characteristic-three classification.
