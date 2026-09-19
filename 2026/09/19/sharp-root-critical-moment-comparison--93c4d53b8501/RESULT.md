# Sharp normalized moment comparison for polynomial zeros and critical points

## Result

Let \(f\) be a complex polynomial of degree \(n\ge 2\). Suppose that its zeros
\(\lambda_1,\dots,\lambda_n\), counted with multiplicity, lie in the closed disk
\(\overline D(c,R)\), and let \(\xi_1,\dots,\xi_{n-1}\) be the zeros of \(f'\),
again counted with multiplicity. For every integer \(m\ge 1\),
\[
\boxed{
\left|
\frac1n\sum_{i=1}^n(\lambda_i-c)^m
-
\frac1{n-1}\sum_{j=1}^{n-1}(\xi_j-c)^m
\right|
\le
\frac{m-1}{n-1}R^m .
}
\tag{1}
\]

For \(m=1\), the two normalized first moments are exactly equal. For every fixed
\(m\ge2\), equality in (1) occurs for infinitely many degrees: if \(m\mid n\), then
\[
f(z)=\big((z-c)^m-R^m\big)^{n/m}
\]
attains equality. Thus the coefficient in (1) cannot be decreased in a bound
valid for all degrees.

By Gauss--Lucas, both normalized moments have modulus at most \(R^m\), so for
very large \(m\) one may combine (1) with the elementary bound \(2R^m\).

## Analytic-test corollary

Let
\[
\phi(c+z)=\sum_{m=0}^{\infty} a_m z^m
\]
be holomorphic on a neighborhood of \(\overline D(c,R)\), with
\(\sum_{m\ge2}(m-1)|a_m|R^m<\infty\). Then
\[
\boxed{
\left|
\frac1n\sum_{i=1}^n\phi(\lambda_i)
-
\frac1{n-1}\sum_{j=1}^{n-1}\phi(\xi_j)
\right|
\le
\frac1{n-1}
\sum_{m\ge2}(m-1)|a_m|R^m .
}
\tag{2}
\]
In particular, if \(\phi\) is holomorphic on a neighborhood of
\(\overline D(c,\rho)\), \(\rho>R\), and
\(\sup_{|z-c|\le\rho}|\phi(z)|\le M\), then Cauchy's estimate gives
\[
\boxed{
\left|
\frac1n\sum_{i=1}^n\phi(\lambda_i)
-
\frac1{n-1}\sum_{j=1}^{n-1}\phi(\xi_j)
\right|
\le
\frac{M}{n-1}
\frac{(R/\rho)^2}{(1-R/\rho)^2}.
}
\tag{3}
\]

Thus the empirical zero measure and the empirical critical-point measure differ
by \(O(n^{-1})\) against every analytic test function controlled on a strictly
larger disk, deterministically and without assumptions on the zero configuration.

## Proof of (1)

The case \(R=0\) is immediate. After translation and dilation, it is enough to
take \(c=0\) and \(R=1\). Put
\[
D=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad
u=\frac1{\sqrt n}(1,\dots,1)^T,
\]
\[
Q=uu^*=\frac1nJ_n,\qquad P=I-Q,\qquad A=PDP.
\]
The Komarova--Rivin differentiator identity implies that the spectrum of \(A\)
is
\[
\{0,\xi_1,\dots,\xi_{n-1}\}
\]
with algebraic multiplicity. Hence
\[
\operatorname{tr}(A^m)=\sum_{j=1}^{n-1}\xi_j^m.
\tag{4}
\]
Because \(|\lambda_i|\le1\), both \(D\) and \(A\) are contractions. Also
\[
AQ=QA=0
\]
and
\[
D-A=QD+PDQ.
\tag{5}
\]

Write
\[
T_m=\operatorname{tr}(D^m-A^m).
\]
The telescoping identity and (5) give
\[
T_m
=
\sum_{k=0}^{m-1}
\operatorname{tr}\!\left(D^{m-1-k}QD\,A^k\right)
+
\sum_{k=0}^{m-1}
\operatorname{tr}\!\left(D^{m-1-k}PDQ\,A^k\right).
\tag{6}
\]
In the second sum every term with \(k\ge1\) vanishes, since cyclicity of trace
places \(QA^k=0\) at the front. In the first sum,
\[
\operatorname{tr}(D^{m-1}QD)
=
\operatorname{tr}(QD^m)
=
\frac1n\operatorname{tr}(D^m).
\tag{7}
\]
For \(m\ge2\), the term \(k=m-1\) in the first sum also vanishes because
\(A^{m-1}Q=0\). Every remaining term in (6) has rank at most one and operator
norm at most one. Therefore
\[
\left|
T_m-\frac1n\operatorname{tr}(D^m)
\right|
\le (m-2)+1=m-1
\qquad (m\ge2).
\tag{8}
\]
For \(m=1\), the same expression is exactly zero:
\[
T_1-\frac1n\operatorname{tr}(D)
=
\operatorname{tr}(PDQ)=0.
\tag{9}
\]

Now set
\[
\mu_m=\frac1n\operatorname{tr}(D^m),\qquad
\eta_m=\frac1{n-1}\operatorname{tr}(A^m).
\]
Since \(T_m=n\mu_m-(n-1)\eta_m\),
\[
T_m-\mu_m=(n-1)(\mu_m-\eta_m).
\tag{10}
\]
Combining (8)--(10) proves (1) in the unit disk, and translation/dilation
restores the factor \(R^m\).

## Equality family

Let \(n=mr\) and
\[
f(z)=\big((z-c)^m-R^m\big)^r.
\]
Every zero satisfies \((\lambda-c)^m=R^m\), so the zero moment in (1) is
\(R^m\). The derivative has the \(m\) roots of
\((z-c)^m=R^m\), each with multiplicity \(r-1\), together with \(c\) of
multiplicity \(m-1\). Consequently
\[
\frac1{n-1}\sum_{j=1}^{n-1}(\xi_j-c)^m
=
\frac{n-m}{n-1}R^m,
\]
and the difference is exactly
\[
\frac{m-1}{n-1}R^m.
\]

## Proof of the analytic-test corollary

The constant term cancels because both empirical measures have mass one, and the
linear term cancels by the exact \(m=1\) identity. Applying (1) term by term gives
(2). If \(\phi\) is bounded by \(M\) on the larger radius \(\rho\), Cauchy's
estimate gives \(|a_m|\le M\rho^{-m}\), and
\[
\sum_{m\ge2}(m-1)(R/\rho)^m
=
\frac{(R/\rho)^2}{(1-R/\rho)^2},
\]
which proves (3).

## Relation to recent literature

Zhang's 2026 effective Sendov paper uses the same Komarova--Rivin compression
and proves, for zeros in the unit disk,
\[
\left|\mathbb E\lambda^m-\mathbb E\xi^m\right|\le \frac{5m}{n}.
\]
The argument there bounds the full perturbation \(D-PDP\) by rank two and norm
two. Formula (6) keeps the two rank-one pieces separate and uses the annihilation
relations \(AQ=QA=0\). This removes all but \(m-1\) unit trace contributions and
also preserves the normalization cancellation in (10), yielding (1).

The older majorization literature gives strong inequalities for the moduli of
zeros and critical points, and the random-polynomial literature gives asymptotic
agreement of empirical zero and critical-point measures under probabilistic
hypotheses. Those statements are different from the deterministic complex
normalized-moment discrepancy in (1).

## Limitations

The bound (1) is attained for every fixed \(m\) along the infinite degree
subsequence \(m\mid n\), but no claim is made that it gives the exact extremal
value for every individual pair \((n,m)\). The analytic-test estimate (3) is a
coefficientwise consequence of (1) and is not asserted to have an optimal
constant for a prescribed test class.

Originality is claimed only to the best of our knowledge. The matrix
differentiator itself is classical, and general rank-one compression or
coefficient-theoretic literature could contain an equivalent trace estimate
under different terminology. No such statement was located in the literature
checked for this record.

## References

1. T. Zhang, *Sendov's conjecture holds for every degree \(n\ge10^{200000}\)*,
   arXiv:2609.20256 (2026), especially Lemmas 2.3 and 2.5.
2. N. L. Komarova and I. Rivin, *Harmonic mean, random polynomials and stochastic
   matrices*, Adv. Appl. Math. 31 (2003), 501--526; arXiv:math/0105236.
3. G. Schmeisser, *Majorization of the Critical Points of a Polynomial by Its
   Zeros*, Comput. Methods Funct. Theory 3 (2003), 95--103.
4. T. Tao, *Sendov's conjecture for sufficiently high degree polynomials*,
   Acta Math. 229 (2022), 347--392; arXiv:2012.04125.
