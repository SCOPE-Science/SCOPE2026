# Exact fixed-sum phase diagram for collision entropy of Bernoulli sums

## Finding

Let \(A\) be a Poisson-binomial random variable, independent of two Bernoulli
variables
\[
B_p\sim{\rm Bernoulli}(p),
\qquad
B_q\sim{\rm Bernoulli}(q),
\]
and put
\[
W=A+B_p+B_q.
\]
Fix their total mean
\[
s=p+q\in[0,2]
\]
and write
\[
r=pq.
\]

Let \(a_k=\Pr(A=k)\), extended by zero outside the support, and define the
first three autocorrelations
\[
c_j=\sum_k a_k a_{k+j},
\qquad j=0,1,2.
\]
Set
\[
D=3c_0-4c_1+c_2
\]
and
\[
G=c_0-2c_1+c_2.
\]
Then
\[
D=\frac12\sum_k
\left(a_k-2a_{k-1}+a_{k-2}\right)^2>0.
\tag{1}
\]

The collision probability
\[
Q(W)=\sum_k\Pr(W=k)^2
\]
is an exact strictly convex quadratic in \(r\):
\[
\boxed{
Q(r)=Q(r_0)+2D(r-r_0)^2,
}
\tag{2}
\]
where
\[
r_0=\frac s2-\frac{G}{2D}.
\]

For fixed \(s\), the feasible product interval is
\[
r_-\le r\le r_+,
\qquad
r_-=\max\{0,s-1\},
\qquad
r_+=\frac{s^2}{4}.
\]
Therefore the order-two Rényi entropy
\[
H_2(W)=-\log Q(W)
\]
is maximized exactly at
\[
\boxed{
r_*=
\min\!\left\{
r_+,\,
\max\{r_-,r_0\}
\right\}.
}
\tag{3}
\]
The optimizing unordered pair \(\{p,q\}\) is the unique pair with sum \(s\)
and product \(r_*\).

Thus pair balancing is not automatically entropy improving at Rényi order
two: its effect is determined by the background autocorrelations through
\(G/D\).

For the fundamental two-coin case \(A=0\), the phase diagram becomes fully
explicit. Put
\[
u=\min\{s,2-s\}
\]
and
\[
\alpha=1-\frac1{\sqrt3}.
\]
Then the collision-entropy maximizer has the following form:

- for \(0\le u\le1/3\), one coin is deterministic;
- for \(1/3<u<\alpha\), both coins are nondegenerate and unequal;
- for \(\alpha\le u\le1\), the coins are balanced.

Equivalently,
\[
\boxed{
p=q=\frac s2
\quad\text{maximizes }H_2(B_p+B_q)
\quad\Longleftrightarrow\quad
|s-1|\le\frac1{\sqrt3}.
}
\tag{4}
\]

In the unequal interior regime, the optimal product is
\[
r_*=\frac s2-\frac16,
\]
so the optimal unordered pair is obtained as the two roots of
\[
z^2-sz+\frac s2-\frac16=0.
\]

The minimal collision probability, and hence the maximal collision entropy,
can also be written explicitly. With \(u=\min\{s,2-s\}\),
\[
Q_{\min}(s)=
\begin{cases}
1-2u+2u^2,
&0\le u\le1/3,\\[1mm]
\dfrac13+\dfrac{(1-u)^2}{2},
&1/3\le u\le\alpha,\\[3mm]
\left(1-\dfrac u2\right)^4
+4\left(\dfrac u2\right)^2
 \left(1-\dfrac u2\right)^2
+\left(\dfrac u2\right)^4,
&\alpha\le u\le1.
\end{cases}
\tag{5}
\]
Hence
\[
H_{2,\max}(s)=-\log Q_{\min}(s).
\]

## Assumptions and scope

The variables in \(A\) and the two displayed Bernoulli variables are mutually
independent. The background \(A\) may be the empty sum, which gives the
two-coin corollary.

The logarithm base in \(H_2\) is immaterial for the optimizer. Natural
logarithms are used in the formulas.

The quadratic identity actually holds for any independent finite-support
integer-valued background \(A\); the Poisson-binomial formulation is used
because it is the entropy-concavity setting motivating the result.

The theorem fixes the sum \(p+q\) and varies only the split between the two
selected Bernoulli parameters. It is not a claim that the full
\(n\)-parameter order-two Rényi entropy has a global Schur monotonicity
property.

## Proof

The law of
\[
T=B_p+B_q
\]
has masses
\[
t_0=1-s+r,
\qquad
t_1=s-2r,
\qquad
t_2=r.
\tag{6}
\]

Let \(A'\) and \(T'\) be independent copies. Since
\[
Q(W)=\Pr(A+T=A'+T'),
\]
conditioning on \(T-T'\) gives
\[
Q(r)
=
c_0(t_0^2+t_1^2+t_2^2)
+
2c_1(t_0t_1+t_1t_2)
+
2c_2t_0t_2.
\tag{7}
\]

Substituting (6) into (7) and differentiating with respect to \(r\) yields
\[
Q'(r)
=
4Dr-2Ds+2G
=
4D(r-r_0).
\tag{8}
\]
A second differentiation gives
\[
Q''(r)=4D.
\]
Identity (1) follows by expanding the squared second differences of the
zero-extended sequence \((a_k)\). Because a nonzero finite-support sequence
cannot have all second differences equal to zero,
\[
D>0.
\]
Integrating (8) therefore gives the exact quadratic identity (2).

For fixed \(s\), the roots \(p,q\) of
\[
z^2-sz+r=0
\]
must lie in \([0,1]\). The resulting feasible interval is exactly
\[
\max\{0,s-1\}\le r\le\frac{s^2}{4}.
\tag{9}
\]
Since \(Q\) is strictly convex, its unique feasible minimizer is the
projection of \(r_0\) onto (9), which is (3). Since
\[
H_2=-\log Q
\]
and the logarithm is increasing, minimizing \(Q\) is equivalent to maximizing
\(H_2\).

For \(A=0\),
\[
c_0=1,
\qquad
c_1=c_2=0,
\]
so
\[
D=3,
\qquad
G=1,
\qquad
r_0=\frac s2-\frac16.
\tag{10}
\]
Directly,
\[
Q_s(r)
=
1-2s+2s^2+(2-6s)r+6r^2.
\tag{11}
\]

By complementing both Bernoulli variables, collision probability is unchanged
when \(s\) is replaced by \(2-s\). It is therefore enough to classify
\(0\le s\le1\).

The stationary point in (10) is below the feasible interval precisely when
\[
s\le\frac13.
\]
It is above the balanced endpoint \(s^2/4\) precisely when
\[
\frac s2-\frac16\ge\frac{s^2}{4},
\]
which is equivalent on \([0,1]\) to
\[
s\ge1-\frac1{\sqrt3}.
\]
Between these two thresholds the stationary point is feasible and gives the
unique unequal optimum. Reflection across \(s=1\) gives the full
\(s\in[0,2]\) phase diagram and proves (4).

Finally, substituting the three optimizing products into (11) gives (5).

## Verification

The accompanying exact-rational checker reconstructs random
Poisson-binomial backgrounds and verifies (7) directly by convolution.

It also checks the identity
\[
2D=
\sum_k
\left(a_k-2a_{k-1}+a_{k-2}\right)^2
\]
and the quadratic completion
\[
Q(r)-Q(r_0)=2D(r-r_0)^2
\]
using exact fractions.

For rational fixed sums it verifies the feasible-product projection and
compares the claimed optimizer against dense rational product grids. The
two-coin phase regions are checked through exact polynomial inequalities,
without numerically approximating the irrational threshold.

Finite replay is not used to infer the universal theorem.

## Relationship to prior work

Hillion and Johnson proved the Shannon Shepp--Olkin concavity theorem and
proposed a Rényi/Tsallis extension. Their 2015 preprint explicitly conjectured
a critical Rényi order equal to \(2\). The inspected Section 4 defines the
Rényi functional and formulates the critical-order conjecture, but it does not
give an exact fixed-sum optimizer at order \(2\).

Subsequent work has shown that the universal joint-concavity threshold is
actually \(1\): for every Rényi order above one, a transverse two-coin path
already gives local convexity. In particular, the recent two-coin witness is
a fixed-sum path of the form
\[
p_1(t)=p+t,
\qquad
p_2(t)=p-t.
\]
That result establishes failure of global joint concavity, but it does not
classify the global fixed-sum optimizer, the deterministic/unequal/balanced
phase boundaries, or the background-dependent autocorrelation criterion
(2)--(3).

Madiman, Melbourne, and Roberto study Rényi entropies of Bernoulli sums by
Fourier methods and obtain sharp entropy--variance comparisons and
anti-concentration consequences. Their inspected work concerns different
optimization constraints and does not state the pair-transfer quadratic or
the fixed-sum order-two phase diagram.

Targeted searches using collision entropy, fixed Bernoulli mean, Rényi order
two, Poisson-binomial balancing, and parameter majorization terminology did
not locate formulas (2)--(5).

## Limitations

The exact quadratic simplification is special to Rényi order \(2\), where the
entropy is the logarithm of a collision probability. Other Rényi orders lead
to higher nonlinearities.

The general theorem changes only two Bernoulli parameters while keeping their
sum fixed. It does not classify the simultaneous global maximizer over all
coordinates under a fixed total mean.

The originality assessment used targeted full-text and statement-level
comparisons. An equivalent collision-probability identity could exist under
older convolution or coding terminology not captured by those searches.

## References

1. E. Hillion and O. Johnson, “A proof of the Shepp--Olkin entropy concavity
   conjecture,” arXiv:1503.01570, first submitted 2015-03-05.
2. H. Wang, “The Sharp Rényi and Tsallis Threshold in the Shepp--Olkin
   Concavity Problem,” arXiv:2609.27433, first submitted 2026-09-23.
3. M. Madiman, J. Melbourne, and C. Roberto, “Bernoulli sums and Rényi
   entropy inequalities,” arXiv:2103.00896, first submitted 2021-03-01.
