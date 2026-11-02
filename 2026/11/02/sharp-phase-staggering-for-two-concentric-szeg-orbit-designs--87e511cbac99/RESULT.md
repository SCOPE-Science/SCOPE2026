# Sharp phase staggering for two concentric Szegő orbit designs

## Finding

In the Hardy space \(H^2(\mathbb D)\), let \(k_z(w)=\sqrt{1-|z|^2}/(1-\overline z w)\) be a unit-norm Szegő reproducing kernel. For every pair of positive integers \(m,n\) and radii \(0<r,s<1\), consider the two regular evaluation orbits
\[
Z_\theta=\{r\exp(2\pi i j/m):0\le j<m\}\ \cup\ \{s\exp(i\theta+2\pi i k/n):0\le k<n\}.
\]
The notation counts the two lists separately; if nodes coincide, the associated Gram matrix is singular. Let \(G_\theta\) be the \((m+n)\)-by-\((m+n)\) Gram matrix of the displayed normalized kernels, and put
\[
 L=\operatorname{lcm}(m,n),\quad g=\gcd(m,n),\quad a=r^L,\quad b=s^L,
 \qquad C_p(u)=\left(\frac{p(1-u^2)}{1-u^{2p}}\right)^p u^{p(p-1)}.
\]
Then the **complete two-orbit phase law** is
\[
 \boxed{\det G_\theta=C_m(r)C_n(s)
 \left(\frac{a^2+b^2-2ab\cos(L\theta)}{1+a^2b^2-2ab\cos(L\theta)}\right)^g.}
\]
The **unique maximizing relative rotations**, modulo the design's period \(2\pi/L\), are
\[
 \boxed{\theta\equiv\frac\pi L\pmod{\frac{2\pi}L}},
 \qquad
 \boxed{\max_\theta\det G_\theta=C_m(r)C_n(s)
 \left(\frac{a+b}{1+ab}\right)^{2g}.}
\]
In particular, the optimal relative angle is independent of both radii, even when the orbit cardinalities are unequal.

The optimality admits a **globally sharp stability estimate**. Define
\[
 \alpha=\frac{2ab}{(a+b)^2},\qquad
 \beta=\frac{2ab}{(1+ab)^2},\qquad
 t=1+\cos(L\theta),\qquad 0<\beta<\alpha\le\tfrac12.
\]
With \(D_*=\max_\phi\det G_\phi\),
\[
 \boxed{\log\frac{D_*}{\det G_\theta}
 =g\log\frac{1-\beta t}{1-\alpha t}
 \ \ge\ g(\alpha-\beta)t.}
\]
If \(\det G_\theta=0\), interpret the logarithm as \(+\infty\). The inequality is strict away from a maximizing phase when the determinant is nonzero. For fixed \(m,n,r,s\), its coefficient \(g(\alpha-\beta)>0\) cannot be increased, because the quotient of the logarithmic deficit by \(t\) tends to that coefficient as \(\theta\) approaches a maximizing phase.

## Assumptions and scope

All angles are real; the two sets of nodes are finite, with multiplicities retained in the matrix. No ordering is required because Gram determinants are permutation-invariant. The kernel normalization \(\|k_z\|_{H^2}=1\) is essential to the displayed \(C_p\), though it does not affect the optimal phase. The dimension ranges over all integers \(m,n\ge1\) with no coprimality assumption. Radii must be strictly between zero and one, including the equal-radius case. The only coincident-node configurations arise when \(r=s\) and \(L\theta\in2\pi\mathbb Z\).

For distinct nodes let \(B\) be the finite Blaschke product whose zero set is \(Z_\theta\). Each kernel \(k_z\) is in \(H^2\ominus BH^2\), and the iterated system \(\{B^qk_z:q\ge0,\ z\in Z_\theta\}\) is a Riesz basis of \(H^2\). Thus the same determinant is the finite seed-block \(D\)-optimality criterion for an infinite orbit basis. It is not the determinant of an infinite Gram operator. At coincident nodes the seed system is linearly dependent and cannot be such a Riesz basis.

## Proof

**1. Cauchy determinant identity.** For any finite list of points \(z_1,\ldots,z_d\) in the disk (including repeated points by continuity), the Cauchy double-alternant formula, with unit kernel normalization, yields
\[
\det[\langle k_{z_i},k_{z_j}\rangle]_{i,j=1}^{d}
=\prod_{1\le i<j\le d}\left|\frac{z_i-z_j}{1-\overline{z_i}z_j}\right|^2.
\]
Split the product into within-first-ring, within-second-ring, and cross-ring factors.

**2. Within-ring contribution.** For \(p\ge1\), the Gram matrix at the points \(u\exp(2\pi i j/p)\) is circulant. Its Fourier eigenvalues are
\[
\lambda_\ell=\frac{p(1-u^2)u^{2\ell}}{1-u^{2p}},\qquad0\le\ell<p,
\]
by summing the geometric series of the Szegő kernel and applying discrete Fourier orthogonality. Their product is precisely \(C_p(u)\). This formula includes \(p=1\), for which \(C_1(u)=1\).

**3. Cross-ring resultants.** Let \(\zeta_p=\exp(2\pi i/p)\). The two root-of-unity product identities are
\[
\prod_{j=0}^{m-1}\prod_{k=0}^{n-1}
(r\zeta_m^j-s e^{i\theta}\zeta_n^k)
=\pm(r^L-s^Le^{iL\theta})^g,
\]
\[
\prod_{j=0}^{m-1}\prod_{k=0}^{n-1}
(1-rs e^{-i\theta}\zeta_m^j\overline{\zeta_n^k})
=(1-(rs)^Le^{-iL\theta})^g.
\]
To verify the first, take the product over \(k\) to get \(r^n\zeta_m^{nj}-s^n e^{in\theta}\) and then note that \(\zeta_m^{nj}\), as \(j\) ranges, traverses the \((m/g)\)-th roots of unity exactly \(g\) times. The second follows by the same calculation with \(1-x\zeta\). Taking squared absolute values gives the cross-ring pseudohyperbolic factor
\[
\left(\frac{|a-be^{iL\theta}|^2}{|1-ab e^{iL\theta}|^2}\right)^g.
\]
Multiplying by the two within-ring determinants proves the boxed exact formula, including collision limits.

**4. Strict phase optimality.** Let \(c=\cos(L\theta)\). The derivative of the unpowered cross-ring fraction is
\[
\frac{d}{dc}\frac{a^2+b^2-2abc}{1+a^2b^2-2abc}
=-\frac{2ab(1-a^2)(1-b^2)}{(1+a^2b^2-2abc)^2}<0.
\]
Thus the cross-ring factor is strictly decreasing in \(c\in[-1,1]\). The unique maximum within one phase period occurs at \(c=-1\), giving the claimed maximizing phases and optimal value.

**5. Sharp stability.** Substitute \(c=t-1\) and divide by the value at \(c=-1\), obtaining
\[
\frac{\det G_\theta}{D_*}
=\left(\frac{1-\alpha t}{1-\beta t}\right)^g.
\]
The identity
\[
\alpha-\beta=\frac{2ab(1-a^2)(1-b^2)}{(a+b)^2(1+ab)^2}>0
\]
implies \(0<\beta<\alpha\le1/2\). For \(0\le t<1/\alpha\), differentiate
\[
 F(t)=\log\frac{1-\beta t}{1-\alpha t}:
 \qquad F'(t)=\frac{\alpha-\beta}{(1-\alpha t)(1-\beta t)}\ge\alpha-\beta,
\]
with strictness for \(t>0\). Since \(F(0)=0\), integration proves the global estimate. At \(\alpha t=1\), which only occurs for coincident nodes, its left side diverges and the result remains valid. Finally \(F(t)/t\to F'(0)=\alpha-\beta\), so no larger coefficient works.

**6. Orbit interpretation.** For a Blaschke product with \(d=m+n\) distinct zeros, its model space \(K_B=H^2\ominus BH^2\) has dimension \(d\). Each kernel at a zero lies in \(K_B\) by the reproducing property and \(B(z)=0\); the Cauchy determinant is positive, so the \(d\) kernels form a basis of \(K_B\). The orthogonal Wold decomposition \(H^2=\bigoplus_{q\ge0}B^qK_B\) transfers that finite seed basis to the stated infinite Riesz basis. Its seed-block determinant is exactly the quantity optimized above.

## Verification

The accompanying executable `CHECK.py` computes normalized kernel Gram determinants directly and compares them with the closed formula across \(160\) finite parameter configurations. It also checks the global sharp-stability inequality on those configurations and verifies the local sharpness ratio at three small angular offsets. All \(163\) checks pass under Python 3 and NumPy. This finite evidence is supplementary: Steps 1–6 prove the statements for every allowed integer, radius, and phase.

## Relationship to prior work

Aguilera and Carando [1, Theorem 2.6] establish the finite-Blaschke-multiplier criterion and an orthonormal Malmquist–Walsh orbit construction, but do not optimize the raw kernel seeds or their relative phase on two radii. The prior exact one-circle result [2] proves regularity and a sharp angular-defect bound with all zeros on **one** fixed circle. It explicitly excludes mixed radii, whereas the present theorem determines the cross-ring interaction for arbitrary, independently prescribed orbit sizes and radii, including the arithmetic exponent \(g=\gcd(m,n)\), the period determined by \(L=\operatorname{lcm}(m,n)\), and the globally sharp phase-loss coefficient.

Neumayer and Ullrich [3] discuss kernel \(D\)-optimal sampling designs in general reproducing-kernel spaces; no two-ring Szegő formula appears in the accessible abstract. A classical two-concentric-circle Fekete discussion [4] motivates regular interlacing, but asks an **unrestricted Euclidean-distance** optimization question and does not establish the present pseudohyperbolic kernel determinant or its sharp stability. The Cauchy double alternant and the cyclotomic product are classical proof ingredients and are not themselves claimed as new.

## Limitations

The design family consists of two **individually regular** polygons, not arbitrary point arrangements on two circles; this theorem does not solve the unrestricted two-circle Fekete problem or prove that arbitrary optimizers must have regular angular gaps. It optimizes the determinant, not the smallest Gram eigenvalue or the spectral condition number. Only the standard disk Szegő kernel and its raw normalized reproducing kernels are considered. The general \(D\)-optimal sampling paper [3] could be inspected at abstract level only; unindexed equivalent classical energy or resultant formulations remain residual originality risks. No independent mathematical audit has been performed.

## References

[1] A. Aguilera and D. Carando, *Frames of orbits of multiplication operators on Hardy spaces*, arXiv:2606.00912v1, first posted 30 May 2026. Author-uploaded full text: https://www.researchgate.net/publication/405683690_Frames_of_orbits_of_multiplication_operators_on_Hardy_spaces .

[2] *Sharp determinant stability and conditioning of concentric Szegő orbit frames* (2026), public mathematical record: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-determinant-stability-and-conditioning-of-concentric-szeg--44f30fce73fa .

[3] S. Neumayer and T. Ullrich, *A sharp bound for sampling widths in the uniform norm: kernel \(D\)-optimal designs and oversampling*, arXiv:2609.15556v1, first posted 14 September 2026, https://arxiv.org/abs/2609.15556 .

[4] *How to best distribute points on two concentric circles?*, MathOverflow question 21298, April 2010, https://mathoverflow.net/questions/21298/how-to-best-distribute-points-on-two-concentric-circles .
