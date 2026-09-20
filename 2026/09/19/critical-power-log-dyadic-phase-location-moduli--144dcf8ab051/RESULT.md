# Critical power-log boundary and dyadic phase transition in location moduli

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Wang and Gao (2026) introduced the inverse Hellinger modulus
\[
\omega_f(t)=\sup\{r\ge 0:\mathsf H^2(f_0,f_{2r})\le t\}
\]
and the dyadic quantile functional
\[
\Delta_f(p)=\left(\sum_{j\ge0:\,2^jp\le1/4}
\frac{2^j}{\{q(2^{j+1}p)-q(2^jp)\}^2}\right)^{-1/2},
\]
where \(\mathsf H^2(P,Q)=\frac12\int(\sqrt{dP}-\sqrt{dQ})^2\). They prove a universal constant-factor equivalence between these quantities for symmetric unimodal monotone-hazard-rate densities and study the compactly supported power-log family
\[
f_{\alpha,\kappa}(x)\propto
\frac{(1-x^2)^\alpha}{[\log(e/(1-x^2))]^\kappa}\mathbf 1_{\{|x|<1\}}
\]
for \(0<\alpha<1\).

This record analyzes the critical endpoint \(\alpha=1\), where the power law is exactly at the classical linear-boundary transition. For \(\kappa\ge0\), define
\[
f_\kappa(x)=\frac1{Z_\kappa}
\frac{1-x^2}{[\log(e/(1-x^2))]^\kappa}\mathbf 1_{\{|x|<1\}},
\qquad
a_\kappa=\frac2{Z_\kappa}.
\]
Every \(f_\kappa\) is symmetric and log-concave. Its location Fisher information is finite exactly when \(\kappa>1\).

As \(r\downarrow0\), the squared Hellinger divergence between locations separated by \(2r\) has the sharp asymptotics
\[
\boxed{
\mathsf H^2(f_{\kappa,0},f_{\kappa,2r})\sim
\begin{cases}
\dfrac{a_\kappa}{1-\kappa}\,r^2[\log(1/r)]^{1-\kappa},&0\le\kappa<1,\\[1.1ex]
a_1r^2\log\log(1/r),&\kappa=1,\\[1.1ex]
\dfrac{I_\kappa}{2}r^2,&\kappa>1,
\end{cases}}
\]
where \(I_\kappa\) is the ordinary location Fisher information. Therefore
\[
\boxed{
\omega_\kappa(t)\sim
\begin{cases}
\sqrt{\dfrac{2^{1-\kappa}(1-\kappa)}{a_\kappa}}\,
\sqrt t\,[\log(1/t)]^{-(1-\kappa)/2},&0\le\kappa<1,\\[1.2ex]
a_1^{-1/2}\sqrt{\dfrac{t}{\log\log(1/t)}},&\kappa=1,\\[1.2ex]
\sqrt{\dfrac2{I_\kappa}}\sqrt t,&\kappa>1.
\end{cases}}
\]
Thus the critical power boundary itself contains a second transition: a logarithmically enhanced information regime for \(\kappa<1\), a \(\log\log\) critical point at \(\kappa=1\), and ordinary finite-Fisher root-\(t\) behavior for \(\kappa>1\).

For the entire infinite-Fisher part \(0\le\kappa\le1\), the new dyadic functional has a sharp asymptotic with the same universal relative constant. Specifically,
\[
\boxed{
\Delta_\kappa(p)\sim
(\sqrt2-1)\sqrt{\frac{2^{1-\kappa}(1-\kappa)\log2}{a_\kappa}}
\sqrt p\,[\log(1/p)]^{-(1-\kappa)/2}}
\]
for \(0\le\kappa<1\), while
\[
\boxed{
\Delta_1(p)\sim
(\sqrt2-1)\sqrt{\frac{\log2}{a_1}}
\sqrt{\frac p{\log\log(1/p)}}.}
\]
Consequently,
\[
\boxed{
\frac{\Delta_\kappa(p)}{\omega_\kappa(p)}
\longrightarrow(\sqrt2-1)\sqrt{\log2}
=0.3448554113\ldots,
\qquad 0\le\kappa\le1.}
\]
This sharpens the constant-factor Hellinger--quantile equivalence on a full critical family.

The behavior changes qualitatively once the dyadic energy becomes summable. Put
\[
\ell_\kappa(u)=q_\kappa(2u)-q_\kappa(u),\qquad
g_\kappa(u)=\frac{u}{\ell_\kappa(u)^2},
\]
\[
J_p=\left\lfloor\log_2\frac1{4p}\right\rfloor,
\qquad z_p=2^{J_p}p\in(1/8,1/4].
\]
The exact identity
\[
p\Delta_\kappa(p)^{-2}
=\sum_{m=0}^{J_p}g_\kappa(2^{-m}z_p)
\]
shows that, when \(\kappa>1\), the endpoint contribution is summable. Along every subsequence with \(z_p\to z\in[1/8,1/4]\),
\[
\boxed{
\frac{\Delta_\kappa(p)}{\sqrt p}\longrightarrow
\left[\sum_{m=0}^{\infty}g_\kappa(2^{-m}z)\right]^{-1/2}.}
\]
Thus a fixed dyadic lattice can retain a phase profile rather than forcing a unique leading constant.

This is not merely a possibility. For the standard Laplace density \(f(x)=e^{-|x|}/2\), one has \(q(u)=\log(2u)\) for \(u\le1/2\), hence \(\ell(u)=\log2\) for all dyadic levels entering \(\Delta\). Therefore
\[
\boxed{
\Delta_{\mathrm L}(p)=
\frac{\log2}{\sqrt{2^{J_p+1}-1}}.}
\]
Since the Hellinger affinity for a shift by \(2r\) is exactly \((1+r)e^{-r}\),
\[
\mathsf H^2(f_0,f_{2r})=1-(1+r)e^{-r}\sim\frac{r^2}{2},
\qquad \omega_{\mathrm L}(t)\sim\sqrt{2t}.
\]
The full sets of subsequential limits are therefore
\[
\boxed{
\operatorname{SubseqLim}_{p\downarrow0}
\frac{\Delta_{\mathrm L}(p)}{\sqrt p}
=[\sqrt2\log2,\,2\log2],}
\]
and
\[
\boxed{
\operatorname{SubseqLim}_{p\downarrow0}
\frac{\Delta_{\mathrm L}(p)}{\omega_{\mathrm L}(p)}
=[\log2,\,\sqrt2\log2].}
\]
Hence the universal constant-factor relation of Wang--Gao cannot in general be upgraded, for their fixed dyadic functional itself, to a single asymptotic efficiency constant even in a regular log-concave location family.

A related exact identity shows how the lattice effect disappears after averaging the dyadic origin. For
\[
E_\theta(p)=\sum_{j\ge0:\,2^{j+\theta}p\le1/4}
\frac{2^{j+\theta}}{\ell(2^{j+\theta}p)^2},\qquad0\le\theta<1,
\]
one has
\[
\boxed{
\int_0^1E_\theta(p)\,d\theta
=\frac1{p\log2}\int_p^{1/4}\frac{du}{\ell(u)^2}.}
\]
This identity is only a structural observation about the multiscale energy; no new estimator or optimality claim is made for the phase-averaged quantity.

## Proof

### 1. Log-concavity and the Fisher-information threshold

Write
\[
y(x)=\log(1-x^2),\qquad L(x)=1-y(x)=\log\frac e{1-x^2}.
\]
For \(0<x<1\), apart from an additive constant,
\[
\log f_\kappa(x)=y(x)-\kappa\log L(x).
\]
Since
\[
y'(x)=-\frac{2x}{1-x^2},\qquad
y''(x)=-\frac{2(1+x^2)}{(1-x^2)^2},
\]
we obtain
\[
(\log f_\kappa)''
=\frac{-2(1+x^2)(1+\kappa/L)+4\kappa x^2/L^2}{(1-x^2)^2}<0.
\]
Indeed \(L\ge1\) and \(2x^2/L\le1+x^2\). Symmetry completes log-concavity on \((-1,1)\).

The location score is
\[
\frac{d}{dx}\log f_\kappa(x)
=-\frac{2x}{1-x^2}\left(1+\frac\kappa{L(x)}\right).
\]
Near \(x=1-s\),
\[
f_\kappa(1-s)\sim a_\kappa s[\log(1/s)]^{-\kappa}.
\]
Hence the Fisher integrand is asymptotic, up to a positive constant, to
\[
\frac1{s[\log(1/s)]^\kappa},
\]
which is integrable at zero exactly for \(\kappa>1\).

### 2. Sharp Hellinger asymptotics at the critical boundary

Let \(h_\kappa=\sqrt{f_\kappa}\). At either support endpoint,
\[
h_\kappa'(1-s)^2
\sim\frac{a_\kappa}{4s}[\log(1/s)]^{-\kappa}.
\]
For a translation by \(d=2r\),
\[
\mathsf H^2(f_0,f_d)=\frac12\|h_\kappa-h_\kappa(\cdot-d)\|_2^2.
\]
When \(\kappa\le1\), split the integral into boundary strips of width comparable to \(d\) and the region at distance much larger than \(d\) from the endpoints. The strips contribute only
\[
O\!\left(d^2[\log(1/d)]^{-\kappa}\right),
\]
whereas on the remaining region the difference quotient is asymptotic to \(h_\kappa'\). Both endpoints contribute equally, so
\[
\mathsf H^2(f_0,f_d)
\sim\frac{d^2}{2}\cdot2\cdot\frac{a_\kappa}{4}
\int_d^{c}\frac{ds}{s[\log(1/s)]^\kappa}.
\]
Substituting \(d=2r\) and using slow variation gives exactly the first two displayed cases.

For \(\kappa>1\), \(h_\kappa\in H^1(\mathbb R)\). Translation differentiability in \(L^2\) yields
\[
\mathsf H^2(f_0,f_{2r})
\sim\frac12(2r)^2\|h_\kappa'\|_2^2
=\frac{I_\kappa}{2}r^2,
\]
since \(I_\kappa=4\|h_\kappa'\|_2^2\). Asymptotic inversion gives the formulas for \(\omega_\kappa\).

### 3. Tail quantiles and the dyadic functional

Let \(s_\kappa(u)=q_\kappa(u)+1\) be the lower-endpoint quantile distance. Endpoint integration gives
\[
u\sim\frac{a_\kappa}{2}s_\kappa(u)^2
[\log(1/s_\kappa(u))]^{-\kappa}.
\]
Since \(\log(1/s_\kappa(u))\sim\frac12\log(1/u)\),
\[
\boxed{
s_\kappa(u)\sim
\sqrt{\frac{2^{1-\kappa}}{a_\kappa}}
\sqrt u\,[\log(1/u)]^{\kappa/2}.}
\]
Regular variation then gives
\[
\ell_\kappa(u)=s_\kappa(2u)-s_\kappa(u)
\sim(\sqrt2-1)s_\kappa(u).
\]
Substitution into the defining dyadic sum reduces the asymptotics to
\[
\sum_{j=0}^{J_p}
[\log(1/(2^jp))]^{-\kappa}.
\]
For \(\kappa<1\), this is asymptotic to
\[
\frac{[\log(1/p)]^{1-\kappa}}{(1-\kappa)\log2};
\]
for \(\kappa=1\), it is asymptotic to
\[
\frac{\log\log(1/p)}{\log2}.
\]
This proves the two sharp formulas for \(\Delta_\kappa\) and the universal ratio to \(\omega_\kappa\).

For \(\kappa>1\), the same tail calculation gives
\[
g_\kappa(u)=\frac{u}{\ell_\kappa(u)^2}
\asymp[\log(1/u)]^{-\kappa}.
\]
Reversing the finite dyadic sum by \(m=J_p-j\) yields
\[
p\Delta_\kappa(p)^{-2}
=\sum_{m=0}^{J_p}g_\kappa(2^{-m}z_p).
\]
The tail is now summable, so dominated convergence along \(z_p\to z\) gives the stated phase-profile limit.

### 4. Exact Laplace phase obstruction

For standard Laplace noise and \(u\le1/4\),
\[
q(2u)-q(u)=\log(4u)-\log(2u)=\log2.
\]
The finite geometric sum in \(\Delta\) gives its exact formula. Also, direct integration of the square-root densities gives
\[
\int\sqrt{f(x)f(x-2r)}\,dx=(1+r)e^{-r}.
\]
The claimed Hellinger and subsequential-limit formulas follow immediately from
\(z_p=2^{J_p}p\in(1/8,1/4]\).

Finally, the phase-averaging identity follows by writing \(t=j+\theta\) and changing variables \(u=2^tp\).

## Verification

`artifacts/verify_location_moduli.py` numerically integrates the critical-family Hellinger divergence, numerically inverts endpoint masses to evaluate the exact dyadic functional, and checks the exact Laplace formulas. The reported ratios approach the stated leading terms; convergence at \(\kappa=1\) is deliberately slow because the leading correction is only logarithmic in a logarithm. The artifact also reports the exact limiting constant
\[
(\sqrt2-1)\sqrt{\log2}=0.344855411357777\ldots
\]
and the Laplace phase intervals.

## Relation to prior work and originality boundary

Wang and Gao (2026) introduce the multiscale functional \(\Delta_f\), prove its universal constant-factor relation to the Hellinger two-point benchmark, and give the power-log example only for \(0<\alpha<1\). Their triangle and Epanechnikov examples already exhibit the \((n\log n)^{-1/2}\) critical linear-boundary rate.

That critical rate is much older. Beckert and McFadden (2007) explicitly record \((n\log n)^{-1/2}\) best rates for triangular and quadratic compact-support location examples and develop Hellinger-rate machinery for nonregular parametric problems. Smith (1985) treats densities behaving as a power at an endpoint and identifies the linear-density boundary as a nonregular critical case; his abstract also notes that the single-location version was already known. Accordingly, this record does not claim the critical linear-boundary rate, Hellinger methods for nonregular location models, or finite-Fisher root-\(n\) theory as new.

The originality claim is narrower: to the best of our knowledge, searches did not locate the explicit slowly varying \(\kappa\)-trichotomy at the critical power-log endpoint, including the \(r^2\log\log(1/r)\) case; the sharp asymptotics of Wang--Gao's 2026 dyadic functional on that critical family and its universal ratio to the inverse Hellinger modulus; or the exact Laplace lattice-phase interval proving that the fixed dyadic functional need not possess a single asymptotic efficiency constant.

The full text of Smith (1985) was not available for direct inspection; its abstract and later full-text discussions of nonregular Hellinger rates were inspected. Older nonregular-location literature cited by Beckert--McFadden is therefore a residual originality risk for the slowly varying Hellinger refinement itself. It cannot contain the claims specifically concerning Wang--Gao's dyadic functional, which was introduced in 2026.

## Limitations

The power-log theorem is local as the shift tends to zero and concerns the critical \(\alpha=1\) family. No uniform remainder in \(\kappa\) is proved. The finite-Fisher phase-profile formula does not assert that the profile is nonconstant for every \(f_\kappa\); exact nonconstancy is established separately for Laplace. The phase-averaged identity is not accompanied by an estimator or an optimality theorem. Independent audit has not been performed.

## References

1. Q. Wang and C. Gao, *Instance-Optimal Adaptive Location Estimation via Multiscale Mid-Summaries*, arXiv:2609.20749v1, 2026. https://arxiv.org/abs/2609.20749v1
2. W. Beckert and D. L. McFadden, *Maximal Uniform Convergence Rates in Parametric Estimation Problems*, CeMMAP Working Paper CWP28/07, 2007. https://eml.berkeley.edu/wp/mcfadden1007.pdf
3. R. L. Smith, *Maximum likelihood estimation in a class of nonregular cases*, Biometrika 72 (1985), 67--90. https://doi.org/10.1093/biomet/72.1.67
