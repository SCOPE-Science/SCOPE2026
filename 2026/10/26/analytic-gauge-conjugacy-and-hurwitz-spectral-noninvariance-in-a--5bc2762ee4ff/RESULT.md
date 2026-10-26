# Analytic gauge conjugacy and Hurwitz-spectral noninvariance in a polynomial oscillator family

## Finding
For the polynomial fields \(F_{\mu,e}\) of Castañeda and Rebollo-Perdomo [1], all real values of \(e\), at a fixed \(\mu>0\), define globally real-analytically and time-preservingly conjugate flows. Nevertheless the original globally Hurwitz member \((\mu,e)=(1/1000,1/10)\) is analytically conjugate to a member with strictly positive \(e=1/100\) whose Jacobian is not Hurwitz at \((3/2,0,0)\). Thus the angular parameter is a dynamical gauge, but not a gauge of the pointwise Jacobian stability test.

## Assumptions and scope
Use real coordinates \((x,y,z)\), parameters \(\mu>0\), \(e\in\mathbb R\), \(R=x^2+y^2\), and
\[
 A_\mu(R,z)=\mu\left((R-5)\left(\frac{20}{21}-R\right)-\frac{400z^2}{21}\right),\qquad B(R,z)=z+\frac{R}{10}.
\]
The polynomial vector field is
\[
 \dot x=A_\mu(R,z)x-(1+eB(R,z))y,\quad
 \dot y=A_\mu(R,z)y+(1+eB(R,z))x,\quad
 \dot z=-B(R,z).
\]
This agrees with [1, Eq. (1)] for its stated positive parameters; the same polynomial formulas also make sense for real \(e\). "Hurwitz" means that every eigenvalue of the spatial Jacobian of the vector field has strictly negative real part, at every point of \(\mathbb R^3\). The conjugacy holds on the maximal common solution intervals, and all these systems are forward complete.

## Proof
**A global analytic conjugacy.** Identify \(u=x+iy\in\mathbb C\). The equations become
\[
 \dot u=\left(A_\mu(R,z)+i(1+eB(R,z))\right)u,\qquad
 \dot z=-B(R,z),\quad R=|u|^2.
\]
For \(e\in\mathbb R\), set \(H_e(u,z)=(e^{iez}u,z)\). This is a globally defined real-analytic diffeomorphism of \(\mathbb R^3\), with inverse \(H_{-e}\), including at \(u=0\). Since \(\frac d{dt}(e^{iez}u)=e^{iez}(\dot u+ie\dot zu)\), one obtains exactly
\[
 \frac d{dt}(e^{iez}u)=(A_\mu(R,z)+i)e^{iez}u,\qquad \dot z=-B(R,z).
\]
Thus \(DH_e\,F_{\mu,e}=F_{\mu,0}\circ H_e\), and consequently \(H_{e-e'}\) takes the \(e\)-flow to the \(e'\)-flow with *unchanged time*, because \(H_{e'}^{-1}\circ H_e=H_{e-e'}\). No polar-coordinate singularity is used. The estimate \(\dot R=2A_\mu(R,z)R<0\) whenever \(R\ge9\), along with \(\dot z=-z-R/10\), bounds forward orbits and proves forward completeness by standard ODE continuation.

**A strict spectral witness.** Set \(\mu=1/1000\) and \(e'=1/100\). At \(q=(3/2,0,0)\), direct differentiation gives the exact Jacobian
\[
 J=\begin{pmatrix}
 97/9600&-4009/4000&0\\
 4027/4000&1199/336000&3/200\\
 -3/10&0&-1
 \end{pmatrix}.
\]
Its characteristic polynomial \(\det(\lambda I-J)=\lambda^3+a_1\lambda^2+a_2\lambda+a_3\) has
\[
 a_1=\frac{165703}{168000},\quad
 a_2=\frac{16053466459}{16128000000},\quad
 a_3=\frac{16201239163}{16128000000}.
\]
All three coefficients are positive, but
\[
 a_1a_2-a_3=-\frac{61700626728323}{2709504000000000}<0.
\]
The strict Routh-Hurwitz cubic criterion therefore rules out a Hurwitz Jacobian (indeed two eigenvalues have positive real part). In contrast, [1, Theorem 1 and Lemma 3] proves that at \((\mu,e)=(1/1000,1/10)\) its Jacobian is Hurwitz at every real point. The explicit diffeomorphism \(H_{9/100}\) conjugates these two vector fields. Hence analytic flow conjugacy does not preserve the global pointwise Hurwitz property, even inside this positive-parameter polynomial family. The global Hurwitz assertion for the first member is invoked from the cited published theorem, not re-certified here.

## Verification
Run `python3 verify.py` using Python's standard library. It derives the rational witness coefficients and determinant directly from the displayed exact Jacobian and checks the complex differential conjugacy identity on deterministic test vectors. The conjugacy proof itself is algebraic and applies to all coordinates and parameters, not only to the numerical test vectors.

## Relationship to prior work
Castañeda and Rebollo-Perdomo [1] construct the two-parameter Hurwitz polynomial family, prove two isolated periodic orbits, and display its cylindrical reduction with \(\dot\theta=1+eB\) and \(\dot z=-B\). Their full text does not formulate or prove the global analytic conjugacy among distinct \(e\)'s, nor the pair of strictly positive, conjugate parameters with different pointwise Hurwitz behavior. The present result uses [1]'s field and its established global Hurwitz certificate; it does not claim authorship of their construction. The exact gauge removal, the conjugacy-class interpretation, and the rational non-Hurwitz witness are the added conclusions.

## Limitations
The proof does not rederive [1]'s large global discriminant certificate establishing the Hurwitz property at \(e=1/10\); that established theorem is an explicitly identified premise. It does not claim that Hurwitzness is always noninvariant under every analytic conjugacy, nor that a global dynamical bifurcation occurs when \(e\) varies. The spectral witness is at one point, sufficient to prove global Hurwitz failure there. No independent scientific audit has been performed.

## References
[1] A. Castañeda and S. Rebollo-Perdomo, *A family of Hurwitz polynomial vector fields in \(\mathbb R^3\) having non-constant periodic orbits*, arXiv:2610.09176v1, first posted 2026-10-06. https://arxiv.org/html/2610.09176v1
