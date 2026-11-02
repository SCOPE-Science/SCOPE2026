# Joint first-passage exposure law for Brownian diffusion with Poisson resetting

## Finding

Let \(D,r,a>0\), let the one-dimensional particle diffuse with generator \(D\partial_{xx}\) on \((0,\infty)\), and reset instantaneously to \(a\) at independent Poisson rate \(r\). It starts at \(a\) and is absorbed at its first hit of zero, at time \(T\). Its point-local-time density at the resetting point and its upper-half-line residence time are
\[
L=\int_0^T\delta(X_t-a)\,dt,\qquad R=\int_0^T\mathbf1_{\{X_t>a\}}\,dt.
\]
The delta is the **occupation-density**, not the semimartingale local time: \(L=\lim_{h\downarrow0}(2h)^{-1}\int_0^T\mathbf1_{\{|X_t-a|<h\}}\,dt\), in probability (and in the usual local-time realization). For every \(s,u,v\ge0\), put \(k_s=\sqrt{(r+s)/D}\) and \(k_{s+v}=\sqrt{(r+s+v)/D}\). The complete joint Laplace transform is
\[
\boxed{\mathbb E_a e^{-sT-uL-vR}
 =\left[\frac{r+s\cosh(a k_s)}{r+s}
 +\frac{\sinh(a k_s)}{Dk_s}\left(u+\frac{s+v}{k_{s+v}}\right)\right]^{-1}.}
\]
This is a joint result about three canonical first-passage observables. Their separate marginal transforms were known; the joint dependence, factorization below, and correlation law are the evaluated assertions here.

Write \(S=\sinh(a\sqrt{r/D})\), \(A=S/\sqrt{Dr}\), and \(\Phi(v)=\sqrt D\,v/\sqrt{r+v}\). In particular,
\[
\mathbb E_a e^{-uL-vR}=(1+A[u+\Phi(v)])^{-1}.
\]
Consequently, the pair \((L,R)\) has the **stopped-subordinator representation** \((E,Y_E)\), where \(E\) is exponential with mean \(A\), \(Y\) is an independent subordinator with Laplace exponent \(\Phi\), and all parameters are positive. Its Lévy measure is
\[
\Pi(dt)=\frac{\sqrt D\,e^{-rt}(1+2rt)}{2\sqrt\pi\,t^{3/2}}\,dt,\qquad t>0.
\]
In particular, for almost every \(\ell>0\),
\[
\mathbb E[R\mid L=\ell]=\ell\sqrt{D/r},\qquad
\operatorname{Var}(R\mid L=\ell)=\ell\sqrt D/r^{3/2},
\]
and the Pearson correlation is exactly
\[
\boxed{\operatorname{Corr}(L,R)=\sqrt{\frac{\sinh(a\sqrt{r/D})}{1+\sinh(a\sqrt{r/D})}}.}
\]
For fixed \(D,a>0\), this correlation is strictly increasing in \(r>0\), tends to zero at weak resetting, and tends to one at rapid resetting. The two first-passage exposures become strongly correlated without becoming identical.

## Assumptions and scope

The process is standard Brownian diffusion between resets, with continuous paths on each excursion and independent Poisson resets to the interior point \(a\). The interface at \(a\) is not reflecting. Reset jumps themselves contribute zero occupation time and zero point-local-time density. The process is killed immediately on hitting zero; all three accumulated observables end then. Parameters \(D,r,a\) are strictly positive; the nonnegative transform arguments \(s,u,v\) are arbitrary and finite. This includes any equalities among the transform arguments. A single reset-free Brownian excursion from \(a\) hits zero before its exponential reset clock with probability \(e^{-a\sqrt{r/D}}>0\); independent repetitions therefore imply \(T<\infty\) almost surely. The random variables \(L,R\) are consequently finite almost surely.

## Proof

**Joint backward equation.** For \(f(x)=\mathbb E_x e^{-sT-uL-vR}\), Feynman–Kac, first conditioning on whether a Poisson reset occurs, gives away from \(a\)
\[
D f''(x)-[r+s+v\mathbf1_{\{x>a\}}]f(x)+r f(a)=0.
\]
The absorbing boundary is \(f(0)=1\), and \(f\) is bounded at infinity. Writing \(q=f(a)\), continuity holds at \(a\), while the occupation-density normalization gives the exact derivative jump
\[
D[f'(a+)-f'(a-)]=u q.
\]
Indeed, replacing the Dirac potential by a symmetric \(u/(2h)\) potential on \((a-h,a+h)\), integrating its backward equation across that interval, and taking \(h\downarrow0\) proves this normalization. The resets have no atomic occupation-time contribution.

**Explicit solution.** Set \(k=k_s\) and \(k_+=k_{s+v}\). On the right, boundedness forces
\[
f_+(x)=\frac{rq}{r+s+v}+\frac{(s+v)q}{r+s+v}e^{-k_+(x-a)}.
\]
On the left, continuity at \(a\) allows
\[
f_-(x)=\frac{rq}{r+s}+\frac{sq}{r+s}\cosh(k(x-a))+B\sinh(k(x-a)),
\]
where \(f_-(0)=1\) yields
\[
B=\frac{q[r+s\cosh(ka)]/(r+s)-1}{\sinh(ka)}.
\]
The derivatives at the interface are \(f'_-(a)=kB\) and \(f'_+(a)=-(s+v)q/(Dk_+)\). Substituting into the jump relation and solving the scalar equation for \(q\) gives the boxed transform. Its positive denominator and uniqueness of the bounded Feynman–Kac solution justify the expression for the entire nonnegative parameter region.

**Conditional subordinator and correlation.** Setting \(s=0\) in the joint transform gives \([1+A(u+\Phi(v))]^{-1}\). The displayed Lévy measure obeys \(\int_0^\infty(1\wedge t)\Pi(dt)<\infty\). Direct integration gives
\[
\int_0^\infty(1-e^{-vt})\Pi(dt)=\Phi(v).
\]
Thus \(\Phi\) is the exponent of a genuine driftless subordinator \(Y\). If \(E\) is independent exponential with mean \(A\), then
\[
\mathbb E[e^{-uE-vY_E}]
=\int_0^\infty A^{-1}e^{-\ell/A-u\ell-\ell\Phi(v)}\,d\ell
=[1+A(u+\Phi(v))]^{-1}.
\]
Uniqueness of multivariate Laplace transforms proves equality in law. Since \(\Phi'(0)=\sqrt{D/r}\) and \(-\Phi''(0)=\sqrt D/r^{3/2}\), the conditional mean/variance formulas follow. With \(\operatorname{Var}(L)=A^2\), the total-variance and total-covariance identities yield
\[
\operatorname{Var}(R)=\frac{S+S^2}{r^2},\qquad
\operatorname{Cov}(L,R)=A^2\sqrt{D/r},
\]
and hence the boxed Pearson correlation. The function \(S=\sinh(a\sqrt{r/D})\) strictly increases from zero to infinity as \(r\) increases, proving strict correlation monotonicity and its two limits.

## Verification

Run `python check_joint.py` in an environment with Python, NumPy, SciPy, SymPy, and mpmath. The checker differentiates the joint transform symbolically, independently discretizes the full two-region backward boundary-value problem including the point potential at the reset location, matches the three previously published marginal specializations, integrates the proposed Lévy density, and checks the correlation formula. Its five finite-difference cases had relative errors below \(0.003\), against the discretized model (not against simulation). These numerical comparisons are corroboration, not a proof of the continuum or subordinator assertions. The analytic argument above supplies that proof.

## Relationship to prior work

Singh and Pal (2022), arXiv:2202.02715, derive the first-passage functionals separately. Their local-time transform (equation 20), residence transform (equation 28), and first-passage transform (equation 67) are all recovered at the corresponding zero-parameter specializations when \(D=1/2\). Their general Feynman–Kac equation (equation 9) motivates the backward method but does not evaluate the three-variable transform or determine this joint coupling.

Colantoni, D'Ovidio, and Pagnini (2025) give the inverse-local-time Laplace exponent \(v/\sqrt{r+v}\) and its Lévy density for **reflected** Brownian motion with resetting. Its coincidence with \(\Phi\) at \(D=1\) is acknowledged as known; neither that exponent nor general excursion subordination is claimed as new. Their reflected, nonabsorbing model does not present the stopped joint first-passage law of \((T,L,R)\) or the absorbing-model correlation formula.

Pal, Chatterjee, Reuveni, and Kundu (2019) study fixed-horizon resetting local time (including absorbing boundaries), and Dubey and Pal (2023) investigate separate first-passage functionals for an Ornstein–Uhlenbeck particle with resetting. Those distinct setups and marginal calculations provide further context, not the evaluated joint law here.

## Limitations

The joint transform is specific to constant-diffusivity Brownian motion, a fixed resetting point, independent Poisson resets, and one absorbing endpoint. It does not establish analogous factorization for state-dependent rates, drifts, non-Poisson resets, other spatial regions, or arbitrary initial positions. It yields distributions and moments through Laplace inversion/differentiation but does not furnish a closed joint probability density. Although the general machinery of Feynman–Kac and excursion theory is established, no claim is made of inventing those methods or the reflected-process Lévy exponent. A more general pre-existing theorem could subsume the evaluated joint specialization, and independent publication-priority review has not been performed.

## References

1. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715 (first posted 2022-02-06), https://arxiv.org/abs/2202.02715. Main comparison: Sections 2–5 and Appendix A.
2. F. Colantoni, M. D'Ovidio, and G. Pagnini, *Time reversal of Reflected Brownian Motion with Poissonian Resetting*, Journal of Statistical Physics 192, 147 (2025), https://doi.org/10.1007/s10955-025-03527-5. Main comparison: Section 6, Theorem 6.
3. A. Pal, R. Chatterjee, S. Reuveni, and A. Kundu, *Local time of diffusion with stochastic resetting*, arXiv:1902.00907, https://arxiv.org/abs/1902.00907. Main comparison: Sections III–V.
4. A. Dubey and A. Pal, *First-passage functionals for Ornstein Uhlenbeck process with stochastic resetting*, arXiv:2304.05226 (first posted 2023-04-11), https://arxiv.org/abs/2304.05226. Main comparison: Sections 3–4.
