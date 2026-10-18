# Parity-inverted jamming and the critical bridge-rate window for clique-pair dimer adsorption

## Finding

Consider two disjoint complete graphs with orders \(m,n\geq2\), connected by exactly one extra edge joining designated vertices (the *bridge*). All vertices are initially vacant. Each internal edge independently attempts deposition of an irreversible dimer at Poisson rate \(1\), while the bridge attempts deposition at rate \(\beta>0\). An attempt succeeds only if both endpoints are vacant; subsequent attempts along any occupied edge have no effect. Let \(B\) be the event that the bridge eventually carries a deposited dimer, let \(P_{m,n}(\beta)=\Pr(B)\), and let \(U\) be the number of vertices still vacant after jamming.

**Exact finite-size law.** For integers \(a,b\geq1\), define \(R_{a,b}(\beta)\) recursively by
\[
 R_{a,b}(\beta)=
 \frac{\beta+\binom{a-1}{2}R_{a-2,b}(\beta)+\binom{b-1}{2}R_{a,b-2}(\beta)}
 {\beta+\binom a2+\binom b2},
\]
where a term with an invalid nonpositive first or second index is omitted (equivalently, its binomial coefficient is zero). In particular, \(R_{1,1}(\beta)=1\). Then \(P_{m,n}(\beta)=R_{m,n}(\beta)\). These are exact rational functions of \(\beta\) and rational numbers whenever \(\beta\) is rational. Moreover,
\[
 U=\begin{cases}
 2\mathbf1_B,&m,n\text{ both even},\\
 2(1-\mathbf1_B),&m,n\text{ both odd},\\
 1,&m+n\text{ odd}.
 \end{cases}
\]
Thus increasing the bridge rate strictly *reduces* expected final coverage when both clique orders are even, strictly *increases* it when both are odd, and leaves it unchanged when their parities differ. For each fixed \(m,n\geq2\), \(P_{m,n}(\beta)\) strictly increases in \(\beta>0\), tends to \(1\) as \(\beta\to\infty\), and has the singular weak-rate limit
\[
 \lim_{\beta\downarrow0}P_{m,n}(\beta)
 =\begin{cases}(mn)^{-1},&m,n\text{ both odd},\\0,&\text{otherwise}.\end{cases}
\]
At the model parameter \(\beta=0\), the bridge never deposits, so the nonzero weak-rate limit in the odd--odd case is genuinely discontinuous.

**All-size critical window.** Let \(m,n\to\infty\) with \(n/m\to\rho\in(0,\infty)\), and permit a bridge rate \(\beta=\beta_m>0\). If \(\beta_m/m\to\alpha\in(0,\infty)\), then
\[
 P_{m,n}(\beta_m)\longrightarrow
 L_\rho(\alpha):=\alpha\int_0^\infty
 \frac{e^{-\alpha u}}{(1+u)(1+\rho u)}\,du.
\]
Here \(L_\rho(\alpha)\) is continuous and strictly increasing in \(\alpha>0\), with endpoint limits \(0\) and \(1\). If \(\beta_m/m\to0\), then \(P_{m,n}(\beta_m)\to0\); if \(\beta_m/m\to\infty\), then \(P_{m,n}(\beta_m)\to1\). For every fixed \(\beta>0\), the leading rare-bridge coefficient is
\[
 \lim_{m\to\infty}mP_{m,n}(\beta)
 =\beta C(\rho),\qquad
 C(\rho)=\begin{cases}\dfrac{\log\rho}{\rho-1},&\rho\ne1,\\1,&\rho=1.\end{cases}
\]
For equal-size cliques and \(\beta_m=m\), the window limit is \(L_1(1)=1-eE_1(1)=0.403652637676805\ldots\), where \(E_1(1)=\int_1^\infty e^{-t}/t\,dt\).

## Assumptions and scope

The graph is finite, simple, and comprises exactly two cliques and one joining edge. Rates are attached to unordered graph edges and are independent exponential-clock rates; a successful dimer occupies its two endpoints irreversibly. The primary statements apply to arbitrary integers \(m,n\ge2\) and arbitrary \(\beta>0\); the limit \(\beta\downarrow0\) is a right limit and must not be confused with setting \(\beta=0\) before evolving for infinite time. The large-graph statements take \(n/m\to\rho\in(0,\infty)\), without parity restrictions. No result is claimed for sparse-community graphs or deposition of objects larger than edges.

## Proof

**1. Exact rate recursion.** In any current configuration, ignored deposition attempts cannot change occupancy. By independent exponential memorylessness, the next *successful* edge is sampled from currently available edges with probabilities proportional to their rates. Condition on both bridge endpoints still vacant, with \(a\) vacant vertices in the left clique and \(b\) in the right. The combined available rate is \(\beta+\binom a2+\binom b2\). If the bridge fires first, success is certain and contributes \(\beta\) to the recursion numerator. If an internal edge not incident to the designated left endpoint fires, both designated endpoints remain vacant and the state becomes \((a-2,b)\); there are \(\binom{a-1}{2}\) such edges. Similarly the right nonincident edges contribute \(\binom{b-1}{2}R_{a,b-2}(\beta)\). Any internal edge incident to a designated endpoint makes bridge occupation impossible. This yields the displayed recursion, including the \((1,1)\) base case. The process terminates almost surely in finite time because at most \(\lfloor(m+n)/2\rfloor\) attempts can succeed.

**2. Parity and finite-rate monotonicity.** Whenever the bridge does not deposit, greedy deposition saturates the remaining complete graph on each side except for exactly one vertex if that side's initial order is odd. If the bridge deposits, each side loses one vertex and subsequently jams with residue given by the opposite parity. This proves the exact piecewise law for \(U\), and hence the expected coverage comparisons. Couple different bridge rates using the same independent internal Poisson clocks, but a common unit exponential \(E\) for their first bridge attempts: \(T_\beta=E/\beta\). If the bridge has not attempted by time \(t\), its two endpoints are vacant precisely when both are vacant in the *bridge-deleted* independent clique processes. Thus the bridge deposits exactly when both distinguished endpoints are vacant at \(T_\beta\). Their survival probabilities are strictly decreasing in \(t>0\) for \(m,n\ge2\), proving that \(P_{m,n}(\beta)\) strictly increases with \(\beta\).

**3. Exact survival representation and the weak-rate boundary.** Let \(J^{(m)}_t\) be the number of vacant sites in an isolated complete clique of order \(m\) under unit internal rates. It is the pure-death chain jumping \(j\mapsto j-2\) at rate \(\binom j2\). By exchangeability, the chance that a specified vertex remains vacant is \(f_m(t)=\mathbb E[J^{(m)}_t]/m\). Independence of the two bridge-deleted cliques, followed by integration over \(T_\beta\sim\operatorname{Exp}(\beta)\), gives
\[
 P_{m,n}(\beta)=\int_0^\infty\beta e^{-\beta t}f_m(t)f_n(t)\,dt.\tag{1}
\]
At infinite time, \(J_t^{(m)}\) equals \(0\) for even \(m\) and \(1\) for odd \(m\), so \(f_m(\infty)=0\) or \(1/m\). As \(\beta\downarrow0\), \(T_\beta\to\infty\) in probability, and bounded convergence in (1) gives precisely the stated right limit. As \(\beta\to\infty\), \(T_\beta\to0\) in probability, yielding \(P\to1\).

**4. The fluid window.** With \(u=mt\), put \(X_m(u)=J^{(m)}_{u/m}/m\). A transition changes \(X_m\) by \(-2/m\) and has rescaled-time intensity \(J^{(m)}(J^{(m)}-1)/(2m)\). Consequently its predictable drift is \(-X_m^2+X_m/m\), while its martingale quadratic-variation rate is at most \(2/m\). For each finite \(U_0\), the martingale maximal inequality and Gronwall's inequality therefore imply convergence uniformly in probability on \([0,U_0]\) to the unique solution of \(x'=-x^2\), \(x(0)=1\), namely \(x(u)=(1+u)^{-1}\). Since \(0\le X_m\le1\), also \(f_m(u/m)\to(1+u)^{-1}\). The analogous right-clique limit is \(f_n(u/m)\to(1+\rho u)^{-1}\). Substitution into (1), followed by \(u=mt\), and dominated convergence for \(\beta_m/m\to\alpha\in(0,\infty)\) prove the integral formula \(L_\rho(\alpha)\).

For \(\beta_m/m\to0\), fix \(U_0>0\). The probability that the bridge attempts before \(U_0/m\) goes to zero, while the chance that both tags survive after that time is bounded by \(f_m(U_0/m)f_n(U_0/m)\to[(1+U_0)(1+\rho U_0)]^{-1}\). Send \(U_0\to\infty\). For \(\beta_m/m\to\infty\), the probability that either tag is internally occupied before \(T_{\beta_m}\) is at most \((m+n-2)/\beta_m\), since its instantaneous hazard is at most its clique order minus one. Thus the limiting bridge probability is \(1\). Finally, \(L_\rho(\alpha)=\mathbb E[((1+E/\alpha)(1+\rho E/\alpha))^{-1}]\) for \(E\sim\operatorname{Exp}(1)\), proving strict monotonicity and the endpoint limits.

**5. Fixed-rate rare-bridge coefficient.** With \(y_m(t)=\mathbb E[J^{(m)}_t]\), the generator gives \(y_m'=-\mathbb E[J^{(m)}_t(J^{(m)}_t-1)]\). Jensen's inequality yields \(y_m'\le-y_m(y_m-1)\), hence comparison with a logistic solution gives
\[
 f_m(t)\le\frac1{m-(m-1)e^{-t}}
 =\frac1{1+(m-1)(1-e^{-t})}.\tag{2}
\]
For \(0\le t\le1\), the right side is bounded by \((1+cmt)^{-1}\) for a universal \(c>0\) and all \(m\ge2\); for \(t\ge1\), it is \(O(m^{-1})\). The corresponding estimate holds for \(n\), and \(n/m\) stays bounded above and below. After the change \(u=mt\), the product in (1) is therefore uniformly integrable: the rescaled integral over \(u\le m\) has an \(O((1+u)^{-2})\) majorant, while its remaining part is \(O(m^{-1})\). Together with the fluid limit,
\[
 \lim mP_{m,n}(\beta)
 =\beta\int_0^\infty\frac{du}{(1+u)(1+\rho u)}
 =\beta C(\rho).
\]
The final integral evaluates by partial fractions; at \(\rho=1\) it equals \(1\) by continuity. This completes all claimed regimes.

## Verification

A standalone Python standard-library checker (`verify.py`) computes the reduced recursion in exact rational arithmetic and independently computes the full available-edge Markov recursion on the explicitly constructed labeled graph. It checks \(144\) rate-and-size pairs, corresponding \(144\) expected-uncovered-count identities, four selected exact unit-rate values, and four monotonicity examples. The analytical proof, rather than finite enumeration, establishes all-size and scaling-limit statements.

Benchmarks at unit bridge rate include \(P_{2,2}(1)=1/3\), \(P_{2,3}(1)=3/10\), \(P_{3,3}(1)=2/7\), and \(P_{4,4}(1)=5/26\). Direct rational recursion also confirms the predicted small-rate limits for the first two odd--odd examples. To reproduce: run `python3 verify.py` from the folder containing this document and the checker.

## Relationship to prior work

Dimer adsorption is the edge-occupation version of random sequential adsorption, and the terminal deposited dimers form a random greedy maximal matching. This framework predates this calculation. Pippenger (1989) studies graphical random sequential adsorption, emphasizing regular or high-girth settings; its available abstract also indicates an edge version, but the full text was not accessible for conclusive specialization checking. Dyer and Frieze (1991) study greedy matchings on arbitrary graphs at the level of performance guarantees. Bal and Bennett's preprint first posted 30 March 2016 studies greedy matching on sparse random regular graphs and hypergraphs; the assumption \(\Delta=o(N^{1/3})\) in its principal matching theorem does not cover the dense clique-pair graphs here. Neither the examined accessible material nor targeted published-results searches supplied the specific tagged-bridge recurrence, the parity-dependent rate response, or the proportional-bridge-rate limit. General random-greedy matching machinery alone does not determine these explicit rare-event quantities.

## Limitations

This result treats precisely one edge between two *complete* graphs, with homogeneous unit internal rates. The crossover uses proportional community sizes and does not address extreme size imbalance, other intercommunity topologies, or deposition objects occupying three or more sites. The finite-rate algebraic recursions are exact, but the leading asymptotic is stated without an error term. An equivalent specialized result in older graphical adsorption or randomized-matching literature cannot be excluded without further full-text inspection; the unavailable Pippenger and Dyer--Frieze complete texts are specific bibliographic risks. No claim of an independent audit is made.

## References

1. N. Pippenger, "Random Sequential Adsorption on Graphs," *SIAM Journal on Discrete Mathematics* **2** (1989), 393--401. DOI: 10.1137/0402034.
2. M. Dyer and A. Frieze, "Randomized greedy matching," *Random Structures & Algorithms* **2** (1991), 29--45. DOI: 10.1002/rsa.3240020104.
3. D. Bal and P. Bennett, "The Matching Process and Independent Process in Random Regular Graphs and Hypergraphs," arXiv:1603.09232, version 1 submitted 2016-03-30; see also revised preprint version 2 (2021).
