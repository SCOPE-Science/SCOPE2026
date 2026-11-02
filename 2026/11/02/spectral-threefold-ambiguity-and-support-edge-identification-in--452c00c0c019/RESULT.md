# Spectral threefold ambiguity and support-edge identification in a telegraph-driven inertial trap

## Finding

**Theorem (complete covariance fiber and one-edge identification).** Let a stationary, athermal, one-dimensional inertial particle obey the symmetrically switching-force equation specified below. The entire stationary position autocovariance determines its four positive normalized parameters uniquely in the underdamped regime. In the overdamped or critically damped regime, however, the same covariance has precisely as many physically different parameter realizations as there are distinct rates in an observable multiset of three positive decay rates: one, two, or three. A single additional observation of the essential position-support radius removes *every* such ambiguity. The claim includes repeated spectral poles and the mechanical critical-damping boundary.

In particular, stationary position and velocity second-order measurements, even with every possible time lag, cannot distinguish the three distinct systems
\[
(q,p,c,f)=(5,6,1,\sqrt6),\quad(4,3,2,\sqrt3),\quad(3,2,3,\sqrt2).
\]
Each has exactly the same position spectrum
\[
S_X(\omega)=\frac{12}{(\omega^2+1)(\omega^2+4)(\omega^2+9)},
\]
while their essential position-support radii are respectively \(1/\sqrt6\), \(1/\sqrt3\), and \(1/\sqrt2\).

## Assumptions and scope

The mass-normalized model is
\[
\ddot X_t+q\dot X_t+pX_t=f\sigma_t,
\qquad q,p,c,f>0.
\]
Here \(\sigma_t\in\{-1,+1\}\) is an independent, symmetric, stationary continuous-time two-state Markov process switching sign at rate \(c/2\). There is **no additional Gaussian thermal driving**, no time-dependent drive parameters, and \(X\) and its velocity are taken in their unique stationary linear-filter regime. The mass is known, normalized to one. For an oscillator with physical mass \(m\), damping \(\gamma\), stiffness \(\mu\), and force amplitude \(a_0\), the identifiable quantities are \(q=\gamma/m\), \(p=\mu/m\), and \(f=a_0/m\), not the four unnormalized coefficients when mass is unknown.

The data are the exact population covariance \(C_X(t)=\mathbb E[X_0X_t]\) for all real lags \(t\), equivalently its Fourier spectral density \(S_X(\omega)=\int_{-\infty}^{\infty}e^{-i\omega t}C_X(t)\,dt\). An additional observation, where indicated, is \(R=\operatorname*{ess\,sup}|X_0|\). These are ideal distributional quantities, not empirical estimates. The physical underdamped region is \(q^2<4p\); the overdamped/critical region is \(q^2\ge4p\).

## Proof

**1. Stationary transfer spectrum.** The impulse response of the stable mechanical equation is integrable and decays exponentially. The stationary telegraph drive is centered and obeys
\[
\mathbb E[\sigma_0\sigma_t]=e^{-c|t|},\qquad
S_{\sigma}(\omega)=\frac{2c}{\omega^2+c^2}.
\]
Filtering through the transfer function \(H(i\omega)=(p-\omega^2+iq\omega)^{-1}\) gives, for every real frequency,
\[
S_X(\omega)=\frac{2K}{(\omega^2+c^2)[(p-\omega^2)^2+q^2\omega^2]},\qquad K=cf^2>0.\tag{1}
\]
With \(z=\omega^2\), the denominator is the monic cubic
\[
P(z)=(z+c^2)\bigl[z^2+(q^2-2p)z+p^2\bigr].\tag{2}
\]
An exact spectrum determines \(K=\frac12\lim_{|\omega|\to\infty}\omega^6S_X(\omega)\) and all coefficients of the monic polynomial \(P\). As \(K>0\), no denominator factor is canceled. Conversely \((K,P)\) determines the complete covariance.

**2. Underdamped identifiability.** When \(q^2<4p\), the mechanical quadratic has discriminant
\[
(q^2-2p)^2-4p^2=q^2(q^2-4p)<0.
\]
It is the unique irreducible real quadratic factor of \(P\), and \(z+c^2\) is the unique real linear factor. Hence \(c>0\) is determined, then the mechanical quadratic's constant term determines \(p>0\), its linear coefficient determines \(q>0\), and \(f=\sqrt{K/c}\). A spectrum from this regime cannot coincide with an overdamped spectrum, whose cubic has only real negative roots.

**3. Complete overdamped/critical covariance fiber.** For \(q^2\ge4p\), define the positive mechanical relaxation rates
\[
a=\frac{q-\sqrt{q^2-4p}}2,\qquad
b=\frac{q+\sqrt{q^2-4p}}2.
\]
Thus \(a+b=q\), \(ab=p\), and equation (1) becomes
\[
S_X(\omega)=\frac{2K}
{(\omega^2+a^2)(\omega^2+b^2)(\omega^2+c^2)}.\tag{3}
\]
The covariance determines precisely the positive **multiset** of rates \(\{a,b,c\}\), with multiplicity, because a monic real polynomial has unique factorization. It does not mark which factor belongs to the telegraph force. Conversely, fix any spectral multiset \(\{u,v,w\}\subset(0,\infty)\) and \(K>0\). For each *distinct* choice of one of its elements as telegraph rate \(c\), let \(a,b\) be the two remaining elements and set
\[
q=a+b,\qquad p=ab,\qquad f=\sqrt{K/c}.\tag{4}
\]
These are all admissible overdamped/critical parameters with exactly the same spectrum. Every realization must arise this way by factorization, so the number of distinct realizations is exactly one, two, or three, according to the number of distinct spectral rates. Repeated roots therefore do not create spurious extra solutions.

**4. Exact support radius and its inverse.** For all overdamped/critical mechanical parameters, the causal impulse response is nonnegative:
\[
g(t)=\begin{cases}
\displaystyle\frac{e^{-at}-e^{-bt}}{b-a},&a<b,\\[4pt]
\displaystyle t e^{-at},&a=b,
\end{cases}\qquad t\ge0,
\]
with \(\int_0^\infty g(t)\,dt=1/(ab)=1/p\). The stationary position is the convergent random integral \(X_0=f\int_0^\infty g(s)\sigma_{-s}\,ds\), and consequently \(|X_0|\le f/p\) almost surely.

This bound is sharp as an **essential** support radius, rather than merely a deterministic bound. For any \(T>0\), the event that the stationary telegraph sign stays \(+1\) throughout the preceding interval of length \(T\) has probability \(\tfrac12e^{-cT/2}>0\). On this event, regardless of earlier signs,
\[
X_0\ge \frac fp-2f\int_T^\infty g(s)\,ds.
\]
The tail integral tends to zero. Hence for every \(\varepsilon>0\), \(\mathbb P(X_0>f/p-\varepsilon)>0\); symmetry gives the negative edge as well. Thus
\[
R=\operatorname*{ess\,sup}|X_0|=\frac fp.\tag{5}
\]
Let \(P_*=uvw=abc>0\) be the product of all **observable** spectral rates. Equations (4)--(5) imply
\[
R^2=\frac{K/c}{(ab)^2}
=\frac{Kc}{P_*^2},\qquad
\boxed{c=\frac{R^2P_*^2}{K}}.\tag{6}
\]
Consequently, covariance plus \(R\) marks the unique telegraph factor among the three (even with collisions), determines the remaining mechanical rates as a multiset, and recovers \(q,p,f\) via (4). In the underdamped regime covariance already determines everything, proving the complete theorem.

**5. Sharp threefold witness and full second-order indistinguishability.** Taking spectral poles \(\{1,2,3\}\) and \(K=6\) gives the three listed quadruples and exactly equation (3). They all have stationary second moments \(\mathbb E[X^2]=\mathbb E[\dot X^2]=1/10\), as may independently be derived from generator moment balance. Because position paths are continuously differentiable and velocity is their derivative, every stationary velocity--velocity and position--velocity second-order function is obtained by differentiation of the same \(C_X\). Hence measuring all such second-order observables cannot separate the three. Equation (5) yields three different radii and therefore resolves them.

## Verification

The included standalone standard-library program `verify.py` independently forms the spectrum both through its cubic in \(\omega^2\) and through numerical-frequency evaluation; it verifies the threefold witness, collision multiplicities, the support-decoding formula, an independent stationary-generator second-moment route, and the negative discriminant of the underdamped mechanical quadratic. It completed 23,003 deterministic randomized assertions successfully. The mathematical proof above, not finite checks, establishes the theorem for the full stated parameter range.

For example, the stationarity generator identities \(\mathbb E[X\dot X]=0\), \(\mathbb E[\dot X\sigma]=c\mathbb E[X\sigma]\), and \(\mathbb E[X\sigma]=f/(p+cq+c^2)\) give
\[
\mathbb E[X^2]=\frac{f^2(q+c)}{pq(p+cq+c^2)},\qquad
\mathbb E[\dot X^2]=\frac{cf^2}{q(p+cq+c^2)},
\]
which evaluate to \(1/10\) for each alias in the exact witness.

## Relationship to prior work

Dutta, Kundu, Sabhapandit, and Basu (2024), arXiv:2406.06120, introduce and analyze the same physical inertial run-and-tumble oscillator and determine stationary moment and spatial-support properties. The existence of the bounded support in the overdamped model, the Markov telegraph autocorrelation, and linear-filter spectral formulas are **not claimed to be new**. Smith and Farago (2022) analyze harmonic confinement under telegraphic active driving, notably the stationary spatial law and its large-deviation limit. Bonciolini, Boujo, and Noiray (2017) discuss output-only inference for a nonlinear colored-noise-driven oscillator but not the precise physical inverse classification proved here.

The narrow contribution assessed here is the **complete and sharp covariance-equivalence classification, including repeated rates and the underdamped boundary, combined with an explicit one-support-edge inverse rule** for the mass-normalized athermal telegraph oscillator. Algebraically it is a spectral-factor allocation ambiguity; the conclusion distinguishes observational equivalence from equality of physical stochastic mechanisms. A general spectral-system-identification theorem may subsume this specialization, which remains a priority risk.

## Limitations

The theorem assumes exact all-lag stationary covariance and, where needed, an exact essential support boundary. Such ideal data cannot be obtained from finitely many noisy observations without additional estimation theory; the result does not assert stable practical inversion. Both the telegraph driving statistics and the linear harmonic equation are known *a priori* as model classes. Additional thermal Brownian forcing, asymmetric telegraph switching, nonlinear mechanics, unknown mass normalization, or nonstationary preparation are not covered. Positivity of the mechanical Green function and the edge formula are asserted only for the overdamped/critical regime; the underdamped identification uses covariance alone. No claims about experimental efficiency, finite-sample recovery, or generic colored-noise models are made.

## References

1. D. Dutta, A. Kundu, S. Sabhapandit, and U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, first public arXiv version June 10, 2024, arXiv:2406.06120; *Physical Review E* 110, 044107 (2024), DOI: 10.1103/PhysRevE.110.044107.
2. N. R. Smith and I. Farago, *Nonequilibrium steady state for harmonically confined active particles*, *Physical Review E* 106, 054118 (2022), DOI: 10.1103/PhysRevE.106.054118.
3. G. Bonciolini, E. Boujo, and N. Noiray, *Output-only parameter identification of a colored-noise-driven Van-der-Pol oscillator: Thermoacoustic instabilities as an example*, *Physical Review E* 95, 062217 (2017), DOI: 10.1103/PhysRevE.95.062217.
