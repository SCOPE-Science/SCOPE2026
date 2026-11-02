# Exact Poisson-plateau crossing counts in equal-rate cyclic transport

## Finding

Let \(n\geq2\) and \(\gamma>0\). A continuous-time Markov chain successively visits the \(n\) states \(0,1,\ldots,n-1\), moving only from \(i\) to \(i+1\pmod n\), always at rate \(\gamma\). In the stationary regime, observe only marked jumps \(n-1\to0\). Write \(\nu=\gamma/n\) for their average intensity, and let \(S_n(\omega)\) be the two-sided power spectral density of the centered stationary point-event train, excluding the atom of its uncentered spectrum at frequency zero. The frequency-independent Poisson shot-noise plateau in this convention is \(\nu\).

**Theorem.** For \(\omega>0\), put \(z=\omega/\gamma\). Then
\[
F_n(\omega):=\frac{S_n(\omega)}{\nu}
=\frac{(1+z^2)^n-1}{\left|(1+iz)^n-1\right|^2}.
\]
The continuous extension is \(F_n(0)=1/n\) and \(F_n(\omega)\to1\) as \(\omega\to\infty\). The equation \(F_n(\omega)=1\) has **exactly**
\[
r_n=\left\lfloor\frac n2\right\rfloor-1
\]
distinct positive-frequency solutions, all simple. Between consecutive solutions the sign of \(F_n-1\) strictly alternates, starting below zero near frequency zero. For \(n=2,3\), the spectrum lies strictly below the Poisson plateau at every finite positive frequency. For the memoryless one-stage case \(n=1\), \(F_1\equiv1\), so the crossing-count statement is deliberately restricted to \(n\ge2\).

More precisely, write the crossings in increasing order as \(\omega_1,\ldots,\omega_{r_n}\). Each has the uniquely determined phase \(\theta_j=\arctan(\omega_j/\gamma)\) in the strict interval
\[
\frac{j\pi}{n-1}<\theta_j<
\min\left\{\frac{(j+1)\pi}{n-1},\frac\pi2\right\},\qquad 1\le j\le r_n.
\]
Here the upper endpoint \(\pi/2\) corresponds to an infinite upper frequency bound. These levels are exactly the positive roots of
\[
\sum_{k=1}^{\lfloor n/2\rfloor}(-1)^k\binom n{2k}z^{2k}=0.
\]
For \(n=4\), the sole crossing is \(\omega=\sqrt6\,\gamma\); for \(n=5\), it is \(\omega=\sqrt2\,\gamma\). For \(n=6\), the two crossings have
\[
\frac{\omega^2}{\gamma^2}=\frac{15\pm\sqrt{165}}2.
\]
Within this homogeneous cyclic model class, any observed positive crossing count \(r\) identifies the number of stages up to precisely the adjacent possibilities \(n=2r+2\) or \(n=2r+3\). A flat spectrum corresponds to the one-stage Poisson special case.

## Assumptions and scope

The finite directed ring has exactly one positive rate, \(\gamma\), shared by every transition. Successive marked-event interarrival intervals are independent sums of \(n\) exponential holding times of rate \(\gamma\), hence have the Erlang law of integer shape \(n\). This statement concerns the point-process spectrum of the **single marked return jump**; it is not a claim about spectra of state-occupancy indicator functions or the unmarked total jump process. Both frequency and the rate are continuous and strictly positive except where one-sided limits are specified. The stationary preparation means the marked event process is the equilibrium renewal process; the interarrival law is defined from one marked event to the next.

For the spectral convention, if \(J=\sum_k\delta_{T_k}\) is the stationary event train as a generalized random process, define \(S_n(\omega)\) as the Fourier transform of its centered covariance distribution. A Poisson event process of intensity \(\nu\) has \(S_n(\omega)=\nu\). This avoids conventional factors of two used in one-sided electrical-noise definitions.

## Proof

**1. Waiting times and spectrum.** A marked return renews the state at \(0\). The next return takes the sum of \(n\) independent exponential waiting times, yielding the characteristic transform
\[
\varphi(\omega)=\mathbb E[e^{-i\omega T}]=(1+i\omega/\gamma)^{-n}.
\]
The standard stationary renewal covariance expansion at every nonzero frequency is
\[
\frac{S_n(\omega)}{\nu}=1+2\Re\frac{\varphi(\omega)}{1-\varphi(\omega)}
=\frac{1-|\varphi(\omega)|^2}{|1-\varphi(\omega)|^2}.
\]
This follows directly by conditioning on an event at the origin: positive-lag conditional event densities are the sum of all positive convolution powers of the waiting-time density; negative lags give the conjugate series. Their Fourier transforms converge for nonzero frequency because \(|\varphi(\omega)|<1\). The diagonal same-event term supplies the constant \(1\). Substituting the Erlang transform proves the claimed rational expression. The denominator is nonzero for every \(\omega>0\).

**2. Reduce the plateau comparison to one real trigonometric function.** Let \(R=(1+z^2)^n\), \(A=\Re(1+iz)^n\). The rational formula gives
\[
F_n-1=\frac{2(A-1)}{R+1-2A}.
\]
The denominator equals \(|(1+iz)^n-1|^2>0\). Thus its sign is precisely that of \(A-1\). Set \(\theta=\arctan z\) so \(0<\theta<\pi/2\), and define
\[
H_n(\theta)=\frac{\cos(n\theta)}{\cos^n\theta}=A.
\]
A direct differentiation simplifies without approximation to
\[
H_n'(\theta)=-\frac{n\sin((n-1)\theta)}{\cos^{n+1}\theta}.
\]
Consequently all interior stationary points are \(\theta_j^*=j\pi/(n-1)\), for integers \(1\le j\le r_n\). At each,
\[
H_n(\theta_j^*)=\frac{(-1)^j}{\cos^{n-1}\theta_j^*}.
\]
These values alternate between numbers strictly smaller than \(-1\) and strictly larger than \(1\). At the left boundary \(H_n(0)=1\); it decreases strictly until the first interior stationary point (or the right boundary if there is none). At the right boundary, \(|H_n(\theta)|\to\infty\), with sign \((-1)^{\lfloor n/2\rfloor}\), as follows from the leading term in the expansion of \(\cos(n\theta)\) near \(\pi/2\). This sign is opposite to the sign at the last interior stationary point when there is one.

There are therefore exactly \(r_n\) solutions of \(H_n=1\): one in each interval \((\theta_j^*,\theta_{j+1}^*)\) for \(1\le j<r_n\), and one in \((\theta_{r_n}^*,\pi/2)\). On the latter interval, if the last stationary point is followed by a boundary, the opposite divergent sign and strict monotonicity give existence and uniqueness. On every such open interval \(H_n'\ne0\), so all crossing roots are simple. The plateau sign alternates at those roots, and it is negative below the first. When \(r_n=0\) (\(n=2,3\)), the derivative is strictly negative on the whole interval, so no positive crossing occurs. Converting from \(\theta\) to \(z=\tan\theta\) gives the stated strict localization brackets. Taking real parts of the binomial expansion gives the polynomial condition.

**3. Endpoints and examples.** Since \((1+z^2)^n-1=nz^2+O(z^4)\) and \(|(1+iz)^n-1|^2=n^2z^2+O(z^4)\), the zero-frequency limit is \(1/n\). The highest-degree terms show the large-frequency limit is \(1\). For \(n=4\), \(A-1=-6z^2+z^4\); for \(n=5\), \(A-1=-10z^2+5z^4\); for \(n=6\), \(A-1=-15z^2+15z^4-z^6\). Factoring these proves the exact crossing examples. The integer inversion follows immediately from \(r_n=\lfloor n/2\rfloor-1\).

## Verification

Run `python verify_stage_noise.py` in an environment with Python 3, NumPy, SciPy, and SymPy. The independent method constructs the full \(n\)-state Markov generator and obtains the nonzero-frequency counted-event spectrum from its resolvent, without using the closed Erlang ratio inside that calculation. Separate exact rational-polynomial Sturm root counts cover \(2\le n\le24\), while numerical phase-bracket checks cover \(4\le n\le47\). A completed run passed 4,464 assertions, with maximal absolute discrepancy between the generator and renewal formulas below \(8\times10^{-15}\). Finite tests corroborate, but do not replace, the analytical all-\(n\) argument in the proof.

## Relationship to prior work

The renewal spectrum identity, sequential-cycle waiting-time law, and the frequency-dependent shot-noise framework are **established results**, not original claims. In *Waiting Times and Noise in Single Particle Transport* (2008), Tobias Brandes gives the renewal/noise relationship and studies unidirectional cyclic chains with unequal and equal transition rates, including a many-stage limit. The online *Neuronal Dynamics* renewal-statistics chapter also develops general stationary renewal spectra. The present contribution is the exact finite-stage count, proof of simple Poisson-plateau crossings, disjoint frequency-localization windows, and the stage-identification ambiguity for this homogeneous family.

Published analyses of maxima of spectra for finite-state Markov observable processes are related, but not directly statements about the marked-jump point-process spectrum. The full cited Brandes text was examined including the unidirectional ring model and limiting spectral discussion. No exact all-finite-stage plateau-crossing count was identified there. This is a claim-to-literature comparison, not a guarantee of historical priority: general phase-type renewal theory could contain the same count in another formulation.

## Limitations

The count is not asserted for unequal stage rates, loops with branching, non-renewal counted jumps, correlated waiting times, or state-function autocorrelation spectra. The number of crossing bands alone cannot distinguish the two adjacent stage numbers stated by the theorem. A high-frequency level crossing should not be interpreted as a true dynamical eigenfrequency, and estimated spectra may fail to resolve all bands under finite sampling. Historical priority has not been independently certified; independent scientific audit has not been performed.

## References

1. Tobias Brandes, *Waiting Times and Noise in Single Particle Transport*, arXiv:0802.2233v1 (first posted 2008-02-15), https://arxiv.org/abs/0802.2233 ; *Annalen der Physik* **520** (2008), 477–496, https://doi.org/10.1002/andp.20085200707 . In particular, sections II.1, III.3, and III.3.2.
2. Wulfram Gerstner, Werner M. Kistler, Richard Naud, and Liam Paninski, *Neuronal Dynamics*, section 7.5 “Renewal statistics”, https://neuronaldynamics.epfl.ch/online/Ch7.S5.html (renewal event spectra).
3. Wang and Yang, *Peak frequencies and relative peak heights of power spectra of stationary irreversible Markov processes*, *Journal of Mathematical Physics* **66** (2025), https://doi.org/10.1063/5.0184974 (related state-observable spectra; not the same counted-jump event observable).
