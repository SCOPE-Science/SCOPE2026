# A square-root-five phase boundary in inverse-Gaussian central-mass Gaussianization
## Finding
Let \(X_{\mu,\lambda}\) have the inverse-Gaussian distribution with mean parameter \(\mu>0\) and shape parameter \(\lambda>0\). Define the dimensionless concentration parameter and the variance-one standardization by
\[
\kappa=\frac{\lambda}{\mu},
\qquad
Z_\kappa=\frac{X_{\mu,\lambda}-\mu}{\sqrt{\mu^3/\lambda}}.
\]
Write \(\Phi\) and \(\varphi\) for the standard normal distribution and density. For every fixed \(c>0\),
\[
\Pr\{|Z_\kappa|\le c\}
=2\Phi(c)-1
+\frac{c^3(5-c^2)\varphi(c)}{4\kappa}
-\frac{c^5(c^2-7)(c^4-18c^2+27)\varphi(c)}{192\kappa^2}
+O_c(\kappa^{-3})
\]
as \(\kappa\to\infty\).

The coefficient of \(\kappa^{-1}\) changes sign exactly at \(c=\sqrt5\). Thus, for every fixed \(0<c<\sqrt5\), the inverse-Gaussian central mass is eventually larger than \(2\Phi(c)-1\), whereas for every fixed \(c>\sqrt5\) it is eventually smaller. At the boundary the first correction vanishes, but the next one is strictly negative:
\[
\Pr\{|Z_\kappa|\le\sqrt5\}-(2\Phi(\sqrt5)-1)
=-\frac{19(\sqrt5)^5\varphi(\sqrt5)}{48\kappa^2}+O(\kappa^{-3}).
\]
Hence \(\sqrt5\) is the sharp local radius boundary for the direction from which concentrated inverse-Gaussian laws approach Gaussian central-window probabilities.

At \(c=1\), the expansion becomes
\[
\Pr\{|Z_\kappa|\le1\}
=2\Phi(1)-1+\frac{\varphi(1)}{\kappa}+\frac{5\varphi(1)}{16\kappa^2}+O(\kappa^{-3}),
\]
quantifying the one-standard-deviation inequality proved for the inverse-Gaussian family in the motivating literature.

## Assumptions and scope
The result holds for arbitrary \(\mu,\lambda>0\) through the single ratio \(\kappa=\lambda/\mu\). The radius \(c>0\) is fixed while \(\kappa\to\infty\). The theorem is an asymptotic statement: it gives eventual comparison at each fixed radius and does not assert a finite-\(\kappa\) global sign classification for every \(c\).

The central interval lies inside the support whenever \(\kappa>c^2\), which is automatic in the asymptotic regime. No claim is made about the normal-inverse-Gaussian distribution; the object here is the ordinary inverse-Gaussian first-passage law.

## Proof
Scaling \(X_{\mu,\lambda}\) by \(\mu\) reduces the family to mean one and shape \(\kappa=\lambda/\mu\). Put \(\varepsilon=\kappa^{-1/2}\). From the exact inverse-Gaussian density, the density of \(Z_\kappa\) is
\[
g_\varepsilon(z)=\varphi(z)
(1+\varepsilon z)^{-3/2}
\exp\!\left(\frac{z^2}{2}-\frac{z^2}{2(1+\varepsilon z)}\right),
\qquad z>-\varepsilon^{-1}.
\]
For fixed \(c\) and sufficiently small \(\varepsilon\), this expression is analytic uniformly for \(|z|\le c\). Moreover
\[
g_\varepsilon(-z)=g_{-\varepsilon}(z),
\]
so the symmetric central integral \(I_c(\varepsilon)=\int_{-c}^c g_\varepsilon(z)\,dz\) is an even analytic function of \(\varepsilon\).

Expanding the density ratio through fourth order gives
\[
\frac{g_\varepsilon(z)}{\varphi(z)}
=1+\text{odd terms in }\varepsilon
+\varepsilon^2 A_2(z)+\varepsilon^4 A_4(z)+O_c(\varepsilon^6),
\]
inside the symmetric integral, where
\[
A_2(z)=\frac{z^6-10z^4+15z^2}{8},
\]
and
\[
A_4(z)=\frac{z^{12}}{384}-\frac{3z^{10}}{32}+\frac{63z^8}{64}-\frac{105z^6}{32}+\frac{315z^4}{128}.
\]
The odd coefficients integrate to zero by the displayed symmetry. For the even coefficients, direct differentiation of a polynomial times \(\varphi\) gives
\[
\int_{-c}^c A_2(z)\varphi(z)\,dz
=\frac{c^3(5-c^2)\varphi(c)}{4},
\]
and
\[
\int_{-c}^c A_4(z)\varphi(z)\,dz
=-\frac{c^5(c^2-7)(c^4-18c^2+27)\varphi(c)}{192}.
\]
Since \(I_c\) is even analytic near \(0\), the next omitted integrated term is \(O_c(\varepsilon^6)\). Substituting \(\varepsilon^2=1/\kappa\) proves the expansion.

For \(c\ne\sqrt5\), the sign of the leading correction is the sign of \(5-c^2\). At \(c=\sqrt5\), substitution into the second coefficient gives
\[
-\frac{19(\sqrt5)^5\varphi(\sqrt5)}{48},
\]
which is negative. This proves the phase statement and the one-standard-deviation specialization.

## Verification
The accompanying exact-arithmetic checker reconstructs the formal density-ratio series from the logarithm of the exact standardized density, verifies the displayed \(A_2\) and \(A_4\) polynomials, and verifies polynomial antiderivatives for both integrated coefficients. It also performs supplementary numerical quadrature at several radii and large \(\kappa\) values. Those numerical checks are regression tests only; the proof is the uniform analytic Taylor expansion above.

## Relationship to prior work
Sun, Hu, and Sun study the same inverse-Gaussian family and prove that its one-standard-deviation central probability is at least the Gaussian value. Their Section 6 works with the exact inverse-Gaussian CDF and proves the fixed-radius comparison corresponding to \(c=1\). The inspected source does not state a fixed-\(c\) Gaussianization expansion, the \(\sqrt5\) sign boundary, or either coefficient above.

Hu, Song, and Tan later study anti-concentration functions over a range of standardized radii for several familiar distribution families. The public record lists uniform, exponential, Gaussian, Student, binomial, Poisson, negative-binomial, hypergeometric, Gamma, Pareto, Weibull, log-normal, and Beta families; inverse Gaussian is not among the families treated in that paper's stated scope.

Targeted searches for inverse-Gaussian central-window expansions, Edgeworth formulations, the coefficient \(5-c^2\), and a \(\sqrt5\) crossover did not locate a statement implying this phase theorem.

## Limitations
The theorem is local to the concentrated regime \(\kappa\to\infty\) with fixed \(c\). It does not determine every finite-shape crossing in \(c\), nor does it claim monotonicity in \(\kappa\) at general radii. The originality search cannot rule out an equivalent asymptotic hidden in older inverse-Gaussian approximation literature under different notation.

## References
1. Ping Sun, Ze-Chun Hu, and Wei Sun, *Variation comparison between infinitely divisible distributions and the normal distribution*, arXiv:2304.11459, first public version 2023-04-22; *Statistical Papers* 65 (2024), 4405–4429, DOI:10.1007/s00362-024-01561-1.
2. Ze-Chun Hu, Renming Song, and Yuan Tan, *On the anti-concentration functions of some familiar families of distributions*, arXiv:2401.09998, first public version 2024-01-18; *Mathematical Theory and Applications* 44 (2024), 1–15.
