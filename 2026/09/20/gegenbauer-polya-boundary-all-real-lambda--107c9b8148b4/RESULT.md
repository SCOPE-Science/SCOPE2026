# Boundary positivity for the Gegenbauer Pólya integral at every real parameter

**Same-model review: passed. Independent audit: not yet performed.**

## Statement

For \(\lambda>0\), \(\delta>0\), \(n\in\mathbb N_0\), and
\(0<t\le \pi\), define
\[
F_n^{\lambda,\delta}(t)
=
\int_0^t
(t-\theta)^\delta
C_n^\lambda(\cos\theta)
(\sin\theta)^{2\lambda}\,d\theta.
\]

### Theorem

For every real \(\lambda>0\), every \(n\in\mathbb N_0\), and every
\(0<t\le\pi\),
\[
\boxed{\quad F_n^{\lambda,\lambda+1}(t)>0.\quad}
\]
Consequently,
\[
\boxed{\quad
\delta\ge \lambda+1
\ \Longrightarrow\
F_n^{\lambda,\delta}(t)>0
\quad
(\lambda>0,\ n\in\mathbb N_0,\ 0<t\le\pi).
\quad}
\]

This proves the sufficiency direction of the literal all-real-parameter
statement in Conjecture 1.4 of Beatson--zu Castell--Xu. Their conjecture was
stated for every real \(\lambda>0\), and the paper explicitly noted that this
was greater generality than needed for its sphere application. Later results
of Xu and Lu establish the sphere-relevant discrete Gegenbauer parameters;
the theorem above supplies the continuous-\(\lambda\) extension.

A useful ingredient is an explicit spherical-cap self-convolution identity
for the Gegenbauer hypergroup, valid for every real \(\lambda>0\).

## 1. Gegenbauer hypergroup and a continuous-parameter cap identity

Write
\[
W_n^\lambda(x)=\frac{C_n^\lambda(x)}{C_n^\lambda(1)}
\]
and put
\[
dm_\lambda(y)
=
a_\lambda(1-y^2)^{\lambda-\frac12}\,dy,
\qquad
a_\lambda=
\frac{\Gamma(\lambda+1)}
{\sqrt{\pi}\,\Gamma(\lambda+\frac12)}.
\]
Thus \(m_\lambda\) is a probability measure on \([-1,1]\).

For \(\lambda>0\), the Gegenbauer product formula gives the generalized
translation
\[
T_x f(y)
=
\kappa_\lambda
\int_{-1}^1
f\!\left(
xy+\sqrt{1-x^2}\sqrt{1-y^2}\,u
\right)
(1-u^2)^{\lambda-1}\,du,
\]
where
\[
\kappa_\lambda
=
\frac{\Gamma(\lambda+\frac12)}
{\sqrt{\pi}\,\Gamma(\lambda)}.
\]
It satisfies
\[
T_xW_n^\lambda(y)=W_n^\lambda(x)W_n^\lambda(y).
\]
Hence the hypergroup convolution
\[
(f*_\lambda g)(x)
=
\int_{-1}^1 f(y)T_xg(y)\,dm_\lambda(y)
\]
has multiplicative Gegenbauer transform:
\[
\widehat{f*_\lambda g}(n)=\widehat f(n)\widehat g(n).
\]

For \(0<\beta<\pi/2\), let
\[
\chi_\beta(y)=\mathbf 1_{[\cos\beta,1]}(y),
\qquad
G_{\lambda,\beta}
=
\chi_\beta *_\lambda \chi_\beta.
\]

### Lemma 1 — cap self-convolution for all real \(\lambda>0\)

For \(0\le r\le\pi\),
\[
G_{\lambda,\beta}(\cos r)
=
\frac{(\cos\beta)^{2\lambda}}{\pi}
\int_{r/2}^{\beta}
\bigl(\tan^2\beta-\tan^2 u\bigr)^\lambda\,du
\]
when \(r<2\beta\), and \(G_{\lambda,\beta}(\cos r)=0\) when
\(r\ge2\beta\).

#### Proof

Set \(x=\cos r\), \(c=\cos\beta\). In the translation integral make the
change
\[
z=xy+\sqrt{1-x^2}\sqrt{1-y^2}\,u.
\]
The discriminant
\[
\Delta=1-x^2-y^2-z^2+2xyz
\]
satisfies
\[
(1-u^2)^{\lambda-1}\,du
=
\frac{\Delta^{\lambda-1}\,dz}
{(1-x^2)^{\lambda-\frac12}
 (1-y^2)^{\lambda-\frac12}}.
\]
The \(y\)-weight in \(dm_\lambda\) cancels the last factor, so
\[
G_{\lambda,\beta}(x)
=
\frac{a_\lambda\kappa_\lambda}
{(1-x^2)^{\lambda-\frac12}}
\iint_{\substack{y,z\ge c\\ \Delta>0}}
\Delta^{\lambda-1}\,dy\,dz.
\]

Put
\[
a=\cos(r/2),\qquad s=\sin(r/2),
\qquad
y=ap+sq,\qquad z=ap-sq.
\]
Then
\[
\Delta=\sin^2r\,(1-p^2-q^2),
\qquad
|dy\,dz|=\sin r\,dp\,dq.
\]
All powers of \(\sin r\) cancel. Thus
\[
G_{\lambda,\beta}(\cos r)
=
a_\lambda\kappa_\lambda
\iint_D(1-p^2-q^2)^{\lambda-1}\,dp\,dq,
\]
where
\[
D=\{p^2+q^2<1,\ ap\pm sq\ge c\}.
\]

Use polar coordinates \(p=\rho\cos\phi\), \(q=\rho\sin\phi\).
By symmetry in \(q\), take \(q\ge0\) and double. The stronger of the two
half-plane inequalities is
\[
\rho\cos(\phi+r/2)\ge c.
\]
Hence, if \(r<2\beta\),
\[
0\le\phi\le\beta-r/2,
\qquad
\frac{c}{\cos(\phi+r/2)}\le\rho\le1.
\]
The radial integral is
\[
\int_{\rho_0}^1
\rho(1-\rho^2)^{\lambda-1}\,d\rho
=
\frac{(1-\rho_0^2)^\lambda}{2\lambda}.
\]
Since
\[
1-c^2\sec^2u
=
c^2(\tan^2\beta-\tan^2u),
\]
we get
\[
G_{\lambda,\beta}(\cos r)
=
\frac{a_\lambda\kappa_\lambda}{\lambda}
c^{2\lambda}
\int_{r/2}^{\beta}
(\tan^2\beta-\tan^2u)^\lambda\,du.
\]
Finally
\[
\frac{a_\lambda\kappa_\lambda}{\lambda}
=
\frac1\pi.
\]
If \(r\ge2\beta\), the two caps have empty hypergroup intersection and the
domain \(D\) is empty. The formula at \(r=0\) follows by continuity. \(\square\)

This identity continuously interpolates the ordinary spherical-cap
intersection formula. Its role here is that
\[
\widehat G_{\lambda,\beta}(n)
=
\widehat{\chi_\beta}(n)^2\ge0.
\]
Moreover, for \(n>0\), the standard Gegenbauer antiderivative formula gives
\[
\frac{n(2\lambda+n)}{2\lambda}
\int_{\cos\beta}^{1}
C_n^\lambda(y)(1-y^2)^{\lambda-\frac12}\,dy
=
(\sin\beta)^{2\lambda+1}
C_{n-1}^{\lambda+1}(\cos\beta).
\]
Therefore, for each fixed \(n>0\),
\(\widehat G_{\lambda,\beta}(n)\) is strictly positive except at finitely
many \(\beta\in(0,\pi/2)\). For \(n=0\) it is always positive.

## 2. Positive mixtures transfer strict coefficient positivity

Lu introduced a strong notion of positive mixture: the representing positive
measure charges every nonempty open subset of its parameter domain. Two of
the mixture facts proved there, valid for arbitrary real exponents, are used
below.

First, for \(0<\beta<\pi/2\) and \(\lambda>0\),
\[
(\beta^2-u^2)_+^\lambda
\]
is a positive mixture, in the parameter \(s\in[0,\beta]\), of
\[
(\tan^2s-\tan^2u)_+^\lambda.
\]
Indeed this is Lemma 3.3(iii) after the substitution
\(x=\tan^2u\).

Define
\[
E_{\lambda,\beta}(r)
=
\int_{r/2}^{\infty}(\beta^2-u^2)_+^\lambda\,du.
\]
Tonelli's theorem and Lemma 1 show that \(E_{\lambda,\beta}\) is a positive
mixture of the functions \(G_{\lambda,s}\), with an additional strictly
positive factor \((\cos s)^{-2\lambda}\). Consequently, its \(n\)-th
Gegenbauer coefficient is an integral of nonnegative quantities. For fixed
\(n\), those quantities vanish at only finitely many
\(s\in(0,\beta)\), while the representing measure charges every open
interval. Hence
\[
\widehat E_{\lambda,\beta}(n)>0
\qquad
(n\in\mathbb N_0,\ 0<\beta<\pi/2).
\]

Second, Lu's Lemma 3.4 with exponent parameter \(1/2\), followed by scaling,
gives a positive measure on \([0,\beta]\) such that
\[
(\beta-u)_+^\lambda
=
\int_0^\beta(s^2-u^2)_+^\lambda\,d\nu_\beta(s).
\]
Therefore
\[
P_{\lambda,\beta}(r)
:=
\int_{r/2}^{\infty}(\beta-u)_+^\lambda\,du
=
\frac{1}{\lambda+1}
(\beta-r/2)_+^{\lambda+1}
\]
is a positive mixture of \(E_{\lambda,s}(r)\). Thus every Gegenbauer
coefficient of \(P_{\lambda,\beta}\) is strictly positive for
\(0<\beta<\pi/2\).

At the endpoint \(\beta=\pi/2\), Lu's Lemma 3.3(iv) states that
\[
(\pi/2-\arctan\sqrt{x})^\lambda
\]
is a nonconstant completely monotone function on \((0,\infty)\). The
Laplace-mixture argument in the same proof represents it, for any chosen
power \(\nu>0\), as a positive mixture of \((t-x)_+^\nu\) over
\(t\in(0,\infty)\). Choose \(\nu=\lambda\), set
\(x=\tan^2u\), and write \(t=\tan^2s\). Then
\[
(\pi/2-u)^\lambda
\]
is a positive mixture of
\[
(\tan^2s-\tan^2u)_+^\lambda,
\qquad 0<s<\pi/2.
\]
After integration in \(u\), \(P_{\lambda,\pi/2}\) is therefore a positive
mixture of \(G_{\lambda,s}\) with \(0<s<\pi/2\). The same finite-zero
argument gives
\[
\widehat P_{\lambda,\pi/2}(n)>0
\qquad(n\in\mathbb N_0).
\]

## 3. Identification with the Pólya integral

Take \(t=2\beta\). Since
\[
P_{\lambda,\beta}(r)
=
\frac{2^{-(\lambda+1)}}{\lambda+1}
(t-r)_+^{\lambda+1},
\]
strict positivity of every Gegenbauer coefficient of
\(P_{\lambda,\beta}\) is exactly
\[
\int_0^t
(t-r)^{\lambda+1}
C_n^\lambda(\cos r)
(\sin r)^{2\lambda}\,dr>0,
\]
because the normalization factors \(C_n^\lambda(1)\), \(a_\lambda\), and
the squared Gegenbauer norm are all positive. This proves
\[
F_n^{\lambda,\lambda+1}(t)>0
\]
for every \(\lambda>0\), \(n\in\mathbb N_0\), and \(0<t\le\pi\).

For \(\delta>\lambda+1\), put
\[
a=\delta-\lambda-1>0.
\]
The beta identity gives, for \(0\le\theta<t\),
\[
(t-\theta)^\delta
=
\frac1{B(a,\lambda+2)}
\int_\theta^t
(t-s)^{a-1}(s-\theta)^{\lambda+1}\,ds.
\]
Fubini's theorem yields
\[
F_n^{\lambda,\delta}(t)
=
\frac1{B(a,\lambda+2)}
\int_0^t
(t-s)^{a-1}F_n^{\lambda,\lambda+1}(s)\,ds>0.
\]
This proves the stated extension to every \(\delta\ge\lambda+1\).

## Relation to the literature

Beatson, zu Castell and Xu stated Conjecture 1.4 for arbitrary real
\(\lambda>0\):
\[
F_n^{\lambda,\delta}(t)>0\ \text{for all }t\in(0,\pi]
\quad\Longleftrightarrow\quad
\delta\ge\lambda+1.
\]
They explicitly observed that the all-real-\(\lambda\) formulation was more
general than needed for their sphere application.

Xu later proved a more general Jacobi integral positivity theorem for
\(\alpha,\beta\in\mathbb N_0\). In the Gegenbauer specialization this covers
the discrete integer parameter family needed in that line of work, but its
stated hypotheses do not include arbitrary real \(\lambda>0\).

Lu subsequently proved positivity of truncated-power spectral coefficients
on ordinary spheres in all integer dimensions. This gives the corresponding
discrete spherical Gegenbauer parameters. Lu's positive-mixture lemmas,
however, are analytic statements for arbitrary real exponents. Combining
those lemmas with the continuous Gegenbauer hypergroup convolution above
removes the integer-dimensional restriction.

The present result addresses only the sufficiency direction of the literal
all-real-parameter conjecture. It does not claim the converse
\(\delta<\lambda+1\Rightarrow\) failure of positivity.

## Limitations

- The necessity direction for arbitrary real \(\lambda\) is not proved here.
- The novelty claim is specifically the continuous Gegenbauer-parameter
  extension. Several later papers describe the sphere-relevant conjecture as
  proved; their theorem statements were checked and use discrete
  integer-dimensional or integer Jacobi parameters.
- The proof imports the positive-mixture lemmas of Lu rather than reproving
  their complete-monotonicity calculations.
- A differently formulated or poorly indexed result may already contain the
  same continuous-parameter extension.
- Independent audit has not been performed.

## References

1. R. K. Beatson, W. zu Castell, Y. Xu,
   “A Pólya criterion for (strict) positive-definiteness on the sphere,”
   *IMA Journal of Numerical Analysis* 34 (2014), 550–568.
   https://doi.org/10.1093/imanum/drt008
   Preprint: https://arxiv.org/abs/1110.2437
2. R. K. Beatson, W. zu Castell,
   “Dimension hopping and families of strictly positive definite zonal basis
   functions on spheres,” *Journal of Approximation Theory* 221 (2017).
   https://doi.org/10.1016/j.jat.2017.04.001
   Preprint: https://arxiv.org/abs/1510.08658
3. Y. Xu,
   “Positive definite functions on the unit sphere and integrals of Jacobi
   polynomials,” *Proceedings of the American Mathematical Society* 146
   (2018), 2039–2048.
   https://doi.org/10.1090/proc/13913
   Preprint: https://arxiv.org/abs/1701.00787
4. T. Lu,
   “Strictly positive definite functions on spheres,”
   *Journal of Approximation Theory* 306 (2025), 106120.
   https://doi.org/10.1016/j.jat.2024.106120
