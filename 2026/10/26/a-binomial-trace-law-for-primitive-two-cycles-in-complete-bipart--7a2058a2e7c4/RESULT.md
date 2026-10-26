# A binomial-trace law for primitive two-cycles in complete-bipartite chip firing

## Finding
For each pair of positive integers \(a,b\), the standard synchronous parallel chip-firing automaton on the **labelled** complete bipartite graph \(K_{a,b}\) has exactly
\[
N_{a,b}=\frac{a^b b^a}{2}\sum_{k=0}^{\min(a,b)}\frac{(a)_{\underline{k}}(b)_{\underline{k}}}{a^k b^k}
\]
primitive two-cycle **orbits**. Here \((m)_{\underline{0}}=1\) and \((m)_{\underline{k}}=m(m-1)\cdots(m-k+1)\). The number of actual period-two **configurations** is \(2N_{a,b}\). For example, \(N_{1,b}=b\), \(N_{2,2}=18\), \(N_{2,3}=84\), and \(N_{3,3}=909\).

Without assuming a fixed ratio of shore sizes, if \(\min(a,b)\to\infty\),
\[
N_{a,b}\sim a^b b^a\sqrt{\frac{\pi ab}{8(a+b)}}.
\]
Among initial states in the natural confined box \(0\le \sigma(v)\le2\deg(v)-1\), the exact proportion lying in a primitive two-cycle is \(2N_{a,b}/(2^{a+b}a^b b^a)\), asymptotic to \(2^{-(a+b)}\sqrt{\pi ab/[2(a+b)]}\). These are **initial** recurrent-state counts, not basin counts.

## Assumptions and scope
All vertices are distinguishable. Each holds a nonnegative integer number of chips, and at every synchronous step a vertex with at least as many chips as its degree fires one chip to each adjacent vertex; others wait. Both shores are nonempty, so the graph is connected. A primitive two-cycle is an unordered orbit of exactly two distinct states exchanged by one update; fixed points are excluded. Falling factorials in the formula always satisfy \(0\le k\le\min(a,b)\), so no zero-denominator or out-of-range case arises. All calculations concern ordinary unforced dynamics.

## Proof
**1. Every vertex fires exactly once in a primitive two-cycle.** If a configuration returns after two steps, let \(u(v)\in\{0,1,2\}\) be its number of firings. Conservation at each vertex implies \(Lu=0\), for the ordinary graph Laplacian \(L\). Connectedness forces \(u\) constant. The constants zero and two make every vertex behave identically at both steps, hence give fixed configurations. Thus a primitive two-cycle necessarily has \(u(v)=1\) for every vertex.

**2. The local chip interval.** Choose the firing phase of every vertex in the first step. Write \(d(v)=\deg(v)\), and \(h(v)\) for its number of neighbours firing at the *opposite* step. If \(v\) fires initially, its initial chips must be exactly one of \(d(v),\ldots,d(v)+h(v)-1\); if it waits initially, its chips are one of \(d(v)-h(v),\ldots,d(v)-1\). These bounds follow directly from the threshold at time zero and its reversed threshold after one update. They are also sufficient, and each vertex has precisely \(h(v)\) allowed initial values. The choices at different vertices are independent once the firing phases are fixed.

**3. Count all phase assignments.** Suppose \(p\) of the \(a\) left vertices and \(q\) of the \(b\) right vertices fire at time zero. The opposite-phase degrees are \(b-q\) at the \(p\) left firing vertices, \(q\) at the remaining left vertices, \(a-p\) at the \(q\) right firing vertices, and \(p\) at the remaining right vertices. Thus the total number of period-two configurations is
\[
2N_{a,b}=\sum_{p=0}^{a}\sum_{q=0}^{b}
\binom ap\binom bq (b-q)^p q^{a-p}(a-p)^q p^{b-q}.
\]
Use the standard convention \(0^0=1\), corresponding to an empty product. Each configuration appears once through its unique time-zero firing assignment, and a primitive orbit contains exactly two states.

**4. Exact binomial-kernel trace.** Define the row-stochastic rectangular matrix
\[
K_{a,b}(p,q)=\binom bq\left(1-\frac pa\right)^q\left(\frac pa\right)^{b-q},
\quad 0\le p\le a,\ 0\le q\le b.
\]
A direct comparison of factors in the preceding double sum gives
\[
2N_{a,b}=a^b b^a\operatorname{tr}(K_{a,b}K_{b,a}).
\]
On functions of \(p\), the matrix \(K_{a,b}K_{b,a}\) preserves polynomials of degree at most \(k\), for every \(0\le k\le\min(a,b)\). Indeed, a binomial average of the falling factorial \((q)_{\underline{k}}\) is \((b)_{\underline{k}}(1-p/a)^k\), whose highest-degree coefficient in \(p\) is \((-1)^k(b)_{\underline{k}}/a^k\). Composing the opposite-direction average therefore gives the associated graded eigenvalue
\[
\lambda_k=\frac{(a)_{\underline{k}}(b)_{\underline{k}}}{a^k b^k}.
\]
When \(a>b\), the composed operator has image contained in the space of degree-at-most-\(b\) polynomial functions of \(p\), since its final stage factors through functions on \(b+1\) states. Hence the remaining \(a-b\) eigenvalues are zero. When \(a\le b\), the polynomial filtration already spans its full \(a+1\)-dimensional state space. In both cases the trace is exactly \(\sum_{k=0}^{\min(a,b)}\lambda_k\), proving the finite sum.

**5. Joint-size asymptotic.** Put \(h=\sqrt{ab/(a+b)}\). If \(\min(a,b)\to\infty\), then \(h\to\infty\). For each fixed \(t\ge0\) and \(k=\lfloor th\rfloor\), elementary logarithmic expansion gives
\[
\log\lambda_k=-\frac{k(k-1)}2\left(\frac1a+\frac1b\right)+o(1)\longrightarrow-\frac{t^2}{2}.
\]
Moreover \(0\le\lambda_k\le\exp[-k(k-1)/(2h^2)]\); this follows by applying \(\log(1-x)\le-x\) separately to every falling-factorial factor. Gaussian domination therefore yields the Riemann-sum limit
\[
\frac1h\sum_{k=0}^{\min(a,b)}\lambda_k\longrightarrow\int_0^\infty e^{-t^2/2}\,dt=\sqrt{\frac\pi2}.
\]
Substitution into the finite sum proves the claimed asymptotic for all joint growth regimes.

**6. Optional exact mass refinement.** Let \([d]_z=\sum_{j=0}^{d-1}z^j\) for positive \(d\), and \([0]_z=0\). For a time-zero phase split \((p,q)\), let \(c=p(b-q)+(a-p)q\), the number of opposite-phase edges. The allowed chip intervals yield the exact primitive-orbit mass polynomial
\[
\mathcal C_{a,b}(z)=\frac12\sum_{p=0}^{a}\sum_{q=0}^{b}\binom ap\binom bq z^{2ab-c}
[b-q]_z^p[q]_z^{a-p}[a-p]_z^q[p]_z^{b-q},
\]
with empty factors equal to one. Each coefficient counts primitive two-cycles with that total number of chips; setting \(z=1\) returns \(N_{a,b}\). The formula is valid also at shore size one.

## Verification
The standalone \(\texttt{verify.py}\) constructs the actual degree-threshold update (without using any matrix or the proof's phase constraints) and exhaustively tests all bounded initial states in nine graphs, from \(K_{1,1}\) through \(K_{3,4}\). This examines 729,348 complete labelled configurations. For each it compares an exact two-step return test to the phase sum and the independent falling-factorial expression. An additional 121 parameter pairs with shore sizes from one through eleven compare the two exact arithmetic formulas. All checks passed and are reproducible by running \(\texttt{python verify.py}\), whose output is provided in \(\texttt{verification_output.txt}\). These finite tests supplement but do not replace the general proof.

## Relationship to prior work
The graph automaton and foundational periodicity questions originate in Bitar and Goles (1992). Jiang (2010, Proposition 2.5 and Section 3) proves the equal-firing-count condition and classifies possible periods on complete bipartite graphs; this is the starting point of Step 1 above, but possible periods alone do not specify the number of distinct two-cycle orbits. Ji, Li, and Wang (2024) study a chip-mass interval forcing eventual period two, not the complete initially recurrent-orbit population. Jung (2026) establishes an all-biclique middle-stair theorem, likewise phrased in terms of eventual period rather than an exact orbit census; its complete text could not be examined, so detailed comparison remains a residual uncertainty. The novelty asserted here is restricted to the exact falling-factorial census, binomial-trace reduction and joint-size asymptotic. No uniqueness or exhaustive historical search claim is made.

## Limitations
This theorem is solely about primitive two-cycles; other periods can occur on complete bipartite graphs, and no general basin or preperiod census is claimed. The mass-refined polynomial is a direct constructive count rather than a separately simplified closed form. The oldest source and the most recent related preprint were not both available in full text; an unindexed or inaccessible equivalent counting theorem remains possible. Independent mathematical review has not been performed.

## References
- J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300, DOI: 10.1016/0304-3975(92)90316-8.
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (2010), especially Proposition 2.5 and Section 3: https://arxiv.org/html/1003.0943v2.
- D. Ji, M. Li and D. Wang, *Non-Stabilizing Parallel Chip-Firing Games*, arXiv:2408.10508v2 (2024): https://arxiv.org/pdf/2408.10508.
- M. Jung, *The Middle Stair for Complete Bipartite Parallel Chip-Firing*, arXiv:2608.01350v1 (2026): https://arxiv.org/abs/2608.01350.
- Z. Scully, T.-Y. Jiang and Y. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, SIAM J. Discrete Math. 29 (2015), 615–630, DOI: 10.1137/130933770.
