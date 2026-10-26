# Unique nontrivial redshift-drift zero for standard FLRW mixtures

## Finding

Let \(y=1+z\geq 1\) and \(E(y)=H(z)/H_0>0\) on the expanding branch of an FLRW universe. Consider a finite mixture of non-interacting fluids with constant equations of state \(p_i=w_i\rho_i\), present density fractions \(\Omega_i\geq0\), and curvature fraction \(\Omega_k\), normalized by \(\Omega_k+\sum_i\Omega_i=1\). Write \(q_i=1+3w_i\), so that

\[
E(y)^2=\Omega_k y^2+\sum_i\Omega_i y^{q_i+2}.
\]

Assume at least one component with \(q_i\geq1\) has positive density and every nonzero-density fluid has either \(q_i<0\) or \(q_i\geq1\). A component with \(q_i=0\) scales like curvature and can be absorbed into \(\Omega_k\). Define the present deceleration parameter

\[
q_0=-\frac{\ddot a_0}{a_0H_0^2}=\frac12\sum_i\Omega_iq_i.
\]

Then the redshift drift \(\dot z=H_0(y-E(y))\) has exactly one nontrivial zero at \(z>0\) if and only if \(q_0<0\). In that case it is positive for \(0<z<z_*\) and negative for \(z>z_*\). If \(q_0\geq0\), it is strictly negative for every \(z>0\), so no nontrivial zero exists. The curvature term cancels from the equation determining \(z_*\).

Equivalently, for \(y>1\), define

\[
\phi_q(y)=\frac{y^q-1}{y-1},\qquad F(y)=\sum_i\Omega_i\phi_{q_i}(y).
\]

The nontrivial zero is exactly the unique solution of \(F(y)=0\) when \(q_0<0\).

## Assumptions and scope

The result is for exact FLRW kinematics on an expanding branch, with finite, non-interacting, constant-\(w_i\) fluids, nonnegative present density fractions, arbitrary curvature consistent with the normalization, and positive total density in at least one component with \(w_i\geq0\). The permitted exponents are \(q_i<0\) (equivalently \(w_i<-1/3\)) or \(q_i\geq1\) (equivalently \(w_i\geq0\)). This covers ordinary dust/radiation together with accelerated dark-energy-like components, including a cosmological constant. It excludes fluids with \(-1/3<w_i<0\), interacting components, time-varying equations of state, negative density fractions, and inhomogeneous cosmologies. The claim concerns the number and sign pattern of zeros, not observational parameter estimation.

## Proof

For \(y>1\), divide the Friedmann equation by \(y^2\) and use \(\Omega_k+\sum_i\Omega_i=1\):

\[
\frac{E(y)^2}{y^2}-1=\sum_i\Omega_i(y^{q_i}-1)=(y-1)F(y).
\]

Consequently,

\[
\dot z=H_0(y-E(y))=-\frac{H_0y^2(y-1)}{y+E(y)}F(y),
\]

so the sign of the drift is the opposite of the sign of \(F\), and its positive-redshift zeros are exactly the zeros of \(F\). Since \(\lim_{y\downarrow1}\phi_q(y)=q\),

\[
F(1+)=\sum_i\Omega_iq_i=2q_0.
\]

For \(q\neq0,1\), direct differentiation gives

\[
\phi_q'(y)=\frac{1-y^{q-1}((1-q)y+q)}{(y-1)^2}.
\]

Put \(g_q(y)=y^{q-1}((1-q)y+q)\). Then \(g_q(1)=1\) and \(g_q'(y)=q(1-q)y^{q-2}(y-1)\). If \(q<0\) or \(q>1\), then \(q(1-q)<0\), hence \(g_q(y)<1\) for every \(y>1\) and \(\phi_q'(y)>0\). For \(q=1\), \(\phi_1(y)=1\); for \(q=0\), \(\phi_0(y)=0\). Therefore \(F\) is nondecreasing and is strictly increasing whenever a positive-density component has \(q_i<0\) or \(q_i>1\).

If \(q_0<0\), then \(F(1+)<0\), which forces at least one positive-density component with \(q_i<0\); hence \(F\) is strictly increasing. As \(y\to\infty\), each \(q_i<0\) term tends to zero from below, each \(q_i=1\) term tends to its positive weight, and each \(q_i>1\) term tends to positive infinity. The assumed positive density in the \(q_i\geq1\) group therefore implies \(F(y)>0\) for all sufficiently large \(y\). Continuity and strict monotonicity give exactly one root \(y_*>1\). The drift sign formula gives the asserted positive-then-negative pattern.

If \(q_0\geq0\), then \(F(1+)\geq0\). When a component with \(q_i<0\) or \(q_i>1\) is present, strict increase gives \(F(y)>0\) for all \(y>1\). Otherwise every positive-density component has \(q_i=1\), so \(F(y)=\sum_{q_i=1}\Omega_i>0\) by assumption. In either case there is no positive-redshift zero and \(\dot z<0\) for every \(z>0\). Curvature cancels because its term is constant in \(E(y)^2/y^2\) and is removed by the present-day normalization.

## Verification

The derivative identity for \(\phi_q\) was checked algebraically, including the boundary cases \(q=0\) and \(q=1\). As a numerical sanity check, for flat \(\Lambda\)CDM with \(\Omega_m=0.3\) and \(\Omega_\Lambda=0.7\), the root equation is \(F(y)=0.3-0.7(y+1)/y^2=0\); bisection gives \(z_*=2.088760432445\), consistent with the published rounded value \(z\approx2.09\). At the acceleration boundary \(\Omega_m=2/3\), \(\Omega_\Lambda=1/3\), one has \(F(1+)=0\) and \(F(y)>0\) for every \(y>1\), so there is no positive-redshift zero. These numerical checks are illustrations; the proof above is analytic.

## Relationship to prior work

Sandage introduced the cosmological redshift-drift observable in 1962, and Loeb later wrote its matter–vacuum form explicitly. Alves and coauthors give the general zero-drift equation for the CPL parameterization and an explicit flat-\(\Lambda\)CDM root, while Lobo and coauthors study FLRW redshift drift for a finite admixture of constant-equation-of-state components and discuss the typical nontrivial root and its low-redshift behavior. The inspected formulations establish the drift law and the root equation, but the inspected sections do not state the exact uniqueness-if-and-only-if-\(q_0<0\) classification proved here for the separated exponent class \(q_i<0\) or \(q_i\geq1\). This finding does not claim novelty for the observable, Friedmann law, or the component model; the contribution is the monotonicity and exact zero-count criterion. A residual risk remains that an uninspected portion of the later general-model literature states an equivalent root-count theorem.

## Limitations

The restriction excluding \(-1/3<w_i<0\) is essential to this monotonicity proof: for \(0<q_i<1\), the divided-power function \(\phi_{q_i}\) is decreasing, so the argument does not apply. No root-count claim is made for that broader class, for interacting or time-varying fluids, or for inhomogeneous space-times. The theorem is a structural statement about the specified FLRW class, not a claim about the actual composition of the universe or the detectability of a measured zero.

## References

1. A. Sandage, “The Change of Redshift and Apparent Luminosity of Galaxies due to the Deceleration of Selected Expanding Universes,” *The Astrophysical Journal* 136 (1962), 319–333. DOI: 10.1086/147385.
2. A. Loeb, “Direct Measurement of Cosmological Parameters from the Cosmic Deceleration of Extragalactic Objects,” *The Astrophysical Journal Letters* 499 (1998), L111–L114. arXiv: astro-ph/9802122; DOI: 10.1086/311375.
3. C. S. Alves, A. C. O. Leite, C. J. A. P. Martins, J. G. B. Matos, and T. A. Silva, “Forecasts of redshift drift constraints on cosmological parameters,” *Monthly Notices of the Royal Astronomical Society* 488 (2019), 3607–3624. arXiv: 1907.05151; DOI: 10.1093/mnras/stz1934.
4. F. S. N. Lobo, J. P. Mimoso, J. Santiago, and M. Visser, “Dynamical analysis of the redshift drift in FLRW universes,” arXiv: 2210.13946 (first submitted 2022-10-25); *Universe* 10 (2024), 162. DOI: 10.3390/universe10040162.
