# Radial inference of the killing index in a planar random flight

## Finding

Consider a planar particle starting at the origin, moving with speed \(c>0\) and initially choosing a uniform angle in \([0,2\pi)\). Events of an independent Poisson process occur at rate \(\lambda>0\). At every event the particle is killed with probability \(p\in(0,1)\); otherwise it chooses a fresh independent uniform angle and continues. Let \(K\ge1\) count the Poisson event at which killing occurs, let \(Z\) be the final position and set \(R=|Z|\). Write

\[
q=1-p,\qquad \beta=\lambda/c,\qquad s=\sqrt{1-q^2}=\sqrt{p(2-p)}.
\]

**Strict radial monotone likelihood ratio.** For every \(0<r_1<r_2\) and every pair of integers \(1\le n<m\), the regular conditional probabilities satisfy

\[
\frac{\Pr(K=m\mid R=r_2)}{\Pr(K=n\mid R=r_2)}
>
\frac{\Pr(K=m\mid R=r_1)}{\Pr(K=n\mid R=r_1)}.
\]

All conditional probabilities in this statement are defined by the everywhere-positive radial densities for \(r>0\). In particular, a farther observed terminal position strictly shifts the conditional killing-index distribution upward in likelihood-ratio order.

**Sharp distant-endpoint inference.** Define the positive constants

\[
a=\frac{\beta q^2}{s},\qquad
b=\frac{\beta q^2(2-q^2)}{s^3}.
\]

For each fixed admissible \((p,\lambda,c)\), as \(r\to\infty\), the conditional law of \(K\), given \(R=r\), obeys

\[
\frac{K-ar}{\sqrt{br}}\ \Longrightarrow\ N(0,1).
\]

The centering and dispersion admit explicit constant-order corrections:

\[
\begin{aligned}
\mathbb E[K\mid R=r]&=ar+2+\frac{q^2}{2s^2}+O(r^{-1}),\\
\operatorname{Var}(K\mid R=r)&=br+\frac{q^2}{s^4}+O(r^{-1}).
\end{aligned}
\]

Here \(K\) counts **all** Poisson events through killing (the terminal event included), not merely the surviving changes of direction. Subtracting one from \(K\) changes the reported constant-order mean, but not the likelihood-ratio property or Gaussian limit.

## Assumptions and scope

The Poisson interarrival times are independent exponential variables of rate \(\lambda\), independent of the independent killing decisions and angles. A surviving event produces a fresh independent angle uniformly distributed over the full circle. Parameters \(c,\lambda\) are finite and strictly positive; \(0<p<1\) is fixed during the \(r\to\infty\) limit. The theorem concerns inference from the final **radius** of a killed flight, not a deterministic-time position or a trajectory observed up to a fixed time. The normal approximation is a conditional weak limit for the continuously conditioned radius \(r>0\), rather than conditioning on a probability-zero event without specifying a density version.

## Proof

**1. Conditional Gamma–normal mixture.** The killing index has the geometric law \(\Pr(K=n)=p q^{n-1}\) for \(n\ge1\). An individual displacement segment is \(cTU\), where \(T\) is exponential with rate \(\lambda\) and \(U\) is uniform on the unit circle. Writing \(\xi\in\mathbb R^2\), its characteristic function is

\[
\mathbb E e^{i\xi\cdot cTU}
=\int_0^\infty\lambda e^{-\lambda t}J_0(c|\xi|t)\,dt
=\frac{\beta}{\sqrt{\beta^2+|\xi|^2}}.
\]

Thus the final position conditional on \(K=n\) has characteristic function \((1+|\xi|^2/\beta^2)^{-n/2}\). This is exactly the distribution of \(\sqrt{V_n}G\), where \(G\sim N_2(0,I_2)\) and \(V_n\) is independent Gamma with shape \(n/2\) and rate \(\beta^2/2\). Its strictly positive spatial density at a radius \(r>0\) is

\[
f_n(r)=\frac{(\beta^2/2)^{n/2}}{2\pi\Gamma(n/2)}
\int_0^\infty v^{n/2-2}\exp\!\left(-\frac{\beta^2v}{2}-\frac{r^2}{2v}\right)dv.
\]

For numerical evaluation, equivalently,

\[
f_n(r)=\frac{\beta^{n/2+1}r^{n/2-1}}{2^{n/2}\pi\Gamma(n/2)}K_{n/2-1}(\beta r).
\]

**2. Strict likelihood-ratio ordering.** Fix \(m>n\) and introduce the probability density \(\nu_{n,r}\) on \((0,\infty)\), proportional to the integrand for \(f_n(r)\). Then \(f_m(r)/f_n(r)\) is a positive constant independent of \(r\), multiplied by \(\mathbb E_{\nu_{n,r}}[V^{(m-n)/2}]\). For \(r_2>r_1>0\),

\[
\frac{d\nu_{n,r_2}}{d\nu_{n,r_1}}(v)
=C\exp\!\left(-\frac{r_2^2-r_1^2}{2v}\right),
\]

which is strictly increasing in \(v\). Therefore the expectation of the strictly increasing, integrable function \(v^{(m-n)/2}\) increases strictly between the two conditional mixing measures. This proves that \(f_m(r)/f_n(r)\) increases strictly in \(r\). Bayes' rule gives \(\Pr(K=n\mid R=r)\propto pq^{n-1}f_n(r)\); the common radial Jacobian \(2\pi r\) cancels, proving the displayed strict posterior likelihood-ratio inequality for all stated pairs.

**3. Positive marked-density decomposition.** For \(r>0\), \(z>0\) and \(qz<1\), define the marked spatial density

\[
H_r(z)=\sum_{n\ge1}pq^{n-1}z^n f_n(r),\qquad
\mathbb E[z^K\mid R=r]=\frac{H_r(z)}{H_r(1)}.
\]

Its planar Fourier transform, with \(w=\sqrt{\beta^2+|\xi|^2}\), is

\[
\widehat H_z(\xi)=\frac{pz\beta}{w-qz\beta}
=\frac{2pqz^2\beta^2}{|\xi|^2+\beta^2(1-q^2z^2)}
+\frac{pz\beta}{w+qz\beta}.
\]

Let \(\kappa(z)=\beta\sqrt{1-q^2z^2}\). The two-dimensional inverse transform of \((|\xi|^2+\kappa^2)^{-1}\) is \(K_0(\kappa r)/(2\pi)\). In the second term, write \((w+qz\beta)^{-1}=\int_0^\infty e^{-t(w+qz\beta)}dt\). Standard Gaussian subordination, which follows by integrating

\[
e^{-t\sqrt A}=\frac{t}{2\sqrt\pi}\int_0^\infty u^{-3/2}\exp\!\left(-\frac{t^2}{4u}-Au\right)du,
\]

gives the inverse planar Fourier transform

\[
\mathcal F^{-1}[e^{-t\sqrt{\beta^2+|\xi|^2}}](r)=
\frac{\beta t}{2\pi(r^2+t^2)}e^{-\beta\sqrt{r^2+t^2}}
\left(1+\frac{1}{\beta\sqrt{r^2+t^2}}\right).
\]

Consequently, without cancellation of signed terms,

\[
\begin{aligned}
H_r(z)={}&\frac{pqz^2\beta^2}{\pi}K_0(\kappa(z)r)\\
&+\frac{pz\beta^2}{2\pi}\int_0^\infty
\frac{t\,e^{-\beta qzt-\beta\sqrt{r^2+t^2}}}{r^2+t^2}
\left(1+\frac{1}{\beta\sqrt{r^2+t^2}}\right)dt.
\end{aligned}
\]

The identity is valid for all stated real parameters. In a sufficiently small complex neighborhood of \(z=1\), the integral is analytic and bounded in absolute value by \(C e^{-\beta r}/r^2\) as \(r\to\infty\): use \(\sqrt{r^2+t^2}\ge r\), \(r^2+t^2\ge r^2\), and \(\Re(qz)>0\) to dominate the \(t\)-integral by \(\int_0^\infty t e^{-\beta\Re(qz)t}dt\). The first term is of order \(e^{-\kappa(z)r}/\sqrt r\); because \(0<\kappa(1)=\beta s<\beta\), it dominates the remainder exponentially, uniformly for complex \(z\) close to one.

**4. Conditional cumulants and Gaussian limit.** The classical uniform large-argument Bessel expansion \(K_0(w)=\sqrt{\pi/(2w)}\,e^{-w}(1+O(w^{-1}))\), valid on an appropriate complex sector, gives, for complex \(t\) close to zero,

\[
\log\mathbb E[e^{tK}\mid R=r]
=r[\kappa(1)-\kappa(e^t)]+2t
+\frac12\log\!\left(\frac{\kappa(1)}{\kappa(e^t)}\right)
+O(r^{-1}).
\]

The error term is analytic and locally uniform in \(t\), so Cauchy's differentiation estimate also controls its first two derivatives by \(O(r^{-1})\). Direct differentiation yields

\[
-\left.\frac{d}{dt}\kappa(e^t)\right|_{t=0}=a,\qquad
-\left.\frac{d^2}{dt^2}\kappa(e^t)\right|_{t=0}=b.
\]

The first two derivatives of \(2t+\frac12\log(\kappa(1)/\kappa(e^t))\) at zero are \(2+q^2/(2s^2)\) and \(q^2/s^4\), respectively. This proves both moment expansions. Substituting \(t=h/\sqrt{br}\) and centering by \(ar\) in the log moment generating function gives \(h^2/2+o(1)\) for every fixed real \(h\). The moment-generating-function continuity theorem proves the conditional standard Gaussian limit.

## Verification

The standalone script `verify_posterior.py` (Python 3, NumPy and SciPy) independently evaluates the conditional Gamma–Bessel densities and the positive Fourier inversion formula, checks normalization on selected indices, tests strict likelihood-ratio inequalities on a finite grid, and compares the exact conditional moments with the predicted large-radius expansions. Invoke `python verify_posterior.py` from this directory; the recorded run is in `verification_output.txt`. This is a numerical consistency check, not a replacement for the two analytic arguments or for the complex-uniform asymptotic estimate.

## Relationship to prior work

Orsingher and Marchione, *Killing random motions with finite velocity* (arXiv:2610.15094; first submitted 2026-10-10), establish the same killed planar process, geometric killing-index law, conditional Bessel densities (Theorems 7 and 9), and the unconditional terminal-position density (Theorems 8, 10 and 11). Those are starting formulas, not claimed as discoveries here. Their Section 4 investigates the distribution of position given a killing index and the survival-conditioned process; the present theorem instead conditions the **killing index on the final observed radius**, proves strict posterior likelihood-ratio ordering, and obtains its sharp far-radius conditional normal law with explicit mean/variance shifts. The positive marked-density inversion isolates the mechanism determining the asymptotic cumulants.

Kolesnik and Orsingher's classical infinite-direction planar random-flight theory concerns positions at fixed observation times and provides background for the segment process. The Gamma–Gaussian variance-mixture and Bessel-transform identities are classical analytical tools, not independently claimed innovations.

## Limitations

The radius is conditioned via a regular density at each \(r>0\); no result is asserted at \(r=0\). The result requires independent isotropic directions, exponential interarrival times and a fixed eventwise killing probability strictly between zero and one. Asymptotic error constants may depend on fixed parameters, and no uniformity as \(p\to0\) or \(p\to1\) is claimed. The inference law does not address directionally persistent flights, non-Poisson renewal laws or pathwise reconstruction. Full historical priority, including possible equivalents under general variance-mixture total positivity or compound-geometric saddlepoint theory, remains unverified; there is no independent mathematical audit.

## References

1. E. Orsingher and M. M. Marchione, *Killing random motions with finite velocity*, arXiv:2610.15094, first submitted 2026-10-10. Section 4, Theorems 7–11. https://arxiv.org/abs/2610.15094
2. A. D. Kolesnik and E. Orsingher, *A planar random motion with an infinite number of directions controlled by the damped wave equation*, Journal of Applied Probability **42** (2005), 1168–1182. DOI: 10.1239/jap/1134587824.
3. A. D. Kolesnik, *Integral equation for the transition density of the multidimensional Markov random flight*, arXiv:1601.06998 (2016). https://arxiv.org/abs/1601.06998
4. G. N. Watson, *A Treatise on the Theory of Bessel Functions*, standard integral and large-argument asymptotic formulas for modified Bessel functions.
