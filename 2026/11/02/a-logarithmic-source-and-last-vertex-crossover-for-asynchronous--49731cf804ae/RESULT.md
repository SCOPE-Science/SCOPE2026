# A logarithmic source-and-last-vertex crossover for asynchronous rumor spreading on double stars

## Finding

Let \(D_{a,b}\) be the tree consisting of adjacent hubs \(u,v\), with \(a\ge1\) pendant neighbors of \(u\) and \(b\ge1\) pendant neighbors of \(v\). In continuous-time asynchronous push-pull dissemination, every vertex independently calls a uniformly selected neighbor at rate one and the endpoints exchange the rumor. Write \(T^{(a)}_{a,b}\) and \(T^{(b)}_{a,b}\) for the completion times when the sole initially informed vertex is the hub with \(a\) leaves or the hub with \(b\) leaves, respectively.

Set
\[
 r_a=1+\frac1{a+1},\quad r_b=1+\frac1{b+1},\quad
 c=\frac1{a+1}+\frac1{b+1}.
\]
Let \(M_a\) and \(M_b\) be independent maxima of \(a\) independent \(\operatorname{Exp}(r_a)\) variables and \(b\) independent \(\operatorname{Exp}(r_b)\) variables, and let \(E\sim\operatorname{Exp}(c)\) be independent of both. Then, exactly for every \(a,b\ge1\),
\[
 T^{(a)}_{a,b}\stackrel d=\max\{M_a,E+M_b\},\qquad
 T^{(b)}_{a,b}\stackrel d=\max\{M_b,E+M_a\}.
\]
In particular, for \(t\ge0\),
\[
 \Pr(T^{(a)}_{a,b}\le t)
 =(1-e^{-r_a t})^a\int_0^t c e^{-cs}(1-e^{-r_b(t-s)})^b\,ds.
\]
The exact formula implies a **hub-source stochastic ordering**: whenever \(a\ge b\),
\[
 T^{(a)}_{a,b}\le_{\mathrm{st}}T^{(b)}_{a,b},
\]
with distinct distributions for \(a>b\). Thus starting at the hub of greater leaf degree is never worse, at every deadline.

There is a sharp logarithmic crossover. Suppose \(a\to\infty\), \(1\le b=b(a)\le a\), and \(b/\log a\to\rho\in(0,\infty)\). With \(Z\sim\operatorname{Exp}(1)\),
\[
 \frac{T^{(a)}_{a,b}}{\log a}\Rightarrow\max\{1,\rho Z\},\qquad
 \frac{T^{(b)}_{a,b}}{\log a}\Rightarrow1+\rho Z.
\]
The first law has an atom \(1-e^{-1/\rho}\) at one and a tail \(\Pr(\max\{1,\rho Z\}>t)=e^{-t/\rho}\) for \(t>1\). For a rumor starting at the larger hub, the probability the **last informed vertex is on that same side** converges to \(1-e^{-1/\rho}\); the other side finishes last with probability \(e^{-1/\rho}\). The mean completion times satisfy
\[
 \frac{\mathbb ET^{(a)}_{a,b}}{\log a}\to1+\rho e^{-1/\rho},\qquad
 \frac{\mathbb ET^{(b)}_{a,b}}{\log a}\to1+\rho.
\]
In the subcritical regime \(b=o(\log a)\),
\[
 r_a T^{(a)}_{a,b}-\log a\Rightarrow G,
 \qquad\Pr(\text{last vertex on the }a\text{-side})\to1,
\]
where \(G\) is standard Gumbel. In the supercritical regime \(b/\log a\to\infty\) with \(b=o(a)\),
\[
 \frac{T^{(a)}_{a,b}}b\Rightarrow\operatorname{Exp}(1),\qquad
 r_b(T^{(a)}_{a,b}-E)-\log b\Rightarrow G,
 \qquad\Pr(\text{last vertex on the }b\text{-side})\to1.
\]
The last statement uses the bridge contact time \(E\) in the same probability space. In the supercritical case the residual limit \(G\) is asymptotically independent of the normalized bridge delay \(cE\).

## Assumptions and scope

All graphs are finite simple undirected trees. Both leaf counts are positive integers, the sole initial informed vertex is one of the two hubs, clocks at vertices are independent rate-one Poisson processes, each call selects a neighbor uniformly and independently, and information only spreads (it is never forgotten). An exponential distribution is parameterized by **rate**. Each displayed convergence is as the integer \(a\) tends to infinity along an arbitrary sequence satisfying the indicated conditions. The Gumbel distribution has CDF \(\exp(-e^{-x})\) for real \(x\). No independence is asserted between the two different hub-start experiments, only the indicated auxiliary edge delays within each representation.

## Proof

**1. Independent edge contacts.** Thinning a vertex's rate-one Poisson clock by its independently selected neighbors yields mutually independent oriented-edge Poisson processes. Superposing the two orientations of each edge gives an independent Poisson process of contacts on that edge, at rate \(1/\deg(x)+1/\deg(y)\). For the pendant edges at \(u\), this rate is \(r_a\); at \(v\), it is \(r_b\); for the central bridge, it is \(c\). Starting with \(u\) informed, the bridge's first contact takes time \(E\), the last contact with an \(u\)-leaf takes \(M_a\), and after the bridge first contacts, the residual independent contacts with \(v\)-leaves take \(M_b\). The strong Markov property and independence of the Poisson processes give the exact maximum representation and its integrated CDF. Interchanging hub labels gives the second representation.

**2. Exact finite moment and finishing-side certificate.** Define \(H_b=\sum_{j=1}^b1/j\) and, for \(1\le i\le a\),
\[
 B_i=\frac{c}{c+i r_a}\prod_{j=1}^b\frac{j r_b}{i r_a+j r_b}.
\]
The formula for the maximum of exponential variables gives \(\mathbb E[e^{-s M_b}]=\prod_{j=1}^b jr_b/(s+jr_b)\); thus \(B_i=\mathbb E[e^{-ir_a(E+M_b)}]\). Expanding the tail of \(M_a\) gives, exactly,
\[
 \Pr(M_a>E+M_b)=\sum_{i=1}^a(-1)^{i+1}\binom ai B_i,
\]
\[
 \mathbb ET^{(a)}_{a,b}=\frac1c+\frac{H_b}{r_b}
 +\sum_{i=1}^a\frac{(-1)^{i+1}}{i r_a}\binom ai B_i.
\]
The second equality follows by writing \(\max(M_a,Y)=Y+(M_a-Y)_+\), with \(Y=E+M_b\), and integrating the exponential tail terms. These are exact finite rational expressions in the integer parameters, not approximations.

**3. Source-order lemma.** More generally, for independent nonnegative \(X,Y,E\) with continuous CDFs \(F_X,F_Y\), if \(F_X(t)/F_Y(t)\) is nondecreasing for \(t>0\), then
\[
 \max\{X,E+Y\}\le_{\mathrm{st}}\max\{Y,E+X\}.
\]
Indeed, conditioning on \(E=s\le t\), the difference between the two CDFs at \(t\) is an average of \(F_X(t)F_Y(t-s)-F_Y(t)F_X(t-s)\), which is nonnegative by the ratio assumption. Here \(F_{M_a}(t)=(1-e^{-r_a t})^a\). For \(a\ge b\), \(r_a\le r_b\), and
\[
 \frac{d}{dt}\log\frac{F_{M_a}(t)}{F_{M_b}(t)}
 =\frac{a r_a}{e^{r_a t}-1}-\frac{b r_b}{e^{r_b t}-1}\ge0.
\]
The inequality holds because \(r/(e^{rt}-1)\) decreases with \(r>0\), and \(a\ge b\); it is strict for \(a>b\). The source ordering follows. This argument preserves independence inside each experiment; merely coupling the two maxima monotonically would not suffice.

**4. Critical scale and finishing mark.** If \(b/\log a\to\rho\in(0,\infty)\), then \(b=o(a)\), \(c b\to1\), and hence \(E/\log a\Rightarrow\rho Z\). Standard exponential-max calculations give \(r_a M_a-\log a\Rightarrow G\), so \(M_a/\log a\to1\) in probability, while \(M_b/\log a\to0\) in probability, since \(\log b=o(\log a)\). Joint convergence follows from independence; the continuous mapping theorem gives the two broadcast-time laws. The last-informed-side event for the \(a\)-hub source is \(M_a>E+M_b\). The limiting inequality \(1>\rho Z\) has no boundary mass, giving the finishing-side probability. The normalized maxima and bridge times have uniformly bounded second moments, so the sequence of normalized completion times is uniformly integrable, proving the mean limits. The atom and tail follow directly from the exponential law.

**5. Outside the window.** If \(b=o(\log a)\), the bridge plus \(b\)-side maximum is \(o_{\Pr}(\log a)\), whereas \(M_a/\log a\to1\). Thus \(T^{(a)}_{a,b}=M_a\) with probability tending to one, yielding the Gumbel fluctuation and last-side assertions. If \(b/\log a\to\infty\) and \(b=o(a)\), then \(c b\to1\), \(M_a/b\to0\) and \(M_b/b\to0\), so \(T^{(a)}_{a,b}/b\Rightarrow\operatorname{Exp}(1)\). Moreover \(E/\log a\to\infty\) in probability while \(M_a=O_{\Pr}(\log a)\), making \(T^{(a)}_{a,b}=E+M_b\) with probability tending to one. The ordinary exponential-max limit for \(M_b\), independent of \(E\), gives the residual Gumbel and joint independence claims.

## Verification

Run `python3 checker.py` from this directory using Python's standard library. It independently computes exact expected completion times and last-side probabilities using a finite-state continuous-time Markov recursion and compares them, as exact rational numbers, with the closed expressions in step 2 for all \(1\le a,b\le9\). It also checks the two source means for all these values, independently evaluates finite-time CDF ordering by numerical quadrature, and performs seeded scaling diagnostics. Successful execution reports **369 exact comparisons and bounds** plus the two diagnostics. Numerical diagnostics are not used as proofs of any limit or ordering; those are established by steps 3–5.

## Relationship to prior work

Acan, Collevecchio, Mehrabian and Wormald establish the independent exponential edge-contact representation for asynchronous push-pull on arbitrary graphs, and derive first-order balanced-double-star spread estimates. This foundational reduction is explicitly used rather than claimed new. Giakkoupis, Mallmann-Trenn and Saribekyan use the balanced double star for comparing classical rumor spreading with agent-based protocols. The present result addresses the unbalanced double star, the full finite-time completion law, a stochastic comparison between initial hubs, and a logarithmic imbalance crossover with a last-vertex mark and a limiting atom. The checked relevant sections of those papers do not present this classification. A general edge-clock reduction alone does not state the source-order ratio criterion or derive these limiting laws, although it supplies their main starting point. Historical priority outside the inspected literature remains a limitation.

## Limitations

Results require Poisson vertex calls and uniform independent neighbor selection, exactly two stars joined by one bridge, no recovery, and initial information at a hub. The threshold theorem concerns strongly unbalanced stars with the small side of order the logarithm of the large side; it is not an all-graph broadcast theorem, not a general statement for synchronous calls, and does not assess agent-based alternatives. The finite formulas and comparison remain valid without asymptotic assumptions. The literature check is not a proof of global uniqueness, and independent review has not occurred.

## References

1. H. Acan, A. Collevecchio, A. Mehrabian, and N. Wormald, *On the push&pull protocol for rumour spreading*, arXiv:1411.0948 (first posted 2014-11-04), Proposition 13 and Sections 2.2–2.4. https://arxiv.org/abs/1411.0948
2. G. Giakkoupis, F. Mallmann-Trenn, and H. Saribekyan, *How to Spread a Rumor: Call Your Neighbors or Take a Walk?*, arXiv:2006.02368v1 (posted 2020-06-03), Section 4.2 and comparison protocol definitions. https://arxiv.org/abs/2006.02368
