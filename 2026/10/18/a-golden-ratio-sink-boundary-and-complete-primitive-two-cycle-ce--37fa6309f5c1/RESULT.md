# A golden-ratio sink boundary and complete primitive two-cycle census for a three-dimensional parabolic map

## Finding

Consider the polynomial map \(F_{a,b,c}:\mathbb R^3\to\mathbb R^3\)
\[
F_{a,b,c}(x,y,z)=\big(ay^2,\;by(1-z),\;c(1-x)\big),\qquad a,b,c>0.
\]
Set \(t=b(1-c)\) and \(\kappa=abc\). A *primitive two-cycle* is an unordered pair of distinct real points interchanged by \(F_{a,b,c}\). For every positive parameter triple, its exact number \(N_2\) is
\[
N_2(t)=\begin{cases}
0,&t\geq-1,\\
1,&-2\leq t<-1,\\
3,&t<-2.
\end{cases}
\]
The single cycle first appearing at \(t=-1\) has opposite \(y\)-coordinates and is called the symmetric cycle. Put \(s=-1-t>0\). This cycle is a hyperbolic attracting sink **if and only if**
\[
0<s<\frac{\sqrt5-1}{4},
\quad\text{equivalently}\quad
-\frac{3+\sqrt5}{4}<b(1-c)<-1.
\]
For \((\sqrt5-1)/4<s<1\) it is a hyperbolic saddle with two unstable multipliers, and for \(s>1\) it is a hyperbolic repeller. At \(s=(\sqrt5-1)/4\) two multipliers have modulus one; at \(s=1\) one multiplier equals \(+1\). No nonlinear classification is claimed on these two boundaries. The two additional cycles for \(t<-2\) are never attracting: the determinant of each two-step Jacobian is exactly \(4\), forcing an unstable multiplier. Consequently, when a hyperbolic primitive-two sink exists, it is the only primitive-two sink in the entire real phase space.

## Assumptions and scope

The phase space is all of \(\mathbb R^3\); no positivity restriction is imposed on states. Parameters \(a,b,c\) are strictly positive, so \(\kappa>0\). No invertibility, bounded-orbit assumption, or genericity of the parameters is required. The word *sink* means all multipliers of the two-iterate derivative have modulus strictly less than one. A *repeller* has all three multipliers of modulus strictly greater than one. At a *hyperbolic saddle with two unstable directions*, exactly two multipliers have modulus greater than one and the third has modulus less than one. Distinct two-cycles are counted up to interchange of their points, not up to sign reversal of their \(y\)-coordinates.

For explicit coordinates, write \(U=\sqrt\kappa\,y_0\) and \(V=\sqrt\kappa\,y_1\). Every two-cycle equals \(\{P(U,V),P(V,U)\}\), where
\[
P(U,V)=\left(\frac{aV^2}{\kappa},\frac{U}{\sqrt\kappa},c\left(1-\frac{aU^2}{\kappa}\right)\right).
\]
When \(t<-1\), the symmetric cycle has \((U,V)=(\sqrt s,-\sqrt s)\). When \(t<-2\), set
\[
H=\sqrt{\frac{-t+\sqrt{t^2-4}}{2}}>1.
\]
The two additional cycles have representatives \((U,V)=(H,-H^{-1})\) and \((U,V)=(-H,H^{-1})\). No other primitive two-cycles exist.

## Proof

**1. Exact reduction to the cubic two-cycle equations.** Suppose \(P_0=(x_0,y_0,z_0)\) and \(P_1=(x_1,y_1,z_1)\) are interchanged by \(F\). Periodicity forces
\[
x_0=ay_1^2,\quad x_1=ay_0^2,\quad z_0=c(1-ay_0^2),\quad z_1=c(1-ay_1^2).
\]
Thus the two remaining equations are
\[
y_1=ty_0+\kappa y_0^3,\qquad y_0=ty_1+\kappa y_1^3.
\]
After multiplication by \(\sqrt\kappa\), they become
\[
V=g_t(U),\qquad U=g_t(V),\qquad g_t(w)=tw+w^3.
\]
Conversely, each such real pair with \(U\neq V\) gives the displayed two distinct points, and direct substitution verifies that they are interchanged. Therefore this reduction is a bijection of primitive two-cycles, even though \(g_t\) is **not** asserted to be a global semiconjugate factor of the three-dimensional map.

**2. Exhaustive cycle census.** Subtract and add the two cubic equations, respectively, obtaining
\[
(U-V)\bigl(t+U^2+UV+V^2+1\bigr)=0,
\]
\[
(U+V)\bigl(t+U^2-UV+V^2-1\bigr)=0.
\]
As \(U\neq V\), the first parenthesis vanishes. When \(U+V=0\), it gives \(U^2=-1-t=s\); this supplies exactly one orbit when \(t<-1\), none otherwise. When \(U+V\neq0\), both parentheses vanish; subtraction gives \(UV=-1\), and substitution gives \(U^2+V^2=-t\). For real nonzero \(U,V\), the identity \(U^2+V^2\ge2|UV|=2\) is strict here because equality would give \(U+V=0\). Thus \(t<-2\). Conversely, when \(t<-2\), \(H>1\) as defined above, and both sign-related ordered pairs \((H,-H^{-1})\), \((-H,H^{-1})\) satisfy the cubic equations. Their time reversals complete the four ordered solutions; they define two distinct unordered cycles. There are no solutions with exactly one of \(U,V\) equal to zero, because \(g_t(0)=0\). This proves the counts, including the boundaries \(t=-1,-2\).

**3. Floquet spectrum of the symmetric cycle.** At its two points the \(y\)-coordinates are \(\pm\sqrt{s/\kappa}\), and \(b(1-z)=-1\). At the point with \(y>0\), write \(J\) for the one-step derivative:
\[
J=\begin{pmatrix}0&2ay&0\\0&-1&-by\\-c&0&0\end{pmatrix},
\qquad D=\operatorname{diag}(1,-1,1).
\]
At the opposite point the derivative is \(DJD\). Hence the two-step derivative is \((DJ)^2\). Direct determinant expansion gives
\[
\det(\lambda I-DJ)=\lambda^3-\lambda^2+2\kappa y^2=\lambda^3-\lambda^2+2s.
\]
There is exactly one negative real root \(-r\), where \(r>0\) is uniquely determined by
\[
2s=r^2(r+1).
\]
Indeed the cubic is negative on the negative half-line only up to one crossing, while its two remaining roots are described by the quadratic below; the discriminant of that quadratic may be positive or negative. Factorization gives
\[
\lambda^3-\lambda^2+2s
=(\lambda+r)\left[\lambda^2-(1+r)\lambda+r(1+r)\right].
\]
For \(0<r\le1/3\), the quadratic roots are real, positive and less than one: their sum is \(1+r<2\), and the quadratic evaluated at \(1\) is \(r^2>0\), ruling out exactly one root above one; both above one are excluded by their sum. For \(r>1/3\) they are a nonreal conjugate pair, each of modulus \(\sqrt{r(1+r)}\). Hence the symmetry-matrix spectrum lies in the open unit disk precisely when \(r(r+1)<1\) (with \(r<1\) automatically). Its critical root is
\[
r_*=(\sqrt5-1)/2,
\qquad s_*=\tfrac12r_*^2(1+r_*)=r_*/2=(\sqrt5-1)/4.
\]
Because the return multipliers are the **squares** of the roots of \(DJ\), they have the same inequalities in modulus. When \(r_*<r<1\), the conjugate pair has modulus greater than one and \(|-r|<1\); when \(r>1\), all three moduli exceed one. At \(r=r_*\), two return multipliers have unit modulus; at \(r=1\), the negative symmetry root \(-1\) squares to the unit return multiplier \(+1\). Since \(r^2(r+1)=2s\) is strictly increasing, these cases are exactly the parameter ranges asserted.

**4. Obstruction for the asymmetric cycles.** For any point of the full map,
\[
\det DF(x,y,z)=2abc\,y^2=2\kappa y^2.
\]
On an asymmetric two-cycle the scaled values satisfy \(UV=-1\). The determinant of the two-step derivative is therefore
\[
\det DF^2(P(U,V))=4\kappa^2y_0^2y_1^2=4U^2V^2=4.
\]
Thus at least one multiplier has modulus at least \(4^{1/3}>1\); neither asymmetric orbit can be a sink. The stated uniqueness of the primitive-two sink follows from the complete census.

## Verification

A standalone exact-algebra verifier is provided as `checker.py`. With Python 3 and SymPy installed, run `python checker.py` from the directory containing both files. It checks the cubic reduction, inverse lifts, Jacobian determinant, conjugacy and characteristic polynomial, the golden-ratio identity, and actual fixed/period-two lifts and determinants for ten rational parameter representatives. Its successful execution reported `PASS: 164 exact algebraic/radical identities; ten rational phase representatives.` These are finite diagnostic checks, **not** a substitute for the all-real proof above.

For comparison, the scalar cubic \(g_t\) has an attracting symmetric two-cycle for \(-2<t<-1\), because its two-step multiplier is \((-1+2s)^2<1\) when \(0<s<1\). The three-dimensional map loses two-coordinate transverse stability already at the strictly earlier exact threshold \(s=s_*\). Therefore the cubic period-two count does **not** itself determine the stability result.

## Relationship to prior work

Wang, Tong, Li, Zhang, Iu and Li (2023), Section 2.1, introduced this three-dimensional map and computed fixed-point Jacobians; Section 3.1 investigates parameter-dependent behavior by numerical Lyapunov spectra and bifurcation plots. The map, fixed-point analysis and numerical bifurcations are **not** claimed as new. The present result supplies a complete **primitive two-cycle** census and exact Floquet classification across the positive-parameter family. The underlying cubic two-cycle algebra and the eigenvalue test are standard tools; the model-specific combination, especially the early golden-ratio transverse loss of stability and the determinant-four obstruction for the additional cycles, is the asserted new content.

Meng, Bao and Xu (2011) study an earlier **two-dimensional** parabolic map, which motivated the three-dimensional construction. That different map does not give the displayed three-dimensional two-step Jacobian or its stability boundary. General discrete-map bifurcation calculations might nevertheless imply portions of this theorem; no claim of verified historical priority is made.

## Limitations

The result classifies primitive period-two points **in the full real phase space** and their local linear stability. It does not classify nonhyperbolic nonlinear dynamics on \(t=-1\), \(t=-2\), or \(s=s_*\); the values \(t=-1\) and \(t=-2\) are only included in the exact count. It does not assert stability for higher periods, global attractors, basins, bounded chaotic dynamics, or the four-dimensional **memristor-augmented** map. Exact-algebra tests of finitely many parameters do not establish universal statements; those follow from the proof. Literature searches cannot establish absolute historical novelty.

## References

1. M. Wang, L. Tong, C. Li, X. Zhang, H. H.-C. Iu and Z. Li, “A Novel Four-Dimensional Memristive Hyperchaotic Map Based on a Three-Dimensional Parabolic Chaotic Map with a Discrete Memristor,” *Symmetry* **15** (2023), 1879, doi:10.3390/sym15101879, https://doi.org/10.3390/sym15101879. First verified public appearance: 2023-10-06. Relevant mathematical material: Sections 2.1 and 3.1.
2. J.-D. Meng, B.-C. Bao and Q. Xu, “Dynamics of two-dimensional parabolic discrete map,” *Acta Physica Sinica* **60** (2011), 010504, doi:10.7498/aps.60.010504, https://doi.org/10.7498/aps.60.010504.
