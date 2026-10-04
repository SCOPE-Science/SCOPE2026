# A sharp stability boundary for the isolated equilibria of a line-equilibrium chaotic flow
## Finding
Consider the integer-order polynomial flow
\[
\dot x=yz-ax,\qquad \dot y=cx-axz,\qquad \dot z=xy-bz,
\]
with \(a,b,c>0\). Besides the equilibrium line \((0,h,0)\), the flow has the two isolated equilibria
\[
E_{\pm}=\left(\pm\frac{c\sqrt{ab}}{a^2},\ \pm\sqrt{ab},\ \frac ca\right).
\]
At either isolated equilibrium the characteristic polynomial is exactly
\[
p(\lambda)=\lambda^3+(a+b)\lambda^2+\frac{bc^2}{a^2}\lambda+\frac{2bc^2}{a}.
\]
Consequently, \(E_+\) and \(E_-\) are asymptotically stable if and only if \(b>a\). If \(0<b<a\), each isolated equilibrium is hyperbolic with exactly two eigenvalues in the open right half-plane and one in the open left half-plane. On the boundary \(b=a\),
\[
p(\lambda)=(\lambda+2a)\left(\lambda^2+\frac{c^2}{a}\right),
\]
so the spectrum is \(-2a\) together with the simple pair \(\pm i c/\sqrt a\).

For the parameters used in the source, \((a,b,c)=(5,2,34)\),
\[
p(\lambda)=\lambda^3+7\lambda^2+\frac{2312}{25}\lambda+\frac{4624}{5},
\]
and the roots are approximately
\[
-8.6570969514,\qquad 0.8285484757\pm 10.3023859562i.
\]
Thus the source's reported zero eigenvalue at the isolated equilibria is incompatible with the printed vector field; the exact isolated equilibria have unstable dimension two at those parameters.

## Assumptions and scope
The claim concerns the classical integer-order autonomous ODE above with real parameters \(a,b,c>0\). It classifies only the two isolated equilibria. The equilibrium line is not reclassified here. No assertion is made about global attractors, basin geometry, nonlinear dynamics at the nonhyperbolic boundary \(b=a\), or stability of the fractional-order system.

## Proof
The equilibrium equations are
\[
yz=ax,\qquad x(c-az)=0,\qquad xy=bz.
\]
For an isolated equilibrium one has \(x\ne0\), hence \(z=c/a\). Then \(xy=bc/a\), while \(yz=ax\). Eliminating \(y\) gives
\[
x^2=\frac{bc^2}{a^3},
\]
which yields the two points \(E_{\pm}\) displayed above.

The Jacobian is
\[
J(x,y,z)=
\begin{pmatrix}
-a&z&y\\
c-az&0&-ax\\
y&x&-b
\end{pmatrix}.
\]
Substituting either \(E_+\) or \(E_-\) into \(\det(\lambda I-J)\) cancels the sign-dependent radical terms and gives
\[
p(\lambda)=\lambda^3+A\lambda^2+B\lambda+C,
\quad
A=a+b,\quad B=\frac{bc^2}{a^2},\quad C=\frac{2bc^2}{a}.
\]
All three coefficients are positive. The nontrivial cubic Routh determinant is
\[
AB-C
 =\frac{bc^2}{a^2}(b-a).
\]
For \(b>a\), the Routh first column is positive, so all three roots lie in the open left half-plane. For \(0<b<a\), its signs are \(+,+,-,+\), hence exactly two roots lie in the open right half-plane. Since a real polynomial has conjugate nonreal roots, this is a two-dimensional unstable subspace. At \(b=a\), direct multiplication gives the displayed factorization, completing the classification.

## Verification
The bundled checker reconstructs \(\det(\lambda I-J)\) at \((a,b,c)=(5,2,34)\) in exact arithmetic over \(\mathbb Q(\sqrt{10})\), verifies that all radical coefficients cancel, checks the exact cubic coefficients and the negative Routh determinant, and independently approximates the three roots by a dependency-free Durand--Kerner iteration. Its recorded output is `VERIFY_OK`.

## Relationship to prior work
Chen, Lei, Lu, Dai, Qiu, and Zhong introduce the modified flow, list the two isolated equilibria, and report a numerical spectrum at \((5,2,34)\) that includes a zero eigenvalue. Their local calculation that follows is instead for the equilibrium line. The article does not state the characteristic polynomial above or the sharp parameter-global boundary \(b=a\).

The cited precursor of Wang studies a different system whose first equation is \(\dot x=a(y-x)\), not \(\dot x=yz-ax\); its isolated-equilibrium characteristic polynomial and stability theorem therefore do not imply the present classification. A later rebuttal of Wang addresses the claimed Shilnikov connection in that precursor system rather than the local spectrum of the modified flow here. Exact-equation, exact-polynomial, title/DOI, and implication-oriented searches located the source and these related papers but no publication stating the present isolated-equilibrium classification.

## Limitations
The proof is local and linear away from \(b=a\). It does not establish a Hopf bifurcation at \(b=a\), because that would require nonlinear nondegeneracy analysis. It does not validate or invalidate the source's chaotic or periodic trajectories, and it does not transfer the integer-order classification to fractional derivative orders. Literature search cannot establish absolute uniqueness; an unindexed or differently parameterized statement could still exist.

## References
1. H. Chen, T. Lei, S. Lu, W. Dai, L. Qiu, and L. Zhong, “Dynamics and Complexity Analysis of Fractional-Order Chaotic Systems with Line Equilibrium Based on Adomian Decomposition,” *Complexity* 2020, Article 5710765. DOI: 10.1155/2020/5710765. First published 22 October 2020.
2. Z. Wang, “Existence of attractor and control of a 3D differential system,” *Nonlinear Dynamics* 60 (2010), 369–373. DOI: 10.1007/s11071-009-9601-1.
3. A. Algaba, F. Fernández-Sánchez, M. Merino, and A. J. Rodríguez-Luis, “Rebuttal of ‘Existence of attractor and control of a 3D differential system’ by Z. Wang,” *Nonlinear Dynamics* 69 (2012), 2289–2291. DOI: 10.1007/s11071-012-0407-1.
