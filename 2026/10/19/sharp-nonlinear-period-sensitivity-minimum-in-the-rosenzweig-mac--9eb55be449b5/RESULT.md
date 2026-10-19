# Sharp nonlinear period-sensitivity minimum in the Rosenzweig–MacArthur oscillator

## Finding
For the physical-time Holling type-II Rosenzweig–MacArthur predator–prey dynamics
\[
\dot x=x(1-x)-\frac{xy}{h+x},\qquad
\dot y=y\left(\frac{x}{h+x}-d\right),
\]
fix any \(0<h<1\) and approach the Hopf curve \(d_H=(1-h)/(1+h)\) from \(d<d_H\). There is a locally unique orbitally stable small periodic orbit. Let \(T\) be its least period, \(r\) its first prey Fourier-harmonic amplitude, and \(\omega_{\mathrm{lin}}\) the positive imaginary part of the coexistence equilibrium's linearization eigenvalues at the *same* value of \(d\). Then
\[
\frac{T\omega_{\mathrm{lin}}}{2\pi}-1=C(h)r^2+o(r^2),
\qquad C(h)=\frac{1+5h-4h^3+7h^4-h^5}{6h(1-h)^2(1+h)^3}.
\]
The coefficient is positive and diverges at both endpoints of \((0,1)\). Its unique sharp global minimum equals \(1.223281644705308\ldots\), attained at \(h_*=0.372462737190824\ldots\), the unique root in \((0,1)\) of
\[
P(h)=h^7-15h^6+23h^5-25h^4-17h^3-h^2+h+1.
\]
The result describes period sensitivity in actual model time; it is not a claim of global period monotonicity.

## Assumptions and scope
The parameters satisfy \(0<h<1\) and positive \(d\) sufficiently close to \(d_H\) from below (the neighborhood can depend on \(h\)). The coexistence equilibrium is
\[
(x_*(d),y_*(d))=\left(\frac{hd}{1-d},\left(1-\frac{hd}{1-d}\right)\left(h+\frac{hd}{1-d}\right)\right).
\]
Its Jacobian is \(J(d,h)\). Define
\[
\omega_{\mathrm{lin}}(d,h)=\sqrt{\det J(d,h)-\frac14(\operatorname{tr}J(d,h))^2},
\]
positive near the Hopf curve. Writing the orbit's prey component with physical-time phase \(\theta=2\pi t/T\), define its first harmonic by
\[
a_1=\frac2T\int_0^T x(t)\cos(2\pi t/T)\,dt,\qquad
b_1=\frac2T\int_0^T x(t)\sin(2\pi t/T)\,dt,
\qquad r=\sqrt{a_1^2+b_1^2}.
\]
The definition of \(r\) is phase-invariant and uses no parameter-dependent amplitude normalization. All limiting assertions in \(d\) hold for each fixed \(h\), not uniformly up to \(h=0\) or \(h=1\).

## Proof
At the Hopf value,
\[
(x_H,y_H)=\left(\frac{1-h}{2},\frac{(1+h)^2}{4}\right),\quad
A=J(d_H,h)=\begin{pmatrix}0&-d_H\\h&0\end{pmatrix},\quad
\omega=\sqrt{hd_H}>0.
\]
The derivative of \(\operatorname{tr}J\) along the coexistence equilibrium, with respect to \(d\) at \(d_H\), is \(-(1-h)(1+h)/(2h)\), hence nonzero. The first eigenpair and normalized complex left eigenfunctional can be chosen as
\[
q=\begin{pmatrix}1\\-i\omega/d_H\end{pmatrix},\qquad
\ell=\begin{pmatrix}1/2&i d_H/(2\omega)\end{pmatrix},
\qquad Aq=i\omega q,\quad\ell q=1,\quad\ell\overline q=0.
\]
Let \(B\) and \(D_3\) denote the second and third multilinear derivatives of the vector field at the Hopf equilibrium (without factorial factors). Their potentially nonzero entries are, in vector-field component order,
\[
\begin{aligned}
&f_{xx}=-2d_H, &&f_{xy}=-\frac{4h}{(1+h)^2},
&&g_{xx}=-\frac{4h}{1+h}, &&g_{xy}=\frac{4h}{(1+h)^2},\\
&f_{xxx}=-\frac{24h}{(1+h)^2},&&f_{xxy}=\frac{16h}{(1+h)^3},
&&g_{xxx}=\frac{24h}{(1+h)^2},&&g_{xxy}=-\frac{16h}{(1+h)^3}.
\end{aligned}
\]
The standard cubic Hopf resonance computation, with the original time coordinate unchanged, yields
\[
G_{21}=\ell\Big(D_3(q,q,\overline q)
+B\big(\overline q,(2i\omega I-A)^{-1}B(q,q)\big)
-2B\big(q,A^{-1}B(q,\overline q)\big)\Big)
= -\frac4{1+h}-8i\omega C(h).
\]
The displayed equality is an exact rational identity after imposing \(\omega^2=hd_H\); the included symbolic checker reconstructs the derivatives, inverses, and identity rather than relying on printed constants. Since \(\operatorname{Re}G_{21}<0\) and the Hopf crossing is transverse, the Hopf bifurcation is supercritical, and the small cycle exists and is orbitally asymptotically stable for \(d<d_H\) sufficiently close.

In the eigenvector amplitude coordinate \(z\), the physical angular speed is
\[
\omega_{\mathrm{lin}}+\tfrac12\operatorname{Im}G_{21}|z|^2+o(|z|^2).
\]
The prey component of \(zq+\overline z\,\overline q\) has first harmonic \(r=2|z|+o(|z|)\), because the prey entry of \(q\) is one. Thus the period correction is \(-\operatorname{Im}G_{21}r^2/(8\omega)+o(r^2)=C(h)r^2+o(r^2)\). Replacing the Hopf frequency by \(\omega_{\mathrm{lin}}(d,h)\) removes the unfolding's linear frequency shift; the omitted mixed parameter-amplitude effects are \(o(r^2)\) on this Hopf branch.

The coefficient is positive: its numerator is \((1+h)+4h(1-h^2)+h^4(7-h)>0\) for \(0<h<1\). Its endpoint behavior is \(C(h)\sim1/(6h)\) as \(h\downarrow0\) and \(C(h)\sim1/(6(1-h)^2)\) as \(h\uparrow1\). Exact differentiation gives
\[
C'(h)=\frac{P(h)}{6h^2(h-1)^3(h+1)^4}.
\]
With \(h=u/(1+u)\), \(u>0\),
\[
(1+u)^7P\left(\frac{u}{1+u}\right)
=1+8u+26u^2+28u^3-48u^4-128u^5-104u^6-32u^7.
\]
There is precisely one change of coefficient sign, so Descartes' rule of signs gives at most one positive root. Since \(P(0)=1\) and \(P(1)=-32\), the intermediate value theorem provides one root in \((0,1)\). The denominator of \(C'\) is strictly negative on this interval, so the derivative changes from negative to positive exactly once. Endpoint divergence makes this root the unique global minimum; numerical root evaluation gives the values stated.

## Verification
Run `python CHECK.py` with SymPy. The file checks the vector field's Hopf equilibrium and parameter transversality, every derivative entering the cubic resonance formula, real and imaginary parts of \(G_{21}\), the coefficient identity, the polynomial derivative, and Descartes' transformed polynomial. Run `python NUMERIC_CHECK.py` with NumPy and SciPy for four finite-distance shooting and Fourier-harmonic corroborations; their relative deviations (approximately 0.15%, 0.44%, 2.12%, 1.33%) are finite-distance effects, not a proof of the limiting formula. The analytic conclusion follows from the resonance calculation, Hopf theorem, and polynomial sign analysis, not from simulations.

## Relationship to prior work
Rosenzweig and MacArthur's 1963 study introduced the predator–prey interaction and stated a period equation in its abstract; the complete original article was not available for comparison. Diz-Pita, Llibre, and Otero-Espinar's openly available analysis proves a supercritical Hopf bifurcation and describes global phase portraits for a polynomial system obtained by a state-dependent time rescaling; its Section 6.1 supplies a real first Lyapunov coefficient but no physical-time first-harmonic period sensitivity or sharp minimum. Time reparametrization does not preserve the physical period. Liou and Cheng's 1988 article studies limit-cycle uniqueness, a logically distinct property. General Hopf normal-form theory supplies the method but not this coefficient or its unique model-specific optimum.

## Limitations
This is an exact *local* amplitude expansion for each fixed \(h\). No global-in-amplitude monotonicity or conclusions for other functional responses follow. No independent scientific audit has been performed. The original 1963 article could not be read in full, and earlier priority for a matching physical-time second-order period expansion cannot be ruled out solely from available sources. Comparisons with other published oscillator formulas do not establish universal uniqueness across systems.

## References
1. M. L. Rosenzweig and R. H. MacArthur, “Graphical Representation and Stability Conditions of Predator-Prey Interactions,” *The American Naturalist* **97** (1963), 209–223, https://doi.org/10.1086/282272.
2. É. Diz-Pita, J. Llibre, and M. V. Otero-Espinar, “Global phase portraits of a predator-prey system,” arXiv:2501.13728 (2025), https://arxiv.org/abs/2501.13728. See especially the introduction and Section 6.1, using a time-rescaled polynomial vector field.
3. L. P. Liou and K. S. Cheng, “On the uniqueness of a limit cycle for a predator-prey system,” *SIAM Journal on Mathematical Analysis* **19** (1988), 867–878.
