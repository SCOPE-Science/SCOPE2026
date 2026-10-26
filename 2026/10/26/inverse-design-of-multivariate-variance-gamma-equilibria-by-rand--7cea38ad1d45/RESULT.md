# Inverse design of multivariate variance-gamma equilibria by random Brownian resetting

## Finding

Let \(d\ge1\), \(D,\lambda>0\), and \(\kappa=D/\lambda\). Consider Brownian diffusion on \(\mathbb R^d\) with generator \(D\Delta\), interrupted at rate-\(\lambda\) Poisson events. At each event the position \(x\) becomes \(Ux\), independently, for a multiplier \(U\in[0,1]\) satisfying \(\Pr(U<1)>0\). For given \(q,\beta>0\), define the symmetric variance-gamma target by its characteristic function
\[
\phi_{q,\beta}(t)=(1+\beta\|t\|^2)^{-q},\qquad t\in\mathbb R^d.
\]
**Inverse classification.** The target is the unique invariant law if and only if
\[
q\ge1,\qquad \beta\ge\kappa,
\]
and, with \(h=\kappa/\beta\in(0,1]\), the multiplier has the **unique** distribution
\[
\mathcal L(U)=\begin{cases}
(1-h)\delta_1+h\delta_0,&q=1,\\
(1-h)\delta_1+h\operatorname{Beta}(2q-2,1),&q>1.
\end{cases}
\]
The beta law uses the ordinary shape convention: its density on \((0,1)\) is \((2q-2)u^{2q-3}\). Thus a target with \(0<q<1\) or \(0<\beta<\kappa\) is impossible under these assumptions. If every reset is effective, namely \(\Pr(U=1)=0\), necessarily \(\beta=\kappa\); as one concrete case, uniform multipliers give \(q=3/2\) and \(\beta=\kappa\). This holds in **every finite dimension**.

## Assumptions and scope

Between Poisson events, \(dX_t=\sqrt{2D}\,dB_t\), where \(B_t\) is standard \(d\)-dimensional Brownian motion. A rate-\(\lambda\) Poisson process and all independent multipliers are independent of Brownian motion. Resetting maps \(x\) to \(Ux\), with the same scalar \(U\) applied to all coordinates; there is no independent additive kick at resetting. The conditions \(\Pr(U<1)>0\) and \(U\in[0,1]\) ensure genuine contraction. The target is the characteristic-function definition above, equivalently the law of \(\sqrt{2\beta G}\,Z\), where \(G\sim\operatorname{Gamma}(q,1)\) and \(Z\sim N(0,I_d)\) independently. No assertion is made about anisotropic covariance, state-dependent multipliers, non-Poisson times, or multipliers outside \([0,1]\).

## Proof

**Existence, uniqueness, and fixed-point identity.** Let \(E\sim\operatorname{Exp}(\lambda)\). Independent Brownian displacement \(Z_0=\sqrt{2D}\,B_E\) has characteristic function
\[
\mathbb E e^{i\langle t,Z_0\rangle}=(1+\kappa\|t\|^2)^{-1}.
\]
At independent exponential event intervals, the usual backward affine perpetuity is
\[
X_\infty\ \stackrel{d}{=}\ \sum_{j=0}^{\infty}\left(\prod_{k=1}^{j}U_k\right)Z_j,
\]
with iid copies of the corresponding multipliers and exponential-time Brownian displacements. Its terms are independent and centered conditional on multipliers, and its series converges in \(L^2\) because \(\mathbb E U^2<1\). Looking backward from a stationary observation time or using the Poisson renewal equation gives
\[
X_\infty\stackrel d=Z_0+UX_\infty',
\qquad
(1+\kappa\|t\|^2)\phi(t)=\mathbb E[\phi(Ut)], \tag{1}
\]
with independent variables on the right. These equations yield the invariant law. Moreover synchronous coupling of two trajectories under the same Brownian path, Poisson events and multipliers gives
\[
\mathbb E\|X_t^{x}-X_t^{y}\|^2=
\exp\bigl(-\lambda t[1-\mathbb E U^2]\bigr)\|x-y\|^2.
\]
The difference actually tends to zero almost surely. Combined with the invariant perpetuity this proves uniqueness for arbitrary initial probability laws, without a moment assumption on the initial law.

**Necessary coefficients.** In (1), substitute \(\phi(t)=(1+\beta\|t\|^2)^{-q}\), set \(z=\beta\|t\|^2\), and put \(h=\kappa/\beta>0\). We must have, for every \(z\ge0\),
\[
\mathbb E(1+zU^2)^{-q}=(1+hz)(1+z)^{-q}. \tag{2}
\]
All the series about \(z=0\) converge in a common neighborhood because \(0\le U\le1\). Equating coefficients gives for every integer \(n\ge1\)
\[
\mathbb E U^{2n}=1-\frac{hn}{q+n-1}. \tag{3}
\]
For \(0<q<1\), (3) forces
\[
\mathbb E U^4-\mathbb E U^2=\frac{h(1-q)}{q(q+1)}>0,
\]
contradicting \(U^4\le U^2\). Hence \(q\ge1\). Since \(U^{2n}\to\mathbf1_{\{U=1\}}\) as \(n\to\infty\), dominated convergence in (3) yields
\[
\Pr(U=1)=1-h\ge0,
\]
so \(h\le1\), equivalently \(\beta\ge\kappa\).

**Recovering the only possible reset law.** If \(q=1\), (3) says \(\mathbb E U^{2n}=1-h\) for all \(n\ge1\), giving \((1-h)\delta_1+h\delta_0\). If \(q>1\), rewrite (3) as
\[
\mathbb E U^{2n}=(1-h)+h\frac{q-1}{q+n-1}.
\]
The second term is the \(n\)-th moment of a \(\operatorname{Beta}(q-1,1)\) random variable \(W=U^2\). Hence the displayed mixture is the unique measure with these moments: probability measures on \([0,1]\) are determined by their full moment sequence (polynomial density in continuous functions). Equivalently, the non-atomic law of \(U\) is \(\operatorname{Beta}(2q-2,1)\).

**Sufficiency and boundary cases.** For \(q>1\) and \(V\sim\operatorname{Beta}(2q-2,1)\), substitution \(w=V^2\) and one differentiation show
\[
\begin{aligned}
\mathbb E(1+zV^2)^{-q}
&=(q-1)\int_0^1 w^{q-2}(1+zw)^{-q}\,dw\\
&=\left[w^{q-1}(1+zw)^{1-q}\right]_{w=0}^{1}\\
&=(1+z)^{1-q}.
\end{aligned}
\]
Adding an atom of weight \(1-h\) at \(U=1\) gives
\[
(1-h)(1+z)^{-q}+h(1+z)^{1-q}
=(1+hz)(1+z)^{-q},
\]
which is (2). For \(q=1\), the stated two-atom law directly gives the same identity. The perpetuity uniqueness above therefore proves that these and only these reset laws realize the requested stationary distributions. Finally, \(\Pr(U=1)=1-h\) proves the fully effective-reset boundary. A uniform multiplier is precisely \(\operatorname{Beta}(1,1)\), giving \(2q-2=1\) and \(q=3/2\).

## Verification

The standalone `verify.py` uses exact rational arithmetic to check 5,769 moment and monotonicity identities/inequalities for selected positive rational shapes and mixture weights, plus 60 independent numerical quadratures of the beta integral. It produces `PASS 5829 exact/numerical identity checks` using Python 3 with no external packages. The infinite classification, existence, and uniqueness depend on the analytical arguments above; finite checks are not substitutes for these arguments. The verification includes the impossible \(q<1\) boundary and all mixture branches.

## Relationship to prior work

Assefa, Keller-Ressel and Palmowski (2026, arXiv:2610.01363) develop general matrix-based formulas for moments of polynomial processes with affine resetting. The present inverse problem specifies an entire stationary characteristic function and classifies every admissible stochastic multiplier. Tal-Friedman, Roichman and Reuveni (2022, arXiv:2205.03363) find the stationary law under a *fixed* partial-reset proportion as an infinite Laplace convolution. Grzywny and collaborators (arXiv:2412.15626, published 2026) treat a fixed multiplier for stable processes, including Brownian motion. Palmowski and collaborators (arXiv:2605.18136) principally study exit identities with a fixed reset fraction. The beta-integral step is a classical beta-gamma algebra identity and is not itself claimed as new. The specific combination of a sharp inverse feasible region, uniqueness of the random multiplier distribution, and all-dimensional variance-gamma realization is the additional statement established here.

## Limitations

Originality is qualified: a more general perpetuity theorem or beta-gamma fixed-point classification not located in the accessible searched literature may imply this special result, and this should be examined independently before a publication priority claim. Fixed-proportion results are not equivalent to the random beta-factor law. The classification is limited to common scalar multipliers in \([0,1]\), ordinary Brownian diffusion, Poisson events, and the stated radial target family. Numerical quadrature is only a consistency check.

## References

1. J. Assefa, M. Keller-Ressel and Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363v1 (first public October 1, 2026), https://arxiv.org/abs/2610.01363.
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363v2 (first public May 6, 2022), https://arxiv.org/abs/2205.03363.
3. Z. Palmowski, N. Beelders, L. Ramsden and A. D. Papaioannou, *Lévy processes with partially stochastic resetting*, arXiv:2605.18136 (first public May 18, 2026), https://arxiv.org/abs/2605.18136.
4. T. Grzywny, Z. Palmowski, K. Szczypkowski and B. Trojan, *Stationary states for stable processes with partial resetting*, arXiv:2412.15626, *Annals of Applied Probability* 36 (2026), 1110–1177, https://arxiv.org/abs/2412.15626.
