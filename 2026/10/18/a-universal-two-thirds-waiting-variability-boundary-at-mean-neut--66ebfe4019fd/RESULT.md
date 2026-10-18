# A universal two-thirds waiting-variability boundary at mean-neutral resetting

## Finding
Consider diffusion on \([0,L]\) with generator \(D\partial_{xx}\), an absorbing target at \(0\), an initial point \(x\in(0,L)\), and \(D>0\). Compare a reflected particle at \(L\) (completion time \(T_{\mathrm{ref}}\)) with a boundary-reset particle (completion time \(T_{\mathrm{reset}}\)): every visit to \(L\) triggers an independent nonnegative holding time \(W\), after which the particle restarts at \(x\), until it reaches \(0\). The mean and variance of \(W\) are \(\tau\) and \(v\). Let
\[
\tau_*=\frac{(L-x)^2}{2D}.
\]
At the unique holding mean \(\tau=\tau_*\), both search protocols have exactly the same expected completion time, for every holding-time distribution with finite second moment:
\[
\mathbb E T_{\mathrm{reset}}=\mathbb E T_{\mathrm{ref}}=\frac{x(2L-x)}{2D}.
\]
Nonetheless their variances differ by the **exact identity**
\[
\boxed{\operatorname{Var}(T_{\mathrm{reset}})-\operatorname{Var}(T_{\mathrm{ref}})=\frac{x}{L-x}\left(v-\frac{2\tau_*^2}{3}\right).}
\]
Therefore the reset protocol strictly reduces, exactly preserves, or strictly increases first-passage variance according as the holding-time coefficient of variation is smaller than, equal to, or larger than \(\sqrt{2/3}\). This is a dimensionless and geometry-independent sharp boundary, despite mean neutrality. A deterministic hold lies below, an exponential hold above, and a gamma hold with shape \(3/2\) attains equality.

## Assumptions and scope
All Brownian excursions have generator \(D\partial_{xx}\) and absorb upon reaching either endpoint, except that a visit to \(L\) starts a holding period instead of terminating the search. The waiting periods are independent and identically distributed copies of a nonnegative random variable \(W\) with finite mean and finite variance, independent of all Brownian excursions. After each hold the particle relocates instantly to the same \(x\). Reflection in the comparison model is instantaneous and normal. There is no resetting in the interior. The target at \(0\) is fully absorbing. The claim is for every real \(L>0\), \(D>0\), and \(0<x<L\), with all relevant second moments finite. \(W\) may have atoms, including a deterministic law.

## Proof
Write \(E\) for the exit time of Brownian motion from the open interval \((0,L)\), with *both* endpoints absorbing, and let \(J\) indicate that this first exit is at \(L\). Its right-exit probability is \(q=x/L\); thus eventual success at the left target has probability \(1-q>0\) in each cycle. The exit-time moment functions solve their standard boundary-value problems (with all displayed values evaluated at the starting point \(x\)):
\[
\begin{aligned}
 u&=\mathbb E E=\frac{x(L-x)}{2D},\\
 h&=\mathbb E(EJ)=\frac{x(L^2-x^2)}{6DL},\\
 u_2&=\mathbb E E^2=\frac{x(L-x)(L^2+Lx-x^2)}{12D^2}.
\end{aligned}
\]
Indeed, \(D u''=-1\), \(D h''=-x/L\), and \(D u_2''=-2u\) on \((0,L)\), with zero endpoint conditions. The equation for \(h\) follows from the Markov property: the conditional future probability of right exit, upon surviving to an intermediate position \(y\), equals \(y/L\).

For the reflecting comparison, the first two raw moments solve \(D m_R''=-1\) and \(D M_R''=-2m_R\), with zero values at \(0\) and zero derivatives at \(L\). This gives
\[
 m_R=\frac{x(2L-x)}{2D},\qquad
 M_R=\frac{x(2L-x)(4L^2+2Lx-x^2)}{12D^2}.
\]
These polynomial functions satisfy the equations and all boundary conditions; uniqueness of the corresponding linear boundary-value problems identifies them as the moments.

The reset-model completion time obeys the regenerative distributional identity
\[
 T_{\mathrm{reset}}\stackrel{d}{=}E+J(W+T'_{\mathrm{reset}}),
\]
where \(T'_{\mathrm{reset}}\) is an independent copy, independent also of \((E,J)\) and \(W\). The number of cycles is geometric with success probability \(1-q\); since an excursion has finite second moment and \(W\) does too, so does \(T_{\mathrm{reset}}\). Taking the first moment yields
\[
 m_S=\frac{u+q\tau}{1-q}=\frac{xL}{2D}+\frac{x\tau}{L-x}.
\]
Consequently \(m_S-m_R=\frac{x}{L-x}(\tau-\tau_*)\), proving uniqueness of the mean-neutral \(\tau_*\).

Squaring the regenerative identity gives the second raw moment
\[
 M_S=\frac{u_2+2h(\tau+m_S)+q(\tau^2+v+2\tau m_S)}{1-q}.
\]
Substitute the explicit \(u,h,u_2\) and \(\tau=\tau_*\); then \(m_S=m_R\). Exact polynomial simplification gives
\[
 M_S-M_R=\frac{x}{L-x}\left(v-\frac{(L-x)^4}{6D^2}\right),
\]
which is the claimed variance difference, since the squared means cancel. Using \(\tau_*^2=(L-x)^4/(4D^2)\), the variance changes sign precisely at \(v/\tau_*^2=2/3\), with a strictly positive prefactor. For \(v=0\), \(W=\tau_*\) is deterministic; for \(v=\tau_*^2\), \(W\) may be exponential; and the \(\operatorname{Gamma}(3/2,2\tau_*/3)\) distribution has \(v=2\tau_*^2/3\). All three regimes, including the equality case, are realized by admissible laws.

## Verification
The included `verify.py` checks every displayed boundary-value differential equation and boundary condition symbolically, reconstructs the first two regenerative moments, and simplifies the variance difference exactly. Independently, the killed-diffusion Laplace transforms are
\[
 A(s)=\frac{\sinh(\sqrt{s/D}(L-x))}{\sinh(\sqrt{s/D}L)},\qquad B(s)=\frac{\sinh(\sqrt{s/D}x)}{\sinh(\sqrt{s/D}L)}.
\]
For \(\phi(s)=\mathbb E e^{-sW}\), the reset-completion transform is \(A(s)/(1-B(s)\phi(s))\). The reflected-completion transform is \(\cosh(\sqrt{s/D}(L-x))/\cosh(\sqrt{s/D}L)\). The script independently expands these four transforms to second order at \(s=0\), reproduces all first and second moments, and tests twelve exact rational parameter/variability combinations. Run `python verify.py` with Python 3 and SymPy installed. These finite and symbolic checks supplement, but do not replace, the analytic proof.

## Relationship to prior work
Chen and Bressloff's 2026 study of **two-dimensional** search with non-target sticky boundary-induced resetting motivates the physical comparison against reflection and develops the renewal/MFPT methodology [1]. Here the explicitly stated new classification is instead for a **one-dimensional interval**, and it concerns the complete second-moment tradeoff at the unique *equal-MFPT* waiting mean. The present proof uses standard killed-Brownian boundary-value formulas and regenerative renewal identities as prerequisites; neither is claimed new. García-Valladares, Gupta, Prados and Plata study refractory time after **spontaneous** reset events rather than boundary-triggered resets [2]. Bressloff and Linn study sticky-target adsorption/desorption for a run-and-tumble particle, also under a different protocol [3]. Georgiou, Bressloff and Bertrand study a finite-interval active Ornstein–Uhlenbeck particle with resetting and low-order first-passage moments, but not this boundary-triggered passive Brownian protocol [4]. In the accessible abstracts of these sources the precise mean-neutral waiting-variance threshold is not stated. This comparison is limited by restricted full-text access (see below).

## Limitations
The theorem is restricted to passive drift-free Brownian excursions on one dimension, a single absorbing target at one endpoint, a non-target reset wall at the other, and iid independent holding periods. It makes no assertion for higher-dimensional small-target domains, arbitrary drift, coupled waiting periods, or infinite waiting-time variance. Several relevant 2026 primary full texts were not retrievable in this investigation despite attempts at open-access retrieval; in particular, the title, abstract and metadata of [1], but not its full body or appendices, were accessible. Implicit or non-indexed prior derivations remain an originality risk. No independent external mathematical audit has been carried out.

## References
1. K. Chen and P. C. Bressloff, *2D target search with boundary-induced resetting*, arXiv:2609.31085v1 (first public 2026-09-25), https://arxiv.org/abs/2609.31085 .
2. G. García-Valladares, D. Gupta, A. Prados and C. A. Plata, *Stochastic resetting with refractory periods: pathway formulation and exact results*, Physica Scripta (2024), DOI: 10.1088/1402-4896/ad317b .
3. P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, Physical Review E 113, 054122 (2026), DOI: 10.1103/dcnh-bhwc .
4. D. K. Georgiou, P. C. Bressloff and T. Bertrand, *Persistence, resetting, and first-passage times of an active Ornstein--Uhlenbeck particle*, arXiv:2609.21124v1 (2026), https://arxiv.org/abs/2609.21124 .
