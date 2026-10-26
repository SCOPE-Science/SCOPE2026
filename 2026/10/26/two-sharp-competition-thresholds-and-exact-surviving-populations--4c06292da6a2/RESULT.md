# Two sharp competition thresholds and exact surviving populations on ecological cycles

## Finding

Consider the synchronous discrete competitive generalized Lotka–Volterra biomass update on a simple cycle of \(n\ge4\) sites, with carrying capacity \(K=2\), uniform competition weight \(\alpha/2\) along every edge, and initially positive biomass in \(\{1,2\}\) at every site. For every \(\alpha>1\), the entire attractor, including its basin determined by each starting state, is explicitly classified by the cyclic maximal runs of sites initially at biomass \(2\):

* For \(1<\alpha<2\), a run of length one becomes a permanently isolated biomass-\(2\) site; a run of length two becomes a neighboring pair alternating synchronously between biomass \((2,2)\) and \((1,1)\); a run of length at least three leaves precisely its two endpoints at permanent biomass \(2\), all other sites becoming extinct. The dynamics becomes periodic by the second update, with period dividing two. It has genuine period two precisely when some initial run has length two.
* At \(\alpha=2\), the same run-support classification holds, but the sites in a length-two run become a stationary neighboring pair at biomass \((1,1)\); all other surviving sites become permanently isolated at biomass \(2\). Every trajectory becomes stationary by the third update.
* For \(\alpha>2\), precisely the length-one runs survive, each as an isolated site at biomass \(2\). Every trajectory becomes stationary by the second update.

If all sites initially have biomass one or all have biomass two, all sites become extinct; these are the sole all-extinction initial conditions when \(1<\alpha\le2\).

For independent equally likely initial biomass values \(1\) and \(2\), the exact expected eventual occupied-site fraction is \(3/8\) throughout \(1<\alpha\le2\), but only \(1/8\) for \(\alpha>2\), for every \(n\ge4\). For \(1<\alpha<2\), exactly \(1/8\) of sites are expected to participate in oscillating pairs and \(1/4\) are expected to become fixed survivors. Thus the expected stationary/periodic biomass per site is \(3/4\) at even times from the second update and \(5/8\) at odd times from the third update. At \(\alpha=2\) the final biomass mean is \(5/8\), whereas for \(\alpha>2\) it is \(1/4\).

The probability of global extinction in \(1<\alpha\le2\) is exactly \(2^{1-n}\). For \(1<\alpha<2\), the probability of a genuine period-two attractor is at least \(1-(15/16)^{\lfloor n/4\rfloor}\), which tends to one exponentially as the cycle size grows.

## Assumptions and scope

Let the vertices be integers modulo \(n\), where \(n\ge4\). Write \(N_i(t)\in\{0,1,2\}\) for biomass at vertex \(i\) at time \(t\in\{0,1,\ldots\}\), with all \(N_i(0)\in\{1,2\}\). Define the simultaneous update by
\[
N_i(t+1)=N_i(t)+\operatorname{sgn}\!\left(N_i(t)\left[2-N_i(t)-\frac{\alpha}{2}\left(N_{i-1}(t)+N_{i+1}(t)\right)\right]\right),
\]
where \(\operatorname{sgn}(0)=0\). In particular, biomass zero is absorbing. This is the \(d=2\), \(K=2\) specialization of the positive-initialization discrete competition model of Sergo et al. The boundary cases \(\alpha=2\) and \(\alpha>2\) are distinguished; the theorem makes no assertion for \(\alpha\le1\).

An *initial two-run* is a maximal cyclic contiguous string of sites having \(N_i(0)=2\), with a site initially at biomass one on each side. If all vertices start at biomass two, treat this separately as the all-two configuration. A site is *eventually occupied* if it has positive biomass at every sufficiently large time. A genuine period-two attractor is one whose complete state vector has least period two.

The probabilistic statements use independently and uniformly assigned initial values, with all \(2^n\) assignments equally likely; they do not invoke a thermodynamic-limit approximation.

## Proof

**First-update reduction.** Since every initial site and both its neighbors have positive biomass, an initial biomass-two site has strictly negative growth and becomes biomass one. An initial biomass-one site has bracket at most \(1-\alpha<0\) for \(\alpha>1\) and becomes extinct. Put \(X_i=\mathbf1\{N_i(0)=2\}\). Therefore the first state is exactly \(N_i(1)=X_i\).

**Second-update classification.** For a site with \(X_i=1\), let \(s_i=X_{i-1}+X_{i+1}\in\{0,1,2\}\). Its next growth has the sign of \(1-\alpha s_i/2\). A site with \(X_i=0\) is already extinct. Thus for \(1<\alpha<2\), the value \(N_i(2)\) is two if \(X_i=1\) and \(s_i\le1\), otherwise zero. At \(\alpha=2\), it is two, one, or zero according as \(X_i=1\) with \(s_i=0,1,2\), respectively. For \(\alpha>2\), it is two exactly when \(X_i=1\) and \(s_i=0\), and is zero otherwise.

**Run dynamics.** For \(1<\alpha<2\), the preceding criterion keeps the single vertex of a one-run, both vertices of a two-run, and only the two boundary vertices of a run of length at least three. Distinct initial runs are separated by an originally biomass-one site and hence by an absorbing zero from the first update onwards. The two retained endpoints of a run of length at least three are nonadjacent; they and all one-run survivors are isolated at biomass two, hence fixed. Each retained two-run is an isolated adjacent pair at biomass \((2,2)\); both become biomass one together in the next update and return together to biomass two after another update because \(1-\alpha/2>0\). These are the only possible nonconstant components. At \(\alpha=2\), a two-run produces the fixed pair \((1,1)\), since \(1-\alpha/2=0\); endpoints of longer runs initially retain biomass one but, now isolated, grow to and stay at biomass two in one further update. Above \(\alpha=2\) only isolated one-run vertices survive. If the initial state contains no one-run boundaries because it is all two, every site has two initial two-neighbors and dies at the second update. If it is all one, all sites die at the first update. Every other initial state contains a finite one-run, two-run, or longer run and thus has a survivor for \(1<\alpha\le2\). This proves the deterministic classification and global-extinction criterion.

**Exact finite-size densities.** Under the independent fair initialization, the three bits \(X_{i-1},X_i,X_{i+1}\) are independent, so
\[
\mathbb P(i\text{ survives for }1<\alpha\le2)
=\mathbb P(X_i=1,s_i\le1)=\frac12\left(1-\frac14\right)=\frac38,
\qquad
\mathbb P(i\text{ survives for }\alpha>2)
=\mathbb P(X_i=1,s_i=0)=\frac18.
\]
For \(n\ge4\), a two-run beginning at a prescribed vertex has the four-bit pattern \((0,1,1,0)\), of probability \(1/16\); its four sites are distinct even for \(n=4\). Every such run accounts for exactly two eventual oscillating sites when \(1<\alpha<2\), and no site belongs to two two-runs. Translation invariance and linearity of expectation give the expected oscillating-site fraction \(2/16=1/8\), leaving \(3/8-1/8=1/4\) fixed occupied sites. The stated biomass means follow from contributions two and one on the fixed and pair components; at \(\alpha=2\), pairs stay at one and all remaining survivors eventually stay at two. For \(\alpha>2\), the surviving sites all have biomass two. Exactly two initial assignments cause global extinction for \(1<\alpha\le2\), proving probability \(2/2^n\).

Finally, divide a fixed sequence of \(4\lfloor n/4\rfloor\) consecutive sites into disjoint blocks of four. A block realizing \((0,1,1,0)\) forces a two-run regardless of the states outside the block. These independent events each have probability \(1/16\), so the probability of no two-run is at most \((15/16)^{\lfloor n/4\rfloor}\). For \(1<\alpha<2\), a two-run is equivalent to a genuine period-two attractor, proving the final bound.

## Verification

Run `python verify.py` using only the Python standard library. The script computes the sign updates using exact `Fraction` arithmetic, enumerates every binary positive initial configuration for cycles of lengths four through ten, and checks seven rational coupling strengths covering all three parameter regimes and the equality boundary. It compares complete states through the fifth update to independently computed run predictions and checks the exact finite-size occupancy, oscillation, and biomass expectations. The completed run reported 14,224 passing initial-state/parameter classifications. These bounded checks are diagnostic; the proof above applies to all finite \(n\ge4\) and all real \(\alpha>1\).

## Relationship to prior work

Sergo, Koller, Erba, and Zdeborová (2026) introduced this discrete competitive ecological map, analyzed typical clustering and percolation primarily on random regular interaction graphs, and established that its eventual periodic orbits have period at most two. That general period bound does not identify which positive initial conditions on finite degree-two cycles generate two-cycles, the exact rapid convergence, or the two exact survival-density regimes. The present result supplies that complementary finite-cycle and finite-population classification.

Earlier discrete Lotka–Volterra work based on nonstandard finite-difference schemes or cyclic competition with mixing describes different dynamical maps, so such results do not directly imply the sign-update run classification here. The finite pattern calculation is elementary once the first-update reduction is identified; its relevance is the exact cycle-level ecological attractor and oscillation phase structure, not a claimed new general theorem about all cellular automata.

## Limitations

The result is restricted to degree-two cycles, positive initial biomasses in \(\{1,2\}\), fixed carrying capacity \(2\), and uniform nearest-neighbor competition. For \(\alpha=1\), the all-one configuration remains fixed rather than becoming extinct, showing why the lower strict inequality is needed. No assertion is made for \(\alpha\le1\), heterogeneous couplings, open paths, degree-three or higher networks, or stochastic disturbances. The oscillations here are deterministic synchronous biomass oscillations, not necessarily oscillations in the set of occupied sites. An equivalent one-dimensional cellular-automaton formulation may have appeared under different terminology; historical priority is not fully settled.

## References

1. D. Sergo, C. Koller, V. Erba, and L. Zdeborová, *Percolation and clustering in ecological communities: A dynamical theory*, arXiv:2606.09494v1, first submitted 2026-06-08, particularly the model and periodic-attractor analysis. https://arxiv.org/abs/2606.09494
2. L.-I. W. Roeger, *Dynamically consistent discrete Lotka–Volterra competition models derived from nonstandard finite-difference schemes*, Discrete and Continuous Dynamical Systems Series B 9 (2008), 415–429. https://doi.org/10.3934/dcdsb.2008.9.415
3. C. W. Feldager, N. Mitarai, and H. Ohta, *Deterministic extinction by mixing in cyclically competing species*, Physical Review E 95 (2017), 032318. https://doi.org/10.1103/PhysRevE.95.032318
