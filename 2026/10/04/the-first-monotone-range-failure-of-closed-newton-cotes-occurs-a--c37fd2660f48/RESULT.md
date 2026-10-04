# The first monotone-range failure of closed Newton–Cotes occurs at twelve panels
## Finding
Let \(n\ge1\), and let
\[
Q_n(y)=\sum_{j=0}^{n}w_j^{(n)}y_j
\]
be the normalized closed Newton–Cotes rule on the equally spaced nodes
\[
0,\frac1n,\ldots,1.
\]
Thus the weights satisfy
\[
\sum_{j=0}^{n}w_j^{(n)}=1,
\qquad
w_j^{(n)}=w_{n-j}^{(n)},
\]
and \(Q_n(y)\) is the quadrature approximation to the average value of the sampled function.

For proper prefix sums
\[
P_k^{(n)}=\sum_{j=0}^{k}w_j^{(n)},
\qquad
0\le k<n,
\]
define
\[
m_n=\min\!\left(0,\min_{0\le k<n}P_k^{(n)}\right).
\]
Then for every \(M\ge0\),
\[
\left\{
Q_n(y):
0\le y_0\le y_1\le\cdots\le y_n\le M
\right\}
=
\left[
m_nM,(1-m_n)M
\right].
\]
In particular, closed Newton–Cotes maps every bounded nondecreasing sample vector into its data range \([0,M]\) if and only if every proper cumulative weight is nonnegative.

Exact evaluation of the Cotes numbers gives
\[
m_n=0
\qquad
(1\le n\le11),
\]
so negative individual weights do not by themselves destroy range preservation. Indeed the \(9\)-point rule \(n=8\), and the \(11\)- and \(12\)-point rules \(n=10,11\), already contain negative weights while every proper cumulative weight remains positive.

The first failure occurs at
\[
n=12.
\]
The normalized \(13\)-point closed Newton–Cotes weights are
\[
\frac1{63063000}
\left(
1364651,
9903168,
-7587864,
35725120,
-51491295,
87516288,
-87797136,
87516288,
-51491295,
35725120,
-7587864,
9903168,
1364651
\right).
\]
Their smallest proper prefix is the central one:
\[
P_6^{(12)}
=
-\frac{147227}{750750}.
\]
Therefore the exact monotone-data range is
\[
-\frac{147227}{750750}M
\le
Q_{12}(y)
\le
\left(
1+\frac{147227}{750750}
\right)M.
\]
The lower endpoint is attained by the monotone step data
\[
y_j=
\begin{cases}
0,&0\le j<6,\\
M,&6\le j\le12,
\end{cases}
\]
and the upper endpoint is attained by the reflected complementary step.

The failure is not an artifact of repeated or zero samples. For \(M>0\), set
\[
y_j=
\begin{cases}
\dfrac{j+1}{1000}M,&0\le j<6,\\[2mm]
\left(1-\dfrac{13-j}{1000}\right)M,&6\le j\le12.
\end{cases}
\]
These samples are strictly positive and strictly increasing, yet
\[
Q_{12}(y)
=
-\frac{34977643}{187687500}M<0.
\]

There is an immediate exceptional recovery at \(n=13\). The \(14\)-point closed rule has six negative individual weights, but its smallest proper cumulative weight is
\[
\min_{0\le k<13}P_k^{(13)}
=
\frac{8181904909}{402361344000}>0.
\]
Hence the \(14\)-point rule again maps every bounded nondecreasing sample vector into \([0,M]\).

Thus, among closed Newton–Cotes rules with at most \(14\) nodes, monotone-range preservation holds exactly for
\[
n\in\{1,2,\ldots,11,13\},
\]
and the unique failure is the \(13\)-point rule \(n=12\), with exact defect
\[
\frac{147227}{750750}
=
0.1961065601\ldots.
\]

## Assumptions and scope
The theorem concerns the classical closed Newton–Cotes rule on one equally spaced panel, normalized so that the weights sum to one. For an interval of length \(H>0\), multiply every displayed quadrature range by \(H\).

Only the sampled values are assumed nondecreasing. Any nondecreasing sample vector can be realized by a continuous nondecreasing function, for example by piecewise-linear interpolation, so the extremal statement is not merely a discrete-data artifact.

The finite classification stops at \(n=13\). No claim is made here about all higher orders. The exact cumulative-weight characterization, however, applies to every closed Newton–Cotes order.

## Proof
Write the monotone increments as
\[
d_0=y_0,
\qquad
d_r=y_r-y_{r-1}\quad(1\le r\le n),
\qquad
s=M-y_n.
\]
Then
\[
d_0,d_1,\ldots,d_n,s\ge0,
\qquad
d_0+\cdots+d_n+s=M.
\]
Also
\[
y_j=\sum_{r=0}^{j}d_r.
\]
Substitution into the quadrature functional gives
\[
Q_n(y)
=
d_0+
\sum_{r=1}^{n}T_r^{(n)}d_r,
\]
where
\[
T_r^{(n)}
=
\sum_{j=r}^{n}w_j^{(n)}
\]
is a tail sum. The slack variable \(s\) has coefficient zero. Thus the feasible monotone data form a simplex in the variables
\[
(d_0,\ldots,d_n,s),
\]
and the minimum and maximum of the linear functional occur at simplex vertices:
\[
\min Q_n
=
M\min\!\left(0,1,T_1^{(n)},\ldots,T_n^{(n)}\right),
\]
\[
\max Q_n
=
M\max\!\left(0,1,T_1^{(n)},\ldots,T_n^{(n)}\right).
\]

Closed Newton–Cotes weights are symmetric. Hence
\[
T_r^{(n)}
=
P_{n-r}^{(n)}.
\]
Moreover
\[
T_r^{(n)}
=
1-P_{r-1}^{(n)}.
\]
Symmetry therefore pairs every proper prefix value \(P_k^{(n)}\) with
\[
1-P_k^{(n)}.
\]
It follows immediately that, with
\[
m_n=\min\!\left(0,\min_k P_k^{(n)}\right),
\]
the exact image interval is
\[
[m_nM,(1-m_n)M].
\]
This proves the general criterion.

For the finite classification, the weights are determined uniquely by the moment equations
\[
\sum_{j=0}^{n}w_j^{(n)}
\left(\frac jn\right)^r
=
\frac1{r+1},
\qquad
0\le r\le n.
\]
Solving these equations over the rationals gives the following exact smallest proper prefixes:
\[
\begin{array}{c|c}
n&\min_{0\le k<n}P_k^{(n)}\\
\hline
1&1/2\\
2&1/6\\
3&1/8\\
4&7/90\\
5&19/288\\
6&41/840\\
7&751/17280\\
8&989/28350\\
9&2857/89600\\
10&16067/598752\\
11&434293/17418240\\
12&-147227/750750\\
13&8181904909/402361344000
\end{array}
\]
Every entry through \(n=11\) is positive, the \(n=12\) entry is negative, and the \(n=13\) entry is positive. The displayed \(n=12\) weights reproduce the published closed Newton–Cotes table and directly sum to the stated central prefix.

For \(n=12\), choosing the simplex vertex with only \(d_6=M\) nonzero gives
\[
Q_{12}=T_6^{(12)}M=P_6^{(12)}M,
\]
which attains the lower endpoint. Symmetry gives the upper endpoint. Direct substitution of the strictly increasing rational data displayed in the finding gives the stated negative value.

## Verification
The accompanying `verify.py` uses exact rational arithmetic only. It independently solves the Newton–Cotes moment equations by Gaussian elimination for every \(1\le n\le13\), checks weight symmetry and normalization, computes every proper prefix, and reproduces the exact table in the proof.

For \(n=12\), the checker matches all \(13\) published coefficients exactly, verifies
\[
\min_kP_k^{(12)}
=
-\frac{147227}{750750},
\]
and evaluates both the step extremizer and the strictly increasing witness.

For \(n=13\), it checks that six individual weights are negative while every proper prefix is positive and that the minimum prefix is exactly
\[
\frac{8181904909}{402361344000}.
\]

The simplex reduction is an analytic proof valid for every order. The finite computation is used only to settle the exact coefficient signs for \(1\le n\le13\).

## Relationship to prior work
El-Mikkawy gives a general derivation of open and closed Newton–Cotes Cotes numbers from the Lagrange basis and provides algorithms for computing them. That coefficient theory is prior work.

Sermutlu derives the standard moment equations, emphasizes the appearance of negative coefficients at higher orders, and publishes exact closed-rule coefficients through \(19\) points. In particular, the published \(n=12\) coefficients agree exactly with those used here. Negative weights, their roundoff implications, and high-order Newton–Cotes instability are therefore not claimed as new.

The present result asks a different order-theoretic question: whether the quadrature functional maps the cone of bounded nondecreasing samples into the original data range. For that cone, individual weight signs are not decisive. The relevant invariant is instead the sequence of cumulative weights. This yields the exact image interval, identifies \(n=12\) as the first failure despite earlier negative weights, quantifies its sharp defect, and shows that range preservation returns at \(n=13\).

Published work on monotonicity of quadrature approximations also studies monotone convergence of quadrature sequences under smoothness or derivative-sign assumptions. That is a different notion from coordinatewise monotone sample data; no implication-equivalent cumulative-weight classification was located in the sources checked.

## Limitations
The classification is complete only through \(14\) nodes. Higher closed Newton–Cotes rules can be tested by the same cumulative-weight criterion, but no infinite-order pattern is asserted.

The range property concerns monotone sampled values and does not imply numerical stability with respect to arbitrary perturbations. Negative individual weights can still amplify noise even when all cumulative sums are nonnegative.

A general theorem on positive linear functionals over ordered data cones may encode the cumulative-sum lemma in different language. Likewise, an older Newton–Cotes table may make the \(n=12\) defect numerically recoverable without highlighting it. These remain the principal originality risks.

## References
1. Moawwad El-Mikkawy, *A Unified Approach to Newton–Cotes Quadrature Formulae*, Applied Mathematics and Computation 138 (2003), 403–413, DOI: 10.1016/S0096-3003(02)00144-3.
2. Emre Sermutlu, *A Close Look at Newton–Cotes Integration Rules*, Results in Nonlinear Analysis 2 (2019), 48–60.
3. D. J. Newman, *Monotonicity of Quadrature Approximations*, Proceedings of the American Mathematical Society 42 (1974), 251–257, DOI: 10.1090/S0002-9939-1974-0330865-8.
