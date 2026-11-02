# Eventual alternating signs of a stationary quenched-current transform

## Finding

Consider a half-line initially populated at density \(\rho>0\) by independent particles that reset to their own initial locations. Let \(Q\) count particles lying to the right of the origin in the stationary limit. For either Brownian particles with diffusivity \(D>0\) and reset rate \(r>0\), or symmetric run-and-tumble particles of speed \(v>0\), tumble rate \(\gamma\geq0\), and simultaneous position/velocity randomization at rate \(r>0\), define

\[
\kappa=\begin{cases}\sqrt{r/D}&\text{Brownian motion},\\[2pt]
\sqrt{r(r+2\gamma)}/v&\text{run-and-tumble motion},\end{cases}
\qquad \lambda=\rho/\kappa>0.
\]

The *logarithmically averaged* or geometric-ensemble current functional associated with the source's quenched cumulant prescription is

\[
G_\lambda(z)=\exp\!\left[-\lambda\,\operatorname{Li}_2\!\left(\frac{1-z}{2}\right)\right]
=\sum_{n\geq0}c_n(\lambda)z^n,\qquad |z|<1.
\]

For each fixed \(\lambda>0\), its coefficients obey the sharp alternating asymptotic law

\[
\boxed{c_n(\lambda)=(-1)^{n+1}\frac{\lambda e^{-\lambda\pi^2/6}}{2n(n-1)}
+O_\lambda\!\left(\frac{\log n}{n^3}\right),\quad n\to\infty.}
\]

In particular, all sufficiently large **even** coefficients are strictly negative, and all sufficiently large **odd** coefficients are strictly positive. Consequently this functional is **not** the probability-generating function of any nonnegative integer-valued law, for any finite positive \(\lambda\). Nor can \(G_\lambda(e^{-p})\) be the Laplace transform of a nonnegative law on \([0,\infty)\). A finite-order witness is

\[
c_2(\lambda)=\frac{\lambda e^{-\lambda\operatorname{Li}_2(1/2)}}{2}
\bigl[\lambda(\log 2)^2+\log 2-1\bigr]<0
\quad\Longleftrightarrow\quad
0<\lambda<\frac{1-\log 2}{(\log 2)^2}.
\]

These statements describe a **formal averaged-log transform**, not negative probabilities for any actual fixed-particle configuration. For actual fixed positions, the current law remains a genuine Poisson-binomial law; under annealed Poisson initial positions it is Poisson with mean \(\lambda/2\).

## Assumptions and scope

All rates and diffusivities above are finite; the reset rate and initial density are strictly positive. Run-and-tumble velocity is independently reassigned to either sign with equal probability after every reset, with Poisson tumbles reversing velocity. The stationary single-particle probability of appearing on the opposite side from a start at distance \(x\geq0\) is \(U(x)=e^{-\kappa x}/2\). The geometric-ensemble functional is constructed by exponentiating the *spatially averaged logarithm* of the fixed-configuration probability-generating function. It should not be confused with either the fixed-configuration generating function or its arithmetic ensemble average. The asymptotic is pointwise for fixed \(\lambda>0\), not uniform in a simultaneous limit where \(\lambda\) grows with the count \(n\).

## Proof

**1. Exact stationary transform.** The reset-resolvent for Brownian motion gives the centered stationary Laplace density \(\kappa e^{-\kappa |y|}/2\) with \(\kappa=\sqrt{r/D}\). For symmetric run-and-tumble motion the corresponding two-velocity stationary resolvent gives the same Laplace density with \(\kappa=\sqrt{r(r+2\gamma)}/v\); equivalently the source's single-particle crossing transform has limit \(U(x)=e^{-\kappa x}/2\). Thus every particle started at \(-x\) lies to the right with probability \(U(x)\), and for fixed positions \(x_j\) its exact generating function is \(\prod_j[1-U(x_j)+zU(x_j)]\). Spatial averaging of the logarithm and exponentiating yields

\[
\log G_\lambda(z)=\rho\int_0^\infty
\log\left(1-\frac{1-z}{2}e^{-\kappa x}\right)dx
=-\lambda\sum_{j\geq1}\frac{((1-z)/2)^j}{j^2}
=-\lambda\operatorname{Li}_2((1-z)/2).
\]

The integral and series equalities hold first for \(|1-z|<2\), then by analytic continuation on the slit plane \(\mathbb C\setminus(-\infty,-1]\).

**2. Dominant logarithmic singularity.** Put \(w=1+z\). The standard dilogarithm expansion in a slit neighborhood of \(w=0\) is

\[
\operatorname{Li}_2(1-w/2)=\frac{\pi^2}{6}
+\frac{w}{2}\log(w/2)-\frac w2+O(w^2\log w).
\]

It follows, in a common dented neighborhood of the unique unit-circle singularity \(z=-1\), that

\[
G_\lambda(z)=e^{-\lambda\pi^2/6}
\left[1-\frac{\lambda}{2}(1+z)\log(1+z)
+\frac{\lambda(1+\log2)}{2}(1+z)
+O_\lambda\!((1+z)^2\log^2(1+z))\right].
\]

There are no other singularities on \(|z|=1\), because the principal dilogarithm is analytic off its cut \([1,\infty)\), whose inverse image under \((1-z)/2\) is \(( -\infty,-1]\). Singularity transfer for logarithmic functions applies in a dented disk. The elementary exact coefficient identity

\[
[z^n](1+z)\log(1+z)=\frac{(-1)^n}{n(n-1)},\qquad n\ge2,
\]

and transfer of the remainder, of order \(O_\lambda(n^{-3}\log n)\), prove the asserted asymptotic. Because \(\lambda e^{-\lambda\pi^2/6}>0\), the eventual signs follow.

**3. Impossibility of an ordinary law.** An integer-valued probability law has a generating function with nonnegative Taylor coefficients, contradicting the eventual negative even coefficients. An independent obstruction is Pringsheim's theorem: \(G_\lambda\) has radius of convergence exactly one due to the branch point at \(z=-1\), yet is analytic at \(z=+1\); a power series with nonnegative coefficients and finite radius one would have a singularity at \(z=+1\). Suppose instead that \(F(p)=G_\lambda(e^{-p})\) were the Laplace transform of a nonnegative measure on \([0,\infty)\). Analyticity gives \(F(p+2\pi i)=F(p)\). For real \(p>0\), taking real parts under the integral implies

\[
\int_0^\infty e^{-px}\bigl[1-\cos(2\pi x)\bigr]d\mu(x)=0.
\]

The integrand is nonnegative, so the measure must be supported on the nonnegative integers. Its Laplace transform would then have nonnegative integer Taylor coefficients, already contradicted. Thus even a continuous nonnegative distribution cannot have this Laplace transform.

**4. Explicit low-order coefficient.** Differentiation yields

\[
\frac{G_\lambda'(z)}{G_\lambda(z)}
=\lambda\frac{\log2-\log(1+z)}{1-z}
=\lambda\sum_{j\ge0}\left(\log2-\sum_{k=1}^{j}\frac{(-1)^{k+1}}k\right)z^j.
\]

The coefficients satisfy the triangular recurrence

\[
(n+1)c_{n+1}=\lambda\sum_{j=0}^{n}
\left(\log2-\sum_{k=1}^{j}\frac{(-1)^{k+1}}k\right)c_{n-j},
\quad c_0=e^{-\lambda\operatorname{Li}_2(1/2)}.
\]

The recurrence gives the stated exact \(c_2\) and the threshold \((1-\log2)/(\log2)^2=0.6386739401\ldots\).

## Verification

Run `python3 verify_coefficients.py` from the directory containing this document. The program requires only the Python standard library and checks the explicit second coefficient, six choices of \(\lambda\), the recurrence through degree 240, signed far-tail samples, agreement with the leading asymptotic, and numerical quadrature against the dilogarithm series. These computations supplement but do not replace the analytic branch-point proof. Actual run output is reported in `VERIFICATION.md`.

## Relationship to prior work

Di Bello et al. (2023), Sections III.2 and IV.2, derive the logarithmically averaged current transform and its stationary dilogarithm form. Their formulas supply the exact starting object; the present finding does **not** claim discovery of that transform, the underlying resetting model, or its ordinary cumulants. Their discussion notes difficulty in extracting the full stationary current distribution from the complex transform. The contribution assessed here is a global *nonrealizability theorem* with a sharp signed tail for every finite density-to-reset-length ratio, and the distinction between that formal logarithmic average and actual conditional probability distributions. The standard singularity-transfer method used in the proof is also prior mathematics. Earlier work of Derrida and Gerschenfeld introduced quenched-versus-annealed current fluctuation methods for nonreset diffusive systems; it does not itself give the above fixed-reset-rate, all-parameter signed-tail statement.

## Limitations

The mathematical claim is about a particular geometric-ensemble transform, not the physical probabilities at a specified initial configuration, and it does not negate the usefulness of the transform for scaled cumulants or asymptotic large-deviation calculations in their proper joint limits. It does not assert that any physical current probability is negative. Large-\(n\) estimates assume fixed finite \(\lambda\); noncommuting limits with \(\lambda\to\infty\) are not covered. Final publication priority and independently repeated scientific review remain open.

## References

1. C. Di Bello, A. K. Hartmann, S. N. Majumdar, F. Mori, A. Rosso and G. Schehr, *Current fluctuations in stochastically resetting particle systems*, arXiv:2302.06696v1 (13 February 2023), especially Sections III.2, IV.2 and V.2. https://arxiv.org/html/2302.06696v1
2. B. Derrida and A. Gerschenfeld, *Current Fluctuations in One Dimensional Diffusive Systems with a Step Initial Density Profile*, arXiv:0907.3294 (2009). https://arxiv.org/abs/0907.3294
3. P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Chapter VI, *Singularity Analysis of Generating Functions*, Cambridge University Press (2009). https://ac.cs.princeton.edu/home/
