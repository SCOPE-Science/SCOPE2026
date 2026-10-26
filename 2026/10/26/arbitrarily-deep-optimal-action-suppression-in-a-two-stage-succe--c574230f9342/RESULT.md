# Arbitrarily deep optimal-action suppression in a two-stage success-conditioning chain

## Finding

Consider exact success-conditioning policy iteration in a discounted Markov decision process with two nonterminal decision states and one absorbing state. An action that is uniquely optimal in the first state may initially *lose* probability under every update, then recover, despite strictly increasing value at both states. The turning iteration, minimum probability, and entire policy trajectory have closed forms.

Specifically, at the downstream state \(B\), the two actions pay \(1\) and \(\varepsilon\), then terminate. At the upstream state \(A\), the safe action pays \(r\) and terminates, while the delayed action pays zero and deterministically enters \(B\). For \(0<\varepsilon,\gamma<1\), \(r>0\), and interior initial probabilities \(p,q\in(0,1)\) of the high-paying action at \(B\) and delayed action at \(A\), respectively, write \(p_k,q_k\) for their probabilities after \(k\) exact iterations. Then for all integers \(k\ge0\),

\[
p_k=\frac{p}{p+(1-p)\varepsilon^k},\qquad
\frac{q_k}{1-q_k}=\frac{q}{1-q}\left(\frac{\gamma}{r}\right)^k\left[p+(1-p)\varepsilon^k\right].
\]

The ratio determining the direction of the upstream update is \(\gamma V_{B,k}/r\), where \(V_{B,k}=\bigl(p+(1-p)\varepsilon^{k+1}\bigr)/\bigl(p+(1-p)\varepsilon^k\bigr)\) increases strictly. In the only potentially nonmonotone regime \(\gamma\varepsilon<r<\gamma\), put

\[
\tau=\frac{p(\gamma-r)}{(1-p)(r-\gamma\varepsilon)}.
\]

If \(\tau<1\), the upstream optimal-action probability decreases strictly until \(K=\lceil \log\tau/\log\varepsilon\rceil\), reaches its global minimum at \(K\), and then increases strictly, except that the minimum is attained at both \(K\) and \(K+1\) when \(\varepsilon^K=\tau\). If \(\tau\ge1\) it is nondecreasing from the start. Outside the regime \(\gamma\varepsilon<r<\gamma\), the upstream policy is monotone.

For fixed \(\gamma\varepsilon<r<\gamma\) and fixed \(q\in(0,1)\), as \(p\downarrow0\), the turning time obeys

\[
K=\frac{\log(1/p)}{\log(1/\varepsilon)}+O(1),
\qquad \min_{k\ge0}q_k=\Theta\left(p^\alpha\right),
\quad \alpha=1-\frac{\log(\gamma/r)}{\log(1/\varepsilon)}\in(0,1).
\]

In particular, the fixed-parameter family \(\varepsilon=1/4\), \(\gamma=3/4\), \(r=3/8\), \(q=1/2\), \(p=1/(1+2\cdot4^N)\) has, for every integer \(N\ge1\), strictly decreasing \(q_k\) for its first \(N\) updates, two equal global minima at \(k=N,N+1\), and then strictly increasing \(q_k\to1\). The exact minimum is

\[
q_N=q_{N+1}=\frac{3\cdot2^N}{1+2\cdot4^N+3\cdot2^N}<\frac{3}{2^{N+1}}.
\]

Thus an eventually optimal action with fixed optimal Bellman advantage \(\gamma-r=3/8\) can lose an arbitrarily large fraction of its initial probability and be suppressed for arbitrarily many iterations, even though the exact state values increase at every step.

## Assumptions and scope

There are precisely three states: nonterminal states \(A,B\), and an absorbing zero-reward state. At \(A\), two actions are available: safe yields immediate deterministic reward \(r\) and terminates; delayed yields immediate reward zero and moves to \(B\). At \(B\), two actions produce deterministic rewards \(1\) and \(\varepsilon\), respectively, and terminate. The discount factor satisfies \(0<\gamma<1\). All decisions are stationary and memoryless. Initial probabilities \(p,q\) lie strictly between zero and one. Exact, rather than sampled, state/action values are used.

The policy update at each state is the standard success-conditioning or reward-weighted update

\[
\pi_{k+1}(a\mid s)=\frac{\pi_k(a\mid s)Q_k(s,a)}{V_k(s)}.
\]

Both \(V_k(A)\) and \(V_k(B)\) are strictly positive. Rewards are nonnegative, bounded, and the absorbing state is reached in at most two decisions; the update is well-defined. When \(r<\gamma\), the delayed action at \(A\) is uniquely optimal under the optimal continuation, and the high-paying action at \(B\) is always uniquely optimal.

## Proof

**Closed downstream law.** At \(B\), the two action values are the constants \(1\) and \(\varepsilon\). Therefore

\[
p_{k+1}=\frac{p_k}{p_k+(1-p_k)\varepsilon},\qquad
\frac{p_{k+1}}{1-p_{k+1}}=\frac1\varepsilon\frac{p_k}{1-p_k}.
\]

Iteration gives the claimed formula for \(p_k\). The downstream value consequently satisfies

\[
V_{B,k}=p_k+(1-p_k)\varepsilon
=\frac{p+(1-p)\varepsilon^{k+1}}{p+(1-p)\varepsilon^k}.
\]

It is strictly increasing because \(0<\varepsilon<1\) and \(p_k\) increases strictly.

**Telescoping upstream law.** The two action values at \(A\) are \(r\) and \(\gamma V_{B,k}\). Writing \(R_k=q_k/(1-q_k)\), the update gives

\[
R_{k+1}=R_k\frac{\gamma V_{B,k}}r.
\]

The product of downstream values telescopes exactly:

\[
\prod_{j=0}^{k-1}V_{B,j}=p+(1-p)\varepsilon^k.
\]

Substitution proves the closed form for \(R_k\) and hence \(q_k=R_k/(1+R_k)\), including \(k=0\).

**Complete shape classification.** Because \(R_k\mapsto R_k/(1+R_k)\) is increasing, the sign of \(q_{k+1}-q_k\) equals the sign of

\[
R_{k+1}-R_k
=\frac{R_0}{r}\left(\frac{\gamma}{r}\right)^k
\left[p(\gamma-r)+(1-p)\varepsilon^k(\gamma\varepsilon-r)\right].
\]

If \(r\le\gamma\varepsilon\), this is positive; if \(r\ge\gamma\), this is negative (strictly, since \(p\in(0,1)\)). In the middle regime \(\gamma\varepsilon<r<\gamma\), it has the sign of \(\tau-\varepsilon^k\). As \(\varepsilon^k\) decreases strictly with \(k\), there can be only one switch from decreasing to increasing. For \(\tau<1\), the first index with \(\varepsilon^k\le\tau\) is precisely \(K=\lceil\log\tau/\log\varepsilon\rceil\). Equality creates the stated two-index plateau, and otherwise the minimizer is unique. If \(\tau\ge1\), no initial decrease occurs. This also proves necessity of every strict inequality in the classification.

**Small-initial-support scaling.** Fix parameters with \(\gamma\varepsilon<r<\gamma\) and \(q\in(0,1)\). Put \(\beta=\gamma/r\in(1,1/\varepsilon)\), \(\eta=\log\beta/\log(1/\varepsilon)\in(0,1)\), and \(C=(\gamma-r)/(r-\gamma\varepsilon)>0\). For small \(p\), \(\tau=Cp/(1-p)<1\). Write \(K=(\log\tau/\log\varepsilon)+\delta\) with \(0\le\delta<1\). Then \(\varepsilon^K=\tau\varepsilon^\delta\) and \(\beta^K=\tau^{-\eta}\beta^\delta\). The exact odds at the minimum are

\[
R_K=\frac{q}{1-q}\,p^{1-\eta}(1-p)^\eta C^{-\eta}\,
\beta^\delta\bigl(1+C\varepsilon^\delta\bigr).
\]

The final two factors remain between strictly positive finite bounds independent of \(p\), proving \(R_K=\Theta(p^{1-\eta})\) and, since this tends to zero, \(q_K=\Theta(p^{1-\eta})\). The formula for \(K\) gives the logarithmic delay. No assertion is made about convergence of the normalized minimum to a single constant; integer rounding produces a bounded log-periodic factor.

**Explicit unbounded-delay family.** For the numerical parameters above, \(\tau=2p/(1-p)=4^{-N}\), so \(K=N\) and \(\varepsilon^K=\tau\) exactly. The upstream odds at \(N\) are \(R_N=3\cdot2^N/(1+2\cdot4^N)\), yielding the exact rational minimum stated above. Since \(1+2\cdot4^N>2\cdot4^N\), its upper bound follows. Moreover, \(r<\gamma\), so \(R_k\to\infty\) and \(q_k\to1\).

**Value monotonicity despite action suppression.** At any iteration, \(V_{A,k}=(1-q_k)r+q_k\gamma V_{B,k}\). Updating \(q_k\) at fixed \(V_{B,k}\) moves weight toward the larger of \(r\) and \(\gamma V_{B,k}\), or leaves it unchanged at equality; therefore it cannot decrease this intermediate value. Subsequently replacing \(V_{B,k}\) by the strictly larger \(V_{B,k+1}\) strictly raises it because \(q_{k+1}>0\). Thus \(V_{A,k+1}>V_{A,k}\) and \(V_{B,k+1}>V_{B,k}\) for all finite \(k\).

## Verification

The analytic proof covers every integer iteration and every real parameter in the stated domains; finite tests are supplementary. The included `checker.py` independently implements the exact Bellman/update recurrence with Python rational arithmetic and compares it against the closed-form expressions at 26,460 parameter/iteration configurations. It additionally verifies 744 steps along the explicit unbounded-delay family, including exact ties, shape inequalities, and trough values. Run `python3 checker.py` using the Python standard library; its expected transcript is in `checker_output.txt`.

## Relationship to prior work

Brun and Sun (2026), arXiv:2610.03642, define the same update in their equation (6), establish monotonicity of value and action-value functions, and prove restricted-optimal convergence and general complexity bounds. Their equation (7) is a product identity; the present contribution is the exact two-stage telescoping solution, the complete optimal-action probability shape classification, and the quantified arbitrarily deep transient. The cited convergence bounds do not directly state or imply monotonicity of each action probability.

Štrupl and coauthors (2021/2022), arXiv:2107.09088, prove convergence of the equivalent reward-weighted-regression update and provide one-state bandit and global-value examples. Their results do not supply the stated transient in a two-stage chain. Russo (2026), arXiv:2601.18175, characterizes one-step success conditioning as a conservative policy-improvement operator; that characterization does not exclude a temporary reduction of an action that is optimal under a different, improved continuation policy. Wang and coauthors (2026), arXiv:2609.36945, document delayed recovery of an optimal action for softmax REINFORCE on bandits with more than two actions, but analyze gradient-based updates rather than exact value-ratio reweighting on a two-stage MDP. The results here do not dispute any value-monotonicity result in those papers.

## Limitations

The conclusion is about exact model-based reweighting in a small acyclic, discounted MDP; it does not establish analogous transients for arbitrary policy-gradient, sampling, or function-approximation methods. The suppression severity uses downstream initial probability \(p\to0\), so it does not give a uniform lower bound at fixed positive initial support. The family has fixed Bellman advantage at the upstream state, but its initial downstream support depends on the desired delay. Earlier equivalent exact constructions under other terminology cannot be completely excluded. No independent validation has been performed.

## References

1. M. Brun and X. A. Sun, *On the Convergence of Success Conditioning for Policy Optimization*, arXiv:2610.03642 (first public version 2026-10-02), https://arxiv.org/abs/2610.03642.
2. M. Štrupl, F. Faccio, D. R. Ashley, R. K. Srivastava, and J. Schmidhuber, *Reward-Weighted Regression Converges to a Global Optimum*, arXiv:2107.09088 (first public version 2021-07-19), https://arxiv.org/abs/2107.09088.
3. D. Russo, *Success Conditioning as Policy Improvement: The Optimization Problem Solved by Imitating Success*, arXiv:2601.18175 (first public version 2026-01-26), https://arxiv.org/abs/2601.18175.
4. Z. Wang, Y. Chen, Y. Li, and B. Ding, *Fine-tuning on self-generated and reward-weighted data: Learning dynamics, Convergence rates, and benefits of off-policyness*, arXiv:2609.36945 (first public version 2026-09-29), https://arxiv.org/abs/2609.36945.
