# Universal strict failure of Bayesian last-success one-step stopping

## Finding

Let \(p\sim\operatorname{Beta}(\alpha,\beta)\), with arbitrary fixed \(\alpha,\beta>0\). Conditional on \(p\), let \(I_1,\ldots,I_N\) be independent \(\operatorname{Bernoulli}(p)\) observations. The single-selection last-success problem rewards stopping on the final occurrence of \(I_j=1\). Define the canonical one-step lookahead (myopic) rule to stop at a success when immediate winning probability is at least that of waiting until the next success and stopping then.

**Theorem.** For every such prior, this myopic rule is **strictly suboptimal at infinitely many arbitrarily large finite horizons**, even though its one-step comparison strictly favors stopping at the relevant reachable state. More precisely, for each positive integer \(m\) define
\[
f_m=\lceil\alpha m-\beta+1\rceil+1,\qquad i_m=f_m+1,\qquad N_m=f_m+m+1.
\]
For all sufficiently large \(m\), \(f_m\ge0\), and the event \(E_m=\{I_1=\cdots=I_{i_m-1}=0,\ I_{i_m}=1\}\) has positive probability. At this first-success state, immediate stopping is strictly favored by one-step lookahead, yet an explicitly defined policy using at most two future successes improves its conditional winning probability by a factor approaching
\[
1+\frac{1}{2(\alpha+1)(\alpha+2)}.
\]
Writing \(V_N^{\mathrm{opt}}\) and \(V_N^{\mathrm{myop}}\) for the unconditional optimal and myopic winning probabilities, respectively, the improvement gives the quantitative bound
\[
\liminf_{m\to\infty}m^{\alpha+1}\bigl(V_{N_m}^{\mathrm{opt}}-V_{N_m}^{\mathrm{myop}}\bigr)
\ge\frac{\alpha\Gamma(\alpha+\beta)}{2\Gamma(\beta)(\alpha+1)^{\alpha+2}(\alpha+2)}>0.
\]
This is a lower bound on the global regret, not an assertion that it is the optimal asymptotic constant.

## Assumptions and scope

The prior parameters are arbitrary real \(\alpha,\beta>0\), fixed independently of \(m\). The decision maker observes the Bernoulli sequence online, may stop only at successes, and wins if and only if the chosen success is the last one through the fixed and known horizon \(N_m\). A strategy that never selects a success loses. Conditional laws are the Beta posterior laws, and all probabilities below integrate over the prior. The myopic rule uses the exact posterior predictive probabilities, not plug-in estimates; it stops on a tie, although the constructed states feature **strict** comparisons and do not depend on tie-breaking.

Use the rising factorial \((x)_r=\prod_{j=0}^{r-1}(x+j)\), with \((x)_0=1\), and \(u_+=\max\{u,0\}\). At \(E_m\), introduce
\[
A=\alpha+1,\qquad b_m=\beta+f_m,\qquad
B_m=b_m+m-1=mA+\delta_m,
\quad \delta_m=\lceil\alpha m-\beta+1\rceil+1-(\alpha m-\beta+1)\in[1,2).
\]
Only sufficiently large \(m\) with \(f_m\ge0\) are required.

## Proof

**1. Strict myopic recommendation to stop.** Bayes' formula gives \(p\mid E_m\sim\operatorname{Beta}(A,b_m)\). There are exactly \(m\) observations remaining. The immediate stopping reward is
\[
g_m=\mathbb E[(1-p)^m\mid E_m]=\frac{(b_m)_m}{(A+b_m)_m}>0.
\]
Let \(P_{m,k}\) be the conditional probability that the first later success occurs \(k\) steps after \(i_m\), for \(1\le k\le m\). Stopping at that first later success has conditional total reward
\[
\sum_{k=1}^{m} P_{m,k}g_{m,k}
 =m\,\mathbb E[p(1-p)^{m-1}\mid E_m]
 =g_m\frac{mA}{B_m},
\]
where \(g_{m,k}\) denotes the chance of no successes after this new success, conditional on its being the next success. Because \(B_m=mA+\delta_m\) with \(\delta_m\ge1\), \(mA/B_m<1\). Thus the myopic rule **strictly stops** on \(E_m\).

**2. A feasible improvement after the first later success.** At the first later success \(j=i_m+k\), the updated posterior is \(\operatorname{Beta}(A+1,b_m+k-1)\), with \(m-k\) trials remaining. The ratio of the reward of waiting until the next success and stopping there to the reward of stopping at \(j\) is
\[
h_{m,k}=\frac{(A+1)(m-k)}{B_m-1}.
\]
Consider this feasible online policy conditional on \(E_m\): reject the current success and wait until the first later success \(j\); if \(h_{m,k}\le1\), stop at \(j\); otherwise reject \(j\) and stop at the next success, if any. This policy consults only the current history and known parameters. Denote its conditional winning probability by \(C_m\).

For **each** \(k=1,\ldots,m\), the exact joint probability of the first later success being at \(i_m+k\) and of no further successes equals
\[
P_{m,k}g_{m,k}
=\mathbb E[p(1-p)^{m-1}\mid E_m]
=\frac{A}{B_m}g_m,
\]
independent of \(k\). Hence
\[
\frac{C_m}{g_m}=\frac{A}{B_m}\sum_{k=1}^{m}\max\{1,h_{m,k}\}.
\]
Subtracting the immediate stopping reward yields the **exact finite-horizon improvement identity**
\[
\boxed{\quad
\frac{C_m-g_m}{g_m}
=-\frac{\delta_m}{B_m}
+\frac{A}{B_m(B_m-1)}
\sum_{k=1}^{m-1}\left(m+1-\delta_m-(A+1)k\right)_+.
\quad}
\]
No optimality theorem beyond Bayes' rule is used in this construction.

**3. Uniform asymptotic conditional advantage.** Since \(1\le\delta_m<2\) and \(A>1\), a Riemann-sum argument gives
\[
\lim_{m\to\infty}\frac{1}{m^2}\sum_{k=1}^{m-1}
\left(m+1-\delta_m-(A+1)k\right)_+
=\int_0^{1/(A+1)}\bigl(1-(A+1)x\bigr)\,dx
=\frac{1}{2(A+1)}.
\]
Also \(B_m/m\to A\) and \((B_m-1)/m\to A\), so
\[
\frac{C_m-g_m}{g_m}\longrightarrow \frac{1}{2A(A+1)}
=\frac{1}{2(\alpha+1)(\alpha+2)}>0.
\]
In particular, \(C_m>g_m\) for every sufficiently large \(m\), despite the strict opposite recommendation of one-step lookahead.

**4. A positive global regret lower bound.** Because \(f_m/m\to\alpha\) and \(b_m/m\to\alpha\), taking logarithms of the rising-factorial expression gives
\[
g_m\to\left(\frac{\alpha}{\alpha+1}\right)^{\alpha+1}>0.
\]
The unconditional probability of \(E_m\) is
\[
q_m=\frac{\mathrm B(\alpha+1,\beta+f_m)}{\mathrm B(\alpha,\beta)}
\sim\frac{\alpha\Gamma(\alpha+\beta)}{\Gamma(\beta)}
(\alpha m)^{-(\alpha+1)},
\]
by the Gamma-function ratio asymptotic. Modify the myopic rule **only on the event \(E_m\)**, where no earlier stopping could have occurred, using the feasible policy above. The unconditional winning probability increases by exactly \(q_m(C_m-g_m)\). Therefore
\[
V_{N_m}^{\mathrm{opt}}-V_{N_m}^{\mathrm{myop}}
\ge q_m(C_m-g_m).
\]
Multiplying by \(m^{\alpha+1}\), taking limits of the right-hand side, and simplifying yields the claimed strictly positive lower bound. Since \(N_m\) increases strictly with \(m\), the exceptional horizons are distinct and unbounded. \(\square\)

## Verification

The accompanying self-contained `verify.py` uses exact rational Beta-posterior arithmetic. For seven explicitly specified rational-prior/horizon instances it independently computes the two-stage policy's reward by summing over the time of the first later success and (if skipped) the next later success; it compares this to the closed-form finite improvement identity and checks the constant joint-mass identity. The program reports all tests passed. These finite tests check algebraic normalization and conditional probabilities; the arbitrary-real-prior and asymptotic results rely on the proof above, not on finite numerics.

The exact formula also provides a reproducible evaluation recipe without any numerical optimization: compute \(f_m\), \(\delta_m\), \(B_m\) and evaluate its \(m-1\) positive-part terms.

## Relationship to prior work

Ano (2026), Section 3.4, equations (69)–(74), establishes the Beta-posterior last-success recursion and the one-step criterion, and supplies individual counterexamples to monotonicity and myopic optimality. Those results and their predictive identities are prior mathematics. The theorem here is the **all-priors, arbitrarily-large-horizon strict failure** with a constructive policy and explicit polynomial-scale global-regret lower bound. It is not the assertion that some finite counterexample exists.

Bruss and Louchard (2009), Section 6, give a general Bayesian dynamic-programming algorithm and a finite-horizon optimal rule; that algorithm can evaluate any particular finite instance, but its displayed theorems do not establish this uniform family or the limiting gain. Paindaveine (2026) treats an unknown fixed Bernoulli parameter with a frequentist plug-in rule and oracle comparisons, rather than the exact Beta-mixture Bayesian one-step rule. Gnedin and Derbazi (2024) study a random number of arrival epochs and a negative-binomial prior for that count, not a fixed horizon with a Beta prior on the common Bernoulli success rate. These differing models do not directly imply the present construction.

## Limitations

The result does not identify the globally optimal strategy or the exact optimal-minus-myopic regret asymptotic; it proves a **strict lower bound** on the latter along an explicit subsequence of horizons. The conditional gain is computed at a particular first-success history, whose unconditional probability decreases with the horizon; no positive asymptotic *global* regret is claimed. The result assumes a proper Beta prior with positive fixed shape parameters, a known deterministic finite horizon, conditionally iid Bernoulli trials, and a single selection. No assertion is made for adaptive horizons, arbitrary priors, or multiple selections. Priority remains subject to independent literature evaluation.

## References

- Katsunori Ano (2026), *Monotone Multiple Stopping and Last-Success Problems*, arXiv:2610.10237v1, first submitted 2026-10-07, especially Section 3.4 and equations (69)–(74). https://arxiv.org/abs/2610.10237
- F. Thomas Bruss and Guy Louchard (2009), *The odds algorithm based on sequential updating and its performance*, *Advances in Applied Probability* **41**, 131–153, doi:10.1239/aap/1240319579, especially Section 6.
- Davy Paindaveine (2026), *Stopping on the last success with unknown odds: Impossibility barriers and quantitative oracle bounds*, arXiv:2604.07183, especially the introduction and the definition of the plug-in rule.
- Alexander Gnedin and Zakaria Derbazi (2024), *The last-success stopping problem with random observation times*, *Mathematical Methods of Operations Research*, doi:10.1007/s00186-024-00880-1, especially Sections 3 and 5.
