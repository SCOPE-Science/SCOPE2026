# The sharp zero-centered Bohr ball for Drury–Arveson multipliers

## Finding
For every integer \(d\ge1\), and also for countably infinitely many coordinates, the following is an exact classification. Let \(H^2_d\) be the Drury–Arveson reproducing-kernel Hilbert space on the open complex \(\ell^2\) unit ball with kernel
\[
K(z,w)=\frac1{1-\langle z,w\rangle}.
\]
For a multiplier \(f(z)=\sum_\alpha c_\alpha z^\alpha\) with \(f(0)=0\), write \(M_f\) for multiplication on \(H^2_d\), and define its absolute monomial majorant at \(z\) by
\[
\mathcal B(f,z)=\sum_{|\alpha|\ge1}|c_\alpha z^\alpha|.
\]
Then the universal zero-centered Bohr set is **exactly**
\[
\boxed{\left\{z:\ \mathcal B(f,z)\le1\ \text{for every } f(0)=0,\ \|M_f\|\le1\right\}
=\left\{z:\|z\|_2\le\frac1{\sqrt2}\right\}.}
\]
The boundary is sharp in every nonzero direction: for each \(z\) of norm \(1/\sqrt2\), an explicit contractive multiplier attains majorant one, and the same directional construction violates the inequality at every point of norm greater than \(1/\sqrt2\).

Boundary equality is rigid at the level of coefficient magnitudes. If \(\|z\|_2=1/\sqrt2\) and \(\mathcal B(f,z)=1\), then, necessarily, for every nonzero finitely supported multiindex \(\alpha\),
\[
\boxed{\lvert c_\alpha\rvert=\frac{\lvert\alpha\rvert!}{\alpha!}\lvert z^\alpha\rvert.}
\]
The displayed directional multipliers realize all these coefficient magnitudes; no uniqueness of the coefficient phases is claimed.

There is also an exact first-order crossing law. For \(0<r<1\), define
\[
B_d(r)=\sup_{\substack{\|M_f\|\le1,\ f(0)=0\\\|z\|_2=r}}\mathcal B(f,z).
\]
Writing \(r_*=1/\sqrt2\), the two one-sided expansions agree:
\[
\boxed{B_d(r)=1+2\sqrt2\,(r-r_*)+O((r-r_*)^2),\qquad r\to r_*.}
\]
The implied second-order constant is uniform in \(d\), including infinite \(d\). No formula for the entire profile \(B_d(r)\) away from \(r_*\) is asserted.

## Assumptions and scope
Coordinates are complex, indexed by \(\{1,\ldots,d\}\) or \(\mathbb N\). Multiindices \(\alpha\) are finitely supported with \(|\alpha|=\sum_j\alpha_j\), \(\alpha!=\prod_j\alpha_j!\). The normalized reproducing kernel gives mutually orthogonal monomials with
\[
\|z^\alpha\|_{H^2_d}^2=\frac{\alpha!}{|\alpha|!},\qquad \|1\|_{H^2_d}=1.
\]
The multiplier norm is the bounded-operator norm of \(M_f:H^2_d\to H^2_d\). For each \(z\) in the open unit ball the absolute majorant converges for all multipliers under consideration. The \(d\)-independent statements refer to these precise coordinate and norm conventions.

## Proof
**Upper bound.** The constant function has norm one, so every multiplier in the claim satisfies
\[
\|f\|_{H^2_d}=\|M_f1\|_{H^2_d}\le\|M_f\|\le1.
\]
With \(f(0)=0\), weighted Cauchy–Schwarz gives, for \(r=\|z\|_2<1\),
\[
\begin{aligned}
\mathcal B(f,z)
&\le\left(\sum_{|\alpha|\ge1}|c_\alpha|^2\frac{\alpha!}{|\alpha|!}\right)^{1/2}
\left(\sum_{|\alpha|\ge1}\frac{|\alpha|!}{\alpha!}|z^\alpha|^2\right)^{1/2}\\
&\le\left(\sum_{n\ge1}\left(\sum_j|z_j|^2\right)^n\right)^{1/2}
=\frac{r}{\sqrt{1-r^2}}.
\end{aligned}
\]
The multinomial theorem justifies the inner sum, including the countable-coordinate case by monotone convergence. This upper bound is at most one exactly when \(r\le1/\sqrt2\).

**Sharpness in every direction.** Let \(a=1/\sqrt2\). Fix any \(z\ne0\) and let \(u=z/\|z\|_2\). Define the linear multiplier \(\ell_u(w)=\langle w,u\rangle\). Since the Drury–Arveson coordinate row operator is a contraction, \(\|M_{\ell_u}\|\le1\). The scalar function
\[
\psi(\xi)=\xi\frac{a-\xi}{1-a\xi}
\]
is a disk Schur function (indeed a degree-two finite Blaschke product up to phase), and \(\psi(0)=0\). By von Neumann's inequality and rational functional calculus,
\[
 f_u(w)=\psi(\ell_u(w)),\qquad \|M_{f_u}\|\le1.
\]
Its one-variable expansion has coefficients \(b_1=a\) and \(b_n=-(1-a^2)a^{n-2}\) for \(n\ge2\). Because \(1-a^2=a^2\), one has \(|b_n|=a^n\) for all \(n\ge1\). If \(r=\|z\|_2\), the multinomial expansion of \(\ell_u^n\) gives
\[
\sum_{|\alpha|=n}|[w^\alpha]f_u|\,|z^\alpha|
=|b_n|\left(\sum_j|\overline{u_j}z_j|\right)^n
=a^n r^n.
\]
Consequently
\[
\boxed{\mathcal B(f_u,z)=\sum_{n\ge1}(ar)^n=\frac{ar}{1-ar}.}
\]
This equals one at \(r=a\), and exceeds one at every \(r>a\). Thus no exterior point belongs to the universal Bohr set. In particular, the upper bound is sharp at every boundary point.

**Coefficient-magnitude rigidity.** Fix \(\|z\|_2=a\). The second Cauchy–Schwarz factor in the upper bound is exactly one. If a contractive multiplier has \(\mathcal B(f,z)=1\), equality must hold in both inequalities. Thus \(\|f\|_{H^2_d}=1\) and Cauchy–Schwarz equality for the nonnegative coefficient sequences forces \(\lvert c_\alpha\rvert\sqrt{\alpha!/\lvert\alpha\rvert!}=\lvert z^\alpha\rvert\sqrt{\lvert\alpha\rvert!/\alpha!}\). This is exactly the stated rigidity formula, including coordinates at which \(z^\alpha=0\). The explicit extremizers satisfy it.

**Crossing coefficient.** The preceding two constructions show for every \(d\) and \(0<r<1\) that
\[
\frac{ar}{1-ar}\le B_d(r)\le\frac{r}{\sqrt{1-r^2}}.
\]
At \(r=a\), both bounds equal one and both have derivative \(2\sqrt2\). Their Taylor expansions differ by at most a constant times \((r-a)^2\) on a fixed neighborhood. The squeezed function \(B_d\) therefore satisfies the claimed two-sided first-order expansion with a dimension-independent quadratic remainder.

## Verification
A standalone standard-library script `CHECK.py` checks exact binomial coefficient mass identities through degree 40 in a two-variable direction, selected radial bounds and the contact derivative. Execute `python CHECK.py` from the directory containing this document. The finite tests are illustrative: the all-dimensional theorem and first-order limit follow from the explicit analytic proof above. Exact critical identities are \(a^2=1/2\), \(\sum_{n\ge1}2^{-n}=1\), and \(\frac{d}{dr}\frac{ar}{1-ar}|_{r=a}=\frac{d}{dr}\frac r{\sqrt{1-r^2}}|_{r=a}=2\sqrt2\).

## Relationship to prior work
Brevig, Seip and Zlotnikov (2026) prove that the ordinary, unrestricted Bohr set for the Drury–Arveson multiplier algebra is the Euclidean ball of radius \(1/3\). The present problem imposes the substantive normalization \(f(0)=0\), so the sharp larger radius \(1/\sqrt2\), the explicit contact functions in every direction and the crossing coefficient are not consequences of merely substituting the unrestricted constant. The scalar zero-at-origin Bohr radius and elementary one-variable Blaschke computations are classical; neither is claimed as new. The additional assertion concerns the absolute **multivariate monomial** majorant rather than the coefficients of a one-dimensional restriction, for which cancellation can hide the monomial sum.

Earlier work of Paulsen, Popescu and Singh (2002) establishes broad operator-theoretic Bohr inequalities, including reproducing-kernel multiplier settings. The comparison available here identifies no published statement that computes this normalized Drury–Arveson Bohr set with the directional contact and crossing law; the precise scope of older and current full manuscripts must still be checked independently.

## Limitations
The assertion is scalar-valued and concerns the Drury–Arveson kernel, not arbitrary complete Pick kernels, operator-valued multipliers, or a full formula for \(B_d(r)\) away from the critical radius. Finite diagnostics are not proofs of the all-dimensional claims. Full-text inspection of two especially plausible primary sources was unavailable; an earlier equivalent or stronger normalized result may exist. The record does not claim priority certification or exhaustiveness of external databases.

## References
1. O. F. Brevig, K. Seip and I. Zlotnikov, *Bohr sets for multiplier algebras of complete Pick spaces*, arXiv:2609.26395, first public version September 22, 2026. https://arxiv.org/abs/2609.26395
2. V. I. Paulsen, G. Popescu and D. Singh, *On Bohr's Inequality*, Proceedings of the London Mathematical Society 85 (2002), 493–512, DOI:10.1112/S0024611502013692.
3. The normalized Drury–Arveson reproducing kernel and the row-contraction property of its coordinate multipliers are standard background; both required normalizations are stated and used explicitly above.
