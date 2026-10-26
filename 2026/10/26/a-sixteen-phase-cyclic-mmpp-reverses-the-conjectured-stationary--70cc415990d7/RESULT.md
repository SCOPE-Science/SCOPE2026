# A sixteen-phase cyclic MMPP reverses the conjectured stationary waiting-time order

## Finding

There is an irreducible sixteen-state Markov-modulated Poisson process (MMPP) for which the time-stationary waiting time and the event-stationary interarrival time have crossing survival functions. This gives an explicit analytic counterexample to the universal stochastic order proposed as Conjecture 3.9 in Asanjarani and Nazarathy (2022), corresponding to assertion (IV) and Conjecture 4.2 in their 2019 preprint. The result **does not** resolve their separate squared-coefficient-of-variation conjecture.

Use states \(j=0,1,\ldots,15\) with one-way cyclic transitions at rate one, and the strictly positive event rates
\[
\lambda_j=1+\frac{1}{1000}\cos\!\left(\frac{\pi j}{8}\right).
\]
Write \(S_{\mathrm t}(u)\) and \(S_{\mathrm e}(u)\) for the time-stationary and event-stationary first-waiting survival probabilities. At the explicit time
\[
u_*=\frac{3\pi}{2\sin(\pi/8)},
\]
one has \(S_{\mathrm t}(u_*)<S_{\mathrm e}(u_*)\), whereas \(S_{\mathrm t}(u)>S_{\mathrm e}(u)\) for all sufficiently small \(u>0\). In particular, the proposed stochastic dominance does not hold for all irreducible MMPPs.

## Assumptions and scope

A stationary sixteen-state continuous-time Markov chain \(J\) has generator \(Q\) given by \(Q_{jj}=-1\) and \(Q_{j,(j+1)\bmod16}=1\), with all other entries zero. Given \(J\), event arrivals form an inhomogeneous Poisson process with instantaneous intensity \(\lambda_{J(u)}\). Thus this is a proper nondegenerate MMPP with the diagonal event matrix \(D=\operatorname{diag}(\lambda_0,\ldots,\lambda_{15})\) and substochastic no-arrival generator \(C=Q-D\). Irreducibility holds because the directed cycle visits every state; the stationary distribution is \(\pi_j=1/16\).

Put \(\varepsilon=10^{-3}\), \(v_j=\cos(\pi j/8)\), and \(V=\operatorname{diag}(v_j)\). Uniform averaging gives \(\pi v=0\), \(\pi v^2=1/2\) and mean intensity \(\bar\lambda=1\). The Palm distribution of the phase observed immediately at a stationary event is \(\alpha_j=\pi_j\lambda_j/\bar\lambda=(1+\varepsilon v_j)/16\). The survival functions are exactly
\[
S_{\mathrm t}(u)=\pi e^{Cu}{\bf1},\qquad S_{\mathrm e}(u)=\alpha e^{Cu}{\bf1}.
\]
No reversibility assumption is imposed; the cycle is intentionally nonreversible.

## Proof

**1. Controlled modulation expansion.** Since \(C=(Q-\varepsilon V)-I\) and \(\alpha=\pi(I+\varepsilon V)\),
\[
S_{\mathrm t}(u)-S_{\mathrm e}(u)=-\varepsilon e^{-u}\pi V e^{(Q-\varepsilon V)u}{\bf1}.
\]
The Duhamel integral equation, with \(e^{Qu}{\bf1}={\bf1}\), yields
\[
e^{(Q-\varepsilon V)u}{\bf1}={\bf1}-\varepsilon\int_0^u e^{Qs}v\,ds+R(u),
\qquad \|R(u)\|_\infty\le \frac{(\varepsilon u)^2}{2}e^{\varepsilon u}.
\]
Indeed, \(e^{Qu}\) is a stochastic sup-norm contraction, \(\|V\|_\infty\le1\), and the terms of the time-ordered Duhamel expansion of order at least two are bounded by \(\sum_{k\ge2}(\varepsilon u)^k/k!\le(\varepsilon u)^2 e^{\varepsilon u}/2\). The zero-order term vanishes after left multiplication because \(\pi V{\bf1}=\pi v=0\). Therefore
\[
S_{\mathrm t}(u)-S_{\mathrm e}(u)=\varepsilon^2e^{-u}I(u)+E(u),\quad
I(u)=\int_0^u\pi V e^{Qs}v\,ds,\quad
|E(u)|\le \varepsilon^3 e^{-u}\frac{u^2}{2}e^{\varepsilon u}.
\]
This error estimate is uniform and rigorously justifies the finite-perturbation sign calculation.

**2. Explicit cycle Fourier mode.** Set \(\vartheta=\pi/8\), \(a=1-\cos\vartheta>0\), and \(b=\sin\vartheta>0\). The complex vector \((e^{i\vartheta j})_{j=0}^{15}\) is a \(Q\)-eigenvector with eigenvalue \(-a+ib\). Averaging the product of two cosine modes over the sixteen states gives
\[
\pi V e^{Qs}v=\tfrac12e^{-as}\cos(bs),\qquad
I(u)=\tfrac12\int_0^u e^{-as}\cos(bs)\,ds.
\]
At \(u_*=3\pi/(2b)\), the integral simplifies, using \(a^2+b^2=2a\), to
\[
I(u_*)=\frac{a-b e^{-a u_*}}{2(a^2+b^2)}
=\frac14\left(1-\frac{e^{-3\pi k/2}}{k}\right),
\qquad k=\frac ab=\tan(\pi/16).
\]

**3. A strict sign with elementary inequalities.** The elementary exact-angle formulas imply \(k<1/5\): this is equivalent to \(\cos(\pi/8)>12/13\), and follows from \(\cos^2(\pi/8)=(2+\sqrt2)/4\) and \(\sqrt2>238/169\). Similarly \(b>3/8\) follows from \(\sin^2(\pi/8)=(2-\sqrt2)/4>9/64\). Thus \(u_*<4\pi<13\), and \(3\pi k/2<3\pi/10<1\). Since \(e<3\),
\[
\frac{e^{-3\pi k/2}}k>\frac{1/3}{1/5}=\frac53,
\qquad I(u_*)<-\frac16.
\]
By \(e^x\le(1-x)^{-1}\) for \(0\le x<1\), the normalized remainder obeys
\[
\frac{|E(u_*)|}{\varepsilon^2e^{-u_*}}
\le\frac{\varepsilon u_*^2}{2}e^{\varepsilon u_*}
<\frac{169}{1974}<\frac16.
\]
Consequently, with no floating-point step,
\[
S_{\mathrm t}(u_*)-S_{\mathrm e}(u_*)
<-\varepsilon^2e^{-u_*}\left(\frac16-\frac{169}{1974}\right)
=-\frac{80}{987}\varepsilon^2e^{-u_*}<0.
\]

**4. The opposite sign near zero.** The two survival functions agree at zero. Differentiating their exact matrix formulas gives
\[
\left.\frac{d}{du}(S_{\mathrm t}-S_{\mathrm e})\right|_{u=0}
=-\pi D{\bf1}+\alpha D{\bf1}
=\varepsilon^2\pi v^2=\varepsilon^2/2>0.
\]
Continuity implies \(S_{\mathrm t}(u)>S_{\mathrm e}(u)\) on some interval \((0,\delta)\). The opposite signs establish a crossing and complete the counterexample.

## Verification

The inequalities in the proof alone certify the sign reversal. For an optional independent numerical check, `verify.py` constructs the sixteen-by-sixteen generator, forms the two initial phase laws, computes both matrix-exponential survival functions at the displayed time using arbitrary-precision arithmetic, checks \(I(u_*)\) against its closed expression, and checks the algebraic lower bound. It prints the two survivals and their difference; the difference is around \(-1.0872871578\times10^{-12}\). Such a small floating-point value is not used as evidence of strict negativity: the analytic bound above establishes the sign. The numerical script requires the third-party Python package `mpmath`.

## Relationship to prior work

Asanjarani and Nazarathy, *Stationary Markovian Arrival Processes: Results and Open Problems* (first posted 5 May 2019 as arXiv:1905.01736; published in *ANZIAM Journal* in 2022), formulate the universal stochastic order as assertion (IV), Conjecture 3.9 (Conjecture 4.2 in the initial preprint). Their positive theorems cover general Markov-switched Poisson processes and two-state MMPPs, which do not include this sixteen-state MMPP; their four-state counterexample concerns nonmonotonic hazard rate, not the two survival functions. This construction is nonreversible, uses a single cyclic Fourier mode, and supplies an exact sign certificate at an explicit time.

An earlier abstract by the same authors, *The Squared Coefficient of Variation for MMPP is Greater than Unity* (arXiv:1802.08400, 2018), states that a proof and a related stochastic order were obtained. Its full text was not accessible during this comparison, and that abstract conflicts with the same authors' later characterization of general stochastic ordering as a conjecture. This historical inconsistency is a concrete priority and interpretation risk, not evidence that either paper was corrected or withdrawn.

## Limitations

Only assertion (IV), the claimed universal stochastic dominance, is disproved. This example neither determines the squared coefficient of variation nor refutes conjecture (III). The certified negative difference at the selected time is small because it is a weak-intensity-modulation example; the strict elementary bound, rather than floating-point computations, establishes the sign. The literature search is bounded. An earlier 2018 manuscript asserting an apparently stronger result could not be inspected in full; its relationship to the published 2022 conjecture needs independent examination.

## References

1. A. Asanjarani and Y. Nazarathy, *Stationary Markovian Arrival Processes, Results and Open Problems*, arXiv:1905.01736, first public version 5 May 2019. https://arxiv.org/abs/1905.01736
2. A. Asanjarani and Y. Nazarathy, *Stationary Markovian Arrival Processes: Results and Open Problems*, *ANZIAM Journal* 64 (2022), 54–68, DOI 10.1017/S1446181122000013. https://doi.org/10.1017/S1446181122000013
3. A. Asanjarani and Y. Nazarathy, *The Squared Coefficient of Variation for MMPP is Greater than Unity*, arXiv:1802.08400 (2018). Full text not inspected. https://arxiv.org/abs/1802.08400
