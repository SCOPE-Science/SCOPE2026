# A three-halves minimum-total regression characterizes arithmetic finite populations

## Finding

Let
\[
z_1<z_2<\cdots<z_N,
\qquad N\ge3,
\]
be a finite population of distinct real values. Choose an unordered pair uniformly from the
\[
\binom{N}{2}
\]
possible pairs. Let
\[
M
\]
be the smaller sampled value and let
\[
S
\]
be the sum of the two sampled values.

Then, for
\[
1\le k<N,
\]
\[
\boxed{
\mathbb E[S\mid M=z_k]
=
z_k+\frac{1}{N-k}\sum_{j=k+1}^{N}z_j.
}
\tag{1}
\]

The population is an arithmetic progression if and only if the conditional regression in (1) has slope exactly
\[
\frac32.
\]
More precisely, the following are equivalent.

1. There is a real constant \(c\) such that
\[
\boxed{
\mathbb E[S\mid M]
=
\frac32 M+c
}
\tag{2}
\]
almost surely.

2. There are real numbers \(a\) and \(d>0\) such that
\[
\boxed{
z_k=a+(k-1)d,
\qquad
1\le k\le N.
}
\tag{3}
\]

In the arithmetic case,
\[
c=\frac{a+Nd}{2}.
\tag{4}
\]

The corresponding maximum
\[
X_{(2)}
\]
has the dual regression
\[
\boxed{
\mathbb E[S\mid X_{(2)}]
=
\frac32X_{(2)}+\frac{a-d}{2}.
}
\tag{5}
\]

Moreover the two extreme order statistics have population-size-free correlation with the pair total:
\[
\boxed{
\operatorname{Corr}(M,S)
=
\operatorname{Corr}(X_{(2)},S)
=
\frac{\sqrt3}{2}.
}
\tag{6}
\]

Thus the familiar three-halves regression of a two-draw finite-uniform sample is not merely a feature of the canonical labels \(1,\ldots,N\): among strictly ordered finite populations, it characterizes equal spacing.

## Assumptions and scope

Sampling is simple random sampling without replacement with sample size two. Each unordered pair of distinct population units has probability
\[
\binom{N}{2}^{-1}.
\]

The population values are assumed strictly increasing only to avoid ties in the identity of the minimum and maximum. Affine changes of scale and location preserve the characterization.

The result is a rigidity statement about the conditional expectation. It does not claim that arbitrary finite populations have linear minimum-total regression; in general the right side of (1) is nonlinear as a function of \(z_k\).

## Proof

Condition on the event
\[
M=z_k.
\]
The second sampled value is then uniformly distributed over
\[
\{z_{k+1},\ldots,z_N\}.
\]
This proves (1).

Assume first that (2) holds. Define the upper-tail mean
\[
U_k=\frac{1}{N-k}\sum_{j=k+1}^{N}z_j,
\qquad
1\le k<N.
\]
Equations (1)--(2) give
\[
U_k=\frac12z_k+c.
\tag{7}
\]

The tail means satisfy
\[
(N-k)U_k=z_{k+1}+(N-k-1)U_{k+1}.
\tag{8}
\]
Substituting (7) into (8) and multiplying by two yields
\[
(N-k+1)z_{k+1}
=
(N-k)z_k+2c.
\tag{9}
\]
Equivalently,
\[
z_{k+1}-z_k
=
\frac{2c-z_k}{N-k+1}.
\tag{10}
\]

Apply the same formula at \(k+1\):
\[
z_{k+2}-z_{k+1}
=
\frac{2c-z_{k+1}}{N-k}.
\]
Using (10),
\[
2c-z_{k+1}
=
2c-z_k-\frac{2c-z_k}{N-k+1}
=
\frac{N-k}{N-k+1}(2c-z_k).
\]
Therefore
\[
z_{k+2}-z_{k+1}
=
z_{k+1}-z_k
\]
for every
\[
1\le k\le N-2.
\]
All consecutive differences are equal. Strict increase makes their common value \(d\) positive, proving (3).

Conversely, suppose (3) holds. Conditional on
\[
M=z_k,
\]
the other draw is uniform on an arithmetic progression from \(z_{k+1}\) to \(z_N\), so its mean is
\[
\frac{z_{k+1}+z_N}{2}.
\]
Hence
\[
\mathbb E[S\mid M=z_k]
=
z_k+\frac{z_{k+1}+z_N}{2}
=
\frac32z_k+\frac{a+Nd}{2},
\]
which proves (2) and (4). Reversing the order gives (5).

For (6), affine location and scale changes do not alter correlation, so it is enough to use the canonical population
\[
\{1,\ldots,N\}.
\]
For a simple random pair,
\[
\operatorname{Var}(S)=\frac{(N+1)(N-2)}6.
\tag{11}
\]
The minimum is the first order statistic from a sample of size two, and its standard finite-population variance is
\[
\operatorname{Var}(M)=\frac{(N+1)(N-2)}{18}.
\tag{12}
\]
From (2),
\[
\operatorname{Cov}(M,S)
=
\operatorname{Cov}\!\left(M,\mathbb E[S\mid M]\right)
=
\frac32\operatorname{Var}(M).
\tag{13}
\]
Combining (11)--(13) gives
\[
\operatorname{Corr}(M,S)=\frac{\sqrt3}{2}.
\]
The maximum statement follows by reflection.

## Verification

The accompanying exact checker enumerates all strictly increasing integer populations obtained by choosing \(N\) values from \(\{0,\ldots,9\}\) for
\[
3\le N\le9.
\]

For each population it enumerates every unordered sample pair, reconstructs the exact conditional mean of the sample total given the minimum, and verifies that the residual
\[
\mathbb E[S\mid M]-\frac32M
\]
is constant exactly for arithmetic populations.

For every arithmetic population in the census it also verifies the dual maximum regression, the covariance identity (13), and the exact squared correlation
\[
\frac34.
\]

The finite census is supplementary. The all-\(N\) rigidity follows from the recurrence (9)--(10).

## Relationship to prior work

Takahasi and Futatsuya study dependence between order statistics under simple random sampling without replacement from a general finite population. Their principal results establish positive likelihood-ratio dependence for order statistics from one sample and covariance-sign consequences. The inspected covariance section gives sign theorems for pairs of order statistics, but does not state a characterization of equally spaced populations through minimum-total conditional regression.

Balakrishnan, Charalambides, and Papadatos derive sharp expectation bounds for finite-population order statistics and the sample range, with covariance results in the sample-size-two case. The accessible abstract does not expose a conditional-regression rigidity result, so the unavailable article body remains a residual risk rather than being declared non-covering.

Čiginas develops asymptotic normality for finite-population \(L\)-statistics under simple random sampling without replacement. This provides archive-era probability and sampling context for linear combinations of order statistics, but its stated results are asymptotic rather than an inverse characterization of the finite population.

O'Neill gives a modern exact treatment of finite-population order statistics, including the joint law and the arbitrary-population rank mapping. That general distribution makes (1) directly computable, but the inspected full text contains no regression or arithmetic-progression characterization. The new content here is the inverse implication: the single three-halves conditional-regression law forces every population spacing to be equal.

## Limitations

The characterization uses sample size two and the specific slope
\[
\frac32.
\]
Other regression slopes can generate different finite-population recurrences and are not classified here.

The strict-order assumption excludes tied population values. A tied-value analogue would require conditioning on multiplicities and is not claimed.

A known joint distribution of finite-population order statistics determines the conditional expectation in principle. The result here is an inverse rigidity theorem extracted from that structure, not a new joint-distribution formula.

Older ranked-set-sampling and finite-population order-statistic literature is extensive. An equivalent regression characterization could exist in material not located by the targeted searches; that is the principal originality risk.

## References

1. A. Čiginas, “On the asymptotic normality of finite population \(L\)-statistics,” arXiv:1204.2109, first submitted 2012-04-10.
2. K. Takahasi and M. Futatsuya, “Dependence Between Order Statistics in Samples from Finite Population and its Application to Ranked Set Sampling,” *Annals of the Institute of Statistical Mathematics* 50 (1998), 49–70, DOI 10.1023/A:1003497213823.
3. N. Balakrishnan, C. Charalambides, and N. Papadatos, “Bounds on expectation of order statistics from a finite population,” *Journal of Statistical Planning and Inference* 113 (2003), 569–588, DOI 10.1016/S0378-3758(01)00321-4.
4. B. O'Neill, “The Distribution of Order Statistics Under Sampling Without Replacement,” arXiv:2207.00270; later *Journal of Statistical Theory and Applications* 24 (2025), 663–698, DOI 10.1007/s44199-025-00125-y.
