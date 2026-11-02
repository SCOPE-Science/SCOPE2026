# All-deadline source ordering and a logistic crossover for two-choice biclique coverage

## Finding
For integers \(a,b\geq1\), let \(K_{a,b}\) have vertex parts \(A\) and \(B\). From a fixed initial vertex, a discrete-time walker receives two independent uniform neighbour offers **with replacement** on every step, and chooses one using the full past and current offers. Write \(T^A_{a,b}\) and \(T^B_{a,b}\) for the optimally controlled vertex-cover times when the initial vertex is in \(A\) and \(B\), respectively, counting it as already visited at time zero.

Define independent positive-integer geometric variables \(G_{m,r}\), for \(1\le r\le m\), with success probabilities
\[
q_{m,r}=\frac{r(2m-r)}{m^2},\qquad U_m=\sum_{r=1}^{m}G_{m,r}.
\]
Copies of \(U_a\) and \(U_b\) appearing together below are independent. First-visit-greedy control (choose an offered unvisited neighbour whenever possible) is optimal simultaneously for every completion deadline, and the following **exact joint-law representation** holds:
\[
T^A_{a,b}\overset d=\max\{2U_a-2,\;2U_b-1\},\qquad
T^B_{a,b}\overset d=\max\{2U_a-1,\;2U_b-2\}.
\]
In particular, if \(F_m(t)=\Pr(U_m\leq t)\), then for every integer \(t\geq0\),
\[
\begin{aligned}
\Pr(T^A_{a,b}\leq2t)&=F_a(t+1)F_b(t),\\
\Pr(T^B_{a,b}\leq2t)&=F_a(t)F_b(t+1),\\
\Pr(T^A_{a,b}\leq2t+1)&=\Pr(T^B_{a,b}\leq2t+1)=F_a(t+1)F_b(t+1).
\end{aligned}
\]
**Source ordering:** if \(a\geq b\), then for every integer deadline \(h\geq0\),
\[
\Pr(T^A_{a,b}\leq h)\geq\Pr(T^B_{a,b}\leq h).
\]
For \(a>b\) the ordering is strict for some even deadlines. Thus an initial vertex in the **larger** part is stochastically optimal among the two possible source parts (despite having smaller vertex degree).

The exact expected source advantage is
\[
\boxed{\quad \mathbb E T^B_{a,b}-\mathbb E T^A_{a,b}
 =\Pr(U_a>U_b)-\Pr(U_b>U_a).\quad}
\]
For \(a>b\), this lies in \((0,1]\): it equals one exactly for \(b=1\), and lies strictly below one for \(b\geq2\). It is zero when \(a=b\).

**Critical crossover:** fix \(\delta\in\mathbb R\), let \(b_n=n\) and \(a_n=n+\lfloor \delta n/\log n\rfloor\), and use either initial part. With a standard Gumbel random variable \(G\),
\[
\boxed{\quad
\frac{T_{a_n,b_n}-n\log n-n\log2}{n}
\ \Longrightarrow\ G+\log(1+e^\delta).\quad}
\]
Moreover,
\[
\boxed{\quad \mathbb E T^B_{a_n,b_n}-\mathbb E T^A_{a_n,b_n}
\longrightarrow \tanh(\delta/2).\quad}
\]
The last formula is signed: for negative \(\delta\), the first part is smaller and starting there is worse. In the same window, the limiting probability that the first collector finishes later than the second is \(e^\delta/(1+e^\delta)\). In particular, at equal part sizes the cover-time limit acquires an additional \(\log2\) Gumbel shift from the competition of two independent bottlenecks. These conclusions concern the full optimal control problem, not merely a specified heuristic.

## Assumptions and scope
All graphs are finite, simple, undirected and complete bipartite, with both part sizes positive. Neighbor offers are independent across the two offers and all times, uniformly distributed within the opposite part. The controller cannot refuse to move, look ahead or teleport. Cover time is measured in individual edge steps. The probability convention is \(\Pr(G_{m,r}=j)=(1-q_{m,r})^{j-1}q_{m,r}\) for \(j=1,2,\ldots\); the case \(q_{m,m}=1\) is deterministic. The standard Gumbel law has CDF \(\exp(-e^{-x})\). The logarithm is natural.

## Proof
**1. Optimal policy and exact decomposition.** Moves alternate deterministically between \(A\) and \(B\). At a move into a part of size \(m\) with \(k\) previously visited vertices, the event that at least one offered vertex is new has probability \(1-(k/m)^2\), independent of which particular \(k\) vertices have been visited. Every policy has conditional probability at most that value of increasing this part's visited count; choosing a new offer whenever one is present attains it. Couple any competing count process to the greedy count process using shared uniforms for successive visits into the part. If the counts agree, the greedy birth probability is no smaller; if the greedy count is ahead, the competitor can gain at most one in a step. Thus the greedy count never falls behind under the coupling. Apply this separately on both alternating parity classes. Completion by any deadline is an increasing event in both counts, proving universal deadline optimality, including randomized history-dependent policies.

With \(r\) still-unvisited vertices in a part of size \(m\), the waiting number of opportunities until another new vertex is chosen is \(G_{m,r}\), independently between levels, with the stated \(q_{m,r}\). The two streams of offered labels, on odd and even steps, are independent. Starting in \(A\) means it already has one visited vertex before the even-step stream begins, so the required number of future draws to cover \(A\) has the law \(U_a-1\): this follows by removing the deterministic first draw from a fresh full collector and using permutation symmetry. Part \(B\) begins empty and requires \(U_b\) odd-step draws. Their last completion times are \(2(U_a-1)\) and \(2U_b-1\), respectively. The \(B\)-start formula follows by parity reversal. This proves both exact laws and their CDF products.

**2. A coupon collector comparison lemma.** Let \(F_m\) denote the above completion CDF. We prove that for \(a\geq b\), the ratio \(F_a(t)/F_b(t)\) is nondecreasing at integers \(t\) where the denominator is positive. Each geometric probability mass function is a nonnegative log-concave sequence with no interior support gaps. Such sequences are closed under convolution: the Toeplitz matrix of one sequence is totally positive of order two exactly when it is log-concave and gap-free, and Cauchy--Binet preserves nonnegative two-by-two minors under matrix multiplication. Summing the mass function cumulatively is convolution with the log-concave step sequence \((1,1,\ldots)\). Consequently every \(F_m(t)\) is log-concave in \(t\).

Next observe, for fixed \(r\leq m\), that \(q_{m+1,r}\leq q_{m,r}\). If \(0<p'\leq p\leq1\), the geometric probability-generating functions give
\[
\frac{p'z/(1-(1-p')z)}{pz/(1-(1-p)z)}
 =\frac{p'}p\left(1+\frac{(p-p')z}{1-(1-p')z}\right),
\]
whose coefficients are a probability distribution on nonnegative integers. Hence an independent \(\operatorname{Geom}(p')\) is distributed as \(\operatorname{Geom}(p)+Z\), with \(Z\geq0\) independent. Apply this to all levels \(r\leq m\), and include the new level \(r=m+1\), for which the geometric wait is exactly one. We obtain the exact *independent-delay representation*
\[
U_{m+1}\overset d=U_m+W_m,\qquad W_m\geq1,
\]
with independence between the right-hand variables. Iteration yields \(U_a\overset d=U_b+W\) where \(W\geq a-b\) is independent of \(U_b\).

Because \(F_b\) is log-concave, for each fixed integer \(w\geq0\) the ratio \(F_b(t-w)/F_b(t)\) is nondecreasing in \(t\): it is a product of \(w\) consecutive nondecreasing ratios \(F_b(j-1)/F_b(j)\). Thus
\[
\frac{F_a(t)}{F_b(t)}
 =\mathbb E\left[\frac{F_b(t-W)}{F_b(t)}\right]
\]
is nondecreasing. Cross multiplication gives
\(F_a(t+1)F_b(t)\geq F_a(t)F_b(t+1)\), including at support boundaries by zero conventions. Comparing the exact even-deadline CDFs proves the source stochastic order; odd-deadline CDFs are identical. If \(a>b\), the ratio is strictly increasing somewhere (the support starts later), so at least one even-deadline inequality is strict.

**3. Exact expected advantage and sharp bound.** Use a common pair of independent collector times \((U_a,U_b)\) in the two displayed laws. If \(U_a>U_b\), starting in \(A\) saves exactly one step; if \(U_a<U_b\), it costs exactly one; if they tie, the two cover times coincide. Taking expectations gives the probability-difference formula and the bound by one. The independent-delay representation implies \(U_a\) strictly stochastically dominates \(U_b\) for \(a>b\). For an independent \(U_b'\), the function \(x\mapsto \Pr(x>U_b')-\Pr(x<U_b')\) is strictly increasing on the support, and its expectation at \(x=U_b\) is zero by exchangeability. Thus the expected advantage is strictly positive for \(a>b\); it is strictly smaller than one when \(b\geq2\), because then \(U_b\) has an unbounded right tail and can exceed independent \(U_a\) with positive probability. When \(b=1<a\), \(U_b=1\) deterministically and \(U_a\geq a>1\), so the advantage is exactly one. For \(a=b=1\), the two sources are symmetric and the advantage is zero.

**4. One-collector Gumbel limit.** Independently over \(r\), write \(U_m=\sum_{r=1}^{m}G_{m,r}\) and note
\[
\frac{2}{m}\mathbb E U_m=H_{2m-1}+\frac1m,
\qquad
\mathbb E U_m=\frac m2H_{2m-1}+\frac12.
\]
For each fixed \(K\), the first \(K\) summands \((2/m)G_{m,r}\) converge jointly as \(m\to\infty\) to independent exponentials of rates \(r=1,\ldots,K\). The remainder's mean equals
\[
\sum_{r=K+1}^{m}\left(\frac1r+\frac1{2m-r}\right)
 =\log(m/K)+\log2+o(1)
\]
for fixed \(K\). Its variance is at most \(4\sum_{r>K}r^{-2}\), uniformly in \(m\), because \(q_{m,r}\geq r/m\). Let \(m\to\infty\), then \(K\to\infty\). The sum of independent exponentials of rates \(1,\ldots,K\) is distributed as the maximum of \(K\) independent unit exponentials, and this maximum minus \(\log K\) tends to a standard Gumbel. Therefore
\[
\frac{2U_m}{m}-\log m-\log2\Longrightarrow G.
\]
The variance bound also gives bounded second centered moments on this scale.

**5. Competing Gumbels and the signed logistic window.** For \(a_n=n+\lfloor\delta n/\log n\rfloor\) and \(b_n=n\), the two independent normalized coupon times satisfy
\[
\left(\frac{2U_{a_n}-n\log n-n\log2}{n},
\frac{2U_{b_n}-n\log n-n\log2}{n}\right)
\Longrightarrow (G_1+\delta,G_2),
\]
where \(G_1,G_2\) are independent standard Gumbels. Fixed parity offsets vanish after scaling. The maximum has CDF
\(\exp[-(1+e^\delta)e^{-x}]\), establishing the displayed Gumbel shift. The Gumbel difference has logistic law, so
\[
\Pr(G_1+\delta>G_2)=\frac{e^\delta}{1+e^\delta}.
\]
There is no limiting mass at a tie. Passing to the bounded expected-advantage identity proves the hyperbolic-tangent limit. No assertion about a Gaussian or law-of-large-numbers approximation was used to infer this distributional result.

## Verification
The standalone `checker.py` reconstructs the coupon pure-birth law with exact rational arithmetic and compares the full finite-state Bellman optimization (all offered-pair choices, both initial parts, every short deadline) against the independent-collector CDF. It also tests source-order inequalities, CDF log-concavity, the geometric delay factorization coefficient by coefficient, and the harmonic mean identity. A deterministic asymptotic-mean diagnostic is included. The current packaged checker completed **4,661** assertions and diagnostics. The infinite claims rest on the proof above, not on finite enumeration. Reproduce with `python3 checker.py` in the extracted package directory.

## Relationship to prior work
The two-choice random walk and its general cover-time optimization problem are established by Georgakopoulos, Haslegrave, Sauerwald and Sylvester [1]; their paper gives a complete-graph benchmark and broad family bounds, but no complete-bipartite source-part ordering or source-advantage crossover in the inspected text. The fixed-start greedy decision on bicliques, which follows directly from alternation and occupancy, is not asserted to be historically new. Xu and Tang [2] prove related choice-coupon results, including an optimal least-collected policy and a distinct-offer first-set expectation; these are one-collector quantities and do not supply the biclique source CDF ordering. Doumas and Spektor [3] prove refined one-collector asymptotics and a Gumbel law for **distinct** multi-draw offers; these known one-collector ideas are explicitly separated here from the with-replacement, two-part source comparison and the signed critical window. The standard Gumbel and logistic distributions themselves are classical and are not claimed as discoveries.

## Limitations
This result is restricted to complete bipartite graphs, two independent uniform offers with replacement per step, and vertex-cover time. The source advantage never exceeds one discrete step, even where the total cover time is much larger; the principal significance is all-deadline source ordering and its exact crossover, not a large performance improvement. The critical limit assumes the displayed near-balanced scaling; general sparse graphs, nonuniform offers, larger numbers of offers, and directed or time-varying walks are not covered. No claim of independent mathematical verification or exhaustive historical priority is made.

## References
[1] A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, first public version 2019-11-12, subsequently *Combinatorics, Probability and Computing* 31 (2022), 73–100. https://arxiv.org/abs/1911.05170

[2] W. Xu and A. K. Tang, *A Generalized Coupon Collector Problem*, *Journal of Applied Probability* 48 (2011), 1081–1094. https://people.ece.cornell.edu/atang/pub/11/Coupon_collector.pdf

[3] A. V. Doumas and S. Spektor, *Two Multi-Draw Coupon Collector Models with Different Retention Rules*, arXiv:2607.01463, publicly posted 2026-07-01. https://arxiv.org/abs/2607.01463
