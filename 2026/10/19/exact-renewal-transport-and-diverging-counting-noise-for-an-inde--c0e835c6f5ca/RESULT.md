# Exact renewal transport and diverging counting noise for an independently gated exclusion bond

## Finding
Fix an integer \(n\ge3\), an open-bond hopping rate \(r>0\), an open-gate fraction \(0<p<1\), and a gate-switching speed \(\kappa>0\). Put \(m=n-1\). In the periodic clockwise exclusion process defined below with one vacancy and one independently gated bond, the times \(\tau\) between consecutive crossings of that bond are independent and identically distributed with Laplace transform
\[
\Phi(s)=\mathbb E(e^{-s\tau})=
\frac{r\left[p(\kappa+s)(1+s)^{-m}+(1-p)s(1+s+\kappa)^{-m}\right]}{s^2+(r+\kappa)s+rp\kappa},\qquad s\ge0.
\]
Writing \(u=(1+\kappa)^{-m}\), their exact mean and second moment are
\[
\mu=m+\frac1{rp}+\frac{1-p}{p\kappa}(1-u),
\]
\[
\mathbb E\tau^2=\frac{r\{p\kappa m(m+1)-2pm-2(1-p)m u/(1+\kappa)\}-2+2\mu(r+\kappa)}{rp\kappa}.
\]
The stationary current through each bond is \(J(\kappa)=\mu^{-1}\), strictly increasing in \(\kappa\) for fixed \(n,r,p\), with sharp limits
\[
\lim_{\kappa\downarrow0}J(\kappa)=\frac{p}{m+1/r},\qquad
\lim_{\kappa\to\infty}J(\kappa)=\frac1{m+1/(rp)}.
\]
If \(N_t\) counts particles crossing the gated bond by time \(t\) in stationarity, its asymptotic counting Fano factor is
\[
F(\kappa)=\lim_{t\to\infty}\frac{\operatorname{Var}N_t}{\mathbb EN_t}
=\frac{\mathbb E\tau^2-\mu^2}{\mu^2}.
\]
In the slow-switching and fast-switching regimes, respectively,
\[
F(\kappa)\sim\frac{2(1-p)}{\kappa(m+1/r)}\quad(\kappa\downarrow0),\qquad
F(\kappa)\longrightarrow\frac{m+(rp)^{-2}}{[m+(rp)^{-1}]^2}<1\quad(\kappa\to\infty).
\]
Therefore \(F\) crosses the Poisson value \(1\) at least once as gate speed increases; no uniqueness of crossings is asserted. The slow-gate current has a strictly positive limit even though its normalized counting fluctuations diverge.

## Assumptions and scope
Sites \(0,\ldots,n-1\) form a directed ring with exactly \(n-1\) indistinguishable particles and one vacancy. An occupied site attempts to transfer its particle one site clockwise only when the destination is vacant. Ordinary directed edges have hopping rate one. The edge from \(n-1\) to \(0\) has rate \(r\) when a two-state external gate is ON and is completely blocked when that gate is OFF. The gate evolves autonomously, independently of particle occupancy, with transition rates \(\mathrm{ON}\to\mathrm{OFF}\) equal to \((1-p)\kappa\) and \(\mathrm{OFF}\to\mathrm{ON}\) equal to \(p\kappa\). All waiting clocks are independent. Crossings count completed particle hops on the special edge. Only finite \(n\) and strictly positive rates are claimed.

## Proof
**Regeneration.** Track the unique vacancy, which advances one site counterclockwise whenever a particle hops clockwise. Immediately after a completed hop across the special edge, the vacancy is at site \(n-1\), and the external gate must be ON. To cross the special edge again, the vacancy must traverse the other \(m=n-1\) edges, each at rate one; their independent total time \(S\) is Gamma with integer shape \(m\) and unit rate. The gate remains an autonomous two-state Markov chain during this traversal. At the next arrival at the special edge it either allows a rate-\(r\) hop or remains blocked until opening. Independence of the clocks and the strong Markov property at each crossing show that successive complete crossing intervals are iid.

**Gated-service transform.** Set \(a=(1-p)\kappa\), \(b=p\kappa\). Let \(\phi_{\rm on}(s)\) and \(\phi_{\rm off}(s)\) be Laplace transforms for the remaining service time at the special edge, conditioned on initial gate state. First-step decomposition gives
\[
\phi_{\rm on}(s)=\frac{r+a\phi_{\rm off}(s)}{r+a+s},\qquad
\phi_{\rm off}(s)=\frac{b\phi_{\rm on}(s)}{b+s}.
\]
Thus \(\phi_{\rm on}=r(b+s)/Q(s)\), \(\phi_{\rm off}=rb/Q(s)\), where \(Q(s)=s^2+(r+\kappa)s+rb\). Starting ON, the gate's conditional probability of being ON after time \(t\) is \(p+(1-p)e^{-\kappa t}\). Since \(\mathbb E e^{-sS}=(1+s)^{-m}\), conditioning on \(S\) yields
\[
\Phi(s)=\phi_{\rm on}(s)[p(1+s)^{-m}+(1-p)(1+s+\kappa)^{-m}]
+\phi_{\rm off}(s)(1-p)[(1+s)^{-m}-(1+s+\kappa)^{-m}],
\]
which simplifies exactly to the stated transform. Its derivatives at \(s=0\) give the displayed first and second moments.

**Current and strict monotonicity.** The renewal-reward theorem gives one special-edge crossing per mean interval, \(J=1/\mu\). Stationary particle conservation forces equal mean current across every bond. Since
\[
\frac{1-(1+\kappa)^{-m}}{\kappa}=m\int_0^1(1+\kappa v)^{-m-1}\,dv,
\]
the extra waiting contribution in \(\mu\) decreases strictly as \(\kappa\) increases (all other parameters held fixed). This proves the strict current law and its boundary values; at the fast end the effective special-edge rate is \(rp\).

**Fluctuations and boundaries.** Every interval is a finite phase-type absorption time, hence has finite moments for every \(\kappa>0\). The renewal count variance theorem gives \(F=\operatorname{Var}\tau/\mu^2\). Expanding \((1+\kappa)^{-m}\) at zero in the exact two moment formulas gives
\[
\mu=\frac{m+1/r}{p}+O(\kappa),\qquad
\operatorname{Var}\tau=\frac{2(1-p)(m+1/r)}{p^2\kappa}+O(1).
\]
At large \(\kappa\), the service time converges to an independent exponential of rate \(rp\); together with the Gamma traversal, this yields the fast-end variance \(m+(rp)^{-2}\), and the displayed Fano limit. Its strict sub-Poissonian bound follows from
\[
[m+(rp)^{-1}]^2-[m+(rp)^{-2}]=m(m-1)+\frac{2m}{rp}>0.
\]
Analyticity in positive \(\kappa\) and the intermediate value theorem give at least one finite Poisson crossover, without asserting its uniqueness.

## Verification
The standalone `verify_gated.py` constructs, for each parameter instance, the complete \(2n\)-state vacancy-plus-gate generator, obtains the stationary current by exact rational linear algebra, independently computes the first two inter-crossing moments from the killed generator, and checks the Laplace transform at two positive rational frequencies. The recorded execution produced `PASS: 96 independent rational generator/current/moment/Laplace identities, 24 parameter instances`, covering \(3\le n\le8\) and four positive rational choices of \((r,a,b)\). SymPy is required. This is a finite verification of the stated symbolic formulas, not the proof for all sizes.

## Relationship to prior work
Turci, Parmeggiani, Pitard, Romano and Ciandrini (2012) studied intermittent transport in a ring with a dynamic *site* defect whose closing is forbidden when the site is occupied; that occupancy feedback is absent here. Waclaw, Cholewa-Waclaw and Greulich (2019; preprint 2018) considered independent site-wise dynamic roadblocks, emphasizing current-density laws and mean-field approximations across varying densities, rather than the present single-edge, one-vacancy exact renewal and counting-noise formulas. Scher and Reuveni (2021) derived broad gated-reaction renewal laws with spatial motion independent of gate state; here gate state directly determines whether the next spatial hop can occur. Their general renewal insight is credited; their stated independence hypothesis does not immediately give this bond-blocking process. These comparisons support a distinct exact specialization, not a proof that no equivalent historical calculation exists.

## Limitations
The gate must switch independently of vacancy occupancy; the result is not a theorem for occupancy-coupled site defects. It concerns exactly one vacancy, one directed gated edge, exponential waiting, specified two-state equilibrium gate fraction \(p\) held fixed when varying speed, and only stationary long-time bond-count statistics. It does not describe general-density exclusion current, higher-order cumulants, arbitrary gate kinetics, or unique crossing-speed optimality. General Markov-modulated renewal theory contains the method; bibliographic equivalence in historical queueing and traffic-light literature is a residual risk. No independent validation is claimed.

## References
1. F. Turci, A. Parmeggiani, E. Pitard, M. C. Romano and L. Ciandrini, *Transport on a Lattice with Dynamical Defects* (initially public 2012-07-07), https://arxiv.org/abs/1207.1804 .
2. B. Waclaw, J. Cholewa-Waclaw and P. Greulich, *Totally asymmetric exclusion process with site-wise dynamic disorder*, Journal of Physics A (2019), author manuscript https://www.pure.ed.ac.uk/ws/portalfiles/portal/82236921/TASEP_annealed_disorder_accepted.pdf .
3. Y. Scher and S. Reuveni, *A Unified Approach to Gated Reactions on Networks* (2021), https://arxiv.org/abs/2101.05124 .
4. Y. Scher and S. Reuveni, *Gated reactions in discrete time and space* (2021), https://arxiv.org/abs/2109.05593 .
