# Correct harmonic-response amplitude for a periodically harvested Allee population model

## Finding
For the subcritical survival regime of the dimensionless model
\[\frac{dn}{dt}=n(1-n)(\sigma n-1)-\alpha\bigl(1+\varepsilon\gamma(t)\bigr)n,\]
write \(n(t)=n_0(t)+\varepsilon n_1(t)+O(\varepsilon^2)\). Define
\[\psi=\frac{\sigma+1}{2\sigma},\qquad \delta=\sigma\psi^2-(1+\alpha)>0,\]
and the stable positive equilibrium and its relaxation rate by
\[c_3=\frac{\sigma\psi+\sqrt{\sigma\delta}}{\sigma},\qquad \phi=2c_3\sqrt{\sigma\delta}.\]
For sinusoidal harvesting \(\gamma(t)=\sin(\omega t)\) with \(\omega>0\), the bounded large-time first-order correction is
\[n_{1,\infty}(t)=\frac{\alpha c_3}{\phi^2+\omega^2}\bigl(\omega\cos(\omega t)-\phi\sin(\omega t)\bigr).\]
Hence the harmonic amplitude is
\[\frac{\alpha c_3}{\sqrt{\phi^2+\omega^2}}.\]
For \(\omega=1\), Alharbi's Eq. (6.1) contains the factor \((\phi^2+1)^{-1}\), but the stated large-time limit and Eq. (6.4) omit it. The corrected Eq. (6.4) therefore requires this divisor in the oscillatory first-order term.

## Assumptions and scope
The claim concerns the perturbative regime \(0<\varepsilon\ll1\), subcritical harvesting \(\delta>0\), and the surviving basin in which \(n_0(t)\to c_3\). It concerns the first-order long-time response, not the full finite-\(\varepsilon\) nonlinear solution, the extinction branch, or the supercritical branch. The forcing frequency \(\omega\) is fixed and positive.

## Proof
The source's first-order equation can be written as
\[n_1'(t)-f'(n_0(t))n_1(t)=-\alpha\gamma(t)n_0(t),\]
where \(f(n)=n\bigl(\delta-\sigma(n-\psi)^2\bigr)\). On the survival branch, \(n_0(t)\to c_3\). Since \(c_3-\psi=\sqrt{\sigma\delta}/\sigma\), differentiation gives
\[-f'(c_3)=2\sigma c_3(c_3-\psi)=2c_3\sqrt{\sigma\delta}=\phi.\]
Therefore the limiting first-order equation is
\[n_1'(t)+\phi n_1(t)=-\alpha c_3\sin(\omega t).\]
Seek its bounded periodic solution as \(n_1(t)=A\cos(\omega t)+B\sin(\omega t)\). Matching cosine and sine coefficients gives
\[\omega B+\phi A=0,\qquad -\omega A+\phi B=-\alpha c_3.\]
Solving,
\[A=\frac{\alpha c_3\omega}{\phi^2+\omega^2},\qquad B=-\frac{\alpha c_3\phi}{\phi^2+\omega^2},\]
which proves the stated formula and amplitude.

At \(\omega=1\), this specializes to
\[n_{1,\infty}(t)=\frac{\alpha c_3}{\phi^2+1}\bigl(\cos t-\phi\sin t\bigr).\]
The source's Eq. (6.1) visibly contains \((\phi^2+1)^{-1}\) in the non-decaying harmonic contribution, while its following large-time line and Eq. (6.4) drop that divisor. The limiting differential equation independently fixes the denominator, so the omission cannot be reconciled by a phase or normalization convention.

For the source's example parameters \(\sigma=5\) and \(\alpha=0.3\),
\[\psi=0.6,\qquad \delta=0.5,\qquad c_3\approx0.9162277660,\qquad \phi\approx2.8973665961.\]
Thus
\[\phi^2+1\approx9.3947331922.\]
The printed Eq. (6.4) therefore makes the first-order harmonic amplitude about \(9.394733\) times the corrected amplitude for those parameters.

## Verification
The accompanying `verify.py` recomputes \(\psi,\delta,c_3,\phi\), checks the identity \(-f'(c_3)=\phi\), substitutes the harmonic coefficients back into the limiting differential equation, and evaluates the source-parameter factor. It uses decimal arithmetic and tests several admissible parameter choices. A successful replay ends with `VERIFY_OK`.

The correction is also an internal consistency check on the source: its Eq. (6.1) retains the denominator, whereas the subsequent limit and Eq. (6.4) do not. The paper states that Figure 5 was generated from Eq. (6.4), so the normalization matters for the reported equilibrium-variation curves rather than being only a typographical rearrangement.

## Relationship to prior work
Alharbi (2024) develops the Allee-effect population model, derives the perturbation equations, gives the stable branch \(c_3\), and prints both Eq. (6.1) and Eq. (6.4). The corrected denominator follows from those equations but is not stated as a correction in the article. Searches by exact title, DOI, the displayed harmonic factors, and correction/erratum terminology located the article but no published correction stating this missing factor.

Idlango, Shepherd, and Gear (2017) study slowly varying Holling type II harvesting in a different logistic model. Its published scope does not contain this Alharbi equation or the denominator comparison above. The general \(\omega>0\) response here is a direct extension of the first-order limiting equation and makes the low-pass frequency dependence explicit.

## Limitations
This is a first-order perturbative correction. It does not establish a uniform error bound in \(\varepsilon\), does not recompute every figure from raw plotting code, and does not alter the source's leading-order equilibrium. The literature search cannot prove that no equivalent observation exists in private correspondence or an unindexed note. The numerical factor quoted above applies specifically to the source's \(\sigma=5\), \(\alpha=0.3\) example.

## References
1. F. M. Alharbi, “Harvesting a population model with Allee effect in a periodically varying environment,” AIMS Mathematics 9 (2024), 8834–8847. DOI: 10.3934/math.2024430.
2. M. A. Idlango, J. J. Shepherd, J. A. Gear, “Logistic growth with a slowly varying Holling type II harvesting term,” Communications in Nonlinear Science and Numerical Simulation 49 (2017), 81–92. DOI: 10.1016/j.cnsns.2017.02.005.
