# Growing-category multinomial modes: Gaussian critical dimension and correction hierarchy

## Setting

Let
\[
X^{(N)}=(X_1,\ldots,X_m)\sim \operatorname{Mult}\!\left(N;\frac1m,\ldots,\frac1m\right),
\]
where \(m=m_N\ge2\) and \(m=o(N)\). Write
\[
N=qm+r,\qquad 0\le r<m,\qquad \theta=\frac rm.
\]
Every mode has \(r\) coordinates equal to \(q+1\) and \(m-r\) coordinates equal to \(q\). Denote the common modal point mass by
\[
P_{N,m}
=
\frac{N!}{m^N(q!)^{m-r}((q+1)!)^r}.
\]

Let \(d=m-1\), retain the first \(d\) coordinates, and let
\[
Y\sim N_d\!\left(\frac Nm\mathbf 1,\,
N\Sigma_m\right),
\qquad
\Sigma_m=\frac1m I_d-\frac1{m^2}\mathbf 1\mathbf 1^\top .
\]
For any modal vector \(k^\star\), write \(G_{N,m}\) for the Gaussian density of \(Y\) evaluated at \(k^\star_{1:d}\). Since
\[
\det\Sigma_m=m^{-m},
\qquad
\Sigma_m^{-1}=m(I_d+\mathbf1\mathbf1^\top),
\]
one obtains
\[
G_{N,m}
=
\frac{m^{m/2}}{(2\pi N)^{(m-1)/2}}
\exp\!\left[-\frac{m^2}{2N}\theta(1-\theta)\right].
\]

For \(j\ge2\), let \(B_j(x)\) be the Bernoulli polynomial, \(B_j=B_j(0)\), and define the phase polynomial
\[
A_j(\theta)
=
(1-\theta)B_j(1-\theta)
+\theta B_j(2-\theta).
\]

## Theorem 1: uniform growing-category expansion at the mode

For every fixed integer \(K\ge1\),
\[
\begin{aligned}
\log\frac{P_{N,m}}{G_{N,m}}
={}&-\frac{m^2-1}{12N}\\
&+\sum_{k=2}^{K}
\frac{(-1)^{k+1}}{k(k+1)N^k}
\left[
B_{k+1}-m^{k+1}A_{k+1}(\theta)
\right]\\
&+O_K\!\left(\frac{m^{K+2}}{N^{K+1}}\right),
\end{aligned}
\]
uniformly in the lattice phase \(\theta\in[0,1)\).

In particular,
\[
\log\frac{P_{N,m}}{G_{N,m}}
=
-\frac{m^2-1}{12N}
+
\frac{m^3}{12N^2}
\theta(1-\theta)(5-4\theta)
+
O\!\left(\frac{m^4}{N^3}\right).
\]

### Critical dimension

If
\[
\frac{m^2}{N}\longrightarrow c\in[0,\infty),
\]
then
\[
\boxed{\frac{P_{N,m}}{G_{N,m}}\longrightarrow e^{-c/12}.}
\]
If instead \(m^2/N\to\infty\) while \(m=o(N)\), then
\[
\log(P_{N,m}/G_{N,m})
\sim-\frac{m^2}{12N},
\qquad
P_{N,m}/G_{N,m}\to0.
\]

Consequently, within the regime \(m=o(N)\), the ordinary Gaussian local approximation is relatively accurate at the multinomial mode,
\[
P_{N,m}/G_{N,m}\to1,
\]
if and only if
\[
\boxed{m=o(\sqrt N).}
\]
At the critical scale \(m\sim a\sqrt N\), the Gaussian density misses the modal mass by the non-vanishing factor \(e^{-a^2/12}\).

## Theorem 2: an explicit correction hierarchy

Define
\[
\mathcal G^{[1]}_{N,m}
=
G_{N,m}\exp\!\left[-\frac{m^2-1}{12N}\right],
\]
and, for \(K\ge2\),
\[
\mathcal G^{[K]}_{N,m}
=
G_{N,m}
\exp\!\left[
-\frac{m^2-1}{12N}
+
\sum_{k=2}^{K}
\frac{(-1)^{k+1}}{k(k+1)N^k}
\left(
B_{k+1}-m^{k+1}A_{k+1}(\theta)
\right)
\right].
\]
Then
\[
\log\frac{P_{N,m}}{\mathcal G^{[K]}_{N,m}}
=
O_K\!\left(\frac{m^{K+2}}{N^{K+1}}\right).
\]
Hence
\[
\boxed{
\frac{P_{N,m}}{\mathcal G^{[K]}_{N,m}}\to1
\quad\text{whenever}\quad
m=o\!\left(N^{(K+1)/(K+2)}\right).
}
\]

The dimension exponents are genuine transition scales. If
\[
\frac{m}{N^{(K+1)/(K+2)}}\to a\in(0,\infty),
\qquad
\theta\to\theta_0,
\]
then, after retaining one further term in Theorem 1,
\[
\log\frac{P_{N,m}}{\mathcal G^{[K]}_{N,m}}
\longrightarrow
\frac{(-1)^{K+3}a^{K+2}}
{(K+1)(K+2)}
A_{K+2}(\theta_0).
\]
Thus the threshold \(N^{(K+1)/(K+2)}\) is sharp for every phase with
\(A_{K+2}(\theta_0)\ne0\).

For example, the single universal factor
\[
\exp[-(m^2-1)/(12N)]
\]
extends modal relative accuracy from \(m=o(N^{1/2})\) to
\(m=o(N^{2/3})\). At the \(N^{2/3}\) scale the remaining distortion is explicitly phase-dependent:
\[
\log\frac{P_{N,m}}{\mathcal G^{[1]}_{N,m}}
\to
\frac{a^3}{12}\theta_0(1-\theta_0)(5-4\theta_0).
\]

## Theorem 3: the critical continuity-correction profile

Let
\[
C_{N,m}
=
\Pr\!\left\{
Y\in
k^\star_{1:d}+[-1/2,1/2]^d
\right\},
\]
the multivariate Gaussian probability of the standard unit lattice cell centered at a mode.

If \(m\to\infty\) and
\[
\frac{m^2}{N}\to c\in[0,\infty),
\]
then
\[
\boxed{
\frac{C_{N,m}}{G_{N,m}}
\longrightarrow
e^{-c/24}(1+c/12)^{-1/2}.
}
\]
Combining this with Theorem 1 gives
\[
\boxed{
\frac{P_{N,m}}{C_{N,m}}
\longrightarrow
\sqrt{1+c/12}\,e^{-c/24}.
}
\]

For every \(c>0\) the last factor is strictly below \(1\), so the usual unit-cell continuity correction does not restore exact relative accuracy at the critical dimension. It does, however, cancel the first-order critical distortion:
\[
\log\frac{P_{N,m}}{C_{N,m}}
=
\frac12\log(1+c/12)-\frac c{24}
=
-\frac{c^2}{576}+O(c^3)
\qquad(c\downarrow0),
\]
whereas
\[
\log(P_{N,m}/G_{N,m})=-c/12+o(1).
\]

## Proof

### 1. Uniform shifted-Gamma expansion

For fixed \(K\) and \(a\) in a compact interval,
\[
\log\Gamma(z+a)
=
\left(z+a-\frac12\right)\log z-z+\frac12\log(2\pi)
+
\sum_{k=1}^{K}
\frac{(-1)^{k+1}B_{k+1}(a)}
{k(k+1)z^k}
+
O_K(z^{-K-1}),
\]
uniformly as \(z\to\infty\).

For a mode write
\[
k_i^\star=\frac Nm+t_i,
\]
where exactly \(m-r\) offsets are \(-\theta\), exactly \(r\) offsets are \(1-\theta\), and
\[
\sum_i t_i=0.
\]
Apply the shifted-Gamma expansion to
\[
\log P_{N,m}
=
\log\Gamma(N+1)
-\sum_{i=1}^m\log\Gamma(N/m+t_i+1)
-N\log m.
\]
The leading terms combine to
\[
\frac m2\log m-\frac{m-1}{2}\log(2\pi N).
\]
For the \(N^{-k}\) term, the numerator contributes \(B_{k+1}\), while the \(m\) denominator terms contribute
\[
m^k\sum_{i=1}^mB_{k+1}(t_i+1)
=
m^{k+1}A_{k+1}(\theta).
\]
The summed remainder is
\[
O_K\!\left(
N^{-K-1}
+
m(N/m)^{-K-1}
\right)
=
O_K(m^{K+2}/N^{K+1}).
\]

At \(k=1\),
\[
A_2(\theta)=\frac16+\theta(1-\theta),
\]
so
\[
\frac{1}{2N}\left[B_2-m^2A_2(\theta)\right]
=
-\frac{m^2-1}{12N}
-\frac{m^2}{2N}\theta(1-\theta).
\]
The last term is exactly the Gaussian Mahalanobis exponent in
\(G_{N,m}\), proving Theorem 1. Also,
\[
A_3(\theta)
=
\frac12\theta(1-\theta)(5-4\theta),
\]
which yields the displayed two-term formula.

Since every subsequent term is smaller than \(m^2/N\) by at least a factor \(m/N=o(1)\), Theorem 1 also gives
\[
\log(P_{N,m}/G_{N,m})
=
-\frac{m^2}{12N}(1+o(1))
\]
whenever \(m^2/N\to\infty\). The finite-\(c\) limit and the
\(m=o(\sqrt N)\) criterion follow immediately.

Keeping \(K\) terms gives Theorem 2. To obtain its critical profile, apply the same expansion through order \(K+1\). The next remainder is
\[
O_K(m^{K+3}/N^{K+2})=o(1)
\]
at \(m\asymp N^{(K+1)/(K+2)}\), while the \((K+1)\)-st omitted term converges to the displayed Bernoulli-polynomial constant.

### 2. Gaussian unit-cell limit

Let \(t=k^\star_{1:d}-(N/m)\mathbf1\), and let
\(U_1,\ldots,U_d\) be independent \(\operatorname{Unif}[-1/2,1/2]\). Dividing the Gaussian cell integral by the Gaussian density at its center gives
\[
\frac{C_{N,m}}{G_{N,m}}
=
\mathbb E\exp\!\left[
-\frac1N t^\top\Sigma_m^{-1}U
-\frac1{2N}U^\top\Sigma_m^{-1}U
\right].
\]

Let \(t_m=-\sum_{i=1}^d t_i\) denote the omitted coordinate. Since
\(\Sigma_m^{-1}=m(I+\mathbf1\mathbf1^\top)\),
\[
t^\top\Sigma_m^{-1}U
=
m\sum_{i=1}^d(t_i-t_m)U_i.
\]
Each coefficient \(t_i-t_m\) has absolute value at most one, and hence
\[
\operatorname{Var}\!\left(
\frac1N t^\top\Sigma_m^{-1}U
\right)
\le
\frac{m^3}{12N^2}
\to0
\]
when \(m^2/N\to c<\infty\).

For the quadratic term,
\[
U^\top\Sigma_m^{-1}U
=
m\left[
\sum_{i=1}^dU_i^2+
\left(\sum_{i=1}^dU_i\right)^2
\right].
\]
The law of large numbers and central limit theorem yield
\[
\frac1m\sum_{i=1}^dU_i^2\to\frac1{12},
\qquad
\frac1{\sqrt m}\sum_{i=1}^dU_i
\Longrightarrow N(0,1/12).
\]
Therefore
\[
\frac1{2N}U^\top\Sigma_m^{-1}U
\Longrightarrow
\frac c{24}(1+Z^2),
\qquad Z\sim N(0,1).
\]
The exponentials are uniformly bounded when \(m^2/N\) is bounded, so dominated convergence applies. Thus
\[
\frac{C_{N,m}}{G_{N,m}}
\to
e^{-c/24}\,
\mathbb E e^{-(c/24)Z^2}
=
e^{-c/24}(1+c/12)^{-1/2}.
\]
This proves Theorem 3.

## Relation to prior work

Elezović (2026) gives the exact multinomial mode criterion and a complete Bernoulli-polynomial local expansion for a fixed multinomial probability vector, explicitly recovering the symmetric central multinomial coefficient. The present result isolates the equiprobable case but lets the number of categories grow with \(N\), supplies a remainder uniform in the lattice phase, and converts the coefficient growth into explicit dimension-transition laws.

Ouimet (2021) proves a precise multinomial local limit theorem and derives normal-comparison results using jittering by a unit cube. Its local asymptotic notation allows constants depending on the fixed dimension and probability vector; it does not give the growing-category modal critical profile above. The paper also identifies finely tuned continuity corrections as a potential application. Theorem 3 evaluates the standard unit-cell correction in the simultaneous \(m^2/N\to c\) regime.

Katsevich (2025) proves that a sample-size condition of order \(N\gg d^2\) suffices for a high-dimensional Bernstein--von Mises theorem in multinomial models. That is a posterior total-variation problem rather than a local lattice-mass theorem, but it makes the square-dimension scale independently relevant. Here the same scale emerges as an exact transition for relative Gaussian accuracy at the equiprobable modal point.

Classical asymptotic expansions for sums of lattice random vectors and elementary Stirling expansions of central multinomial coefficients contain ingredients that recover special cases. In particular, when \(m\mid N\), the first correction \(-(m^2-1)/(12N)\) is already visible from the factorial ratio. The contribution here is the growing-category uniform expansion at arbitrary modal lattice phase, its correction hierarchy and critical exponents, and the explicit Gaussian-cell profile.

## Limitations

- The theorem treats the equiprobable multinomial distribution. Unequal cell probabilities with a growing number of categories are not covered.
- The result is local at modal lattice points. It does not assert a sharp global total-variation, Le Cam, or convex-set approximation threshold.
- The assumption \(m=o(N)\) keeps every expected cell count \(N/m\) divergent. Sparse occupancy regimes with bounded expected cell counts require different asymptotics.
- The continuity-correction formula is proved for the standard unit cube in the first \(m-1\) coordinates. Other lattice cells or optimized multidimensional corrections may have different critical profiles.
- Originality is to the best of our knowledge. Older multidimensional lattice-expansion and central-multinomial literature could contain equivalent special cases under different notation.

## References

1. N. Elezović, "Multinomial probabilities near the mode: integer modes and the complete local expansion", arXiv:2609.20229 (2026). https://arxiv.org/abs/2609.20229
2. F. Ouimet, "A precise local limit theorem for the multinomial distribution and some applications", Journal of Statistical Planning and Inference 215 (2021), 218-233. https://doi.org/10.1016/j.jspi.2021.03.006
3. A. Bikyalis, "Asymptotic Expansions for Distributions of Sums of Identically Distributed Independent Lattice Random Variables", Theory of Probability and Its Applications 14 (1969). https://doi.org/10.1137/1114060
4. A. Katsevich, "Improved dimension dependence in the Bernstein--von Mises theorem via a new Laplace approximation bound", Information and Inference 14(3) (2025), iaaf020. https://doi.org/10.1093/imaiai/iaaf020
