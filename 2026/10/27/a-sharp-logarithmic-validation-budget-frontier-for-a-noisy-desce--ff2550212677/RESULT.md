# A sharp logarithmic validation-budget frontier for a noisy descent safeguard

## Finding

An independent mini-batch acceptance test can accept a strictly worse stochastic-gradient proposal at a **global strongly convex minimizer**. For the two-component quadratic model defined below, the probability of irreversible departure has an exact product representation; its transition from almost-sure departure to positive-probability retention occurs at an explicit logarithmic batch-size constant. A second, sharp logarithm-of-logarithm boundary resolves the critical case.

Let
\[
I=D_{\mathrm{KL}}\!\left(\operatorname{Bern}(3/4)\,\|\,\operatorname{Bern}(1/2)\right)
=\tfrac34\log\tfrac32+\tfrac14\log\tfrac12
=0.1308120359411369\ldots.
\]
For the acceptance procedure below, with batches \(B_k=\max\{1,\lfloor c\log(k+2)\rfloor\}\), the event that the method ever leaves its exact minimizer has probability one **if and only if** \(c\le 1/I\). For \(c>1/I\), the minimizer is retained forever with strictly positive probability. The sharp coefficient is \(1/I=7.64455650281279\ldots\).

At the critical scale, put
\[
B_k=\max\left\{1,\left\lfloor\frac{\log(k+3)+a\log\log(k+3)}{I}\right\rfloor\right\}.
\]
Departure is almost sure exactly when \(a\le 1/2\), and there is positive probability of permanent retention exactly when \(a>1/2\). Thus the polynomial prefactor of the validation error, not just its Chernoff exponent, determines the boundary case.

More generally, for **every deterministic sequence** of positive integer batch sizes \((B_k)_{k\ge1}\), the sharp criterion is
\[
\mathbb P\{X_k=0\text{ for all }k\ge0\}>0
\quad\Longleftrightarrow\quad
\sum_{k\ge1}p_{B_k}<\infty,
\qquad
p_B=2^{-B}\sum_{j=\lfloor3B/4\rfloor+1}^{B}\binom Bj.
\]
For every finite \(N\),
\[
\mathbb P(X_N=0)=\prod_{k=1}^N(1-p_{B_k}),\qquad
\mathbb E[F(X_N)-F(0)]=\tfrac12\left[1-\prod_{k=1}^N(1-p_{B_k})\right].
\]
Here leaving zero is irreversible, although the iterates remain bounded. In particular, every **fixed finite batch size** causes almost-sure eventual departure and a permanent objective gap of \(1/2\).

## Assumptions and scope

For \(s\in\{-1,+1\}\), define the component loss
\[
f_s(x)=\tfrac12(x-s)^2,
\quad F(x)=\tfrac12[f_{-1}(x)+f_{+1}(x)]=\tfrac12x^2+\tfrac12.
\]
Every component has second derivative one. The population objective is globally strongly convex with unique minimizer \(x_*=0\).

Set \(X_0=0\). At each integer stage \(k\ge1\), draw an independent training sign \(S_k\) uniformly from \(\{-1,+1\}\), and propose the **unit-step stochastic gradient** candidate
\[
Y_k=X_{k-1}-\nabla f_{S_k}(X_{k-1})=S_k.
\]
Independently draw \(B_k\) validation signs \(V_{k,1},\ldots,V_{k,B_k}\), also independently and uniformly distributed on \(\{-1,+1\}\), with independent draws across stages. Use the **same** validation batch to compare the current point and the candidate; let \(\widehat F_k(x)=B_k^{-1}\sum_{j=1}^{B_k}f_{V_{k,j}}(x)\) and define
\[
X_k=\begin{cases}Y_k,&\widehat F_k(Y_k)<\widehat F_k(X_{k-1}),\\X_{k-1},&\text{otherwise}.\end{cases}
\]
Equality is rejected. The unit step is held fixed by design: this is the **fixed-step independently validated null-step component**, *not* a claim about the full online preconditioner update or convergence theorem of any adaptive algorithm. The noninterpolating data have persistent stochastic-gradient noise at the population optimum.

## Proof

**1. Exact states and departure law.** The initial state is zero; a proposal is always either \(+1\) or \(-1\); and a rejected step preserves the old state. By induction \(X_k\in\{-1,0,+1\}\). Once \(X_k\ne0\), subsequent states belong to \(\{-1,+1\}\). Moreover, \(F(\pm1)-F(0)=1/2\).

At zero, let \(J_k=\#\{j:V_{k,j}=S_k\}\). Conditionally on every training sign, \(J_k\sim\operatorname{Bin}(B_k,1/2)\). For each validation loss, \(f_{V}(0)=1/2\), whereas \(f_{V}(S)=0\) if \(V=S\), and \(f_{V}(S)=2\) otherwise. Consequently
\[
\widehat F_k(S_k)<\widehat F_k(0)
\ \Longleftrightarrow\ 2(B_k-J_k)/B_k<1/2
\ \Longleftrightarrow\ J_k>3B_k/4.
\]
Thus the conditional probability of departing zero at stage \(k\), given still at zero, is precisely \(p_{B_k}\). Conditional independence of new training and validation batches gives the product identity for finite-time survival. The stated expected gap follows because every other state has gap \(1/2\). Since \(0<p_B\le 1/2\) for every positive integer \(B\), the elementary infinite-product criterion \(\prod_{k\ge1}(1-p_{B_k})>0\iff\sum_{k\ge1}p_{B_k}<\infty\) follows, for example, from \(-2p\le\log(1-p)\le-p\) when \(0\le p\le1/2\).

**2. Sharp binomial-tail envelope.** Put \(m_B=\lfloor3B/4\rfloor+1\), and \(a_{B,j}=2^{-B}\binom Bj\). At the first accepted count \(m_B\), successive summands satisfy
\[
\frac{a_{B,j+1}}{a_{B,j}}=\frac{B-j}{j+1}<\frac13
\quad\text{for }j\ge m_B.
\]
It follows that
\[
a_{B,m_B}\le p_B\le\tfrac32a_{B,m_B}.
\]
Write \(m_B=(3/4)B+\theta_B\) with \(0<\theta_B\le1\). Stirling's inequalities, applied uniformly to \(m_B\) and \(B-m_B\) for all sufficiently large \(B\), yield constants \(0<C_-<C_+<\infty\), independent of \(B\), such that
\[
C_-B^{-1/2}e^{-IB}\le p_B\le C_+B^{-1/2}e^{-IB}.
\]
Indeed the Stirling exponent is \(B D(m_B/B\,\|\,1/2)=BI+\theta_B\log 3+O(1/B)\) uniformly in \(\theta_B\); the factor \(\exp(-\theta_B\log3)\) remains bounded between positive constants. This also proves why dropping the \(B^{-1/2}\) factor gives the wrong critical correction.

**3. The logarithmic and logarithm-of-logarithm borders.** For \(B_k=\max\{1,\lfloor c\log(k+2)\rfloor\}\), \(B_k=c\log k+O(1)\) as \(k\to\infty\). The two-sided tail estimate therefore gives
\[
p_{B_k}\asymp\frac{k^{-cI}}{\sqrt{\log k}}.
\]
Integral comparison shows that the series diverges if \(cI<1\), converges if \(cI>1\), and **diverges at equality** since \(\sum[k\sqrt{\log k}]^{-1}=\infty\). Combined with Step 1, this proves the first exact boundary.

For the second schedule, \(B_k=[\log k+a\log\log k]/I+O(1)\) and hence
\[
p_{B_k}\asymp\frac{1}{k(\log k)^{a+1/2}}.
\]
Its series diverges precisely when \(a+1/2\le1\), proving the sharp \(a=1/2\) boundary.

**4. Behavior after departure.** At \(+1\), a proposal \(-1\) occurs with probability \(1/2\). It is accepted only if more than half of the fresh validation signs equal \(-1\). Therefore the probability of flipping either endpoint to the other at batch size \(B\) is
\[
q_B=\tfrac12\cdot2^{-B}\sum_{j=\lfloor B/2\rfloor+1}^{B}\binom Bj,
\quad0<q_B<1.
\]
The endpoint chain is symmetric. For fixed \(B\), its unique invariant distribution gives probability \(1/2\) to each endpoint, and its total-variation convergence rate after departure is \(|1-2q_B|^n\). This reinforces that the process is bounded but never recovers the optimal objective value.

**5. High-confidence schedule consequence.** The two-sided envelope also gives a quantitative positive-retention construction. Fix \(c>1/I\), and set \(B_k=\lceil c\log(k+2)+d\rceil\) with \(d\ge0\). By the union bound and the upper envelope, for a finite constant \(C_c\),
\[
\mathbb P\{\exists k:X_k\ne0\}\le\sum_{k\ge1}p_{B_k}\le C_c e^{-Id}.
\]
Thus an additive validation-budget offset controls the probability of *ever* accepting a worse step, while the preceding sharp lower bound establishes the limits of its asymptotic slope. This does not guarantee retention with probability one for any finite schedule.

## Verification

The included standalone `verify.py` enumerates **every training sign and every validation sign vector** for each integer batch size from \(1\) through \(11\); it compares the resulting exact rational transition probabilities at all three states with the two binomial formulas, covering **24,564 complete training/validation cases**. Four independent finite schedule families verify the exact transient mass and expected objective gap using rational arithmetic. A separate finite-\(B\) numerical check tests consistency with the \(B^{-1/2}e^{-IB}\) scale. `verification_output.json` records the program's actual output; run `python verify.py` using Python's standard library. Finite exhaustive cases do not prove either infinite-horizon boundary, which follows from the preceding proof.

## Relationship to prior work

Zhang, Gao, Ye and Udell (2026), Algorithm 2, defines independently sampled objective feedback and a null-step choice for its hypergradient specialization; Section 3 and Theorem 3.3 obtain finite-horizon guarantees under **relative gradient and function-value noise hypotheses**. Here only its *fixed-step validation comparison* is investigated. At \(x_*=0\), the component gradient equals \(\pm1\) while the true gradient vanishes, so the gradient-norm relative-noise assumption fails. Over a full neighborhood of zero, relative function-value noise cannot be bounded uniformly because the component deviation is linear in distance while the population optimality gap is quadratic. On this particular discrete trajectory, however, the source function-value condition alone may hold with sufficiently large parameters; **failure of the gradient-noise condition is sufficient** to exclude application of the convergence theorem. Accordingly, the construction **does not contradict or modify** that theorem.

Probabilistic stochastic line searches and adaptive-batching line searches are studied by Mahsereci and Hennig (2015), Krejić and Krklec Jerinkić (2011/2013), and Bollapragada, Byrd and Nocedal (2017). Those formulations use different sampling/acceptance rules or supply general convergence guarantees. In the inspected relevant material, none establishes the exact all-time event law or the \(1/I\) and \(a=1/2\) cutoffs for this specified independent validation safeguard. The proof uses classical binomial tail asymptotics and the elementary infinite-product criterion; those standard tools are not new.

## Limitations

This is a **model-specific, noninterpolating, fixed-unit-step** result, not a theorem about a full adaptive stochastic optimizer, arbitrary step sizes, other training distributions, or arbitrary line searches. A nonzero initial point has a different state law. Strict tie rejection matters for finite-batch formulas. The critical constants are specific to the two shifted losses, equal sign probabilities, and the choice of unit gradient step. Permanent departure means the objective gap persists, not that the iterate becomes unbounded. The theorem addresses mathematical behavior, not empirical efficiency on real datasets. It is not an independent validation of novelty; related older literature under alternative terminology might contain an equivalent special case.

## References

1. W. Zhang, W. Gao, Y. Ye, M. Udell, *Stochastic Gradient Methods with Online Scaling*, Optimization Online, first public posting 2026-05-28, https://optimization-online.org/2026/05/stochastic-gradient-methods-with-online-scaling/ ; full primary text https://optimization-online.org/wp-content/uploads/2026/05/Stochastic_OSGM-4.pdf . Relevant: Algorithm 2, Section 3.1--3.2 and Theorem 3.3.
2. M. Mahsereci and P. Hennig, *Probabilistic Line Searches for Stochastic Optimization*, NeurIPS 2015, https://papers.neurips.cc/paper_files/paper/2015/file/812b4ba287f5ee0bc9d43bbf5bbe87fb-Paper.pdf .
3. N. Krejić and N. Krklec Jerinkić, *Line search methods with variable sample size for unconstrained optimization*, Optimization Online, original public posting 2011-07-07, https://optimization-online.org/2011/07/3091/ .
4. R. Bollapragada, R. Byrd and J. Nocedal, *Adaptive Sampling Strategies for Stochastic Optimization*, arXiv:1710.11258, 2017, https://arxiv.org/abs/1710.11258 .
