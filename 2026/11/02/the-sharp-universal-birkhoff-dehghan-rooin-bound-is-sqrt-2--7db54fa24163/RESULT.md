# The sharp universal Birkhoff–Dehghan–Rooin bound is \(\sqrt{2}\)

## Finding
Let \(X\) be a real Banach space with \(\dim X\ge2\). Define Birkhoff–James orthogonality by \(x\perp_B y\) when \(\|x+\lambda y\|\ge\|x\|\) for every \(\lambda\in\mathbb R\). For nonzero vectors define the angular and skew-angular distances
\[
\alpha[x,y]=\left\|\frac{x}{\|x\|}-\frac{y}{\|y\|}\right\|,
\qquad
\beta[x,y]=\left\|\frac{x}{\|y\|}-\frac{y}{\|x\|}\right\|.
\]
The Birkhoff-restricted Dehghan–Rooin constant is
\[
\operatorname{DR}_B(X)=\sup\left\{\frac{\alpha[x,y]}{\beta[x,y]}:\ x,y\ne0,\ x\perp_B y,\ \beta[x,y]\ne0\right\}.
\]
**Theorem.** For every such \(X\),
\[
1\le\operatorname{DR}_B(X)\le\sqrt{2}.
\]
Both bounds are optimal: Hilbert spaces satisfy the lower equality, and the real square plane \(\ell_\infty^2\) satisfies \(\operatorname{DR}_B(\ell_\infty^2)=\sqrt{2}\). More generally \(\operatorname{DR}_B(\ell_\infty^n)=\sqrt{2}\) for all integers \(n\ge2\), and likewise for real \(\ell_\infty(I)\) with at least two coordinates.

## Assumptions and scope
All spaces and scalars are **real**. No smoothness, reflexivity, strict convexity or finite-dimensionality assumption is used beyond \(\dim X\ge2\). The supremum uses ordered Birkhoff-orthogonal pairs: in general \(x\perp_B y\) does not imply \(y\perp_B x\). The result concerns the Birkhoff-restricted ratio above, **not** the unrestricted Dehghan–Rooin constant. The denominator is nonzero for Birkhoff-orthogonal nonzero pairs, as shown below.

## Proof
**1. Exact scale reduction.** Write \(x=a u\), \(y=b v\), with \(a=\|x\|>0\), \(b=\|y\|>0\), and \(u,v\in S_X\), \(u\perp_B v\). Put \(s=(a/b)^2>0\). Then
\[
\frac{\alpha[x,y]}{\beta[x,y]}=
\frac{\sqrt{s}\,\|u-v\|}{\|su-v\|}.
\]
Conversely, any \(u,v\in S_X\) with \(u\perp_B v\) and any \(s>0\) are represented by \(x=\sqrt{s}\,u\), \(y=v\). Therefore the supremum is exactly the supremum of this one-parameter profile. For every \(s>0\), Birkhoff orthogonality gives
\[
d:=\|su-v\|=s\left\|u-s^{-1}v\right\|\ge s>0.
\]
Also \(d\ge |s-1|\) by the reverse triangle inequality. Write \(m=\|u-v\|\).

**2. Small and intermediate scales.** For \(0<s\le1\), the identity \(u-v=(su-v)+(1-s)u\) gives \(m\le d+(1-s)\), whence
\[
\frac{\sqrt{s}\,m}{d}\le\sqrt{s}\left(1+\frac{1-s}{d}\right).
\]
If \(0<s\le\tfrac12\), then \(d\ge1-s\); hence the ratio is at most \(2\sqrt{s}\le\sqrt2\). If \(\tfrac12\le s\le1\), then \(d\ge s\); hence the ratio is at most \(s^{-1/2}\le\sqrt2\).

**3. Large scales.** If \(s\ge1\), the identity \(u-v=s^{-1}(su-v)-(1-s^{-1})v\) yields \(m\le s^{-1}d+1-s^{-1}\). Since \(d\ge s\),
\[
\frac{\sqrt{s}\,m}{d}
\le\frac{2s-1}{s^{3/2}}
\le\frac{4\sqrt6}{9}<\sqrt2.
\]
The middle inequality follows without approximation by multiplying its square by \(27s^3\):
\[
32s^3-27(2s-1)^2=(2s-3)^2(8s-3)\ge0\qquad(s\ge1).
\]
These cases prove the upper bound for every admissible pair, in every real Banach space.

**4. Attainment in a square.** In real \(\ell_\infty^2\), take \(u=(1,1)\), \(v=(1,0)\). Both are unit vectors. For every real \(\lambda\), \(\|u+\lambda v\|_\infty=\max\{|1+\lambda|,1\}\ge1\), so \(u\perp_B v\). At \(s=\tfrac12\),
\[
\|u-v\|_\infty=1,
\qquad \|su-v\|_\infty=\tfrac12,
\qquad \frac{\sqrt{s}\,\|u-v\|_\infty}{\|su-v\|_\infty}=\sqrt2.
\]
The same two-coordinate witness embeds isometrically in every \(\ell_\infty^n\) or \(\ell_\infty(I)\) with at least two indices. For the lower bound in arbitrary \(X\), choose \(u\in S_X\) and a nonzero \(v\) in the kernel of a norm-one supporting functional attaining value one on \(u\), then normalize \(v\). Thus \(u\perp_B v\), and \(s=1\) gives ratio one. In Hilbert spaces the Pythagorean identity shows every ratio is at most one. This finishes the proof.

## Verification
Each argument above is a norm identity, triangle inequality, or an exact polynomial factorization. The supporting functional argument guarantees nonempty admissible pairs in every dimension at least two. A standalone standard-library checker (`check.py`) tests the factorization and the bound on rational scales, including exact attainment in the square. The checker is supplementary; it does not purport to certify the universally quantified statements by enumeration.

## Relationship to prior work
Du, Hu, Zhang and Liu (2026), Proposition 2.5, give \(1\le\operatorname{DR}_B(X)\le2\) and describe the upper endpoint \(2\) as sharp, with a suggested near-square construction (Example 4.4). Their Corollary 2.4 gives the exact scale reduction used here. The present theorem improves the upper bound to the **strictly smaller sharp universal value** \(\sqrt2\). In particular, the claimed approximation of value \(2\) cannot be valid under the paper's stated definition; this conclusion follows from the direct universal norm inequalities, not from numerical experiments. The paper's lower-bound argument and exact scale formula remain valid inputs.

The 2024 work of Fu and Li addresses the *unrestricted* Dehghan–Rooin comparison; its upper bound for that different invariant does not imply the present sharp restricted bound. The 2026 work of Qi and collaborators introduces other Birkhoff-related geometric constants, but not this angular/skew-angular quotient. The exact universal restricted value was not found in targeted bibliographical and mathematical-record searches. Publication priority has not been independently established.

## Limitations
The argument does not classify equality cases among arbitrary Banach spaces or give quantitative stability near equality. The comparison depends crucially on the direction \(u\perp_B v\) and does not apply to the unrestricted constant. Only real Banach spaces are claimed. The source paper's asserted upper-endpoint sharpness is incompatible with the theorem; no independent correction or publication status is claimed. A potentially equivalent older inequality under unfamiliar terminology cannot be categorically ruled out without further literature access.

## References
1. J. Du, T. Hu, W. Zhang and Q. Liu, *A Birkhoff-Orthogonal Dehghan–Rooin Type Constant in Banach Spaces*, arXiv:2609.27754v1 (first public August 15, 2026), especially Definition 1.1, Corollary 2.4, Proposition 2.5 and Example 4.4. https://arxiv.org/abs/2609.27754
2. J. Qi and collaborators, *Skew geometric constants related to Birkhoff orthogonality in Banach spaces*, arXiv:2602.13974 (2026). https://arxiv.org/abs/2602.13974
3. Y. Fu and Y. Li, *Geometric constant for quantifying the difference between angular and skew angular distances in Banach spaces* (2024), referenced in [1] for the unrestricted constant.
