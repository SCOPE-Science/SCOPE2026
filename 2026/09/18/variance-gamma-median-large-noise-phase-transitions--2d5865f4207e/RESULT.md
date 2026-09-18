# Sharp large-noise asymptotics for variance-gamma medians

## Result

Let
\[
V_{r,\theta,\sigma}\sim \mathrm{VG}(r,\theta,\sigma,0),
\qquad r>0,\quad \theta>0,\quad \sigma>0,
\]
in the parameterization of Fischer, Gaunt and Sarantsev (2025), and write
\[
\kappa=\frac{\sigma^2}{\theta^2},
\qquad
M_r(\kappa)=\frac{\operatorname{Med}(V_{r,\theta,\sigma})}{\theta}.
\]
Gaunt and Ouimet (2026) proved that \(M_r(\kappa)\) is strictly decreasing and
\[
M_r(\kappa)\longrightarrow
\begin{cases}
0,&0<r\le 1,\\
r-1,&r>1,
\end{cases}
\qquad \kappa\to\infty.
\]
The convergence has the following sharp five-regime asymptotics.

### 1. Subcritical cusp: \(0<r<1\)

Define
\[
c_r=
\left[
\frac{r\,\Gamma((r+1)/2)}
{\Gamma((1-r)/2)}
\right]^{1/r}.
\]
Then
\[
\boxed{
M_r(\kappa)
\sim
2c_r\,\kappa^{-(1-r)/(2r)}.
}
\]
Equivalently,
\[
\boxed{
\operatorname{Med}(V_{r,\theta,\sigma})
\sim
2c_r\,\theta^{1/r}\sigma^{-(1-r)/r}.
}
\]

### 2. First critical shape: \(r=1\)

Let \(L=\log\kappa\), and let \(\gamma_{\!E}\) denote Euler's constant. Then
\[
\boxed{
M_1(\kappa)
=
\frac{2}
{L+2\log L+2-2\gamma_{\!E}+o(1)}.
}
\]
In particular,
\[
M_1(\kappa)\sim \frac{2}{\log\kappa}.
\]
Thus
\[
\boxed{
\operatorname{Med}(V_{1,\theta,\sigma})
=
\frac{2\theta}
{\log(\sigma^2/\theta^2)
 +2\log\log(\sigma^2/\theta^2)
 +2-2\gamma_{\!E}+o(1)}.
}
\]

### 3. Intermediate regularity: \(1<r<3\)

Define
\[
a_r=
\frac{2}{r}
\left(\frac{r-1}{2}\right)^{r-1}
\frac{\Gamma((3-r)/2)}
{\Gamma((r-1)/2)}.
\]
Then
\[
\boxed{
M_r(\kappa)
=
(r-1)+a_r\,\kappa^{-(r-1)/2}
+o\!\left(\kappa^{-(r-1)/2}\right).
}
\]
Equivalently,
\[
\boxed{
\operatorname{Med}(V_{r,\theta,\sigma})
=
(r-1)\theta
+a_r\theta^r\sigma^{-(r-1)}
+o\!\left(\theta^r\sigma^{-(r-1)}\right).
}
\]

### 4. Second critical shape: \(r=3\)

At the next threshold,
\[
\boxed{
M_3(\kappa)
=
2+\frac{2}{3}\frac{\log\kappa}{\kappa}
+o\!\left(\frac{\log\kappa}{\kappa}\right).
}
\]
Hence
\[
\boxed{
\operatorname{Med}(V_{3,\theta,\sigma})
=
2\theta+
\frac{2}{3}\frac{\theta^3}{\sigma^2}
\log\!\left(\frac{\sigma^2}{\theta^2}\right)
+o\!\left(
\frac{\theta^3}{\sigma^2}
\log\!\frac{\sigma^2}{\theta^2}
\right).
}
\]

### 5. Smooth regime: \(r>3\)

Define
\[
b_r=\frac{2(r-1)}{3(r-3)}.
\]
Then
\[
\boxed{
M_r(\kappa)
=
(r-1)+\frac{b_r}{\kappa}+o(\kappa^{-1}),
}
\]
or
\[
\boxed{
\operatorname{Med}(V_{r,\theta,\sigma})
=
(r-1)\theta+
\frac{2(r-1)}{3(r-3)}
\frac{\theta^3}{\sigma^2}
+o\!\left(\frac{\theta^3}{\sigma^2}\right).
}
\]

For \(\theta<0\), the formulas follow by reflection,
\[
\operatorname{Med}(V_{r,\theta,\sigma})
=
-\operatorname{Med}(V_{r,-\theta,\sigma}),
\]
and for \(\theta=0\) the median is zero.

The two critical shapes therefore produce logarithmic crossovers:
\[
r=1:\quad \operatorname{Med}(V)\asymp (\log\kappa)^{-1},
\]
and
\[
r=3:\quad
\operatorname{Med}(V)-(r-1)\theta
\asymp
\kappa^{-1}\log\kappa.
\]
Away from them the powers are \(\kappa^{-(1-r)/(2r)}\), \(\kappa^{-(r-1)/2}\), and \(\kappa^{-1}\).

## Proof

Set
\[
s=\frac r2.
\]
The normal variance-mean mixture used by Gaunt and Ouimet gives
\[
\frac{V_{r,\theta,\sigma}}{\theta}
\stackrel d=
Y_\kappa
:=
2G_s+\sqrt{2\kappa G_s}\,N,
\]
where \(G_s\sim\Gamma(s,1)\), \(N\sim N(0,1)\), and the two variables are independent. Let
\[
m_s(\kappa)=\operatorname{Med}(Y_\kappa),
\qquad
q_\kappa=\frac{m_s(\kappa)}2.
\]
Conditioning on \(G_s\) yields
\[
F_\kappa(2q)
=
\mathbb E\,
\Phi\!\left(
\sqrt{\frac2\kappa}\,
\frac{q-G_s}{\sqrt{G_s}}
\right).
\tag{1}
\]

### Boundary imbalance and exact median slope

At \(q=0\),
\[
F_\kappa(0)
=
\Pr\!\left(
T_{2s}\le-\sqrt{\frac{2s}{\kappa}}
\right),
\]
where \(T_{2s}\) is Student \(t\) with \(2s\) degrees of freedom. Consequently
\[
\delta_\kappa
:=
\frac12-F_\kappa(0)
\sim
\frac{\Gamma(s+1/2)}
{\sqrt{\pi}\Gamma(s)}
\kappa^{-1/2}.
\tag{2}
\]

Differentiating (1) and using the standard Bessel-\(K\) integral gives, for \(q>0\),
\[
D_\kappa(q)
:=
\frac{\partial}{\partial q}F_\kappa(2q)
=
\frac{2e^{2q/\kappa}}
{\sqrt{\pi\kappa}\Gamma(s)}
\left(\frac{q}{\sqrt{\kappa+1}}\right)^{s-1/2}
K_{s-1/2}\!\left(
\frac{2q\sqrt{\kappa+1}}{\kappa}
\right).
\tag{3}
\]
The median equation is therefore
\[
\delta_\kappa
=
\int_0^{q_\kappa}D_\kappa(u)\,du.
\tag{4}
\]

### The range \(0<s<1/2\)

Gaunt and Ouimet proved \(q_\kappa\to0\) in this range. Put
\[
\nu=\frac12-s>0.
\]
Using \(K_\nu(z)\sim2^{\nu-1}\Gamma(\nu)z^{-\nu}\) in (3), uniformly on
\(0<u\le q_\kappa\), gives
\[
D_\kappa(u)
\sim
\frac{\Gamma(1/2-s)}
{\sqrt{\pi}\Gamma(s)}
\kappa^{-s}u^{2s-1}.
\]
Combining this with (2) and (4),
\[
q_\kappa^{2s}
\sim
\frac{2s\,\Gamma(s+1/2)}
{\Gamma(1/2-s)}
\kappa^{s-1/2}.
\]
Since \(r=2s\) and \(m_s=2q_\kappa\), this is exactly the formula for \(0<r<1\).

### The critical case \(s=1/2\)

Here \(T_1\) is Cauchy, so
\[
\delta_\kappa
=
\frac1\pi\arctan(\kappa^{-1/2})
=
\frac{1+o(1)}{\pi\sqrt{\kappa}}.
\]
Equation (3) becomes
\[
D_\kappa(q)
=
\frac{2}{\pi\sqrt{\kappa}}
e^{2q/\kappa}
K_0\!\left(
\frac{2q\sqrt{\kappa+1}}{\kappa}
\right).
\]
Since \(q_\kappa\to0\), the expansion
\[
K_0(z)=-\log(z/2)-\gamma_{\!E}+o(1)
\]
can be integrated uniformly on \(0<q\le q_\kappa\). Equation (4) gives
\[
q_\kappa
\left[
\log\kappa-2\log q_\kappa+2-2\gamma_{\!E}+o(1)
\right]
=1.
\tag{5}
\]
First (5) implies \(q_\kappa\sim1/\log\kappa\). Substitution back into (5) then gives
\[
\frac1{q_\kappa}
=
\log\kappa
+2\log\log\kappa
+2-2\gamma_{\!E}
+o(1),
\]
which proves the \(r=1\) formula.

### The range \(s>1/2\)

Put
\[
a=s-\frac12.
\]
Gaunt and Ouimet proved \(q_\kappa\to a\). Define
\[
H(x)=\Phi(x)-\frac12-\phi(0)x.
\]
At \(q=a\), the linear term vanishes exactly because
\[
\mathbb E\frac{a-G_s}{\sqrt{G_s}}
=
a\,\frac{\Gamma(s-1/2)}{\Gamma(s)}
-\frac{\Gamma(s+1/2)}{\Gamma(s)}
=0.
\]
Hence
\[
R_\kappa
:=
F_\kappa(2a)-\frac12
=
\mathbb E\,
H\!\left(
\sqrt{\frac2\kappa}\,
\frac{a-G_s}{\sqrt{G_s}}
\right).
\tag{6}
\]
Moreover, uniformly for \(q\to a\),
\[
D_\kappa(q)
\sim
A_s\kappa^{-1/2},
\qquad
A_s=
\frac{\Gamma(s-1/2)}
{\sqrt{\pi}\Gamma(s)}.
\tag{7}
\]
By the mean-value theorem,
\[
q_\kappa-a
=
-\frac{R_\kappa}{D_\kappa(\xi_\kappa)}
\tag{8}
\]
for some \(\xi_\kappa\) between \(a\) and \(q_\kappa\).

#### Boundary-dominated range \(1/2<s<3/2\)

The contribution from \(G_s\) near zero dominates. With \(G_s=z/\kappa\), while the part bounded away from zero is of smaller order,
\[
\kappa^s R_\kappa
\longrightarrow
\frac{2^{s+1}a^{2s}}{\Gamma(s)}
J_s,
\]
where
\[
J_s
=
\int_0^\infty H(x)x^{-2s-1}\,dx.
\]
Two integrations by parts give
\[
J_s
=
-\frac{2^{-s}\Gamma(3/2-s)}
{2s(2s-1)\sqrt{\pi}}.
\]
Therefore
\[
R_\kappa
\sim
-
\frac{
a^{2s}\Gamma(3/2-s)
}{
s(2s-1)\sqrt{\pi}\Gamma(s)
}
\kappa^{-s}.
\tag{9}
\]
Combining (7)--(9) and converting from \(s\) to \(r=2s\) yields the coefficient \(a_r\).

#### Critical range \(s=3/2\)

Now \(a=1\). The integral in (9) is exactly at its logarithmic integrability boundary. Since
\[
H(x)=-\frac{\phi(0)}6x^3+O(x^5)
\qquad(x\to0),
\]
the rescaled integrand has the intermediate-tail form
\[
-\frac{2}{3\pi}\frac1z+o(z^{-1}).
\]
Consequently
\[
R_\kappa
\sim
-\frac{2}{3\pi}
\kappa^{-3/2}\log\kappa.
\]
Since (7) gives
\[
D_\kappa(\xi_\kappa)
\sim
\frac2\pi\kappa^{-1/2},
\]
equation (8) yields
\[
q_\kappa-1
\sim
\frac13\frac{\log\kappa}{\kappa}.
\]
Multiplication by two proves the \(r=3\) formula.

#### Interior-dominated range \(s>3/2\)

Now the cubic Taylor term is integrable because
\[
\mathbb E G_s^{-3/2}<\infty.
\]
Using \(|H(x)|\le C|x|^3\) and dominated convergence,
\[
\kappa^{3/2}R_\kappa
\longrightarrow
-\frac1{3\sqrt{\pi}}
\mathbb E\!\left[
(a-G_s)^3G_s^{-3/2}
\right].
\]
Gamma recurrences simplify the expectation to
\[
\mathbb E\!\left[
(a-G_s)^3G_s^{-3/2}
\right]
=
a\,\frac{\Gamma(s-3/2)}{\Gamma(s)}.
\]
Together with (7) and (8),
\[
q_\kappa-a
\sim
\frac{a}{3(s-3/2)}\kappa^{-1}.
\]
Since \(m_s=2q_\kappa\), this gives
\[
b_r=\frac{2(r-1)}{3(r-3)}.
\]

## Checks and interpretation

The case \(r=2\) is an independent exact check. The known asymmetric-Laplace formula is
\[
\operatorname{Med}(V_{2,\theta,\sigma})
=
\left(\theta+\sqrt{\theta^2+\sigma^2}\right)
\log\!\left(
1+\frac{\theta}{\sqrt{\theta^2+\sigma^2}}
\right)
\]
for \(\theta>0\). Its large-\(\sigma\) expansion is
\[
\theta+\frac{\theta^2}{2\sigma}+O(\sigma^{-2}),
\]
while the coefficient above gives \(a_2=1/2\).

The first threshold \(r=1\) coincides with the classical change in the local behavior of the VG density at its location: the density is power-singular for \(r<1\), logarithmically singular at \(r=1\), and finite for \(r>1\). This density fact is prior art and is not claimed as new.

The second threshold \(r=3\) has a different origin. After cancellation of the linear normal perturbation at the limiting median, the first surviving interior correction is cubic. Its expectation requires
\(\mathbb E G_s^{-3/2}<\infty\), which holds precisely when \(s>3/2\), i.e. \(r>3\). At equality the inverse moment diverges logarithmically, producing the
\(\kappa^{-1}\log\kappa\) law.

## Context and originality boundary

Gaunt and Ouimet (2026) prove strict monotonicity of the VG median in \(\sigma\), the sharp bounds implied by it, and the endpoint limit
\[
\operatorname{Med}(V_{r,\theta,\sigma})
\to 0\vee(r-1)\theta.
\]
Their proof identifies the limiting sign of the centered cdf but does not state a convergence rate.

The 2025 survey by Fischer, Gaunt and Sarantsev reviews VG median theory and records that, outside special cases such as \(r=2\), no exact closed form is available. The \(r=2\) formula above is known and is used only as a consistency check.

The singular/finite transition of the VG density at \(r=1\), as well as the relevant small-argument expansions of modified Bessel functions, are classical. Siqi Li's 2024 thesis, for example, records the power singularity for \(0<r<1\) and logarithmic singularity at \(r=1\). These mechanisms are not claimed as new.

To the best of our knowledge, targeted searches did not locate the five-regime large-noise median expansion above, the \(r=3\) logarithmic transition, the \(r=1\) two-logarithm refinement, or the displayed constants. The 2001 monograph *The Laplace Distribution and Generalizations* is directly relevant prior literature but was not inspected in full; it remains the principal residual originality risk. The newer 2025 VG review surveys median theory without reporting these asymptotics.

## Limitations

The result concerns the univariate VG family with fixed \(r\) and fixed nonzero \(\theta\) as \(\sigma/|\theta|\to\infty\). It does not provide uniform asymptotics when \(r\) approaches either critical value \(1\) or \(3\) simultaneously with \(\kappa\to\infty\). No higher-order expansion is proved except for the explicit second logarithmic term at \(r=1\). The result does not address generalized hyperbolic medians away from the VG boundary.

## References

- Robert E. Gaunt and Frédéric Ouimet, *Bounds for the median of the generalized hyperbolic and related distributions*, arXiv:2609.20212, 2026. https://arxiv.org/abs/2609.20212
- Adrian Fischer, Robert E. Gaunt and Andrey Sarantsev, *The Variance-Gamma Distribution: A Review*, Statistical Science 40 (2025). https://doi.org/10.1214/24-STS929
- Robert E. Gaunt and Milan Merkle, *On bounds for the mode and median of the generalized hyperbolic and related distributions*, Journal of Mathematical Analysis and Applications 493 (2021), 124508. https://doi.org/10.1016/j.jmaa.2020.124508
- Siqi Li, *Some Contributions to Stein's Method and the Theory of Probability Distributions*, PhD thesis, The University of Manchester, 2024. https://research.manchester.ac.uk/en/studentTheses/some-contributions-to-steins-method-and-the-theory-of-probability
- Samuel Kotz, Tomasz J. Kozubowski and Krzysztof Podgórski, *The Laplace Distribution and Generalizations*, Birkhäuser, 2001.
- NIST Digital Library of Mathematical Functions, Chapter 10, modified Bessel functions. https://dlmf.nist.gov/10
