# Two critical shape thresholds in large-scale variance-gamma medians

Let
\[
V_{r,\theta,\sigma}\sim\mathrm{VG}(r,\theta,\sigma,0),
\qquad r>0,\quad \theta>0,\quad \sigma>0,
\]
in the parametrization with moment generating function
\[
\mathbb E e^{tV}=(1-2\theta t-\sigma^2t^2)^{-r/2}.
\]
Write \(M_{r,\theta,\sigma}=\operatorname{Med}(V_{r,\theta,\sigma})\).

Gaunt and Ouimet (2026) proved that \(M_{r,\theta,\sigma}\) is strictly decreasing in
\(\sigma\) and that
\[
M_{r,\theta,\sigma}\longrightarrow
\begin{cases}
(r-1)\theta,&r>1,\\
0,&0<r\le1,
\end{cases}
\qquad \sigma\to\infty.
\]
The convergence rate has two distinct critical shape parameters, \(r=1\) and
\(r=3\).

## Theorem

For fixed \(r>0\) and \(\theta>0\), as \(\sigma/\theta\to\infty\):

### 1. Power-singular regime: \(0<r<1\)

\[
\boxed{
M_{r,\theta,\sigma}
\sim
C_r\,\theta^{1/r}\sigma^{-(1-r)/r}
}
\]
with
\[
\boxed{
C_r=
\left[
r\,2^r
\frac{\Gamma((r+1)/2)}{\Gamma((1-r)/2)}
\right]^{1/r}.
}
\]

### 2. First critical point: \(r=1\)

\[
\boxed{
M_{1,\theta,\sigma}
=
\frac{\theta}{
\log(\sigma/\theta)
+\log\!\bigl(2\log(\sigma/\theta)\bigr)
+1-\gamma+o(1)
},
}
\]
where \(\gamma\) is Euler's constant. In particular,
\[
M_{1,\theta,\sigma}\sim\frac{\theta}{\log(\sigma/\theta)}.
\]

### 3. Fractional correction regime: \(1<r<3\)

\[
\boxed{
M_{r,\theta,\sigma}
=
(r-1)\theta+
A_r\,\theta^r\sigma^{-(r-1)}
+o\!\left(\theta^r\sigma^{-(r-1)}\right),
}
\]
where
\[
\boxed{
A_r=
\frac{
2\bigl((r-1)/2\bigr)^{r-1}\Gamma((3-r)/2)
}{
r\,\Gamma((r-1)/2)
}.
}
\]

### 4. Second critical point: \(r=3\)

\[
\boxed{
M_{3,\theta,\sigma}
=
2\theta+
\frac{4}{3}\frac{\theta^3}{\sigma^2}
\log(\sigma/\theta)
+
o\!\left(
\frac{\theta^3}{\sigma^2}\log(\sigma/\theta)
\right).
}
\]

### 5. Smooth correction regime: \(r>3\)

\[
\boxed{
M_{r,\theta,\sigma}
=
(r-1)\theta+
\frac{2(r-1)}{3(r-3)}
\frac{\theta^3}{\sigma^2}
+
o(\theta^3/\sigma^2).
}
\]

Thus \(r=1\) separates a vanishing median from a nonzero limiting median and is
also exactly the threshold at which the variance-gamma density changes from a
power singularity to a logarithmic singularity and then to a finite value at the
origin. A second transition occurs at \(r=3\): the first correction to the
nonzero limit is nonanalytic for \(1<r<3\), has a logarithmic resonance at
\(r=3\), and is of ordinary order \(\sigma^{-2}\) for \(r>3\).

## Proof

By scaling it is enough to take \(\theta=1\) and put
\[
\kappa=\sigma^2,\qquad s=r/2,\qquad \nu=(r-1)/2.
\]
The gamma-difference representation gives
\[
V_{r,1,\sqrt\kappa}
\stackrel d=
(\sqrt{1+\kappa}+1)Y_1-(\sqrt{1+\kappa}-1)Y_2,
\]
where \(Y_1,Y_2\) are independent \(\Gamma(r/2,1)\) variables. Hence, with
\(F_\kappa\) the CDF,
\[
F_\kappa(0)
=
I_{p_\kappa}(r/2,r/2),
\qquad
p_\kappa=
\frac12-\frac{1}{2\sqrt{1+\kappa}}.
\]
A Taylor expansion of the symmetric beta density about \(1/2\) yields
\[
\frac12-F_\kappa(0)
=
D_r\kappa^{-1/2}
\left[
1-\frac{r+1}{6\kappa}+O(\kappa^{-2})
\right],
\]
where
\[
D_r=
\frac{\Gamma((r+1)/2)}
{\sqrt\pi\,\Gamma(r/2)}.
\tag{1}
\]

For \(x>0\), the variance-gamma density is
\[
f_\kappa(x)
=
\frac{e^{x/\kappa}}{\sqrt{\pi\kappa}\Gamma(r/2)}
\left(
\frac{x}{2\sqrt{1+\kappa}}
\right)^\nu
K_\nu\!\left(
\frac{\sqrt{1+\kappa}}{\kappa}x
\right).
\tag{2}
\]
The five regimes follow from the standard small-argument expansions of
\(K_\nu\).

### \(0<r<1\)

Set \(\mu=(1-r)/2>0\). Since \(K_{-\mu}=K_\mu\),
\[
f_\kappa(x)
\sim
c_r^-\kappa^{-r/2}x^{r-1},
\qquad
c_r^-=
2^{-r}
\frac{\Gamma((1-r)/2)}
{\sqrt\pi\,\Gamma(r/2)}
\]
uniformly on the shrinking median scale. If \(m_\kappa\) denotes the median,
then \(m_\kappa\to0\), and
\[
\frac12-F_\kappa(0)
=
\int_0^{m_\kappa}f_\kappa(x)\,dx
\sim
\frac{c_r^-}{r}\kappa^{-r/2}m_\kappa^r.
\]
Combining this with (1) gives
\[
m_\kappa
\sim
C_r\kappa^{-(1-r)/(2r)}.
\]

### \(r=1\)

Here
\[
f_\kappa(x)=
\frac{e^{x/\kappa}}{\pi\sqrt\kappa}
K_0\!\left(\frac{\sqrt{1+\kappa}}{\kappa}x\right).
\]
Using
\[
K_0(z)=-\log(z/2)-\gamma+o(1)
\]
on the median scale and (1),
\[
1
=
m_\kappa
\left[
\frac12\log\kappa-\log m_\kappa+\log2+1-\gamma+o(1)
\right].
\]
Consequently
\[
m_\kappa^{-1}
=
\frac12\log\kappa+\log\log\kappa+1-\gamma+o(1).
\]

### \(1<r<3\)

Now \(0<\nu<1\). The two branches in the small-\(z\) expansion of \(K_\nu(z)\)
give
\[
f_\kappa(x)
=
c_r\kappa^{-1/2}
+
d_r x^{2\nu}\kappa^{-\nu-1/2}
+
o(\kappa^{-\nu-1/2}),
\tag{3}
\]
where
\[
c_r=
\frac{\Gamma(\nu)}
{2\sqrt\pi\,\Gamma(r/2)},
\qquad
d_r=
\frac{\Gamma(-\nu)}
{2^{2\nu+1}\sqrt\pi\,\Gamma(r/2)}.
\]
The leading terms in \(F_\kappa(2\nu)-1/2\) cancel because
\[
D_r=2\nu c_r.
\]
The next term from (3) is
\[
F_\kappa(2\nu)-\frac12
=
\frac{d_r(2\nu)^{2\nu+1}}{2\nu+1}
\kappa^{-\nu-1/2}
+o(\kappa^{-\nu-1/2}).
\]
Since \(f_\kappa(2\nu)\sim c_r\kappa^{-1/2}\), one Newton step for the
quantile gives
\[
m_\kappa
=
2\nu+A_r\kappa^{-\nu}+o(\kappa^{-\nu}),
\]
with the stated \(A_r\).

### \(r>3\)

For \(\nu>1\), the regular branch of \(K_\nu\) gives
\[
f_\kappa(x)
=
c_r\kappa^{-1/2}
\left[
1+
\frac{x-\nu+x^2/(4(1-\nu))}{\kappa}
+o(\kappa^{-1})
\right].
\tag{4}
\]
Using (1), integrating (4) from \(0\) to \(2\nu\), and again using
\(D_r=2\nu c_r\), one obtains
\[
F_\kappa(2\nu)-\frac12
=
-\frac{2c_r\nu}{3(\nu-1)}
\kappa^{-3/2}
+o(\kappa^{-3/2}).
\]
Dividing by \(f_\kappa(2\nu)\sim c_r\kappa^{-1/2}\) yields
\[
m_\kappa
=
2\nu+\frac{2\nu}{3(\nu-1)}\kappa^{-1}
+o(\kappa^{-1}).
\]

### \(r=3\)

At \(\nu=1\), the \(1/(\nu-1)\) singularity in the previous coefficient is
replaced by the logarithmic term in
\[
K_1(z)
=
z^{-1}
+\frac z2\left(\log(z/2)+\gamma-\frac12\right)
+O(z^3|\log z|).
\]
At \(x=2\),
\[
F_\kappa(2)-\frac12
=
-\frac{2}{3\pi}
\kappa^{-3/2}\log\kappa
+
O(\kappa^{-3/2}),
\]
whereas
\[
f_\kappa(2)\sim\frac{1}{\pi\sqrt\kappa}.
\]
Therefore
\[
m_\kappa
=
2+\frac{2}{3}\frac{\log\kappa}{\kappa}
+O(\kappa^{-1}).
\]
Restoring \(\theta\) and \(\kappa=(\sigma/\theta)^2\) gives all five formulas.

## Exact consistency check at \(r=2\)

The asymmetric Laplace special case has the exact median
\[
M_{2,\theta,\sigma}
=
\left(\theta+\sqrt{\theta^2+\sigma^2}\right)
\log\!\left(1+\frac{\theta}{\sqrt{\theta^2+\sigma^2}}\right).
\]
Its large-\(\sigma\) expansion is
\[
M_{2,\theta,\sigma}
=
\theta+\frac{\theta^2}{2\sigma}+O(\sigma^{-2}),
\]
which agrees with the theorem because \(A_2=1/2\).

## Wishart small-correlation corollary

Let \(X\sim W_p(V,n)\), and write
\[
V_{ii}=\sigma_i^2,\qquad
V_{jj}=\sigma_j^2,\qquad
V_{ij}=\rho\,\sigma_i\sigma_j
\]
with \(\rho>0\). The marginal law of an off-diagonal entry is
\[
X_{ij}\sim
\mathrm{VG}\!\left(
n,\,
\rho S,\,
S\sqrt{1-\rho^2},\,
0
\right),
\qquad S=\sigma_i\sigma_j.
\]
Hence, as \(\rho\downarrow0\),

\[
\operatorname{Med}(X_{ij})
=
\frac{S\rho}{
\log(1/\rho)+\log(2\log(1/\rho))+1-\gamma+o(1)
},
\qquad n=1,
\]

\[
\operatorname{Med}(X_{ij})
=
S\left[\rho+\frac12\rho^2+o(\rho^2)\right],
\qquad n=2,
\]

\[
\operatorname{Med}(X_{ij})
=
S\left[
2\rho+\frac43\rho^3\log(1/\rho)
+o(\rho^3\log(1/\rho))
\right],
\qquad n=3,
\]

and, for fixed integer \(n>3\),
\[
\operatorname{Med}(X_{ij})
=
S\left[
(n-1)\rho+
\frac{2(n-1)}{3(n-3)}\rho^3
+o(\rho^3)
\right].
\]

Thus the second threshold \(r=3\) has a direct statistical interpretation:
three degrees of freedom is the resonant case for the small-correlation median of
a Wishart off-diagonal entry.

## Numerical verification

`artifacts/verify_asymptotics.py` evaluates the exact zero CDF from the symmetric
beta representation, integrates the Bessel density on the positive half-line,
solves for the median, and compares it with the five asymptotic formulas.
`artifacts/verification.txt` records representative results. The normalized
correction ratios approach \(1\), including the slower logarithmic convergence
at the two critical cases.

## Relation to prior literature and originality boundary

Gaunt and Ouimet (2026) establish monotonicity in \(\sigma\), the limiting median,
and global bounds, but do not state convergence rates. Their proof of the
\(r\le1\) limit already separates \(r<1\) from the borderline \(r=1\), using
different orders of positive contribution, but stops at the limit itself.

Fischer, Gaunt and Sarantsev (2025) record the exact variance-gamma density,
its three local regimes at \(r=1\), the exact \(r=2\) median, and the Wishart
connection. Gaunt (2022) studies medians for products and sums of correlated
zero-mean normals, but does not give the small-correlation asymptotics above.

The contribution claimed here is restricted to the sharp five-regime
large-\(\sigma\) median asymptotics, including the previously unstated second
critical shape \(r=3\), the explicit constants, and the resulting Wishart
small-correlation median formulas. These statements are claimed only to the best
of our knowledge. Older generalized-Laplace literature may contain equivalent
quantile asymptotics under a different parametrization.

## Limitations

The asymptotics hold for fixed \(r\) and fixed \(\theta>0\); they are not uniform
as \(r\) approaches \(1\) or \(3\). No explicit finite-\(\sigma\) remainder bound
is provided. The case \(\theta=0\) is symmetric with median zero, and
\(\theta<0\) follows by reflection. The formulas concern the univariate median,
not joint quantiles of multivariate variance-gamma laws.

## References

1. R. E. Gaunt and F. Ouimet, *Bounds for the median of the generalized
   hyperbolic and related distributions*, arXiv:2609.20212 (2026).
   https://arxiv.org/abs/2609.20212
2. A. Fischer, R. E. Gaunt and A. Sarantsev, *The Variance-Gamma Distribution:
   A Review*, Statistical Science 40 (2025).
   https://doi.org/10.1214/24-STS929
3. R. E. Gaunt, *The basic distributional theory for the product of zero mean
   correlated normal random variables*, Statistica Neerlandica 76 (2022),
   450--470. https://doi.org/10.1111/stan.12267
4. NIST Digital Library of Mathematical Functions, Chapter 10, modified Bessel
   functions, especially §§10.30--10.31. https://dlmf.nist.gov/10.30
5. S. Kotz, T. J. Kozubowski and K. Podgórski, *The Laplace Distribution and
   Generalizations*, Birkhäuser (2001).
   https://doi.org/10.1007/978-1-4612-0173-1
