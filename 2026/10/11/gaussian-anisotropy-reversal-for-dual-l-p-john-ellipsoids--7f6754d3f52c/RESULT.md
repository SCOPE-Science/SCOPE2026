# Gaussian anisotropy reversal for dual \(L_p\) John ellipsoids

## Finding

Let \(n\ge 2\), \(p>0\), and \(R>0\). Suppose that \(\mu\) has a radial density
\[
g(x)=\phi(|x|),
\]
where \(\phi\) is positive and \(C^1\) on a neighborhood of \(R\). Let \(A\) be any real symmetric traceless \(n\times n\) matrix and define the volume-preserving ellipsoidal deformation
\[
K_\varepsilon=R\exp(\varepsilon A)B_2^n.
\]
Let
\[
E_\varepsilon=\widetilde E_{\mu,p}K_\varepsilon
\]
be the unique dual \(L_p\) John ellipsoid for general measures defined by Li--Liu--Huang. Write
\[
E_\varepsilon=T_\varepsilon B_2^n
\]
with \(T_\varepsilon\) positive definite. Then
\[
\boxed{
T_\varepsilon
=
R\left(I+\varepsilon c_R A+o(\varepsilon)\right)
}
\]
in operator norm, where
\[
\boxed{
c_R
=
1+\frac{R\phi'(R)}{(n+p)\phi(R)}.
}
\]

For the standard Gaussian density
\[
\phi(r)=(2\pi)^{-n/2}e^{-r^2/2},
\]
this becomes
\[
\boxed{
c_R=1-\frac{R^2}{n+p}.
}
\]
Hence the first anisotropic response has an exact transition at
\[
\boxed{
R_c=\sqrt{n+p}.
}
\]
For \(R<R_c\) the output ellipsoid follows the input degree-two anisotropy, at \(R=R_c\) its first anisotropic variation vanishes, and for \(R>R_c\) it reverses sign.

## Assumptions and scope

The parameter satisfies \(p>0\), the ambient dimension satisfies \(n\ge2\), and only origin-centered ellipsoidal perturbations are considered. The matrix \(A\) is symmetric and traceless, so
\[
\det\exp(\varepsilon A)=1
\]
and the input deformation preserves Euclidean volume exactly.

The density is radial and positive near the reference sphere. Only one radial derivative,
\[
\eta_R=\frac{R\phi'(R)}{\phi(R)},
\]
enters the response coefficient. No homogeneity assumption on \(\mu\) is made.

The theorem concerns the first derivative at \(\varepsilon=0\). In particular, at \(R=\sqrt{n+p}\) for the Gaussian measure it proves only
\[
T_\varepsilon=RI+o(\varepsilon);
\]
it does not determine the second nonzero anisotropic term.

## Proof

At \(\varepsilon=0\), rotational invariance of both \(\mu\) and \(K_0=RB_2^n\), together with uniqueness of the optimizing ellipsoid, forces
\[
E_0=RB_2^n.
\]
Indeed any rotationally invariant origin-symmetric ellipsoid is a Euclidean ball, and the normalized constraint in the defining optimization problem gives the radius \(R\).

Put
\[
q_A(u)=u^{\mathsf T}Au
\]
for \(u\in S^{n-1}\). Since \(A\) is traceless,
\[
\int_{S^{n-1}}q_A(u)\,d\sigma(u)=0.
\]
The radial function of the input ellipsoid has the first-order expansion
\[
\rho_{K_\varepsilon}(u)
=
R\left(1+\varepsilon q_A(u)\right)+O(\varepsilon^2).
\]

Write a nearby output ellipsoid as
\[
T_\varepsilon
=
R\left(I+\varepsilon B+o(\varepsilon)\right)
\]
with \(B\) symmetric, and put
\[
q_B(u)=u^{\mathsf T}Bu.
\]
Then
\[
\rho_{E_\varepsilon}(u)
=
R\left(1+\varepsilon q_B(u)\right)+o(\varepsilon).
\]

Li--Liu--Huang define the dual conical \(\mu\)-measure by
\[
d\widetilde V_{\mu,K}(u)
=
\frac1n\rho_K(u)^n g(\rho_K(u)u)\,d\sigma(u).
\]
Because \(g(x)=\phi(|x|)\),
\[
d\widetilde V_{\mu,K_\varepsilon}(u)
=
c_0\left[
1+\varepsilon
\left(
n+\eta_R
\right)q_A(u)
\right]d\sigma(u)
+O(\varepsilon^2),
\]
where
\[
c_0=\frac{R^n\phi(R)}n.
\]
The total mass has no first-order change because \(A\) is traceless.

For finite \(p\), Theorem 1.3 of arXiv:2608.21958v1 characterizes \(E_\varepsilon\) by
\[
|\widetilde V_{\mu,K_\varepsilon}|\,
\rho_{E_\varepsilon^*}(x)^{-2}
=
n\int_{S^{n-1}}
|x\cdot u|^2
\rho_{E_\varepsilon}(u)^2
\left(
\frac{\rho_{E_\varepsilon}(u)}
{\rho_{K_\varepsilon}(u)}
\right)^{-p}
d\widetilde V_{\mu,K_\varepsilon}(u).
\]
For \(|x|=1\),
\[
\rho_{E_\varepsilon^*}(x)^{-2}
=
R^2\left(1+2\varepsilon q_B(x)\right)+o(\varepsilon).
\]
The integrand on the right has relative first variation
\[
(2-p)q_B(u)
+
\left(p+n+\eta_R\right)q_A(u).
\]

Use the standard spherical fourth-moment identity
\[
\frac n{|S^{n-1}|}
\int_{S^{n-1}}
(x\cdot u)^2q_C(u)\,d\sigma(u)
=
\frac{\operatorname{tr}C+2q_C(x)}{n+2}
\]
for every symmetric matrix \(C\) and every unit vector \(x\). Comparing first-order terms in the characterization equation gives
\[
2q_B(x)
=
\frac{
(2-p)\left(\operatorname{tr}B+2q_B(x)\right)
+
2\left(p+n+\eta_R\right)q_A(x)
}{n+2}.
\]
Averaging over \(x\in S^{n-1}\) yields
\[
\operatorname{tr}B=0.
\]
The traceless part therefore satisfies
\[
(n+p)q_B(x)
=
\left(p+n+\eta_R\right)q_A(x)
\]
for every \(x\), hence
\[
B=
\left(
1+\frac{\eta_R}{n+p}
\right)A.
\]
This proves the displayed coefficient.

It remains to justify differentiability of the optimizer. Parameterize origin-symmetric ellipsoids near \(RB_2^n\) by positive-definite symmetric matrices. The characterization equation above is a finite-dimensional \(C^1\) system. At the ball, its derivative in the ellipsoid variable acts by the nonzero scalar \(p\) on scalar matrices and by
\[
\frac{2(n+p)}{n+2}
\]
on traceless symmetric matrices. Its Jacobian is therefore invertible. The implicit-function theorem gives the claimed \(C^1\) local branch, and uniqueness from Theorem 1.3 identifies that branch with \(E_\varepsilon\).

For the Gaussian density,
\[
\frac{R\phi'(R)}{\phi(R)}=-R^2,
\]
which gives
\[
c_R=1-\frac{R^2}{n+p}
\]
and the transition at \(R=\sqrt{n+p}\).

## Verification

The proof uses only the published characterization theorem, the radial density expansion, and the exact spherical fourth-moment identity. The scalar and traceless matrix modes were checked separately; both Jacobian eigenvalues are nonzero for every \(p>0\).

As a numerical stress test, the two-dimensional Gaussian optimization was independently evaluated for \(p=3\) and a small traceless elliptic perturbation. The measured first-order shape multipliers agreed with
\[
1-\frac{R^2}{5}
\]
at radii below, at, and above \(\sqrt5\), including the predicted sign reversal. This numerical test is not used in the proof.

## Relationship to prior work

Li--Liu--Huang introduce the dual \(L_p\) John ellipsoid for general measures, prove existence and uniqueness, give the characterization used above, and explicitly specialize their theory to Gaussian measure. Their paper does not state a local ellipsoidal response law at a Euclidean ball, does not identify a critical radius \(\sqrt{n+p}\), and contains no perturbative analysis of the Gaussian ellipsoid map.

Yu--Leng--Wu develop the classical dual \(L_p\) John ellipsoid for Lebesgue measure. In that homogeneous setting affine covariance makes ellipsoids behave without the radial-density correction. Their theory has no Gaussian density and therefore cannot produce the factor
\[
1-\frac{R^2}{n+p}.
\]

Ai--Huang study the nondual \(L_p\) John ellipsoid for general measures and include Gaussian applications. That construction is based on the Minkowski--Firey rather than harmonic-radial variation and does not imply the dual response formula above.

Targeted searches for the exact critical radius, Gaussian anisotropy reversal, degree-two linear response, radial-measure response coefficient, and equivalent perturbative formulations found no prior statement implying this theorem.

## Limitations

The result is local in the deformation parameter and is restricted to ellipsoidal, degree-two perturbations of a Euclidean ball. It does not determine the full nonlinear image of an arbitrary ellipsoid under the Gaussian dual \(L_p\) John map.

At the critical Gaussian radius \(R=\sqrt{n+p}\), the theorem identifies a vanishing first derivative but does not determine whether the leading nonzero anisotropic response is quadratic, cubic, or of another order.

The originality search cannot exclude an unindexed perturbative observation under different terminology. The closest older dual \(L_p\) literature is unweighted and therefore lacks the Gaussian transition mechanism.

## References

1. A.-J. Li, B. Liu, Q. Huang, “Dual \(L_p\) John ellipsoids for general measures,” arXiv:2608.21958v1, first public 2026-08-22.
2. W. Yu, G. Leng, D. Wu, “Dual \(L_p\) John ellipsoids,” Proceedings of the Edinburgh Mathematical Society 50 (2007), 737--753, DOI: 10.1017/S0013091506000332.
3. W. Ai, Q. Huang, “The \(L_p\) John ellipsoids for general measures,” Geometriae Dedicata 217 (2023), Article 17, DOI: 10.1007/s10711-022-00750-2.
