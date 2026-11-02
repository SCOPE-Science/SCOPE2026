# A square-root cascade law for finite-core SIR epidemics on complete bipartite graphs

## Finding

**Finite-core cascade theorem.** Fix an integer \(b\ge2\). For each integer \(n\ge1\), run the stochastic susceptible–infectious–removed (SIR) epidemic on the complete bipartite graph \(K_{n,b}\), consisting of \(n\) peripheral vertices and \(b\) core vertices. Initially only core vertex 1 is infectious. Every infected vertex is infectious for its independently sampled lifetime; every ordered core–periphery contact occurs at rate \(\lambda_n\), independently of all other contacts and lifetimes. A contact infects a susceptible recipient, and recovery is permanent. Let \(C_n\subseteq\{1,\ldots,b\}\) be the set of eventually infected core vertices and \(X_n\) the number of eventually infected peripheral vertices.

Assume core infectious periods \(R_1,\ldots,R_b\) are independent, strictly positive, finite almost surely, and peripheral infectious periods are independent copies of a nonnegative finite random variable \(J\) with \(\mu=\mathbb E J\in(0,\infty)\). Assume all these variables and contact processes are mutually independent. Suppose
\[
\lambda_n\longrightarrow0,\qquad n\lambda_n\longrightarrow\infty,\qquad n\lambda_n^2\longrightarrow\xi\in[0,\infty].
\]
Here \(\xi=\infty\) is permitted. If \(0<\xi<\infty\), conditional on the core periods \((R_i)\), form a directed random graph on the core: for each ordered pair of distinct vertices \(i,j\), independently place an arc \(i\to j\) with probability \(1-\exp(-\xi\mu R_i)\). Let \(C\) be the set reachable from vertex 1. When \(\xi=0\), set \(C=\{1\}\); when \(\xi=\infty\), set \(C=\{1,\ldots,b\}\). Then the joint limit is
\[
\boxed{\big(C_n,\;X_n/(n\lambda_n)\big)\ \Longrightarrow\ \big(C,\;\sum_{i\in C}R_i\big).}
\]
In particular, the **two-step core cascade changes scale at** \(\lambda_n\asymp n^{-1/2}\). Below this scale, yet with \(n\lambda_n\to\infty\), only the initial core vertex is infected with probability tending to one; above it, all \(b\) core vertices are infected with probability tending to one. At the scale \(\lambda_n=c/\sqrt n\) with fixed \(c>0\), the limiting random directed graph has nontrivial, lifetime-dependent arc probabilities.

**Explicit two-core Markovian law.** If \(b=2\), all infectious periods are independent rate-one exponentials, and \(\lambda_n=c/\sqrt n\) with \(c>0\), then, with independent rate-one exponentials \(R_1,R_2\), let \(B\), conditional on \(R_1\), be Bernoulli with success probability \(1-e^{-c^2R_1}\). Then
\[
\boxed{\left(\mathbf1_{\{2\in C_n\}},X_n/\sqrt n\right)
\Longrightarrow\left(B,c(R_1+BR_2)\right).}
\]
Consequently \(\mathbb P(B=1)=c^2/(1+c^2)\). The Laplace transform of the peripheral limit \(Y=c(R_1+BR_2)\) is, for every \(t\ge0\),
\[
\boxed{\mathbb E e^{-tY}=\frac1{1+c^2+ct}
+\frac1{1+ct}\left(\frac1{1+ct}-\frac1{1+c^2+ct}\right).}
\]
The expected peripheral size additionally obeys \(\mathbb E X_n/\sqrt n\to c\big(1+c^2/(1+c^2)\big)\). This is a continuously varying stochastic crossover, **not** a nonzero critical reproduction threshold in the fixed-core family.

**Exact finite-population companion.** For arbitrary \(n\ge1\), \(\lambda>0\), and \(b=2\) in the rate-one Markovian model, put \(p=\lambda/(1+\lambda)\), and let \(K\sim\operatorname{Bin}(n,p)\) and \(K'\sim\operatorname{Bin}(n-1,p)\). Then
\[
\boxed{\begin{aligned}
\mathbb P(2\in C_n)&=1-\mathbb E\frac1{1+\lambda K},\\
\mathbb E X_n&=np\left(1+\frac1{1+\lambda}-\mathbb E\frac1{1+\lambda(1+K')}\right).
\end{aligned}}
\]
These are exact finite expressions, not merely scaling approximations.

## Assumptions and scope

The graph is a fixed-width complete biclique, with \(b\ge2\) fixed and \(n\to\infty\). The epidemic has one initial core seed, independent infectious periods, independent directed Poisson contacts of identical rate along every bipartite edge, and no reinfection. In the general limit theorem, core infectious periods need not be exponential or identically distributed, but they must be strictly positive and almost surely finite; the peripheral period distribution has finite positive mean \(\mu\). The claim concerns joint **final-outcome distributions**, not epidemic completion time. The exact finite and explicit Laplace formulas require unit-rate exponential infectious periods throughout.

## Proof

**1. Exact directed-path representation.** Sample all infectious periods before the epidemic and, for each ordered edge \(u\to v\), sample an independent first-contact delay with exponential rate \(\lambda_n\), measured from the time \(u\) becomes infectious. Declare the ordered edge open if the delay is shorter than \(u\)'s infectious period. The vertices eventually infected are precisely those reachable from the initial seed by directed open paths. Indeed, a directed path can be traversed successively by its finite-delay contacts, and every actual infection creates such a predecessor path. This is the epidemic-percolation representation, already established in Kenah and Robins (2006/2007); the path representation itself is not claimed as new.

Conditional on fixed \((R_i)\), for core \(i\) and peripheral vertex \(v\), the event that \(i\to v\) is open has probability \(1-e^{-\lambda_nR_i}\). For peripheral \(v\) and core \(j\), the event that \(v\to j\) is open has probability \(1-e^{-\lambda_nJ_v}\). The first events for distinct ordered edges are independent conditional on the durations, as are the second events conditional on \(J_v\). Every directed path between core vertices alternates through peripheral vertices; replacing every two-edge segment \(i\to v\to j\) by a core arc preserves core reachability exactly.

**2. Rare two-step contacts form independent directed arcs.** For distinct core vertices \(i,j\) define \(Z_{ij,v}\) as the indicator that \(i\to v\to j\) is an open two-step path. For fixed \((R_i)\), the arrays indexed by \(v\) are independent identically distributed, and
\[
\mathbb P(Z_{ij,v}=1\mid R_1,\ldots,R_b)
=(1-e^{-\lambda_nR_i})\,\mathbb E(1-e^{-\lambda_nJ})
\sim \lambda_n^2\mu R_i.
\]
If \(0<\xi<\infty\), the expected count \(N_{ij,n}=\sum_{v=1}^nZ_{ij,v}\) therefore tends to \(\xi\mu R_i\). Simultaneous contributions by the same peripheral vertex to two *different* ordered core arcs have probability \(o(1/n)\): for two different origins, their probability is at most a constant (depending on fixed \((R_i)\)) times \(\lambda_n^2\mathbb E(1-e^{-\lambda_nJ})=O(\lambda_n^3)\); for one common origin and two destinations, the bound is a constant times \(\lambda_n\mathbb E(1-e^{-\lambda_nJ})^2=o(\lambda_n^2)\). The latter little-oh follows from dominated convergence applied to \((1-e^{-\lambda_nJ})^2/\lambda_n\le J\) and finiteness of \(\mathbb E J\). Because \(n\lambda_n^2\) stays bounded, both joint-event contributions vanish after multiplication by \(n\).

The elementary law of small numbers for these finite-dimensional indicator vectors therefore yields conditionally independent Poisson limiting counts \(N_{ij}\) of means \(\xi\mu R_i\). The indicators \(\mathbf1_{\{N_{ij,n}>0\}}\) converge jointly to conditionally independent Bernoulli arcs with probability \(1-e^{-\xi\mu R_i}\). For \(\xi=0\), a union bound eliminates all inter-core arcs. For \(\xi=\infty\), each specified two-step arc is present with probability tending to one, since its absence probability is \((1-\mathbb P(Z_{ij,v}=1\mid R))^n\to0\). As there are finitely many core vertices, the reachable core set \(C_n\) converges jointly with the sampled core lifetimes to the asserted \(C\).

**3. Uniform peripheral count approximation.** For each deterministic subset \(S\) of the core, let \(Y_n(S)\) count peripheral vertices receiving at least one open edge from a vertex in \(S\). Conditional on all core durations, 
\[
Y_n(S)\sim\operatorname{Bin}\left(n,1-\exp(-\lambda_n\sum_{i\in S}R_i)\right).
\]
Since \(n\lambda_n\to\infty\), conditional means divided by \(n\lambda_n\) tend to \(\sum_{i\in S}R_i\), and conditional variances divided by \((n\lambda_n)^2\) tend to zero. There are only \(2^b\) subsets, so the approximation is uniform in \(S\) in probability. A peripheral vertex is infected exactly when it has an open incoming edge from some ultimately infected core vertex. Hence \(X_n=Y_n(C_n)\) and
\[
X_n/(n\lambda_n)-\sum_{i\in C_n}R_i\xrightarrow{\mathbb P}0.
\]
Together with joint core reachability convergence, this proves the full theorem, including both degenerate endpoint regimes. No independence between \(C_n\) and \(Y_n(C_n)\) was assumed.

**4. Explicit two-core law.** At critical rate \(c/\sqrt n\), the single arc from core 1 to core 2 has conditional existence probability \(1-e^{-c^2R_1}\). The second core period \(R_2\) remains independent of this event. When the periods are independent unit exponentials, the limit in the theorem becomes \(c(R_1+BR_2)\). Conditioning on \(R_1\) gives \(\mathbb P(B=1)=1-\mathbb E e^{-c^2R_1}=c^2/(1+c^2)\). Conditioning on \((R_1,B)\) and integrating the two exponential Laplace transforms yields the displayed \(\mathbb E e^{-tY}\). Since \(X_n/(n\lambda_n)\le\sum_{i=1}^b R_i\) in conditional expectation and the core durations have finite expectation here, the family is uniformly integrable after a straightforward second-moment bound: \(X_n\le Y_n(\{1,2\})\) with conditional binomial mean at most \(n\lambda_n(R_1+R_2)\) and variance at most that mean. Consequently the limiting mean is \(c(1+\mathbb EB)=c(1+c^2/(1+c^2))\).

**5. Exact finite two-core formulas.** Let \(R\sim\operatorname{Exp}(1)\) be the initial core infectious period and \(p=\lambda/(1+\lambda)\). Conditional on \(R=r\), each peripheral vertex is an intermediary from core 1 to core 2 with probability \(p(1-e^{-\lambda r})\), independently over peripheral vertices. Therefore
\[
\mathbb P(2\notin C_n)
=\mathbb E_R(1-p+pe^{-\lambda R})^n
=\mathbb E_K(1+\lambda K)^{-1},
\quad K\sim\operatorname{Bin}(n,p).
\]
For a tagged peripheral vertex \(v\), conditional on \(R=r\), its probability of remaining uninfected is
\[
e^{-\lambda r}\left[1-p+p(1-p+pe^{-\lambda r})^{n-1}\right].
\]
The first factor says core 1 does not reach \(v\). In that event core 2 can be infected only via the other \(n-1\) peripheral vertices; the remaining bracket accounts for the possibility that core 2 then reaches \(v\). Integrating over \(R\), using the binomial expansion with \(K'\sim\operatorname{Bin}(n-1,p)\), and multiplying the tagged infection probability by \(n\) gives the stated exact \(\mathbb E X_n\) formula. Finally \(K\lambda\to c^2\) in probability for \(\lambda=c/\sqrt n\), recovering the limiting infection probability and mean directly from these finite identities.

## Verification

A standalone Python 3 standard-library checker (`CHECKER.py`) compares the exact finite formulas for core-2 infection probability and peripheral outbreak expectation against a separately constructed finite-state continuous-time Markov recursion with exact rational arithmetic. It performs 70 exact equality assertions for \(1\le n\le7\) and five infection rates, plus deterministic numerical convergence diagnostics for the critical \(n^{-1/2}\) scaling. These finite checks support, but cannot replace, the analytic proof of the infinite-population limits. Conditional independence and the little-oh bounds in the proof are the essential non-finite steps.

## Relationship to prior work

Kenah and Robins' epidemic-percolation network provides the exact SIR directed-path representation employed in Step 1 and is fully credited. Ball, Sirl and Trapman (first publicly available 2022-04-14) establish limits for epidemics in *large* internally transmitting sub-communities with weaker between-community contacts; that framework motivates the question of persistent randomness under weak coupling, but its model does not have a fixed-width core with all transmission exclusively across one complete bipartite cut. Omic and collaborators analyze the complete-bipartite scale in a **persistent SIS** virus model, not the present finite SIR final-outbreak law. Existing general multi-type, epidemic-percolation and bipartite-threshold results make historical coverage a serious issue; the claim is the precise finite-core directed-cascade **joint limit and two-core distribution**, not the generic percolation representation or the observation that square-root scales can arise.

## Limitations

The core size \(b\) is fixed; the theorem does not address a core growing with \(n\), within-part contacts, heterogeneous edge rates, repeated introductions, or time-to-extinction. The \(\lambda_n\to0\) and \(n\lambda_n\to\infty\) conditions exclude constant-rate macroscopic outbreaks and extremely rare infections. The exact formulas and stated Laplace transform specialize to exponential infectious periods. The result gives a crossover in connectivity and outbreak size, not a universal nonzero reproduction threshold. Novelty is supported by comparisons with the cited scientific results, but unlocated historical coverage remains a risk.

## References

1. F. Ball, D. Sirl and P. Trapman, *SIR epidemics in populations with large sub-communities*, first publicly available 2022-04-14, [arXiv:2204.06902](https://arxiv.org/abs/2204.06902).
2. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, first publicly available 2006-10-30, [arXiv:q-bio/0610057](https://arxiv.org/abs/q-bio/0610057); *Physical Review E* 76, 036113 (2007).
3. J. Omic, R. E. Kooij and P. Van Mieghem, *Virus spread in complete bipartite graphs*, 2008, [DOI:10.4108/ICST.BIONETICS2007.2399](https://doi.org/10.4108/ICST.BIONETICS2007.2399).
4. C. Fransson and P. Trapman, *SIR epidemics and vaccination on random graphs with clustering*, first publicly available 2018-02-14, [arXiv:1802.05011](https://arxiv.org/abs/1802.05011).
