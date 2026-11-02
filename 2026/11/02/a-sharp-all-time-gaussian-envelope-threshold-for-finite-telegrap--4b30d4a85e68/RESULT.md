# A sharp all-time Gaussian envelope threshold for finite telegraph dephasing baths

## Finding
Fix an integer \(N\geq1\), a switching-relaxation rate \(k>0\), and a total noise standard deviation \(\sigma>0\). Let \(\epsilon_1,\ldots,\epsilon_N\) be independent stationary symmetric continuous-time Markov chains on \(\{-1,+1\}\), each changing sign at rate \(k/2\). Set
\[
Z_N(t)=\frac{\sigma}{\sqrt N}\sum_{j=1}^{N}\epsilon_j(t),\qquad
F_N(t)=\mathbb E\exp\!\left(i\int_0^t Z_N(u)\,du\right).
\]
Let \(G(t)\) be the corresponding characteristic functional for a *stationary centered Gaussian Ornstein–Uhlenbeck bath* with the exactly matching autocovariance \(\sigma^2e^{-k|u|}\). Then \(G(t)>0\) for \(t\geq0\), and the following is a necessary-and-sufficient classification:
\[
\boxed{\ |F_N(t)|<G(t)\text{ for every }t>0\quad\Longleftrightarrow\quad
\frac{\sigma^2}{Nk^2}\leq\frac12.\ }
\]
Above the sharp threshold, \(\sigma^2/(Nk^2)>1/2\), there are *arbitrarily large* times at which \(|F_N(t)|>G(t)\), and also arbitrarily large times at which \(F_N(t)=0\). For every positive parameter choice, the short-time comparison starts in the opposite direction:
\[
F_N(t)-G(t)=-\frac{\sigma^4}{12N}t^4+O(t^5)\qquad(t\downarrow0).
\]
Thus at fixed total variance and switching rate, the Gaussian comparator dominates the entire finite-ensemble coherence envelope precisely for integer counts \(N\geq\lceil2\sigma^2/k^2\rceil\). The all-time ordering threshold differs from the onset of oscillatory single-source coherence, which occurs already at \(\sigma^2/(Nk^2)=1/4\).

## Assumptions and scope
All processes are stationary from the initial observation time, noise is classical, and coupling is longitudinal pure dephasing with unit phase-coupling coefficient (a different coupling can be absorbed into \(\sigma\)). Each Markov spin switches independently at rate \(k/2\); consequently both noises have precisely the same autocovariance \(\mathbb E[Z_N(0)Z_N(t)]=\sigma^2e^{-k|t|}\). The Gaussian comparator is the unique centered stationary Gaussian Ornstein–Uhlenbeck process with this covariance. There is no additional control pulse, spontaneous-emission factor, or time-dependent coupling. The conclusion compares absolute Ramsey coherence, not scattering intensity or trace-distance non-Markovianity.

## Proof
Write \(\tau=kt\) and \(s=\sigma^2/(Nk^2)>0\). Independence gives \(F_N(t)=f_s(\tau)^N\), where the one-spin Feynman–Kac generator is \(\begin{psmallmatrix}-1/2+i\sqrt{s}&1/2\\1/2&-1/2-i\sqrt{s}\end{psmallmatrix}\) and
\[
f_s''+f_s'+sf_s=0,\quad f_s(0)=1,\quad f_s'(0)=0.
\]
The matched Gaussian envelope is \(G(t)=g_s(\tau)^N\), with
\[
g_s(\tau)=\exp\{-s(\tau-1+e^{-\tau})\}.
\]
Hence it is enough to compare \(|f_s|\) with \(g_s\). The exponential functional formulas follow respectively by two-state Feynman–Kac and by the Gaussian characteristic-functional identity \(\mathbb E e^{i\int X}=e^{-\operatorname{Var}(\int X)/2}\).

**(I) Nonoscillatory region \(0<s\leq1/4\).** The explicit solution \(f_s=e^{-\tau/2}[\cosh(d\tau/2)+d^{-1}\sinh(d\tau/2)]\), with \(d=\sqrt{1-4s}\), is positive (the continuous \(d=0\) case is understood). Direct differentiation yields
\[
(\partial_\tau^2+\partial_\tau+s)g_s
=s^2(1-e^{-\tau})^2g_s>0\quad(\tau>0).
\]
The causal Green kernel of \(\partial_\tau^2+\partial_\tau+s\) is strictly positive for \(s\leq1/4\). Since \(g_s-f_s\) has zero Cauchy data and a strictly positive forcing, its Green representation gives \(0<f_s(\tau)<g_s(\tau)\) for every \(\tau>0\).

**(II) Oscillatory but Gaussian-dominated region \(1/4<s\leq1/2\).** Put \(q=\sqrt{4s-1}\in(0,1]\), \(R=\sqrt{1+q^{-2}}\), and \(\phi=\arctan(1/q)\). Then
\[
f_s(\tau)=e^{-\tau/2}R\cos(q\tau/2-\phi),
\]
and its first positive zero is \(T_0=(\pi+2\phi)/q\geq3\pi/(2q)\). Before this zero \(f_s>0\). Let \(h=-f_s'/f_s\), \(h_G=-g_s'/g_s=s(1-e^{-\tau})\). Their difference \(w=h-h_G\) solves
\[
w'=(h+h_G-1)w+h_G^2,\qquad w(0)=0.
\]
An integrating factor gives \(w>0\) at every \(0<\tau<T_0\), so \(f_s/g_s\) decreases strictly from one.

For \(\tau\geq T_0\), the absolute ratio is bounded above by
\[
H(\tau)=R\exp\{(s-1/2)\tau-s(1-e^{-\tau})\},
\]
which strictly decreases for \(s\leq1/2\). To show \(H(T_0)<1\), set \(d_0=1-e^{-3\pi/2}\) and \(A=3\pi/8-1/2>0\). Using \(-\log q\leq(1-q^2)/(2q)\), \(\log R=\frac12\log(1+q^2)-\log q\), and the bound on \(T_0\), one obtains
\[
\log H(T_0)\leq\tfrac12\log2-A(q^{-1}-q)-\tfrac{d_0}{4}(1+q^2)<0.
\]
Indeed \(A(q^{-1}-q)+d_0(1+q^2)/4\) decreases with \(q\in(0,1]\) (its derivative is at most \(-2A+d_0/2<0\)); its minimum is \(d_0/2>\log2/2\). Thus \(|f_s|<g_s\) also after the first zero, including \(s=1/2\).

**(III) Strong region \(s>1/2\).** Now \(q=\sqrt{4s-1}>1\), with the same oscillatory formula. At each sequence \(\tau_m=2(\phi+m\pi)/q\to\infty\), \(|\cos(q\tau_m/2-\phi)|=1\), and
\[
\log\frac{|f_s(\tau_m)|}{g_s(\tau_m)}
=\log R+(s-1/2)\tau_m-s(1-e^{-\tau_m})\longrightarrow+\infty.
\]
Consequently the telegraph magnitude exceeds the Gaussian envelope at arbitrarily late times. The cosine has infinitely many positive zeros, at which the opposite strict inequality holds. Finally, the ODE and Gaussian formula give \(f_s^{(4)}(0)=s^2-s\), \(g_s^{(4)}(0)=3s^2-s\). Their first three derivatives coincide, hence \(F_N-G=-N(2s^2)(kt)^4/24+O(t^5)=-\sigma^4t^4/(12N)+O(t^5)\). This completes the necessary-and-sufficient proof.

## Verification
The standalone `check_coherence.py` checks the one-spin solution independently against a two-state matrix exponential, the Gaussian exponent against numerical covariance integration, the comparison on grids spanning both regions and multiple \(N\), and analytic auxiliary inequalities. Running `python check_coherence.py` completed 3229 deterministic comparisons/inequalities successfully. These finite checks supplement the analytic argument; they do not certify its universal quantifiers.

## Relationship to prior work
Bogaczewicz and Machnikowski, *Resonance fluorescence of noisy systems* (arXiv:2303.01531, first version 2023-03-02), calculate scattering under finite-state Markov and multiple independent telegraph noise sources; their source supplies the experimentally motivated finite-to-Gaussian setup, not the stated global comparator threshold. Berthelot and collaborators (2010) give the established telegraph relaxation function, its product rule, and its Gaussian limit. Ramos and García-Ripoll (2018) relate scattering spectra to exact Ramsey envelopes and include telegraph and Gaussian models. Cai (2020) examines Markovianity and revivals under random telegraph dephasing, a different threshold property. These publications establish the forward formulas and motivating physical effects; the all-time strict comparison with a covariance-matched Gaussian envelope, including the sharp \(1/2\) crossing criterion and critical equality, is the evaluated additional claim. The present result does not claim new forward solutions.

## Limitations
The proof assumes identical symmetric two-state Markov fluctuators at a common switching rate and equal rescaled coupling. It does not apply to asymmetric telegraphs, heterogeneous rates, nonstationary preparations, quantum baths, arbitrary pulse controls, or experimentally finite-frequency/finite-time sampling without additional analysis. A full-spectrum formula exists in the prior literature; the mathematical priority of this global inequality is assessed from inspected literature and searches, not guaranteed by them. The theorem is a model-specific mathematical comparison, not an independent experimental validation.

## References
1. R. A. Bogaczewicz and P. Machnikowski, *Resonance fluorescence of noisy systems*, arXiv:2303.01531 (first public version 2023-03-02), https://arxiv.org/abs/2303.01531.
2. A. Berthelot et al., *From Random Telegraph to Gaussian Stochastic Noises: Decoherence and Spectral Diffusion in a Semiconductor Quantum Dot*, Advances in Mathematical Physics 2010, 494738, https://doi.org/10.1155/2010/494738.
3. T. Ramos and J. J. García-Ripoll, *Correlated Dephasing Noise in Single-photon Scattering*, arXiv:1806.08402, https://arxiv.org/abs/1806.08402.
4. X. Cai, *Quantum dephasing induced by non-Markovian random telegraph noise*, Scientific Reports 10, 88 (2020), https://doi.org/10.1038/s41598-019-57081-8.
