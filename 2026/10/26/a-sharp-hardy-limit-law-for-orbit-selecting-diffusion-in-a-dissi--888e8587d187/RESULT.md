# A sharp Hardy-limit law for orbit-selecting diffusion in a dissipative time crystal

## Finding

Consider the orbit-label diffusion operator appearing in the boundary-time-crystal sector of a collectively damped spin [1]. For every \(q\geq0\), define
\[
\mathcal L_q f(x)=\frac{1+q^2x^2}{4}\frac{d}{dx}\left[(1-x^2)f'(x)\right],\qquad -1<x<1,
\]
with the natural zero-flux endpoint realization. Its stationary eigenfunction is constant. Let \(\mu(q)\) be the smallest *positive* eigenvalue of \(-\mathcal L_q\).

**Theorem.** The unnormalized gap \(\mu(q)\) is strictly increasing for \(q\geq0\), whereas \(\mu(q)/(1+q^2)\) is strictly decreasing. Both endpoint values are exact:
\[
\mu(0)=\frac12,\qquad
\mu(q)=\frac12+\frac3{10}q^2+O(q^4)\quad(q\downarrow0),
\]
\[
\boxed{\displaystyle \lim_{q\to\infty}\frac{\mu(q)}{1+q^2}=\frac1{16}.}
\]
In particular, the strict inequalities
\[
\mu(q)>\frac12,\qquad \frac1{16}<\frac{\mu(q)}{1+q^2}<\frac12
\]
hold for every \(q>0\). The lower constant \(1/16\) is sharp and originates from the threshold \(1/4\) in the half-line Hardy inequality.

In the spin notation of [1], let \(\omega>\kappa>0\) and \(\Omega=\sqrt{\omega^2-\kappa^2}\). Then \(q=\kappa/\Omega\), so the equivalent critical-drive law is
\[
\boxed{\displaystyle \lim_{\kappa/\omega\uparrow1}\left(1-\frac{\kappa^2}{\omega^2}\right)\mu\!\left(\frac{\kappa}{\sqrt{\omega^2-\kappa^2}}\right)=\frac1{16}.}
\]
This concerns the *reduced orbit-label diffusion gap*; it is not a uniform estimate of the full finite-spin Liouvillian spectrum near \(\Omega=0\).

## Assumptions and scope

The endpoint realization is the self-adjoint, nonpositive natural extension in \(L^2((-1,1),w_q(x)\,dx)\), where
\[
w_q(x)=\frac1{1+q^2x^2}.
\]
Its nonnegative quadratic form is \(\frac14\int_{-1}^1(1-x^2)|f'|^2dx\), with the standard closed weighted Sobolev form domain. No endpoint value of \(f\) is prescribed; the limiting flux \((1-x^2)f'(x)\) vanishes at both endpoints. The physical source identification concerns the transverse-drive, purely collective-lowering-jump special case (the squeezing coefficient \(\beta=0\)); the mathematical diffusion theorem itself depends only on the stated operator. The constant eigenfunction spans the nullspace. For each finite \(q\), the weight is bounded above and below by positive constants, so the usual Legendre form has compact resolvent; oscillation and simplicity of the separated eigenvalues apply. No finite-spin or simultaneous \(q,S\to\infty\) limit is assumed.

## Proof

**1. Identification of the first positive mode.** Multiplication by \(w_q\) gives the self-adjoint Sturm–Liouville equation
\[
-\frac{d}{dx}\big[(1-x^2)f'(x)\big]=4\mu w_q(x)f(x).
\]
The first nonconstant eigenfunction has one interior zero by Sturm oscillation. The coefficients and natural endpoint conditions are invariant under reflection, and the corresponding eigenvalue is simple. Its eigenfunction is therefore either odd or even. An even eigenfunction with exactly one interior zero would have that zero at \(x=0\) together with \(f'(0)=0\), forcing the zero solution by uniqueness of the regular initial-value problem. It is consequently odd. Restricting to \((0,1)\), it obeys \(f(0)=0\) and the natural condition at \(1\). Hence
\[
4\mu(q)=\inf_{\substack{f(0)=0\\f\not\equiv0}}
\frac{\displaystyle\int_0^1(1-x^2)|f'(x)|^2\,dx}
{\displaystyle\int_0^1\frac{|f(x)|^2}{1+q^2x^2}\,dx}.
\tag{1}
\]
The infimum is taken over the corresponding finite-energy form domain and is attained for each finite \(q\).

**2. Strict increase of the unnormalized gap.** If \(q_2>q_1\geq0\), then the denominator in (1) is strictly smaller at \(q_2\) for every nonzero admissible function. Using a minimizing eigenfunction at \(q_2\) as a trial function at \(q_1\) gives
\[
4\mu(q_1)\leq R_{q_1}(f_{q_2})<R_{q_2}(f_{q_2})=4\mu(q_2).
\]
The strictness follows because an eigenfunction cannot vanish almost everywhere on \((0,1)\).

**3. Independent strict decrease after normalization.** Substitute \(x=\tanh y\), \(g(y)=f(\tanh y)\), and \(a=\sqrt{1+q^2}\). A direct Jacobian computation yields
\[
\int_0^1(1-x^2)|f'|^2dx=\int_0^\infty |g'|^2dy,
\quad
\int_0^1\frac{f^2}{1+q^2x^2}dx=\int_0^\infty\frac{g^2}{1+a^2\sinh^2y}\,dy.
\]
Thus
\[
\frac{4\mu(q)}{a^2}=\inf_{g(0)=0}
\frac{\displaystyle\int_0^\infty|g'|^2dy}
{\displaystyle\int_0^\infty\frac{g^2}{\sinh^2y+a^{-2}}dy}.
\tag{2}
\]
For every fixed nonzero test function, the denominator in (2) increases *strictly* with \(a\). Comparing minimizing functions as in step 2 proves that \(\mu(q)/(1+q^2)\) decreases strictly. The transformed form permits nonzero finite limits of \(g(y)\) as \(y\to\infty\); no artificial Dirichlet condition is imposed at infinity.

**4. Exact weak-dissipation coefficient.** At \(q=0\) the operator is one-quarter of the Legendre generator, with first positive eigenvalue \(\mu(0)=1/2\) and odd eigenfunction \(f_0(x)=x\). Put \(t=q^2\) and \(\lambda(t)=4\mu(\sqrt t)\). Since the eigenvalue is simple and the weight \((1+tx^2)^{-1}\) is analytic near \(t=0\), standard isolated-eigenvalue perturbation theory applies. Differentiating the generalized eigenvalue identity yields
\[
\lambda'(0)=\lambda(0)
\frac{\int_{-1}^1x^2 f_0(x)^2dx}{\int_{-1}^1f_0(x)^2dx}
=2\frac{\int_{-1}^1x^4dx}{\int_{-1}^1x^2dx}=\frac65.
\]
Dividing by four proves \(\mu(q)=1/2+3q^2/10+O(q^4)\).

**5. Sharp critical limit.** The half-line Hardy inequality states that every finite-energy \(g\) with \(g(0)=0\) satisfies
\[
\int_0^\infty|g'(y)|^2dy\geq\frac14\int_0^\infty\frac{|g(y)|^2}{y^2}dy.
\]
It extends from compactly supported functions by finite-energy cutoffs; a finite nonzero limit at infinity is allowed. Because \(\sinh y\geq y\), equation (2) implies
\[
\frac{\mu(q)}{a^2}\geq\frac1{16}.
\tag{3}
\]
Conversely, for any *fixed* compactly supported admissible finite-energy \(g\) with \(g(0)=0\), dominated convergence gives
\[
\lim_{a\to\infty}\int_0^\infty
\frac{g^2}{\sinh^2y+a^{-2}}dy
=\int_0^\infty\frac{g^2}{\sinh^2y}dy.
\]
The infimum of \(\int|g'|^2/\int g^2/\sinh^2y\) over these tests is exactly \(1/4\). For the lower bound, use Hardy and \(\sinh y\ge y\). For sharpness, choose a smooth cutoff \(\chi\) equal to one near zero and use \(g_\epsilon(y)=y^{1/2+\epsilon}\chi(y)\). As \(\epsilon\downarrow0\), both its energy and its inverse-hyperbolic-square mass have leading divergences proportional to \(1/(2\epsilon)\), and their ratio tends to \((1/2)^2=1/4\). Taking the large-\(a\) limit first for each fixed test and then approaching these tests shows
\[
\limsup_{q\to\infty}\frac{\mu(q)}{1+q^2}\leq\frac1{16}.
\]
Together with (3), this proves the asserted exact limit. Strict normalized monotonicity from step 3 rules out equality at a finite \(q\). The two limits are deliberately taken in this order: the critical test functions are not fixed physical eigenfunctions across varying parameters.

## Verification

The self-contained program `verify.py`, requiring only the open-source scientific Python packages specified in `requirements.txt`, computes the lowest odd mode by **two independent discretizations**: a weighted Legendre–Galerkin generalized eigenproblem on \((-1,1)\), and a piecewise-linear transformed-half-line generalized eigenproblem. Run from the extracted directory using `python verify.py`.

The program checks the exact Legendre normalization, the perturbative coefficient, strict inequalities at sampled parameters, the Hardy lower bound, the one-mode Rayleigh upper bound, and cross-method agreement. On the included run it reported **57 successful numerical comparisons**. These finite checks do *not* prove universal monotonicity or the singular limit; those depend on the analytic argument above.

## Relationship to prior work

Tindall [1], Eq. (13) and its supplementary derivation, furnish the orbit diffusion operator, the identification of its first nonzero eigenvalue as the slow orbit-relaxation rate, and the limit \(\mu\to1/2\) for weak dissipation. The strict opposing monotonicities, the evaluated weak-dissipation correction, and the sharp Hardy coefficient at the critical-drive boundary are not stated in its inspected main text or supplement.

The underlying orbit diffusion and stationary weight were already studied in the cooperative-fluorescence work of Drummond and Carmichael [2,3]; neither that Fokker–Planck model nor Hardy's inequality is claimed as new. Those older articles could not be fully inspected, so an earlier equivalent spectral-edge calculation remains a priority risk. Dutta, Zhang and Haque [4] analyze Liouvillian spectral collapse and critical slowing in a *different* nonlinear-spin model; its main text does not supply this orbit-label Sturm–Liouville asymptotic. Carollo and Lesanovsky [5] study the boundary-time-crystal transition and quantum fluctuations, but complete text of that paper was not available for comparison.

## Limitations

All limits in this theorem concern the **fixed reduced diffusion operator** and its eigenvalues. The large-\(q\) theorem is not uniform in the spin size \(S\); the source's finite-\(S\) operator corrections grow near \(\omega=\kappa\). Consequently the theorem does **not** identify the gap of the full finite-spin Liouvillian in a simultaneous \(S\to\infty\), \(\omega\downarrow\kappa\) regime or justify a finite-system relaxation-time estimate at that boundary. It establishes neither the entire spectrum nor error terms beyond the stated leading strong-coupling law. The priority assessment is conditional on the accessible literature and has not undergone independent scientific validation.

## References

[1] J. Tindall, *Emergent quantum algebras in dissipative time crystals*, arXiv:2610.16609v1 (first publicly submitted 2026-10-12), Eq. (13) and supplemental orbit Fokker–Planck derivation. https://arxiv.org/abs/2610.16609

[2] P. D. Drummond and H. J. Carmichael, *Volterra cycles and the cooperative fluorescence critical point*, Optics Communications **27** (1978), 160–164. https://doi.org/10.1016/0030-4018(78)90198-0

[3] H. J. Carmichael, *Analytical and numerical results for the steady state in cooperative resonance fluorescence*, Journal of Physics B **13** (1980), 3551–3575. https://doi.org/10.1088/0022-3700/13/18/009

[4] S. Dutta, S. Zhang and M. Haque, *Quantum Origin of Limit Cycles, Fixed Points, and Critical Slowing Down*, Physical Review Letters **134** (2025), 050407. https://doi.org/10.1103/PhysRevLett.134.050407

[5] F. Carollo and I. Lesanovsky, *Exact solution of a boundary time-crystal phase transition: time-translation symmetry breaking and non-Markovian dynamics of correlations*, Physical Review A **105** (2022), L040202. https://arxiv.org/abs/2110.00030
