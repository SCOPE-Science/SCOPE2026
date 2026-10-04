# Two missed equilibria and an exact stability threshold in the Fu–Cheng–Liu hyperchaotic flow
## Finding
Consider the smooth four-dimensional flow
\[
\dot x=35(y-x)+w,\qquad
\dot y=12y-10xz,\qquad
\dot z=-3z+10xy,\qquad
\dot w=dy+x^2,
\]
with parameter \(d>0\). It has exactly three equilibria, not one:
\[
O=(0,0,0,0),
\]
and
\[
E_\sigma=\left(
\sigma\frac35,
-\frac{9}{25d},
-\sigma\frac{18}{25d},
35\left(\sigma\frac35+\frac{9}{25d}\right)
\right),\qquad \sigma\in\{-1,+1\}.
\]
The origin is never asymptotically stable because its spectrum is exactly
\[
\{-35,12,-3,0\}.
\]

On the parameter range \(0<d\le 30\) used in the source's sweep, \(E_{+1}\) always has exactly one eigenvalue in the open right half-plane. The negative branch \(E_{-1}\) is asymptotically stable exactly for
\[
0<d<d_H,\qquad
d_H=\frac{119105-455\sqrt{68521}}{3}
\approx 0.617107352606750.
\]
At \(d=d_H\), its Jacobian has one simple imaginary pair
\[
\lambda=\pm i\omega_H,\qquad
\omega_H^2=\frac{9(261+\sqrt{68521})}{50},
\]
while the remaining two eigenvalues have negative real part. For \(d_H<d\le30\), \(E_{-1}\) has exactly two eigenvalues in the open right half-plane.

Thus the source's statements that the system has a sole equilibrium and that the regime \(27<d\le30\) is stable at the origin are incompatible with its displayed vector field. In the small-\(d\) interval \(0<d<d_H\), any non-equilibrium attractor would necessarily coexist with the open basin of the stable equilibrium \(E_{-1}\).

## Assumptions and scope
The statement concerns the vector field printed in Fu, Cheng, and Liu, with the source parameters \(a=35\), \(b=3\), \(c=12\) and variable \(d>0\). The stability classification is proved on \(0<d\le30\), matching the source's displayed parameter sweep. The result is local at equilibria except for the exhaustive algebraic enumeration of equilibria.

The phrase “spectral Hopf point” is used only for the simple imaginary-pair crossing of the Jacobian at \(d=d_H\). No nonlinear Hopf bifurcation, branch of periodic orbits, global boundedness, or existence of a hyperchaotic attractor is asserted here.

## Proof
At an equilibrium, the fourth equation gives
\[
dy+x^2=0,
\]
so
\[
y=-\frac{x^2}{d}.
\]
If \(x=0\), then \(y=0\); the second and third equations give \(z=0\), and the first gives \(w=0\). Hence \(O\) is one equilibrium.

Assume now \(x\ne0\). From \(12y-10xz=0\),
\[
z=\frac{12y}{10x}=-\frac{6x}{5d}.
\]
Substituting this and \(y=-x^2/d\) into \(-3z+10xy=0\) yields
\[
\frac{18x}{5d}-\frac{10x^3}{d}=0.
\]
Since \(x\ne0\),
\[
x^2=\frac{9}{25},
\]
so \(x=\sigma 3/5\), \(\sigma\in\{-1,+1\}\). Back-substitution gives the displayed \(y\), \(z\), and \(w=35(x-y)\). This proves the equilibrium list is exhaustive.

The Jacobian is
\[
J(x,y,z)=
\begin{pmatrix}
-35&35&0&1\\
-10z&12&-10x&0\\
10y&10x&-3&0\\
2x&d&0&0
\end{pmatrix}.
\]
At \(O\),
\[
\det(\lambda I-J(O))
=\lambda(\lambda+35)(\lambda+3)(\lambda-12),
\]
which proves the stated spectrum and instability for every \(d>0\).

For \(E_{+1}\), direct substitution gives
\[
p_+(\lambda)=
\lambda^4+26\lambda^3
-\frac{1581d+1260}{5d}\lambda^2
+\frac{18d-7560}{5d}\lambda
-\frac{216}{5}.
\]
Its Routh first column is
\[
1,\quad
26,\quad
-\frac{6(3427d+2100)}{65d},\quad
\frac{18(47d^2-1437240d-882000)}
{5d(3427d+2100)},\quad
-\frac{216}{5}.
\]
The positive root of \(47d^2-1437240d-882000\) is larger than \(30\), while its other root is negative. Hence on \(0<d\le30\) the signs are
\[
+,+,-,-,-.
\]
Routh's criterion therefore gives exactly one right-half-plane eigenvalue.

For \(E_{-1}\),
\[
p_-(\lambda)=
\lambda^4+26\lambda^3
+\frac{1260-1569d}{5d}\lambda^2
+\frac{7560-18d}{5d}\lambda
+\frac{216}{5}.
\]
The Routh first column is
\[
1,\quad
26,\quad
-\frac{12(1699d-1050)}{65d},\quad
-\frac{54(3d^2-238210d+147000)}
{5d(1699d-1050)},\quad
\frac{216}{5}.
\]
The smaller positive root of
\[
3d^2-238210d+147000=0
\]
is exactly \(d_H\); the other positive root is larger than \(30\). Also
\[
d_H<\frac{1050}{1699}<30.
\]
Thus, for \(0<d<d_H\), all entries in the Routh first column are positive and \(E_{-1}\) is asymptotically stable. For \(d_H<d<1050/1699\), the signs are \(+,+,+,-,+\), giving two right-half-plane roots. For \(1050/1699<d\le30\), the signs are \(+,+,-,+,+\), again giving two right-half-plane roots. At \(d=1050/1699\), the polynomial has no imaginary-axis root because
\[
3d^2-238210d+147000
=-\frac{621075000}{2886601}\ne0,
\]
so the right-half-plane count remains two by continuity.

At \(d=d_H\), the Routh crossing condition vanishes. Setting
\[
\omega_H^2=\frac{7560-18d_H}{130d_H}
=\frac{9(261+\sqrt{68521})}{50}>0
\]
gives the exact factorization
\[
p_-(\lambda;d_H)
=(\lambda^2+\omega_H^2)
\left(
\lambda^2+26\lambda
-\frac{783}{5}+\frac{3\sqrt{68521}}{5}
\right).
\]
The final quadratic has positive constant term and positive linear coefficient, so both remaining roots have negative real part. The Routh count changes from zero to two across \(d_H\), giving the stated simple spectral crossing.

## Verification
The bundled `verify.py` reconstructs the three equilibria, checks every equilibrium residual symbolically, derives both characteristic polynomials directly from the Jacobian, reconstructs the Routh first columns, verifies the defining quadratic for \(d_H\), and checks the exact factorization at the spectral crossing. Running it from the package directory returns `VERIFY_OK`.

The proof itself is exact algebra plus the classical Routh criterion. Numerical approximations are used only to report the decimal value of \(d_H\), not to establish the theorem.

## Relationship to prior work
Fu, Cheng, and Liu introduce exactly this vector field and state that it has only the origin as an equilibrium. Their equilibrium linearization at the origin also displays the eigenvalues \(-35\), \(12\), \(-3\), and \(0\), while their subsequent parameter-sweep discussion labels \(27<d\le30\) as stable at the origin. The equilibrium completion and the exact off-origin stability threshold above are not present in the checked source.

Exact-title, DOI, formula, parameter, correction, and equilibrium searches were also compared against published-finding corpus records and indexed web literature. The closest published-finding corpus findings concern different flows and do not imply the three-equilibrium classification or the threshold \(d_H\).

## Limitations
This result does not prove that any numerical hyperchaotic attractor reported by the source exists, is invariant under exact arithmetic, or coexists with \(E_{-1}\). It does not determine basin boundaries, global dissipativity beyond the constant-divergence calculation, nonlinear Hopf nondegeneracy, periodic-orbit creation at \(d_H\), or consequences for the audio-encryption construction.

The literature comparison was targeted rather than exhaustive. An unindexed later note, thesis, or correction could independently contain the same equilibrium completion or threshold.

## References
1. S. Fu, X. Cheng, and J. Liu, “Dynamics, circuit design, feedback control of a new hyperchaotic system and its application in audio encryption,” *Scientific Reports* **13**, 19385 (2023). DOI: 10.1038/s41598-023-46161-5.
2. Mathematical Reviews, MSC2020, 37C25: fixed points and periodic points of dynamical systems; fixed-point index theory; local dynamics.
