# Exact global vacuum stability on the affine Bargmann–Fock subspace

## Finding

Write \(c=\sqrt{\pi}/2\). On the first two homogeneous levels of the Bargmann–Fock space, the squared phaseless distance from the vacuum has the following **sharp global remainder**, in every complex dimension \(d\ge1\):
\[
\big\|\,|F|-1\,\big\|_{L^2(\gamma_d)}^2\;\ge\;
(1-c)\min_{|\lambda|=1}\|F-\lambda\|_{L^2(\gamma_d)}^2
+c\big(\|F\|_{L^2(\gamma_d)}-1\big)^2.
\]
For an affine holomorphic function \(F(z)=a+\sum_{j=1}^d b_jz_j\), equality in the remainder holds **if and only if** \(a=0\) or \(b_1=\cdots=b_d=0\), including the zero function. In particular, the sharp smallest constant in
\[
\min_{|\lambda|=1}\|F-\lambda\|_{L^2(\gamma_d)}
\le C_{\mathrm{aff}}\big\|\,|F|-1\,\big\|_{L^2(\gamma_d)}
\]
for *all* affine \(F\), without any smallness hypothesis, is
\[
C_{\mathrm{aff}}=\left(1-\frac{\sqrt\pi}{2}\right)^{-1/2}
=2.9646965828533536\ldots.
\]
Equality with positive distances is realized by every normalized pure linear function \(F(z)=\sum_jb_jz_j\) with \(\sum_j|b_j|^2=1\). The constant is independent of dimension.

## Assumptions and scope

For each integer \(d\ge1\), the normalized measure on \(\mathbb C^d\) is
\[
d\gamma_d(z)=\pi^{-d}\exp(-\textstyle\sum_{j=1}^d|z_j|^2)\prod_{j=1}^d dA(z_j),
\]
where \(dA\) is two-dimensional Lebesgue measure. The affine holomorphic subspace \(\mathcal A_d\) consists of all \(F(z)=a+\sum_{j=1}^d b_j z_j\) with \(a,b_j\in\mathbb C\). Its norm is \(\|F\|_2^2=|a|^2+\sum_j|b_j|^2\). The reference function \(1\) has unit norm. The observation map is \(F\mapsto|F|\), not \(F\mapsto |F|^2\); its observation distance uses the **full Gaussian measure**, not discrete samples, a bounded observation window, or derivative-weighted norms. We assert no sharp constant for the unrestricted infinite-dimensional Fock space or for pairs of two arbitrary non-vacuum signals.

## Proof

**1. A sharp modulus bound for a displaced circular Gaussian.** Let \(Z\) be a standard circular complex Gaussian with law \(\pi^{-1}e^{-|z|^2}dA(z)\). For every \(a,s\ge0\), put \(m(a,s)=\mathbb E|a+sZ|\). We prove
\[
m(a,s)^2\le a^2+\frac\pi4s^2,
\]
with equality precisely if \(a=0\) or \(s=0\).

The cases \(s=0\) and \(a=0\) follow from \(m(a,0)=a\), \(\mathbb E|Z|=\sqrt\pi/2\), and \(\mathbb E|Z|^2=1\). Fix \(s>0\). Write \(a+sZ=R e^{i\Theta}\), where \(R>0\) almost surely and \(a\) is on the positive real axis. Gaussian integrability allows differentiating under the expectation, so
\[
\frac{\partial m}{\partial a}=\mathbb E\cos\Theta,
\qquad \mathbb ER^2=a^2+s^2.
\]
It follows that
\[
\frac{\partial}{\partial a}\operatorname{Var}(R)
=2\big(\mathbb E[R\cos\Theta]-\mathbb ER\,\mathbb E[\cos\Theta]\big)
=2\operatorname{Cov}(R,\cos\Theta).
\]
Conditional on \(R=r>0\), the angle \(\Theta\) has a von Mises density proportional to \(\exp(2ar\cos\theta/s^2)\). Thus for
\(h_a(r)=\mathbb E(\cos\Theta\mid R=r)\), differentiation of the bounded angular integral gives
\[
h'_a(r)=\frac{2a}{s^2}\operatorname{Var}(\cos\Theta\mid R=r)\ge0.
\]
The inequality is strict at \(a>0\), because this conditional angular law is nondegenerate. Hence
\(\operatorname{Cov}(R,\cos\Theta)=\operatorname{Cov}(R,h_a(R))\ge0\), strictly if \(a>0\). For completeness, any increasing \(h\) obeys
\[
2\operatorname{Cov}(R,h(R))
=\mathbb E[(R-R')(h(R)-h(R'))]\ge0,
\]
with an independent copy \(R'\). Consequently the Rice modulus variance \(\operatorname{Var}|a+sZ|\) is strictly increasing as the displacement \(a\) increases from zero. At zero displacement it equals \(s^2(1-\pi/4)\). Since \(\operatorname{Var}R=a^2+s^2-m(a,s)^2\), the claimed bound and its equality cases follow.

**2. Rotation reduction.** Put \(s=(\sum_j|b_j|^2)^{1/2}\), \(A=|a|\), and \(r=(A^2+s^2)^{1/2}=\|F\|_2\). The complex Gaussian linear combination \(\sum_jb_jZ_j\) has the same law as \(sZ\), and rotation removes the phase of \(a\). Therefore, by Step 1,
\[
\int_{\mathbb C^d}|F|\,d\gamma_d
\le\sqrt{A^2+c^2s^2}\le cr+(1-c)A.
\]
The second inequality follows upon squaring its nonnegative sides: the difference between the right square and the left square is \(2c(1-c)A(r-A)\). It is an equality precisely when \(A=0\) or \(s=0\). Thus the composite inequality is strict if both \(A\) and \(s\) are positive.

**3. The sharp remainder.** Orthogonality of constants and linear monomials yields
\[
\min_{|\lambda|=1}\|F-\lambda\|_2^2=r^2+1-2A,
\qquad
\big\|\,|F|-1\,\big\|_2^2=r^2+1-2\int|F|\,d\gamma_d.
\]
Using \(\int|F|\,d\gamma_d\le cr+(1-c)A\) and rearranging proves the displayed remainder. Both its equality cases and the exclusion of all mixed nonzero cases follow from Step 2.

Since the additional term \(c(r-1)^2\) is nonnegative, the remainder implies the claimed Lipschitz bound. To see it is best possible, choose \(F(z)=z_1\). Its norm is one, its phase-orbit distance squared from \(1\) is \(2\), and its modulus distance squared is \(2-\sqrt\pi=2(1-c)\). Thus equality holds at the specified constant, and no smaller constant works in any dimension. The argument also proves the exact classification of equality in the stronger remainder.

## Verification

A standalone numerical supplement, `verify_affine.py`, evaluates the Rician mean using **exponentially scaled** modified Bessel functions \(I_0\) and \(I_1\), so large displacement does not cause the usual exponential overflow. It tests 64 noncentrality/variance parameter pairs including both equality boundaries, strict mixed cases, all inequalities in Steps 1–3, and the exact first-Hermite ratio. These tests passed. The proof is analytic, applies to unbounded parameters and all dimensions, and does not depend on the finite numerical grid. The computation requires Python 3 and SciPy.

## Relationship to prior work

Bertolini, de Dios Pont, Pineau, Ramos, and Taylor (2026) establish the existence of \(L^2\) phase-retrieval stability at the Gaussian vacuum in the full Bargmann–Fock space and formulate higher-dimensional extensions, without determining the sharp constant on the affine subspace; their explicit estimates are not optimized. Bortolotto and Ramos (2026) prove a square-restricted coercivity inequality in the full one-dimensional Fock space, involving squared amplitudes and no corresponding sharp affine constant. General Cheeger-based phase-retrieval bounds address broader observation geometries without identifying this two-level exact modulus constant. The present contribution is the **exact**, **dimension-free**, **global** affine-subspace constant together with a sharp radial remainder and equality rigidity; the Gaussian law, Rice distribution, and existing qualitative Fock stability are standard prerequisites rather than claimed discoveries.

## Limitations

The observation must be over the entire normalized Gaussian space; finite Gabor samples, truncated regions, other reference signals, higher Hermite degrees, and the full unrestricted Fock space require separate analysis. The variance monotonicity property is a known type of property of the Rician family; its use here does not imply priority for that underlying probabilistic phenomenon. No independent external audit is represented, and historical-priority risk remains for an unindexed exact two-level phase-retrieval inequality.

## References

1. S. Bertolini, J. de Dios Pont, B. Pineau, J. P. G. Ramos, and M. A. Taylor, *L²-Stability for STFT phase retrieval*, arXiv:2605.20527v1, 19 May 2026. https://arxiv.org/abs/2605.20527
2. C. Bortolotto and J. P. G. Ramos, *A complex-analytic proof of square-restricted stable phase retrieval in Fock space*, arXiv:2608.26365v1, 26 August 2026. https://arxiv.org/abs/2608.26365
3. H. Führ and M. Getter, *Cheeger Bounds for Stable Phase Retrieval in Reproducing Kernel Hilbert Spaces*, arXiv:2512.24169, 30 December 2025. https://arxiv.org/abs/2512.24169
