# A unique endemic-prevalence reversal between the two four-vertex trees

## Finding

For the homogeneous deterministic susceptible–infected–susceptible network equations on a connected, four-vertex, three-edge graph, the only two graph isomorphism types are the star \(K_{1,3}\) and the path \(P_4\). The total endemic occupation in the star is strictly greater at low transmission-to-recovery ratios, whereas the path has strictly greater endemic occupation at high ratios. There is **exactly one positive-occupation crossover**, at

\[
\tau_*=\frac{1}{2^{2/3}-1}=1.702414383919315\ldots.
\]

More precisely, write \(S(\tau)\) and \(P(\tau)\) for the sums of the four equilibrium infection probabilities, choosing zero when no positive equilibrium exists. Then

\[
\begin{array}{c|c}
0<\tau\le 1/\sqrt 3 & S(\tau)=P(\tau)=0\\
1/\sqrt 3<\tau<\tau_* & S(\tau)>P(\tau)\\
\tau=\tau_* & S(\tau)=P(\tau)>0\\
\tau>\tau_* & S(\tau)<P(\tau).
\end{array}
\]

The separate onset thresholds are \(1/\sqrt3\) for the star and \((\sqrt5-1)/2\) for the path, with the latter strictly larger. At strong transmission the ranking persists, but the difference tends to zero:

\[
P(\tau)-S(\tau)=\frac{1}{3\tau}+O(\tau^{-2})
\qquad(\tau\to\infty).
\]

## Assumptions and scope

Let \(G=(V,E)\) be a finite simple undirected graph on four vertices, with three edges and connected. Its symmetric adjacency matrix is \(A\). For every vertex \(i\), the state \(v_i(t)\in[0,1]\) evolves by the *N-intertwined mean-field (NIMFA)* equations

\[
\dot v_i=-\delta v_i+\beta(1-v_i)\sum_{j\in V}A_{ij}v_j,
\qquad \beta,\delta>0.
\]

Set \(\tau=\beta/\delta\). At equilibrium,

\[
v_i=\frac{\tau\sum_j A_{ij}v_j}{1+\tau\sum_j A_{ij}v_j}.
\]

The equilibrium quantity compared is \(\sum_i v_i\), *not* the probability that an actual finite-state stochastic SIS process remains infected, and *not* its quasistationary prevalence. In a finite stochastic SIS process without exogenous infection the genuine stationary law is concentrated on total extinction. The comparison is local to this homogeneous, dimensionless, deterministic network model. No demographic or observational inference is asserted.

## Proof

**1. The two graph types and symmetry.** A connected graph on four vertices with three edges is a tree. Degree enumeration gives only \(K_{1,3}\) (degrees \(3,1,1,1\)) or \(P_4\) (degrees \(2,2,1,1\)). Each fixed point with all components positive is unique: if \(v,w>0\) are two different fixed points, interchange their roles if necessary so that \(c=\max_i v_i/w_i>1\), attained at \(i\). The function \(f(z)=\tau z/(1+\tau z)\) is increasing and satisfies \(f(cz)<c f(z)\) for \(z>0\), \(c>1\). Therefore

\[
v_i=f(\sum_j A_{ij}v_j)
\le f(c\sum_j A_{ij}w_j)<c w_i=v_i,
\]

a contradiction. Every strictly positive equilibrium must consequently respect each automorphism of the graph. Also, on a connected graph a nonzero nonnegative fixed point must be strictly positive: a zero component forces every neighbor to be zero. Hence the equations below exhaust all physical nonzero equilibria.

**2. Star equilibrium.** Let \(x\) denote the central occupancy and \(y\) any leaf occupancy. Their fixed-point equations are

\[
x=\frac{3\tau y}{1+3\tau y},\qquad
 y=\frac{\tau x}{1+\tau x}.
\]

Their unique nonzero algebraic solution is

\[
x=\frac{3\tau^2-1}{\tau(3\tau+1)},\qquad
 y=\frac{3\tau^2-1}{3\tau(\tau+1)}.
\]

Both values lie strictly between zero and one exactly when \(\tau>1/\sqrt3\). Below or at that threshold only the physical zero equilibrium exists. Consequently,

\[
S(\tau)=\frac{2(2\tau+1)(3\tau^2-1)}{\tau(\tau+1)(3\tau+1)}
\quad\text{when }\tau>1/\sqrt3.
\]

**3. Path equilibrium.** Let \(u\) denote either endpoint occupancy and \(v\) either internal-node occupancy. Then

\[
u=\frac{\tau v}{1+\tau v},\qquad
v=\frac{\tau(u+v)}{1+\tau(u+v)}.
\]

Set \(q=1+\tau v\). In any positive solution \(q>1\) and

\[
u=1-\frac1q,\qquad v=\frac{q-1}{\tau}.
\]

Substituting into the second equation, canceling the strictly positive factor \(q-1\), and simplifying gives \(q^2=\tau(\tau+1)\). Hence

\[
q=\sqrt{\tau(\tau+1)},\qquad
u=1-\frac1{\sqrt{\tau(\tau+1)}},\qquad
v=\frac{\sqrt{\tau(\tau+1)}-1}{\tau}.
\]

They lie strictly between zero and one if and only if \(\tau(\tau+1)>1\), or \(\tau>(\sqrt5-1)/2\). Thus

\[
P(\tau)=2+2\sqrt{\frac{\tau}{\tau+1}}-\frac2\tau
\quad\text{when }\tau>(\sqrt5-1)/2.
\]

**4. Unique positive crossover.** Since \(1/\sqrt3<(\sqrt5-1)/2<1<\tau_*\), the star is strictly dominant on the interval where it alone has a positive equilibrium. Where both equilibria are positive, write

\[
B(\tau)=\frac{3\tau^2+2\tau+1}{(\tau+1)(3\tau+1)}>0.
\]

Direct reduction of the star expression gives

\[
S(\tau)=2-\frac2\tau+2B(\tau),\qquad
P(\tau)=2-\frac2\tau+2\sqrt{\frac{\tau}{\tau+1}}.
\]

Because both terms whose difference matters are positive, the sign of \(S-P\) is the sign of

\[
B(\tau)^2-\frac{\tau}{\tau+1}
=\frac{(\tau+1)^3-4\tau^3}{(\tau+1)^2(3\tau+1)^2}.
\]

The numerator has the same sign as \((1+1/\tau)^3-4\), which is strictly decreasing from positive values to \(-3\) as \(\tau\) grows. It has precisely one zero, \(\tau_*=(2^{2/3}-1)^{-1}\), and the claimed complete ranking follows. Since \(2^{2/3}<2\), \(\tau_*>1\), safely above the second onset threshold.

**5. Large-transmission limit.** Expansion of the explicit functions gives

\[
S(\tau)=4-\frac{10}{3\tau}+O(\tau^{-2}),\qquad
P(\tau)=4-\frac3\tau+O(\tau^{-2}),
\]

which proves the strict eventual path advantage and its leading coefficient.

## Verification

The separately included `checker.py` uses exact SymPy simplification to test both pairs of stationary equations, the closed forms, the sign-factorization identity, the strong-rate coefficient, and values at \(\tau=1,2\). It also performs 40,000 randomized numeric residual and ordering checks, plus 400 separate full-vector fixed-point iterations, and tests both subcritical branches on a 10,000-point grid. On the packaged version it completed **60,415 assertions**. Those samples are regression tests; the analytical proof above, not finite sampling, establishes the universal quantifiers. Run from the package directory with `python checker.py` after installing SymPy.

For illustrative exact comparisons, at \(\tau=1\), \(S=3/2>\sqrt2=P\); at \(\tau=2\), \(S=55/21<1+2\sqrt{2/3}=P\).

## Relationship to prior work

Van Mieghem, Omic and Kooij (first publicly issued 24 June 2008) introduce and analyze the N-intertwined SIS network approximation and spectral threshold; this analysis relies on their established model rather than claiming it. Van Mieghem (2011), especially Sections 2–3 and Figure 3/Section 5, describes the star equilibrium and a qualitative *different-graph* ranking reversal between a star and an approximately equal-density regular network. These are substantial antecedents: neither spectral threshold separation nor the existence of some ranking reversal is proposed as new here. The narrow assessed claim is the **closed, all-rate and unique crossover classification for the only two equal-edge four-vertex trees**, including the exact algebraic crossing constant and the high-rate signed gap.

Gilarranz and Bascompte (2012) discuss ranking reversals in a stochastic metapopulation colonization/extinction process on large heterogeneous networks; its invariant and mechanism differ from NIMFA endemic infection sums. Li, van de Bovenkamp and Van Mieghem (2012) compare NIMFA and heterogeneous mean field approximations on path and other graphs; the available abstract does not identify this exact two-tree classification, but full text could not be retrieved and remains a priority risk. He (2020, thesis Chapter 5) explicitly derives the general star formula and studies path prevalence through numerical series convergence. The exact special case for four vertices is algebraically tractable, although the general long-path problem is not; the full Chapter 5 relevant sections examined do not state the four-vertex crossover.

## Limitations

This is a small-network, uniform-rate, deterministic mean-field result. The general phenomenon of reversal between epidemic-threshold and prevalence rankings was known. The contribution is an exact minimal tree classification rather than a new spreading theory. No statement about the true stochastic SIS stationary or quasistationary distribution, heterogeneous rates, other graphs, intervention efficacy, or general graph monotonicity is proved. Completeness of literature coverage is not certified: the full Li–van de Bovenkamp–Van Mieghem 2012 manuscript and some earlier network epidemic work were inaccessible. The checked references do not entail the exact crossover, but priority remains provisional pending external review.

## References

1. P. Van Mieghem, J. Omic, R. Kooij, *Virus Spread in Networks*, IEEE/ACM Transactions on Networking 17 (2009), 1–14, **first publicly issued 24 June 2008**. https://doi.org/10.1109/TNET.2008.925623 (lawful PDF: https://www.nas.ewi.tudelft.nl/people/Piet/papers/IEEEToN_virusspread.pdf).
2. P. Van Mieghem, *The N-intertwined SIS epidemic network model*, Computing 93 (2011), 147–169, online 13 October 2011. https://doi.org/10.1007/s00607-011-0155-y (open-access PDF: https://link.springer.com/content/pdf/10.1007/s00607-011-0155-y.pdf).
3. L. J. Gilarranz, J. Bascompte, *Spatial network structure and metapopulation persistence*, Journal of Theoretical Biology 297 (2012), 11–16, first posted 8 December 2011. https://doi.org/10.1016/j.jtbi.2011.11.027.
4. C. Li, R. van de Bovenkamp, P. Van Mieghem, *Susceptible-infected-susceptible model: A comparison of N-intertwined and heterogeneous mean-field approximations*, Physical Review E 86 (2012), 026116. https://doi.org/10.1103/PhysRevE.86.026116.
5. Z. He, *Performance of Complex Networks: Efficiency and Robustness*, TU Delft dissertation (2020), Chapter 5, Sections 5.3.2–5.3.3. https://doi.org/10.4233/uuid:a9ae2b62-0cf8-4cf3-86af-abd33bc99080.
