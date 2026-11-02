# Sharp triplet collapse in the two-fluctuator Kubo lineshape

## Finding
Let two independent stationary symmetric random-telegraph processes take the values \(\pm1\), each changing sign at Poisson rate \(\gamma>0\). Their equal frequency shifts have magnitude \(v>0\). Define the normalized intrinsic optical lineshape by
\[
L_{v,\gamma}(\omega)=\frac1\pi\operatorname{Re}\int_0^\infty e^{i\omega t}\,\mathbb E\exp\!\left(iv\int_0^t[\xi_1(s)+\xi_2(s)]\,ds\right)dt,
\qquad \omega\in\mathbb R.
\]
Set
\[
q_* = \sqrt{\frac{24\sqrt{15}-53}{343}}=0.34128722336301964\ldots.
\]
If \(0<\gamma/v<q_*\), the spectrum has **exactly three strict local maxima**: one at \(\omega=0\) and two symmetric nonzero maxima, separated from the central peak by two strict local minima. If \(\gamma/v>q_*\), its only stationary maximum is the strict central maximum and the spectrum strictly decreases as \(|\omega|\) increases. At equality there is only the central local maximum, but also two nonzero stationary horizontal shoulders, neither maxima nor minima. In particular, no regime with exactly two local maxima is possible.

The spectrum itself is explicitly
\[
L_{v,\gamma}(\omega)=\frac{4\gamma v^2(\omega^2+16\gamma^2+4v^2)}{\pi(\omega^2+4\gamma^2)[(\omega^2-4v^2)^2+16\gamma^2\omega^2]}.
\]
At the threshold the shoulders are situated at \(|\omega|=v\sqrt{(8-20q_*^2)/3}\), approximately \(1.374828549720923v\).

## Assumptions and scope
Each \(\xi_j\) is an independent stationary continuous-time Markov chain with states \(\pm1\) and jump rate \(\gamma\) in either direction. Thus the initial sign pair is uniform on four possibilities. Frequencies are measured relative to their unperturbed carrier; there is no additional homogeneous linewidth, instrumental convolution, asymmetric switching, or inequality of the two modulation amplitudes. The result concerns the stationary ensemble-averaged intrinsic spectral density and all real detunings, not individual finite-time realizations. Both \(v\) and \(\gamma\) are strictly positive; at exactly zero switching the spectrum is discrete and the classification of smooth local peaks does not apply.

## Proof
For one fluctuator, stationary averaging of the integrated phase gives \(f''+2\gamma f'+v^2f=0\), with \(f(0)=1\), \(f'(0)=0\). Independence gives the phase relaxation function \(C(t)=f(t)^2\) for nonnegative \(t\). The two characteristic roots of the single-fluctuator equation have negative real parts for \(\gamma,v>0\); hence \(C\) is integrable.

Set \(U=f^2\), \(V=ff'\), \(W=(f')^2\). The closed system
\[
U'=2V,\quad V'=W-2\gamma V-v^2U,\quad W'=-4\gamma W-2v^2V
\]
with \((U,V,W)(0)=(1,0,0)\) yields the exact Laplace transform
\[
\widehat C(s)=\frac{s^2+6\gamma s+8\gamma^2+2v^2}{(s+2\gamma)(s^2+4\gamma s+4v^2)}\qquad(\operatorname{Re}s>0).
\]
Continuity to \(s=-i\omega\) is legitimate because of exponential decay. Taking its real part establishes the displayed rational spectrum. As the Fourier transform of a stationary phase-correlation function with \(C(0)=1\), it is a nonnegative probability density on frequencies, integrating to one.

Write \(t=(\gamma/v)^2>0\) and \(z=(\omega/v)^2\ge0\). Apart from the positive factor \(4\sqrt t/(\pi v)\), the spectrum is
\[
h_t(z)=\frac{z+16t+4}{(z+4t)[(z-4)^2+16tz]}.
\]
Both denominator factors are strictly positive for \(t>0\), \(z\ge0\). Direct differentiation yields
\[
h_t'(z)=-\frac{2P_t(z)}{(z+4t)^2[(z-4)^2+16tz]^2},
\]
where
\[
P_t(z)=z^3+(34t+2)z^2+(320t^2-48t-32)z+512t^3-128t^2+32t+32.
\]
Crucially,
\[
P_t'(z)=3(z+16t+4)\left(z-\frac{8-20t}{3}\right),
\qquad P_t(0)=32[t(16t^2-4t+1)+1]>0.
\]
If \(t\ge2/5\), the polynomial is strictly increasing on \(z>0\) and stays positive. If \(0<t<2/5\), it decreases to its unique positive minimum at \(z_m=(8-20t)/3\), then increases. At that point,
\[
P_t(z_m)=-\frac{32}{27}(t-1)(343t^2+106t-17).
\]
Since \(t-1<0\), the minimum is negative precisely when \(343t^2+106t-17<0\). The quadratic has exactly one positive zero
\[
t_* = \frac{24\sqrt{15}-53}{343} \in (0,2/5).
\]
For \(0<t<t_*\), \(P_t\) therefore has exactly two distinct positive zeros, giving a strict local minimum then a strict local maximum of \(h_t\) on \(z>0\), or two symmetric minima and two symmetric side maxima in \(\omega\). Positivity of \(P_t(0)\) makes the central line a strict local maximum for all \(t>0\). For \(t>t_*\), \(P_t>0\) on \(z\ge0\), so there are no off-center extrema. At \(t=t_*\), the minimum of \(P_t\) is a double positive zero, leaving a horizontal stationary shoulder but no sign change of \(h_t'\). These cases exhaust all admissible parameters.

## Verification
Run `python3 check_spectrum.py` with Python 3 and NumPy. The verifier constructs the independent four-state telegraph Markov generator, evaluates its complex matrix resolvent, and checks 390 detuning/parameter combinations against the closed spectral density. It also checks derivative factorizations and root-count transitions on both sides of the exact threshold. In its recorded execution, all comparisons passed, with maximum normalized discrepancy \(1.0620\times10^{-15}\). Numerical tests corroborate but do not replace the polynomial sign proof.

## Relationship to prior work
Random-frequency modulation and exchange narrowing were introduced by Anderson (1954) and developed by Kubo. Wódkiewicz, Shore and Eberly (1984) formulated pre-Gaussian spectra for a sum of independent dichotomous fluctuators; their general construction supplies the underlying relaxation functions. Berthelot and collaborators (2010), in an accessible complete treatment, write the independent-fluctuator relaxation function as a product and discuss the doublet-to-singlet crossover for a single fluctuator and the many-fluctuator Gaussian limit. The present statement isolates a different, finite two-fluctuator **triplet-to-singlet** morphology and gives its exact, unique algebraic boundary and stationary-point count. It does not claim the underlying product correlation function, resolvent framework, or qualitative motional narrowing as new.

## Limitations
The result is exact for identical independent symmetric Poisson fluctuators without an extra Lorentzian or instrumental convolution. Unequal couplings or switching rates, additional broadening, finite observation windows, fluorescence under strong driving and quantitative detection thresholds can change the peak pattern. Historical priority is provisional: the complete text of the highly relevant 1984 pre-Gaussian paper was not available for comparison, although its abstract, preview page and figure descriptions were examined; the exact two-fluctuator threshold might have been analyzed elsewhere. No independent scientific audit has been performed.

## References
1. P. W. Anderson, *A Mathematical Model for the Narrowing of Spectral Lines by Exchange or Motion*, Journal of the Physical Society of Japan 9 (1954), 316–339, DOI: 10.1143/JPSJ.9.316.
2. K. Wódkiewicz, B. W. Shore and J. H. Eberly, *Pre-Gaussian noise in strong laser–atom interactions*, Journal of the Optical Society of America B 1 (1984), 398–405, DOI: 10.1364/JOSAB.1.000398.
3. A. Berthelot et al., *From Random Telegraph to Gaussian Stochastic Noises: Decoherence and Spectral Diffusion in a Semiconductor Quantum Dot*, Advances in Mathematical Physics 2010 (2010), 494738, DOI: 10.1155/2010/494738.
4. M. Blume, *Stochastic Theory of Line Shape: Generalization of the Kubo-Anderson Model*, Physical Review 174 (1968), 351, DOI: 10.1103/PhysRev.174.351.
