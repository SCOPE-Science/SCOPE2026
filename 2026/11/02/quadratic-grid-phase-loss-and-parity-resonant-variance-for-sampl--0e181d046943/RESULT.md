# Quadratic grid-phase loss and parity-resonant variance for sampled bang-bang control

## Finding

For scalar linear-affine optimal control with linear terminal and running cost, consider the optimal objective restricted to controls that are constant on a common shifted uniform sampling grid of nominal width \(h=1/m\). Assume its switching function \(\sigma\in C^2([0,1])\) has finitely many simple interior zeros \(\tau_1,\ldots,\tau_s\), no endpoint zeros, and no other zeros. Put \(a_j=|\sigma'(\tau_j)|>0\) and \(g(r)=\min\{r^2,(1-r)^2\}\) for \(0\le r\le1\), extended periodically.

For a shift \(\theta\in[0,1)\), the difference \(\Delta_{m,\theta}\) between the sampled-data and unrestricted minimum satisfies, **uniformly in** \(\theta\),
\[
\Delta_{m,\theta}=h^2\sum_{j=1}^{s}a_j g(\{m\tau_j-\theta\})+O(h^3).
\]
The braces denote fractional part, with \(g(0)=g(1)=0\). For a single shift \(\Theta\sim\operatorname{Unif}[0,1)\) shared by all cells, and writing \(V_m=\operatorname{Var}_{\Theta}(\Delta_{m,\Theta})\),
\[
\mathbb E_{\Theta}\Delta_{m,\Theta}=\frac{h^2}{12}\sum_{j=1}^{s}a_j+O(h^3),
\]
\[
h^{-4}V_m=\frac{1}{2\pi^4}\sum_{k=1}^{\infty}\frac{1}{k^4}\left|\sum_{j=1}^s a_j e^{2\pi i k m\tau_j}\right|^2+O(h).
\]
The leading variance on the right is an \(m\)-dependent covariance profile, **not** a general convergent constant. It can retain arithmetic resonance between distinct switching times.

For the natural two-switch test \(\sigma(t)=(t-\tfrac14)(t-\tfrac34)\), the leading normalized variance equals \(1/180\) for even \(m\) and \(1/2880\) for odd \(m\), a factor of exactly 16, although both parity subsequences have the same leading mean \(h^2/12\). For a single affine zero with slope magnitude \(a\), the entire normalized loss law is exact:
\[
\Pr\!\left\{\frac{\Delta_{m,\Theta}}{a h^2}\le y\right\}=2\sqrt y\quad(0\le y\le\tfrac14),
\]
when the switch lies in an interior full-width sampling cell.

## Assumptions and scope

Fix \(x_0,c\in\mathbb R\). Let \(a,b,d,e\in C^2([0,1];\mathbb R)\) and let the scalar state satisfy
\[
x'(t)=a(t)x(t)+b(t)u(t),\qquad x(0)=x_0,\qquad -1\le u(t)\le1.
\]
The cost to **minimize** is
\[
J(u)=c\,x(1)+\int_0^1[d(t)x(t)+e(t)u(t)]\,dt.
\]
There is no terminal-state constraint, quadratic control penalty, or discretization error in the state evolution or integration. The sampled restriction concerns **only** zero-order-hold controls; state propagation and the cost are exact.

The adjoint \(p\) solves \(p'=-a p-d\), \(p(1)=c\), and \(\sigma=e+b p\). Assume \(s\ge1\), \(\sigma\) has precisely \(s\) distinct simple zeros in \((0,1)\), and \(\sigma(0)\sigma(1)\ne0\). The grid consists of \(0,1\) and all points \((k+\theta)/m\) in \((0,1)\), for integers \(k\); the first and last cells can be shorter than \(h=1/m\). For each sufficiently large \(m\), every zero lies at least one full sampling-cell width from the physical endpoints, and distinct zeros occupy different cells. A root exactly on a sampling boundary contributes zero loss.

For each grid \(\theta\), \(J^*_{m,\theta}\) is the minimum among controls constant on every grid cell; \(J^*\) is the unrestricted minimum; \(\Delta_{m,\theta}:=J^*_{m,\theta}-J^*\ge0\). All remainders for fixed coefficients are uniform over \(\theta\in[0,1)\), as \(m\to\infty\). The random shift is **one common uniform phase** for the whole grid, not independent shifts at each switch.

## Proof

**1. Exact reduction to the switching function.** The identity
\[
\frac{d}{dt}(p(t)x(t))=-d(t)x(t)+p(t)b(t)u(t)
\]
implies
\[
J(u)=p(0)x_0+\int_0^1\sigma(t)u(t)\,dt.
\]
Hence \(J^*=p(0)x_0-\int_0^1|\sigma(t)|dt\), attained by \(u^*(t)=-\operatorname{sign}\sigma(t)\) almost everywhere. For a grid cell \(I\), the exact best constant control equals \(-\operatorname{sign}\int_I\sigma\), with any value allowed when that integral is zero. Therefore
\[
\Delta_{m,\theta}=\sum_{I\in\mathcal P_{m,\theta}}\left(\int_I|\sigma(t)|dt-\left|\int_I\sigma(t)dt\right|\right).
\tag{1}
\]
The summands are nonnegative and vanish on cells with a constant sign of \(\sigma\).

**2. Local crossing law.** Once \(m\) is sufficiently large, each zero \(\tau_j\) is the only zero of its grid cell \(I_j=[\ell_j,\ell_j+h]\); a zero on a grid boundary contributes exactly zero and may be assigned to either adjacent cell. Let \(r_j=(\tau_j-\ell_j)/h=\{m\tau_j-\theta\}\). Taylor's theorem gives \(\sigma(t)=\sigma'(\tau_j)(t-\tau_j)+R_j(t)\), where \(|R_j(t)|\le\frac12\|\sigma''\|_{\infty}h^2\) throughout that cell. For integrable \(q,\widetilde q\), the local loss functional \(L_I(q)=\int_I|q|-|\int_I q|\) obeys
\[
|L_I(q)-L_I(\widetilde q)|\le2\int_I|q-\widetilde q|.
\]
Thus replacing \(\sigma\) by its linearization changes the local loss by at most \(\|\sigma''\|_\infty h^3\). Direct integration of the linearization with slope magnitude \(a_j\) gives
\[
L_{I_j}(\sigma'(\tau_j)(t-\tau_j))=a_j h^2\min\{r_j^2,(1-r_j)^2\}.
\]
Summing finitely many switch cells proves the uniform \(O(h^3)\) claim. This includes switch-grid alignment because both the true and linear crossing losses vanish then.

**3. Random-shift mean and covariance.** The common uniform shift makes each \(r_j\) uniformly distributed modulo one. Elementary integration yields
\[
\int_0^1g(r)dr=\frac1{12},\quad
\int_0^1g(r)^2dr=\frac1{80},\quad
\operatorname{Var}(g(U))=\frac1{180}.
\]
The absolutely and uniformly convergent cosine series is
\[
g(r)=\frac1{12}+\sum_{k=1}^{\infty}\frac{(-1)^k}{\pi^2k^2}\cos(2\pi kr).
\tag{2}
\]
Write \(F_m(\theta)=\sum_j a_j g(m\tau_j-\theta)\). Fourier orthogonality applied to (2) gives exactly
\[
\operatorname{Var}_\Theta(F_m(\Theta))=
\frac1{2\pi^4}\sum_{k=1}^{\infty}k^{-4}\left|\sum_j a_j e^{2\pi ikm\tau_j}\right|^2.
\]
Uniformly, \(h^{-2}\Delta_{m,\theta}=F_m(\theta)+O(h)\), while \(F_m\) is bounded independently of \(m,\theta\). The mean follows by integrating; the variance changes by \(O(h)\) under this uniformly bounded perturbation. This proves both assertions, with the variance's explicit dependence on \(m\).

**4. The sharp one- and two-switch tests.** For an affine \(\sigma(t)=a_0(t-\tau)\) with \(\tau\in(0,1)\) and sufficiently large \(m\), the linear crossing formula is exact; \(\{m\tau-\Theta\}\) is uniform, and \(g(U)\le y\) precisely when \(U\) lies within \(\sqrt y\) of either endpoint for \(0\le y\le\frac14\). This gives the stated exact distribution.

For \(\sigma(t)=(t-\frac14)(t-\frac34)\), both slope magnitudes equal \(\frac12\). If \(m\) is even, the phases differ by an integer, so \(F_m(\Theta)=g(U)\) and the variance is \(1/180\). If \(m\) is odd, the phases differ by \(\frac12\) modulo one, so \(F_m(\Theta)=\frac12(g(U)+g(U+\frac12))\). In (2) the odd harmonics cancel; Parseval gives
\[
\operatorname{Var}\left(\frac{g(U)+g(U+\frac12)}2\right)=
\frac1{2\pi^4}\sum_{k\ge1,\ 2\mid k}k^{-4}=
\frac1{2880}.
\]
The two means remain \(1/12\); the variance ratio is \(16\). These are coefficients of the asymptotic variance \(h^4\), not finite-m exact variances for the quadratic switching function.

## Verification

The standalone standard-library program `verify.py` integrates the two-zero polynomial exactly using rational arithmetic on 512 grid/shift configurations (eight mesh sizes and 64 rational phases). It verifies a concrete uniform \(O(h^3)\) remainder bound for that polynomial. It also checks the exact rational phase moments, harmonic parity coefficients, and near-asymptotic mean and variance using 1024 shifts for four mesh sizes. Run `python3 verify.py` to obtain `VERIFY_OK`. The random phase integrals, Fourier identity and uniform asymptotics above are analytic proofs; finite checks neither establish an infinite sum nor exhaust all smooth switching functions.

## Relationship to prior work

Bourdin and Trélat (2023) prove broad qualitative sampled-data optimal-control convergence of states and costates. That result does not specify a sharp objective error, a subcell-switching phase, or covariance under grid randomization. Aghaee and Hager (2020/2021) optimize switching times as continuous decision variables, whereas here **all** permitted switches are fixed by the sampling grid. Scarinci and Veliov (2017/2018) prove higher-order estimates for a distinct enriched Volterra–Fliess discretization that retains within-cell switching; their theorem does not imply the phase-resolved value loss for exact zero-order-hold control restriction. A published two-level qubit result derives a cubic phase law for the time excess of a one-interior-pulse endpoint branch; that model has a nonlinear terminal endpoint condition, a different order, and an adjustable within-cell pulse. Its cubic law does not imply the present quadratic control-value law or the shared-phase Fourier variance.

The local integral loss identity and Fourier orthogonality are elementary and not claimed as novel independently. The assessed joint contribution is a uniform exact leading-order value-gap profile for the scalar linear-affine sampled optimal control class, together with its shifted-mesh harmonic covariance and explicit two-switch variance-resonance diagnostic. Searches found no source covering this combined assertion; absence from searched material does not prove priority across all literature.

## Limitations

The dynamics and cost are scalar and linear-affine, terminal state is free, there is no state constraint or quadratic cost, and only exact piecewise-constant control restrictions are studied. The result does **not** give a general nonlinear optimal-control error theorem, an improved discretization method, or a universal unshifted-mesh limit coefficient. The variance profile can oscillate with \(m\). The two-switch constants are asymptotic and require a single common randomized grid phase. Floating-point grid rounding, measurement noise and optimizing the grid origin are not treated. Independent validation and a broader literature priority assessment remain outstanding.

## References

1. L. Bourdin and E. Trélat, *Convergence in nonlinear optimal sampled-data control problems*, arXiv:2302.02965v1, first public 2023-02-06, https://arxiv.org/abs/2302.02965.
2. M. Aghaee and W. W. Hager, *The Switch Point Algorithm*, arXiv:2011.10022v1, first public 2020-11-19, https://arxiv.org/abs/2011.10022; SIAM Journal on Control and Optimization 59 (2021), 2570–2593.
3. T. Scarinci and V. M. Veliov, *Higher-order numerical scheme for linear quadratic problems with bang–bang controls*, first published online 2017-10-06, *Computational Optimization and Applications* 69 (2018), 403–422, https://doi.org/10.1007/s10589-017-9948-z.
4. *Cubic grid-phase law for a sampled bang switch in a controlled qubit*, publicly available mathematical research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-cubic-grid-phase-law-for-a-sampled-bang-switch-in-a-controlled-q--99b8c1c493cd.
