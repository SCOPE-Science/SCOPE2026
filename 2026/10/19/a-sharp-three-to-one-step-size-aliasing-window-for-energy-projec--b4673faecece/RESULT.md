# A sharp three-to-one step-size aliasing window for energy-projected Taylor oscillators

## Finding

Fix a positive oscillator frequency \(\omega\), a nonzero planar state, and a positive step \(h\). Let \(P_m(\zeta)=\sum_{j=0}^{m}\zeta^j/j!\) be the exponential Taylor polynomial of degree \(m\), and define the normalized step
\[
\mathcal U_m(h)u=\frac{\|u\|_2}{\|P_m(\omega h J)u\|_2}P_m(\omega h J)u,
\qquad J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
For each integer \(1\le m\le5\), this expression is defined for every \(h>0\), preserves the oscillator's quadratic energy exactly, and is a planar rotation. For \(1\le m\le4\), the rotation is injective as a function of the positive step size, even when angles are identified modulo \(2\pi\).

For \(m=5\), write \(z=\omega h\) and let \(\vartheta_5(z)\in(0,\pi)\) be the rotation angle. Let \(x_-\in(6,7)\) and \(x_+\in(15,16)\) be the two positive roots of
\[
F(x)=x^4-16x^3+2880,
\qquad z_- = \sqrt{x_-},\quad z_+=\sqrt{x_+}.
\]
The function \(\vartheta_5\) increases strictly on \((0,z_-)\), decreases strictly on \((z_-,z_+)\), and increases strictly on \((z_+,\infty)\). Its unique maximum is \(\vartheta_{\max}=\vartheta_5(z_-)>\pi/2\); its positive local minimum is \(\vartheta_{\min}=\vartheta_5(z_+)<\pi/2\); and it approaches \(\pi/2\) from below at infinity. **Every rotation angle strictly between \(\vartheta_{\min}\) and \(\pi/2\) is realized by exactly three distinct positive time steps.** Thus degree five is the first Taylor truncation degree exhibiting this three-to-one aliasing after exact energy projection.

The full inverse-multiplicity law for a prescribed angle \(\varphi\in(0,\pi)\) is one step for \(0<\varphi<\vartheta_{\min}\), two for \(\varphi=\vartheta_{\min}\), three for \(\vartheta_{\min}<\varphi<\pi/2\), two for \(\pi/2\le\varphi<\vartheta_{\max}\), one for \(\varphi=\vartheta_{\max}\), and none for larger angles. All counts refer to distinct *finite* positive steps.

## Assumptions and scope

Work in exact real arithmetic with the planar linear oscillator \(u'=\omega Ju\), \(\omega>0\), \(u\ne0\), and \(h>0\). Its invariant is \(E(u)=\|u\|_2^2/2\). The projected method selects the point on the original energy circle nearest to the unprojected predictor \(v=P_m(h\omega J)u\), equivalently the positive radial normalization displayed above. The theorem concerns degrees \(m\in\{1,2,3,4,5\}\) and unrestricted positive steps, not general nonlinear differential equations or noncanonical higher-dimensional oscillators.

For each \(m\in\{2,3,4,5\}\), the predictor is the exact linear-oscillator specialization of the explicit \(m\)-stage Runge–Kutta method
\[
 k_1=f(u),\qquad k_j=f(u+h k_{j-1})\quad (2\le j\le m),
 \qquad v=u+h\sum_{j=1}^{m}b_jk_j,
\]
where \(b_j=1/j!-1/(j+1)!\) for \(1\le j<m\), and \(b_m=1/m!\). These methods have the Taylor stability polynomial on linear scalar test problems but are **not asserted to have classical nonlinear order \(m\)**. On the nonzero planar oscillator, \(k_1\) and \(k_2\) are linearly independent because \(k_2-k_1=-h\omega^2u\) while \(k_1=\omega Ju\). Thus the stage-derivative span is all of \(\mathbb R^2\), and the quasi-orthogonal energy-projection direction equals the radial direction. Degree one is included only as a normalized-Taylor comparison, without claiming full-stage-span quasi-orthogonality.

## Proof

**1. Polynomial and stage identities.** For the stage chain, an induction gives \(k_j=\sum_{r=1}^j h^{r-1}(\omega J)^r u\). For each \(1\le r\le m\), the weights telescope:
\[
\sum_{j=r}^m b_j=\frac1{r!}.
\]
Therefore \(v=P_m(h\omega J)u\). Identify \(\mathbb R^2\) with \(\mathbb C\), under which \(J\) becomes multiplication by \(i\). Let \(P_m(iz)=a_m(z)+ib_m(z)\). Since \(P_m(iz)\ne0\) for the listed degrees and \(z>0\), radial projection is the unit complex multiplier \(P_m(iz)/|P_m(iz)|\), hence a rotation and an exact energy isometry.

**2. Nonvanishing and phase derivatives.** For \(m=1,2\), \(b_m(z)=z>0\). For \(m=3,4\), \(b_m(z)=z(1-z^2/6)\), which vanishes only at \(z=\sqrt6\), where \(a_3=-2\) and \(a_4=-1/2\). For \(m=5\),
\[
 b_5(z)=\frac z{120}\big[(z^2-10)^2+20\big]>0.
\]
Thus \(P_m(iz)\ne0\) for all \(z>0\). Choose the continuous lifted angle \(\vartheta_m(0)=0\). Its derivative obeys
\[
 \vartheta_m'(z)=\frac{a_m(z)b_m'(z)-b_m(z)a_m'(z)}{a_m(z)^2+b_m(z)^2},
\]
and direct exact differentiation yields the following *numerators*, in the order \(m=1,\ldots,5\):
\[
 1,\qquad \frac{z^2+2}{2},\qquad \frac{z^4+12}{12},\qquad
 \frac{z^6-6z^4+144}{144},\qquad
 \frac{z^8-16z^6+2880}{2880}.
\]
The first three are positive. For the fourth put \(x=z^2\); the cubic \(x^3-6x^2+144\) has its minimum on \([0,\infty)\) at \(x=4\), where it equals \(112>0\). Thus \(\vartheta_m\) is strictly increasing for \(m\le4\). From the highest powers of \(P_m(iz)\) its limiting lifted angles are, respectively, \(\pi/2\), \(\pi\), \(3\pi/2\), and \(2\pi\), none attained at finite \(z\). Hence two distinct finite positive step sizes never have the same rotation matrix for these four degrees.

**3. Exactly two turning steps for degree five.** Here
\[
 \vartheta_5'(z)=\frac{F(z^2)}{2880\,|P_5(iz)|^2},\qquad
 F'(x)=4x^2(x-12).
\]
The polynomial \(F\) decreases strictly on \((0,12)\) and increases strictly on \((12,\infty)\), with \(F(0)=2880\), \(F(12)=-4032\), and \(F(x)\to+\infty\). Furthermore \(F(6)>0>F(7)\) and \(F(15)<0<F(16)\), giving exactly two simple positive roots in the advertised intervals and precisely the three derivative-sign intervals.

The real part is \(a_5(z)=(z^4-12z^2+24)/24\), whose squared-step zeros are \(6\pm2\sqrt3\). The first critical squared step belongs to \((6,7)\), where \(a_5<0\), while the second belongs to \((15,16)\), where \(a_5>0\). Since \(b_5>0\), this proves
\[
 0<\vartheta_{\min}<\pi/2<\vartheta_{\max}<\pi.
\]
As \(z\to0^+\), \(\vartheta_5(z)\to0\); as \(z\to\infty\), the leading \(iz^5/120\) term gives \(\vartheta_5(z)\to\pi/2\). Strict monotonicity on the three intervals and the endpoint values give the complete inverse-multiplicity law. Because \(\vartheta_5\in(0,\pi)\), equality of lifted angles and equality of rotation matrices coincide; the triple-aliasing conclusion is not an artifact of angle unwrapping.

**4. Exact conservation in the aliasing region.** The one-step operator is \(P_5(iz)/|P_5(iz)|\), so its modulus equals one for every positive \(z\). Thus its arbitrary positive integer iterates conserve \(E\), even on the interval where phase speed is negative. Three different time steps with the same target angle give exactly the same one-step matrix on *every* nonzero initial state. This establishes phase nonidentifiability despite exact energy conservation.

## Verification

The standalone `verify_phase.py` reconstructs the Runge–Kutta stage-chain stability polynomials, differentiates the phases symbolically, proves numerical interval brackets via exact rational signs, checks the stage-span rank and tests the independently implemented stage-and-projection update. It also computes the two turning steps, finds three distinct steps producing angle exactly one radian to high precision, and checks repeated energy conservation. The completed script passed **754 assertions**. The script's finite numerical checks are diagnostic; the preceding symbolic arguments prove the universally quantified results.

Numerically, the turning steps and phase extrema are
\[
 z_-\approx2.605131303140441,\qquad z_+\approx3.895640529451688,\qquad
 \vartheta_{\max}\approx2.195024091695401,\qquad
 \vartheta_{\min}\approx0.467591743846912.
\]
The target angle of one radian is attained near \(z=1.001048767532676\), \(z=3.243692019976769\), and \(z=8.701834821345539\). These approximate values are illustrations, not the definition of the exact three-to-one window.

## Relationship to prior work

Najafian and Vermeire [1] define quasi-orthogonal Runge–Kutta stage-span projection for invariant preservation. Its energy-preserving framework, not the general projection idea, is the starting point here. For this particular planar oscillator and the explicit stage chains defined above, the projected update is exactly normalized Taylor propagation. The new claim concerns the global injectivity of its step-size-to-rotation map, its sharp minimal polynomial degree, and the complete inverse-multiplicity classification.

Phase-lag and amplification analyses of Runge–Kutta oscillator integrators are classical; see Chen [2] and van der Houwen and Sommeijer [3]. Calvo and collaborators [4] also study dispersion/dissipation in projected Runge–Kutta integrators. None of the *material inspected* established the exact degree-five three-to-one aliasing classification. This absence is not a proof of priority; see the access limitation below.

## Limitations

The theorem is about one planar linear oscillator, exact arithmetic, the explicit stage-chain Taylor stability polynomials, and the positive radial energy projection. It does not assert nonlinear method order \(m\), symplecticity on arbitrary Hamiltonian systems, accuracy of the true elapsed time when the rotation aliases, or robustness under floating-point rounding. A full comparison with the 2015 Calvo–Laburta–Montijano–Rández article was not possible, so an equivalent specialized analysis remains a literature-priority risk. Neither computational tests nor a negative database search proves novelty. Independent scholarly assessment has not been performed.

## References

[1] M. R. Najafian and B. C. Vermeire, *Quasi-Orthogonal Runge-Kutta Projection Methods*, arXiv:2409.18328, first public version September 26, 2024. https://arxiv.org/abs/2409.18328

[2] J. Chen, *A New Family of Phase-Fitted and Amplification-Fitted Runge-Kutta Type Methods for Oscillators*, Mathematical Problems in Engineering (2012), article 236281. https://doi.org/10.1155/2012/236281

[3] P. J. van der Houwen and B. P. Sommeijer, *Explicit Runge–Kutta (–Nyström) Methods with Reduced Phase Errors for Computing Oscillating Solutions*, SIAM Journal on Numerical Analysis (1987). https://doi.org/10.1137/0724041

[4] M. Calvo, M. P. Laburta, J. I. Montijano, and L. Rández, *Runge–Kutta projection methods with low dispersion and dissipation errors*, Advances in Computational Mathematics 41 (2015), 231–251. https://doi.org/10.1007/s10444-014-9355-2
