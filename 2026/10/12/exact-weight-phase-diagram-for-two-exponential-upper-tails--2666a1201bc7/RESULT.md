# Exact weight phase diagram for two exponential upper tails
## Finding
Let \(X_1,X_2\) be independent exponential random variables with mean \(1\). For nonnegative weights \(a,b\) with \(a+b=1\), define
\[
T_t(a,b)=\Pr\{aX_1+bX_2\ge t\},\qquad t>1.
\]
The fixed-sum normalization makes \(\mathbb E(aX_1+bX_2)=1\). By symmetry it is enough to take \(a\ge b\). Put \(r=a/b\in[1,\infty]\), where \(r=\infty\) denotes the sparse endpoint \((a,b)=(1,0)\).

Let \(\tau\) be the unique root in \((1,3/2)\) of
\[
e^\tau=1+2\tau.
\]
Numerically,
\[
\tau=1.2564312086261696769\ldots.
\]
For every \(1<t<3/2\), let \(x_t\) be the unique solution in \((0,t/(t-1))\) of
\[
\log\!\frac{(1+x)(t+x)}{t-(t-1)x}
=x+\frac{tx}{t+x},
\]
and set \(r_t=1+x_t/t\).

Then the complete extremal phase diagram is as follows. If \(1<t<\tau\), equal weights uniquely maximize \(T_t\), while \(r_t\) uniquely minimizes it. At \(t=\tau\), the equal and sparse endpoints are the two maximizers, while \(r_t\) is the unique minimizer. If \(\tau<t<3/2\), the sparse endpoint uniquely maximizes \(T_t\), while \(r_t\) uniquely minimizes it. Finally, for every \(t\ge3/2\), \(T_t\) is strictly increasing with weight imbalance: equal weights uniquely minimize and the sparse endpoint uniquely maximizes. Uniqueness is always understood up to interchanging \(a\) and \(b\).

## Assumptions and scope
The variables are exactly independent mean-one exponential variables. The weights are nonnegative and have fixed sum \(1\). The sparse endpoint is included by continuity; if weights are required to be strictly positive, the corresponding sparse maximum is a supremum approached as one weight tends to zero. The theorem concerns thresholds \(t>1\), the same above-mean regime used in exponential concentration inequalities. No assertion is made here for \(t\le1\), for three or more summands, or for gamma shapes different from one.

## Proof
For \(a>b>0\), direct convolution gives
\[
T_t(a,b)=\frac{a e^{-t/a}-b e^{-t/b}}{a-b}.
\]
With \(a=r/(r+1)\) and \(b=1/(r+1)\), this becomes
\[
T_t(r)=e^{-t}\frac{r e^{-t/r}-e^{-tr}}{r-1},\qquad r>1.
\]
The continuous endpoint values are
\[
T_t(1)=e^{-2t}(1+2t),\qquad T_t(\infty)=e^{-t}.
\]
The first value is the survival function of a shape-two gamma variable with scale \(1/2\); the second is the one-summand exponential tail.

Since the factor \(e^{-t}\) is irrelevant to monotonicity, set
\[
F_t(r)=\frac{r e^{-t/r}-e^{-tr}}{r-1}.
\]
A direct differentiation shows that the sign of \(F_t'(r)\) is the sign of
\[
h_t(r)=t-1-\frac tr+\bigl(1+t(r-1)\bigr)e^{-t(r-1/r)}.
\]
Put
\[
x=t(r-1),\qquad u=\frac{tx}{t+x}=t\left(1-\frac1r\right).
\]
If \(u\ge1\), then \(h_t(r)>0\) immediately. If \(u<1\), then \(h_t(r)>0\) is equivalent to \(L_t(x)>0\), where
\[
L_t(x)=
\log\!\frac{(1+x)(t+x)}{t-(t-1)x}
-x-\frac{tx}{t+x}.
\]
On \(0<x<t/(t-1)\), exact differentiation and factorization give
\[
L_t'(x)=
\frac{x^2 P_t(x)}{(t+x)^2(1+x)\bigl(t-(t-1)x\bigr)},
\]
with
\[
P_t(x)=(t-1)x^2+t(2t-3)x+t^2(2t-3).
\]

If \(t\ge3/2\), every coefficient of \(P_t\) is nonnegative and the leading coefficient is positive; at \(t=3/2\), \(P_t(x)=x^2/2\). Hence \(L_t'(x)>0\) for every \(x>0\). Since \(L_t(0)=0\), this gives \(h_t(r)>0\), and therefore \(T_t(r)\) is strictly increasing for \(r>1\). This proves the final phase.

Now suppose \(1<t<3/2\). Then \(P_t(0)<0\), while the leading coefficient is positive. Its two real roots have negative product, so \(P_t\) has exactly one positive root. Consequently \(L_t\) first decreases and then increases. Moreover,
\[
L_t(0)=0,
\qquad
L_t(x)\longrightarrow+\infty
\quad\text{as}\quad x\uparrow\frac{t}{t-1}.
\]
Thus \(L_t\) has exactly one positive zero \(x_t\) after its minimum. It follows that \(T_t(r)\) strictly decreases for \(1<r<r_t\) and strictly increases for \(r>r_t\), where \(r_t=1+x_t/t\). Hence \(r_t\) is the unique interior global minimizer.

Only the two endpoints can therefore maximize when \(1<t<3/2\). Their ratio is
\[
\frac{T_t(1)}{T_t(\infty)}=e^{-t}(1+2t).
\]
The function \(e^t-1-2t\) is strictly increasing for \(t>\log 2\), is negative at \(t=1\), and positive at \(t=3/2\). Hence it has a unique root \(\tau\in(1,3/2)\). Endpoint comparison gives the three remaining cases exactly.

## Verification
The convolution formula follows by integrating the two exponential densities and can also be checked from the partial-fraction decomposition of the Laplace transform. The derivative identity above was independently expanded and refactored algebraically. The key sign reduction is exhaustive: for \(u<1\) it is equivalent to \(L_t(x)>0\), while for \(u\ge1\) positivity of \(h_t\) is immediate. The quadratic \(P_t\) determines the complete derivative sign pattern, so no finite sampling is used to infer the global theorem.

The endpoint crossover constant is defined exactly by \(e^\tau=1+2\tau\). Its decimal value is only a convenience and is not used in the proof.

## Relationship to prior work
Li and Tkocz review Janson's tail inequality for weighted sums of independent mean-one exponentials and emphasize the large-threshold role of the largest weight; their paper then develops corresponding bounds for two-sided exponentials and broader nonnegative laws. The inspected full text gives bounds in terms of the ratio of total weight to largest weight, but not the exact two-summand fixed-mean extremal profile proved here.

The classical gamma-convolution literature gives strong comparison results. In particular, Bock, Diaconis, Huffer, and Perlman established Schur-type tail comparisons in suitable tail regions, while Diaconis and Perlman studied unique crossings under weight majorization. Yu later gives a theorem-level formulation for two gamma summands: under explicit product and largest-weight conditions, two weighted-gamma distribution functions cross exactly once. These results govern comparisons between fixed pairs of weight vectors; they do not state the global optimization over the entire two-weight simplex at a fixed threshold, the unique interior minimizer for \(1<t<3/2\), or the distinct endpoint crossover \(e^\tau=1+2\tau\).

A closely related published database result on two-gamma sums identifies the local equal-weight curvature transition; for exponential shape one this corresponds to the threshold \(t=3/2\). The present result does not claim that local threshold as new. Its contribution is the global derivative classification, the unique interior minimizer below the transition, and the exact switch of the global maximizer at \(\tau\).

## Limitations
The theorem is a two-summand result. It does not classify extrema on higher-dimensional weight simplices, where additional stationary configurations can occur. It also does not replace the more general unique-crossing or majorization theorems for gamma convolutions.

An originality risk remains because some older gamma-convolution papers are not fully available in open text and may contain equivalent calculations under different notation. The inspected theorem-level restatements and abstracts cover pairwise crossings and tail-region Schur properties, not the complete fixed-threshold two-weight phase diagram stated here.

## References
1. Jiawei Li and Tomasz Tkocz, “Tail bounds for sums of independent two-sided exponential random variables,” arXiv:2109.14387, first submitted 2021-09-29; later in *High Dimensional Probability IX*, Progress in Probability 80, 2023.
2. Yaming Yu, “On the Unique Crossing Conjecture of Diaconis and Perlman on Convolutions of Gamma Random Variables,” arXiv:1607.02689; *Annals of Applied Probability* 27 (2017), 3893–3910.
3. M. E. Bock, P. Diaconis, F. W. Huffer, and M. D. Perlman, “Inequalities for linear combinations of gamma random variables,” *Canadian Journal of Statistics* 15 (1987), 387–395.
4. P. Diaconis and M. D. Perlman, “Bounds for tail probabilities of weighted sums of independent gamma random variables,” *IMS Lecture Notes–Monograph Series* 16 (1990), 147–166.
