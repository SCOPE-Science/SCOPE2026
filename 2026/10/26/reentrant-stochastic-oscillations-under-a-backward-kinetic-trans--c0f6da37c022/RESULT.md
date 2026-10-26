# Reentrant stochastic oscillations under a backward kinetic transition

## Finding
For a three-state continuous-time kinetic cycle with fixed forward transition rates \(a,b,c>0\) and a tunable reverse transition \(h\ge0\), increasing \(h\) strictly decreases the steady forward cycle current, yet can first **create** and then **destroy** damped population oscillations. This reentrant regime occurs if and only if
\[
c>(\sqrt a+\sqrt b)^2.
\]
There are two sharp exceptional-point rates
\[
h_{-}=c-(\sqrt a+\sqrt b)^2,\qquad
h_{+}=c-(\sqrt a-\sqrt b)^2,
\]
and the nonstationary eigenvalues are complex precisely for \(h\in(h_-,h_+)\cap[0,\infty)\). When the reentrant condition holds, the three phases are real-spectrum for \(0\le h<h_-\), complex-spectrum for \(h_-<h<h_+\), and real-spectrum for \(h>h_+\). The coalescences at \(h_\pm\) are genuine defective eigenvalues.

In the oscillatory phase, define the *spectral coherence ratio* as the angular frequency divided by the decay rate. For the reentrant regime it has a unique global maximizing backward rate
\[
h_*=c-a-b-\frac{2ab}{c},\qquad
\rho_* =\sqrt{\frac{ab}{c^2-ab}}.
\]
More generally, put
\[
c_0=(\sqrt a-\sqrt b)^2,\qquad
c_1=\frac{a+b+\sqrt{(a+b)^2+8ab}}2.
\]
If \(c\le c_0\), no nonnegative reverse rate produces an oscillatory mode. If \(c_0<c\le c_1\), the unique maximal coherence ratio occurs at \(h=0\); if \(c>c_1\), it occurs at the displayed strictly positive \(h_*\). The comparison uses \(\rho=0\) where the nonzero spectrum is real.

The assertions concern the entire specified parameter domain, including the exceptional boundaries, not just an asymptotic regime or selected numerical values.

## Assumptions and scope
There are three states indexed \(0,1,2\), with physical transitions \(0\to1\) at rate \(a\), \(1\to2\) at rate \(b\), \(2\to0\) at rate \(c\), and the controlled reverse step \(1\to0\) at rate \(h\). No other transitions occur. With row probability vectors evolving as \(p'(t)=p(t)Q\), the generator is
\[
Q=\begin{pmatrix}
-a&a&0\\
h&-(h+b)&b\\
c&0&-c
\end{pmatrix}.
\]
All three forward rates are fixed and strictly positive; \(h\) is any nonnegative real number. Irreducibility and a unique positive stationary distribution hold even at \(h=0\). By an oscillatory mode we mean a complex-conjugate pair among the two nonzero generator eigenvalues. This implies that the return probability from state \(0\), minus its stationary value, has infinitely many sign crossings in time. A real nonzero spectrum gives at most one such crossing. The coherence ratio is a spectral quantity, not a claim of sustained oscillation or of a thermodynamic quality factor.

## Proof
Set \(S=a+b+c\) and \(P=ab+ac+bc\). Expansion of the characteristic polynomial gives
\[
\det(zI-Q)=z\{z^2+(S+h)z+P+ch\}.
\]
The quadratic discriminant factors exactly as
\[
\mathcal D(h)=(S+h)^2-4(P+ch)
=(h-c+a+b)^2-4ab.
\]
Writing \(H=c-a-b\), the nonzero eigenvalues are
\[
\lambda_\pm=-\frac{S+h}{2}\pm\frac12\sqrt{(h-H)^2-4ab}.
\]
Since \(P+ch>0\) and \(S+h>0\), both nonzero eigenvalues have negative real part. The inequality \(\mathcal D(h)<0\) is equivalent to \(H-2\sqrt{ab}<h<H+2\sqrt{ab}\), which is precisely \(h_-<h<h_+\). This interval intersects \([0,\infty)\) with positive length exactly when \(h_+>0\), i.e., \(c>(\sqrt a-\sqrt b)^2\). It is bounded strictly away from \(h=0\) exactly when \(h_->0\), i.e., \(c>(\sqrt a+\sqrt b)^2\). These are necessary and sufficient, including the equality cases.

At either nonnegative exceptional rate, the two nonzero eigenvalues coincide at \(\lambda=-(S+h)/2<0\). If this eigenvalue were semisimple, \(Q\) would equal \(\lambda(I-\mathbf1\pi)\), where \(\mathbf1\) is the all-ones column and \(\pi\) is the strictly positive stationary row. But this would force \(Q_{02}=-\lambda\pi_2>0\), whereas \(Q_{02}=0\). Thus each such rate has a genuine size-two Jordan block on the nonstationary subspace, not two independent modes.

The stationary weights and directed cycle current are
\[
\pi=\frac{(c(b+h),ac,ab)}{c(b+h)+ac+ab},\qquad
J(h)=b\pi_1=c\pi_2=a\pi_0-h\pi_1
=\frac{abc}{c(b+h)+ac+ab}.
\]
The current derivative is strictly negative:
\[
J'(h)=-\frac{abc^2}{[c(b+h)+ac+ab]^2}<0.
\]
Thus the induction of damped oscillations in the reentrant regime occurs while the steady current is falling, not because the stationary circulation increases.

When \(\mathcal D(h)<0\), the decay rate and angular frequency are
\[
\gamma(h)=\frac{S+h}{2},\qquad
\omega(h)=\frac12\sqrt{4ab-(h-H)^2}.
\]
Consequently
\[
\rho(h)^2=\frac{4ab-(h-H)^2}{(S+h)^2},\qquad
\frac{d}{dh}\rho(h)^2
=\frac{4c(h_*-h)}{(S+h)^3},
\]
with \(h_*=H-2ab/c\). The derivative has exactly one possible sign change, from positive to negative. The threshold \(h_*>0\) is equivalent to \(c>c_1\), by solving \(c^2-(a+b)c-2ab>0\). For \(c>c_1\) one has \(c>\sqrt{ab}\), and
\[
h_*-h_-=2\sqrt{ab}\left(1-\frac{\sqrt{ab}}{c}\right)>0,\qquad
h_+-h_*=2\sqrt{ab}\left(1+\frac{\sqrt{ab}}{c}\right)>0.
\]
Hence \(h_*\) is inside the oscillatory interval and is its unique global spectral-coherence maximizer on \([0,\infty)\). Substitution gives \(\rho_*^2=ab/(c^2-ab)\). If \(c_0<c\le c_1\), then \(h_*\le0\), \(h=0\) lies inside the oscillatory interval, and the same derivative shows that \(h=0\) is the unique maximizer. If \(c\le c_0\), all coherence ratios are zero, so there is no unique coherence maximizer; only the no-oscillations claim is made for that case.

Finally, starting in state \(0\), the deviation \(P_{00}(t)-\pi_0\) is nonzero at \(t=0\). In the complex regime the entire two-dimensional nonstationary dynamics has eigenvalues \(-\gamma\pm i\omega\), so this deviation is \(e^{-\gamma t}(A\cos\omega t+B\sin\omega t)\) with \(A=1-\pi_0>0\), and consequently infinitely many crossings. Outside it the deviation is a combination of two real decaying exponentials or, at a defective boundary, \(e^{-\gamma t}(A+Bt)\); each can have at most one zero on \([0,\infty)\). This proves the asserted observable distinction.

## Verification
The standalone `verify_cycle.py` first checks the exact symbolic determinant, discriminant, balance, flux derivative, and coherence derivative identities, then independently diagonalizes 2,200 random generator matrices, solves 2,200 stationary distributions as linear systems, and checks 2,200 steady cycle currents. It also tests 900 independent parameter sets against dense numeric scans for the coherence maximizer, confirms 600 defective-boundary matrix ranks, and compares 900 exact transient formulas against matrix exponentials. All tests passed. The analytic characteristic polynomial, factorization, inequalities, and monotonicity arguments—not finite sampling—prove the complete statements.

A concrete reentrant case is \(a=b=1\), \(c=5\). It has \(h_-=1\), \(h_+=5\), \(h_*=13/5\), \(\rho_*=1/\sqrt{24}\), and strictly decreasing current \(J(h)=5/(11+5h)\). The eigenvalues are real at \(h=0\), nonreal at \(h=3\), and real again at \(h=6\).

Reproduce with `python verify_cycle.py` using Python, NumPy, SciPy, and SymPy.

## Relationship to prior work
Cycle-current and stochastic biochemical-kinetic models are established, including Qian's 2006 nonequilibrium statistical-thermodynamics review and Pressé et al.'s 2010 study of forward and backward biochemical cycles. Weber and Pande (2015) demonstrated damped population oscillations in a much larger, driven triangle network. Takahashi and Ohzeki (first public preprint September 28, 2015) analyzed three-state Markov generators and complex eigenvalues in a distinct fastest-relaxation problem. The present statement is not a new general eigenvalue formula, nor a claim that finite Markov cycles or complex modes were previously unknown. It instead gives the complete single-reverse-rate reentrant classification, its exceptional-point boundaries, and the unique coherence optimum jointly with strictly decreasing stationary current. The general three-state spectral framework is strongly relevant prior coverage; its implications for this specific one-parameter optimization and the independent historical literature should be reviewed before any external priority claim.

## Limitations
This is an ideal three-state linear continuous-time Markov model with an irreversible pair of forward edges; it does not model finite reverse rates at every link, thermal local-detailed-balance constraints, nonlinear feedback, multi-particle coupling, or sustained oscillations. The ratio \(\omega/\gamma\) is a spectral proxy for damped-cycle visibility; it is not optimized power, entropy production, period, or relaxation time. The observable return-probability crossings are exact in the ideal generator, not necessarily resolvable under measurement noise. Full text of Qian (2006) and Pressé et al. (2010) was not obtained during comparison; equivalent treatments there or in other specialist work remain a priority risk. Nothing here establishes priority over those inaccessible materials.

## References
- H. Qian, “Open-System Nonequilibrium Steady State: Statistical Thermodynamics, Fluctuations, and Chemical Oscillations,” *J. Phys. Chem. B* 110 (2006), 15063–15074, doi:10.1021/jp061858z (first online July 11, 2006).
- S. Pressé, K. Ghosh, R. Phillips, and K. A. Dill, “Dynamical fluctuations in biochemical reactions and cycles,” *Phys. Rev. E* 82 (2010), 031905, doi:10.1103/PhysRevE.82.031905.
- J. K. Weber and V. S. Pande, “Entropy-production-driven oscillators in simple nonequilibrium networks,” *Phys. Rev. E* 91 (2015), 032136, doi:10.1103/PhysRevE.91.032136.
- K. Takahashi and M. Ohzeki, “Optimization of Markov process violates detailed balance condition,” arXiv:1509.08212 (first public September 28, 2015); published as “Conflict between fastest relaxation of a Markov process and detailed balance condition,” *Phys. Rev. E* 93 (2016), 012129.
