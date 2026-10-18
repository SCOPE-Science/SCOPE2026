# An exact projective singular-value map and a three-dimensional finite-termination barrier for polar descent

## Finding

For the isotropic quadratic \(F(X)=\frac12\|X\|_F^2\) on real square matrices, the minimum-Frobenius-norm polar direction combined with exact nonnegative line search has a sharp dimension transition: in dimensions one and two it terminates in at most two steps, while dimension three admits nonterminating geometric orbits. More strongly, the full-rank three-dimensional singular-value dynamics after the first iteration reduce to one explicit piecewise fractional map.

Write the three nonzero singular values in decreasing order as \(a\ge b\ge c>0\). After any full-rank three-dimensional iteration, they obey \(a=b+c\). Thus put \(t=b/a\in[1/2,1)\). Provided the next iterate remains full rank, its normalized ratio is

\[
T(t)=\begin{cases}3t-1,&\frac12\le t<\frac23,\\\frac{1}{3t-1},&\frac23<t<1.\end{cases}
\]

The next largest singular value equals \(a/3\) on the first branch and \(a(t-1/3)\) on the second. At \(t=2/3\), the next rank becomes two and one more update gives zero.

The map has the asymmetric fixed point

\[
t_* = \frac{1+\sqrt{13}}6,\qquad q=\frac{\sqrt{13}-1}6\in(0,1).
\]

Starting with \(X_0=\operatorname{diag}(1,t_*,1-t_*)\), every iterate is nonzero and full rank, with singular values a permutation of \(q^k(1,t_*,1-t_*)\), for every integer \(k\ge0\). Consequently \(F(X_k)=q^{2k}F(X_0)\), so no finite iteration reaches the minimum although the Hessian is the identity. The separate fixed ratio \(t=1/2\) has singular-value scaling factor \(1/3\).

## Assumptions and scope

All matrices are real square matrices of dimension \(d\in\{1,2,3\}\). Arithmetic is exact, no momentum or stochastic perturbation is included, and the objective is \(F(X)=\frac12\operatorname{tr}(X^\top X)\). For every nonzero \(X\), let \(X=U\operatorname{diag}(s_1,\ldots,s_r)V^\top\) be a thin singular-value decomposition with all \(s_i>0\); the polar direction is \(P(X)=UV^\top\), zero on the null singular subspaces. The update uses \(\eta(X)=\operatorname*{argmin}_{\eta\ge0}F(X-\eta P(X))\), and is \(X^+=X-\eta(X)P(X)\). Set \(X^+=0\) for \(X=0\). At rank deficiency this specific thin-polar choice matters: arbitrary extensions of the polar factor are not claimed to obey the same dynamics.

## Proof

**Exact line search.** Since \(\langle X,P(X)\rangle=\sum_{i=1}^r s_i\) and \(\|P(X)\|_F^2=r\), direct differentiation of \(F(X-\eta P(X))\) shows the unique minimizer is \(\eta=\overline s=\frac1r\sum_{i=1}^r s_i\). In the singular-vector coordinates, the new nonzero spectral entries are \(s_i-\overline s\); its singular values are precisely \(|s_i-\overline s|\), with zero entries removed. This calculation holds also when the iterate becomes rank deficient.

**Dimensions at most two.** At rank one, the sole singular value is annihilated by exact line search. At rank two, the pair \((u,v)\), with \(u\ge v>0\), becomes \(((u-v)/2,(u-v)/2)\). If these both vanish, termination is immediate; otherwise they are equal and vanish at the following step. This proves at most two steps for any initial real matrix of dimension \(d\le2\).

**Three-value invariant.** Let \((z_1,z_2,z_3)\) be any three real numbers summing to zero. The absolute value of one of them equals the sum of the absolute values of the other two: when exactly one sign differs from the remaining two, the sum-zero identity gives this equality; zeros are handled by continuity or directly. For a full-rank three-dimensional polar descent step, the three centered deviations sum to zero. Hence when their absolute values are nonzero, the sorted resulting singular values satisfy \(a=b+c\). With \(a>0\), set \(t=b/a\); sortedness and \(c>0\) give \(1/2\le t<1\).

**Projective law.** The mean of \((a,at,a(1-t))\) is \(2a/3\). The absolute deviations, divided by \(a\), are \((1/3,|t-2/3|,t-1/3)\). If \(t\in[1/2,2/3)\), they sort as \((1/3,t-1/3,2/3-t)\), giving largest-value factor \(1/3\) and ratio \(3t-1\). If \(t\in(2/3,1)\), they sort as \((t-1/3,1/3,t-2/3)\), giving factor \(t-1/3\) and ratio \(1/(3t-1)\). At \(t=2/3\), the output has one zero and two singular values \(a/3\); the rank-two computation above then annihilates both.

**Nontermination with identity curvature.** The equation \(t=1/(3t-1)\) has the unique solution in \((2/3,1)\) equal to \(t_*=(1+\sqrt{13})/6\). Its largest-value scaling is \(q=t_*-1/3=(\sqrt{13}-1)/6\). Since its next normalized spectrum equals itself, induction shows each following spectrum is exactly the initial one scaled by \(q^k\). Here \(0<q<1\), all three singular values remain positive for every finite integer \(k\), and the Frobenius objective scales as \(q^{2k}\). The first-branch fixed point \(t=1/2\) similarly gives the other geometric orbit, with scale \(1/3\). Thus dimension three is minimal for nonterminating exact-line-search polar descent on an isotropic quadratic, and the displayed geometric instance is explicit.

## Verification

The embedded standard-library program `CHECK.py` checks the fractional map exactly over rational grid points, checks two-dimensional termination using exact fractions, and checks 26 iterates of the asymmetric fixed-point orbit at 90-digit decimal precision. Successful execution prints `PASS`. These finite computations support but are not substituted for the algebraic proof for every real admissible parameter.

## Relationship to prior work

Oikonomidis et al. (2026) study constrained and stochastic spectral preconditioning and explicitly formulate thin-polar matrix-sign updates. Nguyen et al. (2026) study stability and rates attributable to spectral flattening, including a maximum stable step derived from average singular values. Li and Hong (2025) study convergence bounds for Muon. Their mathematical guarantees do not, in their inspected statements and relevant proofs, provide this post-first-step invariant, the one-dimensional three-mode map, or the minimal-dimension nontermination construction for exact line search. The latter statements therefore concern a different fine-grained dynamical question. General matrix-polar and exact-line-search formulas are established ingredients, not claimed as inventions.

## Limitations

The findings are restricted to exact arithmetic, an isotropic Frobenius quadratic, and the thin-polar direction under an exact line search. They do not apply without further proof to finite-precision Newton–Schulz approximations, momentum, noise, arbitrary spectral preconditioners, or dimensions above three. The piecewise map describes nonzero full-rank iterates after the first step, not rank-loss states. No global worst-case convergence rate is claimed. Literature coverage is not exhaustive and unindexed equivalent formulations remain a residual originality risk. Independent verification has not been performed.

## References

1. K. Oikonomidis, J. Quan, K. Antonakopoulos, A. Silveti-Falls, V. Cevher, P. Patrinos, *Constrained Stochastic Spectral Preconditioning Converges for Nonconvex Objectives*, arXiv:2605.11850v1, 12 May 2026. https://arxiv.org/html/2605.11850v1
2. T.-P. Nguyen et al., *Spectral Flattening Is All Muon Needs: How Orthogonalization Controls Learning Rate and Convergence*, arXiv:2605.13079v1, 13 May 2026. https://arxiv.org/html/2605.13079v1
3. X. Li and D. Hong, *A Note on the Convergence of Muon*, arXiv:2502.02900, February 2025. https://arxiv.org/abs/2502.02900
