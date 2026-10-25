# A sharp two-channel peak-merger tomography theorem for telegraph frequency noise

## Finding

For a stationary symmetric telegraph frequency perturbation with positive homogeneous decay \(g\), positive frequency displacement \(a\), and total telegraph correlation-decay rate \(q\), the **coherent-amplitude** and **absorptive** spectral channels lose their two off-center peaks at different, exactly determined rates. If their observed positive coalescence rates are respectively \(Q\) and \(P\), then the two observations uniquely determine both previously unknown positive parameters \(g\) and \(a\) if and only if

\[
P>0,\qquad \frac{Q}{P}>\rho_*:=\sqrt{\frac{1+\sqrt2}{2}}.
\]

Every such pair is realized, uniquely. No positive parameter pair realizes \(Q/P\leq\rho_*\); the lower ratio boundary is sharp but not attained. This is an exact model-identifiability statement, not a noise-robust inference claim.

## Assumptions and scope

Let \(S_t\in\{-1,+1\}\) be a stationary continuous-time two-state Markov chain with transition rate \(q/2\) in **each** direction and \(q\geq0\). Take \(g>0\) and \(a>0\). The dimensionless, unit-forcing complex linear response at frequency detuning \(\omega\in\mathbb R\) is

\[
F(\omega)=\int_0^\infty e^{-(g-i\omega)t}\,\mathbb E\!\left[\exp\!\left(ia\int_0^t S_s\,ds\right)\right]dt.
\]

Define the two measured channels as coherent amplitude \(M(\omega)=|F(\omega)|\) and absorptive intensity \(I(\omega)=\operatorname{Re}F(\omega)\). An off-center doublet means precisely two strict global maxima at nonzero symmetric frequencies; a merged line has its unique global maximum at zero. At a merger, zero is a unique, quartically flat maximum. The convention \(q=2\times\text{individual state-switching rate}\) is essential.

## Proof

Put \(C(t)=\mathbb E[\exp(ia\int_0^t S_sds)]\). The two conditional phase averages obey the two-state Kolmogorov system. Adding and subtracting shows \(C''+qC'+a^2C=0\) with \(C(0)=1\) and \(C'(0)=0\). Its Laplace transform gives

\[
F(\omega)=\frac{g+q-i\omega}{(g-i\omega)(g+q-i\omega)+a^2}.
\]

Write \(h=g+q\), \(c=gh+a^2\), \(z=\omega^2\), and \(B=(2g+q)^2-2c\). The common strictly positive denominator is

\[
D(z)=(c-z)^2+(2g+q)^2z=z^2+Bz+c^2>0 \quad(z\geq0),
\]

and elementary complex arithmetic yields

\[
M(\omega)^2=\frac{h^2+z}{D(z)},\qquad I(\omega)=\frac{hc+gz}{D(z)}.
\]

The numerators of the derivatives with respect to \(z\), after multiplying by \(D(z)^2\), are respectively

\[
-z^2-2h^2z+(c^2-h^2B),
\qquad
-gz^2-2hcz+c(gc-hB).
\]

Both are strictly decreasing on \([0,\infty)\) (their derivatives are strictly negative). Hence **each** channel has an off-center doublet precisely when the corresponding derivative at \(z=0\) is positive. A zero derivative at \(z=0\) gives a single quartically flat central maximum, since both derivative numerators are then strictly negative for positive \(z\). Solving the two central-sign conditions gives the exact thresholds

\[
M\text{ splits}\iff a^2>A_g(q),\quad
A_g(q)=\frac{(g+q)^3}{2g+q+\sqrt{(g+q)^2+(2g+q)^2}},
\]

\[
I\text{ splits}\iff a^2>B_g(q),\quad
B_g(q)=\frac{(g+q)^3}{3g+2q}.
\]

For any \(g>0\) and \(q\geq0\), \(A_g(q)<B_g(q)\). To see this, put \(u=g/(g+q)\in(0,1]\) and \(t=1+u\). Then \(A_g(q)=(g+q)^2/(\sqrt{1+t^2}+t)\) while \(B_g(q)=(g+q)^2/(1+t)\). Both thresholds are strictly increasing with \(q\): the square \((g+q)^2\) increases, while \(u\) and each positive denominator decrease. At zero rate, \(A_g(0)=g^2(\sqrt5-2)\) and \(B_g(0)=g^2/3\). Thus when \(a^2>g^2/3\), absorption merges at a unique positive \(P\), then amplitude merges at a unique larger positive \(Q\), characterized by

\[
a^2=B_g(P)=A_g(Q),\qquad0<P<Q.
\]

For uniqueness in the inverse direction fix \(0<P<Q\) and consider \(H(g)=A_g(Q)/B_g(P)\). Its endpoint limits are

\[
H(0+)=2(\sqrt2-1)(Q/P)^2,
\qquad
H(+\infty)=3(\sqrt5-2)<1.
\]

We prove that \(H\) is strictly decreasing. At fixed \(q\), with \(u=g/(g+q)\), direct differentiation gives

\[
\frac{\partial\log A_g(q)}{\partial g}=
\frac{1}{g+q}\left(2-\frac{1-u}{\sqrt{1+(1+u)^2}}\right),
\]

\[
\frac{\partial\log B_g(q)}{\partial g}=
\frac{1}{g+q}\left(2-\frac{1-u}{2+u}\right).
\]

The first logarithmic derivative is strictly decreasing as \(q\) increases at fixed \(g\): after multiplying by \(g\), it equals \(u[2-(1-u)/\sqrt{1+(1+u)^2}]\), a strictly increasing function of \(u\), while \(u\) decreases in \(q\). At equal \(g,q\), the first logarithmic derivative is strictly less than the second because \(\sqrt{1+(1+u)^2}<2+u\). Since \(Q>P\), these facts imply

\[
\frac{H'(g)}{H(g)}=
\frac{\partial\log A_g(Q)}{\partial g}-
\frac{\partial\log B_g(P)}{\partial g}<0.
\]

Thus \(H(g)=1\) has exactly one positive solution if and only if \(H(0+)>1\), namely \(Q/P>\sqrt{(1+\sqrt2)/2}\). Recover \(g\) from this unique root and set \(a=\sqrt{B_g(P)}\). All inequalities are strict, so the constructed model has the required two positive coalescence rates. If equality holds in the observed ratio, the only limiting solution has \(g=0\), excluded by hypothesis. This proves necessity, sufficiency, and uniqueness.

## Verification

The standalone `check.py` reproduces the response from the conditional two-state linear system, compares its rational expression numerically, checks the signs of both peak derivatives on each side of their transitions, and reverses the map from \((g,a)\) to \((P,Q)\) and back. Its deterministic tests cover 500 parameter pairs, 1,500 independently evaluated matrix responses, and 1,500 peak-sign cases. The limiting spectral-ratio boundary is checked numerically. These finite tests corroborate; the analytic monotonicity and derivative arguments above establish the infinite-parameter theorem.

## Relationship to prior work

The Kubo–Anderson stochastic line-broadening framework and its characteristic two-peak-to-one-peak behavior are classical. Dykman and collaborators (2010) analyze coupled partial susceptibilities and the general frequency-jump forward response. Li and collaborators (2012) display the symmetric random-telegraph absorption line in their equation (3) and describe motional averaging. Sun and collaborators (2015) calculate the complex-amplitude moments of a fluctuating mechanical resonator and experimentally observe the coalescence of two coherent-amplitude peaks. The normalized absorptive and amplitude channels here are consistent with those forward descriptions after matching the switching-rate convention. The asserted distinct contribution is their **joint global inverse theorem from the two channel-specific coalescence rates**, including its exact ratio obstruction and uniqueness proof; it is not a new stochastic response formula nor a new experimental observation of peak merger.

## Limitations

This conclusion assumes symmetric stationary telegraph switching, exact linear response, identical linewidth across states, and strictly positive homogeneous damping. It concerns two **different** spectral readouts observed while varying the same switching rate, with the absolute scale of the switching-rate axis calibrated. It does not address finite frequency sampling, finite averaging time, detector noise, power broadening, asymmetric state occupancies, extra spectral modes, or statistical stability near the sharp boundary. Specialized spectroscopic literature may contain an equivalent unlocated classification; independent originality assessment remains outstanding.

## References

1. M. I. Dykman, M. Khasin, J. Portman, and S. W. Shaw, *Spectrum of an oscillator with jumping frequency and the interference of partial susceptibilities*, arXiv:1006.2402, first public posting 2010-06-11. https://arxiv.org/abs/1006.2402
2. J. Li et al., *Motional Averaging in a Superconducting Qubit*, arXiv:1205.0675, first posting 2012-05-03. https://arxiv.org/abs/1205.0675
3. F. Sun, J. Zou, Z. A. Maizelis, and H. B. Chan, *Telegraph frequency noise in electromechanical resonators*, arXiv:1511.00893, first posting 2015-11-03. https://arxiv.org/abs/1511.00893
4. P. W. Anderson, *A Mathematical Model for the Narrowing of Spectral Lines by Exchange or Motion*, J. Phys. Soc. Japan 9 (1954), 316–339. https://doi.org/10.1143/JPSJ.9.316
