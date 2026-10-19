# A rate-driven Braess reversal for one long chord in random dimer adsorption

## Finding

Give every edge of the cycle \(C_n\) an independent exponential arrival clock of rate one. Add one chord joining vertices \(0\) and \(d_n\), with independent exponential clock of rate \(\lambda>0\). Process all edges in increasing arrival-time order, accepting an edge when both its endpoints are unmatched. Let \(M_n(\lambda)\) denote the terminal number of accepted dimers and let \(M_n(0)\) denote the count when the chord is absent.

**Theorem.** If \(2\le d_n\le n-2\), \(d_n\to\infty\), and \(n-d_n\to\infty\), then for each fixed \(\lambda>0\), the following finite expected difference converges:

\[
\lim_{n\to\infty}\left(\mathbb E M_n(\lambda)-\mathbb E M_n(0)\right)
=\mathcal D(\lambda)
=e^{-2}\int_0^1 \lambda(1-x)^{\lambda-1}e^{-2x}(2x-1)\,dx.
\]

The function \(\mathcal D\) is continuous and strictly decreasing on \((0,\infty)\), with

\[
\lim_{\lambda\downarrow0}\mathcal D(\lambda)=e^{-4},\qquad
\mathcal D(1)=-e^{-4},\qquad
\lim_{\lambda\to\infty}\mathcal D(\lambda)=-e^{-2}.
\]

There is exactly one critical rate \(\lambda_*\in(0,1)\), numerically \(\lambda_*\approx0.425946020979\), at which the effect changes sign. In particular, inserting a *unit-rate* chord **decreases** the expected terminal number of dimers by \(e^{-4}+o(1)\), whereas inserting a sufficiently slow positive-rate chord increases it. For an absent chord, the difference is identically zero at every finite order; the positive weak-rate limit therefore reflects the noncommutation of the large-system and zero-chord-rate limits.

## Assumptions and scope

Each edge attempts adsorption only at its first independent exponential-clock time. This is equivalent to repeated Poisson attempts because an attempted edge rejected after either endpoint is occupied can never subsequently be accepted. The chord endpoints become separated by arbitrarily many ordinary edges in both cyclic directions; the theorem does not concern chords of bounded cyclic length. The limiting statement is at each **fixed** positive chord rate and concerns the expected **number** of accepted edges, not the macroscopic dimer-density change (which vanishes).

Write \(x=1-e^{-t}\in[0,1]\) for ordinary-edge time and \(h(x)=e^{-x}\). The transformed density of the chord's first attempt is

\[
\varphi_\lambda(x)=\lambda(1-x)^{\lambda-1},\qquad 0<x<1.
\]

## Proof

**1. Cavity factorization on a tree.** For an oriented tree edge \(u\to v\) with exponential rate \(r_{uv}\), let \(q_{u\to v}(t)\) be the probability that its branch does not attempt to occupy \(v\) successfully by time \(t\) when \(v\) is kept artificially available. Removing \(uv\), the branches incident to \(u\) are independent; conditioning on the clock of \(uv\) therefore gives

\[
q_{u\to v}(t)=1-\int_0^t r_{uv}e^{-r_{uv}s}
 \prod_{w\sim u,\,w\ne v}q_{w\to u}(s)\,ds.
\]

Similarly the chance that edge \(uv\) is accepted at time \(t\) has density

\[
r_{uv}e^{-r_{uv}t}
\prod_{w\sim u,\,w\ne v}q_{w\to u}(t)
\prod_{z\sim v,\,z\ne u}q_{z\to v}(t).
\]

These formulas follow from first-arrival conditioning; there are no independence assumptions between competing claims to the *same* vertex. On a homogeneous one-sided infinite path, the sole cavity message satisfies \(h'= -h\) in transformed time \(x\) and \(h(0)=1\), hence \(h(x)=e^{-x}\). A typical ordinary edge is accepted with probability \(\int_0^1h(x)^2dx=(1-e^{-2})/2\).

**2. The isolated chord defect.** At fixed distance from the chord, the graphs tend to two disjoint bi-infinite paths connected by one bridge. Its endpoints each have two ordinary arms and one bridge. By reflection symmetry the cavity message sent from either endpoint along the bridge is

\[
b(x)=1-\int_0^x\varphi_\lambda(y)h(y)^2\,dy,
\qquad k(x)=1-b(x)=\int_0^x\varphi_\lambda(y)e^{-2y}\,dy.
\]

The bridge's acceptance probability is

\[
P_{\rm bridge}=\int_0^1\varphi_\lambda(x)h(x)^4\,dx.
\]

Along any of the four ordinary rays, let \(m_1\) denote the cavity message from the degree-three endpoint to its first ordinary neighbor, and \(m_j\) the next outgoing message at distance \(j\). Then

\[
m_1(x)=1-\int_0^x h(y)b(y)\,dy,
\qquad m_{j+1}(x)=1-\int_0^x m_j(y)\,dy\quad(j\ge1).
\]

Set \(\delta_j(x)=m_j(x)-h(x)\). The first deviation satisfies \(\delta_1'(x)=h(x)k(x)\), and successive deviations satisfy \(\delta_{j+1}'(x)=-\delta_j(x)\), with \(\delta_j(0)=0\). Their sum \(S(x)=\sum_{j\ge1}\delta_j(x)\) converges uniformly on \([0,1]\) by the factorial bounds obtained by iterating integration. It obeys

\[
S'(x)=h(x)k(x)-S(x),\qquad
S(x)=e^{-x}\int_0^x k(y)\,dy.
\]

The edge immediately adjacent to the bridge is accepted with probability \(\int_0^1h(x)^2b(x)dx\). Every more distant arm edge, indexed \(j\ge2\), has acceptance probability \(\int_0^1h(x)m_{j-1}(x)dx\). Thus the total excess expected number of occupied edges contributed by one ray over its homogeneous comparison is

\[
\mathcal A=\int_0^1 e^{-2x}\left[-k(x)+\int_0^xk(y)\,dy\right]dx.
\]

Accounting for four rays and the new bridge yields \(\mathcal D=P_{\rm bridge}+4\mathcal A\). Fubini's theorem gives, for each \(0\le y\le1\),

\[
\int_y^1e^{-2x}(x-y-1)dx
=\frac{e^{-2}}4(2y-1)-\frac{e^{-2y}}4.
\]

Using \(k(x)=\int_0^x\varphi_\lambda(y)e^{-2y}dy\), the terms \(-\int_0^1\varphi_\lambda(y)e^{-4y}dy\) and \(P_{\rm bridge}\) cancel, leaving precisely the claimed integral for \(\mathcal D\).

**3. From long cycles to the isolated defect.** Couple the with-chord and without-chord processes using the same ordinary-edge clocks. For an ordinary edge at line-graph distance at least \(r\) from the chord, changing the chord can affect its fate only if there is a path of \(r\) or more consecutively earlier ordinary-edge priorities connecting it to the chord. The line graphs have maximum degree at most four; the number of possible length-\(r\) paths is at most \(4^r\), while a specified sequence of \(r\) iid continuous ordinary clocks has probability at most \(1/r!\) of lying in the necessary strict order. Hence the probability of a remote influence is bounded by \(4^r/r!\), uniformly in \(n\) and in the positive chord rate. There are at most a constant number of ordinary cycle edges at each fixed line-graph distance from the chord, so the sum of expected differences outside radius \(R\) is dominated by \(C\sum_{r\ge R}4^r/r!\to0\). Inside each fixed radius, both cyclic arcs tend to disjoint infinite rays under the separation hypotheses; coupling and the same factorial bound identify the limiting local expectation. This proves convergence of the total expected difference to the tree value.

**4. A unique rate reversal.** Let \(U_\lambda\) have distribution \(\operatorname{Beta}(1,\lambda)\); its density is \(\varphi_\lambda\). Then

\[
\mathcal D(\lambda)=e^{-2}\mathbb E[g(U_\lambda)],
\qquad g(u)=e^{-2u}(2u-1),
\qquad g'(u)=4(1-u)e^{-2u}>0\quad(0\le u<1).
\]

The tail \(\mathbb P(U_\lambda>u)=(1-u)^\lambda\) strictly decreases in \(\lambda\) for \(0<u<1\). Strict stochastic ordering thus makes \(\mathcal D\) strictly decreasing. Weak convergence \(U_\lambda\Rightarrow1\) as \(\lambda\downarrow0\) and \(U_\lambda\Rightarrow0\) as \(\lambda\to\infty\) gives the endpoint values. Direct elementary integration at \(\lambda=1\) yields \(\mathcal D(1)=-e^{-4}\). Continuity and the intermediate-value theorem give a unique zero; numerical quadrature gives the stated rate.

## Verification

The accompanying `verify.py` implements an exact first-clock decomposition of the finite-graph stochastic process: condition on the first arriving edge, remove both its endpoints, and recurse on the remaining weighted edge set. It independently computes the limiting integral by midpoint quadrature in beta-quantile coordinates and compares its values against the finite cycle with twenty vertices and an antipodal chord at four distinct rates. The code tests strict rate ordering, the positive/negative sign change, the special value \(-e^{-4}\), and both extreme-rate limits. Run `python verify.py` using Python 3; no additional dependencies are required. These numerical checks are supplementary to the infinite-volume proof.

## Relationship to prior work

The classical literature establishes random sequential adsorption of dimers and randomized greedy matchings. Pippenger (1989) treats RSA on graphs; Evans (1993) reviews exact one-dimensional adsorption methods; Dyer and Frieze (1991) analyze randomized greedy matching; Miller and Pritikin (1997) provide bounds for weighted greedy matchings. Gamarnik and Goldberg (2009, first preprint 2008) rigorously study weighted and unweighted randomized greedy matchings on regular graphs, and Krivelevich, Mészáros, Michaeli, and Shikhelman (2024, first published 2023) study random greedy independent sets through local limits, noting the line-graph reduction for matchings. These establish context and methods, but their inspected statements do not explicitly give the **order-one signed adsorption defect** generated by a single isolated long-range chord, its exact rate integral, or its unique sign reversal. General correlation-decay techniques alone describe locality, not the evaluated defect constant. Relevant older full text was not uniformly available, so absolute novelty is not claimed.

## Limitations

This is an expectation theorem for a single added chord with asymptotically separated endpoints, not a finite-order monotonicity assertion. Finite graphs need not have precisely the limiting sign at the threshold. The baseline rates are exactly one and the chord rate is fixed as size grows. Neither concentration of the count difference nor an error bound uniform over all positive chord rates is established. One older foundational paper on graph RSA and some weighted-greedy-matching publications remained inaccessible in full text; potential equivalent formulations therein are an originality risk. No independent scientific audit has been performed.

## References

- P. Schaaf and J. Talbot, “Kinetics of Random Sequential Adsorption,” *Physical Review Letters* 62, 175 (1989), doi:10.1103/PhysRevLett.62.175 (published 1989-01-09).
- N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* 2, 393–401 (1989), doi:10.1137/0402034.
- M. Dyer and A. Frieze, “Randomized greedy matching,” *Random Structures & Algorithms* 2, 29–45 (1991), doi:10.1002/rsa.3240020104.
- J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* 65, 1281 (1993), doi:10.1103/RevModPhys.65.1281.
- Z. Miller and D. Pritikin, “On randomized greedy matchings,” *Random Structures & Algorithms* 10, 353–383 (1997), doi:10.1002/(SICI)1098-2418(199705)10:3<353::AID-RSA5>3.0.CO;2-V.
- D. Gamarnik and D. A. Goldberg, “Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections,” *Combinatorics, Probability and Computing* 19, 61–85 (2010); arXiv:0807.1277 (first public version 2008).
- M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, “Greedy maximal independent sets via local limits,” *Random Structures & Algorithms* 64, 986–1015 (2024), doi:10.1002/rsa.21200.
