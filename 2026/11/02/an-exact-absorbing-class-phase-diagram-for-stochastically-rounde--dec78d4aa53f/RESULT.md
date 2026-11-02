# An exact absorbing-class phase diagram for stochastically rounded logistic dynamics on 16-bit uniform grids

## Finding
Consider a finite uniform grid and apply a single unbiased stochastic rounding operation to the exact parameter-four logistic map. Across **every grid denominator up to the 16-bit cutoff**, the closed communicating classes are classified solely by divisibility by four:

\[
\mathcal C_N=\begin{cases}
\{\{0\}\},&4\nmid N,\\
\{\{0\},\{3/4\}\},&4\mid N.
\end{cases}
\]

Every trajectory is eventually absorbed in these classes with probability one. For \(4\nmid N\), the unique stationary probability is \(\delta_0\); for \(4\mid N\), the stationary simplex is \(\{(1-t)\delta_0+t\delta_{3/4}:0\le t\le1\}\). In particular, the adjacent denominators \(65535\) and \(65536\) have different stationary-simplex dimensions.

The quantitative long-time discrepancy from the continuum chaotic invariant law \(\rho\) is
\[
W_1(\delta_0,\rho)=\frac12,
\qquad
\min_{0\le t\le1}W_1((1-t)\delta_0+t\delta_{3/4},\rho)
=\frac1{12}+\frac{\arcsin\sqrt{3/8}+\sqrt3-\sqrt{15}/2}{2\pi}
\approx0.15568790319968789436.
\]
The minimizer places mass \(1-2\arcsin\sqrt{3/8}/\pi\) at \(3/4\).

## Assumptions and scope
Let \(N\) be any **integer** with \(2\le N\le65536\), and \(G_N=\{j/N:0\le j\le N\}\). The exact real logistic expression is \(f(x)=4x(1-x)\). Set \(y=f(j/N)\), \(a=\lfloor Ny\rfloor\), and \(b=\lceil Ny\rceil\). If \(a=b\), the next state is \(a/N\) with probability one; otherwise the next state is \(a/N\) with probability \(b-Ny\) and \(b/N\) with probability \(Ny-a\). Fresh independent roundings are used on successive steps. Thus \(\mathbb E[X_{k+1}\mid X_k]=f(X_k)\) but the chain is **not** a floating-point or multistage-arithmetic implementation. Endpoints zero and one are both representable.

Let \(\tau_N\) be the first hitting time of the set \(A_N=\{0\}\) if \(4\nmid N\), or \(A_N=\{0,3/4\}\) if \(4\mid N\). The comparison continuum law has density \(1/[\pi\sqrt{x(1-x)}]\) on \((0,1)\). Wasserstein distance is computed using the ordinary Euclidean distance on \([0,1]\).

## Proof
**Exact directed support.** At state \(j/N\), integer arithmetic yields
\[
Ny=\frac{4j(N-j)}{N},\quad a=\left\lfloor\frac{4j(N-j)}{N}\right\rfloor,\quad b=\left\lceil\frac{4j(N-j)}{N}\right\rceil.
\]
There is a positive-probability directed edge to each distinct integer index in \(\{a,b\}\). If \(a=b\), the single edge has probability one. Since \(0\le4j(N-j)\le N^2\), all edges remain in the grid. The product is at most \(4(65536)^2<2^{35}\), so the unsigned 64-bit integer operations in `verify.cpp` do not overflow.

The complete finite certificate performs the following deterministic operation **for each** \(N\in\{2,3,\ldots,65536\}\): enumerate all \(N+1\) vertices and their one or two outgoing support edges; create the reverse adjacency lists; breadth-first search backward from vertex zero; check, vertex by vertex, that the set *not* reaching zero is empty when \(4\nmid N\), and exactly \(\{N/4,3N/4\}\) when \(4\mid N\). This is an exhaustive finite algorithm rather than sampling. Its proof of exhaustive coverage uses the explicit loop bounds, the exact floor/ceiling formula, complete integer-indexed adjacency arrays, and the per-vertex comparison to the predicted set. The four independently completed denominator blocks are documented under Verification. Their maximum observed shortest path to zero is 27, with a common global upper bound 27.

**Absorbing classes.** Zero is fixed. If \(4\mid N\), the grid also contains \(1/4\), which maps deterministically to \(3/4\), and \(3/4\), which maps to itself; neither can reach zero. Thus the two non-zero-reaching states found by the certificate comprise one transient feeder and one absorbing singleton. Every other vertex admits a directed path to zero. A closed communicating class disjoint from zero (or \(3/4\) if present) would contain a state admitting a path outside the class to zero, a contradiction. All remaining states are transient in a finite Markov chain. Because every transient vertex has a positive-probability route to an absorbing class of at most 27 edges, its absorption time is almost surely finite. In fact every positive transition probability is at least \(1/N\), so for each integer \(m\ge0\),
\[
\mathbb P(\tau_N>27m)\le(1-N^{-27})^m.
\]
All invariant probabilities of a finite chain are convex mixtures of its closed-class invariant probabilities, proving the asserted simplex.

**Sharp discrepancy.** The continuum logistic map at parameter four has invariant density \(\rho(x)=1/(\pi\sqrt{x(1-x)})\) and mean \(1/2\), giving \(W_1(\delta_0,\rho)=\int x\,\rho(dx)=1/2\). For measures supported on \(\{0,3/4\}\), the least Wasserstein cost is obtained by transporting each continuum location to its closer support site, breaking the tie at \(3/8\). The optimal mass at \(3/4\) equals \(\rho((3/8,1))\). Consequently the sharp cost is
\[
\int_0^{3/8}x\rho(x)\,dx
+\int_{3/8}^1|x-3/4|\rho(x)\,dx
=\frac1{12}+\frac{\arcsin\sqrt{3/8}+\sqrt3-\sqrt{15}/2}{2\pi}.
\]
That optimal two-atom measure is stationary for every \(4\mid N\), so the bound is attained. This calculation is analytic and independent of the finite certificate.

## Verification
The standalone C++17 verifier `verify.cpp` uses 64-bit exact products, no floating-point numbers, and full reverse-edge breadth-first search. The entire denominator interval was split into four independently completed contiguous execution blocks to keep resources bounded. Their output was:

```text
N=255 states=256 edges=510 missing=0 max_path=12
N=256 states=257 edges=481 missing=2 max_path=12
PASS grids=32767 total_states=536920062 total_edges=1073608932 global_max_shortest_path=25 first_at_N=30432
PASS grids=16384 total_states=671113216 total_edges=1342100940 global_max_shortest_path=26 first_at_N=35684
PASS grids=8192 total_states=436219904 total_edges=872375708 global_max_shortest_path=26 first_at_N=50131
N=65535 states=65536 edges=131070 missing=0 max_path=25
N=65536 states=65537 edges=130561 missing=2 max_path=25
PASS grids=8192 total_states=503328768 total_edges=1006592960 global_max_shortest_path=27 first_at_N=58789
```

Totals are 65,535 integer denominators, 2,147,581,950 denominator-state pairs, and 4,294,678,540 complete support edges. Additional independently implemented sparse strongly connected-component calculations at four representative denominators confirmed that the only closed classes were the ones stated. The Wasserstein integral was separately checked to high precision. Full reproduction commands and limitations appear in `VERIFICATION.md`.

## Relationship to prior work
Klöwer, Coveney, Paxton, and Palmer study finite-precision logistic and generalized Bernoulli maps, including stochastic rounding and finite-trajectory invariant-measure comparisons [1, 2]. Their logistic experiments use different arithmetic formats and do not provide this finite uniform-grid theorem, its divisibility-by-four stationary classification or the sharp Wasserstein optimization. Their reported Bernoulli-map absorption illustrates that randomized arithmetic does not in general prevent finite-state collapse, but conjugacy of the **continuum** logistic and doubling maps does **not** commute with discretization or rounding. Previously recorded work on deterministic ties-to-even binary16 rounding of the logistic map is also about a different numerical transition graph.

A 2011 paper on *rounding logistic maps over integers* [3] is relevant. Its abstract was accessible but full text was not: its potential overlap is unresolved and prevents any absolute publication-priority claim. The novelty assessment is limited to the inspected materials, not a proof of uniqueness against all literature.

## Limitations
The exhaustive claim covers only \(2\le N\le65536\); the certificate is finite, not a universal theorem over all integers. The mesh is uniform rational spacing; no inference about IEEE half precision, fused or intermediate arithmetic, finite pseudorandom periods, floating overflows, or other number formats is made. The hitting-time estimate is deliberately non-sharp. The long-time stationary law can differ radically from the practically observed finite-time histogram, because rare transitions may have extremely long expected waiting times. A related 2011 paper could not be materially inspected, leaving a real originality risk. No independent audit has been performed.

## References
[1] M. Klöwer, P. V. Coveney, E. A. Paxton, T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Research Square preprint, posted November 8, 2022, DOI 10.21203/rs.3.rs-2223046/v1.

[2] The same authors, *Scientific Reports* 13 (2023), 11410, DOI 10.1038/s41598-023-37004-4 (full open-access article, published July 14, 2023).

[3] *Rounding logistic maps over integers and the properties of the generated sequences*, IEICE Transactions on Fundamentals E94-A (2011), DOI 10.1587/transfun.E94.A.1817 (abstract checked; full text inaccessible).
