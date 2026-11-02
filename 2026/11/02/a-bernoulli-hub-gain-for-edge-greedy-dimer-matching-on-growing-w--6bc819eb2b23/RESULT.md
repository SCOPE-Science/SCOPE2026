# A Bernoulli hub gain for edge-greedy dimer matching on growing wheels

## Finding

For each integer \(n\ge3\), form a cycle \(C_n\) with \(n\) rim vertices and a wheel \(W_{n+1}=K_1\vee C_n\) by adjoining a hub adjacent to every rim vertex. Give every edge an independent continuous uniform priority and process the edges in increasing priority, accepting an edge precisely when both endpoints are still unmatched. Couple the two processes by assigning identical priorities to their common rim edges and independent priorities to the additional spokes. Write \(M_n^{\mathrm C}\) and \(M_n^{\mathrm W}\) for the respective final matching sizes, and set \(\Delta_n=M_n^{\mathrm W}-M_n^{\mathrm C}\).

**Theorem.** For every \(n\ge3\), on every realization with distinct priorities, \(\Delta_n\in\{0,1\}\). With
\[
\rho=\frac{1-e^{-2}}2,
\]
the expectations satisfy
\[
\mathbb E M_n^{\mathrm C}=\rho n+o(1),\qquad
\mathbb E M_n^{\mathrm W}=\rho(n+1)+o(1).
\]
Consequently,
\[
\Delta_n\xrightarrow{\mathrm{TV}}\operatorname{Bernoulli}(\rho),
\qquad
\lim_{n\to\infty}\Pr(\Delta_n=1)=\rho\approx0.4323323584.
\]
The comparison is under the specified *common-edge-priority coupling*. It is not an independent difference of two matching-size samples.

## Assumptions and scope

All graphs are finite, simple and undirected. The random priorities on distinct edges are independent and continuous; their common distribution does not affect the edge ordering. A chosen edge permanently occupies both endpoints. Equivalently, at each step an edge is chosen uniformly among all edges whose endpoints remain unmatched. The cycle has \(n\) vertices and the wheel has \(n+1\); for \(n=3\), the wheel is \(K_4\). The limit is through all integers \(n\to\infty\).

The mean formula uses the classical one-dimensional irreversible dimer-deposition constant \(\rho\); novelty is not claimed for this constant alone. The substantive assertion is the coupled, one-bit change caused by a hub of growing degree, with its exact limiting success probability.

## Proof

**1. Deterministic one-vertex stability.** Fix any graph \(G\), a vertex \(v\), and a strict total priority order on the edges of \(G\). Couple greedy matchings on \(G\) and \(G-v\) by the same priorities on common edges. At any point, their sets of unmatched vertices, viewed inside \(V(G)\), are nested and differ by exactly one vertex. Initially the difference is \(\{v\}\). Indeed, processing an edge either changes neither set, changes both sets identically, or consumes the unique extra free vertex and one other common free vertex in just the larger set, reversing which set is larger. The nesting and singleton difference are thus preserved by induction. Since both matched-vertex counts are even, the respective numbers of accepted edges differ by either zero or one. In particular, deleting one vertex can decrease the greedy matching size by at most one and can never increase it.

In the wheel/cycle coupling, before the first accepted spoke the same rim edges are accepted in both processes. If there is no accepted spoke, the matchings coincide. Otherwise, the accepted spoke consumes the hub and a rim vertex \(v\), and future rim edges are processed in the same relative order in both graphs, except that \(v\) is absent from the wheel process. The preceding lemma therefore gives \(\Delta_n\in\{0,1\}\), deterministically. In particular \(\Pr(\Delta_n=1)=\mathbb E M_n^{\mathrm W}-\mathbb E M_n^{\mathrm C}\).

**2. Exact path mean.** Let \(g_m\) be the mean edge-greedy matching size on a path with \(m\) vertices, with \(g_0=g_1=0\). Conditioning on the first selected edge gives, for \(m\ge2\),
\[
g_m=1+\frac{2}{m-1}\sum_{j=0}^{m-2}g_j.
\]
Writing \(G(z)=\sum_{m\ge0}g_m z^m\), multiplying this recurrence by \((m-1)z^{m-2}\) and summing gives the ordinary generating function
\[
G(z)=\frac{z(1-e^{-2z})}{2(1-z)^2}.
\]
Extracting coefficients yields, for \(m\ge1\),
\[
g_m=\frac m2-\frac12\sum_{k=0}^{m-1}\frac{(m-k)(-2)^k}{k!}
=\rho m-e^{-2}+\varepsilon_m,
\]
where \(\varepsilon_m\to0\) superfactorially and \(\sup_{m\ge0}|\varepsilon_m|<\infty\). This follows by extending the finite sum to the exponential series \(e^{-2}\), with a factorially small Taylor tail. The first edge in a cycle deletes its two endpoints, leaving a path on \(n-2\) vertices; hence
\[
\mathbb E M_n^{\mathrm C}=1+g_{n-2}=\rho n+\varepsilon_{n-2},
\]
because \(2\rho+e^{-2}=1\). Thus the asserted cycle asymptotic holds.

**3. The hub is selected before significant rim damage.** Let \(J_n\) count the number of accepted rim edges in the wheel before the first accepted spoke; if no spoke is ever accepted, let \(J_n\) be the total number of accepted rim edges. Whenever there are \(m>0\) unmatched rim vertices and the hub is free, precisely \(m\) spokes are eligible, while at most \(m\) rim edges are eligible. Thus the next accepted edge is a spoke with conditional probability at least \(1/2\). In particular, for every integer \(k\ge0\),
\[
\Pr(J_n\ge k)\le2^{-k},
\]
subject to interpreting \(J_n\ge0\) as certain, and \(\Pr(\text{no accepted spoke})\le2^{-\lfloor n/2\rfloor}\). Hence \(J_n\) is uniformly tight and has uniformly bounded moments.

**4. Separation of the early occupied blocks.** Fix integers \(K,L\ge1\). Until \(K\) accepted rim edges, at least \(n-3K\) rim edges are eligible and at least \(n-2K\) spokes are eligible: each accepted rim edge removes two vertices and at most three distinct rim edges. Conditional on the next accepted edge being of either kind, its location is uniform among eligible edges of that kind. The union bound therefore gives
\[
\Pr(\text{some of the first }K\text{ rim dimers or first hub endpoint are within }L\text{ rim sites of another})
\le O(K^2L/n)
\]
for \(n>4K\), with an absolute implicit constant. This also covers adjacency and wrap-around along the cycle. Together with the preceding geometric tail, we may take \(K\to\infty\), \(L\to\infty\), \(K^2L/n\to0\), so that with probability tending to one the \(J_n+1\) occupied blocks (each dimer is one block and the hub's rim partner is one block) are disjoint and separated by paths of lengths tending uniformly to infinity.

**5. Conditional decomposition at hub selection.** Independent unit exponential clock times on edges induce the same random uniform priority order and, by memorylessness, imply that conditional on the configuration immediately after the first accepted spoke, all remaining eligible rim edges have a fresh independent uniform relative order. If this spoke follows \(j\) accepted rim dimers, the surviving rim graph is a disjoint union of \(q\le j+1\) paths with lengths \(\ell_1,\ldots,\ell_q\) adding up to \(n-2j-1\). Thus the expected total matching size conditional on that configuration is exactly
\[
 j+1+\sum_{h=1}^qg_{\ell_h}
=\rho(n+1)+e^{-2}(j+1-q)+\sum_{h=1}^q\varepsilon_{\ell_h}.
\]
On the good separation event of Step 4, \(q=j+1\) and each path length grows, so this correction vanishes. On the complementary event its absolute value is bounded by a constant multiple of \(j+1\), since \(q\le j+1\) and the \(\varepsilon_m\) are uniformly bounded. The geometric tail of \(J_n\) gives uniform integrability of these bounds. The no-spoke event has probability at most \(2^{-\lfloor n/2\rfloor}\) and contributes at most \(O(n2^{-n/2})\) to the expectation. Consequently, taking expectations in the displayed identity proves
\[
\mathbb E M_n^{\mathrm W}=\rho(n+1)+o(1).
\]

**6. Bernoulli limit.** By Step 1, the coupled difference \(\Delta_n\) is already Bernoulli-valued for each \(n\). Steps 2 and 5 show that its success probability converges to \(\rho\). For Bernoulli variables this is precisely convergence in total variation, proving all assertions.

## Verification

The accompanying `checker.py` implements an exact rational recurrence for paths, a separate exact wheel-state recursion, direct edge-order enumeration for small wheels, and fixed-order exhaustive checks of the vertex-deletion coupling. It performs 49,615 exact assertions and numerical asymptotic diagnostics. The exact finite computations are checks of the formulas and boundary cases, not a substitute for the analytic all-order proof above. Run in a standard Python installation by executing `python checker.py` from the directory containing this file.

## Relationship to prior work

Dyer and Frieze (1991) introduced the same uniform-eligible-edge randomized greedy matching process and proved general performance bounds; the present result is not a new definition of that process. Their paper's abstract is accessible, but its full text was unavailable here. Hertz, Bonte, Devillez and Mélot (2022), Section 5.1, derive wheel results for the **uniform average over all maximal matchings**, explicitly distinguishing that law from greedy-edge output probabilities in their Introduction, so their wheel formulas cannot be substituted for the present law. Pasinetti and collaborators (2019) study random sequential adsorption on Euclidean/fractal substrates and vertex-first adsorption on random networks, obtaining numerical jamming behavior, not the asymptotic *coupled* cycle/wheel edge-priority difference. The one-dimensional constant \(\rho\) is classical; the new comparison concerns its appearance as a Bernoulli increment from adjoining a high-degree hub.

## Limitations

The result is for random **edge-priority** (or uniform-eligible-edge) matching, not for uniformly sampling maximal matchings or for choosing a vertex before choosing its incident edge. The total-variation conclusion pertains to a particular coupled difference, not to independent matching outcomes. The proof provides no full joint central limit theorem, and the limiting positive probability is not an all-size identity. Historical priority remains uncertain because the full 1991 general-process paper was not accessible; the present review is not independent mathematical certification.

## References

- M. Dyer and A. Frieze, *Randomized greedy matching*, Random Structures & Algorithms **2** (1991), 29–45, https://doi.org/10.1002/rsa.3240020104.
- P. M. Pasinetti, L. S. Ramirez, P. M. Centres, A. J. Ramirez-Pastor and G. A. Cwilich, *Random sequential adsorption on Euclidean, fractal and random lattices*, arXiv:1907.02572, first public 2019-07-04, https://arxiv.org/abs/1907.02572.
- A. Hertz, S. Bonte, G. Devillez and H. Mélot, *The average size of maximal matchings in graphs*, arXiv:2204.10236, first public 2022-04-21, https://arxiv.org/abs/2204.10236.
- J. W. Evans, *Random and cooperative sequential adsorption*, Reviews of Modern Physics **65** (1993), 1281–1329, https://doi.org/10.1103/RevModPhys.65.1281.
