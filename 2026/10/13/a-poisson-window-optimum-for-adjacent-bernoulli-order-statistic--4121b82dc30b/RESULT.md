# A Poisson-window optimum for adjacent Bernoulli order-statistic correlation

## Finding

Let \(X_1,\ldots,X_n\) be independent identically distributed Bernoulli variables of success probability \(p\in(0,1)\), for an integer \(n\ge2\). Their increasing order statistics are \(X_{1:n}\le\cdots\le X_{n:n}\). Define the **optimized Pearson correlation**
\[
C_n=\max_{0<p<1}\operatorname{Corr}(X_{1:n},X_{2:n}).
\]
The maximum is attained in the interior for each \(n\ge2\). There is a unique \(c_*>0\) satisfying
\[
e^{c_*}=1+c_*+c_*^2,
\quad c_*=1.7932821329008\ldots.
\]
For **every** selection of finite-sample maximizers \(p_n\),
\[
\boxed{n(1-p_n)\longrightarrow c_*},\qquad
\boxed{C_n\longrightarrow \frac{\sqrt{c_*}}{1+c_*}=0.4794126698321\ldots.}
\]
In particular, the sharp asymptotic squared maximum equals \(c_* /(1+c_*)^2=0.2298365079955\ldots\).

## Assumptions and scope

Each observation independently takes value zero with probability \(q=1-p\), and value one otherwise. The statistic is **ordinary Pearson correlation**, not maximal correlation over nonlinear transformations. The optimization varies the Bernoulli parameter freely over \((0,1)\), separately for each sample size. There are no ties-related conventions beyond counting multiplicities among ordinary order statistics. Every assertion is for integers \(n\ge2\). The theorem does not assert uniqueness of a maximizer at any particular finite \(n\).

## Proof

Write \(K=\sum_{j=1}^{n}\mathbf1_{\{X_j=0\}}\sim\operatorname{Bin}(n,q)\). Because observations are binary,
\[
X_{1:n}=\mathbf1_{\{K=0\}},\qquad X_{2:n}=\mathbf1_{\{K\le1\}}.
\]
These indicator events are nested. Set
\[
a=(1-q)^n,\qquad b=(1-q)^n+nq(1-q)^{n-1}.
\]
Then \(0<a<b<1\), and direct covariance and variance calculations give
\[
\operatorname{Cov}(X_{1:n},X_{2:n})=a(1-b),\qquad
\operatorname{Corr}(X_{1:n},X_{2:n})^2
=R_n(q):=\frac{a(1-b)}{b(1-a)}.\tag{1}
\]
This is an exact finite-sample identity, valid throughout \(0<q<1\).

Since \(R_n(q)\le a/b=(1-q)/(1-q+nq)\), it tends to zero as \(q\uparrow1\). As \(q\downarrow0\), \(1-b=O(q^2)\) while \(1-a\sim nq\), so \(R_n(q)\to0\) for fixed \(n\ge2\). Continuity therefore proves that \(R_n\) attains a strictly positive maximum in \((0,1)\).

Put \(c=nq\). If \(c\to c_0\in(0,\infty)\) as \(n\to\infty\), standard binomial-to-Poisson probabilities, or the elementary limits \((1-q)^n\to e^{-c_0}\) and \(nq(1-q)^{n-1}\to c_0e^{-c_0}\), yield
\[
R_n(q)\longrightarrow F(c_0)
:=\frac{e^{c_0}-1-c_0}{(1+c_0)(e^{c_0}-1)}.\tag{2}
\]
To justify optimization *over all parameters*, rather than only pointwise convergence, we must exclude both escaping regimes. If \(c=nq\to\infty\), then using the event nesting,
\[
0\le R_n(q)\le\frac ab=\frac{1-q}{1-q+nq}\le\frac1{1+c}\longrightarrow0.\tag{3}
\]
If instead \(c\to0\), the binomial union and pair-count bounds give
\[
1-a=\Pr(K\ge1)\ge nq-\binom n2q^2\ge c-c^2/2,
\quad 1-b=\Pr(K\ge2)\le\binom n2q^2\le c^2/2.
\]
For all sufficiently small \(c>0\), it follows that
\[
0\le R_n(q)\le\frac{1-b}{1-a}
\le\frac{c}{2-c}\longrightarrow0.\tag{4}
\]
The middle upper bound uses \(a/b<1\). Thus any sequence along which \(R_n(q)\) remains bounded away from zero has \(nq\) bounded above and bounded away from zero.

The limiting function is positive for \(c>0\), vanishes at both endpoints \(c\downarrow0\) and \(c\to\infty\), and has derivative
\[
F'(c)=\frac{e^c(1+c+c^2-e^c)}{(1+c)^2(e^c-1)^2}.\tag{5}
\]
Let \(h(c)=1+c+c^2-e^c\). It satisfies \(h(0)=h'(0)=0\) and \(h''(c)=2-e^c\). Hence \(h'\) first strictly increases and then strictly decreases, eventually becoming negative; therefore \(h\) is initially positive and crosses zero exactly once on \((0,\infty)\). Denote the unique positive zero by \(c_*\). Equation (5) proves that \(F\) has the unique global maximum at \(c_*\). Substituting \(e^{c_*}=1+c_*+c_*^2\) into (2) gives
\[
F(c_*)=\frac{c_*}{(1+c_*)^2}.\tag{6}
\]

Choose any finite-sample maximizers \(q_n=1-p_n\). Evaluating (1) at the competitor \(q=c_*/n\) (valid for sufficiently large \(n\)) gives \(\liminf_n R_n(q_n)\ge F(c_*)>0\). Bounds (3)–(4) force every subsequence of \(nq_n\) to have further subsequences converging inside \((0,\infty)\). At any limit \(c_0\), (2) and optimality imply \(F(c_0)\ge F(c_*)\). Uniqueness of the limiting maximizer forces \(c_0=c_*\). Thus the *whole* sequence satisfies \(nq_n\to c_*\), and \(R_n(q_n)\to F(c_*)\). Taking positive square roots proves the theorem.

## Verification

The standalone pure-Python script `artifacts/verify_adjacent.py` computes the exact covariance independently by enumerating all binary sample paths for lengths two through eight and four rational parameters per length: 28 exact fraction-based equalities. It also brackets the unique nonzero exponential root and checks the convergence of (1) against (6) at four growing sample sizes. The infinite, optimized, boundary-uniform conclusion is proved by equations (1)–(6), **not** inferred from the finite checks.

## Relationship to prior work

López-Blázquez and Salamanca-Miño (2021) formulate discrete-parent order-statistic correlation as an optimization over probabilities and positions. Their complete paper develops gradient-based numerical optimization and reports the binary-support values for sample sizes two through nine (Table 3); these are finite-sample numerical results, not the optimized large-sample Poisson-window limit or its unique optimizing rare-event scale. Our result concerns the adjacent extreme ranks \((1,2)\) specifically and supplies a closed limiting constant and localization theorem. Papadatos (2022) studies correlation extremizers for two observations and discusses broader order-statistic correlation questions, but does not imply the above large-sample result. Previously published finite-support extremizers with a sample size of two, or results allowing dependence instead of iid Bernoulli observations, do not establish this asymptotic optimization.

## Limitations

The result applies only to iid Bernoulli parents and the first two order statistics, plus the reflected last-two case by swapping zero and one. It does not determine exact finite-sample optimal parameters, give a uniform error bound or second-order expansion, optimize arbitrary discrete or continuous parents, or address nonlinear maximal correlation. Bibliographic searching is not exhaustive; equivalent formulations through nested Bernoulli events or Poisson threshold indicators remain a priority risk. Numerical checks are corroboration, not infinite certification.

## References

1. F. López-Blázquez and B. Salamanca-Miño, *Automatic differentiation and maximal correlation of order statistics from discrete parents*, Computational Statistics 36 (2021), 2889–2915, first online April 12, 2021. DOI: 10.1007/s00180-021-01103-5. Lawful full text: https://grupo.us.es/fqm331/wp-content/uploads/2021/07/justopuerto.pdf.
2. N. Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, first submitted May 28, 2022, arXiv:2205.14360v1, https://arxiv.org/abs/2205.14360.
3. Published comparison: *Sharp min–max correlation over three-point probability weights*, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-uniform-maximizes-three-point-minmax-correlation--92f0f4188ee4. This treats two observations with a three-atom parent, not large samples of two-atom parents.
