# Sharp path-count laws for forward-loop-erased ants on parallel-route networks

## Finding

Consider the forward-loop-erased reinforcement walk on a graph formed from \(k\ge 2\) internally vertex-disjoint paths joining a nest \(N\) to food \(F\), with respective integer lengths \(\ell_1,\ldots,\ell_k\ge3\). Initially every edge has weight one. Each ant takes the current conductance-weighted random walk from \(N\) until its first visit to \(F\), and every edge in the *chronological forward loop-erasure* of that walk receives weight one more. Let \(A_i(n)\) be the number of the first \(n\) ants whose erased paths equal route \(i\).

Put \(m=\min_i\ell_i\), \(I=\{i:\ell_i=m\}\), \(h=|I|\), and \(r_i=m/\ell_i\). On one probability space there exist independent standard exponential random variables \(E_1,\ldots,E_k\), with \(S=\sum_{j\in I}E_j\), for which the following **joint almost-sure limits** hold:

\[
\frac{A_i(n)}{n}\longrightarrow\frac{E_i}{S}\quad(i\in I),
\qquad
\frac{A_i(n)}{n^{r_i}}\longrightarrow E_iS^{-r_i}\quad(i\notin I).
\]

These limits characterize the joint law of the original ant process (via a coupling). In particular, every nonshortest route is chosen infinitely often, but its fraction tends to zero at the sharp polynomial exponent \(r_i<1\). The limiting allocation among the \(h\) shortest routes is \(\operatorname{Dirichlet}(1,\ldots,1)\) and is strictly positive in every coordinate. Every normalized edge weight therefore converges almost surely.

For a nonshortest route \(i\), its limiting amplitude \(V_i=E_iS^{-r_i}\) has, for \(x\ge0\),

\[
\mathbb P(V_i\le x)=1-\frac1{\Gamma(h)}\int_0^\infty t^{h-1}e^{-t-xt^{r_i}}\,dt.
\]

For \(q\ge0\), its moments satisfy the *sharp integrability threshold*

\[
\mathbb E[V_i^q]=
\frac{\Gamma(1+q)\Gamma(h-r_iq)}{\Gamma(h)}
\quad\text{if }r_iq<h,
\qquad
\mathbb E[V_i^q]=+\infty\quad\text{if }r_iq\ge h.
\]

## Assumptions and scope

The graph is finite, undirected, simple, and **consists exactly** of the given parallel routes, whose interior vertices are disjoint. There are no extra inter-route edges or chords. Each route has at least three edges; lengths may coincide. All edges start with conductance weight one, an ant updates weights only after reaching \(F\), and the erased route is formed chronologically from \(N\) to \(F\). Ant trajectories are conditionally independent given the current weights. Each reinforced path necessarily equals exactly one whole route. No assertion is made for networks with cross-links, general series-parallel compositions, or different erasure/reinforcement protocols.

## Proof

**Step 1: exact transition probabilities.** Because every reinforced path is one full route, after \(n\) ants all edges on route \(i\) have a common weight \(w_i(n)=A_i(n)+1\). Conditional on the weights, consider the next walk's excursions from \(N\), each ending on the first subsequent visit to \(N\) or \(F\). An excursion begins along route \(i\) with probability \(w_i/\sum_jw_j\). Starting from its first interior vertex, its chance of reaching \(F\) before returning to \(N\) is exactly \(1/\ell_i\): interior transitions have equal weights in the two directions, and the discrete harmonic function along this route has boundary values zero and one. The walk's first successful excursion therefore uses route \(i\) with conditional probability

\[
p_i(n)=\frac{(A_i(n)+1)/\ell_i}{\sum_{j=1}^k(A_j(n)+1)/\ell_j}.
\]

Every failed excursion returning to \(N\) is erased by the chronological loop-erasure; the last excursion, which reaches \(F\) without revisiting \(N\), stays within one route, and its loop-erasure is precisely that whole route. Thus \(p_i(n)\) is the *exact* probability that route \(i\) receives reinforcement, not an approximation or mean-field closure. The same probability follows independently from the weighted-spanning-tree representation: in every spanning tree one route is intact and exactly one edge is removed from each other route; summing the tree weights gives intact-route probabilities proportional to \(w_i/\ell_i\).

**Step 2: independent pure-birth embedding.** Let \(Y_1(t),\ldots,Y_k(t)\) be independent continuous-time Yule processes, each started at one and jumping from population \(y\) to \(y+1\) with rate \(y/\ell_i\). At any superposed birth, the conditional chance of a type-\(i\) birth is its rate divided by the total rate. Consequently the embedded sequence of birth colors has *exactly* the transition kernel in Step 1. There is no explosion, since the combined instantaneous rate at total population \(z\) is bounded by \(z/m\); equivalently a linear pure-birth process dominates it. If \(\tau_n\) is the time of its \(n\)-th birth, then jointly in law

\[
Y_i(\tau_n)=A_i(n)+1,\qquad\sum_iY_i(\tau_n)=n+k,
\qquad\tau_n\longrightarrow\infty.
\]

**Step 3: positive Yule martingale limits.** For each \(i\), \(e^{-t/\ell_i}Y_i(t)\) is a nonnegative martingale. The exact geometric distribution

\[
\mathbb P(Y_i(t)=z)=e^{-t/\ell_i}(1-e^{-t/\ell_i})^{z-1},\qquad z=1,2,\ldots,
\]

shows that its limit \(E_i\) has the standard exponential distribution. In particular it is positive almost surely; the independent processes give independent limits. Martingale convergence and the explicit finite-time law together justify the almost-sure and distributional assertions without relying on finite-time simulation.

**Step 4: invert the total population.** If \(\ell_i>m\), then

\[
e^{-t/m}Y_i(t)
=e^{-(1/m-1/\ell_i)t}\bigl(e^{-t/\ell_i}Y_i(t)\bigr)
\longrightarrow0.
\]

The shortest-route terms instead converge to their respective \(E_i\). Hence

\[
e^{-\tau_n/m}(n+k)=e^{-\tau_n/m}\sum_iY_i(\tau_n)\longrightarrow S>0.
\]

For a shortest route \(i\), division by this identity gives \(Y_i(\tau_n)/(n+k)\to E_i/S\). For a longer route with \(r_i=m/\ell_i\), raising the total-population identity to power \(r_i\) yields

\[
\frac{Y_i(\tau_n)}{(n+k)^{r_i}}
=\frac{e^{-\tau_n/\ell_i}Y_i(\tau_n)}{
  [e^{-\tau_n/m}(n+k)]^{r_i}}
\longrightarrow E_iS^{-r_i}.
\]

Subtracting the initial one and replacing \(n+k\) by \(n\) leaves every limit unchanged. The finitely many limits hold jointly. Because \(E_i,S>0\), each long-route count grows without bound on the indicated sublinear scale. For the shortest routes, the independent-exponential normalization gives the stated Dirichlet vector. Since edge weight equals \(1+A_i(n)\), the same conclusions give edge-weight convergence after division by \(n\).

**Step 5: laws of the random amplitudes.** The sum of \(h\) independent exponentials has a \(\operatorname{Gamma}(h,1)\) distribution, and it is independent of every long-route \(E_i\). Conditioning on \(S=t\) proves the displayed cumulative distribution function. Independence and gamma integrals yield

\[
\mathbb E[E_i^qS^{-r_iq}]
=\Gamma(1+q)\frac{\Gamma(h-r_iq)}{\Gamma(h)}
\]

when \(r_iq<h\). When \(r_iq\ge h\), the integral of \(t^{h-1-r_iq}\) near zero diverges, giving an infinite moment. This proves all assertions.

## Verification

The standalone standard-library script `verify.py` brute-force enumerates weighted spanning trees for several two-terminal parallel-route graphs (including unequal and tied lengths) and compares exact rational intact-route probabilities with \((w_i/\ell_i)/\sum_j(w_j/\ell_j)\). It also checks the one-dimensional gambler's-ruin harmonic identity, the embedded birth-color probabilities, and elementary gamma-moment identities. The supplied script was run successfully; it reports 262 exact checks. These finite checks do **not** certify the almost-sure statements, which rest on the proof above.

## Relationship to prior work

Armfield and Mailler [1, §§1.1–1.3 and 2.4–2.5] introduced the forward-loop-erased ant process, gave its weighted-spanning-tree representation, and proved general-graph shortest-path selection when the nest-to-food distance is two. They explicitly identify higher graph distance and process convergence as remaining problems. On the highly structured parallel-route family, the exact excursion computation permits a stronger analysis at distance at least three.

Kious, Mailler, and Schapira [2, Theorem 1.3 and Proposition 2.5] prove geodesic selection and convergence on series-parallel graphs for the *backward* loop-erased protocol. Thus the mere existence of a geodesic limit on our graph family is not claimed as a new general series-parallel phenomenon. Their results do not state the joint precise polynomial path-count limits, gamma ratios, or sharp moments obtained here. The Yule embedding is a familiar tool in reinforced-urn theory [2,3]; the specific route-selection identity supplies the link to this model.

## Limitations

The theorem treats only parallel networks without chords and starting weights exactly one. Known general convergence results for a different erasure convention and general urn-limit technology mean that this is a structured-model result, not a solution to the global shortest-path conjecture; the priority of any equivalent special-case formulation in older urn or ant literature remains open to independent assessment. The almost-sure coupling does not quantify finite-\(n\) approximation errors. The cited doctoral-thesis abstract [4] discusses the process, but its complete text was inaccessible for a comprehensive overlap comparison.

## References

[1] W. Armfield and C. Mailler, *The forward-loop-erased ants walk*, arXiv:2610.18453v1 (first public submission 2026-10-13), https://arxiv.org/html/2610.18453v1.

[2] D. Kious, C. Mailler, and B. Schapira, *Finding geodesics on graphs using reinforcement learning*, Annals of Applied Probability 32 (2022), 3889–3929, arXiv:2010.04820, https://arxiv.org/abs/2010.04820.

[3] B. Jiang, D. R. Figueiredo, B. Ribeiro, and D. Towsley, *On the Duration and Intensity of Competitions in Nonlinear Pólya Urn Processes with Fitness*, arXiv:1604.02097 (2017), https://arxiv.org/abs/1604.02097.

[4] W. Armfield, *An Analysis of Learning Processes Through Reinforced Random Walks*, doctoral thesis, University of Bath (2026), https://researchportal.bath.ac.uk/en/studentTheses/an-analysis-of-learning-processes-through-reinforced-random-walks/.
