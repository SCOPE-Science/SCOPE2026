# Complete equilibrium geometry and zero-Hopf strata of a cubic line-equilibrium oscillator

## Finding

Consider
\[
\dot x=F(y)+a_4x^2,\qquad
\dot y=-a_5xz,\qquad
\dot z=a_6xy+a_7x^2,
\]
with
\[
F(y)=a_1y^3-a_2y^2-a_3y
\]
and \(a_i>0\) for \(i=1,\ldots,7\). The complete equilibrium set is exactly three affine lines and two isolated points. Put
\[
\Delta=\sqrt{a_2^2+4a_1a_3},\qquad
r_\pm=\frac{a_2\pm\Delta}{2a_1},
\]
and
\[
B=\frac{a_4a_6^2}{a_7^2}-a_2,\qquad
s_\pm=\frac{-B\pm\sqrt{B^2+4a_1a_3}}{2a_1}.
\]
Then the equilibrium set is
\[
L_0=\{(0,0,z):z\in\mathbb R\},\qquad
L_\pm=\{(0,r_\pm,z):z\in\mathbb R\},
\]
together with
\[
P_\pm=\left(-\frac{a_6}{a_7}s_\pm,s_\pm,0\right).
\]

For a point \((0,r,z)\) on any of the three lines,
\[
\chi_{r,z}(\lambda)=\lambda\left(\lambda^2+a_5zF'(r)\right).
\]
Since \(F'(0)=-a_3<0\) and \(F'(r_\pm)>0\), the zero-Hopf locus is precisely
\[
\{(0,0,z):z<0\}\ \cup\
\{(0,r_+,z):z>0\}\ \cup\
\{(0,r_-,z):z>0\}.
\]
The complementary open half-lines have a real normal saddle pair, and every line point with \(z=0\) has a triple-zero spectrum.

At the published chaotic parameter set
\[
a_1=\frac1{10},\qquad a_2=a_3=a_4=a_5=a_6=1,\qquad a_7=\frac15,
\]
the three equilibrium lines occur at
\[
y=0,\qquad y=5+\sqrt{35},\qquad y=5-\sqrt{35}.
\]
On these lines the zero-Hopf frequencies are respectively
\[
\sqrt{-z},\qquad
\sqrt{z(7+\sqrt{35})},\qquad
\sqrt{z(7-\sqrt{35})}
\]
on their stated sign half-lines. The displayed line formula in the introducing article instead contains the radicand \(4a_1a_3-a_2^2\), which equals \(-3/5\) at these parameters and therefore cannot describe the real equilibrium lines.

## Assumptions and scope

All seven parameters are strictly positive, as in the parameter regime used for the article's principal chaotic example. The claim is an exact algebraic and linear-spectral classification of equilibria of the printed vector field. It does not assert nonlinear stability at the nonhyperbolic line points, nor does it establish or exclude periodic or chaotic invariant sets away from the equilibrium manifold.

A zero-Hopf line point here means that the Jacobian has one zero eigenvalue and one nonzero purely imaginary conjugate pair. The zero eigenvalue is tangent to the equilibrium line.

## Proof

At an equilibrium,
\[
F(y)+a_4x^2=0,\qquad -a_5xz=0,\qquad x(a_6y+a_7x)=0.
\]

If \(x=0\), the first equation reduces to
\[
F(y)=y(a_1y^2-a_2y-a_3)=0.
\]
Because \(a_1,a_2,a_3>0\), the quadratic factor has discriminant \(a_2^2+4a_1a_3>0\), with one positive and one negative root \(r_+\) and \(r_-\). The variable \(z\) is unrestricted. This gives exactly \(L_0,L_+,L_-\).

If \(x\ne0\), the second equation forces \(z=0\), and the third forces
\[
x=-\frac{a_6}{a_7}y.
\]
The value \(y=0\) would imply \(x=0\), so \(y\ne0\). Substitution into the first equation gives
\[
a_1y^2+By-a_3=0,
\qquad
B=\frac{a_4a_6^2}{a_7^2}-a_2.
\]
Its discriminant \(B^2+4a_1a_3\) is strictly positive and its constant term is negative, so it has exactly the two real nonzero roots \(s_+\) and \(s_-\). These give exactly \(P_+\) and \(P_-\). The two cases exhaust the equation \(x(a_6y+a_7x)=0\), proving completeness.

The Jacobian is
\[
J(x,y,z)=
\begin{pmatrix}
2a_4x&F'(y)&0\\
-a_5z&0&-a_5x\\
a_6y+2a_7x&a_6x&0
\end{pmatrix}.
\]
At \((0,r,z)\),
\[
\det(\lambda I-J)
=\lambda\left(\lambda^2+a_5zF'(r)\right).
\]
For \(r=0\), \(F'(0)=-a_3<0\). For either nonzero root \(r_\pm\), write \(F(y)=yq(y)\), where \(q(y)=a_1y^2-a_2y-a_3\). Since \(q(r_\pm)=0\),
\[
F'(r_\pm)=r_\pm q'(r_\pm).
\]
Here \(r_+>0\) and \(q'(r_+)=\Delta>0\), while \(r_-<0\) and \(q'(r_-)=-\Delta<0\). Thus \(F'(r_\pm)>0\). The sign classification of the quadratic factor in \(\chi_{r,z}\) now gives the stated zero-Hopf, saddle-normal, and triple-zero strata.

## Verification

The equilibrium equations were reconstructed directly from the printed system and solved by the exhaustive split \(x=0\) versus \(x\ne0\). The Jacobian determinant was independently expanded symbolically from the reconstructed vector field. Substitution of both isolated-root formulas into all three equilibrium equations simplifies identically to zero.

At the article's numerical parameters, direct substitution gives \(r_\pm=5\pm\sqrt{35}\) and \(s_\pm=-120\pm\sqrt{14410}\). The line characteristic polynomial specializes to the three frequencies stated above. These checks use exact algebra; numerical trajectory experiments are not part of the proof.

## Relationship to prior work

Almatroud, Shukur, Pham, and Grassi introduce this exact vector field and analyze its equilibrium structure and zero-Hopf behavior. Their displayed equilibrium-line formula uses \(\sqrt{4a_1a_3-a_2^2}\), and Proposition 1 states a different parameter condition for a point \((0,0,z)\) to be zero-Hopf. The exact case split above instead gives the plus-discriminant \(a_2^2+4a_1a_3\), adds the full line \(L_0\), identifies the two isolated equilibria for positive parameters, and locates the zero-Hopf strata by the sign of \(zF'(r)\).

Veeman, Natiq, Ali, Rajagopal, and Hussain analyze a different conservative oscillator with one equilibrium line and show that spectral type varies along that line. That general phenomenon does not determine the equilibrium set or zero-Hopf locus of the present cubic oscillator.

Semantic searches of the published mathematical-finding index for the article title, DOI, exact vector-field monomials, equilibrium-line aliases, and zero-Hopf formulations returned no same-system result that states or implies this classification. The closest returned items concern zero-Hopf or equilibrium geometry in different vector fields.

## Limitations

The classification is restricted to the printed three-dimensional system with \(a_i>0\). It does not repair or reassess the article's control, synchronization, Lyapunov-exponent, or secure-communications results. It also does not supply a nonlinear center-manifold analysis of the nonisolated zero-Hopf points. The first public-date evidence used here is a public author-upload record dated 13 June 2024; the journal page lists 16 June 2024.

## References

1. O. A. Almatroud, A. A. Shukur, V.-T. Pham, and G. Grassi, “Oscillator with Line of Equilibiria and Nonlinear Function Terms: Stability Analysis, Chaos, and Application for Secure Communications,” *Mathematics* 12 (2024), 1874. DOI: 10.3390/math12121874.
2. D. Veeman, H. Natiq, A. M. Ali Ali, K. Rajagopal, and I. Hussain, “A Simple Conservative Chaotic Oscillator with Line of Equilibria: Bifurcation Plot, Basin Analysis, and Multistability,” *Complexity* 2022 (2022), 9345036. DOI: 10.1155/2022/9345036.
