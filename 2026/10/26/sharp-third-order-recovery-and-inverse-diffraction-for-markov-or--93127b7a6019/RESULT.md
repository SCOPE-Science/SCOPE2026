# Sharp third-order recovery and inverse diffraction for Markov-oriented close-packed dimers

## Finding
Let \(m,\rho\) be the two parameters of the stationary Markov-dimer ensemble defined below. Its diffraction uniquely determines the transition eigenvalue \(\rho\) and the absolute orientation bias \(|m|\), but cannot determine the sign of \(m\). The first possible signed third-order measurement occurs at spatial diameter three:
\[
C_{013}:=\mathbb E[W_0W_1W_3]=\frac12m(1-m^2)(1-\rho)^2.
\]
The triple \((0,1,2)\) has correlation zero for every parameter choice, whereas \(C_{013}\) is nonzero whenever \(m\ne0\). The shortest informative triple is therefore sharp. Moreover, over the full irreducible aperiodic two-state Markov family, the largest achievable absolute value of this shortest informative triple is
\[
\boxed{\sup_{m,\rho}|C_{013}|=6-4\sqrt2,}
\]
with equality **exactly** at
\[
(m,\rho)=(\sqrt2-1,-(\sqrt2-1))\quad\text{or}\quad(m,\rho)=(1-\sqrt2,-(\sqrt2-1)).
\]
At these extremizers the underlying transition matrix has one zero off-diagonal complement (a deterministic jump in one direction) but remains irreducible and aperiodic. The equality statement includes the physically meaningful boundary of the primitive Markov family.

The complete diffraction is
\[
\widehat\gamma=m^2\sum_{k\in\mathbb Z}\delta_{k+1/2}+(1-m^2)\,\frac{(1-\cos2\pi t)(1-\rho^2)}{1+\rho^2-2\rho\cos4\pi t}\,dt.
\]
Thus the pure-point mass at each half integer is \(B=m^2\). With \(\eta(2)\) the spatial autocorrelation at displacement two, recover
\[
\rho=\frac{\eta(2)-B}{1-B},\qquad
m=\frac{2C_{013}}{(1-B)(1-\rho)^2}.
\]
Consequently the inverse-diffraction fiber is exactly \(\{(m,\rho),(-m,\rho)\}\) for nonzero \(m\), and a singleton for \(m=0\). The pair \((\widehat\gamma,C_{013})\) identifies every admissible Markov-dimer law.

## Assumptions and scope
Let \((S_j)_{j\in\mathbb Z}\) be a stationary binary Markov chain with values \(\{-1,+1\}\), stationary mean \(m\in(-1,1)\), and transition law
\[
\Pr(S_{j+1}=t\mid S_j=s)=\frac{1+t[m+\rho(s-m)]}{2},\qquad s,t\in\{-1,+1\}.
\]
The exact admissible primitive regime is
\[
-\frac{1-|m|}{1+|m|}\le\rho<1,\qquad \rho>-1.
\]
These conditions allow one zero transition, but guarantee irreducibility and aperiodicity. Independently let \(\theta\) be uniform on \(\{0,1\}\) and form the stationary two-sided sequence
\[
W_{\theta+2j}=S_j,\qquad W_{\theta+2j+1}=-S_j\quad (j\in\mathbb Z).
\]
The associated scattering comb is \(\omega=\sum_{n\in\mathbb Z}W_n\delta_n\). All expectations are with respect to the stationary Markov measure and independent uniform dimer phase. Diffraction is the Fourier transform of \(\gamma=\sum_{n\in\mathbb Z}\eta(n)\delta_n\), using the convention \(\widehat f(t)=\int e^{-2\pi i tx}f(x)\,dx\), and is periodic of period one as a measure on real frequency space. At the special unbiased uncorrelated point \((m,\rho)=(0,0)\), this reduces to the previously studied fair independent dimer model. No claim is made for the degenerate transition endpoints \(\rho=1\) or \((m,\rho)=(0,-1)\), where Markov mixing fails.

## Proof
**1. Stationarity and correlations.** The two-state transition law has stationary distribution \(\Pr(S_j=s)=(1+ms)/2\); it is reversible because every stationary two-state chain satisfies detailed balance. On centered observables, its transition operator has eigenvalue \(\rho\). Consequently, for every integer \(k\ge0\),
\[
r_k:=\mathbb E(S_0S_k)=m^2+(1-m^2)\rho^k.
\]
The phase-uniform dimer process is stationary. Its square shift restricts on each phase to the mixing Markov chain; since a unit shift exchanges the two phases, the full shift is ergodic. The ergodic theorem gives almost-sure autocorrelation coefficients \(\eta(n)=\mathbb E(W_0W_n)\). Enumerating the two phases gives, for \(k\ge0\),
\[
\eta(2k)=r_k,\qquad \eta(2k+1)=-\frac{r_k+r_{k+1}}2,
\]
with \(\eta(-n)=\eta(n)\). In particular, \(\eta(2)=m^2+(1-m^2)\rho\).

**2. Diffraction and inverse fibers.** Separate \(\eta(n)=m^2(-1)^n+\eta_c(n)\). The transform of the first term is \(m^2\sum_{k\in\mathbb Z}\delta_{k+1/2}\). The standard absolutely convergent Poisson-kernel identity, valid because \(|\rho|<1\), is
\[
\sum_{k\in\mathbb Z}\rho^{|k|}e^{4\pi ikt}
=\frac{1-\rho^2}{1+\rho^2-2\rho\cos4\pi t}.
\]
Multiplication by \(1-\cos2\pi t\) yields Fourier coefficients \((1-m^2)\rho^k\) at positive even displacement \(2k\) and \(-\frac12(1-m^2)(\rho^k+\rho^{k+1})\) at odd displacement \(2k+1\), exactly \(\eta_c\). This proves the displayed measure identity. Its mutually singular Lebesgue and atomic parts determine \(B=m^2\); Fourier inversion of the measure determines \(\eta(2)\). Since \(|m|<1\), the displayed inverse formula determines \(\rho\). Conversely, the formula plainly depends only on \(m^2\) and \(\rho\), so these are the complete diffraction equivalence classes.

**3. The first phase-sensitive triple.** Every one-site mean vanishes because the two sites of each dimer have opposite signs and the phase is uniform. Hence any product with repeated indices reduces to a one-site mean or pair statistic and cannot recover the bias sign. For three distinct sites at diameter at most two, the only pattern up to translation is \((0,1,2)\). In each phase its product has expectation zero after averaging the two phases, directly: phase zero gives \(-S_0S_1\cdot S_0=-S_1\), while phase one gives \((-S_{-1})S_0(-S_0)=S_{-1}\). Both have respective expectations \(-m\) and \(m\).

At \((0,1,3)\), the phase-zero product is \(S_1\), whereas the phase-one product is \(-S_{-1}S_0S_1\). By reversible Markov conditional independence of past and future given \(S_0\),
\[
\mathbb E(S_{-1}S_0S_1)=\mathbb E\!\left[S_0\left(m(1-\rho)+\rho S_0\right)^2\right]
=m^3(1-\rho)^2+2m\rho(1-\rho)+m\rho^2.
\]
Subtracting from \(m\) and dividing by two gives \(C_{013}=\frac12m(1-m^2)(1-\rho)^2\). Its sign is the sign of \(m\) throughout the stated domain. This proves the sharp minimal diameter, the signed inverse formula, and identification by diffraction plus one triple.

**4. Universal sharp third-order bound.** Set \(s=|m|\in[0,1)\). Admissibility implies \(1-\rho\le2/(1+s)\), so
\[
|C_{013}|\le\frac{s(1-s^2)}2\left(\frac2{1+s}\right)^2
=\frac{2s(1-s)}{1+s}.
\]
The right-hand side has derivative \(2(1-2s-s^2)/(1+s)^2\), vanishes uniquely at \(s=\sqrt2-1\), and its maximum is \(6-4\sqrt2\). Equality requires \(\rho=-(1-s)/(1+s)=-(\sqrt2-1)\), giving precisely the two stated parameter pairs. Since \(s>0\), the lower-bound transition is irreducible and aperiodic (one directed transition is certain while the other state retains a positive self-loop). Both maximizers are admissible, establishing attainment rather than merely a supremum.

## Verification
The standalone `verify.py` enumerates finite stationary two-state Markov paths using exact rational arithmetic rather than stochastic simulation. It independently evaluates 130 spatial autocorrelation instances, 30 three-site identities, Markov stationarity and transition normalization, and the inversion formulas at ten rational parameter samples, including two primitive boundary cases with one zero transition. Running `python3 verify.py` produced:

`VERIFY_OK: 10 rational Markov laws; 40 transition probabilities; 130 exact autocorrelation/Fourier identities (including primitive boundary cases); 30 three-site identities; complete signed-parameter inversion at all samples`

The universal bound and extremizer classification are proved symbolically above; the finite rational tests are supplementary and are not claimed to verify all real parameters.

## Relationship to prior work
Baake and van Enter's close-packed dimer example (arXiv:1011.1628v1) supplies the unbiased, independent special case and the underlying hidden period-two dynamical factor. Their one-step two-point calculation is not claimed as new. Baake and Höffe (arXiv:math-ph/9904005) treat diffraction of much more general stochastic tilings and Markov systems; their spectral framework can obtain general Markov two-point formulas and dominates the standard spectral derivation here. The distinct statement assessed in this work is the **complete inverse-diffraction ambiguity for the explicitly parameterized correlated dimer family together with the minimal third-order signed-recovery window and its attained sharp global constant**. General phase ambiguity and the use of higher correlations to distinguish homometric structures were previously known, including from Baake and Grimm's 2008 discussion; no blanket novelty is claimed for those principles. A full earlier derivation in a differently parameterized Markov scattering model remains a priority risk.

## Limitations
The theorem is limited to real-valued binary weights, nearest-neighbor stationary reversible two-state Markov orientations, and a uniform random dimer phase. It does not characterize more general hidden Markov orientation processes, different scattering amplitudes, noisy finite-sample recovery, or the nonprimitive endpoint chains. The identification formula needs the *signed* third-order correlation; diffraction alone does not determine the orientation sign. This is a mathematical statement about stationary ensemble spatial diffraction, not a temporal mixing-rate classification. Mathematical checks are internal and do not constitute independent audit or historical-priority certification.

## References
1. M. Baake and A. van Enter, *Close-packed dimers on the line: diffraction versus dynamical spectrum*, arXiv:1011.1628v1, first public 2010-11-07; *J. Stat. Phys.* **143** (2011), 88–101.
2. M. Baake and M. Höffe, *Diffraction of random tilings: some rigorous results*, arXiv:math-ph/9904005, 1999.
3. M. Baake and U. Grimm, *Can Kinematic Diffraction Distinguish Order from Disorder?*, arXiv:0810.5750, 2008.
4. M. Baake, M. Birkner and R. V. Moody, *Diffraction of stochastic point sets: explicitly computable examples*, arXiv:0803.1266, 2008.
