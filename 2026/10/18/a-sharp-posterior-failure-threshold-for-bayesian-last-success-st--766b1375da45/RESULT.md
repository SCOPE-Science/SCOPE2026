# A sharp posterior-failure threshold for Bayesian last-success stopping

## Finding

Consider a sequence of exchangeable Bernoulli observations which, conditionally on an unknown success probability \(p\), are independent with law \(\operatorname{Bernoulli}(p)\). At an observed success, suppose the posterior distribution of \(p\) is \(\operatorname{Beta}(A,B)\), with arbitrary real \(A,B>0\). Exactly \(k\geq1\) further observations remain. The decision maker has one selection right and wins precisely when the selected success is the final success, including the current one. Decisions must be adapted to the observations; selecting a failure never helps.

Write \(Q_k(A,B)=\Pr(\text{all remaining observations are failures}\mid A,B)\), and let \(H_k(A,B)\) be the optimal conditional probability of winning if the current success is rejected and the next \(k\) observations are played optimally. Then the following sharp phase description holds.

**Theorem.** For every \(k\geq1\) and \(B>0\), there is a unique \(A_c(B,k)>0\) such that accepting the current success is optimal exactly for \(0<A\leq A_c(B,k)\) (with acceptance and rejection tied at equality). The function \(B\mapsto A_c(B,k)\) is strictly increasing. Moreover,

\[
 A_c(B,k)=\frac{B+k-1}{k}
 \quad\Longleftrightarrow\quad
 \bigl(k=1\ \text{or}\ B\geq k(k-1)+1\bigr).
\]

For \(k\geq2\) and \(0<B<k(k-1)+1\), the inequality is strict:

\[
 0<A_c(B,k)<\frac{B+k-1}{k}.
\]

The large-\(B\) region is algorithmically explicit: if \(B\geq k(k-1)+1\) and \(A\leq(B+k-1)/k\), it is optimal to accept the current success; if the current success is rejected, the policy *accept the first subsequent success, if any* is optimal. In the opposite direction, \(A>(B+k-1)/k\) always makes rejection strictly preferable, for every \(B>0\).

For exactly two future observations the entire phase boundary is elementary:

\[
 A_c(B,2)=\min\!\left\{
 \frac{\sqrt{(B+1)(5B+1)}-(B+1)}{2},\ \frac{B+1}{2}
 \right\}.
\]

Its two branches meet sharply at \(B=3\). This shows explicitly how Bayesian learning can defeat the one-step odds comparison below the critical posterior-failure shape.

## Assumptions and scope

The posterior at the currently observed success, not necessarily the original prior, is \(\operatorname{Beta}(A,B)\). The parameter \(p\) is constant within the remaining experiment. Conditional on \(p\), every remaining Bernoulli outcome is independent of previous outcomes. The number \(k\) of remaining trials is deterministic, finite and known. Only one success may be selected, no recall is allowed, and a loss occurs when there is no selected final success. The theorem is a conditional statewise result; no claim is made that one fixed calendar-time threshold works along all posterior paths.

Use the rising factorial \((z)_j=z(z+1)\cdots(z+j-1)\), with \((z)_0=1\). The beta-binomial predictive law gives

\[
 Q_k(A,B)=\frac{(B)_k}{(A+B)_k}.
\]

When the current success is rejected, optimality is characterized by

\[
 H_0(A,B)=0,\qquad
 H_k(A,B)=\frac{A}{A+B}\max\{Q_{k-1}(A+1,B),H_{k-1}(A+1,B)\}
 +\frac{B}{A+B}H_{k-1}(A,B+1).
\]

This recurrence is used for finite checks, but the sharp all-horizon threshold requires the structural argument below.

## Proof

### 1. A unique, strictly monotone posterior acceptance boundary

Fix \(k\geq1\), \(B>0\), and any deterministic observation-adapted future selection rule \(\pi\). The set \(W_\pi\subseteq\{0,1\}^k\) of future binary words on which \(\pi\) selects their last success is finite. Every such word has \(r\geq1\) successes. Its beta-binomial predictive probability is

\[
 \Pr(w\mid A,B)=\frac{(A)_r(B)_{k-r}}{(A+B)_k}.
\]

Dividing the rule's winning probability by the probability of accepting the current success yields the exact nonnegative sum

\[
 R_\pi(A,B,k)
 =\frac{\Pr(\pi\text{ wins}\mid A,B)}{Q_k(A,B)}
 =\sum_{w\in W_\pi}\frac{(A)_{r(w)}}{(B+k-r(w))_{r(w)}}.
\]

Each nonzero summand is strictly increasing and continuous in \(A>0\) and strictly decreasing and continuous in \(B>0\). There are finitely many deterministic rules (randomized rules cannot improve the maximum), hence

\[
 R(A,B,k)=\frac{H_k(A,B)}{Q_k(A,B)}=\max_\pi R_\pi(A,B,k)
\]

is continuous and strictly increasing in \(A>0\), strictly decreasing in \(B>0\). Strictness holds because the maximizing rule always has a nonempty winning set: selecting the final trial on a success already has positive winning probability. For fixed \(B,k\), \(R(A,B,k)\to0\) as \(A\downarrow0\), while \(R(A,B,k)\to\infty\) as \(A\to\infty\), since the rule selecting a success at the last trial has among its winning paths the all-success word with ratio \((A)_k/(B)_k\). The intermediate value theorem therefore gives one and only one positive root of \(R=1\), named \(A_c(B,k)\). Strict decrease in \(B\) shows this root is strictly increasing as a function of \(B\). Accepting the current success is optimal exactly when \(R\leq1\).

### 2. An unconditional upper bound for the acceptance boundary

If the current success is rejected, a legal strategy is to select the first success among the remaining \(k\) observations. It wins exactly when there is one success in the remaining sample, so its probability is

\[
 P_{\mathrm{first}}(A,B,k)
 =k\,\mathbb E[p(1-p)^{k-1}\mid A,B]
 =\frac{kA(B)_{k-1}}{(A+B)_k}.
\]

Consequently,

\[
 R(A,B,k)\geq\frac{P_{\mathrm{first}}(A,B,k)}{Q_k(A,B)}
 =\frac{kA}{B+k-1}.
\]

Therefore \(A_c(B,k)\leq(B+k-1)/k\), and above this line rejection is strictly better for every \(B>0\).

### 3. An exact region where the first-future-success policy is optimal

Put \(C_k=k(k-1)+1\). We prove simultaneously by induction on \(k\) that whenever

\[
 B\geq C_k,\qquad kA\leq B+k-1,
\]

(a) accepting an available current success is optimal, and (b) from before the next \(k\) trials, selecting the first success is an optimal future-only rule.

At \(k=1\), the future-only rule is forced; the acceptance comparison is \(B/(A+B)\geq A/(A+B)\), exactly \(A\leq B\).

Assume both assertions for \(k-1\) and let \(k\geq2\). If the first of the future \(k\) observations is a success, the updated posterior is \(\operatorname{Beta}(A+1,B)\). The assumptions imply

\[
 B\geq C_{k-1},\qquad
 (k-1)(A+1)\leq B+k-2,
\]

where the latter inequality follows by inserting \(kA\leq B+k-1\) and \(B\geq k(k-1)+1\). Thus, by induction, stopping at that success is optimal. If the first future observation is a failure, the updated posterior is \(\operatorname{Beta}(A,B+1)\), and

\[
 B+1\geq C_{k-1},\qquad
 (k-1)A\leq B+k-1=(B+1)+(k-1)-1.
\]

The induction hypothesis makes the first-success rule optimal for the remaining \(k-1\) observations. Conditioning on the first observation proves (b) at level \(k\). Its success probability is \(P_{\mathrm{first}}\), and \(P_{\mathrm{first}}\leq Q_k\) by the assumed odds inequality; hence stopping now is optimal, proving (a).

In particular, on \(B\geq C_k\), accepting now is optimal up to the upper-bound line \(kA=B+k-1\), and step 2 shows it is strictly inferior above that line. Thus \(A_c(B,k)=(B+k-1)/k\) throughout this region.

### 4. Sharp failure of the simple odds bound below the quadratic boundary

Let \(k\geq2\), \(B<C_k\), and choose \(A_0=(B+k-1)/k\). At \(A=A_0\), the strategy selecting the first future success wins with probability exactly \(Q_k\). Modify that strategy only on the strictly positive-probability event that the *very next* observation is a success: rather than selecting that success, defer and select the first success in the remaining \(k-1\) observations. The posterior immediately after this next success is \(\operatorname{Beta}(A_0+1,B)\). There, deferring beats stopping precisely when

\[
 (k-1)(A_0+1)>B+k-2
 \quad\Longleftrightarrow\quad B<k(k-1)+1.
\]

Thus the modified valid future strategy has strictly greater expected winning probability than \(Q_k\), proving \(R(A_0,B,k)>1\). By the unique-crossing result of step 1, \(A_c(B,k)<A_0\). This also proves the necessity and sharpness of the stated quadratic boundary; no exceptional positive \(B\) below it attains the naive odds line.

### 5. Closed form with two future trials

For \(k=2\), a future-only rule need only decide whether to select the first trial when it succeeds or postpone selection to the final trial. These choices produce the respective unconditional predictive win probabilities

\[
 \frac{2AB}{(A+B)(A+B+1)}
 \quad\text{and}\quad
 \frac{A}{A+B}.
\]

Their maximum equals \(H_2(A,B)\), while \(Q_2(A,B)=B(B+1)/[(A+B)(A+B+1)]\). Acceptance therefore holds precisely when both

\[
 2AB\leq B(B+1),\qquad A(A+B+1)\leq B(B+1)
\]

hold. Solving these inequalities gives the displayed minimum of two explicit roots. The roots coincide only at \(B=3\), with lower-\(B\) values governed by the square-root branch and higher-\(B\) values by the linear branch. For example, at \((k,B,A)=(2,2,3/2)\), the naive first-future strategy and immediate acceptance both win with probability \(8/21\), but selecting only on a success at the final trial wins with probability \(3/7\); this is a strict counterexample below the sharp \(B=3\) boundary.

## Verification

The companion standalone program `verify_bayes_last_success.py` is executable with Python 3.10+ without dependencies. It uses exact rational arithmetic and checks the Bellman recurrence and the quadratic critical line for \(1\leq k\leq7\) across integer and rational parameter grids; it independently enumerates every deterministic success-only stopping policy for horizons up to four trials. The supplied run passed 1181 exact finite assertions. These checks support the algebra and boundary cases but do not replace the finite-horizon all-parameter proof in Sections 1–5.

## Relationship to prior work

Ano's October 2026 treatment develops the recursive Bayesian last-success Bellman algorithm with a Beta prior and emphasizes that posterior updating generally invalidates the pathwise monotonicity assumption behind a one-step-lookahead argument. The present finding identifies a **sharp, explicitly parameterized posterior-state region** in which the first-subsequent-success policy is nevertheless globally optimal, and proves the quadratic boundary beyond which adaptive postponement strictly improves that rule at its nominal odds equality. The distinction is between a computable recurrence for individual states and a closed uniform all-horizon structural phase theorem.

Bruss' odds theorem treats independent trials with *known* success probabilities; it yields the first-success comparison under fixed odds but not the adaptive posterior region or its critical failure-shape. Paindaveine's 2026 unknown-odds work studies unknown fixed parameters and frequentist oracle-free guarantees, not this exact Beta-posterior decision phase. Gnedin and Derbazi's last-success treatment addresses random observation times and a different success-probability specification. Generic Bayesian dynamic programming implies computability of individual finite cases but does not directly furnish the strict universal quadratic boundary.

## Limitations

The result concerns one selection right and a known fixed remaining horizon under a Beta posterior. It does not assert monotonicity along realized paths, optimality for multiple selections, a universal calendar-time cutoff, or results under non-Beta mixing laws. The simple odds boundary is exact only in the stated high-\(B\) region; for lower \(B\), the unique threshold is not given in general by a closed elementary expression, except for \(k=2\). Finite verification does not constitute an infinite-parameter certificate. Possible earlier equivalent formulations in Bayesian secretary/last-success theory remain a literature risk.

## References

1. Katsunori Ano, *Monotone Multiple Stopping and Last-Success Problems*, arXiv:2610.10237v1, first public October 7, 2026; in particular Section 3.4 (Bayesian last-success problem).
2. F. T. Bruss, *Sum the odds to one and stop*, Annals of Probability 28 (2000), 1384–1391, DOI:10.1214/aop/1019160340.
3. Davy Paindaveine, *Stopping on the last success with unknown odds: Impossibility barriers and quantitative oracle bounds*, arXiv:2604.07183v1, first public April 8, 2026.
4. Alexander Gnedin and Zakaria Derbazi, *The Last-Success Stopping Problem with Random Observation Times*, arXiv:2207.05156 (2022).
