# Universal extremal rigidity for monotone weighted Fock Korenblum radii

## Finding

Let \(W\ge0\) be a nonzero non-increasing radial weight on \([0,\infty)\), with all moments
\[
m_k
=
\int_0^\infty t^kW(t)\,dt
\]
finite. Let
\[
F_W^2
=
\left\{
f\text{ entire}:
\|f\|_W<\infty
\right\},
\]
where
\[
\|f\|_W^2
=
\frac1\pi
\int_{\mathbb C}
|f(z)|^2W(|z|^2)\,dA(z).
\]
Put
\[
R_W
=
\sqrt{\frac{m_1}{m_0}}.
\]

The sharp Korenblum theorem for non-increasing radial weights says that
\[
|f(z)|\le|g(z)|
\qquad
(|z|>R_W)
\]
implies
\[
\|f\|_W\le\|g\|_W.
\]

The equality cases are exactly the following.

Either
\[
f=\eta g,
\qquad
|\eta|=1,
\]
or there are parameters
\[
c\in\mathbb C\setminus\{0\},
\qquad
|\eta|=1,
\qquad
|a|<1,
\]
such that
\[
f(z)
=
c(\eta R_W+az),
\qquad
g(z)
=
c(z+\overline a\,\eta R_W).
\]

Thus the extremal family has the same linear Möbius form for every non-increasing radial weight. The weight enters only through its sharp radius \(R_W\).

## Assumptions and scope

A radial weight is measurable, nonnegative, not almost everywhere zero, and has all moments finite.

The proof uses the sharp-radius theorem for non-increasing weights and its moment-duality construction. No smoothness or strict monotonicity of \(W\) is assumed.

The result concerns equality at the sharp radius \(R_W\). It does not classify equality for arbitrary smaller domination radii, nor does it address radial weights outside the non-increasing class when the exact Korenblum radius is unknown.

## Proof

Multiplying \(W\) by a positive constant does not alter the problem, so normalize
\[
m_0=1.
\]
Set
\[
s=m_1,
\qquad
R_W=\sqrt s.
\]

Write
\[
f(z)=\sum_{k\ge0}a_kz^k,
\qquad
g(z)=\sum_{k\ge0}b_kz^k,
\]
and define
\[
d_k
=
|a_k|^2-|b_k|^2,
\]
\[
x_k=(d_k)_+,
\qquad
y_k=(-d_k)_+,
\]
together with
\[
X(t)=\sum_{k\ge0}x_kt^k,
\qquad
Y(t)=\sum_{k\ge0}y_kt^k.
\]

The sharp-radius proof for non-increasing \(W\) takes a random variable \(T\) with density \(W\) and uses the probability law
\[
\nu
=
\operatorname{Law}(\max(T,s))
\]
in the moment-duality theorem. The Schwarz--Pick coefficient estimate gives
\[
X(t)
\le
\frac{s}{t}Y(t)
\qquad
(t\ge s).
\]
The moment inequalities for \(\nu\) then give the chain
\[
\sum_kx_km_k
\le
\int X(t)\,d\nu(t)
\le
\int\frac{s}{t}Y(t)\,d\nu(t)
\le
\sum_ky_km_k.
\]

Assume now
\[
\|f\|_W=\|g\|_W.
\]
Then
\[
\sum_kx_km_k
=
\sum_ky_km_k,
\]
so every inequality in the displayed chain is an equality.

If \(X=Y=0\), the circular means of \(|f|^2\) and \(|g|^2\) agree on every circle. Since \(|f|\le|g|\) in the exterior region, equality of the circular integrals forces
\[
|f|=|g|
\]
there. Hence \(f/g\) is a unimodular constant and the first equality family follows.

Assume from now on that the quotient is nonconstant. The function
\[
\frac{s}{t}Y(t)-X(t)
\]
is nonnegative for \(t\ge s\), and its integral against \(\nu\) is zero.

The distribution of \(T\) is not a point mass because it has an absolutely continuous density. Its mean \(s\) is therefore strictly smaller than its essential supremum. Since \(W\) is non-increasing, there is an interval
\[
(s,b)
\]
on which \(W\) is positive almost everywhere. On that interval \(\nu\) has positive density. Thus
\[
sY(t)-tX(t)=0
\]
on a set with an accumulation point.

Both \(X\) and \(Y\) are entire functions of \(t\), so the identity theorem yields
\[
tX(t)=sY(t)
\]
identically.

The Schwarz--Pick estimate used in the source has the more precise form
\[
(1-|\alpha|^2)Y(r^2)
\le
M_2(r,g-\overline\alpha f)^2
\le
(1-|\alpha|^2)
\frac{r^2}{r^2-s}
\left(
Y(r^2)-X(r^2)
\right),
\]
where
\[
\alpha
=
\left(\frac fg\right)(\infty)
\in\mathbb D.
\]
The identity
\[
r^2X(r^2)=sY(r^2)
\]
makes the first and last quantities equal. Hence equality holds in the integrated pointwise Schwarz--Pick inequality on every circle
\[
|z|=r>\sqrt s.
\]

The pointwise defect is continuous and nonnegative. Its circle integral vanishes, so the Schwarz--Pick estimate itself is an equality. Equality in Schwarz--Pick at one nonzero point forces the transformed quotient to be a disk automorphism. Consequently
\[
\frac{f(z)}{g(z)}
=
\frac{az+\eta R_W}
{z+\overline a\,\eta R_W}
\]
for some
\[
|a|<1,
\qquad
|\eta|=1.
\]

Since \(f\) and \(g\) are entire, there is an entire function \(h\) such that
\[
g(z)
=
(z+\overline a\,\eta R_W)h(z),
\]
\[
f(z)
=
(az+\eta R_W)h(z).
\]

Write
\[
h(z)
=
\sum_{j\ge0}c_jz^j.
\]
Radial orthogonality of monomials gives the exact identity
\[
\|g\|_W^2-\|f\|_W^2
=
(1-|a|^2)
\sum_{j\ge0}
|c_j|^2
\left(
m_{j+1}-R_W^2m_j
\right).
\]

The term \(j=0\) is zero because
\[
R_W^2m_0=m_1.
\]
For \(j\ge1\), with \(T\) distributed according to the normalized density \(W\),
\[
m_{j+1}-m_1m_j
=
\operatorname{Cov}(T,T^j).
\]
If \(T'\) is an independent copy, then
\[
\operatorname{Cov}(T,T^j)
=
\frac12
\mathbb E
\left[
(T-T')
(T^j-T'^j)
\right].
\]
The integrand is nonnegative and is strictly positive with positive probability because \(T\) is nondegenerate. Hence
\[
m_{j+1}-m_1m_j>0
\qquad
(j\ge1).
\]

Therefore equality of norms forces
\[
c_j=0
\qquad
(j\ge1),
\]
so \(h\) is constant. This gives precisely
\[
f(z)=c(\eta R_W+az),
\qquad
g(z)=c(z+\overline a\,\eta R_W).
\]

Conversely, for every such pair,
\[
|g(z)|^2-|f(z)|^2
=
|c|^2(1-|a|^2)
\left(
|z|^2-R_W^2
\right).
\]
Thus
\[
|f(z)|\le|g(z)|
\]
for \(|z|\ge R_W\), and
\[
\|g\|_W^2-\|f\|_W^2
=
|c|^2(1-|a|^2)
\left(
m_1-R_W^2m_0
\right)
=
0.
\]
This proves both necessity and sufficiency.

## Verification

The primary source was inspected through the definition of \(F_W^2\), the coefficient identity for radial norms, the Schwarz--Pick estimate at infinity, the moment-duality theorem, the proof of the sharp radius for non-increasing weights, and its equality discussion for the standard Fock space.

The new step is equality propagation in the non-increasing-weight moment measure. The measure used by the source has continuous mass immediately above its mean, so equality of the moment-duality endpoints forces equality in the Schwarz--Pick coefficient estimate on an interval. Analytic continuation then makes that equality global in the auxiliary radius variable.

The final linearity step is independent of the detailed weight. After the quotient becomes Möbius, the norm difference is an exact positive diagonal sum. Strict positivity of the higher coefficients follows from the elementary covariance identity
\[
2\operatorname{Cov}(T,T^j)
=
\mathbb E
\left[
(T-T')
(T^j-T'^j)
\right].
\]

No numerical computation, finite sampling, or unproved limiting assertion is used.

## Relationship to prior work

Wikström's 2026 paper determines the sharp Korenblum radius
\[
R_W=\sqrt{m_1/m_0}
\]
for every non-increasing radial weight. It gives a complete equality classification for the standard Gaussian Fock space, but the weighted theorem itself states the optimal radius and admissibility rather than a complete equality classification for every monotone weight.

Wee and Le's earlier weighted-Fock work derives explicit upper bounds from elementary probe pairs for several weighted Fock families. The new sharp-radius theorem shows those bounds are attained in the Hilbert case. Their published scope is upper-bound determination rather than classification of all equality pairs.

The present finding shows that the standard-Fock extremal geometry is universal across the entire non-increasing radial class: after replacing the unit radius by \(R_W\), no new nonlinear equality pairs occur.

This applies, for example, to all weights
\[
W(t)=e^{-t^{m/2}},
\qquad
m>0,
\]
and to the decreasing gamma-type weights
\[
W(t)=t^\beta e^{-\alpha t},
\qquad
-1<\beta\le0.
\]

Targeted searches for weighted-Fock Korenblum equality cases, extremal pairs, Möbius extremizers, and the exact source identifier did not locate a published statement with this full equality classification.

## Limitations

The proof uses the particular moment measure available for non-increasing radial weights. It does not establish the same classification for arbitrary radial weights for which the sharp radius is unknown.

The result is a Hilbert-space statement. No equality classification is asserted for \(F_W^p\) when \(p\ne2\).

The theorem classifies exact equality only; it does not provide a quantitative stability estimate for near-extremizers.

## References

1. F. Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622v1, 2026.
2. J. Wee and H. K. Le, *Korenblum constants for some function spaces*, Proceedings of the American Mathematical Society 148 (2020), 1175--1185. DOI: 10.1090/proc/14778.
3. J. Wee and H. K. Le, *Korenblum constants for various weighted Fock spaces*, Complex Variables and Elliptic Equations 68 (2023), 1385--1406. DOI: 10.1080/17476933.2022.2052862.
4. I. Efraimidis, A. Llinares and D. Vukotić, *Korenblum's Principle for Bergman Spaces with Radial Weights*, Computational Methods and Function Theory 25 (2025), 239--250. DOI: 10.1007/s40315-024-00543-6.
