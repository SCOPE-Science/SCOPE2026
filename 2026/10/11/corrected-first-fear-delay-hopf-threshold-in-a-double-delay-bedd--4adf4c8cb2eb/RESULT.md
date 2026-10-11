# Corrected first fear-delay Hopf threshold in a double-delay Beddington–DeAngelis model
## Finding
For the deterministic predator–prey delay system
\[
\dot x(t)=\frac{kx(t)}{1+f y(t-\tau_1)}-\alpha x(t)^2-\frac{p x(t)y(t)}{a x(t)+b y(t)+c},
\]
\[
\dot y(t)=\frac{\mu p x(t-\tau_2)y(t-\tau_2)}{a x(t-\tau_2)+b y(t-\tau_2)+c}-d y(t)-h y(t)^2,
\]
use the Section 5 parameters
\[
f=1.5,\ p=4,\ a=4.8,\ b=5,\ c=2.1,\ \mu=1.2,\ d=0.1,\ h=0.01,\ k=0.9,\ \alpha=0.6.
\]
On the Case II slice \(\tau_2=0\), the positive equilibrium is
\[
E_*=(0.12190814516912455\ldots,\ 0.57015890856106163\ldots).
\]
The first imaginary-axis crossing of its characteristic equation occurs at
\[
\boxed{\tau_{1,*}=4.87168883017987792\ldots},
\qquad
\omega_*=0.18402882564735636\ldots,
\]
not at the published numerical value \(4.5923\). The crossing is transversal toward instability. Consequently the coexistence equilibrium is linearly asymptotically stable for \(0\le \tau_1<\tau_{1,*}\) and first loses linear stability at \(\tau_{1,*}\).

Repeating the calculation with the paper's rounded equilibrium \((0.1219,0.5702)\) gives \(4.874589989058015\ldots\), so equilibrium rounding does not explain the discrepancy. The paper's simulations at \(\tau_1=3.5\) and \(\tau_1=5\) still lie on the correct stable and unstable sides, respectively.

## Assumptions and scope
All model parameters are the positive numerical values displayed above, and only the one-delay slice \(\tau_2=0\) is considered. Stability means local linear asymptotic stability of the positive equilibrium for the retarded functional differential equation. No assertion is made about nonlinear Hopf criticality, global attractivity, the existence or stability of a bifurcating periodic branch, or the source's two-delay Case IV boundary.

## Proof
Write \(D_*=a x_*+b y_*+c\). At \(\tau_2=0\), differentiating the printed vector field at the positive equilibrium gives
\[
A_{11}=\frac{k}{1+fy_*}-2\alpha x_*-\frac{p y_*(b y_*+c)}{D_*^2},
\quad
A_{12}=-\frac{p x_*(a x_*+c)}{D_*^2},
\]
\[
B_{12}=-\frac{k f x_*}{(1+fy_*)^2},
\quad
A_{22}=-d-2hy_*,
\]
\[
C_{21}=\frac{\mu p y_*(b y_*+c)}{D_*^2},
\qquad
C_{22}=\frac{\mu p x_*(a x_*+c)}{D_*^2}.
\]
Numerically,
\[
A_{11}=-0.02959921704027105\ldots,
\quad A_{12}=-0.04272458459092166\ldots,
\]
\[
B_{12}=-0.04781531925074255\ldots,
\quad A_{22}=-0.11140317817122123\ldots,
\]
\[
C_{21}=0.44210677105029230\ldots,
\quad C_{22}=0.05126950150910599\ldots.
\]
The characteristic determinant is therefore
\[
\Delta(\lambda,\tau_1)
=(\lambda-A_{11})(\lambda-A_{22}-C_{22})-C_{21}A_{12}-C_{21}B_{12}e^{-\lambda\tau_1}
\]
\[
=\lambda^2+P\lambda+Q+R e^{-\lambda\tau_1},
\]
where
\[
P=0.08973289370238628\ldots,
\quad Q=0.02066873788490888\ldots,
\quad R=0.02113947640068467\ldots.
\]
Putting \(\lambda=i\omega\) and eliminating the phase yields, with \(z=\omega^2\),
\[
z^2+(P^2-2Q)z+(Q^2-R^2)=0.
\]
Its roots are
\[
z_+=0.03386660866914509\ldots,
\qquad
z_-=-0.000581125111531085\ldots.
\]
Hence there is exactly one positive crossing frequency,
\[
\omega_*=\sqrt{z_+}=0.18402882564735636\ldots.
\]
At a crossing,
\[
\cos(\omega\tau_1)=\frac{\omega^2-Q}{R},
\qquad
\sin(\omega\tau_1)=\frac{P\omega}{R}.
\]
The principal phase is \(0.89653117433734639\ldots\), and thus
\[
\tau_{1,*}=\frac{0.89653117433734639\ldots}{0.18402882564735636\ldots}
=4.87168883017987792\ldots.
\]
All later imaginary-axis crossings add \(2\pi/\omega_*\) to the delay. Implicit differentiation gives
\[
\frac{d\lambda}{d\tau_1}
=\frac{R\lambda e^{-\lambda\tau_1}}{2\lambda+P-R\tau_1e^{-\lambda\tau_1}},
\]
and at the first crossing
\[
\operatorname{Re}\!\left(\frac{d\lambda}{d\tau_1}\right)
=0.005780976092865250\ldots>0.
\]
At zero delay the characteristic polynomial is \(\lambda^2+P\lambda+Q+R\), which is Hurwitz because \(P>0\) and \(Q+R>0\). Also \(\Delta(0,\tau_1)=Q+R>0\) for every delay, so no zero eigenvalue occurs. Since the imaginary-frequency equation has only the one positive frequency, the value above is the first possible spectral boundary and the positive transversality establishes loss of linear stability there.

## Verification
Run `python verify.py`. The script resolves the equilibrium at high precision, reconstructs the derivatives directly from the printed equations, checks the frequency polynomial and phase condition, evaluates the characteristic residual at the corrected crossing, checks positive transversality, and independently repeats the calculation at the paper's rounded equilibrium. A successful run begins with `VERIFY_OK`.

## Relationship to prior work
Cui, Shao, Xue and Zhao introduce this exact double-delay Beddington–DeAngelis predator–prey model and, in their Section 5 Case II with \(\tau_2=0\), report a critical fear delay \(\tau_1^*=4.5923\). The same section uses \(\tau_1=3.5\) for a stable numerical trajectory and \(\tau_1=5\) for an unstable one. Those simulations remain compatible with the corrected threshold because \(3.5<4.87168883017987792\ldots<5\).

Targeted exact-title, DOI, author, model-alias, reported-value, corrected-value, and characteristic-equation searches did not locate a published correction of this Case II number. Closely related delay-bifurcation work with Beddington–DeAngelis response studies different state dimensions or delay architectures and does not imply this source-specific recomputation.

## Limitations
The result corrects one local spectral number for one numerical parameter set. It does not establish a nonlinear Hopf theorem or classify periodic solutions. It does not recompute the source's other delay cases. Literature searches cannot prove global absence of an unindexed equivalent correction. The source's coarse stable/unstable simulations at \(3.5\) and \(5\) are not invalidated.

## References
1. M. Cui, Y. Shao, R. Xue, J. Zhao, *Dynamic Behavior of a Predator–Prey Model with Double Delays and Beddington–DeAngelis Functional Response*, Axioms 12 (2023), 73, DOI 10.3390/axioms12010073; first public date 2023-01-11; MSC 34C23, 60H10, 92D25.
2. Y. Wang, Y. Shao, C. Chai, *Dynamics of a predator-prey model with fear effects and gestation delays*, AIMS Mathematics 8 (2023), 8160–8180, DOI 10.3934/math.2023378; comparison source for a distinct delayed food-chain model.
3. S. Pal, N. Pal, S. Samanta, J. Chattopadhyay, *Role of Fear in a Predator–Prey Model with Beddington–DeAngelis Functional Response*, Zeitschrift für Naturforschung A 74 (2019), DOI 10.1515/zna-2018-0449; background on fear effects in the same response family.
