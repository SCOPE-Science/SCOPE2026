# Fixed-width biclique flooding: a Gumbel core and an exponential seed penalty

## Finding

Let \(K_{a,b}\) have parts \(A\) and \(B\), where \(a\ge b\ge2\). At each vertex an independent rate-one Poisson clock calls a uniformly chosen neighbor; information is transmitted across a call if exactly one endpoint is informed. All informed vertices remain informed. Let \(T_{a,b}(i,j)\) be the time until every vertex is informed, given exactly \(i\) informed vertices of \(A\) and \(j\) of \(B\) initially, and write \(c_{a,b}=1/a+1/b\).

**Exact finite source ordering.** With one initial seed, there is a random variable \(Z_{a,b}\), independent of the indicated exponentials, such that
\[
T_{a,b}(0,1)\overset d=\operatorname{Exp}(a c_{a,b})+Z_{a,b},\qquad
T_{a,b}(1,0)\overset d=\operatorname{Exp}(b c_{a,b})+Z_{a,b}.
\]
Consequently, for every \(a\ge b\ge2\), placing the seed in \(B\), the higher-degree part, stochastically minimizes completion time among all single-vertex choices. When \(a>b\) the dominance is strict at every positive deadline, and
\[
\mathbb E T_{a,b}(1,0)-\mathbb E T_{a,b}(0,1)=\frac{a-b}{a+b}.
\]

**All fixed-size seed allocations in an extreme biclique.** Fix integers \(b\ge2\) and \(k\ge1\), and let \(a\to\infty\). For any fixed nonnegative \(i,j\) with \(i+j=k\) and \(j\le b\), the centered completion time obeys
\[
T_{a,b}(i,j)-\log a\ \Longrightarrow\
\begin{cases}
G,&j\ge1,\\
G+E_k,&j=0,
\end{cases}
\]
where \(\Pr(G\le x)=\exp(-e^{-x})\), \(E_k\sim\operatorname{Exp}(k)\), and \(G,E_k\) are independent. The corresponding expectations satisfy
\[
\mathbb E T_{a,b}(i,j)=\log a+\gamma+\mathbf 1_{\{j=0\}}/k+o(1),
\]
where \(\gamma\) is Euler's constant. The last informed vertex belongs to \(A\) with probability tending to one in either regime. In particular, having at least one hub-side seed removes a nondegenerate exponential delay; merely adding a fixed number of seeds on the larger, low-degree side does not remove it.

For each fixed real \(x\), the limiting CDF is \(e^{-e^{-x}}\) if \(j\ge1\), whereas if \(j=0\) it is
\[
F_k(x)=\int_0^\infty k e^{-kt}\exp(-e^{t-x})\,dt.
\]
For one seed and the deadline \(\log a\), the two completion probabilities converge respectively to \(e^{-1}\approx0.367879\) and \(e^{-1}-E_1(1)\approx0.148496\), where \(E_1(z)=\int_z^\infty e^{-u}/u\,du\).

## Assumptions and scope

All calls occur independently at unit rate and choose neighbors uniformly, with replacement across calls. Any call between an informed and an uninformed endpoint transmits immediately; transmission is permanent, simultaneous calls have probability zero, and there are no delays, failures, or recoveries. Time is continuous and measured in units of one call per vertex per unit time. In the limit, \(b\) and \(k\) are fixed while \(a\) tends through positive integers; the claim does not concern growing \(b\), synchronous rounds, or push-only dissemination. The exact finite comparison holds for all \(a\ge b\ge2\) independently of the fixed-width limit.

## Proof

**1. Independent edge contacts and the state generator.** Independent Poisson splitting gives independent directed contact processes of rate \(1/\deg(v)\) along every oriented edge out of \(v\). Superposition in the two directions makes every undirected edge an independent rate-\(c_{a,b}\) contact process. Thus, for an informed-count state \((i,j)\), the only nontrivial transitions are
\[
(i,j)\to(i+1,j)\quad\text{at rate }(a-i)j c_{a,b},\qquad
(i,j)\to(i,j+1)\quad\text{at rate }(b-j)i c_{a,b}.
\]
The absorbing state is \((a,b)\).

**2. Exact one-seed decomposition.** Starting with one \(B\) seed, the first informative contact occurs after an \(\operatorname{Exp}(a c_{a,b})\) wait, at which point the state is \((1,1)\). Starting with one \(A\) seed, the corresponding wait is \(\operatorname{Exp}(b c_{a,b})\), again followed by state \((1,1)\). The strong Markov property identifies a common independent residual completion time \(Z_{a,b}\). Convolution preserves stochastic ordering; comparing the exponential rates gives the stated strict order when \(a>b\). Taking expectations gives \((b c_{a,b})^{-1}-(a c_{a,b})^{-1}=(a-b)/(a+b)\). This compares the entire distribution, not just its mean.

**3. Rapid saturation of the fixed-width part.** Fix initial \((i,j)\) with \(j\ge1\) and fixed total number of seeds. Put \(\varepsilon_a=a^{-1/3}\), and designate one initially informed vertex \(v\in B\). Among the previously uninformed \(A\)-vertices, direct contacts with \(v\) during \([0,\varepsilon_a/2]\) independently infect a binomial number with mean asymptotic to \(a^{2/3}/(2b)\). A Chernoff bound shows that at least \(C a^{2/3}\) such vertices are informed by \(\varepsilon_a/2\), except with probability \(\exp(-\Omega(a^{2/3}))\), for a constant \(C>0\). Each remaining \(B\)-vertex then receives contacts from these vertices during \([\varepsilon_a/2,\varepsilon_a]\) at total rate at least \(C a^{2/3}c_{a,b}\). These contacts involve disjoint edge clocks from those used for the first stage. Therefore
\[
\Pr(B\text{ is not completely informed by }\varepsilon_a)
\le \exp(-\Omega(a^{2/3}))+b\exp(-\Omega(a^{1/3}))=o(1).
\]
Conversely, a previously uninformed \(A\)-vertex cannot become informed before it receives some contact on any of its \(b\) incident edges. Those all-edge contact clocks have total rate \(b c_{a,b}=1+b/a\) and are independent between different \(A\)-vertices. Hence the number of additional \(A\)-infections by \(\varepsilon_a\) is stochastically bounded by \(\operatorname{Bin}(a-i,1-e^{-(1+b/a)\varepsilon_a})\), whose expectation is \(O(a^{2/3})\). Thus, at time \(\varepsilon_a\), all of \(B\) is informed with probability tending to one, but \(M_a/a\to1\) in probability, where \(M_a\) is the number of uninformed \(A\)-vertices.

**4. Gumbel completion and means.** On that high-probability event, after \(\varepsilon_a\) the \(M_a\) remaining \(A\)-vertices have independent exponential first-contact waits of rate \(b c_{a,b}=1+b/a\). Their maximum has conditional CDF
\[
\left(1-e^{-(1+b/a)t}\right)^{M_a},\quad t\ge0.
\]
For each fixed real \(x\), substituting \(t=\log a+x-\varepsilon_a\), using \(M_a/a\to1\) and \((1+b/a)\log a\to\log a\), gives \(\exp(-e^{-x})\). The exceptional event has vanishing probability, proving the Gumbel limit.

For expectations, direct contacts from the designated initial \(B\)-seed inform all \(A\) by a time stochastically bounded by the maximum of \(a\) independent \(\operatorname{Exp}(c_{a,b})\) variables. Once all \(A\) are informed, the remaining \(B\)-completion requires at most the maximum of \(b\) fresh independent \(\operatorname{Exp}(a c_{a,b})\) variables. For fixed \(b\), this bounds the second moment of completion time by \(O((\log a)^2)\). The probability in step 3 is exponentially small in \(a^{1/3}\), so the exceptional event contributes \(o(1)\) to the mean. On the typical event, the conditional mean of the final stage is \(H_{M_a}/(b c_{a,b})\), with \(H_m=\sum_{r=1}^m1/r\). The binomial upper bound for prior infections yields \(\mathbb E|H_{M_a}-\log a-\gamma|\to0\) after discarding the exponentially unlikely exceptional event. It follows that \(\mathbb E T_{a,b}(i,j)=\log a+\gamma+o(1)\) whenever \(j\ge1\).

**5. Seeds confined to \(A\).** With \(i=k\) and \(j=0\), only contacts from the \(k\) seeded \(A\)-vertices to \(B\) can initially transmit. The first \(B\)-infection occurs after an independent \(\operatorname{Exp}(k b c_{a,b})\) wait, followed by state \((k,1)\). Since \(k b c_{a,b}=k(1+b/a)\to k\), the strong Markov property and step 4 yield the independent convolution \(G+E_k\), with mean \(\log a+\gamma+1/k+o(1)\). In both cases, the small part is fully informed before the last of the \(a-o_{\mathbb P}(a)\) larger-part vertices, so the final newly informed vertex belongs to \(A\) with probability tending to one.

## Verification

The standalone Python program `check.py` verifies the exact rational state-recursion for the mean and Laplace transforms on \(K_{a,b}\) with \(2\le a\le8\) and \(1\le b\le\min(a,5)\) at three positive Laplace parameters. It tests the finite source convolution identities and signed mean difference, and performs fixed-seed Monte Carlo diagnostics for the predicted limiting means. The checker reports 526 passing assertions and diagnostics. These computations check the generator and finite identities but do not prove the infinite-population convergence; that is supplied by steps 3–5.

To reproduce: run `python check.py` using Python 3 and its standard library. The numerical diagnostics have a fixed random seed. The public derivation is self-contained.

## Relationship to prior work

Acan, Collevecchio, Mehrabian and Wormald [1] introduce the independent exponential edge-contact representation for asynchronous push-pull and explicitly compute the star case \(b=1\), including the difference between central and leaf starts. That known boundary case is not claimed as new. Here the fixed-width biclique has \(b\ge2\), two interacting infected-count coordinates, arbitrary fixed-size seed allocations, and a source-dependent convolution limit. Their general graph bounds do not establish the present sharp CDFs or finite \(K_{a,b}\) source difference.

Leskelä and Ngo [2], first publicly available on June 25, 2018, study flooding in sparse configuration-model random graphs with independent exponential link weights and boundary delays. Their degree-regularity regime does not cover \(K_{a,b}\) with fixed \(b\) and \(a\to\infty\), whose maximum degree is of order the total vertex count and whose size-biased degree second moment diverges. Their logarithmic-scale laws do not imply an order-one Gumbel-plus-exponential source penalty. Doerr and Kostrygin [3] study discrete-round complete-graph rumor spreading with different symmetry assumptions and do not supply the present continuous-time bipartite law.

Related work on near-balanced biclique exponential first-passage infections concerns last-infection side competition under fixed per-edge rates, not the source-allocation laws for degree-normalized asynchronous calls in the extreme-width regime. Exact asynchronous spreading on double-star trees has a mandatory bridge whose delay scales differently; neither result gives the distribution stated here.

## Limitations

The extreme-biclique result fixes \(b\) and \(k\); it does not establish a crossover for growing \(b\), optimality of every multi-seed allocation at finite size, or stochastic comparisons between arbitrary initial configurations. The finite all-deadline comparison is proved only for one seed. The model requires uniform neighbor choice, independent rate-one Poisson callers and permanent infection. The claim is an analytical result with self-review, not an independently audited theorem. Historical priority beyond the searched literature remains uncertain.

## References

[1] H. Acan, A. Collevecchio, A. Mehrabian and N. Wormald, *On the push&pull protocol for rumour spreading*, arXiv:1411.0948, first submitted November 4, 2014. https://arxiv.org/abs/1411.0948

[2] L. Leskelä and H. Ngo, *First passage percolation in sparse random graphs with boundary weights*, arXiv:1806.09568, first submitted June 25, 2018. https://arxiv.org/abs/1806.09568

[3] B. Doerr and A. Kostrygin, *Randomized Rumor Spreading Revisited*, arXiv:2303.11150, first submitted March 20, 2023. https://arxiv.org/abs/2303.11150
