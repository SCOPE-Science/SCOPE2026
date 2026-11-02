# A sharp stochastic-order boundary for the first two projective-plane coupon mechanisms

## Finding

Consider independent draws of blocks until all points have appeared. For a prime power \(q\), let \(T_{\mathrm{PG},q}\) be the number of draws required when each draw is a uniformly selected line of \(\operatorname{PG}(2,q)\), and let \(T_{\mathrm{full},q}\) be the corresponding coverage time when each draw is a uniformly selected \((q+1)\)-subset of its \(q^2+q+1\) points. The draws are with replacement and independent.

For the Fano plane, \(q=2\), there is **strict first-order stochastic domination**: for every integer \(t\ge 1\),

\[
\Pr(T_{\mathrm{PG},2}>t)-\Pr(T_{\mathrm{full},2}>t)
=\frac{7}{35^t}\bigl(3\cdot5^t-5\cdot4^t+5\bigr).
\]

The difference vanishes for \(t=1,2\) and is strictly positive for every integer \(t\ge3\). The survival functions also agree at \(t=0\). Thus \(T_{\mathrm{PG},2}\) stochastically dominates \(T_{\mathrm{full},2}\), and the inequality is strict at every nontrivial tail.

**This ordering already fails at the next projective-plane order.** For \(q=3\), define
\[
\Delta_t=\Pr(T_{\mathrm{PG},3}>t)-\Pr(T_{\mathrm{full},3}>t).
\]

Then \(\Delta_t=0\) for \(t=0,1,2,3\), whereas

\[
\Delta_4=-\frac{15480}{2924207}<0,
\quad \Delta_5=\frac{2178216}{418161601}>0,
\]

and **\(\Delta_t>0\) for every integer \(t\ge5\)**. Hence the two coverage times for the thirteen-point projective plane are not comparable under first-order stochastic order, despite the projective-plane mechanism having the larger expectation. This is a complete sign classification of the discrete survival-function difference for the first two projective-plane orders, not a claim about larger orders.

## Assumptions and scope

A projective plane of order \(q\in\{2,3\}\) has \(n=q^2+q+1\) points and the same number of lines, each incident with exactly \(q+1\) points. Every two distinct points lie on exactly one common line. For the full mechanism, the allowable blocks are all \(\binom{n}{q+1}\) subsets of size \(q+1\). Both processes begin with no points covered. The stopping time is the positive integer index of the first full-coverage draw. All comparisons below are at integer draw counts.

Write \(L_q\) for the set of projective lines. For any nonempty point set \(S\), let \(a_q(S)\) be the number of lines disjoint from \(S\), and define signed avoidance coefficients

\[
 c_q(r)=\sum_{\varnothing\ne S\subseteq V:\,a_q(S)=r}(-1)^{|S|+1}.
\]

All probabilities and coefficient computations use exact rational and integer arithmetic.

## Proof

**1. Exact survival identity.** Inclusion–exclusion over the event that a given point has never appeared gives, for every integer \(t\ge1\),

\[
 \Pr(T_{\mathrm{PG},q}>t)=\sum_{r=0}^{n}c_q(r)\left(\frac{r}{n}\right)^t.
\]

For the full mechanism, if \(s\) specified points have not appeared, there are \(\binom{n-s}{q+1}\) eligible blocks avoiding them out of \(N_q=\binom{n}{q+1}\). Consequently,

\[
 \Pr(T_{\mathrm{full},q}>t)
 =\sum_{s=1}^{n}(-1)^{s+1}\binom ns
 \left(\frac{\binom{n-s}{q+1}}{\binom n{q+1}}\right)^t,
\]

where a binomial coefficient is zero if its upper argument is smaller than the lower one.

**2. Exact finite geometric certificate.** Represent projective points by the unique normalized nonzero vectors of \(\mathbb F_q^3\), whose first nonzero coordinate is one. Each normalized dual vector \(a\) specifies the line of normalized points \(v\) satisfying \(a\cdot v=0\) over \(\mathbb F_q\). Enumerating the \(2^n-1\) nonempty subsets \(S\) and accumulating \((-1)^{|S|+1}\) by \(a_q(S)\) produces the following exact coefficient tables. This is a finite, exhaustive algorithm; its complete standard-library implementation is provided in `verify.py`, along with separate time-step recurrences checking the resulting probabilities.

| Avoidance count \(r\) | \(c_2(r)\) |
|---:|---:|
| 0 | -6 |
| 1 | 21 |
| 2 | -21 |
| 4 | 7 |

| Avoidance count \(r\) | \(c_3(r)\) |
|---:|---:|
| 0 | -38 |
| 1 | 130 |
| 2 | -78 |
| 3 | -182 |
| 4 | 234 |
| 6 | -78 |
| 9 | 13 |

The geometry construction itself is elementary and is checked independently: there are respectively seven and thirteen normalized points and lines, every line has the advertised size, and every pair of points lies on exactly one line. All coefficients are obtained from complete subset enumeration, not from a truncated simulation.

**3. Fano stochastic order.** Substituting the first table into the survival identity, and using the full-model formula for \(n=7\), \(q+1=3\), yields

\[
\begin{aligned}
\Pr(T_{\mathrm{PG},2}>t)&=7(4/7)^t-21(2/7)^t+21(1/7)^t,\\
\Pr(T_{\mathrm{full},2}>t)&=7(4/7)^t-21(2/7)^t+35(4/35)^t-35(1/35)^t.
\end{aligned}
\]

Thus the stated difference formula follows. Let \(b_t=3\cdot5^t-5\cdot4^t+5\). Then \(b_1=b_2=0\) and

\[
 b_{t+1}-5b_t=5(4^t-4)>0\quad(t\ge2),
\]

which implies \(b_t>0\) for all integers \(t\ge3\). (Equivalently, after division by \(5^t\), the bracket is increasing for \(t\ge2\).)

**4. Ternary plane: exact single crossing.** In the \(q=3\) case the first two nonzero avoidance bases coincide between the two models and cancel in the difference. Using denominator \(715=\binom{13}{4}\), the remaining exact numerator is

\[
\begin{aligned}
715^t\Delta_t={}&234\cdot220^t-286\cdot210^t-182\cdot165^t
+715\cdot126^t-78\cdot110^t\\
&-1287\cdot70^t+130\cdot55^t+1716\cdot35^t
-1716\cdot15^t+1287\cdot5^t-715.
\end{aligned}
\]

This identity holds for every integer \(t\ge1\); the vanishing for \(t=0,1,2,3\) is checked directly from coverage geometry and the exact formulas. Exact substitution gives the displayed rational values at \(t=4,5\), and

\[
\Delta_6=\frac{10152590256}{1494927723575}>0.
\]

For \(t\ge7\), discard all positive terms other than \(234\cdot220^t\), divide by \(220^t\), and obtain

\[
\frac{715^t\Delta_t}{220^t}\ge B(t),
\]

where

\[
\begin{aligned}
B(t)={}&234-286(21/22)^t-182(3/4)^t-78(1/2)^t\\
&-1287(7/22)^t-1716(3/44)^t-715(1/220)^t.
\end{aligned}
\]

Each ratio is strictly between zero and one, so \(B(t)\) increases with \(t\). The exact computation

\[
 B(7)=\frac{980071992656237}{453519616000000}>0
\]

therefore proves \(\Delta_t>0\) for all integers \(t\ge7\). Together with the exact cases \(t=5,6\) and the negative case \(t=4\), this establishes the complete sign classification.

## Verification

Running `python3 verify.py` under a standard Python 3 interpreter reproduces the signed geometric coefficient tables, line-incidence checks, exact fractions at the crossing, and the monotone positive lower envelope. It also independently computes finite-time full-coverage probabilities by a dynamic recurrence over subsets of already-covered points rather than relying on inclusion–exclusion. The included `verification_output.txt` records **250 passed exact assertions**. The analytical all-time positivity relies on the displayed monotone bound, not on the finite numerical test horizon.

As a further consistency test, summing the exact survival series reproduces the published four means: \(163/30\) and \(85691/15810\) for the seven-point comparison, and \(43633/4620\) and \(1746879067753/185252315340\) for the thirteen-point comparison.

## Relationship to prior work

Barak-Pelleg and Berend establish that projective-plane mechanisms for \(q=2,3,4\) have larger **expected** coverage time than the corresponding uniform full model; their Fano proof follows a small Markov chain and the larger cases use exact recovery-set counts. The present result compares **every survival probability** for the first two orders, not just their sums. The distinction is substantive: the order-two plane has stochastic domination, while the order-three plane has a strict sign reversal between draw counts four and five even though its mean is larger.

Grunbaum and Yaakobi developed recovery-set identities and formulated a conjecture about expected coverage-time extremality. Berend and Sher studied the different problem of minimizing expected collection time over group-drawing laws. Neither of these investigated statements implies this pointwise distributional classification. The elementary inclusion–exclusion mechanism is classical and is not itself claimed as new.

## Limitations

The theorem classifies only \(q=2\) and \(q=3\), and makes no assertion about stochastic comparisons for \(q\ge4\) or for arbitrary fair hypergraphs. It does not assert an explicit sample-path monotone coupling, finite-sample estimation rate, or statistical confidence interval. The novelty assessment is based on accessible primary sources and targeted mathematical-record searches; broader unindexed prior work could contain equivalent calculations.

## References

- D. Barak-Pelleg and D. Berend, *Fano Geometry and Slow Coupon Collecting*, arXiv:2606.28216v1, first posted 2026-06-26. https://arxiv.org/abs/2606.28216
- Y. Grunbaum and E. Yaakobi, *General Coverage Models: Structure, Monotonicity, and Shotgun Sequencing*, arXiv:2510.25305, first posted 2025-10-29. https://arxiv.org/abs/2510.25305
- D. Berend and T. Sher, *On a Conjecture on Uniform Group Drawings in the Coupon Collector Problem*, arXiv:2509.17201, first posted 2025-09-21. https://arxiv.org/abs/2509.17201
