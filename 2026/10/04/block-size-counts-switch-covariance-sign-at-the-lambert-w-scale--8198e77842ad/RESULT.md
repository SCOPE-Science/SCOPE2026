# Block-size counts switch covariance sign at the Lambert-W scale

## Finding

Let \(\Pi_n\) be uniformly distributed over all set partitions of
\[
[n]=\{1,\ldots,n\}.
\]
Let \(K_n\) be the total number of blocks, and for \(1\le r\le n\) let \(X_{n,r}\) be the number of blocks of size \(r\).

Write \(B_m\) for the \(m\)-th Bell number, with \(B_0=1\), and put
\[
q_m=\frac{B_{m+1}}{B_m},
\qquad
\mu_m=\mathbb E K_m=q_m-1.
\]

There is an exact Palm identity for a marked \(r\)-block. For every measurable \(f\) for which the displayed expectations exist,
\[
\boxed{
\frac{\mathbb E[X_{n,r}f(K_n)]}{\mathbb E X_{n,r}}
=
\mathbb E f(1+K_{n-r}).
}
\tag{1}
\]
The normalizing factor is
\[
\boxed{
\mathbb E X_{n,r}
=
\binom nr\frac{B_{n-r}}{B_n}.
}
\tag{2}
\]

Taking \(f(k)=k\) gives the exact covariance
\[
\boxed{
\operatorname{Cov}(K_n,X_{n,r})
=
\binom nr\frac{B_{n-r}}{B_n}
\left(1+q_{n-r}-q_n\right).
}
\tag{3}
\]

The sign has a single transition in block size. Define
\[
t_n=
\min\left\{1\le r\le n:1+q_{n-r}-q_n\le0\right\}.
\tag{4}
\]
Then
\[
\boxed{\operatorname{Cov}(K_n,X_{n,r})>0\quad\text{for }r<t_n,}
\tag{5}
\]
\[
\boxed{\operatorname{Cov}(K_n,X_{n,t_n})\le0,}
\tag{6}
\]
and
\[
\boxed{\operatorname{Cov}(K_n,X_{n,r})<0\quad\text{for }r>t_n.}
\tag{7}
\]

Let \(\alpha_n>0\) solve
\[
\alpha_ne^{\alpha_n}=n+1.
\]
Then the sign boundary lies at the natural Lambert-\(W\) block scale:
\[
\boxed{\frac{t_n}{\alpha_n+1}\longrightarrow1.}
\tag{8}
\]
Equivalently, for every fixed \(\varepsilon>0\), all sufficiently large \(n\) satisfy
\[
\operatorname{Cov}(K_n,X_{n,r})>0
\quad\text{when}\quad
r\le(1-\varepsilon)(\alpha_n+1),
\tag{9}
\]
and
\[
\operatorname{Cov}(K_n,X_{n,r})<0
\quad\text{when}\quad
r\ge(1+\varepsilon)(\alpha_n+1).
\tag{10}
\]

Thus extra small blocks accompany partitions with more blocks overall, while blocks beyond the natural logarithmic size scale accompany partitions with fewer blocks. The transition is already encoded in the exact finite-\(n\) Palm identity (1).

## Assumptions and scope

The set partition is uniform over the \(B_n\) partitions of \([n]\).

The variable \(X_{n,r}\) counts blocks of one fixed size \(r\); the result does not claim independence among the block-size counts.

Equation (1) is a size-biased or Palm identity: after weighting a partition by its number of \(r\)-blocks, the law of \(K_n\) is exactly the law of \(1+K_{n-r}\).

The threshold result concerns only the sign of covariance with the total block count, not the full conditional distribution of \(X_{n,r}\) given \(K_n\).

## Proof

Consider pairs \((\pi,B)\), where \(\pi\) is a set partition of \([n]\) and \(B\) is a distinguished block of \(\pi\) having size \(r\).

There are exactly
\[
\binom nr B_{n-r}
\]
such pairs: choose the \(r\) labels in the distinguished block and partition the remaining \(n-r\) labels arbitrarily.

Deleting the distinguished block gives a bijection
\[
(\pi,B)\longleftrightarrow(S,\rho),
\]
where \(S\subset[n]\), \(|S|=r\), and \(\rho\) is an arbitrary partition of the complement. Under this bijection,
\[
K_n(\pi)=1+K_{n-r}(\rho).
\]
Therefore
\[
\begin{aligned}
\mathbb E[X_{n,r}f(K_n)]
&=\frac1{B_n}\sum_{\pi}\sum_{\substack{B\in\pi\\|B|=r}}f(K_n(\pi))\\
&=\binom nr\frac{B_{n-r}}{B_n}\,\mathbb E f(1+K_{n-r}).
\end{aligned}
\]
Setting \(f=1\) proves (2), and division gives (1).

Taking \(f(k)=k\), and using
\[
\mathbb E K_m=\frac{B_{m+1}}{B_m}-1=q_m-1,
\]
gives (3).

It remains to analyze
\[
c_n(r)=1+q_{n-r}-q_n.
\tag{11}
\]
The Bell numbers have the moment representation
\[
B_m=\mathbb E Z^m,
\qquad Z\sim\operatorname{Poisson}(1).
\]
Cauchy--Schwarz is strict for this nondegenerate \(Z\), so
\[
B_m^2<B_{m-1}B_{m+1}
\qquad(m\ge1).
\tag{12}
\]
Hence \(q_m\) is strictly increasing, and \(c_n(r)\) is strictly decreasing in \(r\). Also
\[
c_n(n)=2-q_n<0
\qquad(n\ge2),
\]
because \(q_1=2\) and the ratios increase strictly. This proves existence and uniqueness of the sign transition (4)--(7).

For its asymptotic location, use the standard Bell-ratio estimate
\[
q_m=\frac{m}{\alpha_m}+O\!\left(\frac1{\alpha_m}\right),
\tag{13}
\]
where \(\alpha_me^{\alpha_m}=m+1\).

For real \(x\), let \(\alpha_xe^{\alpha_x}=x+1\) and put \(F(x)=x/\alpha_x\). Implicit differentiation gives
\[
\alpha_x'=\frac{\alpha_x}{(x+1)(1+\alpha_x)}
\]
and
\[
F'(x)=\frac1{1+\alpha_x}+\frac1{\alpha_x(x+1)(1+\alpha_x)}.
\tag{14}
\]
Uniformly for \(r=O(\alpha_n)\), one has \(\alpha_x=\alpha_n+o(1)\) on \([n-r,n]\). Integrating (14) and combining with (13) yields
\[
q_n-q_{n-r}=\frac{r}{\alpha_n+1}+o(1)
\tag{15}
\]
uniformly for such \(r\). Thus
\[
c_n(r)=1-\frac{r}{\alpha_n+1}+o(1).
\tag{16}
\]
For any fixed \(\varepsilon>0\), (16) is positive below \((1-\varepsilon)(\alpha_n+1)\) and negative above \((1+\varepsilon)(\alpha_n+1)\) for all sufficiently large \(n\). Strict monotonicity then proves (8)--(10).

## Verification

The accompanying checker exhaustively enumerates all set partitions through \(n=9\) using restricted-growth strings.

For every admissible block size it verifies the marked-block identity for several functions of \(K_n\), the exact mean (2), the covariance formula (3), and the finite sign pattern.

A separate exact Bell-number computation verifies strict monotonicity and the threshold through \(n=300\). Numerical evaluation of \(\alpha_n\) is used only as a sanity check on the asymptotic threshold ratio; the proof of (8) is analytic.

Finite replay is supplementary. The all-\(n\) theorem is the marked-block bijection plus strict Bell log-convexity and the Bell-ratio asymptotic above.

## Relationship to prior work

Chern, Diaconis, Kane, and Rhoades give a general algebra of set-partition statistics whose aggregates are shifted Bell polynomials. Their full text explicitly includes the total number of blocks and the number of blocks of a prescribed size, gives their separate first moments, and proves closure under multiplication. Thus their framework guarantees that mixed moments of these statistics have shifted-Bell formulas. The inspected paper does not state the marked-block Palm identity (1), the explicit mixed covariance (3), or its sign transition.

Their companion central-limit paper uses Stam's random-partition algorithm and records the standard asymptotic (13), which supplies the asymptotic input used here.

Timashev studies the number of blocks of a given size conditional on a known total number of blocks and derives asymptotic expectations, variances, and limit laws. Only abstract-level material was accessible in the inspected source, so it remains a residual originality risk for an equivalent covariance statement.

Sachkov's earlier probability treatment of uniformly random set partitions with marked subsets places this subject in combinatorial probability and lists primary classification \(60C05\). Its accessible abstract concerns marked-subset distributions rather than the block-size/total-block covariance phase.

## Limitations

The sign transition concerns covariance with the total number of blocks. It does not imply stochastic monotonicity of \(X_{n,r}\) conditional on \(K_n\).

The exact finite threshold is determined by Bell ratios through (4); integer rounding can make it oscillate around \(\alpha_n+1\).

The marked-block bijection is elementary. Older multivariate Bell-generating-function literature may contain the mixed moment implicitly; the originality claim is the Palm formulation together with the exact one-switch covariance interpretation and its asymptotic location.

## References

1. B. Chern, P. Diaconis, D. M. Kane, and R. C. Rhoades, “Closed expressions for averages of set partition statistics,” arXiv:1304.4309, first submitted 2013-04-16; later *Research in the Mathematical Sciences* 1 (2014), article 2.
2. B. Chern, P. Diaconis, D. M. Kane, and R. C. Rhoades, “Central Limit Theorems for some Set Partition Statistics,” arXiv:1502.00938, first submitted 2015-02-03; later *Advances in Applied Mathematics* 70 (2015), 92–105.
3. A. N. Timashev, “Random partitions of sets with a known number of blocks,” *Discrete Mathematics and Applications* 13 (2003), 307–317.
4. V. N. Sachkov, “Random partitions of sets with marked subsets,” *Mathematics of the USSR-Sbornik* 21 (1973), 485–498, DOI 10.1070/SM1973v021n03ABEH002030.
