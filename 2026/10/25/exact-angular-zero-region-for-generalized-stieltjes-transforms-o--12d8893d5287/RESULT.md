# Exact angular zero region for generalized Stieltjes transforms of interval-supported measures

## Finding

Let \(0\le a<b<\infty\), let \(\lambda>0\), and let \(\mu\) range over all nonzero finite positive Borel measures supported on \([a,b]\). Define

\[
S_{\lambda,\mu}(z)=\int_{[a,b]}(z+t)^{-\lambda}\,d\mu(t),\qquad z\in\Omega_a:=\mathbb C\setminus(-\infty,-a],
\]

where the power uses the principal branch, positive on the positive real axis. Put

\[
\Theta(z)=\left|\arg(z+a)-\arg(z+b)\right|,
\]

with principal arguments. The exact union of zero locations attainable as \(\mu\) varies is

\[
\mathcal Z_{\lambda,[a,b]}=\left\{z\in\Omega_a:\Theta(z)\ge\frac{\pi}{\lambda}\right\}.
\]

In particular, every zero of any fixed \(S_{\lambda,\mu}\) lies in this region; conversely, each point of the region is a zero for some positive measure with at most two atoms. Since \(\Theta(z)<\pi\) throughout \(\Omega_a\), no such transform has a zero when \(0<\lambda\le1\). At \(\lambda=2\), the region is exactly the nonreal part of the disk with diameter \([-b,-a]\).

## Assumptions and scope

The measure is finite, nonzero, positive, and supported on the compact interval \([a,b]\) with \(0\le a<b\). The transform is considered only on the slit plane \(\Omega_a\), so \(z+t\) never lies on the branch cut or vanishes. The theorem classifies the union of possible zero locations over the measure class; it does not assert that every measure has a zero at every point in the region.

## Proof

Fix \(z=x+iy\in\Omega_a\). If \(y=0\), then \(z>-a\), so \(z+t>0\) for all \(t\in[a,b]\), and positivity of \(\mu\) gives \(S_{\lambda,\mu}(z)>0\). Thus real points of the domain are not zeros.

Suppose \(y\ne0\), and write \(\theta(t)=\arg(z+t)\). Differentiation gives

\[
\theta'(t)=-\frac{y}{(x+t)^2+y^2},
\]

so \(\theta\) is continuous and strictly monotone on \([a,b]\), with total variation \(\Theta(z)\in(0,\pi)\). The integrand has the form

\[
(z+t)^{-\lambda}=|z+t|^{-\lambda}e^{-i\lambda\theta(t)}.
\]

If \(\lambda\Theta(z)<\pi\), rotate the integrand by \(e^{i\lambda(\theta(a)+\theta(b))/2}\). Every rotated value has argument in the open interval \((-\lambda\Theta(z)/2,\lambda\Theta(z)/2)\subset(-\pi/2,\pi/2)\), hence strictly positive real part. Integrating against a nonzero positive measure preserves strict positivity of the real part, so \(S_{\lambda,\mu}(z)\ne0\). Therefore a zero requires \(\Theta(z)\ge\pi/\lambda\).

Conversely, suppose \(\Theta(z)\ge\pi/\lambda\). Necessarily \(\lambda>1\), because \(\Theta(z)<\pi\). By continuity and strict monotonicity of \(\theta\), there are distinct \(t_1,t_2\in[a,b]\) such that

\[
|\theta(t_1)-\theta(t_2)|=\frac{\pi}{\lambda}.
\]

Choose the positive two-atom measure

\[
\mu=|z+t_1|^{\lambda}\,\delta_{t_1}+|z+t_2|^{\lambda}\,\delta_{t_2}.
\]

Its transform at \(z\) is the sum of two unit complex numbers whose arguments differ by exactly \(\pi\), so the sum is zero. This proves attainability and the exact union formula.

For \(\lambda=2\), the condition \(\Theta(z)\ge\pi/2\) is equivalent to

\[
\operatorname{Re}\big((z+a)\overline{(z+b)}\big)\le0
\quad\Longleftrightarrow\quad
\left|z+\frac{a+b}{2}\right|^2\le\frac{(b-a)^2}{4}.
\]

The slit removes the real diameter, leaving the nonreal part of the disk. This also checks the classical squared-resolvent case.

## Verification

The proof covers all \(\lambda>0\), all allowed support intervals, and all nonzero finite positive measures. The branch domain and the real-axis case are handled explicitly. The necessary condition follows from a strict half-plane separation; sharpness follows from a two-atom construction, not from numerical evidence. No numerical experiment or external certificate is needed. The result concerns attainable zero locations as the measure varies; it does not determine the zeros for a particular fixed measure.

## Relationship to prior work

Karp and Prilepkina develop the generalized Stieltjes-transform framework for arbitrary positive order and discuss its complex-variable properties. Their inspected full text includes order-dependent sector mappings and a global estimate, but it does not state the endpoint-dependent visual-angle region above or the two-atom attainability criterion. The result here sharpens that general framework for measures supported on a known compact interval by identifying the exact geometric region in which cancellation is possible. At order \(\lambda=2\), the visual-angle criterion reduces to the disk with diameter \([-b,-a]\). A related 1980 paper on real inversion theorems was located, but its full text was not available for inspection; this remains a limitation on the literature comparison.

## Limitations

The theorem is an exact classification of the union of attainable zeros, not a classification of the zero set for each fixed measure. It uses a compact interval of support and the principal branch on the slit plane. The full text of one related inversion paper could not be inspected, so the originality assessment is not an exhaustive novelty proof. Independent audit has not been performed.

## References

1. D. Karp and E. Prilepkina, “Generalized Stieltjes transforms: basic aspects,” arXiv:1111.4271v1 (first public version dated 18 November 2011); journal version, *Journal of Classical Analysis* 1(1) (2012), 53–74, DOI: 10.7153/jca-01-07.
2. E. R. Love and A. Byrne, “Real Inversion Theorems for Generalized Stieltjes Transforms,” *Journal of the London Mathematical Society* (2) 22 (1980), 285–306, DOI: 10.1112/jlms/s2-22.2.285. Abstract inspected; full text not available in this run.
