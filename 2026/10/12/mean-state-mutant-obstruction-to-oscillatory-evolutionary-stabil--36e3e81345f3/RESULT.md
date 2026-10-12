# Mean-state mutant obstruction to oscillatory evolutionary stability

## Finding

**Theorem (strict period-averaged payoff no-go).** Fix an integer \(n\ge2\), a real payoff matrix \(A\in\mathbb R^{n\times n}\), and a nonconstant, continuous, \(\tau\)-periodic map \(r:\mathbb R\to\Delta_{n-1}\), where \(\tau>0\) and
\[
\Delta_{n-1}=\{z\in\mathbb R^n:z_i\ge0,\ \sum_{i=1}^n z_i=1\},\qquad
p=\frac1\tau\int_0^\tau r(t)\,dt.
\]
Under the strict time-averaged opponent-payoff definition in Chakraborty, Dubey, Madhok and Chakraborty [1, Definition 1a, Eq. (6)], the resident \(r\) **cannot** be an oscillatory evolutionarily stable state: the distinct constant mutant \(m(t)\equiv p\) yields equal averaged resident and mutant fitness at every positive invasion fraction. Under [1, Definition 1c, Eq. (9)] the strict local comparison also fails: distinct mutants
\[
m_\eta(t)=(1-\eta)r(t)+\eta p,\qquad 0<\eta<1,
\]
are arbitrarily close to \(r\) and give equal averaged fitness. If \(r\) is an orbit of the autonomous replicator equation, \(p\) is itself a stationary replicator state. The counter-mutant is therefore dynamically admissible even under a restriction of Definition 1a to genuine replicator trajectories.

## Assumptions and scope

The theorem concerns **exactly** the strict, universally quantified mutant comparisons in Definitions 1a and 1c of [1]. Let the full-period sliding average of any mutant sequence \(m\) be
\[
\overline m(t)=\frac1\tau\int_{t-\tau}^{t}m(s)\,ds.
\]
Definition 1a requires, for *each* mutant state sequence distinct from \(r\), a positive invasion barrier below which
\[
\frac1\tau\int_0^\tau r(t)^{\mathsf T}A
\big[(1-\epsilon)p+\epsilon\overline m(t)\big]dt
>
\frac1\tau\int_0^\tau m(t)^{\mathsf T}A
\big[(1-\epsilon)p+\epsilon\overline m(t)\big]dt.\tag{1}
\]
Definition 1c requires the strict inequality
\[
\frac1\tau\int_0^\tau r(t)^{\mathsf T}A\overline m(t)\,dt
>
\frac1\tau\int_0^\tau m(t)^{\mathsf T}A\overline m(t)\,dt\tag{2}
\]
for every distinct mutant sequence in some deleted neighborhood of the resident sequence. Nonconstant means not identically equal to a single simplex point. Neither symmetry nor any sign condition on \(A\) is assumed. These definitions have no explicit exception for mutants sharing the resident's period mean; the source's separate equal-mean proviso concerns its later uniqueness propositions [1, Sec. III], not the quantified definitions themselves.

## Proof

**Constant mutant and Definition 1a.** Every full-period sliding average of the periodic resident equals \(p\). The state \(p\) belongs to the simplex by convexity. Select the mutant \(m(t)=p\) for every \(t\in\mathbb R\), so \(\overline m(t)=p\). The mixture in (1) is identically \((1-\epsilon)p+\epsilon p=p\) for every \(0<\epsilon<1\). Its resident payoff is
\[
\frac1\tau\int_0^\tau r(t)^{\mathsf T}Ap\,dt
=\Big(\frac1\tau\int_0^\tau r(t)\,dt\Big)^{\mathsf T}Ap=p^{\mathsf T}Ap.
\]
Its mutant payoff is likewise \(\tau^{-1}\int_0^\tau p^{\mathsf T}Ap\,dt=p^{\mathsf T}Ap\). Both sides are **identical**, regardless of the invasion fraction. Since the periodic resident is nonconstant, the constant mutant is a distinct state sequence. Hence no positive invasion barrier can produce the required strict inequality. This already proves the global no-go.

**Arbitrarily close mutant and Definition 1c.** Let \(0<\eta<1\) and \(m_\eta(t)=(1-\eta)r(t)+\eta p\). Each state lies in the simplex; the mutant sequence is distinct from \(r\) because the latter is nonconstant. Moreover,
\[
\sup_t\|m_\eta(t)-r(t)\|=\eta\sup_t\|p-r(t)\|\longrightarrow0
\qquad(\eta\downarrow0)
\]
for any norm on the finite-dimensional state space. The mutant is periodic with period \(\tau\) and period mean \((1-\eta)p+\eta p=p\); thus \(\overline m_\eta(t)=p\) at all times. Both sides of (2) consequently equal \(p^{\mathsf T}Ap\), contradicting strictness in *every* deleted neighborhood.

**Dynamical admissibility of the constant mutant.** Suppose in addition that \(r\) solves the autonomous replicator system
\[
\dot r_i=r_i\big((Ar)_i-r^{\mathsf T}Ar\big),\qquad i=1,\ldots,n.
\]
The support \(S=\{i:r_i(t)>0\}\) is independent of time by uniqueness of solutions and the invariance of simplex faces. For every \(i\in S\), \(r_i(t)>0\) throughout the periodic orbit, and integrating its logarithmic derivative gives
\[
0=\frac1\tau\int_0^\tau\frac{d}{dt}\log r_i(t)\,dt
=(Ap)_i-c,\qquad
c=\frac1\tau\int_0^\tau r(t)^{\mathsf T}Ar(t)\,dt.
\]
Because \(p_i>0\) exactly for \(i\in S\) and \(\sum_{i\in S}p_i=1\), multiplication by \(p_i\) and summation yield \(p^{\mathsf T}Ap=c\). Thus \((Ap)_i=p^{\mathsf T}Ap\) for each occupied strategy, while all other coordinates have \(p_i=0\). Therefore \(p_i((Ap)_i-p^{\mathsf T}Ap)=0\) for every \(i\), proving that \(p\) is a replicator equilibrium. The constant comparison mutant is an actual solution, not a fabricated state path. The rest-state identity is classical replicator averaging [3] and is used here only to establish admissibility; the universal strict-comparison obstruction follows already from the two preceding paragraphs.

## Verification

The proof is finite-dimensional algebra and period averaging; it needs no numerical integration, simulation, or unproved analytic lemma. The accompanying executable `verify.py` uses exact rational arithmetic with the four-strategy payoff matrix printed in [1, Appendix E(i)], a nonconstant interior Fourier-mode simplex path whose mean is known exactly, and distinct same-mean mutants. It verifies exact equality of the two sides of (1) and (2) for rational invasion and proximity parameters, and verifies a separate zero-sum replicator equilibrium identity. These checks are **illustrations**, not proofs for arbitrary matrices or orbits. Execute `python verify.py` using Python 3 without external packages.

## Relationship to prior work

Chakraborty et al. [1] introduce the quantified strict comparisons as Definitions 1a and 1c and in Appendix E(i) report a stable limit cycle satisfying their condition based on neighboring-trajectory tests. Their Sec. III notes equal-period-mean exceptions in a different context (the uniqueness propositions) but does not exempt the universally quantified mutant in Definition 1a. The constant mean-state competitor of this theorem is admissible under those literal definitions, so no nonconstant periodic orbit can satisfy them; finite tests on other perturbations cannot establish the universal claim. This does **not** disprove the existence or dynamical stability of their numerical cycles.

The periodic-orbit mean equilibrium in a replicator system is known mathematics; see the time-average dynamics literature [3]. Earlier heterogeneity-stable and information-stable orbit constructions [2,4] use discrete-time replicator maps and different fitness functionals. Their statements do not imply a no-go for the specific continuous-time strict period-averaged test of [1]. The contribution here is the explicit universally admissible counter-mutant and the local same-mean interpolation, not a new averaging identity or a new attractor theorem.

## Limitations

The conclusion applies to the **literal** universally quantified strict time-average tests in [1, Definitions 1a and 1c]. A repaired notion that excludes mean-matched mutants, compares synchronous instantaneous payoffs, or restricts admissible variations differently is not analyzed here. The local interpolation need not solve the replicator equation, although the global constant-mean mutant does when the resident is a replicator cycle. The theorem does not classify limit cycles, prove or refute their asymptotic stability, or establish a physically meaningful invasion process for the alternative payoff interpretation.

## References

[1] S. Chakraborty, V. K. Dubey, V. Madhok, and S. Chakraborty, *Oscillatory evolutionarily stable state and limit cycle in replicator dynamics*, arXiv:2601.01996v1 (first posted 2026-01-05), Definitions 1a and 1c, Section III, Appendix A, Appendix E; later published as *Physical Review E* 113, L062201 (2026), doi:10.1103/vhst-f25m. https://arxiv.org/html/2601.01996v1

[2] V. K. Dubey, S. Chakraborty, and S. Chakraborty, *Oscillatory equilibrium in asymmetric evolutionary games: Generalizing evolutionarily stable strategy*, arXiv:2410.13922v1 (2024), Sections III–V. https://arxiv.org/html/2410.13922v1

[3] J. Hofbauer, S. Sorin, and Y. Viossat, *Time Average Replicator and Best-Reply Dynamics*, *Mathematics of Operations Research* 34 (2009), 263–269, doi:10.1287/moor.1080.0359. https://hal.science/hal-00360767v1

[4] A. Mukhopadhyay and S. Chakraborty, *Periodic Orbit can be Evolutionarily Stable: Case Study of Discrete Replicator Dynamics*, arXiv:2102.11034v1 (2021), Section III.3. https://arxiv.org/html/2102.11034v1
