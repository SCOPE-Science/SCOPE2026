# A universal survival-reversal threshold for spatially distributed resetting in a lethal habitat

## Finding

For a diffusing, linearly reproducing population living on a one-dimensional interval with lethal endpoints, the effect of *spreading the reset destinations* changes sign at an exact habitat half-width. Two destination laws with the same mean squared displacement and ordered in convex order can have opposite effects on the dominant population-growth exponent, depending only on habitat size. The crossover is
\[
L_\times=\sqrt{m_2+2/r},
\]
where \(m_2\) is the shared second moment of the reset destinations and \(r>0\) is the resetting rate. At this width every such destination law has dominant growth exponent \(1-r\), independent of all its higher moments. At smaller admissible widths, a strict mean-preserving spread of the squared reset displacement increases the growth exponent; at larger widths it decreases that exponent.

The effect is strong enough to reverse the extinction-versus-growth verdict **for exactly the same physical habitat**. Set \(L=79/50\). For the concentrated law \(\mu=(\delta_{-1/\sqrt2}+\delta_{1/\sqrt2})/2\) and the dispersed law \(\nu=\delta_0/2+(\delta_{-1}+\delta_1)/4\), both with \(m_2=1/2\), at rate \(r=4/5\) the concentrated population declines exponentially and the dispersed population grows exponentially. At rate \(r=2\), their respective verdicts reverse. All four strict assertions admit short exact rational-arithmetic certificates reproduced by `verification.py`.

When the critical habitat half-width exists above the support of the reset law, at \(r=1\) it is exactly \(\sqrt{2+m_2}\). Near this resetting rate, the first effect of a strict mean-preserving spread on the critical habitat half-width is quantified by the difference of the fourth moments:
\[
L_{c,\nu}(r)-L_{c,\mu}(r)
=\frac{m_{4,\nu}-m_{4,\mu}}{24\sqrt{2+m_2}}(r-1)
+O((r-1)^2).
\]
The strict convex-order assumption implies the fourth-moment difference is positive when finite; here all measures have compact support.

## Assumptions and scope

Fix \(r>0\), \(0<b<L\), and a Borel probability measure \(\mu\) supported in \([-b,b]\). The physical habitat is \(I_L=(-L,L)\), with absorbing (immediately lethal) endpoints. Diffusivity and intrinsic linear reproduction rate are each normalized to one. All individuals inside the habitat reset at independent Poisson times of rate \(r\) to independently sampled sites drawn from \(\mu\), irrespective of their pre-reset locations. Between resets they diffuse with infinitesimal generator \(\partial_{xx}\); birth and death are linear, without density dependence.

In weak measure notation the mean population intensity satisfies
\[
\partial_t u=\partial_{xx}u+(1-r)u+r\mu\,\int_{-L}^{L}u(dx,t),\qquad u(\pm L,t)=0.
\]
For an atomic reset law, \(u\) may be understood as a finite measure; after positive elapsed diffusion time its population profile has a density. The associated positive evolution has a real dominant exponential growth rate \(\lambda_\mu(L,r)\). Positive and negative signs of this exponent mean respectively exponential growth and exponential decay in this **linear** model, rather than a claim about nonlinear population persistence or stochastic extinction probabilities.

For comparisons, take two compactly supported reset laws \(\mu,\nu\), both inside \((-b,b)\), and let \(Y_\mu\sim\mu\), \(Y_\nu\sim\nu\). Assume \(\mathbb E Y_\mu^2=\mathbb E Y_\nu^2=m_2\). The assertion that \(Y_\mu^2\preceq_{\mathrm{cx}}Y_\nu^2\) means that for every convex real function \(\phi\) on \([0,b^2]\), \(\mathbb E\phi(Y_\mu^2)\le\mathbb E\phi(Y_\nu^2)\). *Strict spread* means the laws of these two squared variables are unequal. No symmetry or equal mean of the signed reset destinations is assumed.

## Proof

**1. Scalar equation for the leading rate.** Denote the positive Dirichlet heat semigroup on \((-L,L)\) by \(S_L(t)\), with Laplacian \(\Delta_D\). For any real \(q>-\pi^2/(4L^2)\), define
\[
W_{q,L}(y)=\int_0^\infty e^{-qt}\,[S_L(t)\mathbf1](y)\,dt
=\big[(q-\Delta_D)^{-1}\mathbf1\big](y).
\]
It is the unique solution of \(-W''+qW=1\), with \(W(-L)=W(L)=0\). Solving the elementary boundary-value problem gives
\[
W_{q,L}(y)=
\begin{cases}
\dfrac{1-\cosh(\sqrt q\,y)/\cosh(\sqrt q\,L)}q,&q>0,\\[2mm]
\dfrac{L^2-y^2}{2},&q=0,\\[2mm]
\dfrac{\cos(\sqrt{-q}\,y)/\cos(\sqrt{-q}\,L)-1}{-q},&-\pi^2/(4L^2)<q<0.
\end{cases}
\]
For every \(y\in(-L,L)\), \(W_{q,L}(y)>0\) and it strictly decreases continuously with real \(q\). For any interior reset law, \(\int W_{q,L}\,d\mu\) goes to infinity as \(q\downarrow-\pi^2/(4L^2)\): the first Dirichlet eigenfunction \(\cos(\pi y/(2L))\) is strictly positive at every reset site. The integral goes to zero as \(q\to\infty\). Thus the equation
\[
\boxed{\quad r\int W_{\lambda+r-1,L}(y)\,\mu(dy)=1\quad}
\tag{1}
\]
has exactly one real root with \(\lambda>\lambda_0=1-r-\pi^2/(4L^2)\). This is the leading exponential population-growth rate. Indeed, an eigenmeasure of the forward equation with total mass \(M>0\) satisfies \((\lambda+r-1-\Delta_D)u=rM\mu\). Integrating its resolvent yields (1), and the resulting eigenmeasure is strictly positive. To exclude a nonreal eigenvalue to its right, use the nonnegative Dirichlet survival kernel in the Laplace representation: for complex \(q\) with real part above the first Dirichlet pole, \(|\int W_{q,L}\,d\mu|\le\int W_{\Re q,L}\,d\mu\), with strict inequality if \(\Im q\ne0\). The right side is less than one above the root of (1). Zero-mass eigenmodes, if any, are Dirichlet Laplacian eigenmodes shifted by \(1-r\) and have real part at most \(\lambda_0\). Consequently, (1) determines the unique simple dominant real root. Equivalently, the nonnegative renewal kernel arising from resets has its rightmost Laplace singularity at this root.

**2. Strict curvature in squared displacement.** Put \(z=y^2\) and \(F_{q,L}(z)=W_{q,L}(\sqrt z)\) for \(0\le z\le b^2\). For \(q>0\), the function \(z\mapsto\cosh(\sqrt{qz})\) is strictly convex: with \(s=\sqrt{qz}>0\), its second derivative has the sign of \(s\cosh s-\sinh s>0\), with the same positive limiting curvature at zero. Since the coefficient of this cosh term in \(W\) is negative, \(F_{q,L}\) is strictly concave. For \(-\pi^2/(4L^2)<q<0\), write \(k=\sqrt{-q}\); \(z\mapsto\cos(k\sqrt z)\) has second derivative of the sign \(\sin s-s\cos s>0\), for \(0<s<\pi/2\) (and has a positive limit at zero), so \(F_{q,L}\) is strictly convex. At \(q=0\), \(F_{0,L}(z)=(L^2-z)/2\) is affine. These curvature statements hold for every supported \(z\), including at zero.

Under a strict convex-order spread of the squared displacement, therefore,
\[
\int W_{q,L}\,d\nu
\begin{cases}
>\int W_{q,L}\,d\mu,&q<0,\\
=\int W_{q,L}\,d\mu,&q=0,\\
<\int W_{q,L}\,d\mu,&q>0.
\end{cases}
\tag{2}
\]
This is strict because the squared-variable laws are different and the curvature is everywhere strict for nonzero \(q\).

**3. Universal crossing.** Evaluate (1) at \(\lambda=1-r\), so \(q=0\). Both reset laws have identical score
\[
r\int W_{0,L}\,d\mu=\frac r2(L^2-m_2).
\]
The strict decrease of the score in \(\lambda\) implies
\[
\operatorname{sgn}(\lambda_\mu(L,r)-(1-r))
=\operatorname{sgn}(L^2-m_2-2/r).
\]
The same holds for \(\nu\). At \(L=L_\times=\sqrt{m_2+2/r}\), both roots are \(1-r\). If \(b<L<L_\times\), the root for \(\mu\) has negative \(q\). By (2), the score for \(\nu\) is strictly larger at that root, so its root is strictly larger. If \(L>\max(b,L_\times)\), the sign of \(q\) is positive, the score for \(\nu\) is strictly smaller, and its root is strictly smaller. This proves the claimed global ordering for **all** admissible half-widths, not merely for sufficiently small perturbations.

**4. Critical width and fourth moment.** The leading growth exponent strictly increases with \(L\): enlarging an absorbing habitat strictly increases survival probabilities in the Dirichlet heat representation, hence also the rightmost renewal growth exponent. At \(r=1\), the equation at exponent \(\lambda=0\) becomes \((L^2-m_2)/2=1\). If \(b<L_0=\sqrt{2+m_2}\), this gives the unique admissible positive critical width \(L_c(1)=L_0\). By the implicit-function theorem, both critical-width branches exist smoothly near \(r=1\). Expand \(W_{q,L}\) at \(q=0\) by solving \((-\partial_{xx}+q)W=1\) recursively:
\[
W_{q,L}(y)=\frac{L^2-y^2}{2}
-\frac q{24}(5L^4-6L^2y^2+y^4)+O(q^2),
\]
with the remainder uniform for \(|y|\le b\), \(L\) near \(L_0\). Differentiating the threshold relation \(r\mathbb E W_{r-1,L_c(r)}(Y)=1\) at \(r=1\) yields
\[
L_c'(1)=\frac{1}{L_0}
\left[\frac{5L_0^4-6L_0^2m_2+m_4}{24}-1\right].
\]
Subtract the two branches to obtain the announced fourth-moment contrast. The common-second-moment convex-order relation implies \(m_{4,\nu}>m_{4,\mu}\) by choosing the strictly convex test \(z^2\).

**5. Exact reversal in one habitat.** For the displayed two reset laws, the squared displacement is deterministically \(1/2\) under \(\mu\), while under \(\nu\) it is equally likely to be \(0\) or \(1\); hence the latter is a strict mean-preserving spread, \(m_2=1/2\), and the actual reset sites lie strictly within \(L=79/50\). Also \(\lambda_0<0\) at both \(r=4/5\) and \(r=2\), so the sign of the dominant growth exponent is determined by whether the left side of (1) evaluated at \(\lambda=0\) exceeds one.

For \(r=4/5\), put \(k=1/\sqrt5\). The growth condition is exactly
\[
\frac45\mathbb E\cos(kY)>\cos(kL).
\]
For \(\mu\) the left-minus-right difference belongs to the rigorous rational enclosure \([-0.000243134545,-0.000243134544]\); for \(\nu\) it belongs to \([0.000086879311,0.000086879312]\). Thus \(\mu\) decays and \(\nu\) grows. For \(r=2\), the growth condition is exactly
\[
\cosh(L)>2\mathbb E\cosh(Y).
\]
The left-minus-right difference for \(\mu\) belongs to \([0.009281781678,0.009281781679]\), while for \(\nu\) it belongs to \([-0.012615180095,-0.012615180094]\); hence the verdict reverses. The bounds are outward-rounded for presentation and are obtained from finite rational Taylor sums with rigorous alternating-series and geometric-tail errors. Their signs do not rely on floating-point approximations.

## Verification

Execute `python3 verification.py` with any standard Python 3 interpreter. This standalone source file uses exact `fractions.Fraction` arithmetic and validates the four strict inequalities with Taylor remainder enclosures; it also verifies both reset laws' common second moment and distinct fourth moments. The entire crossing theorem and the smooth critical-width expansion are analytic proofs above; no finite computation is substituted for those infinite-dimensional claims. The included checker is intentionally limited to the concrete parameter witness.

## Relationship to prior work

Menon, de Castro and Anteneodo study critical population habitat size under stochastic resetting to a fixed site and explicitly propose distributions of resetting sites for future investigation; the lethal-boundary setup and ecological persistence motivation are shared. The new statements address *arbitrary compactly supported reset-site laws* at fixed second moment, a universal convex-order crossover and an exact same-habitat change in the extinction sign. The prior fixed-site conclusions are not claimed as new.

Evans and Majumdar give foundational renewal/resolvent methods for resetting to a random position. Julián-Salgado, Dagdug and Boyer analyze two reset sites and general distributed reset sites in search/first-passage models. Méndez, Flaquer-Galmés and Campos investigate first passage to a single target under distributed resetting. The related 2026 confined-ring work likewise concerns optimized first passage. These establish crucial general machinery and distribution-dependent search phenomena, but the inspected statements concern first-passage optimization or a different boundary geometry, rather than the two-lethal-boundary population-growth spectral comparison and universal convex-order crossing proved here. General operator-theoretic results could still imply aspects of this specialization, and the absence of a matching result in examined literature does not constitute a uniqueness proof.

## Limitations

The growth, extinction, and critical-width statements concern a linear deterministic mean-population equation on a symmetric one-dimensional interval with perfectly absorbing endpoints, spatially constant diffusion and reproduction, spatially independent Poisson relocation at one common rate, and a reset law supported strictly inside the habitat. No stochastic extinction probability, nonlinear carrying-capacity equilibrium, finite external mortality, asymmetric habitat or higher-dimensional extension is proved. The ordering compares distributions of the **squared** destination positions in convex order at equal second moment; without that hypothesis no all-width ordering is asserted. A critical width above the support is only claimed where the support-size condition holds. The positive-versus-negative exponential-growth reversal is a theorem about the linear operator, not a claim of permanent persistence of an individual finite stochastic population. 

## References

1. L. Menon Jr., P. de Castro and C. Anteneodo, *Critical habitat size of organisms diffusing with stochastic resetting*, arXiv:2505.03727v1 (first posted 6 May 2025), https://arxiv.org/abs/2505.03727 .
2. M. R. Evans and S. N. Majumdar, *Diffusion with optimal resetting*, arXiv:1107.4225 (2011), https://arxiv.org/abs/1107.4225 .
3. P. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (2023), https://arxiv.org/abs/2311.11897 .
4. V. Méndez, I. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125 (2024), https://arxiv.org/abs/2401.01125 .
5. P. Julián-Salgado, L. Dagdug and D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, arXiv:2507.14483 (2025), https://arxiv.org/abs/2507.14483 .
6. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer, *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414 (2026), https://arxiv.org/abs/2605.08414 (abstract compared; complete text not inspected).
