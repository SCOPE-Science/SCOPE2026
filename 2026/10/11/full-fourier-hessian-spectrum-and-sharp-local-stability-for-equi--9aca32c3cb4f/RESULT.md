# Full Fourier Hessian spectrum and sharp local stability for equispaced Bergman poles

## Finding
Fix an integer \(N\ge2\). For angles \(\boldsymbol\theta=(\theta_0,\ldots,\theta_{N-1})\in\mathbb R^N\), let
\[
\mathcal E_N(\boldsymbol\theta)=\frac{2}{\pi}\int_{|z|<1}\left|\sum_{j=0}^{N-1}\frac1{z-e^{i\theta_j}}\right|^2(1-|z|^2)\,dA(z),
\]
with unnormalized planar area \(dA\). At the regular configuration \(\theta_j^\star=2\pi j/N\), its full real angle Hessian has the Fourier eigenvector \((e^{2\pi i s j/N})_{j=0}^{N-1}\) and eigenvalue \(\lambda_s\), for \(0\le s<N\), where \(\lambda_0=0\) and
\[
\boxed{\lambda_s=2N\int_0^1\frac{(1-t^s)(1-t^{N-s})}{1-t^N}\,dt
=2N+2\left[\psi\!\left(\frac{s+1}{N}\right)+\psi\!\left(\frac{N-s+1}{N}\right)-2\psi\!\left(1+\frac1N\right)\right]}
\quad (1\le s<N),
\]
where \(\psi=\Gamma'/\Gamma\). All the nonrotational eigenvalues are positive. Their exact extremal modes are
\[
\boxed{\lambda_{\min}=\lambda_1=\lambda_{N-1}
=N+2\left[\psi\!\left(1+\frac2N\right)+\psi(1)-2\psi\!\left(1+\frac1N\right)\right],}
\]
and
\[
\boxed{\lambda_{\max}=\lambda_{\lfloor N/2\rfloor}=\lambda_{\lceil N/2\rceil}.}
\]
For fixed \(N\), write \(\varepsilon_j^\circ=\varepsilon_j-N^{-1}\sum_k\varepsilon_k\). The coefficient in the local stability law
\[
\mathcal E_N(\boldsymbol\theta^\star+\boldsymbol\varepsilon)-\mathcal E_N(\boldsymbol\theta^\star)
\ge\frac{\lambda_{\min}}2\sum_j|\varepsilon_j^\circ|^2+o\!\left(\sum_j|\varepsilon_j^\circ|^2\right)
\]
is sharp, attained asymptotically along the first nonconstant Fourier mode. As \(N\to\infty\),
\[
\boxed{\lambda_{\min}=N-\frac{4\zeta(3)}{N^2}+\frac{12\zeta(4)}{N^3}+O(N^{-4}),\qquad
\lambda_{\max}=2N-8\log 2+o(1),\qquad
\frac{\lambda_{\max}}{\lambda_{\min}}\longrightarrow 2.}
\]
Thus, after quotienting simultaneous rotation, the local angle Hessian is asymptotically uniformly conditioned, with sharp limiting condition number two.

## Assumptions and scope
The weight is exactly the critically weighted Bergman weight \(1-|z|^2\) and the squared norm uses the factor \(2/\pi\). Poles lie on the boundary unit circle; near the equispaced configuration the poles remain distinct. Hessian derivatives are with respect to ordinary real angles in radians. The zero eigenvalue is forced by joint rotation. Statements about local stability are for each fixed \(N\) and sufficiently small angle perturbations; they do not assert a global quadratic estimate. The primary classification is MSC2020 \(30\mathrm{H}20\) (Bergman spaces and Fock spaces).

## Proof
**Moment reduction.** For each integer \(m\ge0\), direct radial integration gives
\[
\frac2\pi\int_{|z|<1}|z|^{2m}(1-|z|^2)\,dA(z)
=\frac{2}{(m+1)(m+2)}.
\]
Expanding each pole as a power series inside the disk yields the absolutely convergent identity
\[
\mathcal E_N(\boldsymbol\theta)=\sum_{n=1}^\infty\frac{2}{n(n+1)}\left|\sum_{j=0}^{N-1}e^{in\theta_j}\right|^2
=2N+2\sum_{0\le j<k<N}\phi(\theta_j-\theta_k),
\]
where
\[
\phi(\theta)=2\sum_{n=1}^\infty\frac{\cos(n\theta)}{n(n+1)}.
\]
The first equality is norm convergence; the second follows from expanding the squares and the telescoping sum \(\sum_{n\ge1}2/[n(n+1)]=2\). For \(\theta\notin2\pi\mathbb Z\), putting \(w=e^{i\theta}\) gives
\[
\phi(\theta)=2\operatorname{Re}\left[1+(w^{-1}-1)\log(1-w)\right].
\]
Differentiating this expression, or integrating the Fourier coefficients with an Abel factor, gives the positive Poisson representation
\[
\phi''(\theta)=1+2\operatorname{Re}\int_0^1\frac{t e^{i\theta}}{1-t e^{i\theta}}\,dt
=\int_0^1\frac{1-t^2}{1-2t\cos\theta+t^2}\,dt>0.
\]
All differentiations here occur a positive angular distance from collisions.

**Circulant curvature.** The regular polygon is stationary, because its gradient is constant by cyclic symmetry and orthogonal to the all-ones vector by rotational invariance. If \(w_r=\phi''(2\pi r/N)\), then the Hessian \(H\) at the regular polygon has
\[
H_{jj}=2\sum_{r=1}^{N-1}w_r,\qquad H_{jk}=-2w_{j-k\bmod N}\quad(j\ne k).
\]
Therefore it is real symmetric and circulant. Fourier diagonalization gives
\[
\lambda_s=2\sum_{r=1}^{N-1}w_r\left(1-\cos\frac{2\pi sr}{N}\right).
\]
With \(P_t(\theta)=(1-t^2)/(1-2t\cos\theta+t^2)\), the absolutely convergent Poisson series for \(0<t<1\) yields the exact cyclic identities
\[
\sum_{r=0}^{N-1}P_t(2\pi r/N)=N\frac{1+t^N}{1-t^N},\qquad
\sum_{r=0}^{N-1}P_t(2\pi r/N)\cos(2\pi sr/N)=N\frac{t^s+t^{N-s}}{1-t^N}
\]
for \(1\le s<N\). Since the term at \(r=0\) cancels after taking the difference, substituting the Poisson representation gives
\[
\lambda_s=2N\int_0^1\frac{1+t^N-t^s-t^{N-s}}{1-t^N}\,dt
=2N\int_0^1\frac{(1-t^s)(1-t^{N-s})}{1-t^N}\,dt.
\]
The integrand has a removable zero at \(t=1\), is positive for \(0<t<1\), and the formula is valid without differentiating a conditionally convergent series.

**Closed form and extremizers.** Expanding \((1-t^N)^{-1}\) and grouping the four terms before integrating, the convergent digamma-difference identity yields
\[
\lambda_s=2\left[\psi\!\left(\frac{s+1}{N}\right)+\psi\!\left(\frac{N-s+1}{N}\right)-\psi\!\left(\frac1N\right)-\psi\!\left(1+\frac1N\right)\right].
\]
The recurrence \(\psi(x+1)=\psi(x)+1/x\) produces the displayed formula in the finding. For any \(0<t<1\), the real-variable function \(s\mapsto t^s+t^{N-s}\) is strictly convex and symmetric about \(N/2\). Consequently the integral is smallest at \(s=1,N-1\) and largest at the integer(s) nearest \(N/2\). In particular, all nonrotational eigenvalues are strictly positive.

**Sharp local stability.** Smoothness of the energy near distinct poles and stationarity give
\[
\mathcal E_N(\boldsymbol\theta^\star+\boldsymbol\varepsilon)-\mathcal E_N(\boldsymbol\theta^\star)
=\tfrac12\boldsymbol\varepsilon^{\circ T}H\boldsymbol\varepsilon^\circ+O_N(\|\boldsymbol\varepsilon^\circ\|_2^3).
\]
The spectral theorem proves the sharp quadratic coefficient \(\lambda_{\min}/2\). Choosing a real first Fourier mode makes the quadratic Rayleigh quotient exactly \(\lambda_{\min}\); along a scalar multiple of that mode the remainder divided by the squared norm tends to zero.

**Large-polygon regime.** Using \(\psi(1+u)=-\gamma+\sum_{k\ge1}(-1)^{k+1}\zeta(k+1)u^k\) for \(|u|<1\), the formula for \(\lambda_{\min}\) gives its two displayed correction terms. For \(s=\lfloor N/2\rfloor\), setting \(t=e^{-u/N}\) in the positive integral gives
\[
2N-\lambda_s=2\int_0^\infty e^{-u/N}\frac{e^{-su/N}+e^{-(N-s)u/N}-2e^{-u}}{1-e^{-u}}\,du.
\]
Since \(s/N\to1/2\), the integrand tends to \(2/(e^{u/2}+1)\) before the outside factor two. Dominated convergence (boundedness near \(u=0\) and uniform exponential decay for \(u\ge1\)) makes the limit \(4\int_0^\infty(e^{u/2}+1)^{-1}du=8\log2\). The ratio of the extremal eigenvalues therefore tends to two.

## Verification
The standalone file `check_spectrum.py` uses only the Python standard library. Running `python3 check_spectrum.py` checks, for several finite polygon sizes, agreement between the direct curvature eigenvalues and Poisson integrals, the extremizing Fourier modes, and separately computed second differences of the original squared Bergman energy. The reported result was `PASS: Poisson integral, direct Hessian, modal extrema, finite differences`. As an exact boundary check, \(N=2\) gives \(\lambda_1=8\log2-4>0\). These experiments supplement, but cannot replace, the all-\(N\) analytic proof above.

## Relationship to prior work
Abakumov, Borichev, and Fedorovskiy (2020) prove global equispaced-pole minimization and derive strict convexity of the pair interaction for this weight; their Lemma 12 includes a Fourier representation of the second derivative. Corbett (2026) proves global minimization through a Hessian argument and through universal discrete-energy optimality, but does not give the full circulant Hessian spectrum or its sharp modal condition number. Bezrukov (2026) proves a more general global Chui minimization principle, not quantitative second variations for the fixed weighted Hilbert norm. The present finding gives exact nonrotational eigenvalues, identifies the least and greatest curvature modes, and determines the sharp local stability coefficient and asymptotic condition number. Equivalent unindexed work may exist.

## Limitations
No claim is made for weights other than \(1-|z|^2\), for globally separated configurations beyond local perturbations, or for the unweighted \(L^1\) Chui functional. The error term in the local expansion is for fixed \(N\), not uniform over all polygon sizes. The numerical checker samples finitely many cases; the infinite family is justified by the Poisson and digamma identities. The source literature comparison cannot exclude all unpublished or unindexed equivalents.

## References
1. Georgia Corbett, *Two new proofs of Chui's Conjecture in Weighted Bergman Spaces*, arXiv:2609.21121v1, first public 2026-09-17, https://arxiv.org/html/2609.21121v1 (especially Sections 1.1, 2.3, and 3).
2. Evgeny Abakumov, Alexander Borichev, and Konstantin Fedorovskiy, *Chui's conjecture in Bergman spaces*, arXiv:2009.01898v1, first public 2020-09-03, https://arxiv.org/html/2009.01898v1 (especially Theorem 1 and Lemma 12).
3. Egor Bezrukov, *Proof of the generalized Chui conjecture*, arXiv:2609.03134v1, first public 2026-09-02, https://arxiv.org/html/2609.03134v1 (Theorems 1 and 2 and proof).
