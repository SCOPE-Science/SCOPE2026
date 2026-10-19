# A raywise extinction threshold and an unrescuable composition cone in a three-member open hypercycle

## Finding
Consider the three-member open hypercycle with equal positive losses,
\[
\dot w_i=w_i\bigl(e^{-\gamma S}w_{i-1}-d\bigr),\qquad S=w_1+w_2+w_3,
\]
where indices are cyclic and \(d,\gamma>0\). Assume \(0<3d\gamma<e^{-1}\), and let \(S_-<\gamma^{-1}<S_+\) be the two roots of \(Se^{-\gamma S}=3d\).

**Raywise dichotomy and critical orbit.** For each strictly positive composition \(p\) with \(p_1+p_2+p_3=1\), there exists \(\sigma(p)\in[S_-,\infty]\) such that initial states \(w_i(0)=S_0p_i\), with \(S_0>0\), have the following limits as physical time tends to infinity:

* If \(S_0<\sigma(p)\), all three concentrations tend to zero.
* If \(\sigma(p)<\infty\) and \(S_0=\sigma(p)\), they tend to \((S_-/3,S_-/3,S_-/3)\).
* If \(\sigma(p)<\infty\) and \(S_0>\sigma(p)\), they tend to \((S_+/3,S_+/3,S_+/3)\).

For the uniform composition, \(\sigma(p)=S_-\); for each nonuniform composition having finite \(\sigma(p)\), the inequality \(\sigma(p)>S_-\) is strict. A neighborhood of the uniform composition has finite thresholds.

**An explicit positive-measure no-rescue cone.** Define
\[
\varepsilon_*:=\frac{d\gamma e}{2}\exp\!\left(-\frac{2}{d\gamma}\right)>0.
\]
If, after any cyclic relabeling, \(p_2+p_3<\varepsilon_*\), then \(\sigma(p)=\infty\). Thus every finite initial total biomass, however large, becomes extinct for a nonempty open subset of *strictly positive* compositions, despite the existence of a locally attracting coexistence equilibrium.

## Assumptions and scope
The system is an autonomous ODE in \(\mathbb R^3_{>0}\), without immigration, mutation, or intercommunity interactions. All three losses are identical. The result includes every fixed \(d,\gamma>0\) with \(3d\gamma<e^{-1}\) and every strictly positive initial composition. It concerns eventual deterministic population limits, not finite-time biological elimination. All time-dependent assertions in the theorem refer to original physical time \(t\ge0\), unless the auxiliary time \(\tau\) is explicitly named.

The equilibria \(S_\pm\) and local stability of the upper equilibrium are already established in the motivating literature; the new claim is the *complete raywise limit classification* and the *quantified, biomass-independent extinction cone*. The theorem does not claim that \(\sigma(p)\) admits an elementary closed form for all compositions.

## Proof
**1. Exact decomposition.** Set \(p_i=w_i/S\) and introduce the increasing clock
\[
\frac{d\tau}{dt}=S e^{-\gamma S}.
\]
As long as all concentrations are positive, a direct differentiation gives
\[
\frac{dp_i}{d\tau}=p_i(p_{i-1}-q),\qquad
q(\tau)=p_1p_2+p_2p_3+p_3p_1,\qquad
\frac{dS}{d\tau}=S q(\tau)-d e^{\gamma S}.
\tag{1}
\]
The first equations are autonomous and independent of initial biomass \(S_0\). On the simplex, \(q\le1/3\), with equality precisely at the uniform composition. Also
\[
\frac{d}{d\tau}\log(p_1p_2p_3)=1-3q\ge0.
\tag{2}
\]
The product is bounded above by \(1/27\) and bounded below by its strictly positive initial value. Thus the orbit stays in a compact interior subset of the simplex. The nonnegative expression \(1-3q\) is integrable in \(\tau\), and its derivative is bounded along this compact orbit. It therefore tends to zero. Consequently \(p_i(\tau)\to1/3\) and \(q(\tau)\to1/3\) as \(\tau\to\infty\).

**2. Extinction or one of the two positive equilibria.** For a fixed initial composition, equation (1) is a scalar, locally Lipschitz equation with a prescribed continuous forcing \(q(\tau)\). Its solutions retain strict order in their initial values while positive. The inequality
\[
\frac{dS}{d\tau}\le \frac S3-d e^{\gamma S}
\tag{3}
\]
bounds all positive solutions from above and shows that any solution reaching \(S<S_-\) decreases to zero in finite auxiliary time. More generally, whenever \(S\le3d/2\), its derivative is at most \(-d/2\), so a positive solution cannot approach zero only as \(\tau\to\infty\). Hence each solution either reaches zero at finite auxiliary time or remains uniformly separated from zero for all \(\tau\ge0\).

For a solution reaching zero at finite auxiliary time \(\tau_*\), equation (1) gives \(dS/d\tau\to-d\), and the inverse clock \(dt/d\tau=e^{\gamma S}/S\) implies \(t\to\infty\) as \(\tau\uparrow\tau_*\). In physical time the concentrations therefore tend to zero. For a surviving solution, \(S\) stays in a compact positive interval and the auxiliary clock covers \([0,\infty)\). Because \(q(\tau)\to1/3\), the scalar equation becomes asymptotic to
\[
F(S)=S/3-d e^{\gamma S}.
\]
The zeros of \(F\) are exactly \(S_-\) and \(S_+\), both simple, with \(F<0\) below \(S_-\), \(F>0\) strictly between them, and \(F<0\) above \(S_+\). Uniform eventual derivative signs on every closed interval away from those two zeros exclude any other limiting behavior in one dimension. Therefore every surviving solution tends to either \(S_-\) or \(S_+\), and its composition tends to the uniform vector.

**3. Exactly one boundary orbit on each rescuable ray.** By the scalar comparison principle, the set of biomasses whose trajectories survive auxiliary time is an upper set. Extinction is open in \(S_0\) because a zero crossing is transverse, with derivative \(-d\). Consequently the survival set is either empty or a closed half-line \([\sigma(p),\infty)\), where \(\sigma(p)\ge S_-\). If finite, the boundary initial mass survives and cannot converge to the upper equilibrium: uniform convergence of \(q\) and the strictly negative linearization \(F'(S_+)<0\) make its attracting basin open in initial biomass. Hence the boundary converges to \(S_-\).

There cannot be two distinct surviving initial masses converging to \(S_-\). Indeed, for two ordered solutions \(S_1<S_2\), their difference \(\Delta>0\) satisfies
\[
\frac{d}{d\tau}\log\Delta=q(\tau)-d\frac{e^{\gamma S_2}-e^{\gamma S_1}}{S_2-S_1}.
\]
If both approached \(S_-\), the right side would tend to
\[
\frac13-d\gamma e^{\gamma S_-}=\frac{1-\gamma S_-}{3}>0,
\]
contradicting \(\Delta\to0\). Thus every strictly larger initial biomass converges to \(S_+\). At uniform composition, \(q\equiv1/3\) and the scalar phase portrait gives \(\sigma=S_-\). If \(p\) is nonuniform, then \(q(0)<1/3\), so starting at \(S_-\) makes \(dS/d\tau<0\), immediately enters the region below \(S_-\), and becomes extinct. Openness of the extinction event implies \(\sigma(p)>S_-\) whenever finite. For compositions sufficiently close to uniform, \(q(\tau)\) stays uniformly close to \(1/3\), so initial biomass \(S_+\) remains in a positively invariant neighborhood of the attracting upper scalar root. This establishes the asserted nonempty set of finite thresholds.

**4. Quantified no-rescue cone.** Suppose \(p_2(0)+p_3(0)<\varepsilon_*\). From the simplex equation, each \(p_i'\le p_i\), hence
\[
q(\tau)\le p_2(\tau)+p_3(\tau)
\le (p_2(0)+p_3(0)) e^{\tau}.
\]
For every \(0\le\tau\le T:=2/(d\gamma)\), this gives \(q(\tau)<d\gamma e/2\). Since \(S e^{-\gamma S}\le1/(\gamma e)\) for every \(S\ge0\), equation (1) implies, as long as \(S>0\),
\[
\frac{dS}{d\tau}\le-\frac d2e^{\gamma S},\qquad
\frac{d}{d\tau}e^{-\gamma S}\ge \frac{d\gamma}{2}.
\]
If any positive solution survived until \(\tau=T\), then \(e^{-\gamma S(T)}\ge e^{-\gamma S_0}+1>1\), impossible for positive \(S(T)\). So every initial biomass on that open cone reaches zero before \(T\), proving \(\sigma(p)=\infty\). Cyclic permutations give three such cones.

## Verification
The supplied `CHECK.py` uses only Python's standard library. It checks 153 interior rational simplex configurations for the exact identities \(\sum p_i'=0\), \(\sum p_i'/p_i=1-3q\), \(q\le1/3\), and \(q\le p_2+p_3\); reconstructs both biomass equilibrium roots for \(d=1/20\), \(\gamma=1\); and checks the strict positive cone-aperture identity. The checker is a finite sanity test, *not* a substitute for the preceding all-parameter proof.

## Relationship to prior work
Bratus–Drozhzhin–Novozhilov (2025) introduce this open replicator and cyclic matrix and prove existence and local stability of the two positive hypercycle equilibria (Proposition 2.4). Their adjacent discussion describes basin separation as a numerically motivated conjectural phenomenon, primarily illustrating five species. The present theorem treats the specified equal-loss *three-species* case and proves a stronger raywise basin classification, as well as an open family of initial proportions for which **no total biomass can rescue coexistence**. The normalized replicator entropy calculation is classical; its coupling with the globally forced biomass equation and the sharp ray threshold supplies the claim.

Pavlovich–Bratus (2012) analyze older open cyclic-replication dynamics and stability dependence on parameters. Its indexed abstract and excerpts establish a close modeling antecedent, but the full article was not available for comprehensive theorem-to-theorem inspection. The statements accessible in that comparison did not establish the quantified biomass-independent composition cones or the all-ray limit trichotomy. Thus independent full-text historical comparison remains a material originality risk. Related later work on exclusion of dominated types concerns unequal interaction advantages, absent in this equal-cycle matrix.

## Limitations
The result is specific to three species, a common loss rate, exponential density factor, and positive strictly interior initial data. No extension to cycles of length four or greater or unequal losses is asserted. The cone aperture is a guaranteed analytic bound, **not claimed optimal**. No closed form for the global threshold function \(\sigma(p)\) is established. The historical 2012 article is a remaining full-text originality limitation. Scientific correctness and originality have been reviewed here; no independent audit has been performed.

## References
1. A. S. Bratus, S. V. Drozhzhin, A. S. Novozhilov, *A mathematical framework of consumer–resource dynamics: How to incorporate interactions between interactions in evolutionary process*, arXiv:2511.06509v1 (first public 2025-11-09), Section 2, Proposition 2.4 and Appendix. https://arxiv.org/abs/2511.06509
2. E. N. Pavlovich, A. S. Bratus, *Studying the dynamics of open cyclic replication systems*, Moscow University Computational Mathematics and Cybernetics **36** (2012), 137–144. DOI: 10.3103/S0278641912030077. Full text not inspected.
3. E. N. Pavlovich, A. S. Bratus, *Exclusion of dominated species in open replicator systems*, Mathematical Models and Computer Simulations (2013), DOI: 10.1007/s10598-013-9165-2.
4. A. S. Bratus et al., *The replicator equation in evolution and population dynamics* (review of normalized dynamics), arXiv:2604.05720 (2026).
