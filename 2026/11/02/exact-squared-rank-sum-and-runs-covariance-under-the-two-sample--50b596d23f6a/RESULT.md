# Exact squared-rank-sum and runs covariance under the two-sample permutation null

## Finding

For integers \(a,b\ge1\) with \(N=a+b\ge3\), sample a binary sequence uniformly among those with \(a\) ones and \(b\) zeros. Define the centered Wilcoxon rank sum \(W\) and runs count \(R\) in the next section. Then

\[\operatorname{Cov}(W,R)=0,\qquad \operatorname{Cov}(W^2,R)=-\frac{ab(ab-1)}{3N}<0.\]

For \(N\ge4\), each local transition has the exactly position-dependent covariance

\[\begin{aligned}
&\operatorname{Cov}\bigl(W^2,\mathbf1\{X_t\ne X_{t+1}\}\bigr)\
&=\frac{2ab}{N(N-1)}\left[-\frac{ab-1}{6}+\frac{N(N+1)-6ab}{(N-2)(N-3)}\left(\left(t-\frac N2\right)^2-\frac{N(N-2)}{12}\right)\right].
\end{aligned}\]

Thus the ordinary linear cross-covariance vanishes by symmetry, whereas the two-sided Wilcoxon departure \(W^2\) has strictly negative covariance with runs. The local terms need not be equal: their position-dependent corrections cancel upon summation.

## Assumptions and scope

Let \(N=a+b\ge3\), with integers \(a,b\ge1\). Take \(X_i\in\{0,1\}\) uniformly over words with \(\sum_{i=1}^N X_i=a\). Put

\[W=\sum_{i=1}^N iX_i-\frac{a(N+1)}2,\qquad R=1+\sum_{t=1}^{N-1}J_t,\quad J_t=\mathbf1\{X_t\ne X_{t+1}\}.\]

Equivalently, under a common atomless two-sample null, label the pooled sorted observations by sample membership. Their label word is uniform over precisely these fixed-composition words. There are no independence or Gaussian assumptions beyond the common continuous sampling null.

## Proof

Reverse the \(N\) ranks. This leaves \(R\) unchanged and sends \(W\) to \(-W\), proving \(\operatorname{Cov}(W,R)=0\).

Write \(A=ab\) and \(z_t=t-N/2\). The unconditional rank-sum variance is

\[\mathbb E[W^2]=\frac{A(N+1)}{12}.\]

Fix \(t\) and condition on \(J_t=1\). Exactly one of ranks \(t,t+1\) is selected, with each orientation having probability one half. Independently, the remaining \(a-1\) selected ranks form a uniform subset of size \(a-1\) among the remaining \(N-2\) ranks. Therefore

\[\mathbb P(J_t=1)=\frac{2A}{N(N-1)}.\]

The remaining population has centered sum of squares

\[B_t=\frac{N(N^2-1)}{12}-\frac12-\frac{2N}{N-2}z_t^2.\]

Finite-population sampling without replacement and the independent orientation sign give, for \(N\ge4\),

\[\mathbb E[W^2\mid J_t=1]=\frac14+\frac{(a-1)(b-1)}{(N-2)(N-3)}B_t+\frac{(a-b)^2}{(N-2)^2}z_t^2.\]

Here the conditional mean is \(- (a-b)z_t/(N-2)\); the variance contribution \(1/4\) is from the two equally likely pair orientations. Substituting \((a-b)^2=N^2-4A\) and collecting terms yields

\[\mathbb E[W^2\mid J_t=1]-\mathbb E[W^2]= -\frac{A-1}{6}+\frac{N(N+1)-6A}{(N-2)(N-3)}\left(z_t^2-\frac{N(N-2)}{12}\right).\]

Multiplication by \(\mathbb P(J_t=1)\) proves the local formula. The exact finite identity

\[\sum_{t=1}^{N-1}z_t^2=\frac{(N-1)N(N-2)}{12}\]

annihilates the second term when the local covariances are summed. Therefore

\[\operatorname{Cov}(W^2,R)=\sum_{t=1}^{N-1}\operatorname{Cov}(W^2,J_t)=-\frac{A(A-1)}{3N}.\]

For \(N=3\), necessarily \(\{a,b\}=\{1,2\}\). Directly enumerating its three possible marked-rank positions gives \(\operatorname{Cov}(W^2,R)=-2/9\), the same formula. Finally \(A=ab\ge2\) when \(N\ge3\), proving strict negativity.

## Verification

Run the included standalone \(`verify.py`\) using Python 3. It independently enumerates every fixed-composition binary word for all \(3\le N\le11\) and checks the global mixed covariance against the rational formula. It independently checks every local position for all \(4\le N\le10\), using exact rational arithmetic. The script completed both sets of checks. Exhaustive finite verification is corroborative, not a proof for unbounded \(N\).

## Relationship to prior work

Bhattacharya, *A General Asymptotic Framework for Distribution-Free Graph-Based Two-Sample Tests*, arXiv:1508.07530 (first posted 2015-08-30), gives a general asymptotic treatment of the Wald–Wolfowitz runs test and comparisons with rank-based two-sample testing methods. Its inspected introduction, run-test construction and pertinent covariance discussion do not give the finite null covariance between the squared centered Wilcoxon rank sum and run count. Earlier established exact relationships involving runs versus bridge energy, and squared rank sum versus bridge energy, do not algebraically determine this mixed covariance. This is not a claim of exhaustive bibliographic priority: an uninspected joint generating function for runs and binary-word inversion count may imply it.

## Limitations

The result describes exact second-order dependence under the common continuous two-sample null. Zero covariance of \(W\) and \(R\) does not imply independence, and a strictly negative covariance of \(W^2\) and \(R\) does not establish negative association of arbitrary transformations. No alternative-distribution power comparison, optimal combined test or general limit law is proved. Independent auditing and exhaustive historical priority verification have not been performed.

## References

1. B. B. Bhattacharya, *A General Asymptotic Framework for Distribution-Free Graph-Based Two-Sample Tests*, arXiv:1508.07530, first posted 2015-08-30, https://arxiv.org/abs/1508.07530.
2. A. Wald and J. Wolfowitz, *On a Test Whether Two Samples Are from the Same Population*, Annals of Mathematical Statistics **11** (1940), 147–162 (classical definition and motivation for runs testing).
3. F. Wilcoxon, *Individual Comparisons by Ranking Methods*, Biometrics Bulletin **1** (1945), 80–83 (classical rank-sum methodology).
