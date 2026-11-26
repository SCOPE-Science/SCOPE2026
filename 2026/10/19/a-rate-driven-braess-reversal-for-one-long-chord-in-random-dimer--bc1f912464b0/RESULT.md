# A rate-driven Braess reversal for one long chord in random dimer adsorption

## Finding

Give each edge of the cycle \(C_n\) an independent exponential arrival clock of rate one. Add a chord joining vertices \(0\) and \(d_n\), with independent exponential clock of rate \(\lambda>0\). Process edges in increasing arrival order, accepting an edge if both endpoints are unmatched. Let \(M_n(\lambda)\) be the terminal number of accepted dimers, let \(M_n(0)\) denote the count when the chord is absent, and put \(\Delta_n(\lambda)=\mathbb E M_n(\lambda)-\mathbb E M_n(0)\).

**Theorem.** Suppose \(2\le d_n\le n-2\), \(d_n\to\infty\), and \(n-d_n\to\infty\). For each fixed \(\lambda>0\),
\[
 \lim_{n\to\infty}\Delta_n(\lambda)=\mathcal D(\lambda)
 =e^{-2}\int_0^1\lambda(1-x)^{\lambda-1}e^{-2x}(2x-1)\,dx.
\]
The function \(\mathcal D\) is continuous and strictly decreasing on \((0,\infty)\), with
\[
 \lim_{\lambda\downarrow0}\mathcal D(\lambda)=e^{-4},\qquad
 \mathcal D(1)=-e^{-4},\qquad
 \lim_{\lambda\to\infty}\mathcal D(\lambda)=-e^{-2}.
\]
There is exactly one critical rate \(\lambda_*\in(0,1)\), numerically \(\lambda_*\approx0.425946020979\). A unit-rate chord decreases the expected terminal count by \(e^{-4}+o(1)\), whereas a sufficiently slow positive-rate chord increases the limiting expected count. The two iterated limits through **positive** rates agree:
\[
 \lim_{\lambda\downarrow0}\lim_{n\to\infty}\Delta_n(\lambda)
 =\lim_{n\to\infty}\lim_{\lambda\downarrow0}\Delta_n(\lambda)
 =e^{-4}.
\]
In contrast, \(\Delta_n(0)=0\) by the no-chord convention. A vanishing positive rate makes the chord attempt arbitrarily late, rather than removing its attempt from the terminal process.

## Assumptions and scope

Attempts after the first clock of the same edge cannot affect the result: once an edge is rejected because an endpoint is occupied, that endpoint remains occupied. Both cyclic arcs between the chord endpoints must diverge in length. The result concerns an order-one change in the expected **number** of accepted edges, not a nonzero change in limiting dimer density. For ordinary edges the transformed arrival variable \(x=1-e^{-t}\) is uniform on \([0,1]\). The transformed chord density is \(\varphi_\lambda(x)=\lambda(1-x)^{\lambda-1}\).

## Proof

**1. Cavity factorization on a tree.** For an oriented tree edge \(u\to v\), write \(q_{u\to v}(t)\) for the probability that its branch has not made a successful attempt on \(v\) by time \(t\) in the cavity experiment in which \(v\) is always available to this branch. If the edge has rate \(r_{uv}\), first-arrival conditioning and branch independence give
\[
 q_{u\to v}(t)=1-\int_0^t r_{uv}e^{-r_{uv}s}
 \prod_{w\sim u,\ w\ne v}q_{w\to u}(s)\,ds.
\]
The acceptance-time density of edge \(uv\) is
\[
 r_{uv}e^{-r_{uv}t}\prod_{w\sim u,\ w\ne v}q_{w\to u}(t)
 \prod_{z\sim v,\ z\ne u}q_{z\to v}(t).
\]
Indeed, a vertex remains free up to the first successful attempt into it in the separate cavity experiments. No independence of the actual acceptance events competing for the same vertex is needed. In transformed time the single homogeneous half-line message \(h\) satisfies \(h'=-h\), \(h(0)=1\), so \(h(x)=e^{-x}\). A typical ordinary edge is accepted with probability \(\int_0^1h(x)^2dx=(1-e^{-2})/2\), and a vertex between two homogeneous half-lines is unmatched at the end with probability \(h(1)^2=e^{-2}\).

**2. The isolated chord defect.** In the limit the neighborhood of the chord is two bi-infinite paths connected by a single bridge. Each bridge endpoint has two homogeneous half-line arms. From either endpoint the cavity message along the bridge is
\[
 b(x)=1-\int_0^x\varphi_\lambda(y)h(y)^2\,dy,
 \qquad k(x)=1-b(x).
\]
The probability of accepting the bridge is \(P_{\mathrm{bridge}}=\int_0^1\varphi_\lambda(x)h(x)^4\,dx\).

On any arm write \(m_1\) for the cavity message from the bridge endpoint toward its first ordinary neighbor, and \(m_2,m_3,\ldots\) for the successive messages in the same direction. Then
\[
 m_1(x)=1-\int_0^x h(y)b(y)\,dy,\qquad
 m_{j+1}(x)=1-\int_0^x m_j(y)\,dy.
\]
For \(\delta_j=m_j-h\) this gives \(\delta_1'=hk\) and \(\delta_{j+1}'=-\delta_j\), with \(\delta_j(0)=0\). Since \(0\le hk\le1\), repeated integration gives \(|\delta_j(x)|\le x^j/j!\). The sum \(S=\sum_{j\ge1}\delta_j\) therefore satisfies \(S'=hk-S\), \(S(0)=0\), so \(S(x)=e^{-x}\int_0^x k(y)\,dy\).

The bridge-adjacent arm edge is accepted with probability \(\int_0^1 h(x)^2b(x)\,dx\). The \(j\)-th edge, \(j\ge2\), is accepted with probability \(\int_0^1 h(x)m_{j-1}(x)\,dx\). Subtracting the homogeneous probability from each and summing gives one arm's net contribution
\[
 \mathcal A=\int_0^1e^{-2x}\left[-k(x)+\int_0^x k(y)\,dy\right]dx.
\]
The total contribution is \(P_{\mathrm{bridge}}+4\mathcal A\). By Fubini, using the definition of \(k\) and
\[
 \int_y^1e^{-2x}(x-y-1)\,dx=\frac{e^{-2}}4(2y-1)-\frac{e^{-2y}}4,
\]
the term \(-\int_0^1\varphi_\lambda(y)e^{-4y}\,dy\) in \(4\mathcal A\) cancels \(P_{\mathrm{bridge}}\). What remains is the stated integral.

**3. Localization from finite cycles.** Use the same ordinary clocks with and without the chord. Regard greedy matching as greedy independent set on the line graph: an edge's status depends only on earlier neighboring edges. A change in status can therefore propagate only along paths of strictly decreasing clocks when traced from the edge back toward the chord. If an ordinary edge is at line-graph distance at least \(r\) from the chord, the dependency path must begin with at least \(r\) ordinary clocks in descending order. The line graph has maximum degree four, so a union bound gives probability at most \(4^r/r!\), independent of \(n\) and the positive chord rate. There are at most four ordinary edges at any given distance from the chord, as seen by walking along the two cyclic arcs in both directions. Thus the expected defect outside radius \(R\) is bounded in absolute value by \(4\sum_{r\ge R}4^r/r!\).

Within any fixed radius the ordinary arcs converge to the four disjoint arms of the bridge. To identify the limiting status of a fixed edge, first compute it in a finite neighborhood, then enlarge that neighborhood. A disagreement with the full-graph status requires a descending dependency path exiting the neighborhood; the same factorial bound applies, using the ordinary clocks along the path (at most one clock is the chord's). This also defines the infinite-tree status and justifies the cavity calculation. Taking the local limit and then sending \(R\to\infty\) proves convergence of the total defect.

**4. Strict reversal.** The chord's transformed arrival has distribution \(U_\lambda\sim\mathrm{Beta}(1,\lambda)\). For \(g(u)=e^{-2u}(2u-1)\) one has \(g'(u)=4(1-u)e^{-2u}\); thus \(g\) is strictly increasing on \([0,1]\). The tail \(\Pr(U_\lambda>u)=(1-u)^\lambda\) strictly decreases with \(\lambda\) for all \(0<u<1\). Hence \(\mathcal D(\lambda)=e^{-2}\mathbb E g(U_\lambda)\) strictly decreases. The representation \(U_\lambda=1-V^{1/\lambda}\) for one uniform \(V\in(0,1)\), with bounded \(g\), gives continuity and both endpoint limits. The integral at \(\lambda=1\) is evaluated using the primitive \(-u e^{-2u}\), giving \(-e^{-4}\). Strict decrease and the endpoint signs imply exactly one zero. For numerical evaluation one may substitute \(y=1-u\), expand the exponential, and use
\[
 \mathcal D(\lambda)=e^{-4}\lambda\sum_{j=0}^{\infty}\frac{2^j}{j!}
 \left(\frac1{\lambda+j}-\frac2{\lambda+j+1}\right).
\]
The expansion is justified by uniform absolute convergence of the exponential series times the integrable factor \(y^{\lambda-1}\). The absolute truncation error is bounded by \(e^{-4}\sum_{j\ \text{omitted}}2^j/j!\), since \(|1-2y|\le1\) on \([0,1]\).

**5. Weak positive rate at fixed cycle size.** Write the chord clock as \(E/\lambda\) for a common independent rate-one exponential \(E>0\). At fixed \(n\), as \(\lambda\downarrow0\) the chord eventually arrives after the last ordinary clock almost surely. On that event the count difference is the indicator that both chord endpoints are unmatched in the ordinary terminal matching. For fixed \(n\) the count difference is bounded, so
\[
 \lim_{\lambda\downarrow0}\Delta_n(\lambda)
 =\Pr(0\text{ and }d_n\text{ are both unmatched on } C_n).
\]
The latter probability tends to \(e^{-4}\). For a fixed truncation radius, the neighborhoods of the two endpoints are disjoint for all sufficiently large \(n\), hence the two truncated vacancy events are independent. Each vacancy event is determined by its incident edge statuses; the descending-path bound of part 3 makes the truncation error tend to zero as the radius grows, uniformly in such \(n\). The limiting full-path vacancy probability is \(h(1)^2=e^{-2}\) from part 1, so the product is \(e^{-4}\). Together with part 4 this proves the equality of the iterated limits. Setting the chord rate to zero in the sense of omitting the edge is not taking the right limit after running the process to its terminal state.

## Verification

The accompanying standard-library `verify.py` implements the exponential first-arrival recursion for finite graphs, evaluating it in floating-point arithmetic. It conditions on the first edge, removes its endpoints and invokes the memoryless property for the remaining clocks. It compares four rates for the twenty-vertex cycle with its antipodal chord against quadrature in beta-quantile coordinates. These checks are supplementary and do not prove the infinite-volume limit, the iterated limits, or uniqueness of the critical rate. The convergent series in part 4 gives a separate way to compute the zero by bisection.

## Relationship to prior work

Classical random sequential adsorption and greedy matching works establish the setting, one-dimensional adsorption methods and dependency-path bounds. In particular, Gamarnik and Goldberg treat correlation decay for random greedy matchings on regular graphs, and Krivelevich, Mészáros, Michaeli and Shikhelman give the line-graph reduction and local-limit priority-path bounds. These methods do not by themselves evaluate the signed sum of acceptance-probability differences created by a single added bridge. The contribution here is the exact order-one signed defect integral for a long chord, and the unique sign reversal as a function of its rate, not a new general nonmonotonicity principle. Related short-chord results for greedy **vertex** independent sets on cycles concern a different process; on the line graph, adding the original chord adds a vertex adjacent to four ordinary-edge vertices. Changing the rate of an existing bond on a path and adding a hub with spokes at every cycle vertex are different perturbations from the one studied here.

## Limitations

The formula is for a fixed positive chord rate and both cyclic arc lengths tending to infinity; the weak-rate statement above concerns the two iterated limits. The theorem is not a claim that the finite-cycle sign always matches the limiting sign or changes monotonically in the rate. It does not address bounded-length chords or give concentration of the count difference. Some older full texts on graph adsorption and weighted greedy matching could not be inspected; historical priority is not asserted exhaustively.

## References

- P. Schaaf and J. Talbot, “Kinetics of Random Sequential Adsorption,” *Physical Review Letters* 62, 175 (1989), doi:10.1103/PhysRevLett.62.175.
- N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* 2, 393–401 (1989), doi:10.1137/0402034.
- M. Dyer and A. Frieze, “Randomized greedy matching,” *Random Structures & Algorithms* 2, 29–45 (1991), doi:10.1002/rsa.3240020104.
- J. W. Evans, “Random and cooperative sequential adsorption,” *Reviews of Modern Physics* 65, 1281 (1993), doi:10.1103/RevModPhys.65.1281.
- Z. Miller and D. Pritikin, “On randomized greedy matchings,” *Random Structures & Algorithms* 12, 353–383 (1997), doi:10.1002/(SICI)1098-2418(199705)10:3<353::AID-RSA5>3.0.CO;2-V.
- D. Gamarnik and D. A. Goldberg, “Randomized greedy algorithms for independent sets and matchings in regular graphs: Exact results and finite girth corrections,” *Combinatorics, Probability and Computing* 19, 61–85 (2010), arXiv:0807.1277.
- M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, “Greedy maximal independent sets via local limits,” *Random Structures & Algorithms* 64, 986–1015 (2024), arXiv:1907.07216.
