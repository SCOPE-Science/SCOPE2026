# Two equilibria at the zero-dissipation boundary of the Liu–Wu–Fu scroll flow
## Finding
Consider the Liu–Wu–Fu system
\[
\dot x=y(a-z),\qquad \dot y=z(x-b),\qquad \dot z=x(c+y)-dz.
\]
For real parameters with \(a b c\neq0\), the zero-dissipation boundary \(d=0\) has exactly two equilibria,
\[
E_0=(0,0,0),\qquad E_1=(b,-c,a),
\]
not a unique equilibrium. Their characteristic polynomials are
\[
\chi_{E_0}(\lambda)=\lambda^3+abc,\qquad
\chi_{E_1}(\lambda)=\lambda^3-abc.
\]
Hence both equilibria are hyperbolic. If \(abc>0\), then \(E_0\) has unstable dimension two and \(E_1\) has unstable dimension one; if \(abc<0\), the unstable dimensions are one and two, respectively. The divergence is identically zero at \(d=0\), so this parameter boundary is volume preserving wherever the flow is defined. As \(d\to0\) with \(abc\neq0\), the source's finite equilibria \(S_1\) and \(S_2\) tend to \(E_0\) and \(E_1\), while \(S_3=(b,0,bc/d)\) escapes to infinity.

## Assumptions and scope
The claim concerns the printed autonomous system above with real \(a,b,c\neq0\) and exactly \(d=0\). The excluded cases \(a=0\), \(b=0\), or \(c=0\) can contain additional degeneracies and are not classified here. No claim is made about the source's numerical chaotic regimes, all of which use \(d>0\), nor about global boundedness at \(d=0\).

## Proof
At \(d=0\), an equilibrium satisfies
\[
y(a-z)=0,\qquad z(x-b)=0,\qquad x(c+y)=0.
\]
If \(z=0\), then \(a\neq0\) forces \(y=0\), and then \(c\neq0\) forces \(x=0\). Thus this branch gives only \(E_0=(0,0,0)\).

If \(z\neq0\), then \(x=b\). Because \(b\neq0\), the third equilibrium equation gives \(y=-c\). Since \(c\neq0\), the first equation then gives \(z=a\). Thus this branch gives only \(E_1=(b,-c,a)\). Therefore there are exactly two equilibria.

The Jacobian is
\[
J(x,y,z)=
\begin{pmatrix}
0&a-z&-y\\
z&0&x-b\\
c+y&x&-d
\end{pmatrix}.
\]
At \(d=0\),
\[
J(E_0)=
\begin{pmatrix}
0&a&0\\
0&0&-b\\
c&0&0
\end{pmatrix},
\qquad
J(E_1)=
\begin{pmatrix}
0&0&c\\
a&0&0\\
0&b&0
\end{pmatrix}.
\]
Direct determinants give
\[
\det(\lambda I-J(E_0))=\lambda^3+abc,
\qquad
\det(\lambda I-J(E_1))=\lambda^3-abc.
\]
For \(abc>0\), the roots of \(\lambda^3=-abc\) are one negative real root and a complex pair with positive real part, while the roots of \(\lambda^3=abc\) are one positive real root and a complex pair with negative real part. The roles reverse when \(abc<0\). None of these roots has zero real part, so both equilibria are hyperbolic with the stated unstable dimensions.

Finally, the divergence of the vector field is \(-d\), hence is identically zero at \(d=0\). The source's formulas \(S_1=(0,0,0)\), \(S_2=(b,(ad-bc)/b,a)\), and \(S_3=(b,0,bc/d)\) show directly that \(S_1\to E_0\), \(S_2\to E_1\), and \(|S_3|\to\infty\) as \(d\to0\) when \(bc\neq0\).

## Verification
The accompanying `verify.py` reconstructs the printed vector field symbolically, substitutes both equilibrium candidates, computes the two Jacobians and their characteristic polynomials, and checks the divergence. Its recorded output is `VERIFY_OK`.

The classification is algebraic and exhaustive under \(abc\neq0\); no numerical root search or finite sampling is used.

## Relationship to prior work
Liu, Wu, and Fu introduce the system and state in Section 2 that when \(d=0\) it has a unique equilibrium \((b,-c,a)\). Direct substitution shows that the origin remains an equilibrium as well. Their displayed characteristic equation for \(S_1\), specialized to \(d=0\), is \(\lambda^3+abc=0\), while their displayed characteristic equation for \(S_2\), specialized to \(d=0\), is \(\lambda^3-abc=0\); these are exactly the two spectra above.

A closely related published analysis of the same flow concerns the local weak-focus character of \(S_3\) for \(d>0\). That statement neither treats the zero-dissipation boundary nor implies the two-equilibrium classification and complementary unstable indices proved here.

## Limitations
The result is restricted to the natural generic boundary \(abc\neq0\), \(d=0\). It does not classify the further degenerate coordinate hyperplanes \(a=0\), \(b=0\), or \(c=0\), and it does not establish existence of periodic, quasiperiodic, or chaotic invariant sets at \(d=0\). It also does not alter the source's later simulations performed with \(d>0\).

## References
1. M. Liu, Z. Wu, X. Fu, “Dynamical Analysis of a One- and Two-Scroll Chaotic System,” *Mathematics* 10 (2022), 4682. DOI: 10.3390/math10244682. Published 9 December 2022. MSC 34C28.
