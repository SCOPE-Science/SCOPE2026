# An Apéry correction at the large-shape Weibull one-sigma endpoint
## Finding
Let \(X_{k,\lambda}\) have Weibull distribution
\[
\Pr\{X_{k,\lambda}\le x\}=1-\exp\!\left[-(x/\lambda)^k\right],\qquad x\ge0,
\]
with \(k>0\) and \(\lambda>0\). Define the scale-free one-standard-deviation central mass
\[
C_k=
\Pr\!\left\{
\left|X_{k,\lambda}-\mathbb E X_{k,\lambda}\right|
\le
\sqrt{\operatorname{Var}(X_{k,\lambda})}\right\}.
\]
Put
\[
a=\frac{\pi}{\sqrt6},\qquad
u_-=e^{-\gamma-a},\qquad
u_+=e^{-\gamma+a},
\]
where \(\gamma\) is Euler's constant. Then
\[
C_k=C_\infty-\frac{A}{k}+O(k^{-2})
\qquad (k\to\infty),
\]
with
\[
C_\infty=e^{-u_-}-e^{-u_+}
=0.7237512675197103\ldots
\]
and
\[
A=
\frac{\zeta(3)}{a}
\left(u_-e^{-u_-}+u_+e^{-u_+}\right)
=
0.3754669303473501\ldots>0.
\]
Thus the standardized Weibull one-sigma central mass approaches its reflected-Gumbel endpoint from below. In particular, because
\[
C_\infty>2\Phi(1)-1=0.6826894921370859\ldots,
\]
there exists a finite \(K\) such that
\[
C_k>2\Phi(1)-1
\]
for every \(k\ge K\).

## Assumptions and scope
The parameterization is the scale Weibull law
\[
F_{k,\lambda}(x)=1-\exp\!\left[-(x/\lambda)^k\right].
\]
The central probability is invariant under positive rescaling, so \(\lambda\) plays no role and may be set to \(1\). The theorem is an asymptotic statement as the shape \(k\) tends to infinity. It does not identify the smallest finite \(k\) at which the Gaussian comparison is restored, nor does it assert monotonicity of \(C_k\) over the entire range \(k>1\).

## Proof
Set
\[
r=\frac1k
\]
and, after taking \(\lambda=1\), write
\[
X=e^{rY},
\]
where \(E=e^Y\) has the unit exponential law. Hence
\[
\Pr\{Y\le y\}=1-e^{-e^y},
\]
so \(Y\) is a reflected Gumbel variable. Its exponential moments are
\[
\mathbb E e^{tY}=\Gamma(1+t),\qquad t>-1.
\]
The expansion
\[
\log\Gamma(1+t)
=
-\gamma t+\frac{\zeta(2)}2t^2-\frac{\zeta(3)}3t^3+O(t^4)
\]
shows that \(Y\) has
\[
\mu=-\gamma,\qquad
v=\zeta(2)=\frac{\pi^2}{6}=a^2,\qquad
\kappa_3=-2\zeta(3).
\]

Let
\[
m_r=\mathbb E X=\Gamma(1+r)
\]
and
\[
s_r^2=\operatorname{Var}(X)
=\Gamma(1+2r)-\Gamma(1+r)^2.
\]
Expanding the moment generating function gives
\[
m_r
=
1+\mu r+\frac{\mu^2+v}{2}r^2+O(r^3)
\]
and
\[
s_r^2
=
vr^2+\left(2\mu v+\kappa_3\right)r^3+O(r^4).
\]
Therefore
\[
s_r
=
ar+a\left(\mu-\frac{\zeta(3)}v\right)r^2+O(r^3).
\]

For all sufficiently small positive \(r\), \(m_r-s_r>0\). Since the exponential map is increasing, the one-sigma event for \(X\) is equivalent to
\[
y_-(r)\le Y\le y_+(r),
\qquad
y_\pm(r)=\frac1r\log(m_r\pm s_r).
\]
Substitution of the preceding expansions yields
\[
y_-(r)
=
\mu-a+\frac{\zeta(3)}a r+O(r^2),
\]
and
\[
y_+(r)
=
\mu+a-\frac{\zeta(3)}a r+O(r^2).
\]
Thus, in reflected-Gumbel coordinates, the one-standard-deviation interval contracts symmetrically at first order by
\[
\frac{\zeta(3)}{ak}.
\]

Let
\[
F_Y(y)=1-e^{-e^y},
\qquad
f_Y(y)=e^y e^{-e^y}.
\]
Taylor expansion at the fixed endpoints \(\mu\pm a\) gives
\[
C_k
=
F_Y(y_+(1/k))-F_Y(y_-(1/k))
\]
and hence
\[
C_k
=
F_Y(\mu+a)-F_Y(\mu-a)
-
\frac{\zeta(3)}{ak}
\left(f_Y(\mu+a)+f_Y(\mu-a)\right)
+O(k^{-2}).
\]
Because
\[
e^{\mu-a}=u_-
\quad\text{and}\quad
e^{\mu+a}=u_+,
\]
this is exactly the stated formula for \(C_\infty\) and \(A\). Positivity of \(A\) is immediate. The limiting value is the one-sigma central mass of a reflected Gumbel law; reflection does not change a symmetric central probability.

## Verification
The proof is analytic and applies to all sufficiently large real \(k\). The standalone script `verify_weibull_gumbel_endpoint.py` recomputes \(C_k\) directly from the exact Weibull mean, variance and CDF for several large shapes, compares it with the first-order formula, and checks the numerical constants. It prints:
`VERIFY_OK Cinf=0.723751267519710 A=0.375466930347350 scaled_k1000=0.374582858306976`.

The finite computations are regression checks only. They are not used to infer the order of the remainder, the sign of the coefficient, or the eventual Gaussian comparison.

## Relationship to prior work
Sun, Hu and Sun study exactly the functional \(C_k\). Their Theorem 3.1 proves the Gaussian comparison for the infinitely divisible Weibull range \(0<k\le1\). Their Remark 3.2 explicitly observes that the comparison can fail when \(k>1\), gives
\[
C_3=0.667713\ldots<2\Phi(1)-1,
\]
and plots the difference for \(1\le k\le10\). In the same paper, Theorem 2.2 computes the Gumbel one-sigma central mass \(0.723751\ldots\). The inspected full text does not state a large-\(k\) Weibull limit, a \(1/k\) correction, or the coefficient involving \(\zeta(3)\).

The exact logarithmic relation between Weibull and reflected Gumbel variables explains the limiting family, but it does not by itself determine the one-sigma interval after centering and variance normalization. The calculation above shows that the normalization moves both log-endpoints inward by the same first-order amount and therefore supplies a signed quantitative endpoint law.

Targeted published-record searches for large-shape Weibull standardization, reflected-Gumbel limits, one-sigma central probabilities, Gamma-function moment expansions, and the \(\zeta(3)\) correction found no statement covering this coefficient. Earlier work in the same research record on Weibull anti-concentration concerns the opposite small-shape regime and a different tail functional, so it does not imply this result.

## Limitations
The result is asymptotic and does not provide an explicit optimal threshold \(K\), prove global monotonicity in \(k\), or classify all crossings of the Gaussian benchmark. The Weibull-to-log-Gumbel transform and Gamma-function expansions are classical, so there remains a possibility that an equivalent first-order endpoint expansion occurs in older reliability or extreme-value literature under different terminology.

## References
P. Sun, Z.-C. Hu and W. Sun, *Variation comparison between infinitely divisible distributions and the normal distribution*, arXiv:2304.11459v1, first public version 2023-04-22. The paper lists primary MSC \(60E15\); Theorem 2.2 treats the Gumbel one-sigma probability, while Theorem 3.1 and Remark 3.2 treat the Weibull variation comparison.
