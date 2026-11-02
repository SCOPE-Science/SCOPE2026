# A sharp nonbacktracking cover-time law for clique windmills

## Finding

For fixed integer \(m\ge3\) and growing integer \(n\), let \(W_{n,m}=K_1\vee(nK_m)\) be the graph formed by identifying one vertex of \(n\) complete graphs on \(m+1\) vertices. Denote the common vertex by the hub. Start at the hub and consider two walks: the simple random walk (S) chooses each neighbor uniformly; the nonbacktracking walk (N) chooses each neighbor other than the vertex immediately preceding its current position uniformly (and chooses uniformly on its initial step). Let \(T^{\mathrm S}_{n,m}\) and \(T^{\mathrm N}_{n,m}\) be the first edge-traversal times at which all \(nm+1\) vertices have been visited.

Put \(q_{\mathrm S}=(m+1)/(2m)\), \(q_{\mathrm N}=(m+2)/(2m)\), and \(G(x)=\exp(-e^{-x})\). For each \(P\in\{\mathrm S,\mathrm N\}\) and each real \(x\),

\[
\lim_{n\to\infty}\Pr\left\{\frac{q_P T^P_{n,m}}{(m+1)n}-\log(nm)\le x\right\}=G(x).
\]

Moreover,

\[
\mathbb E T^P_{n,m}\sim\frac{m+1}{q_P}\,n\log n,
\qquad
\lim_{n\to\infty}\frac{\mathbb E T^{\mathrm N}_{n,m}}{\mathbb E T^{\mathrm S}_{n,m}}=\frac{m+1}{m+2}.
\]

This comparison uses the genuine nonbacktracking rule even when the walker is at the hub. In particular, the strict improvement is \(4/5\) at \(m=3\), and diminishes as the fixed clique size grows.

## Assumptions and scope

All graphs are finite, simple and undirected. An excursion starts with an edge from the hub and ends at the next return to the hub. The graph has \(n\) petals, each with exactly \(m\) private vertices. In the nonbacktracking walk the incoming peripheral neighbor is excluded from the choices at the hub after each excursion. For \(m\ge3\), every visit to a nonhub vertex eventually returns to the hub almost surely. In all limits \(m\) is fixed and \(n\to\infty\); no result is asserted for growing \(m\). The cover time is in **individual edge traversals**, not in completed excursions.

For a subset \(A\) of \(s\) specified vertices of a single petal, write \(h_P(s)\) for the probability that an excursion visits at least one of them, *conditional on starting in that petal with a uniform entrance vertex*. The exact single-petal laws are

\[
 h_{\mathrm S}(s)=1-\frac{m-s}{m(s+1)},
 \qquad
 h_{\mathrm N}(s)=1-\frac{(m-s)(m-s-1)}{m(m-1)(s+1)},
 \quad 1\le s\le m.
\]

They imply \(h_P(1)=q_P\) and \(h_P(s)>q_P\) for every \(2\le s\le m\) and \(m\ge3\). These are exact finite excursion identities; they are not approximations.

## Proof

**1. Excursion avoidance.** For the simple walk, the uniformly chosen first outer vertex avoids the \(s\) marked vertices with probability \((m-s)/m\). From any unmarked outer vertex the next step hits the hub with probability \(1/m\), hits a marked vertex with probability \(s/m\), and otherwise remains among unmarked outer vertices. The probability of reaching the hub before a marked vertex is therefore \(1/(s+1)\). Multiplication yields \(1-h_{\mathrm S}(s)=(m-s)/(m(s+1))\).

For the nonbacktracking walk, the first two distinct outer vertices are an ordered uniformly sampled pair: the second step cannot return to the hub. Both are unmarked with probability \((m-s)(m-s-1)/(m(m-1))\). Thereafter every step, conditional on still avoiding the hub and all marked vertices, has exactly one hub choice and \(s\) marked-vertex choices out of \(m-1\) allowed neighbors. The chance of reaching the hub before a marked vertex is exactly \(1/(s+1)\). Multiplication proves the second displayed excursion formula. In both protocols a full excursion has mean length \(\ell=m+1\): the simple walk takes its first edge and then a geometric number with success probability \(1/m\), while the nonbacktracking walk takes two edges and then a geometric number with success probability \(1/(m-1)\). Their lengths, indexed by successive excursions, are identically distributed and independent within each protocol, with finite exponential moments near zero.

**2. Rare-set survival despite hub memory.** Fix a finite set \(A\) of outer vertices, with \(s_i\ge1\) marked vertices in each of \(p\) distinct petals and total \(k=\sum_i s_i\). Write \(H_P(A)=\sum_{i=1}^p h_P(s_i)\). For the simple walk, the successive excursions are independent, and the probability that no element of \(A\) is visited during the first \(r\) excursions is exactly

\[
 \left(1-\frac{H_{\mathrm S}(A)}n\right)^r.
\]

For the nonbacktracking walk, condition on the peripheral vertex \(a\) from which the last excursion returned to the hub. There are \(nm-1\) available outgoing neighbors. Summing conditional chances of hitting marked vertices over all \(m\) possible entrances to each marked petal, the next-excursion hit probability is

\[
 \frac{mH_{\mathrm N}(A)-\mathbf1\{a\text{ lies in a marked petal}\}\,\eta(a)}{nm-1},
 \qquad 0\le\eta(a)\le1.
\]

The parameter \(\eta(a)\) is the probability of hitting the marked subset of its own petal if one enters through the excluded neighbor \(a\). Independently of the previous incoming vertex, the probability that the next excursion *enters* one of the \(p\) marked petals is at most \(pm/(nm-1)\). Therefore, after conditioning that all earlier excursions avoided \(A\), the chance that the immediately preceding excursion returned from one of the marked petals is at most

\[
 \frac{pm/(nm-1)}{1-pm/(nm-1)}=O_{m,p}(n^{-1}).
\]

This follows by considering that preceding excursion: entering a marked petal is necessary for its incoming vertex to belong to that petal, while conditional avoidance has probability at least \(1-pm/(nm-1)\). The first excursion has a uniform entrance and hence hit probability exactly \(H_{\mathrm N}(A)/n\). In every later excursion, conditional on avoiding \(A\) previously, the hit probability is

\[
 \frac{H_{\mathrm N}(A)}n+O_{m,k}(n^{-2}).
\]

Consequently, for \(r=O(n\log n)\), uniformly over all fixed-size tagged configurations \(A\),

\[
 \Pr\{A\text{ remains unvisited through }r\text{ excursions}\}
 =\exp\left(-\frac{rH_{\mathrm N}(A)}n+O_{m,k}\!\left(\frac{r}{n^2}\right)\right).
\]

For the simple walk this follows directly from its exact product. This tagged-survival estimate also supplies the key control on the dependence caused by excluding the incoming hub edge; treating hub excursions as independent for the nonbacktracking walk would be unjustified.

**3. Poisson law for uncovered vertices.** Let \(U_r^P\) count outer vertices not yet visited after \(r\) complete excursions, and fix \(x\in\mathbb R\). Take

\[
 r=r_n^P(x)=\left\lfloor\frac{n}{q_P}(\log(nm)+x)\right\rfloor.
\]

For any fixed positive integer \(k\), compute the factorial moment \(\mathbb E[(U_r^P)_k]\) by summing the tagged-survival probability over ordered \(k\)-tuples of distinct outer vertices. Tuples with vertices in \(k\) distinct petals number \((n)_k m^k=(nm)^k(1+o(1))\), have \(H_P=kq_P\), and contribute \(e^{-kx}+o(1)\). For a tuple supported on \(p<k\) petals, at least one petal contains two or more of its vertices. Because \(h_P(s)>q_P\) for every \(s\ge2\), its \(H_P/q_P>p\). There are only \(O_{m,k}(n^p)\) tuples with that fixed occupancy pattern, but their total survival probability is \(O_{m,k,x}((nm)^{-H_P/q_P})\); their contribution vanishes. Thus

\[
 \mathbb E[(U_{r_n^P(x)}^P)_k]\longrightarrow e^{-kx}
 \quad\text{for every fixed }k\ge1.
\]

These factorial moments identify \(\operatorname{Poisson}(e^{-x})\) as the limit. The event of no uncovered vertex is exactly that all vertices have been covered; hence the completed-excursion cover index \(C_{n,m}^P\) satisfies

\[
 \Pr\left\{\frac{q_P C_{n,m}^P}{n}-\log(nm)\le x\right\}
 \longrightarrow \exp(-e^{-x}).
\]

**4. From excursions to edge steps.** Let \(L_j^P\) be the number of edge steps in excursion \(j\) and \(S_r^P=\sum_{j=1}^r L_j^P\). We have \(\mathbb E L_j^P=m+1\) and \(\operatorname{Var}(L_j^P)<\infty\). Uniformly for \(r\le K n\log n\), Kolmogorov's maximal inequality gives \(\max_{j\le r}|S_j^P-(m+1)j|/n\to0\) in probability. The largest of these geometric-tailed excursion lengths divided by \(n\) also converges to zero in probability. Since the last vertex is covered during excursion \(C_{n,m}^P=O_{\Pr}(n\log n)\), not necessarily at its end, the difference between \(T_{n,m}^P\) and \((m+1)C_{n,m}^P\) is \(o_{\Pr}(n)\). The asserted edge-step Gumbel limits follow.

**5. Means and comparison.** The rare-set survival estimate for \(k=1\) is uniform in the number of excursions, since its one-step conditional bound is uniform. For sufficiently large \(n\),

\[
 \Pr\{C_{n,m}^P>r\}\le nm\exp\left(-r\left(\frac{q_P}{n}-\frac{K_m}{n^2}\right)\right)
\]

for a constant \(K_m\) independent of \(r\). Summation over the positive integers yields \(\mathbb E C_{n,m}^P\le (n/q_P)\log(nm)+O_m(n)\). Conversely the Gumbel limit gives \(C_{n,m}^P/(n\log n)\to1/q_P\) in probability; nonnegativity then gives the matching asymptotic lower bound for the expectation. Wald's identity gives \(\mathbb E S_{C_{n,m}^P}^P=(m+1)\mathbb E C_{n,m}^P\). The mean difference between this return-to-hub time and the earlier actual cover time is at most the expected maximum of the first \(C_{n,m}^P\) geometric-tailed lengths, which is \(O_m(\log n)\) by a union bound and the finite mean of \(C_{n,m}^P\). Therefore \(\mathbb E T_{n,m}^P\sim(m+1)n\log n/q_P\). Taking the ratio yields \(q_{\mathrm S}/q_{\mathrm N}=(m+1)/(m+2)\), as claimed.

## Verification

The standalone `verify_windmill.py` solves finite absorbing Markov-chain systems over exact rational numbers, independently of the displayed excursion formulas, for both protocols, all \(m\in\{2,3,4,5,6,7\}\), and every marked-set size \(1\le s\le m\). It checks the sharp single-vertex constants, strict multi-vertex hazard separation for \(m\ge3\), and the ratio. It reports `PASS 114 exact rational checks`. Run `python3 verify_windmill.py` with Python 3 and no nonstandard packages.

The additional seeded simulation `simulate_windmill.py` runs the genuine nonbacktracking rule, including at the hub, and compares observed finite cover-time means with the leading Gumbel-predicted means for \(m\in\{3,4\}\). The simulation is a diagnostic, not a proof of any infinite limit.

## Relationship to prior work

The arXiv paper by Tishby, Biham and Katzav (2021), *Analytical results for the distribution of cover times of random walks on random regular graphs*, obtains Gumbel limits for simple walks and discusses nonbacktracking walks on random regular graphs. Its random regular graph geometry does not include \(W_{n,m}\), whose hub degree grows with \(n\), and it does not imply the petal-specific constants here.

Breen, Faught, Glover, Kempton, Knudson and Oveson (2022), *Kemeny's constant for non-backtracking random walks*, studies a different quantity: averages of hitting times, not the distribution of the time to cover every vertex of a clique windmill. Sylvester (2021), *The Cover Time of a (Multiple) Markov Chain with Rational Transition Probabilities is Rational*, gives a general rationality principle for finite expected cover times, not this Gumbel law or explicit speedup.

The triangle-petal case \(m=2\) is simpler because each nonbacktracking excursion necessarily visits both vertices of its petal; exact triangle-bouquet coupon-collector identities are not asserted as a new special case. The substantive statement here concerns all fixed clique sizes \(m\ge3\), where individual excursions can cover only part of a petal, and nonbacktracking excursions remain dependent through the hub's excluded entrance edge.

## Limitations

The regime is fixed \(m\ge3\) with \(n\to\infty\). No uniform-in-\(m\) assertion, finite-\(n\) stochastic ordering, exact finite-\(n\) law for the nonbacktracking cover time, or claim about general graphs is made. The graph starts at the hub, and both protocols select uniformly among allowed neighbors. The statement is analytically proved but has not undergone independent mathematical audit. Historical priority could be affected by specialized cover-time results not found in the comparisons performed.

## References

- I. Tishby, O. Biham, E. Katzav, *Analytical results for the distribution of cover times of random walks on random regular graphs* (first public 2021-10-26), arXiv:2110.13592, https://arxiv.org/abs/2110.13592.
- J. Breen, N. Faught, C. Glover, M. Kempton, A. Knudson, A. Oveson, *Kemeny's constant for non-backtracking random walks* (first public 2022-03-22), arXiv:2203.12049, https://arxiv.org/abs/2203.12049.
- J. Sylvester, *The Cover Time of a (Multiple) Markov Chain with Rational Transition Probabilities is Rational* (first public 2021-02-24), arXiv:2102.12356, https://arxiv.org/abs/2102.12356.
