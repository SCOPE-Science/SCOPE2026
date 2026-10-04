# A one-switch covariance law for occupancy richness and frequency counts

## Finding

Throw
\[
n\ge2
\]
balls independently and uniformly into
\[
m\ge2
\]
boxes. Let \(N_i\) be the number of balls in box \(i\), let
\[
K=\#\{i:N_i>0\}
\]
be the number of occupied boxes, and for
\[
1\le r\le n
\]
let
\[
K_r=\#\{i:N_i=r\}
\]
be the number of boxes containing exactly \(r\) balls.

Put
\[
q=\frac{m-1}{m},
\qquad
s=\frac{m-2}{m}.
\]
Then
\[
\boxed{
\operatorname{Cov}(K,K_r)
=
\binom nr
\frac{m-1}{m^{r-1}}
\left(
q^{\,2n-r-1}-s^{\,n-r}
\right).
}
\tag{1}
\]

For \(m=2\),
\[
\operatorname{Cov}(K,K_r)>0
\quad(1\le r<n),
\qquad
\operatorname{Cov}(K,K_n)<0.
\tag{2}
\]

For \(m\ge3\), define
\[
\kappa_{m,n}
=
(n-1)
\frac{\log\!\left(m/(m-1)\right)}
{\log\!\left((m-1)/(m-2)\right)}
\tag{3}
\]
and
\[
r_\star
=
n-\left\lfloor\kappa_{m,n}\right\rfloor.
\tag{4}
\]
Then
\[
0<\kappa_{m,n}<n-1,
\qquad
\kappa_{m,n}\notin\mathbb Z,
\tag{5}
\]
and the entire frequency spectrum has exactly one covariance sign switch:
\[
\boxed{
\operatorname{Cov}(K,K_r)>0
\quad\text{for }1\le r<r_\star,
}
\tag{6}
\]
while
\[
\boxed{
\operatorname{Cov}(K,K_r)<0
\quad\text{for }r_\star\le r\le n.
}
\tag{7}
\]

In particular,
\[
\operatorname{Cov}(K,K_1)>0
\]
for every \(m,n\ge2\): under the equal-box occupancy model, observed richness and the singleton count move together in covariance. At the opposite end,
\[
\operatorname{Cov}(K,K_n)<0,
\]
because an \(n\)-ton means that all balls fell into one box.

For fixed \(m\ge3\),
\[
\frac{r_\star}{n}
\longrightarrow
1-
\frac{\log(m/(m-1))}
{\log((m-1)/(m-2))}
\qquad(n\to\infty).
\tag{8}
\]
For fixed \(n\), as \(m\to\infty\), eventually
\[
r_\star=2,
\]
so singletons are the only positive-covariance frequency class and every \(r\)-ton with \(r\ge2\) is negatively correlated with richness.

## Assumptions and scope

The allocation is the classical finite uniform occupancy model: each ball independently chooses one of \(m\) boxes with probability \(1/m\).

The result concerns covariance between total observed richness \(K\) and one coordinate \(K_r\) of the occupancy frequency spectrum. It does not claim that the full vector \((K_1,\ldots,K_n)\) has a one-sign covariance matrix; different \(r\)-counts can have their own dependence structure.

The sign classification is exact at finite \(m,n\). No asymptotic approximation is used in (1), (6), or (7).

## Proof

For each box \(i\), write
\[
I_i=\mathbf 1_{\{N_i>0\}},
\qquad
J_{i,r}=\mathbf 1_{\{N_i=r\}}.
\]
Then
\[
K=\sum_{i=1}^m I_i,
\qquad
K_r=\sum_{i=1}^m J_{i,r}.
\]

Set
\[
A_r
=
\Pr(N_i=r)
=
\binom nr
m^{-r}q^{\,n-r}.
\tag{9}
\]
For a fixed box,
\[
\operatorname{Cov}(I_i,J_{i,r})
=
A_r-(1-q^n)A_r
=
A_rq^n.
\tag{10}
\]

Now take two distinct boxes \(i\ne j\). Since \(J_{j,r}=1\) already implies that exactly \(r\) balls went to box \(j\),
\[
\Pr(N_j=r,N_i=0)
=
\binom nr m^{-r}s^{\,n-r}.
\tag{11}
\]
Therefore
\[
\begin{aligned}
\operatorname{Cov}(I_i,J_{j,r})
&=
\Pr(N_j=r)-\Pr(N_j=r,N_i=0)
-
\Pr(N_i>0)\Pr(N_j=r)\\
&=
A_rq^n
-
\binom nr m^{-r}s^{\,n-r}.
\end{aligned}
\tag{12}
\]

Summing (10) over the \(m\) diagonal pairs and (12) over the \(m(m-1)\) off-diagonal pairs gives
\[
\begin{aligned}
\operatorname{Cov}(K,K_r)
&=
mA_rq^n
+
m(m-1)
\left(
A_rq^n-\binom nr m^{-r}s^{\,n-r}
\right)\\
&=
m^2A_rq^n
-
m(m-1)\binom nr m^{-r}s^{\,n-r}.
\end{aligned}
\]
Substituting (9) and simplifying yields (1).

For \(m=2\), \(s=0\). If \(r<n\), the second term inside the parentheses in (1) vanishes and the covariance is positive. If \(r=n\), the parenthesis is
\[
q^{\,n-1}-1<0,
\]
which proves (2).

Assume now \(m\ge3\), and put
\[
k=n-r.
\]
The prefactor in (1) is positive, so the covariance has the sign of
\[
q^{\,n+k-1}-s^k.
\]
Because \(q>s>0\),
\[
q^{\,n+k-1}>s^k
\]
is equivalent to
\[
q^{\,n-1}\left(\frac qs\right)^k>1.
\]
Taking logarithms gives
\[
k>
(n-1)
\frac{\log(1/q)}{\log(q/s)}
=
\kappa_{m,n}.
\tag{13}
\]

The two logarithms in (3) are positive. Moreover,
\[
\frac{m}{m-1}
<
\frac{m-1}{m-2},
\]
so
\[
0<\kappa_{m,n}<n-1.
\]

There is never equality in (13) for an integer \(k\). Indeed, equality would imply
\[
\left(\frac{m-1}{m}\right)^{n+k-1}
=
\left(\frac{m-2}{m}\right)^k,
\]
hence
\[
(m-1)^{n+k-1}
=
m^{n-1}(m-2)^k.
\tag{14}
\]
But \(m-1\) is coprime to both \(m\) and \(m-2\). The left side of (14) is greater than one and has a prime divisor of \(m-1\), while the right side has none, a contradiction. Thus \(\kappa_{m,n}\notin\mathbb Z\).

Since \(k=n-r\) is integral, (13) is equivalent to
\[
n-r\ge\lfloor\kappa_{m,n}\rfloor+1,
\]
which is exactly
\[
r<r_\star.
\]
This proves (6) and (7).

The limit (8) follows directly from (3)--(4). Finally,
\[
\frac{\log(m/(m-1))}
{\log((m-1)/(m-2))}
\longrightarrow1
\]
from below as \(m\to\infty\). Hence \(\kappa_{m,n}\to n-1\) from below for fixed \(n\), so eventually
\[
\lfloor\kappa_{m,n}\rfloor=n-2
\]
and therefore \(r_\star=2\).

## Verification

The accompanying checker uses exact rational arithmetic for the covariance formula itself.

It directly enumerates all allocations for a bounded grid of \((m,n)\), computes \(K\) and every \(K_r\), and checks that the empirical exact covariance equals (1). It separately checks the diagonal/off-diagonal decomposition, the strict singleton and \(n\)-ton signs, and the existence of exactly one sign transition across \(r=1,\ldots,n\) for a larger grid.

The logarithmic threshold is only used to name the transition index. The no-zero statement is proved arithmetically in (14), not inferred from floating-point computation.

Finite enumeration is supplementary; it does not prove the all-\(m,n\) theorem.

## Relationship to prior work

Barbour and Gnedin study the classical occupancy counts
\[
K_n
\quad\text{and}\quad
X_{n,r},
\]
with emphasis on joint normal approximation, moment growth, and limiting covariance structures in infinite-box schemes. Their full paper explicitly writes
\[
K_n=\sum_{r\ge1}X_{n,r}
\]
and develops covariance formulas for Poissonized \(r\)-counts. Those results establish the natural dependence framework for occupancy frequency counts, but the inspected statements do not give the finite uniform covariance \(\operatorname{Cov}(K,K_r)\) or classify its sign across \(r\).

Barbour's later univariate treatment likewise identifies \(K_n\) and the counts of boxes containing exactly \(r\) balls as the central occupancy statistics, and studies distributional approximation for each. Its aim is approximation rather than an exact finite sign phase diagram.

The formula in (1) is elementary enough that closely related finite-occupancy moment identities may exist in classical urn-model references. The contribution assessed here is the exact reduction of the richness--frequency covariance to one scalar comparison, the proof that equality is impossible, and the resulting unique strict sign-switch index (4).

## Limitations

Uniform box probabilities are essential to the one-parameter sign threshold. For nonuniform boxes, the same indicator decomposition gives exact sums, but there is no single scalar \(q/s\) controlling every pair.

The theorem concerns covariance, not conditional monotonicity or stochastic association between \(K\) and \(K_r\).

The originality search was targeted. Classical finite-urn texts may contain the raw covariance formula under different notation; no whole-literature uniqueness claim is made. The sign-switch classification and its no-zero arithmetic criterion are the parts compared most closely.

## References

1. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387, first submitted 2008-09-25; later *Electronic Journal of Probability* 14 (2009), 365–384, DOI 10.1214/EJP.v14-608.
2. A. D. Barbour, “Univariate approximations in the infinite occupancy scheme,” arXiv:0902.0879, first submitted 2009-02-05.
