# Global symplectic balancing of transverse Lagrangian ellipsoid sums

## Finding

Let \(n\ge 2\), let \(J=\left(\begin{smallmatrix}0&I_n\\-I_n&0\end{smallmatrix}\right)\), and let \(F,G\in\mathbb R^{2n\times n}\) satisfy \(F^\mathsf TJF=G^\mathsf TJG=0\) and \(\det(F^\mathsf TJG)\ne0\). Write \(B_2^n\) for the Euclidean unit ball, and define the full-dimensional, centrally symmetric convex body
\[
 K=FB_2^n+GB_2^n\subset\mathbb R^{2n}.
\]
Let \(\sigma_1,\ldots,\sigma_n>0\) be the singular values of \(H=F^\mathsf TJG\), let \(Z\) have the standard \(n\)-dimensional Gaussian law, and set
\[
 \gamma_d=\mathbb E\|Z_d\|=\sqrt2\,\Gamma((d+1)/2)/\Gamma(d/2).
\]
For \(M(L)=\int_{S^{2n-1}}(h_L(u)+h_L(-u))\,d\omega(u)\), with \(\omega\) probability spherical measure, the exact global optimum over **linear** symplectic maps is
\[
 \boxed{\min_{S\in\operatorname{Sp}(2n,\mathbb R)}M(SK)
 =\frac4{\gamma_{2n}}\mathbb E\sqrt{\sum_{i=1}^n\sigma_iZ_i^2}.}
\]
This minimum is attained. After independent orthogonal changes of the ball coordinates of \(F\) and \(G\), every minimizing pair of images is, for some orthogonal symplectic map \(U\in\operatorname{Sp}(2n,\mathbb R)\cap O(2n)\),
\[
 (SF,SG)=U\left(\begin{bmatrix}\Sigma^{1/2}\\0\end{bmatrix},
                       \begin{bmatrix}0\\\Sigma^{1/2}\end{bmatrix}\right),
 \qquad\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_n).
\]
Consequently every minimizing body is a unitary image of the Cartesian product of two identical, generally anisotropic, ellipsoids with semiaxes \(\sqrt{\sigma_i}\). Conversely every displayed pair is realized by a linear symplectic map and is minimizing.

At fixed \(\tau=\sum_i\sigma_i\), the optimal value has the sharp spectral envelope
\[
 \frac{4\sqrt{2\tau/\pi}}{\gamma_{2n}}
 <\min_{S}M(SK)
 \le \frac{4\gamma_n\sqrt{\tau/n}}{\gamma_{2n}},
\]
where the upper equality holds exactly when all singular values coincide, and the lower constant is the unattained infimum approached as all but one singular value tend to zero. In dimension four (\(n=2\)), for \(\sigma_1\ge\sigma_2>0\), the optimum is
\[
 \frac{16\sqrt{\sigma_1}}{3\pi}
 \int_0^{\pi/2}\sqrt{1-(1-\sigma_2/\sigma_1)\sin^2 t}\,dt.
\]

## Assumptions and scope

Both summands are images of full-dimensional Euclidean balls under injective maps to transverse Lagrangian \(n\)-planes. The nonsingularity of \(H\) is precisely transversality of those two Lagrangian planes. Only the action of the **linear** symplectic group is optimized. The statement neither optimizes arbitrary nonlinear symplectomorphisms nor asserts an analogous result for arbitrary convex factors.

## Proof

**Normalize the cross-pairing.** Multiplying \(F\) and \(G\) on the right by independent orthogonal matrices leaves \(K\) unchanged. A singular-value decomposition therefore allows \(F^\mathsf TJG=\Sigma\), positive diagonal. The block matrix \(W=[F\ G]\) is invertible: otherwise a nonzero vector in the span of one Lagrangian frame lies in the other's span, contradicting nonsingularity of the cross-pairing. With the indicated \(J\),
\[
 W^\mathsf TJW=\begin{bmatrix}0&\Sigma\\-\Sigma&0\end{bmatrix}.
\]

**Gaussian representation.** Let \(S\) be any symplectic linear map and write \(E=SF\) and \(D=SG\). Since the support function of the Minkowski sum is additive,
\[
 h_{SK}(x)=\|E^\mathsf Tx\|+\|D^\mathsf Tx\|.
\]
For a standard Gaussian \(X\in\mathbb R^{2n}\) and independent standard Gaussian \(z\in\mathbb R^n\), the random vectors \(E^\mathsf TX\) and \(E z\) have the same respective norm distributions: both are governed by the nonzero singular values of \(E\). The same holds for \(D\). Gaussian polar decomposition gives
\[
 M(SK)=\frac2{\gamma_{2n}}\mathbb E_z
   \bigl(\|Ez\|+\|Dz\|\bigr).
\]
This is a sum of marginal expectations, so using the *same* \(z\) in the two summands is legitimate; no claim about joint Gaussian distributions is required.

**Pointwise lower bound.** Symplecticity and the Lagrangian hypotheses give
\[
 (Ez)^\mathsf TJ(Dz)=z^\mathsf T\Sigma z\ge0.
\]
Because \(J\) is orthogonal, ordinary Cauchy–Schwarz followed by arithmetic–geometric mean yields, for every \(z\),
\[
 \|Ez\|+\|Dz\|\ge2\sqrt{\|Ez\|\|Dz\|}
 \ge2\sqrt{(Ez)^\mathsf TJ(Dz)}
 =2\sqrt{z^\mathsf T\Sigma z}.
\]
Integrating proves the proposed universal inequality.

**Attainment.** Set \(E_0=(\Sigma^{1/2},0)^\mathsf T\), \(D_0=(0,\Sigma^{1/2})^\mathsf T\), and \(W_0=[E_0\ D_0]\). Then \(W_0^\mathsf TJW_0=W^\mathsf TJW\); hence \(S_0=W_0W^{-1}\) satisfies \(S_0^\mathsf TJS_0=J\). The two images have equal norm \(\sqrt{z^\mathsf T\Sigma z}\) for each \(z\), and the Cauchy–Schwarz step is an equality, attaining the bound.

**Equality rigidity.** Equality of the integrated nonnegative pointwise gap implies equality for almost every \(z\), hence for every \(z\) by continuity. Equality of arithmetic–geometric mean gives \(\|Ez\|=\|Dz\|\), while positive equality in Cauchy–Schwarz gives \(Ez=J(Dz)\). By linearity \(D=-JE\), and therefore
\[
 \Sigma=E^\mathsf TJD=E^\mathsf TE.
\]
Thus \(E\Sigma^{-1/2}\) is an orthonormal Lagrangian frame. The orthogonal symplectic group acts transitively on these frames, proving the complete unitary-orbit description and the converse.

**Sharp trace envelope.** The map \(\sigma\mapsto\mathbb E\sqrt{\sum_i\sigma_iZ_i^2}\) is symmetric and strictly concave on positive spectra (the Gaussian vector has nonzero and unequal squared coordinates with positive probability). Averaging over coordinate permutations proves the unique equal-spectrum maximum. Every nonnegative spectrum of trace \(\tau\) is a convex combination of the extreme points \(\tau e_i\); concavity gives the lower value \(\mathbb E\sqrt\tau|Z_1|=\sqrt{2\tau/\pi}\). Strictness makes the lower inequality strict for positive spectra; rank-one limits establish sharpness. For \(n=2\), write the planar Gaussian in polar coordinates; its mean radius is \(\gamma_2\), its angle is uniform, and \(\gamma_2/\gamma_4=2/3\), producing the stated elliptic integral.

## Verification

The standalone `check.py` uses only exact rational arithmetic. It constructs transverse Lagrangian frames and an explicit balancing symplectic transformation in dimensions \(2,4,6,8\), verifies pairing and symplectic Gram identities, and checks the pointwise bound for all \(776\) nonzero vectors in small integer grids. All checks passed. The finite tests illustrate the algebra; the universal proof above uses Cauchy–Schwarz and an exact symplectic normal form, not enumeration. Run `python3 check.py`.

## Relationship to prior work

Ahn and Kerman, *On the symplectic capacity and mean width of convex bodies* (arXiv:2602.07220, submitted 2026-02-06), investigate local linear-symplectic mean-width minima for quadratic and ball-product convex bodies, and distinguish linear optimization from nonlinear symplectomorphisms. Their local analysis does not furnish this global singular-value formula and rigidity theorem. In *Optimal symplectic positions for the mean width* (arXiv:2311.02870, submitted 2023-11-06), they establish a global result for the four-dimensional Lagrangian bidisk (among other results for toric bodies and ellipsoids). The isotropic four-dimensional bidisk is a known special case of the formula here and is expressly not claimed as new. The new statement concerns arbitrary transverse Lagrangian ellipsoid summands in all even dimensions, with anisotropic symplectic-pairing spectra and a complete orbit classification. This is not the single-ellipsoid or toric-body theorem.

## Limitations

The possible historical existence of an equivalent result under symplectic frame normalization or Gaussian matrix norms remains a priority risk, despite targeted comparisons. Equality is classified for parametrized pairs after independent orthogonal changes of their ball coordinates; coincident minimizing bodies can admit additional parameter descriptions. The theorem is strictly about linear symplectic maps, not the nonlinear optimization studied elsewhere. The finite rational checker is corroborative; it is not an independent scientific review or an infinite certification.

## References

1. J. Ahn and E. Kerman, *On the symplectic capacity and mean width of convex bodies*, arXiv:2602.07220 (first posted 2026-02-06), https://arxiv.org/abs/2602.07220.
2. J. Ahn and E. Kerman, *Optimal symplectic positions for the mean width*, arXiv:2311.02870 (first posted 2023-11-06), https://arxiv.org/abs/2311.02870.
