# Ewens frequency counts switch covariance sign at a macroscopic threshold

## Finding

Fix
\[
\theta>0.
\]
Let a random permutation of \([n]\) have Ewens probability proportional to
\[
\theta^{K_n},
\]
where \(K_n\) is its total number of cycles. Let
\[
A_{n,r}
\]
be the number of cycles of length \(r\), for \(1\le r\le n\).

Equivalently, under the Ewens sampling formula in population genetics, \(K_n\) is the total number of observed allelic types and \(A_{n,r}\) is the number of types represented exactly \(r\) times.

For every measurable function \(f\) for which the displayed expectations exist, size-biasing by the number of \(r\)-cycles gives the exact Palm identity
\[
\boxed{
\frac{\mathbb E[A_{n,r}f(K_n)]}{\mathbb E A_{n,r}}
=
\mathbb E f(1+K_{n-r}).
}
\tag{1}
\]
Here the variable on the right has the Ewens law with the same parameter \(\theta\) on \(S_{n-r}\).

The normalizing mean is
\[
\boxed{
\mathbb E A_{n,r}
=
\frac{\theta}{r}
\frac{n!}{(n-r)!}
\frac{\Gamma(\theta+n-r)}{\Gamma(\theta+n)}.
}
\tag{2}
\]

Write
\[
\mu_m
=
\mathbb E K_m
=
\sum_{i=0}^{m-1}\frac{\theta}{\theta+i},
\qquad
\mu_0=0.
\]
Then
\[
\boxed{
\operatorname{Cov}(K_n,A_{n,r})
=
\mathbb E A_{n,r}
\left(
1+\mu_{n-r}-\mu_n
\right).
}
\tag{3}
\]
Equivalently,
\[
\boxed{
\operatorname{Cov}(K_n,A_{n,r})
=
\mathbb E A_{n,r}
\left(
1-
\sum_{i=n-r}^{n-1}
\frac{\theta}{\theta+i}
\right).
}
\tag{4}
\]

The sign changes exactly once as the component size increases. Define
\[
t_n
=
\min
\left\{
1\le r\le n:
1+\mu_{n-r}-\mu_n\le0
\right\}.
\tag{5}
\]
For every \(n\ge2\),
\[
\boxed{
\operatorname{Cov}(K_n,A_{n,r})>0
\quad\text{for }r<t_n,
}
\tag{6}
\]
\[
\boxed{
\operatorname{Cov}(K_n,A_{n,t_n})\le0,
}
\tag{7}
\]
and
\[
\boxed{
\operatorname{Cov}(K_n,A_{n,r})<0
\quad\text{for }r>t_n.
}
\tag{8}
\]

The threshold is macroscopic:
\[
\boxed{
\frac{t_n}{n}
\longrightarrow
1-e^{-1/\theta}.
}
\tag{9}
\]
Thus, for the uniform-permutation case \(\theta=1\), the transition occurs asymptotically at
\[
1-e^{-1}
\]
of the sample size.

More precisely, if
\[
\frac{r_n}{n}\longrightarrow x\in(0,1),
\]
then
\[
\boxed{
 n\operatorname{Cov}(K_n,A_{n,r_n})
\longrightarrow
\frac{\theta}{x}(1-x)^{\theta-1}
\left(1+\theta\log(1-x)\right).
}
\tag{10}
\]
The limiting profile is positive for
\[
0<x<1-e^{-1/\theta},
\]
zero at the threshold, and negative above it.

In allele-frequency language, types represented by a small fraction of the sample covary positively with total allelic richness, while sufficiently macroscopic types covary negatively with richness. The sign boundary depends only on the Ewens parameter.

## Assumptions and scope

The theorem uses the classical Ewens measure with a fixed parameter \(\theta>0\). No approximation is used in the finite identities.

The statistic \(A_{n,r}\) counts cycles of exactly one size. The Palm identity is stronger than the covariance formula because it determines every mixed expectation with one size-biased factor \(A_{n,r}\).

The population-genetic interpretation is the usual Ewens sampling formula: the cycle-size multiplicity vector and the allelic occupancy multiplicity vector have the same distribution.

Equation (10) assumes a sequence of integer sizes \(r_n\) satisfying \(r_n/n\to x\in(0,1)\). It does not describe boundary regimes with \(r_n=o(n)\) or \(n-r_n=o(n)\).

## Proof

Under the Ewens law,
\[
\Pr(\pi)
=
\frac{\theta^{K(\pi)}}{\theta^{(n)}},
\qquad
\theta^{(n)}
=
\theta(\theta+1)\cdots(\theta+n-1).
\tag{11}
\]

Consider pairs \((\pi,C)\), where \(\pi\in S_n\) and \(C\) is one distinguished \(r\)-cycle of \(\pi\). Choose the \(r\) labels of \(C\), arrange them into a cycle in \((r-1)!\) ways, and let \(\sigma\in S_{n-r}\) be the permutation on the remaining labels.

The marked cycle contributes one cycle and one factor of \(\theta\). Therefore
\[
\begin{aligned}
\mathbb E[A_{n,r}f(K_n)]
&=
\frac{\binom nr(r-1)!\theta}{\theta^{(n)}}
\sum_{\sigma\in S_{n-r}}
\theta^{K(\sigma)}f(1+K(\sigma))\\
&=
\binom nr(r-1)!\theta
\frac{\theta^{(n-r)}}{\theta^{(n)}}
\mathbb E f(1+K_{n-r}).
\end{aligned}
\tag{12}
\]
Setting \(f=1\) gives
\[
\mathbb E A_{n,r}
=
\binom nr(r-1)!\theta
\frac{\theta^{(n-r)}}{\theta^{(n)}},
\tag{13}
\]
which is exactly (2) after writing rising factorials with gamma functions. Dividing (12) by (13) proves (1).

The standard Chinese-restaurant recursion gives
\[
K_m
\overset d=
\sum_{i=0}^{m-1}B_i,
\qquad
B_i\sim\operatorname{Bernoulli}\left(\frac{\theta}{\theta+i}\right),
\]
with independent summands. Hence
\[
\mu_m
=
\sum_{i=0}^{m-1}\frac{\theta}{\theta+i}.
\tag{14}
\]
Taking \(f(k)=k\) in (1) gives
\[
\mathbb E[K_nA_{n,r}]
=
\mathbb E A_{n,r}(1+\mu_{n-r}).
\]
Subtracting \(\mu_n\mathbb E A_{n,r}\) proves (3)--(4).

Put
\[
c_n(r)
=
1-
\sum_{i=n-r}^{n-1}\frac{\theta}{\theta+i}.
\tag{15}
\]
As \(r\) increases by one, exactly one positive summand is added to the sum, so \(c_n(r)\) decreases strictly. Also
\[
c_n(1)
=
1-
\frac{\theta}{\theta+n-1}
>0
\]
for \(n\ge2\), while
\[
c_n(n)
=
1-
\sum_{i=0}^{n-1}\frac{\theta}{\theta+i}
<0.
\]
This proves existence and uniqueness of the sign transition and yields (6)--(8).

Now suppose
\[
\frac{r_n}{n}\to x\in(0,1).
\]
The harmonic tail is a Riemann sum:
\[
\sum_{i=n-r_n}^{n-1}\frac{\theta}{\theta+i}
=
\frac{\theta}{n}
\sum_{i=n-r_n}^{n-1}
\frac{1}{i/n+\theta/n}
\longrightarrow
\theta\int_{1-x}^{1}\frac{du}{u}
=
-\theta\log(1-x).
\tag{16}
\]
Therefore
\[
c_n(r_n)
\longrightarrow
1+\theta\log(1-x).
\tag{17}
\]
The unique zero of the limiting function is
\[
x_\theta
=
1-e^{-1/\theta}.
\]
Strict monotonicity of \(c_n\), evaluated at any two fixed fractions on opposite sides of \(x_\theta\), now proves (9).

Finally, (2) can be written
\[
\mathbb E A_{n,r}
=
\frac{\theta}{r}
\frac{\Gamma(n+1)}{\Gamma(n-r+1)}
\frac{\Gamma(\theta+n-r)}{\Gamma(\theta+n)}.
\tag{18}
\]
If \(r_n/n\to x\in(0,1)\), the standard gamma-ratio asymptotic gives
\[
n\mathbb E A_{n,r_n}
\longrightarrow
\frac{\theta}{x}(1-x)^{\theta-1}.
\tag{19}
\]
Multiplying (17) and (19) proves (10).

## Verification

The accompanying checker exhaustively enumerates permutations through order \(7\) for several rational Ewens parameters. It verifies the normalizing mean (2), the Palm identity (1) for several test functions, and the covariance formula (3) for every admissible cycle length.

A separate exact-rational loop checks strict monotonicity and finite sign thresholds from the harmonic bracket. Numerical large-\(n\) checks confirm the threshold ratios for several \(\theta\) values and the macroscopic covariance profile in (10).

Finite computation is supplementary. The theorem for arbitrary \(n\) and \(\theta>0\) is proved by the marked-cycle bijection and the harmonic-tail argument above.

## Relationship to prior work

Bakšajeva and Manstavičius give the Ewens cycle-structure distribution explicitly, classify additive functions built from cycle counts, and analyze the number of cycles with restricted lengths. Their full public text records the conditioned-Poisson representation and treats the total number of cycles in detail. The inspected text does not state a covariance between total cycle count and one size-class count, nor a one-switch sign law across cycle size.

Lugo gives exact joint factorial moments of fixed cycle-size counts for uniform permutations and develops limiting laws for cycles whose lengths are proportional to \(n\). This directly covers the macroscopic cycle-length scale appearing in (9)--(10), but the inspected full text does not introduce the total cycle count as the paired statistic or state the covariance sign threshold.

Hoppe studies size-biased filtering of Poisson--Dirichlet samples and identifies a characteristic size-biased property of the Ewens sampling formula. The accessible abstract is closely related in spirit, but it does not expose enough detail to determine whether the finite marked-\(r\)-cycle identity (1) appears there. That source is therefore retained as a residual originality risk rather than treated as non-covering.

The accepted contribution is the finite Palm identity specialized to one frequency class together with its exact covariance consequence, strict one-switch sign geometry, and macroscopic threshold/profile.

## Limitations

The size-biased identity is elementary once a marked cycle is introduced. An equivalent formula may exist implicitly in older generating-function or population-genetic treatments of the Ewens sampling formula.

The sign transition is for covariance with total richness. It does not imply stochastic monotonicity of \(A_{n,r}\) conditional on \(K_n\).

For generalized weighted permutation measures that are not Ewens, deleting a marked cycle need not leave the same law on the complement, so (1) can fail.

## References

1. T. Bakšajeva and E. Manstavičius, “On statistics of permutations chosen from the Ewens distribution,” arXiv:1303.4540, first submitted 2013-03-19; later *Combinatorics, Probability and Computing* 23 (2014), 889–913, DOI 10.1017/S0963548314000376.
2. M. Lugo, “The number of cycles of specified normalized length in permutations,” arXiv:0909.2909, first submitted 2009-09-16.
3. F. M. Hoppe, “Size-biased filtering of Poisson–Dirichlet samples with an application to partition structures in genetics,” *Journal of Applied Probability* 23 (1986), 1008–1012, DOI 10.2307/3214473.
4. R. Arratia, A. D. Barbour, and S. Tavaré, *Logarithmic Combinatorial Structures: A Probabilistic Approach*, EMS, 2003.
