# A three-habitat minimum of joint occupancy under partially synchronized catastrophes

## Finding

For an exchangeable three-habitat colonization--extinction model with independent background immigration, pairwise rescue, and catastrophic losses of fixed **per-occupied-habitat hazard**, varying the fraction of catastrophic hazard assigned to a common event has an exactly classified effect on the stationary probability that all three habitats are occupied. In a nonempty interval of rescue rates, this probability has a **unique strict interior minimum** as catastrophe synchronization increases. Outside that interval it is strictly monotone. The interior-minimum regime is absent from the corresponding two-habitat model.

Fix background colonization rate \(c>0\), local extinction rate \(e>0\), total catastrophe hazard \(k>0\) per occupied habitat, and additional per-occupied-neighbor rescue rate \(d\ge0\). Let \(\rho\in[0,1]\) be the common-shock fraction. Write \(s=c+e+k\), and set

\[
 d_- = \sqrt{(e+k)^2+\frac74s^2}-(e+k),\qquad
 d_+ = \sqrt{e^2+\frac74s^2-ks}-e.
\]

Then \(0<d_-<d_+\). Writing \(J(\rho)\) for the stationary probability of three occupied habitats:

1. If \(0\le d\le d_-\), \(J\) is strictly increasing on \([0,1]\).
2. If \(d_-<d<d_+\), \(J\) decreases strictly to a unique interior minimum at
   \[
   \rho_* = \frac{4d^2+8d(e+k)-7s^2}{4k(2d-s)}\in(0,1),
   \]
   and then increases strictly.
3. If \(d\ge d_+\), \(J\) is strictly decreasing on \([0,1]\).

For example, at \(c=e=k=1\) and \(d=5/2\), the unique minimizing catastrophe fraction is \(\rho_*=1/4\), with the exact comparisons
\[
 J(0)=\frac{21}{62}>J(1/4)=\frac{504}{1489}<J(1)=\frac{63}{185}.
\]

## Assumptions and scope

There are exactly three exchangeable habitat patches, each either occupied or vacant. Each vacant patch receives immigrants from outside at rate \(c\), independently of the other patches. If \(i\) of the other patches are occupied, a vacant patch receives additional successful internal colonizations at rate \(di\). Each occupied patch independently becomes vacant by ordinary local extinction at rate \(e\), and suffers an independent catastrophic clearing at rate \((1-\rho)k\). A single common catastrophic clock of rate \(\rho k\) simultaneously clears every occupied patch. The per-occupied-patch instantaneous catastrophic loss hazard is therefore exactly \(k\) at every \(\rho\), so only dependence between shocks changes.

The resulting continuous-time Markov chain has occupied-patch count \(N_t\in\{0,1,2,3\}\). From state \(i\), its ordinary upward rate is \(\lambda_i=(3-i)(c+di)\), its ordinary downward rate is \(\mu_i=i[e+(1-\rho)k]\), and when \(i>0\), a common clearing event sends the chain directly to state zero at rate \(\rho k\). In state one both independent and common clearing transitions target zero and their rates add. All positive model parameters are finite, and \(d=0\) is permitted. Since \(c,e>0\), this finite chain is irreducible and has a unique stationary distribution \(\pi\); \(J(\rho)=\pi_3\).

## Proof

**Exact stationary law.** Put \(u=e+(1-\rho)k\) and \(v=\rho k\). The stationary balance at state three gives \(\lambda_2\pi_2=(3u+v)\pi_3\). Balances successively at states two and one give
\[
 \pi_2=\frac{3u+v}{c+2d}\pi_3,\qquad
 \pi_1=\frac{[2(c+2d)+2u+v]\pi_2-3u\pi_3}{2(c+d)},
\]
\[
 \pi_0=\frac{[2(c+d)+u+v]\pi_1-2u\pi_2}{3c}.
\]
All denominators are positive. Normalizing \(\sum_{i=0}^{3}\pi_i=1\) and simplifying gives
\[
 J(\rho)=\frac{6c(c+d)(c+2d)}{D(\rho)},
\]
where
\[
 D(\rho)=6(s^3+3cds+2cd^2)
 +k\rho[4d^2+8d(e+k)-7s^2]
 +2k^2\rho^2(s-2d).
\]
The stationary construction (or irreducibility and positivity of \(\pi_3\)) proves \(D(\rho)>0\) throughout the admissible domain. Differentiation gives
\[
 J'(\rho)=\frac{6c(c+d)(c+2d)k}{D(\rho)^2}\,H(\rho),
 \qquad H(\rho)=7s^2-4d^2-8d(e+k)-4k\rho(s-2d).
\]

**Thresholds and sign changes.** The equation \(H(0)=0\) has one positive root \(d_-\), while \(H(1)=0\) has one positive root \(d_+\); each follows from a strictly decreasing quadratic in \(d\ge0\). Further,
\[
 H(0)\big|_{d=s/2}=2s^2+4sc>0,
\]
so \(d_->s/2\). Consequently \(H(1)>H(0)=0\) at \(d=d_-\), and since \(H(1)\) decreases strictly with \(d\), its root obeys \(d_+>d_-\). For \(d\le s/2\), both endpoint values of \(H\) are positive. For \(s/2<d<d_-\), \(H(0)>0\) and \(H\) increases with \(\rho\), so remains positive; equality at \(d_-\) occurs only at the endpoint \(\rho=0\). For \(d_-<d<d_+\), \(H(0)<0<H(1)\) and \(H\) is strictly increasing in \(\rho\), so it crosses zero exactly once, at the stated \(\rho_*\). For \(d\ge d_+\), \(H(1)\le0\) and \(H(\rho)<0\) for \(\rho<1\). These facts establish all three regimes and their boundary cases.

**Exact example.** At \(c=e=k=1\), \(d=5/2\), the denominator reduces to \(D(\rho)=372+2\rho-4\rho^2\), so \(J(\rho)=126/D(\rho)\). The unique maximum of the positive denominator is at \(\rho=1/4\), which produces the rational values stated above. The sign changes are strict.

## Verification

The included `CHECKER.py` uses exact rational arithmetic to solve the complete four-state stationary master equation by Gauss--Jordan elimination, independently of the closed-form expression. It checks the formula, the positivity of its denominator, and the analytic derivative signs for 3,750 parameter tuples plus the exact interior-minimum example, completing 18,755 assertions. Run `python3 CHECKER.py` in the directory containing this file. The checker prints `VERIFY_OK assertions= 18755`. The proof of the infinite parameter-domain theorem is the preceding algebraic argument, not the finite grid.

## Relationship to prior work

Holyoak and Lawler (1996) and Holyoak (2000) document how dispersal, local extinction, and synchrony affect persistence in fragmented populations. Keeling (2000) analyzes coupling and stochastic metapopulation persistence using moment closure, rather than this exact four-state common-shock chain. Etienne and Heesterbeek (2001) study stochastic occupancy and conservation interventions, but the accessible abstract does not establish the present matched-marginal catastrophe-synchrony law. A previous **two-habitat** exact calculation for common versus independent catastrophic clearing gives a derivative of fixed sign throughout the synchronization interval. That result does not imply the present **three-habitat interior minimum**, which is a qualitative change in the joint-occupancy observable. The general idea of rescue, synchronized extinction, and finite Markov occupancy chains is established; novelty is claimed only for the stated all-parameter three-habitat classification and exact interior-minimum mechanism, subject to the access limitations below.

## Limitations

The theorem concerns the stationary probability that all three habitats are occupied, not mean persistence time, biological richness, or long-run population abundance. Background colonization must remain strictly positive; the zero-immigration chain can instead absorb at extinction. Rescue is linear in the number of occupied sources, habitats are exchangeable, shocks are memoryless and completely synchronized when common, and this is not a field-calibrated conservation recommendation. Exact priority against every earlier common-shock occupancy treatment has not been independently established; the full text of a closely related stochastic conservation paper was unavailable.

## References

- M. Holyoak and S. P. Lawler (1996), *Persistence of an Extinction-Prone Predator--Prey Interaction Through Metapopulation Dynamics*, Ecology 77, 1867--1879. https://doi.org/10.2307/2265790 (published September 1, 1996).
- M. Holyoak (2000), *Habitat Patch Arrangement and Metapopulation Persistence of Predators and Prey*, American Naturalist 156, 378--389. https://doi.org/10.1086/303395.
- M. J. Keeling (2000), *Metapopulation moments: coupling, stochasticity and persistence*, Journal of Animal Ecology 69, 725--736. https://doi.org/10.1046/j.1365-2656.2000.00430.x.
- R. S. Etienne and J. A. P. Heesterbeek (2001), *Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model*, American Naturalist 158, 389--407. https://doi.org/10.1086/321986.
