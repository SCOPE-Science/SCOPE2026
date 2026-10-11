# Exact phase reduction and corrected first crossing in a fractional Lotka–Volterra feedback example
## Finding
For the printed Example 4.1, fix \(q=19/20\), \(E_*=(2/3,1/3)\), and \(-1<k\le 0\). Direct linearization gives
\[
D^q u(t)=B(k)u(t-\tau),\qquad
B(k)=\begin{pmatrix}k-2/3&-2/3\\2/3&-1/3\end{pmatrix}.
\]
Thus
\[
\det\!\left(s^qI-e^{-s\tau}B(k)\right)=0
\]
is equivalent, after setting \(z=s^q e^{s\tau}\), to
\[
z^2+(1-k)z+\frac{2-k}{3}=0.
\]
For \(-1<k\le0\), its roots are the conjugate pair
\[
z_\pm=-\frac{1-k}{2}\pm\frac{i}{2}\sqrt{\frac{(5-3k)(k+1)}{3}}.
\]
Writing
\[
\theta(k)=\pi-\arctan\!\left(\frac{\sqrt{(5-3k)(k+1)/3}}{1-k}\right),
\]
the first positive imaginary-axis crossing of the printed characteristic equation is
\[
\omega(k)=\left(\frac{2-k}{3}\right)^{10/19},\qquad
\tau_*(k)=\frac{\theta(k)-19\pi/40}{\omega(k)}.
\]
At \(k=-1/2\), this becomes
\[
\omega_*=(5/6)^{10/19}=0.908501523595597\ldots,
\]
\[
\tau_*=
\frac{21\pi/40-\arctan\sqrt{13/27}}{(5/6)^{10/19}}
=1.147739992150082\ldots.
\]
Therefore the paper's quoted frequency \(0.9085\) is consistent with its printed linearization, but the quoted critical delay \(1.0229\) is not. The corrected first crossing lies strictly between the paper's stable numerical trajectory at \(\tau=0.93\) and its oscillatory trajectory at \(\tau=1.16\).

For the other gains explicitly listed in the text, the same exact formula gives
\[
\tau_*(-0.2)=1.006426722476691\ldots,
\]
\[
\tau_*(-0.4)=1.099212921322829\ldots,
\]
\[
\tau_*(-0.6)=1.199539746365918\ldots.
\]
These replace the printed sequence \(0.9825,1.185,1.324\) for those three stated gains. The value \(1.324\) is numerically close to the exact threshold \(1.324532019436339\ldots\) at \(k=-0.8\), which is the third gain actually shown in Figures 7--8; no claim is made about how the textual mismatch arose.

## Assumptions and scope
The calculation uses the model exactly as printed in Example 4.1,
\[
D^{19/20}x(t)=x(t)\bigl[1-x(t-\tau)-y(t-\tau)\bigr]+k\bigl[x(t-\tau)-2/3\bigr],
\]
\[
D^{19/20}y(t)=y(t)\bigl[-1+2x(t-\tau)-y(t-\tau)\bigr].
\]
The range \(-1<k\le0\) contains the source's displayed feedback gains and keeps the quadratic roots nonreal. Fractional powers use the principal branch, matching the source's substitution \(s=i\omega\) and \((i\omega)^q=\omega^q e^{iq\pi/2}\). The result is a spectral statement about the printed linearization. It does not establish a nonlinear Hopf normal form, cycle direction, or cycle stability.

## Proof
At \(E_*=(2/3,1/3)\), the current-state derivatives of the Lotka--Volterra brackets vanish because the equilibrium brackets are zero. Differentiating only the delayed arguments gives
\[
B(k)=\begin{pmatrix}k-2/3&-2/3\\2/3&-1/3\end{pmatrix}.
\]
Therefore
\[
0=\det\!\left(s^qI-e^{-s\tau}B(k)\right)
=s^{2q}+(1-k)s^q e^{-s\tau}+\frac{2-k}{3}e^{-2s\tau}.
\]
Multiplication by \(e^{2s\tau}\) and the definition \(z=s^q e^{s\tau}\) give the quadratic claimed above.

Its discriminant is
\[
\Delta=(1-k)^2-\frac{4(2-k)}3=\frac{(3k-5)(k+1)}3<0
\]
for \(-1<k\le0\). Hence
\[
|z_\pm|^2=\frac{2-k}{3}
\]
and the upper root has argument \(\theta(k)\) displayed above. For an imaginary root \(s=i\omega\),
\[
z=\omega^q e^{i(q\pi/2+\omega\tau)}.
\]
Matching moduli gives
\[
\omega=|z_+|^{1/q}=\left(\frac{2-k}{3}\right)^{10/19}.
\]
Matching the smallest positive phase for \(z_+\) gives
\[
\tau_*(k)=\frac{\theta(k)-19\pi/40}{\omega(k)}.
\]
The lower conjugate root first matches at
\[
\frac{2\pi-\theta(k)-19\pi/40}{\omega(k)},
\]
which is larger because \(\theta(k)<\pi\); every further phase match adds \(2\pi/\omega(k)\). Thus \(\tau_*(k)\) is the first positive imaginary-axis crossing of this characteristic equation.

At \(k=-1/2\),
\[
z_\pm=-\frac34\pm i\sqrt{\frac{13}{48}},\qquad |z_\pm|=\sqrt{\frac56},
\]
so the exact expressions for \(\omega_*\) and \(\tau_*\) follow.

Finally, along either scalar spectral branch \(s^q e^{s\tau}=z_\pm\), implicit differentiation gives
\[
\left(\frac{q}{s}+\tau\right)\frac{ds}{d\tau}+s=0.
\]
At \(s=i\omega\),
\[
\operatorname{Re}\frac{ds}{d\tau}
=\frac{q\omega^2}{q^2+\tau^2\omega^2}>0,
\]
so the first crossing is transversal and moves into the open right half-plane as \(\tau\) increases.

## Verification
The bundled checker reconstructs the delayed Jacobian, verifies the quadratic coefficients, evaluates the exact phase formulas, confirms the ordering of the two first phase branches, and checks the characteristic residual and the positive crossing derivative. At \(k=-1/2\) it returns \(\omega_*=0.908501523595597\ldots\), \(\tau_*=1.147739992150082\ldots\), and crossing speed \(0.394068327579239\ldots\).

The primary source itself gives an independent coarse numerical bracket: its Figures 1--2 label \(\tau=0.93\) as asymptotically stable, whereas Figure 3 shows periodic oscillation at \(\tau=1.16\). The corrected spectral crossing lies inside that bracket.

## Relationship to prior work
Li, Zhang, Huang and Zhou derive the same characteristic quasipolynomial in their equation (3.3) but proceed through separate trigonometric equations. Their Example 4.1 reports \(\omega_0=0.9085\) and \(\tau_0=1.0229\), and the text lists further thresholds \(0.9825,1.185,1.324\) for \(k=-0.2,-0.4,-0.6\). The article's own Figure 1, however, labels the trajectory at \(\tau=0.93\) asymptotically stable, contrary to the prose immediately above it that calls the same case unstable. The exact common-delay reduction resolves the numerical boundary directly from the printed linearization and reconciles the first crossing with the stable/oscillatory simulations.

The 2018 Huang--Song--Fang--Xiao--Cao paper studies feedback control in a different delayed fractional predator--prey model, and the 2019 Li--Huang--Song paper treats a three-species two-prey/one-predator system. Neither inspected statement gives this two-dimensional Example 4.1 phase reduction or its corrected thresholds.

## Limitations
The finding is local and spectral. It does not prove the nonlinear existence, direction, or orbital stability of a Hopf branch, and it does not validate the source's numerical integration scheme. The first-public-date metadata has a one-day discrepancy: OpenAlex records \(2020\text{-}10\text{-}26\), while the publisher PDF labels the article published on \(2020\text{-}10\text{-}27\); the earlier public bibliographic date is retained in the metadata. Searches for corrections and equivalent statements are necessarily non-exhaustive.

## References
1. Z. Li, W. Zhang, C. Huang, J. Zhou, “Bifurcation for a fractional-order Lotka-Volterra predator-prey model with delay feedback control,” AIMS Mathematics 6(1), 675--687. DOI: 10.3934/math.2021040.
2. C. Huang, X. Song, B. Fang, M. Xiao, J. Cao, “Modeling, Analysis and Bifurcation Control of a Delayed Fractional-Order Predator--Prey Model,” International Journal of Bifurcation and Chaos 28(9), 1850117. DOI: 10.1142/S0218127418501171.
3. S. Li, C. Huang, X. Song, “Bifurcation Based-Delay Feedback Control Strategy for a Fractional-Order Two-Prey One-Predator System,” Complexity 2019, 9673070. DOI: 10.1155/2019/9673070.
