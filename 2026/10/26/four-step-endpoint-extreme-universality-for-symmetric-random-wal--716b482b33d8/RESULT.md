# Four-step endpoint-extreme universality for symmetric random walks

## Finding

Let \(X_1,X_2,X_3,X_4\) be independent, identically distributed real random variables with a common **non-atomic** law symmetric about zero. Put \(S_0=0\), \(S_k=\sum_{i=1}^k X_i\), and let \(t_{\max}\) and \(t_{\min}\) denote the unique maximizer and minimizer of \((S_0,\ldots,S_4)\). Then
\[
\Pr(t_{\max}=0,\ t_{\min}=4)=\Pr(t_{\min}-t_{\max}=4)=\frac18.
\]

There is also a conditional classification revealing how this distribution-free probability arises. Conditional on the **sorted absolute increment magnitudes** \(0<u<v<w<z\), the signs and order are uniformly distributed over \(2^4 4!=384\) signed orders. If \(w<u+v\), exactly \(24\) orders have all four jumps negative and exactly \(24\) have precisely one positive jump, giving \(48\) favorable orders. If \(w>u+v\), the corresponding counts are \(24\), \(20\), and \(4\) for zero, one, and two positive jumps, again totaling \(48\). The equality \(w=u+v\) has probability zero under the hypotheses.

This is a finite-horizon statement for four steps, not a proof of the corresponding assertion at arbitrary horizons.

## Assumptions and scope

The common increment law may be singular or heavy-tailed. Non-atomicity and symmetry suffice; no density, moment, or variance hypothesis is imposed. Non-atomic independent increments imply almost surely that all five partial sums are distinct, since each nonempty interval sum is non-atomic. Also, the four absolute magnitudes are distinct and \(w\ne u+v\) almost surely.

Write a sign word from left to right in temporal order, and regard magnitudes in each order as a permutation of \(u,v,w,z\). Strict inequalities matter, but exceptional ties are null events.

## Proof

**1. Signed-order reduction.** Symmetry gives an independent fair sign for each increment, independent of its absolute magnitude. Conditional on their increasing order statistics, all \(4!\) assignments of magnitudes to the time positions are equally likely. Therefore every signed order has conditional probability \(1/384\). If the global maximum is at time zero and the global minimum is at time four, the first and fourth increments must both be negative. Thus only the four sign words `----`, `-+--`, `--+-`, and `-++-` are possible.

**2. No internal positive jump.** Every permutation of \(u,v,w,z\) under the word `----` strictly decreases the path. It supplies \(24\) favorable signed orders.

**3. One internal positive jump.** Under `-+--`, write the ordered positive magnitudes as \((a,b,c,d)\). The five partial sums are \(0,-a,-a+b,-a+b-c,-a+b-c-d\). Their maximum is attained first and their minimum last exactly when
\[
 b<a\quad\text{and}\quad b<c+d.
\]
For \(b=u\), there are three choices of \(a\) and two orders for \((c,d)\), contributing \(6\). For \(b=v\), \(a\) can be either \(w\) or \(z\), with two orders for the remaining magnitudes, contributing \(4\). For \(b=w\), only \(a=z\) is possible, and the two remaining magnitudes are \(u,v\), contributing \(2\) exactly when \(w<u+v\). The largest magnitude \(b=z\) contributes nothing. Hence the count is
\[
 10+2\mathbf1_{\{w<u+v\}}.
\]
Reverse the temporal order of the increments: if the original partial sums are \(S_k\), the reversed-increment partial sums are \(S_4-S_{4-k}\), so a path with its maximum first and minimum last retains this property. This bijects `-+--` with `--+-`. Equivalently, direct partial-sum inequalities for `--+-` require its positive third magnitude to be smaller than both the fourth magnitude and the sum of the first two magnitudes. Both arguments produce the same count \(10+2\mathbf1_{\{w<u+v\}}\).

**4. Two internal positive jumps.** Under `-++-`, write the magnitudes as \((a,b,c,d)\). The path has its maximum first and minimum last exactly when
\[
 a>b+c\quad\text{and}\quad d>b+c.
\]
Both negative endpoints must therefore use the two largest magnitudes, \(w,z\), and the positive internal jumps must use \(u,v\). Such an assignment exists exactly when \(w>u+v\), in which case there are \(2!\cdot2!=4\) choices.

**5. Cancellation.** Put \(I=\mathbf1_{\{w<u+v\}}\). Since the equality case is null, the total number of favorable signed orders is
\[
 24+2(10+2I)+4(1-I)=48.
\]
It follows that the desired conditional probability is \(48/384=1/8\), regardless of the ordered magnitudes. Averaging over those magnitudes completes the proof.

## Verification

The accompanying `verify.py` independently enumerates all \(384\) signed orders using exact rational arithmetic for each of eight generic magnitude configurations, on both sides of \(w=u+v\). It checks the individual sign-pattern counts against the analytic formulas, verifies the total \(48\), and reports \(48\) exact-rational assertions. Run `python3 verify.py` in the directory containing these files. The enumeration is a check of the four-step proof, not a computational substitute for the universal argument.

## Relationship to prior work

Mori, Majumdar and Schehr's 2019 study established the time-between-extrema observable and an asymptotic boundary density for symmetric random walks. Their longer 2020 analysis established \(\Pr(t_{\min}-t_{\max}=n)=1/(2n)\) for double-exponential increments and for arbitrary symmetric continuous increments only at horizons \(n\le3\). They explicitly posed the remaining \(n>3\) finite-horizon universality as a conjecture (Section VI and Appendix E). The present result verifies its first untreated instance, \(n=4\), by a distribution-free signed-order argument and supplies the exact two-regime cancellation of conditional sign patterns.

The classical Sparre Andersen results concern one-sided persistence and extremal-time marginal distributions; these do not directly assert this joint endpoint-extrema probability. The claim is restricted to the four-step case and does not claim a general solution of the 2020 conjecture.

## Limitations

No conclusion is proved here at \(n\ge5\), for dependent or nonexchangeable increments, or for distributions with atoms. Conditional sign-pattern probabilities depend on the magnitudes even though their sum is universal. A later specialist treatment of extremal-time distributions may have additional results not visible from accessible abstracts; historical priority is not independently certified.

## References

1. F. Mori, S. N. Majumdar and G. Schehr, *Time between the maximum and the minimum of a stochastic process*, arXiv:1909.05594, first posted 2019-09-12, especially the discrete-walk extremal-boundary discussion.
2. F. Mori, S. N. Majumdar and G. Schehr, *Distribution of the Time Between Maximum and Minimum of Random Walks*, arXiv:2002.12352, first posted 2020-02-26, Section VI and Appendix E; Phys. Rev. E **101** (2020), 052111.
3. S. N. Majumdar and G. Schehr, *Time of the Maximum and the Minimum*, in *Statistics of Extremes and Records in Random Sequences*, Oxford University Press (2024), Chapter 5; only chapter metadata and abstract inspected.
