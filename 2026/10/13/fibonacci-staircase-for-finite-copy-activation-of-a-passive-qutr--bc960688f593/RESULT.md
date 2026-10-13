# Fibonacci staircase for finite-copy activation of a passive qutrit with a golden-ratio gap

## Finding

Let \(\varphi=(1+\sqrt5)/2\), \(\beta>0\), and \(\delta>0\). The three-level Hamiltonian and its passive, nonthermal diagonal state are
\[
H=\operatorname{diag}(0,1,1+\varphi),\qquad
\rho_{\beta,\delta}=Z^{-1}\operatorname{diag}(1,e^{-\beta},e^{-\beta(1+\varphi+\delta)}),
\quad Z=1+e^{-\beta}+e^{-\beta(1+\varphi+\delta)}.
\]
Write \(N_{\rm act}(\delta)\) for the *smallest* positive integer \(N\) such that a global unitary decreases the energy expectation of \(\rho_{\beta,\delta}^{\otimes N}\) with respect to \(\sum_{j=1}^N H_j\). Define Fibonacci numbers by \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and put
\[
\varepsilon_k=\frac{F_{2k+3}}{F_{2k+2}}-\varphi
=\frac{\varphi^{-(2k+2)}}{F_{2k+2}}\quad (k\ge0),\qquad \varepsilon_{-1}=+\infty.
\]
Then, for the unique integer \(k\ge0\) satisfying \(\varepsilon_k<\delta\le\varepsilon_{k-1}\),
\[
\boxed{N_{\rm act}(\delta)=F_{2k+4}.}
\]
In particular the exact successive first-activation copy counts are \(3,8,21,55,144,\ldots\), as the departure \(\delta\) from the Gibbs logarithmic slope is reduced. The staircase has a sharp oscillatory small-departure envelope:
\[
\boxed{\liminf_{\delta\downarrow0}\sqrt\delta\,N_{\rm act}(\delta)=\frac{\varphi^2}{5^{1/4}},\qquad
\limsup_{\delta\downarrow0}\sqrt\delta\,N_{\rm act}(\delta)=\frac{\varphi^4}{5^{1/4}}.}
\]
Thus there is no single limiting coefficient for the copy cost at order \(\delta^{-1/2}\). The entire result is independent of the strictly positive inverse-temperature scale \(\beta\).

## Assumptions and scope

The energy levels are exactly \(0,1,1+\varphi\), the state is full rank, and both \(\beta\) and \(\delta\) are arbitrary positive real numbers. Only positive work from a unitary on finitely many independent identical copies is counted; no catalyst or auxiliary system is supplied. Degeneracies among tensor-product energies and probabilities do not cause a reversal by themselves: work extraction requires a *strict* energy-population inversion. Each equality endpoint in the displayed staircase is therefore assigned to the larger copy count.

For the derivation it is useful to allow any second-gap ratio \(r>0\), with Hamiltonian \(H_r=\operatorname{diag}(0,1,1+r)\) and the analogous full-rank state \(\rho_{r,\beta,\delta}\) formed by replacing \(\varphi\) by \(r\) above. The general reduction below is an auxiliary lemma; the assessed sharp physical conclusion is the explicit golden-ratio staircase and its nonconvergent asymptotic envelope.

## Proof

**1. Exact tensor-power inversion criterion.** For a product eigenstate of \(N\) copies, let \((a,b,c)\) be its three occupation counts, so \(a+b+c=N\). Ignoring the common additive normalization in its negative logarithmic probability, its energy and dimensionless logarithmic cost are
\[
E=b+(1+r)c,\qquad Q=b+(1+r+\delta)c.
\]
Passivity of a finite diagonal state is equivalent to absence of a pair of eigenvectors whose higher energy carries strictly higher probability (rearrangement inequality for unitary conjugations). Let \(\Delta\) be the difference of the higher-energy count vector minus the lower-energy count vector. Set \(p=\Delta b+\Delta c\) and \(n=\Delta c\). A strict inversion gives simultaneously
\[
\Delta E=p+rn>0,\qquad \Delta Q=p+(r+\delta)n<0.
\]
Subtracting, \(\delta n<0\), hence \(n=-q\) with an integer \(q>0\), and \(r q<p<(r+\delta)q\) with an integer \(p>0\). The count differences are exactly
\[
(\Delta a,\Delta b,\Delta c)=(-p,p+q,-q).
\]
The component \(\Delta b=p+q\) forces \(N\ge p+q\). Conversely, whenever integers \(p,q>0\) satisfy \(r<p/q<r+\delta\), a transposition of the product vectors \(|1\rangle^{\otimes(p+q)}\) and \(|0\rangle^{\otimes p}\otimes|2\rangle^{\otimes q}\) lowers mean energy strictly: the first vector is higher in energy by \(p-rq>0\) but has larger occupation probability because \(p<(r+\delta)q\). Therefore
\[
N_{\rm act}(r,\delta)=\min_{p,q\in\mathbb Z_{>0}}\{p+q:r<p/q<r+\delta\}. \tag{1}
\]
The minimum exists because the rationals are dense. This criterion is *necessary* for every possible global unitary, not merely a sufficient construction by a selected two-level swap. Tensoring both vectors with a common additional factor proves that all larger copy counts are likewise active.

**2. Golden-ratio Farey certificate.** Let \(U_k=F_{2k+3}/F_{2k+2}\). The usual Fibonacci determinant identity, or Binet's formula, yields \(U_k>\varphi\) and the stated exact formula for \(\varepsilon_k=U_k-\varphi\). These errors decrease strictly to zero, so \(k\) is unique.

For \(k=0\), \(\delta>\varepsilon_0=2-\varphi\) admits \(p/q=2/1\), hence a three-copy inversion. Every rational above \(\varphi>1\) has \(p\ge2\), \(q\ge1\), so three is minimal.

For \(k\ge1\), introduce the neighboring rational bounds
\[
L=\frac{F_{2k+2}}{F_{2k+1}}<\varphi
< U=\frac{F_{2k+1}}{F_{2k}},\qquad
F_{2k+1}^{\,2}-F_{2k}F_{2k+2}=1.
\]
The last identity makes \(L\) and \(U\) Farey neighbors. Because \(\delta\le\varepsilon_{k-1}\), every rational in \((\varphi,\varphi+\delta)\) lies strictly between \(L\) and \(U\). Any fraction \(p/q\) strictly between two Farey neighbors has denominator at least the *sum* of their denominators: writing \(p/q\) in reduced or unreduced form, the two positive integer determinants \(p q_L-p_Lq\) and \(p_Uq-pq_U\), multiplied by the opposing denominators and added, give
\[
q=(p q_L-p_L q)q_U+(p_Uq-pq_U)q_L\ge q_U+q_L=F_{2k+2}.
\]
Since \(p>\varphi q\), monotonicity together with \(F_{2k+3}-\varphi F_{2k+2}=\varphi^{-(2k+2)}\in(0,1)\) yields \(p\ge F_{2k+3}\). Hence every activating pair satisfies \(p+q\ge F_{2k+4}\). Equality is achieved by the mediant \(U_k=F_{2k+3}/F_{2k+2}\), which lies strictly inside the activation interval because \(\delta>\varepsilon_k\). Combining with (1) proves the exact staircase, including all endpoints.

**3. Sharp accumulation envelope.** Set \(m=2k+2\). Binet's formula gives
\[
F_m\sim\frac{\varphi^m}{\sqrt5},\quad
\varepsilon_k\sim\sqrt5\,\varphi^{-2m},\quad
F_{m+2}\sim\frac{\varphi^{m+2}}{\sqrt5},\quad
\frac{\varepsilon_{k-1}}{\varepsilon_k}\longrightarrow\varphi^4.
\]
On the interval \(\varepsilon_k<\delta\le\varepsilon_{k-1}\), the copy count is the constant \(F_{m+2}\), whereas its scaled value \(F_{m+2}\sqrt\delta\) increases continuously with \(\delta\). The lower endpoint is approached from above, yielding \(\varphi^2/5^{1/4}\); the included upper endpoint yields \(\varphi^4/5^{1/4}\). These two sequences realize the respective global lower and upper accumulation values, proving the liminf and limsup. Their strict inequality proves there is no single constant limit.

## Verification

The standalone standard-library program `verify_passivity.py` implements exact signs of integers plus integer multiples of \(\varphi\), exact rational windows for thirteen positive values of \(\delta\), brute-force enumeration of all candidate fractions below the proposed minimum, and separate occupation-vector enumeration of possible energy/probability inversions for the feasible smaller cases. It checks the Cassini/Farey determinant and mediant identities for the first eight steps and the next activating fraction at six exact equality breakpoints, then reports approximate values of the two *analytically established* asymptotic coefficients. Run from any directory with `python3 verify_passivity.py`. The finite tests do not establish the infinite staircase; the proof above does.

## Relationship to prior work

Alicki and Fannes (2012, arXiv:1211.1209) established the work-extraction/passivity framework and asymptotic multi-copy thermodynamic improvement. Skrzypczyk, Silva and Brunner (2014, arXiv:1412.5485, equation (9)) gave a *sufficient* rational-gap inequality for finite-copy activation. Sparaciari, Jennings and Oppenheim (2017, doi:10.1038/s41467-017-01505-4, equations (12), (26)) studied closely related rational-gap inequalities for qutrit work-extraction cycles with an auxiliary machine; those protocols are not the no-ancilla global-unitary first-copy optimum studied here. Koukoulekidis, Alexander, Hebdige and Jennings (2019/2021, arXiv:1912.07968, lemma 7) provided a general necessary-and-sufficient geometric test of \(N\)-passivity. Thus neither the rational inequality nor the existence of a copy-number algorithm is asserted to be new.

The additional conclusion established here is an *explicit sharp minimum* in the canonical irrational-gap family, its Fibonacci-valued jump positions, its strict endpoint convention, and the two unequal accumulation constants at square-root scale. The general geometric test does not itself state those evaluated arithmetic quantities. This mathematical specialization remains susceptible to priority overlap with quantitative finite-passivity, Farey-approximation, or related thermodynamic work beyond the inspected sources.

## Limitations

The theorem does not quantify the maximum extractable work, nor does it address restricted-control unitaries, catalysts, nonidentical copies, or spectra of four or more levels. The explicit Fibonacci staircase requires the golden-ratio second gap. The general rational minimization formula is not claimed as a new replacement for existing geometric passivity criteria. The literature comparison is not an independent originality certification; unlocated equivalent calculations remain a residual risk.

## References

1. R. Alicki and M. Fannes, *Extractable work from ensembles of quantum batteries. Entanglement helps*, arXiv:1211.1209v1 (first public 2012-11-06), https://arxiv.org/abs/1211.1209.
2. P. Skrzypczyk, R. Silva and N. Brunner, *A short note on passivity, complete passivity and virtual temperatures*, arXiv:1412.5485v1 (first public 2014-12-17), https://arxiv.org/abs/1412.5485.
3. C. Sparaciari, D. Jennings and J. Oppenheim, *Energetic instability of passive states in thermodynamics*, Nature Communications **8**, 1895 (2017), doi:10.1038/s41467-017-01505-4.
4. N. Koukoulekidis, R. Alexander, T. Hebdige and D. Jennings, *The geometry of passivity for quantum systems and a novel elementary derivation of the Gibbs state*, arXiv:1912.07968 (first public 2019; final text 2021), https://arxiv.org/abs/1912.07968.
