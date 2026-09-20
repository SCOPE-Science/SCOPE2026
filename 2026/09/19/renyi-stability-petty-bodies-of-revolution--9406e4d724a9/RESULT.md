# Rényi-divergence stability for Petty's quotient on bodies of revolution

## Result

Let \(n\ge 3\), write \(p=n-1\), and let
\[
Q(K)=\frac{V_n(\Pi K)}{V_n(K)^p}
\]
be Petty's projection-volume quotient. Mielke-Sulz recently proved that among convex bodies of revolution in \(\mathbb R^n\),
\[
Q(K)\ge Q(B^n)=\frac{\kappa_{n-1}^{\,n}}{\kappa_n^{\,n-2}},
\]
with equality exactly for ellipsoids.

The proof contains substantially more quantitative information. It yields a two-channel deficit decomposition: one term measures the volume gain under Blaschke symmetrization, while a second term is a Rényi divergence of the transformed meridional profile.

### Profile transform

Let
\[
K^{\mathrm B}=2^{-1/p}(K\#(-K))
\]
be the normalized Blaschke symmetral, with the centrally symmetric representative chosen. Then
\[
\Pi K^{\mathrm B}=\Pi K,
\qquad
V_n(K^{\mathrm B})\ge V_n(K).
\]
Set
\[
\mathcal A(K)=\frac{V_n(K^{\mathrm B})}{V_n(K)}\ge 1.
\]
After a rotation and a scaling in the directions perpendicular to the revolution axis, normalize
\[
\operatorname{proj}_{e_n^\perp}K^{\mathrm B}=B^{n-1}.
\]
Write the normalized body as
\[
K^{\mathrm B}=\{(x,z):x\in B^{n-1},\ |z|\le f(|x|)\},
\]
where \(f\) is concave and nonincreasing, and let \(\rho\) be the profile measure of Mielke-Sulz. If \(\rho_0\) denotes the profile measure of \(B^n\), its transform is
\[
A_\rho(t)=\frac{2\kappa_{n-2}}{p\,t^p}
\int_{[(1-t^2)^{p/2},1]}
\frac{(y^{2/p}-1+t^2)^{(p-1)/2}}{y}\,d\rho(y),
\qquad 0<t<1.
\]
For the ball,
\[
A_{\rho_0}(t)=\kappa_{n-1}
\]
is constant. Define the probability measure
\[
d\mu_n(t)=\frac{1}{Z_n}\frac{t^n}{\sqrt{1-t^2}}\,dt,
\qquad
Z_n=\int_0^1\frac{t^n}{\sqrt{1-t^2}}\,dt,
\]
and put
\[
X_K(t)=\frac{A_\rho(t)}{\kappa_{n-1}},
\qquad
m_K=\int X_K\,d\mu_n,
\qquad
Y_K=\frac{X_K}{m_K}.
\]
Then \(Y_K\ge0\) and \(\int Y_K\,d\mu_n=1\). Hence
\[
d\nu_K=Y_K\,d\mu_n
\]
is a probability measure on \((0,1)\).

### Theorem 1: two-channel Rényi deficit

For every convex body of revolution \(K\subset\mathbb R^n\),
\[
\boxed{
\log\frac{Q(K)}{Q(B^n)}
\ge
p\log \mathcal A(K)
+(p-1)D_p(\nu_K\Vert\mu_n)
}
\]
where
\[
D_p(\nu_K\Vert\mu_n)
=\frac{1}{p-1}\log\int Y_K^p\,d\mu_n
\]
is the order-\(p\) Rényi divergence.

More generally, monotonicity of Rényi divergence gives, for every \(1\le q\le p\),
\[
\boxed{
\log\frac{Q(K)}{Q(B^n)}
\ge
p\log \mathcal A(K)
+(p-1)D_q(\nu_K\Vert\mu_n).
}
\]
At \(q=1\), \(D_1\) is relative entropy.

Thus the Petty deficit controls two geometrically different failures of equality:

1. \(\mathcal A(K)>1\) detects the gain under Blaschke symmetrization and hence central asymmetry;
2. \(D_q(\nu_K\Vert\mu_n)>0\) detects nonconstant transformed profile of the symmetric part.

For an origin-symmetric body of revolution, \(\mathcal A(K)=1\), and the first term disappears.

### Corollary 2: explicit variance and total-variation stability

Since
\[
D_2(\nu_K\Vert\mu_n)
=\log\int Y_K^2\,d\mu_n
=\log\bigl(1+\operatorname{CV}_{\mu_n}(X_K)^2\bigr),
\]
where
\[
\operatorname{CV}_{\mu_n}(X_K)^2
=\frac{\operatorname{Var}_{\mu_n}(X_K)}{(\mathbb E_{\mu_n}X_K)^2},
\]
we obtain
\[
\boxed{
\frac{Q(K)}{Q(B^n)}
\ge
\mathcal A(K)^{n-1}
\bigl(1+\operatorname{CV}_{\mu_n}(X_K)^2\bigr)^{n-2}.
}
\]
Equivalently,
\[
\operatorname{CV}_{\mu_n}(X_K)^2
\le
\left(
\frac{Q(K)}{Q(B^n)\,\mathcal A(K)^{n-1}}
\right)^{1/(n-2)}-1.
\]

Pinsker's inequality gives another explicit consequence. With
\[
\operatorname{TV}(\nu_K,\mu_n)
=\frac12\int|Y_K-1|\,d\mu_n,
\]
we have
\[
\boxed{
\log\frac{Q(K)}{Q(B^n)}
\ge
(n-1)\log\mathcal A(K)
+2(n-2)\operatorname{TV}(\nu_K,\mu_n)^2.
}
\]
Hence if \(Q(K)\le(1+\varepsilon)Q(B^n)\), then
\[
\mathcal A(K)
\le(1+\varepsilon)^{1/(n-1)},
\]
and
\[
\operatorname{TV}(\nu_K,\mu_n)
\le
\sqrt{\frac{\log(1+\varepsilon)}{2(n-2)}}.
\]
For origin-symmetric bodies, the same near-equality assumption also gives
\[
\operatorname{CV}_{\mu_n}(X_K)^2
\le(1+\varepsilon)^{1/(n-2)}-1.
\]
Thus near equality forces the normalized profile transform to approach the ball transform quantitatively in both \(L^2\) and total variation.

### Theorem 3: the strongest divergence bound is exact on cylinders

Let
\[
C_h=B^{n-1}\times[-h,h],\qquad h>0.
\]
Its profile measure is
\[
\rho_{C_h}=p h\,\delta_1,
\]
so
\[
A_{\rho_{C_h}}(t)=\frac{2\kappa_{n-2}h}{t},
\qquad
X_{C_h}(t)=\frac{2\kappa_{n-2}h}{\kappa_{n-1}t}.
\]
For
\[
I_j=\int_0^1\frac{t^j}{\sqrt{1-t^2}}\,dt,
\]
one therefore has
\[
\int Y_{C_h}^p\,d\mu_n
=
\frac{I_1 I_n^{p-1}}{I_{n-1}^{p}}.
\]
On the other hand, the brightness of the cylinder is
\[
h_{\Pi C_h}(u)
=
\kappa_{n-1}|u_n|
+2h\kappa_{n-2}\sqrt{1-u_n^2},
\]
so
\[
\Pi C_h
=
(2h\kappa_{n-2})B^{n-1}
\times[-\kappa_{n-1},\kappa_{n-1}].
\]
A direct volume computation, followed by the beta-gamma identity for the \(I_j\), gives
\[
\boxed{
\frac{Q(C_h)}{Q(B^n)}
=
\int Y_{C_h}^p\,d\mu_n
=
\frac{I_1 I_n^{p-1}}{I_{n-1}^{p}}
=
\frac{2\kappa_{n-2}^{\,n-1}\kappa_n^{\,n-2}}
{\kappa_{n-1}^{\,2n-3}}.
}
\]
Thus the order-\((n-1)\) Rényi lower bound is not merely an infinitesimal refinement at ellipsoids: it is exact on every right circular cylinder as well.

For \(n=3\), this specializes to
\[
\frac{Q(C_h)}{Q(B^3)}
=\frac{32}{3\pi^2}
=1+\operatorname{CV}_{\mu_3}(X_{C_h})^2
\approx1.0807592922,
\]
so the variance bound itself is exact on cylinders in dimension three.

## Proof

Mielke-Sulz proves for every origin-symmetric normalized body of revolution that
\[
\frac{V_n(\Pi K)}{V_n(\Pi B^n)}
\ge
\frac{\mathfrak B(\rho_K,\ldots,\rho_K)}
{\mathfrak B(\rho_0,\ldots,\rho_0)},
\]
where
\[
\mathfrak B(\rho_1,\ldots,\rho_p)
=c_n\int_0^1\frac{t^n}{\sqrt{1-t^2}}
A_{\rho_1}(t)\cdots A_{\rho_p}(t)\,dt.
\]
Because \(A_{\rho_0}=\kappa_{n-1}\) is constant, the first ratio is exactly
\[
\int X_K^p\,d\mu_n.
\]
The same paper proves the mixed identity
\[
\frac{\mathfrak B(\rho_K,\rho_0,\ldots,\rho_0)}
{\mathfrak B(\rho_0,\ldots,\rho_0)}
=
\frac{\rho_K([0,1])}{\rho_0([0,1])}
=
\frac{V_n(K)}{V_n(B^n)}.
\]
The left side is \(\int X_K\,d\mu_n=m_K\). Consequently,
\[
\frac{Q(K)}{Q(B^n)}
\ge
\frac{\int X_K^p\,d\mu_n}
{(\int X_K\,d\mu_n)^p}
=
\int Y_K^p\,d\mu_n
=
\exp\bigl((p-1)D_p(\nu_K\Vert\mu_n)\bigr)
\]
for every origin-symmetric body of revolution.

For a general body of revolution, \(\Pi K^{\mathrm B}=\Pi K\), hence exactly
\[
Q(K)
=
\left(\frac{V_n(K^{\mathrm B})}{V_n(K)}\right)^p
Q(K^{\mathrm B})
=
\mathcal A(K)^p Q(K^{\mathrm B}).
\]
Applying the preceding inequality to \(K^{\mathrm B}\) gives Theorem 1.

Monotonicity \(D_p\ge D_q\) for \(1\le q\le p\) gives the Rényi hierarchy. The \(q=2\) formula follows from \(\int Y_K\,d\mu_n=1\), and the total-variation estimate follows from Pinsker's inequality
\[
D_1(\nu_K\Vert\mu_n)\ge2\operatorname{TV}(\nu_K,\mu_n)^2.
\]
The cylinder identities are direct substitutions into the profile transform and the projection-body definition.

## Equality information and stability meaning

The transform \(\rho\mapsto A_\rho\) is injective on the profile measures considered by Mielke-Sulz. Hence
\[
D_q(\nu_K\Vert\mu_n)=0
\]
for the normalized origin-symmetric profile if and only if \(A_\rho\) is constant, equivalently \(\rho=c\rho_0\), which gives an ellipsoid of revolution. Likewise, equality \(\mathcal A(K)=1\) in the Kneser-Süss step means that \(K\) is centrally symmetric up to translation.

Therefore the two terms in Theorem 1 vanish simultaneously exactly on ellipsoids, although the quantitative lower bound can also be attained away from equality in Petty's inequality, as the cylinder computation shows.

For a sequence of origin-symmetric normalized bodies of revolution with \(Q(K_j)/Q(B^n)\to1\), the theorem implies \(Y_{K_j}\to1\) in \(L^2(\mu_n)\) and in total variation. Since the profile measures have fixed mass after an axial normalization, weak-* compactness together with continuity and injectivity of the transform then forces the normalized profile measures to converge weak-* to \(\rho_0\). This is a qualitative profile-measure compactness consequence; no quantitative inverse-transform modulus is asserted.

## Context and originality boundary

The qualitative Petty conjecture for bodies of revolution, the profile measure \(\rho_K\), the transform \(A_\rho\), its injectivity, and the multilinear estimate above are all due to Mielke-Sulz. The new content here is the quantitative reorganization of those ingredients into:

- an explicit two-channel logarithmic deficit separating Blaschke asymmetry from symmetrized profile shape;
- a full Rényi-divergence hierarchy;
- coefficient-of-variation and total-variation stability bounds with explicit constants;
- the observation that the strongest divergence refinement is exactly attained by the entire family of right circular cylinders.

The current v1 of Mielke-Sulz's paper contains no statements indexed by the terms stability, deficit, variance, quantitative, entropy, or Rényi. Targeted searches for Petty's conjecture together with these terms located no equivalent quantitative formulation. Earlier work of Saroglou gives lower bounds for the same quotient and an almost optimal high-dimensional bound for bodies of revolution, but not this profile-transform deficit. Literature using the established phrase “Petty projection inequality” often concerns the different polar projection-body inequality and is not coverage of the present conjectural quotient.

A public note by Felix Dorrek reports an independent proof of the qualitative bodies-of-revolution case but does not provide a mathematical quantitative refinement of the form above; unpublished overlap therefore remains a residual originality risk.

## Limitations

The stability distance here lives in the one-dimensional transformed profile space. It is not a Hausdorff, Banach-Mazur, symmetric-difference, or Wasserstein distance between convex bodies. The transform is injective, but no quantitative stability estimate for its inverse is proved here.

For a non-centrally-symmetric body, the Rényi term measures the Blaschke symmetral rather than the original meridional asymmetry; the separate factor \(\mathcal A(K)\) records only the volume gain under Blaschke symmetrization. No quantitative geometric conversion of \(\mathcal A(K)-1\) to a standard asymmetry distance is claimed.

The theorem is restricted to convex bodies of revolution and relies on the profile-transform machinery of the recent proof. It does not resolve Petty's conjecture for arbitrary convex bodies.

## References

1. F. Mielke-Sulz, *The Petty Conjecture for Convex Bodies of Revolution*, arXiv:2609.13517, submitted 11 September 2026. https://arxiv.org/abs/2609.13517
2. C. Saroglou, *On the shape of a convex body with respect to its second projection body*, Adv. Appl. Math. 73 (2016), 1–12; arXiv:1409.4347. https://arxiv.org/abs/1409.4347
3. F. Dorrek, *Proving a math conjecture with AI, and the shape of machine intelligence*, public note, August 2026. https://felixdorrek.com/writing/petty-conjecture
