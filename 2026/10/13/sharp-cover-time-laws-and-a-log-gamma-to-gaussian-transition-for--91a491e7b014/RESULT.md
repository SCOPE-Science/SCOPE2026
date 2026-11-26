# Critical log-Gamma cover-time laws for steered balanced bicliques

## Finding

Start at any vertex of the complete bipartite graph \(K_{m,m}\), with the initial vertex already visited. At each step, independently, a steering opportunity occurs with probability \(\varepsilon_m\). On such a step a controller may choose any neighbor using the past; otherwise the step goes to an independently uniform neighbor. Write \(\tau_m^*\) for the vertex-cover time under the policy that takes an unvisited neighbor whenever it can. This policy attains the best achievable cover-time CDF at each horizon.

If \(m\varepsilon_m\to c\) for any real \(c\in[0,\infty)\), then
\[
\frac{\tau_m^*}{2m}-\log m\ \Longrightarrow\ \max\{-\log H_1,-\log H_2\},
\qquad H_1,H_2\ \text{independent }\operatorname{Gamma}(c+1,1).
\]
The gamma parameters are shape and rate. Equivalently, the limiting best achievable cover-time CDF at \(x\in\mathbb R\) is
\[
\left[\frac{\Gamma(c+1,e^{-x})}{\Gamma(c+1)}\right]^2,
\qquad \Gamma(a,y)=\int_y^\infty t^{a-1}e^{-t}\,dt.
\]
This is a continuous critical-window family, including noninteger \(c\). At \(c=0\) the CDF reduces to \(\exp(-2e^{-x})\), the standard Gumbel CDF translated by \(\log 2\).

## Assumptions and scope

The walk alternates between equal parts, edges go between every pair of opposite-side vertices, and steering opportunities are independent of the past. The controller has no power on uncontrolled steps. The claim concerns distributional convergence for the critical scale \(m\varepsilon_m\to c<\infty\); it does not assert a uniform error rate, a limit for fixed positive steering, or a limit on unequal parts. A geometric waiting time counts its successful trial.

## Proof

**Reduction to two clocks.** At an arrival to a part with \(k\ge1\) unseen vertices, the greedy policy discovers one with conditional probability \(p_{m,k}=\varepsilon_m+(1-\varepsilon_m)k/m\), the largest possible given the history. Couple its unseen counts with those of any other policy. At any arrival where the two counts on that side are equal and positive, use a common uniform variable for the two discoveries. A success for the other policy then forces a success for greedy. Conditional on each discovery indicator the rest of each step can be sampled from its prescribed conditional distribution, so this preserves each walk's law. If the greedy count is strictly smaller, its order cannot reverse in a step because each count falls by at most one; zero stays zero. Iteration over both parts gives the greedy optimum for every horizon.

For the greedy policy, the count transition depends only on the count in the part being entered; its indicators can be generated from fresh independent uniforms. The count paths for the two parts thus use disjoint subsequences of independent randomness. Let \(S_m=\sum_{k=1}^m G_{m,k}\) for independent geometrics of parameters \(p_{m,k}\). This is the completion clock on the initially empty part, measured in arrivals. On the initial part the clock has law \(S_m-1\), because \(p_{m,m}=1\). Accordingly, with independent copies \(S_m',S_m''\),
\[
\tau_m^*\overset d=\max\{2S_m'-1,\ 2S_m''-2\}.
\]

**Critical transform.** For large \(m\) set \(a_m=m\varepsilon_m/(1-\varepsilon_m)\) and \(b_m(s)=(m+a_m)(e^{s/m}-1)\). Then \(p_{m,k}=(k+a_m)/(m+a_m)\) and \(a_m\to c\). For real \(s\) in a fixed sufficiently small neighborhood of zero, \(1+a_m+b_m(s)>0\) for all large \(m\), which ensures the geometric transforms exist. Multiplication gives
\[
\begin{aligned}
\mathbb E e^{-s(S_m/m-\log m)}
&=m^s\prod_{k=1}^m \frac{k+a_m}{k+a_m+b_m(s)}\\
&=m^s\frac{\Gamma(m+1+a_m)}{\Gamma(m+1+a_m+b_m(s))}
      \frac{\Gamma(1+a_m+b_m(s))}{\Gamma(1+a_m)}.
\end{aligned}
\]
Because \(a_m\) is bounded, \(b_m(s)=s+O(m^{-1})\) uniformly on that neighborhood. The large-argument ratio is \(m^{-b_m(s)}(1+O(m^{-1}))\) by Stirling's formula uniformly for these bounded shifts. Hence the centered transform converges to \(\Gamma(1+c+s)/\Gamma(1+c)=\mathbb E[H^s]\) for \(H\sim\operatorname{Gamma}(c+1,1)\). Convergence of moment-generating functions on a neighborhood of zero gives \(S_m/m-\log m\Rightarrow-\log H\). The two independent clocks converge jointly, the offsets divided by \(2m\) vanish, and taking their maximum gives the theorem. The CDF follows by converting \(-\log H\le x\) to \(H\ge e^{-x}\).

## Relationship to other work

The finite two-clock representation and stochastic optimality on complete bipartite graphs are covered by *A square-root imbalance transition for optimally biased bipartite walks* ([Resultary c51f7839a720](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-square-root-imbalance-transition-for-optimally-biased-bipartit--c51f7839a720)). They are included above to specify the optimum and make the limit proof self-contained. That work studies an imbalance window at fixed positive steering probability rather than the critical vanishing-steering window.

For an integer \(j\ge0\) and exactly \(\varepsilon_m=j/(m+j)\), the single-side clock \(S_m\) coincides with the ordinary partial coupon-collection time to have only \(j\) coupons unseen out of \(m+j\) initially unseen. The geometric probabilities agree term by term. Thus the integer-shape cases connect directly to classical partial collection (Baum and Billingsley, *Asymptotic Distributions for the Coupon Collector’s Problem*, 1965, doi:10.1214/aoms/1177699813). The statement here allows every real critical intensity, including nonintegers for which this integer stopping rule is not available. Nakata and Kubo, *A coupon collector's problem with bonuses* (2006, doi:10.46298/dmtcs.3515), use extra draws triggered by distinguished coupons, rather than choices at independent steering opportunities. Bukh and Dubroff (arXiv:2605.18712) and Tung and Ueltzen (arXiv:2607.25016) give expected cover-time bounds on more general graphs, not the displayed critical law. The contribution is the optimal cover-time distributional limit across the real-valued critical window, not the geometric waiting-time decomposition, the ordinary coupon-collector limit, or the gamma-ratio method themselves.
