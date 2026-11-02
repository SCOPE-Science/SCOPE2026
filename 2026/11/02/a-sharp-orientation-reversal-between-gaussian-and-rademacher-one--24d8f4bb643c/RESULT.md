# A sharp orientation reversal between Gaussian and Rademacher one-probe range finders

## Finding

Let \(A\in\mathbb R^{m\times 2}\), \(m\ge2\), have full column rank and singular values \(\sigma_1\ge\sigma_2>0\). Draw one nonzero test vector \(\omega\in\mathbb R^2\), form \(y=A\omega\), and approximate \(A\) by the orthogonal range projection \(\widehat A=yy^\top A/(y^\top y)\). The reported error quantity here is the **squared** Frobenius residual \(\mathcal E(\omega)=\|A-\widehat A\|_F^2\), not the unsquared norm or an error in estimated singular values.

For a standard real Gaussian test vector, \(\omega\sim N(0,I_2)\),
\[
\mathbb E_G\mathcal E=\sigma_1\sigma_2.
\]
For independent Rademacher coordinates, \(\omega_j\in\{-1,1\}\) equiprobably, write \(B=A^\top A\), \(s=\operatorname{tr}(B)/2\), \(b=B_{12}\), and \(D=\det B\). Then
\[
\mathbb E_R\mathcal E=\frac{Ds}{s^2-b^2},\qquad
\frac{2\sigma_1^2\sigma_2^2}{\sigma_1^2+\sigma_2^2}
\le\mathbb E_R\mathcal E\le\frac{\sigma_1^2+\sigma_2^2}{2}.
\]
Both bounds are attained for any prescribed singular values. If \(\sigma_1>\sigma_2\), the lower bound is attained exactly when the coordinate basis is a right-singular basis (\(b=0\)); the upper bound is attained exactly when the two diagonal entries of \(B\) are equal, equivalently when the right-singular axes make angles of \(45\) degrees with the coordinate axes. If \(\sigma_1=\sigma_2\), the two probe laws always have the same deterministic squared error.

For \(\sigma_1>\sigma_2\), Rademacher is strictly better than Gaussian in expected squared Frobenius residual precisely if
\[
|b|<\sqrt{s(s-\sigma_1\sigma_2)};
\]
it is strictly worse precisely for the reversed inequality, with equality at the threshold. If \(\theta\) is the right-singular rotation angle, so that \(|b|=(\sigma_1^2-\sigma_2^2)|\sin(2\theta)|/2\), then the crossing is
\[
|\sin(2\theta)|=
\frac{\sqrt{\sigma_1^2+\sigma_2^2}}{\sigma_1+\sigma_2}.
\]
Under a uniformly random right-singular orientation (modulo the symmetries of the two axes), the fraction of orientations for which Rademacher is worse is exactly
\[
\frac{2}{\pi}\arccos\!\left(
\frac{\sqrt{\kappa^2+1}}{\kappa+1}\right),
\qquad\kappa=\sigma_1/\sigma_2>1.
\]
This fraction is asymptotic to \(2\sqrt2/(\pi\sqrt\kappa)\) as \(\kappa\to\infty\). Averaging the Rademacher error over the orientation exactly recovers the Gaussian error.

The best- and worst-orientation Rademacher error relative to the optimal squared rank-one error \(\sigma_2^2\) are, respectively, \(2\kappa^2/(\kappa^2+1)\) and \((\kappa^2+1)/2\); the Gaussian ratio is \(\kappa\). Thus a sign probe can stay within a factor two of optimal at one orientation yet lose a factor of order \(\kappa^2\) at another, despite an unchanged singular spectrum.

## Assumptions and scope

All matrices are real. Only one test vector is drawn, with no oversampling or power iterations, and arithmetic is exact. The column dimension is exactly two; the number of rows can be arbitrary \(m\ge2\). The rank-two assumption excludes zero sketches and guarantees every projector is defined. The Rademacher coordinates are independent in the *given coordinate basis*; their law is not orthogonally invariant. When \(\sigma_1=\sigma_2\), orientation effects disappear and all formulas extend continuously.

The same distributional example can be embedded in arbitrarily many columns as \([A\ \ 0]\); this is an embedding observation, not a claim for arbitrary rank-two right singular subspaces in higher column dimension.

## Proof

**1. A samplewise residual identity.** Put \(B=A^\top A\succ0\) and \(P=yy^\top/(y^\top y)\), with \(y=A\omega\). Cyclicity of trace gives
\[
\mathcal E(\omega)=\operatorname{tr}B-
\frac{\omega^\top B^2\omega}{\omega^\top B\omega}.
\]
The Cayley–Hamilton identity for a two-by-two matrix, \(B^2-(\operatorname{tr}B)B+(\det B)I_2=0\), therefore yields
\[
\mathcal E(\omega)=D\frac{\|\omega\|_2^2}{\omega^\top B\omega}.
\tag{1}
\]
This formula is valid for every nonzero real \(\omega\), regardless of the probe distribution.

**2. Gaussian integral.** A standard Gaussian's direction is uniform on the real unit circle and independent of its length. Diagonalize \(B\) with eigenvalues \(\lambda=\sigma_1^2\) and \(\mu=\sigma_2^2\). Equation (1) gives
\[
\mathbb E_G\mathcal E=\frac{D}{2\pi}\int_0^{2\pi}
\frac{d\phi}{\lambda\cos^2\phi+\mu\sin^2\phi}.
\]
Using four equal quadrants and \(t=\tan\phi\), the integral is \(4\int_0^\infty dt/(\lambda+\mu t^2)=2\pi/\sqrt{\lambda\mu}\). Hence the expectation is \(D/\sqrt{\lambda\mu}=\sigma_1\sigma_2\).

**3. Exact Rademacher formula and sharp extrema.** The four sign vectors yield only two projective directions, \((1,1)^\top\) and \((1,-1)^\top\), each with probability \(1/2\). Their Rayleigh quotients per unit squared length are \(s+b\) and \(s-b\). Equation (1) gives
\[
\mathbb E_R\mathcal E=\frac D2\left(\frac1{s+b}+\frac1{s-b}\right)
=\frac{Ds}{s^2-b^2}.
\tag{2}
\]
Writing \(d=(\lambda-\mu)/2\), the possible Gram matrices with these eigenvalues have \(|b|\le d\), with \(s^2-d^2=D\). The expression in (2) increases strictly with \(|b|\) for distinct eigenvalues. Its values at \(|b|=0\) and \(|b|=d\) are \(D/s\) and \(s\). Matrices with these equality configurations exist: take \(B=\operatorname{diag}(\lambda,\mu)\) or \(B=\left(\begin{smallmatrix}s&d\\d&s\end{smallmatrix}\right)\). Every such positive-definite Gram matrix equals \(A^\top A\) for some real \(A\) with \(m\ge2\). If \(\lambda=\mu\), then \(b=0\) necessarily.

**4. Crossing, orientation measure, and average.** Compare (2) with \(\sqrt D\). Multiplication by the positive denominator shows \(\mathbb E_R\mathcal E<\sqrt D\) exactly when \(b^2<s(s-\sqrt D)\). An orthogonal right-singular rotation gives \(|b|=d|\sin(2\theta)|\), and
\[
\frac{s(s-\sqrt D)}{d^2}=
\frac{s}{s+\sqrt D}=
\frac{\sigma_1^2+\sigma_2^2}{(\sigma_1+\sigma_2)^2}.
\]
For \(\theta\) uniform on \([0,\pi/2)\), \(2\theta\) is uniform on \([0,\pi)\). The measure of angles with \(\sin(2\theta)\) above this positive threshold proves the stated arccosine fraction. The asymptotic follows from \(1-\sqrt{\kappa^2+1}/(\kappa+1)\sim1/\kappa\) and \(\arccos(1-\varepsilon)\sim\sqrt{2\varepsilon}\). Finally, randomizing a Rademacher probe by an independent uniform rotation makes its direction uniform on the circle. Applying step 2 to this mixed experiment proves that the orientation-average of (2) equals \(\sigma_1\sigma_2\). The ratios to the optimal error follow by division by \(\sigma_2^2\).

## Verification

The included standalone Python script `verify_rank_one.py` uses the standard library only. It verifies the residual via the expanded projected-Frobenius formula, separately from the Cayley–Hamilton shortcut, over 7,904 exact-rational algebraic checks. It also makes 1,123 deterministic numerical checks of the Gaussian angular integral, Rademacher extremizers, crossover, and orientation-average formulas. Its output is `VERIFY_OK exact=7904 numerical=1123`. Finite checks do not replace steps 1–4, which prove the result for all stated real matrices and parameters.

At \(\sigma_1=10\) and \(\sigma_2=1\), Gaussian probes have expected squared error \(10\). Rademacher probes have expected squared error \(200/101\) when \(B=\operatorname{diag}(100,1)\), but \(101/2\) when \(B=\left(\begin{smallmatrix}101/2&99/2\\99/2&101/2\end{smallmatrix}\right)\).

## Relationship to prior work

Randomized range finding and its projection-error viewpoint are classical [1]. A study of non-Gaussian low-rank approximation [2] includes Gaussian and Rademacher sketch distributions, but its high-probability bounds are formulated under sample-size conditions and do not state a one-column, fixed-spectrum, orientation-complete expected-error comparison. Related Gaussian range-approximation bounds in [3] assume an oversampled regime and do not provide this comparison. The present exact equalities do not supersede their large-dimensional guarantees.

The elementary two-dimensional matrix identity and angular integral used here are classical. The distinct contribution assessed here is their combination into an exact one-probe, two-distribution orientation classification, the sharp Gaussian crossover, and the fraction of adverse orientations. An equivalent earlier specialized derivation may exist; no independent priority determination is claimed.

## Limitations

The result is restricted to a rank-two column space and the first, unpowered, unoversampled range sketch. It does not give general high-dimensional sketch-quality guarantees, concentration inequalities, or numerical-rounding stability. A Rademacher vector rotated together with the singular vectors would have a different law; orientation dependence requires fixing the coordinate distribution. The stated average and orientation-probability claims concern uniform *external* right-singular rotation, not intrinsic randomness of a fixed input matrix.

## References

[1] N. Halko, P.-G. Martinsson, and J. A. Tropp, *Finding structure with randomness: Probabilistic algorithms for constructing approximate matrix decompositions*, arXiv:0909.4061, 2009; SIAM Review 53 (2011), 217–288. https://arxiv.org/html/0909.4061v2

[2] A. K. Saibaba and A. Międlar, *Randomized low-rank approximations beyond Gaussian random matrices*, arXiv:2308.05814, first public version 10 August 2023; SIAM Journal on Mathematics of Data Science 7 (2025), 136–162. https://arxiv.org/html/2308.05814v1

[3] Y. Diouane, S. Gürol, A. Scotto Di Perrotolo, and X. Vasseur, *A general error analysis for randomized low-rank approximation methods*, arXiv:2206.08793, first public version 17 June 2022. https://arxiv.org/abs/2206.08793
