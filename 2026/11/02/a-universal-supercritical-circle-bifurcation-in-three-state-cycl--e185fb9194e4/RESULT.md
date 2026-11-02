# A universal supercritical circle bifurcation in three-state cyclic softmax feedback

## Finding
Let \(\Delta_2=\{x\in[0,1]^3:\sum_{j=0}^2x_j=1\}\), let \(P(x_0,x_1,x_2)=(x_2,x_0,x_1)\), and let \(\sigma_\beta(x)_j=e^{\beta x_j}/\sum_k e^{\beta x_k}\). For fixed \(0<\varepsilon<1\), \(\varepsilon\ne 2/3\), consider the analytic simplex map
\[
F_{\beta,\varepsilon}(x)=((1-\varepsilon)I+\varepsilon P)\sigma_\beta(x),\qquad \beta>0.
\]
Write \(r_\varepsilon=\sqrt{1-3\varepsilon+3\varepsilon^2}\) and \(\beta_c=3/r_\varepsilon\). The uniform fixed point \(x_*=(1/3,1/3,1/3)\) is locally exponentially attracting for \(0<\beta<\beta_c\), and is repelling on the simplex for \(\beta>\beta_c\). At \(\beta=\beta_c\) it is locally asymptotically attracting and, for every sufficiently close initial point other than \(x_*\),
\[
\left|\sum_{j=0}^2e^{2\pi i j/3}x_{n,j}\right|\sim r_\varepsilon\sqrt{\frac{2}{3n}}.
\]
For all sufficiently small \(\mu=\beta-\beta_c>0\), a locally attracting smooth invariant Jordan curve \(\mathcal C_{\beta,\varepsilon}\) bifurcates from \(x_*\). Uniformly along this curve, its complex Fourier coordinate satisfies
\[
\left|\sum_{j=0}^2e^{2\pi i j/3}x_j\right|=\frac23 r_\varepsilon^{3/2}\sqrt{\mu}+O_\varepsilon(\mu).
\]
The exact radial cubic coefficient of the critical Neimark–Sacker normal form is \(-3/(4r_\varepsilon^2)\), strictly negative throughout this family. In the balanced case \(\varepsilon=1/2\), the threshold is exactly \(\beta_c=6\), the cubic coefficient is exactly \(-3\), the critical decay is \((6n)^{-1/2}\), and the newborn curve has Fourier radius \(\sqrt{\mu/18}+O(\mu)\).

## Assumptions and scope
The state space is the two-dimensional simplex with its relative topology. The parameter \(\varepsilon\) is fixed while \(\beta\) varies. The endpoint mixing values \(\varepsilon=0,1\) and the fourth-order resonance \(\varepsilon=2/3\) are excluded. “Attracting curve” means normally locally attracting as an invariant compact set; dynamics restricted to the curve may be phase locked and are not claimed to be irrational or chaotic. No global basin classification is asserted.

## Proof
Set \(\omega=e^{2\pi i/3}\), \(z=x_0+\omega x_1+\omega^2x_2\), and \(y=x-x_*\). Since \(\sum_jy_j=0\),
\[
y_j=\frac{z\omega^{-j}+\overline z\omega^j}{3},\quad \sum_jy_j^2=\frac23|z|^2,\quad \sum_j\omega^jy_j^2=\frac13\overline z^2.
\]
Expanding the softmax at \(x_*\), using the cubic identity \(y_j^3=(\sum_ky_k^2)y_j/2+(\sum_ky_k^3)/3\), gives the exact third-order Fourier jet
\[
z\longmapsto\lambda\left(\frac\beta3z+\frac{\beta^2}{18}\overline z^2-\frac{\beta^3}{54}z|z|^2\right)+O_\beta(|z|^4),\qquad \lambda=1-\varepsilon+\varepsilon\omega.
\]
Here \(|\lambda|=r_\varepsilon\) and the two real tangent multipliers at \(x_*\) are \(\beta\lambda/3\) and its conjugate. Hence their modulus crosses one transversely at \(\beta_c=3/r_\varepsilon\), with slope \(r_\varepsilon/3>0\).

At criticality write \(a=\lambda/r_\varepsilon=e^{i\theta}\), \(b=a/(2r_\varepsilon)\), and \(c=-a/(2r_\varepsilon^2)\). The critical third-order jet is \(az+b\overline z^2+cz|z|^2\). The allowed angles satisfy \(0<\theta<2\pi/3\); the only fourth-order strong resonance in this interval occurs at \(\theta=\pi/2\), equivalently \(\varepsilon=2/3\). Third-order resonance occurs only at the excluded endpoint \(\varepsilon=1\). Thus the quadratic term can be eliminated using \(z=w+p\overline w^2+O(|w|^3)\), with
\[
p=\frac{b}{\overline a^2-a}=\frac{a^3}{2r_\varepsilon(1-a^3)}.
\]
After elimination, the coefficient of \(w|w|^2\) is \(d=c+2b\overline p\). Therefore
\[
\Re(\overline a d)=\frac1{2r_\varepsilon^2}\Re\left(-1+\frac1{a^3-1}\right)=-\frac3{4r_\varepsilon^2},
\]
using \(\Re[(e^{it}-1)^{-1}]=-1/2\) whenever \(t\not\in2\pi\mathbb Z\). The nonvanishing negative coefficient, transverse crossing, and fourth-order nonresonance meet the classical supercritical Neimark–Sacker theorem for analytic plane diffeomorphisms. The resulting attracting invariant Jordan curve has normal-form radius squared equal to
\[
\frac{(\beta-\beta_c)r_\varepsilon/3}{3/(4r_\varepsilon^2)}+o(\beta-\beta_c)=\frac49r_\varepsilon^3(\beta-\beta_c)+o(\beta-\beta_c).
\]
The near-identity change of coordinates changes radius by \(O(\beta-\beta_c)\), giving the stated amplitude.

At criticality, the same normal form yields \(|w_{n+1}|=|w_n|-[3/(4r_\varepsilon^2)]|w_n|^3+O_\varepsilon(|w_n|^4)\). For every nearby nonzero orbit the radius decreases to zero, and its inverse square gains \(3/(2r_\varepsilon^2)+o(1)\) per iterate. Cesàro summation yields \(|w_n|\sim r_\varepsilon\sqrt{2/(3n)}\); the near-identity coordinate change gives the identical leading law for \(|z_n|\). In the balanced case \(\lambda=e^{i\pi/3}/2\), so \(p=-1/2\), \(d=-3e^{i\pi/3}\), giving the specialized constants.

## Verification
The standalone `verify.py` checks the exact Fourier identities and normal-form coefficients with symbolic arithmetic at three mixing parameters; it also evaluates finite trajectory consistency, the Taylor jet, linear multipliers, the critical decay, and emerging radial scaling. Run `python verify.py` with Python 3, NumPy, and SymPy. Its finite numerical tests do not prove the general analytic assertions, which follow from the algebraic jet and the classical local bifurcation theorem.

## Relationship to prior work
Jones (2026) proves a Lyapunov descent for the network-free *tied* softmax feedback map and observes that untied embeddings permit recurrent behavior; the present calculation supplies a three-state, network-free, untied example with exact universal onset and radial coefficients. Wang (2026) gives a global logit contraction certificate \(\beta\|\Pi W\Pi\|<2\), which for the conjugate cyclic payoff map covers \(\beta<2/r_\varepsilon\) but not the local bifurcation at \(3/r_\varepsilon\). Tino (2009) concerns iterated unmixed softmax equilibria. Umezuki (2018) proves an attracting invariant curve for a rock–paper–scissors logit game and is a directly relevant qualitative antecedent; the present statement is specifically the exact mixing-family coefficient, critical decay, and amplitude law, not the generic existence of logit oscillations. The complete 2018 article was unavailable for comparison, leaving a historical-priority risk.

## Limitations
This is a local bifurcation result for a three-state cyclic interaction. The resonance \(\varepsilon=2/3\) is outside its stated hypotheses. No claim is made about global uniqueness, global stability, higher-temperature dynamics, the rotation number on the born curve, or arbitrary untied readouts. Comparison with the inaccessible complete 2018 rock–paper–scissors article remains an explicit priority limitation. Independent external scientific validation has not been performed.

## References
1. Timothy D. Jones, *Chaos and bifurcations in continuous language-model feedback*, arXiv:2610.31692v1, first posted 2026-10-20. https://arxiv.org/html/2610.31692v1
2. Tongxi Wang, *Sharp Spectral Thresholds for Logit Fixed Points*, arXiv:2605.15651v1, first posted 2026-05-15. https://arxiv.org/html/2605.15651v1
3. Yosuke Umezuki, *Bifurcation analysis of the rock–paper–scissors game with discrete-time logit dynamics*, Mathematical Social Sciences 95 (2018), 54–65. https://doi.org/10.1016/j.mathsocsci.2017.12.001
4. Peter Tiňo, *Bifurcation structure of equilibria of iterated softmax*, Chaos, Solitons & Fractals 41 (2009), 1804–1816. https://doi.org/10.1016/j.chaos.2008.07.026
5. Yuri A. Kuznetsov, *Elements of Applied Bifurcation Theory*, fourth edition, Springer, 2023 (local Neimark–Sacker normal-form theorem).
