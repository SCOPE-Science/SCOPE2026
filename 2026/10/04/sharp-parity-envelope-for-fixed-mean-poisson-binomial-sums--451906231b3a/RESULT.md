# Sharp parity envelope for fixed-mean Poisson-binomial sums

## Finding

Let \(B_1,\ldots,B_n\) be mutually independent Bernoulli variables and write
\[
S=\sum_{i=1}^n B_i,\qquad p_i=\Pr(B_i=1),\qquad
\lambda=\sum_{i=1}^n p_i.
\]
The parity bias is
\[
\beta:=\mathbb E[(-1)^S]
=\prod_{i=1}^n(1-2p_i),
\qquad
\Pr(S\ {\rm even})=\frac{1+\beta}{2}.
\]

Assume first that \(0\le\lambda\le n/2\). For each integer
\(0\le r\le\lfloor2\lambda\rfloor\), define
\[
M_0(n,\lambda)=\left(1-\frac{2\lambda}{n}\right)^n,
\]
and, for \(r\ge1\),
\[
M_r(n,\lambda)=
\begin{cases}
\displaystyle
\left(\frac{n-2\lambda+r}{n-r}\right)^{n-r},
& r\le\lambda,\\[1.1em]
\displaystyle
\left(\frac{2\lambda-r}{r}\right)^r,
& r\ge\lambda.
\end{cases}
\]
At an integer \(r=\lambda\), the two formulas agree and equal \(1\).

Put
\[
K_0(n,\lambda)
=
\max_{\substack{0\le r\le\lfloor2\lambda\rfloor\\ r\ {\rm even}}}
M_r(n,\lambda).
\]
Then
\[
\boxed{\beta_{\max}=K_0(n,\lambda).}
\]
If \(\lambda>1/2\), put
\[
K_1(n,\lambda)
=
\max_{\substack{1\le r\le\lfloor2\lambda\rfloor\\ r\ {\rm odd}}}
M_r(n,\lambda).
\]
Then
\[
\boxed{\beta_{\min}=-K_1(n,\lambda).}
\]
For the remaining regime \(0\le\lambda\le1/2\),
\[
\boxed{\beta_{\min}=1-2\lambda.}
\]
Consequently,
\[
\boxed{
\Pr(S\ {\rm even})_{\max}=\frac{1+K_0(n,\lambda)}2
}
\]
and
\[
\boxed{
\Pr(S\ {\rm even})_{\min}=
\begin{cases}
1-\lambda,&0\le\lambda\le1/2,\\[0.4em]
\displaystyle\frac{1-K_1(n,\lambda)}2,&1/2<\lambda\le n/2.
\end{cases}
}
\]

The finite maxima over \(r\) have a simple phase structure. For fixed parity,
\(M_r\) increases as \(r\) approaches \(\lambda\) from below and decreases as
\(r\) moves away from \(\lambda\) above. Hence \(K_0\) or \(K_1\) is obtained
from at most the nearest admissible integer of the required parity on each
side of \(\lambda\).

For \(n/2<\lambda\le n\), set \(\lambda'=n-\lambda\). Complementing every
Bernoulli variable gives the whole remaining range. If \(n\) is even, the
parity endpoints at \(\lambda\) equal those at \(\lambda'\). If \(n\) is odd,
they are complemented:
\[
\Pr(S\ {\rm even})_{\max}
=
1-\Pr(S'\ {\rm even})_{\min},
\qquad
\Pr(S\ {\rm even})_{\min}
=
1-\Pr(S'\ {\rm even})_{\max},
\]
where \(S'\) has mean \(\lambda'\).

Each displayed endpoint has an explicit extremizer. For a chosen
\(1\le r\le\lambda\), take \(r\) deterministic successes and make the
remaining \(n-r\) trials equiprobable with
\[
p=\frac{\lambda-r}{n-r}.
\]
For \(\lambda\le r\le2\lambda\), take \(n-r\) deterministic failures and
make the remaining \(r\) trials equiprobable with
\[
p=\frac{\lambda}{r}.
\]
The \(r=0\) endpoint is the ordinary binomial vector
\(p_1=\cdots=p_n=\lambda/n\). For \(0\le\lambda\le1/2\), the lower endpoint
is attained by one active Bernoulli of parameter \(\lambda\) and
\(n-1\) deterministic failures. Complements give the endpoint constructions
above \(n/2\).

## Assumptions and scope

The only probabilistic assumption is mutual independence of the Bernoulli
summands. The number of trials \(n\) is a positive integer, and the mean
constraint is exact: \(0\le\lambda\le n\). Deterministic Bernoulli variables
with parameter \(0\) or \(1\) are allowed.

The theorem concerns the parity probability, equivalently the Fourier
coefficient at frequency \(\pi\). It does not claim a stochastic-order
comparison of the full Poisson-binomial laws.

## Proof

Independence gives
\[
\beta=\mathbb E[(-1)^S]
=\prod_{i=1}^n\mathbb E[(-1)^{B_i}]
=\prod_{i=1}^n(1-2p_i).
\tag{1}
\]
Assume \(0\le\lambda\le n/2\), and set
\[
x_i=1-2p_i.
\]
Then \(x_i\in[-1,1]\) and
\[
\sum_{i=1}^n x_i=n-2\lambda=:s\ge0.
\tag{2}
\]

Fix a configuration with exactly \(r\) strictly negative \(x_i\)'s. Write
those factors as \(-a_1,\ldots,-a_r\), with \(a_i\in(0,1]\), and the
remaining factors as \(y_1,\ldots,y_{n-r}\), with \(y_j\in[0,1]\). Put
\[
A=\sum_{i=1}^r a_i.
\]
Equation (2) becomes
\[
\sum_{j=1}^{n-r}y_j=s+A.
\tag{3}
\]
The box constraints imply
\[
0\le A\le r,\qquad s+A\le n-r,
\]
hence
\[
0\le A\le \min(r,2\lambda-r).
\tag{4}
\]
In particular, a sign class can occur only when \(r\le2\lambda\).

By AM--GM in each block,
\[
|\beta|
\le
\left(\frac{A}{r}\right)^r
\left(\frac{s+A}{n-r}\right)^{n-r},
\tag{5}
\]
with the \(r=0\) case interpreted separately. For fixed \(r\), the right
side of (5) is nondecreasing in \(A\), and is strictly increasing whenever
it is positive. Therefore the largest possible magnitude in sign class
\(r\) occurs at
\[
A_*=\min(r,2\lambda-r).
\tag{6}
\]

If \(r\le\lambda\), then \(A_*=r\), and (5) gives
\[
|\beta|
\le
\left(\frac{n-2\lambda+r}{n-r}\right)^{n-r}
=M_r(n,\lambda).
\]
Equality requires all \(a_i=1\) and all \(y_j\) equal, which is exactly the
construction with \(r\) deterministic successes and a common residual
Bernoulli parameter.

If \(r\ge\lambda\), then \(A_*=2\lambda-r\), and (5) gives
\[
|\beta|
\le
\left(\frac{2\lambda-r}{r}\right)^r
=M_r(n,\lambda).
\]
Equality requires all \(y_j=1\) and all \(a_i\) equal, giving \(n-r\)
deterministic failures and \(r\) common active parameters. Thus even \(r\)
produce positive endpoint candidates \(M_r\), while odd \(r\) produce
negative endpoint candidates \(-M_r\). Taking the best candidate of each
parity proves the formulas whenever a negative sign class is feasible.

For \(0\le\lambda\le1/2\), all \(p_i\le1/2\): otherwise one coordinate alone
would exceed the total mean. Hence every factor \(1-2p_i\) is nonnegative.
For numbers \(u_i=2p_i\in[0,1]\),
\[
\prod_i(1-u_i)\ge1-\sum_i u_i=1-2\lambda,
\tag{7}
\]
by repeated use of \((1-u)(1-v)\ge1-u-v\). Equality is attained by putting
all the mean on one Bernoulli coordinate. This proves the lower endpoint in
the small-mean regime.

It remains to justify the nearest-\(r\) simplification. For \(r\le\lambda\),
write \(a=\lambda-r\) and \(c=n-\lambda\). Then
\[
M_r=
\left(\frac{c-a}{c+a}\right)^{c+a}.
\]
The logarithm of the right side is strictly decreasing in \(a\in[0,c)\);
hence \(M_r\) strictly increases with \(r\) on the left of \(\lambda\).
For \(r\ge\lambda\), writing \(b=r-\lambda\) and \(c=\lambda\) gives the
same expression
\[
M_r=
\left(\frac{c-b}{c+b}\right)^{c+b},
\]
which strictly decreases with \(b\). This proves the stated phase structure.

Finally, for \(q_i=1-p_i\), the complementary sum
\[
S'=\sum_i(1-B_i)=n-S
\]
has mean \(n-\lambda\) and
\[
(-1)^S=(-1)^n(-1)^{S'}.
\]
This proves the complement rule for \(\lambda>n/2\), and completes the proof.

## Verification

A standalone exact-rational checker accompanies this result. It evaluates the
theorem without floating-point arithmetic. It exhaustively scans rational
parameter grids for small \(n\), checks that every resulting parity bias lies
inside the asserted envelope, explicitly constructs every endpoint family,
and verifies the complement rule and the sign-class formulas.

The computation is corroborative. The global theorem is proved by the
blockwise AM--GM optimization and complement symmetry above; finite
enumeration is not used to infer the infinite parameter statement.

## Relationship to prior work

Poisson-binomial distributions are the laws of sums of independent,
non-identically distributed Bernoulli variables. Le Cam's classical work
studied their Poisson approximation. Later Fourier-analytic work by
Diakonikolas, Kane, and Stewart explicitly uses the product structure of the
Fourier transform of a Poisson-binomial distribution. Formula (1), evaluated
at the parity frequency, is an elementary specialization of that standard
product representation and is not claimed as new.

The contribution here is the fixed-mean extremal problem for that parity
coefficient: the exact upper and lower endpoints, the finite phase competition
between sign counts, and the endpoint constructions. Classical homogenization
results for Bernoulli sums, including Hoeffding's fixed-mean convex-order
principle, do not directly settle this objective because parity is an
oscillatory, nonconvex functional.

Targeted searches for fixed-mean Poisson-binomial parity, even/odd probability
envelopes, and extremization of the product \(\prod_i(1-2p_i)\) did not locate
the displayed endpoint theorem. Closely related public results on
Poisson-binomial stop-loss functionals and low cumulants were inspected; their
objectives and implication sets do not contain the parity envelope.

## Limitations

The parity identity itself is elementary, and the extremal proof uses standard
AM--GM. An equivalent optimization theorem may exist in older inequality,
Boolean-Fourier, reliability, or Bernoulli-sum literature under terminology
that does not mention Poisson-binomial parity. The literature search was
targeted rather than exhaustive, so this remains the main originality risk.

The theorem uses only a first-moment constraint. Adding variance, support,
lower/upper parameter bounds, or other moment information changes the feasible
extremizers and is not addressed here. No claim is made for dependent
Bernoulli variables.

## References

1. L. Le Cam, “An Approximation Theorem for the Poisson Binomial
   Distribution,” *Pacific Journal of Mathematics* 10 (1960), 1181–1197.
2. I. Diakonikolas, D. M. Kane, and A. Stewart, “Properly Learning Poisson
   Binomial Distributions in Almost Polynomial Time,” arXiv:1511.04066v1,
   first posted 2015-11-12.
3. W. Hoeffding, “On the Distribution of the Number of Successes in
   Independent Trials,” *Annals of Mathematical Statistics* 27 (1956),
   713–721.
