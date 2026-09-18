# Exact self-decomposability threshold for Gaussian compound-Poisson perturbations of symmetric variance-gamma laws

## Statement

Let \(V\) be a centered symmetric variance-gamma (equivalently symmetric generalized Laplace) random variable with characteristic function
\[
\phi_V(t)=(1+b^2t^2)^{-\beta},
\qquad \beta>0,\ b>0.
\]
Let
\[
C_{\lambda,\sigma}=\sum_{j=1}^{N_\lambda} Z_j,
\]
where \(N_\lambda\sim{\rm Poisson}(\lambda)\), the jumps \(Z_j\) are iid \(N(0,\sigma^2)\), and all variables are independent. Put
\[
X_{\lambda,\sigma}=V+C_{\lambda,\sigma}.
\]

Define the scale ratio
\[
r=\frac{\sigma}{b},
\]
and let \(y_r\in(0,1)\) be the unique solution of
\[
r=\frac{y_r(3-y_r^2)}{1-y_r^2}.
\]
Then define
\[
\boxed{
\lambda_c(\beta,b,\sigma)
=
\beta\sqrt{2\pi}\,r\,
\frac{\exp(-r y_r+y_r^2/2)}{1-y_r^2}.
}
\]

### Theorem 1: exact self-decomposability threshold

The infinitely divisible law \(X_{\lambda,\sigma}\) is self-decomposable if and only if
\[
\boxed{0\le \lambda\le \lambda_c(\beta,b,\sigma).}
\]

At the critical value \(\lambda=\lambda_c\), the canonical self-decomposability profile has a unique positive tangency point \(x=\sigma y_r\), with the symmetric tangency at \(-\sigma y_r\).

### Theorem 2: a Goldilocks jump-scale window

For fixed \(\beta,b\), the critical activity \(\lambda_c\) as a function of \(r=\sigma/b\) has a unique global maximum at
\[
\boxed{
r_*=\sqrt{2+\sqrt3}.
}
\]
The maximum admissible compound-Poisson activity is
\[
\boxed{
\lambda_{\max}
=
\beta\sqrt{2\pi}\,
\frac{\sqrt{2+\sqrt3}}{\sqrt3-1}
e^{-\sqrt3/2}
\approx 2.7823542896\,\beta.
}
\]

Consequently:

- if \(\lambda>\lambda_{\max}\), no Gaussian jump scale \(\sigma\) preserves self-decomposability;
- if \(\lambda=\lambda_{\max}\), self-decomposability holds only at \(\sigma/b=r_*\);
- if \(0<\lambda<\lambda_{\max}\), there are exactly two boundary ratios
  \[
  0<r_-(\lambda)<r_*<r_+(\lambda)<\infty,
  \]
  and self-decomposability holds exactly for
  \[
  r\in[r_-(\lambda),r_+(\lambda)].
  \]

Thus both very narrow and very broad finite-activity Gaussian shocks can destroy class \(L\), while an intermediate range survives.

The endpoint behavior is
\[
y_r=\frac r3-\frac{2r^3}{81}+O(r^5),
\qquad
\frac{\lambda_c}{\beta\sqrt{2\pi}}
=
r-\frac{r^3}{6}+O(r^5)
\quad(r\downarrow0),
\]
and
\[
y_r=1-\frac1r+O(r^{-2}),
\qquad
\frac{\lambda_c}{\beta\sqrt{2\pi}}
\sim
\frac{e^{3/2}}2r^2e^{-r}
\quad(r\to\infty).
\]

### Corollary: arbitrarily weak finite-activity perturbations can destroy self-decomposability

Fix any \(\lambda>0\). As \(\sigma\downarrow0\),
\[
C_{\lambda,\sigma}\to0
\]
in probability, and
\[
{\rm Var}(C_{\lambda,\sigma})=\lambda\sigma^2\to0.
\]
Hence
\[
X_{\lambda,\sigma}\Rightarrow V.
\]
Nevertheless,
\[
\lambda_c(\beta,b,\sigma)
\sim
\beta\sqrt{2\pi}\frac{\sigma}{b}
\to0,
\]
so for every fixed \(\lambda>0\), \(X_{\lambda,\sigma}\) fails to be self-decomposable for all sufficiently small \(\sigma\).

Therefore self-decomposability is not locally stable along this natural family of arbitrarily weak infinitely divisible perturbations.

### Theorem 3: explicit background-driving jump law

When \(0\le\lambda\le\lambda_c\), define
\[
j_{\lambda,\sigma}(x)
=
\frac{e^{-|x|/b}}{2b}
-
\frac{\lambda}{2\beta}
\left(1-\frac{x^2}{\sigma^2}\right)
\varphi_\sigma(x),
\]
where
\[
\varphi_\sigma(x)
=
\frac{1}{\sqrt{2\pi}\sigma}
e^{-x^2/(2\sigma^2)}.
\]
Then \(j_{\lambda,\sigma}\) is a probability density. The background-driving Lévy process of \(X_{\lambda,\sigma}\) is compound Poisson with rate \(2\beta\) and jump density \(j_{\lambda,\sigma}\).

At criticality, \(j_{\lambda_c,\sigma}\) touches zero at exactly
\[
x=\pm \sigma y_r.
\]

## Proof

### 1. Canonical Lévy density

The symmetric variance-gamma law has Lévy density
\[
\nu_V(dx)
=
\beta\frac{e^{-|x|/b}}{|x|}\,dx.
\]
The Gaussian compound-Poisson component has Lévy density
\[
\nu_C(dx)=\lambda\varphi_\sigma(x)\,dx.
\]
Hence the sum is infinitely divisible with Lévy density
\[
\nu(dx)
=
\left[
\beta\frac{e^{-|x|/b}}{|x|}
+
\lambda\varphi_\sigma(x)
\right]dx.
\]

For a symmetric infinitely divisible law on \(\mathbb R\), the classical one-dimensional self-decomposability criterion says that a Lévy density of the form
\[
\nu(dx)=\frac{k(|x|)}{|x|}\,dx
\]
is self-decomposable exactly when \(k\) is nonincreasing on \((0,\infty)\).

Here
\[
k(x)=\beta e^{-x/b}+\lambda x\varphi_\sigma(x),
\qquad x>0.
\]
Differentiation gives
\[
k'(x)
=
-\frac{\beta}{b}e^{-x/b}
+
\lambda\varphi_\sigma(x)
\left(1-\frac{x^2}{\sigma^2}\right).
\]

For \(x\ge\sigma\), the second term is nonpositive, so \(k'(x)<0\). Therefore the only constraint comes from \(0<x<\sigma\), where
\[
k'(x)\le0
\]
is equivalent to
\[
\lambda
\le
\frac{\beta b^{-1}e^{-x/b}}
{\varphi_\sigma(x)(1-x^2/\sigma^2)}.
\]

Set
\[
y=\frac{x}{\sigma},\qquad r=\frac{\sigma}{b}.
\]
The upper bound becomes
\[
\lambda
\le
\beta\sqrt{2\pi}\,r\,
\frac{e^{-ry+y^2/2}}{1-y^2},
\qquad 0<y<1.
\]
Thus the exact admissible activity is the infimum over \(y\in(0,1)\).

### 2. The minimizing point is unique

Let
\[
F_r(y)=\frac{e^{-ry+y^2/2}}{1-y^2}.
\]
Then
\[
\frac{d}{dy}\log F_r(y)
=
-r+y+\frac{2y}{1-y^2}
=
-r+\frac{y(3-y^2)}{1-y^2}.
\]
Define
\[
h(y)=\frac{y(3-y^2)}{1-y^2}.
\]
For \(0<y<1\),
\[
h'(y)
=
\frac{y^4+3}{(1-y^2)^2}>0,
\]
while \(h(0+)=0\) and \(h(1-)=\infty\). Hence there is a unique \(y_r\in(0,1)\) satisfying
\[
h(y_r)=r.
\]
It is the unique minimizer, which proves Theorem 1.

At \(\lambda=\lambda_c\), equality holds only at \(x=\sigma y_r\), so the canonical profile has the claimed tangency.

### 3. Optimizing over the jump scale

Write
\[
\lambda_c
=
\beta\sqrt{2\pi}\,G(r),
\qquad
G(r)
=
r\frac{e^{-r y_r+y_r^2/2}}{1-y_r^2}.
\]
Because \(y_r\) minimizes the exponent-plus-barrier term, the envelope theorem gives
\[
\frac{d}{dr}\log G(r)=\frac1r-y_r.
\]
The unique stationary point therefore satisfies
\[
r=\frac1{y_r}.
\]
Combining this with \(r=h(y_r)\) yields
\[
\frac1y
=
\frac{y(3-y^2)}{1-y^2},
\]
or
\[
y^4-4y^2+1=0.
\]
The only solution in \((0,1)\) is
\[
y_*^2=2-\sqrt3,
\]
hence
\[
r_*=\frac1{y_*}=\sqrt{2+\sqrt3}.
\]

At this point,
\[
r_*y_*=1,\qquad
1-y_*^2=\sqrt3-1,
\]
and
\[
-r_*y_*+\frac{y_*^2}{2}
=
-\frac{\sqrt3}{2}.
\]
This gives the stated formula for \(\lambda_{\max}\).

Moreover,
\[
G(r)\to0
\quad\text{as }r\downarrow0
\quad\text{and as }r\to\infty,
\]
and the derivative changes sign only once. Thus \(G\) is strictly increasing before \(r_*\) and strictly decreasing after it, proving the complete scale-window phase diagram.

Expanding
\[
h(y)=3y+2y^3+O(y^5)
\]
near zero gives
\[
y_r=\frac r3-\frac{2r^3}{81}+O(r^5),
\]
which substituted into \(G\) yields
\[
G(r)=r-\frac{r^3}{6}+O(r^5).
\]
For large \(r\), inversion near \(y=1\) gives
\[
y_r=1-\frac1r+O(r^{-2}),
\]
and substitution yields
\[
G(r)\sim \frac{e^{3/2}}2r^2e^{-r}.
\]

### 4. An independent background-driving certificate

The characteristic exponent of \(X_{\lambda,\sigma}\) is
\[
\Psi(t)
=
\beta\log(1+b^2t^2)
+
\lambda\left(1-e^{-\sigma^2t^2/2}\right).
\]
Therefore
\[
t\Psi'(t)
=
\frac{2\beta b^2t^2}{1+b^2t^2}
+
\lambda\sigma^2t^2e^{-\sigma^2t^2/2}.
\]
It satisfies
\[
t\Psi'(t)\to0
\quad(t\to0),
\qquad
t\Psi'(t)\to2\beta
\quad(|t|\to\infty).
\]

A recent criterion of Wang and Yin states, under these conditions for a symmetric law with positive characteristic function, that self-decomposability is equivalent to the function
\[
J(t)
=
1-\frac{t\Psi'(t)}{2\beta}
\]
being a characteristic function of a symmetric probability distribution with no atom at zero. Here
\[
J(t)
=
\frac1{1+b^2t^2}
-
\frac{\lambda\sigma^2}{2\beta}
t^2e^{-\sigma^2t^2/2}.
\]

The inverse Fourier transform is
\[
j_{\lambda,\sigma}(x)
=
\frac{e^{-|x|/b}}{2b}
-
\frac{\lambda}{2\beta}
\left(1-\frac{x^2}{\sigma^2}\right)\varphi_\sigma(x),
\]
because
\[
\mathcal F\!\left[
\left(1-\frac{x^2}{\sigma^2}\right)\varphi_\sigma(x)
\right](t)
=
\sigma^2t^2e^{-\sigma^2t^2/2}.
\]
Also
\[
\int_\mathbb R j_{\lambda,\sigma}(x)\,dx=1.
\]

For \(|x|\ge\sigma\), the Gaussian correction is nonnegative. For \(|x|<\sigma\), the condition \(j_{\lambda,\sigma}(x)\ge0\) is exactly
\[
\lambda
\le
\frac{\beta b^{-1}e^{-|x|/b}}
{\varphi_\sigma(x)(1-x^2/\sigma^2)},
\]
the same inequality obtained from the canonical Lévy-density criterion. Hence \(j_{\lambda,\sigma}\) is a probability density exactly for
\[
\lambda\le\lambda_c.
\]
The Wang-Yin characterization then independently recovers Theorem 1 and identifies the background-driving compound-Poisson law in Theorem 3.

### 5. Weak-perturbation fragility

Couple the Gaussian jumps as \(Z_j=\sigma G_j\), with \(G_j\sim N(0,1)\). For fixed \(N_\lambda\),
\[
C_{\lambda,\sigma}
=
\sigma\sum_{j=1}^{N_\lambda}G_j
\to0
\]
almost surely as \(\sigma\downarrow0\), and therefore also in probability. Its variance is
\[
\lambda\sigma^2.
\]
Thus
\[
X_{\lambda,\sigma}\Rightarrow V.
\]

But the small-\(r\) expansion gives
\[
\lambda_c
=
\beta\sqrt{2\pi}\frac{\sigma}{b}
+O(\sigma^3).
\]
For every fixed \(\lambda>0\), eventually \(\lambda>\lambda_c\), and the perturbed law is not self-decomposable. This proves the fragility corollary.

## A general perturbation identity

The preceding calculation isolates a simple mechanism that is useful beyond the Gaussian example.

Suppose a symmetric self-decomposable law has a locally absolutely continuous canonical function \(k_0(x)\), \(x>0\), and add an independent symmetric compound-Poisson law of rate \(\lambda\) with even \(C^1\) jump density \(g\). Then the new canonical function is
\[
k_\lambda(x)=k_0(x)+\lambda xg(x).
\]
Hence the perturbed law is self-decomposable exactly when
\[
k_0'(x)+\lambda(xg(x))'\le0
\quad\text{for almost every }x>0.
\]
Consequently the exact admissible activity is
\[
\lambda_*
=
\operatorname*{ess\,inf}_{\{x:(xg(x))'>0\}}
\frac{-k_0'(x)}{(xg(x))'},
\]
with the infimum interpreted as \(+\infty\) if the positive-derivative set is empty.

This identity is an immediate specialization of the classical canonical-density characterization and is not claimed here as a new general theorem. Its value in the present setting is that the variance-gamma/Gaussian pair makes the threshold and its scale optimization fully explicit.

## Context

Self-decomposable laws form class \(L\), a strict and structurally important subclass of infinitely divisible distributions. The one-dimensional canonical-density criterion
\[
\nu(dx)=\frac{k(x)}{|x|}\,dx,
\]
with monotonicity of \(k\) on the positive and negative half-lines, is classical.

The variance-gamma family is a standard self-decomposable family; modern treatments also place it inside broader generalized gamma convolution and weak-subordination constructions. Exact parameter thresholds for self-decomposability are known in several other distribution families, so the existence of a threshold phenomenon is not by itself novel.

The contribution here is the explicit phase diagram for a natural finite-activity perturbation of the symmetric variance-gamma law: the exact Gaussian compound-Poisson activity threshold, the unique optimal jump scale, the maximal admissible activity, the weak-perturbation fragility mechanism, and an explicit background-driving jump density. Financial Lévy models combining variance-gamma dynamics with separate compound-Poisson shocks have appeared previously, but the sources inspected did not analyze this self-decomposability boundary.

## Limitations

- The explicit phase diagram is one-dimensional and symmetric.
- The compound-Poisson jumps are centered Gaussian. Other jump laws reduce to the general derivative criterion above but need not admit a closed-form threshold or a single scale window.
- No ordinary stochastic ordering, tail ordering, unimodality ordering, or option-pricing consequence is claimed.
- Infinite divisibility is automatic throughout the family; the theorem separates class \(L\) from the larger infinitely divisible class, not infinite divisibility from non-infinite-divisibility.
- The weak-perturbation statement is path-specific: it demonstrates failure of local stability along a concrete family but is not a topological classification of class \(L\).
- Originality is to the best of our knowledge. Older class-\(L\), convolution-factor, and parametric self-decomposability literature could contain equivalent special cases under different terminology.

## References

1. M. Wang and S. Yin, “Self-decomposability of α-Cauchy distributions”, arXiv:2609.18536 (2026). https://arxiv.org/abs/2609.18536
2. K.-I. Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge University Press, 1999.
3. A. G. Pakes, “On generalized stable and related laws”, Journal of Mathematical Analysis and Applications 411 (2014), 201–222. https://doi.org/10.1016/j.jmaa.2013.09.041
4. B. Buchmann, K. Lu and D. B. Madan, “Self-decomposability of weak variance generalised gamma convolutions”, Stochastic Processes and their Applications 130 (2020), 1355–1377. https://doi.org/10.1016/j.spa.2019.02.012
5. A. Fischer, R. E. Gaunt and A. Sarantsev, “The Variance-Gamma Distribution: A Review”, Statistical Science 39 (2024), 435–458; arXiv:2303.05615. https://arxiv.org/abs/2303.05615
6. R. V. Ivanov and K. Ano, “Option pricing in time-changed Lévy models with compound Poisson jumps”, Modern Stochastics: Theory and Applications 6 (2019), 409–424. https://doi.org/10.15559/18-VMSTA124
7. A. Iksanov, Z. J. Jurek and B. M. Schreiber, “A new factorization property of selfdecomposable probability measures”, Annals of Probability 32 (2004), 1356–1369; arXiv:math/0205316. https://arxiv.org/abs/math/0205316
