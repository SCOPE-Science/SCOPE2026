# Bisector sections of affine double cones and a strict section-root gap

## Finding
Let \(d\ge3\) be an integer, \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), and let the solid centrally symmetric circular double cone be
\[
C_d=\{(x,z)\in\mathbb R^{d-1}\times\mathbb R:\|x\|_2+|z|\le1\}.
\]
For the unit bisector direction \(u_*=(e_1+e_d)/\sqrt2\), the full hyperplane-section profile is exactly
\[
A_{d,u_*}(t)=\frac{2\sqrt2\,\kappa_{d-2}}{d}(1-2t^2)^{(d-2)/2},\qquad |t|\le\frac1{\sqrt2},
\]
and is zero outside that interval. In particular, the profile is a rescaled power of a quadratic, even though the sections are not generally balls.

Define \(\alpha_d=(d-2)/(d-1)\) and the affine-invariant directional section-root functional
\[
F_d(K;u)=\frac{\left[\int_{-h_K(u)}^{h_K(u)} A_{d,u}(t)^{\alpha_d}\,dt\right]^{d-1}}{h_K(u)\,V_d(K)^{d-2}}.
\]
Here \(h_K(u)=\max_{y\in K}\langle y,u\rangle\), \(A_{d,u}(t)=V_{d-1}(K\cap\{y:\langle y,u\rangle=t\})\), \(u\in S^{d-1}\), and \(K\) is centrally symmetric about the origin with nonempty interior. The exact evaluated directional benchmark is
\[
\boxed{F_d(C_d;u_*)=\left(\frac{\kappa_{d-2}}{\kappa_{d-1}}\right)^{d-2}B\left(\frac12,1+\frac{(d-2)^2}{2(d-1)}\right)^{d-1}.}
\]
It holds unchanged for every invertible linear image \(TC_d\) along \(u=T^{-T}u_*/\|T^{-T}u_*\|\).

In dimension three this is a strict, explicit subclass benchmark for the max-direction functional in Saroglou's Conjecture 1.6:
\[
F_3(C_3;u_*)=\frac2\pi B\!\left(\frac12,\frac54\right)^2
=2\left(\frac{\Gamma(5/4)}{\Gamma(7/4)}\right)^2
=1.94527965797909\ldots\ .
\]
For any invertible \(T\), every centered ellipsoid \(E\), and \(\mathcal S(K)=\max_{\|u\|=1}F_3(K;u)\), one has the rigorous strict separation
\[
\boxed{\mathcal S(TC_3)\ \ge F_3(TC_3;u)\ >\frac{3\pi^2}{16}+\frac1{100}\ =\mathcal S(E)+\frac1{100}.}
\]
The actual directional gap for the displayed bisector is \(0.09472883277483\ldots\). No claim is made that this bisector maximizes \(F_3(C_3;\cdot)\).

## Assumptions and scope
Every \(d\) is an integer at least three; the Euclidean norm and volumes are unnormalized. The double cone \(C_d\) is the convex hull of the unit \((d-1)\)-ball in \(z=0\) and the two points \(\pm e_d\). The beta function is \(B(a,b)=\int_0^1s^{a-1}(1-s)^{b-1}ds\) for \(a,b>0\). The stated affine family comprises invertible linear images of this centered body, including double cones with ellipsoidal bases and inclined axes. The directional formula is *not* the global directional maximum in dimensions three or higher.

## Proof
**Section profile.** Introduce orthonormal coordinates \(t=(x_1+z)/\sqrt2\), \(v=(x_1-z)/\sqrt2\), and \(w=(x_2,\dots,x_{d-1})\). Because \(\|x\|_2+|z|\le1\), the support range is \(|t|\le 1/\sqrt2\). At fixed \(t\), the feasible \(v\) interval is precisely \([-1/\sqrt2,1/\sqrt2]\). The allowable \((d-2)\)-ball in \(w\) has squared radius
\[
R^2(t,v)=\begin{cases}
(1-\sqrt2t)(1+\sqrt2v),&v\le t,\\
(1+\sqrt2t)(1-\sqrt2v),&v\ge t.
\end{cases}
\]
This follows directly by squaring \(\sqrt{x_1^2+\|w\|_2^2}\le1-|z|\) on the two halfplanes \(z\ge0\) and \(z\le0\). The positivity conditions hold on the specified intervals. Integrating the \((d-2)\)-ball volumes in the orthonormal coordinate \(v\) gives, with \(p=(d-2)/2\),
\[
A_{d,u_*}(t)=\kappa_{d-2}\left[(1-\sqrt2t)^p\int_{-1/\sqrt2}^t(1+\sqrt2v)^p dv
+(1+\sqrt2t)^p\int_t^{1/\sqrt2}(1-\sqrt2v)^p dv\right]
=\frac{2\sqrt2\,\kappa_{d-2}}d(1-2t^2)^p.
\]
Both endpoint values vanish for \(d\ge3\). In contrast, the axial sections are \(A_{d,e_d}(t)=\kappa_{d-1}(1-|t|)^{d-1}\) for \(|t|\le1\).

**Beta evaluation.** The full cone volume is \(V_d(C_d)=2\kappa_{d-1}/d\); its bisector support value is \(1/\sqrt2\). Raise the section formula to \(\alpha_d\), substitute \(s=\sqrt2t\), and use
\[
\int_{-1}^1(1-s^2)^qds=B\left(\frac12,q+1\right),\qquad q>-1.
\]
The factor of \(\kappa_{d-2}/\kappa_{d-1}\) survives all normalization, giving the boxed all-dimensional identity.

**Affine invariance.** For invertible \(T\), set \(\lambda=1/\|T^{-T}u_*\|\) and \(u=T^{-T}u_*/\|T^{-T}u_*\|\). Then \(T^Tu=\lambda u_*\), the support is multiplied by \(\lambda\), the section at \(t\) has \((d-1)\)-volume \(|\det T|\lambda^{-1}A_{d,u_*}(t/\lambda)\), and total volume is multiplied by \(|\det T|\). Therefore the numerator of \(F_d\) is multiplied by \(|\det T|^{d-2}\lambda\), precisely the multiplier of its denominator. Thus \(F_d(TC_d;u)=F_d(C_d;u_*)\).

**Strict three-dimensional separation.** With \(d=3\), the preceding beta identity simplifies using the gamma recursion to \(2(\Gamma(5/4)/\Gamma(7/4))^2\). Every ellipsoid has \(\mathcal S(E)=3\pi^2/16\): by affine invariance one may use the unit ball, whose sections have area \(\pi(1-t^2)\), so \(\int_{-1}^1\sqrt{\pi(1-t^2)}dt=\pi^{3/2}/2\) and \(V_3(B_2^3)=4\pi/3\).

To show a *rigorous* positive gap, write \(\mathcal B=B(1/2,5/4)=\int_{-1}^1(1-t^2)^{1/4}dt\). Since \((1-z)^{-1/4}\) has positive binomial-series coefficients, for \(0\le z<1\)
\[
(1-z)^{-1/4}\ge1+\frac z4+\frac{5z^2}{32}+\frac{15z^3}{128},
\]
with strict inequality on \(0<z<1\). Multiply by \(\sqrt{1-t^2}\), substitute \(z=t^2\), and integrate. The four even semicircle moments, normalized by \(\pi/2\), are \(1,1/4,1/8,5/64\), yielding
\[
\mathcal B>\frac\pi2\left(1+\frac1{16}+\frac5{256}+\frac{75}{8192}\right)=\frac\pi2\frac{8939}{8192}.
\]
Put \(S=8939/8192\). Using elementary \(157/50<\pi<22/7\), the above exact lower estimate implies
\[
F_3(C_3;u_*)-\frac{3\pi^2}{16}>\frac\pi2\left(S^2-\frac{3\pi}8\right)
>\frac{157}{100}\left(S^2-\frac{33}{28}\right)
=\frac{893631283}{46976204800}>\frac1{100}.
\]
The final strict inequality is integer arithmetic. Affine invariance and \(\max_u F_3\ge F_3(C_3;u_*)\) finish the subclass result.

## Verification
Run the self-contained standard-library file `verify.py` with \(\texttt{python3 verify.py}\). It checks the rational gap certificate exactly, compares the closed beta expression with numerical integration of the section profile in dimensions three through seven, and recomputes the section areas from independent one-dimensional geometric quadrature. The script does not prove the infinite-dimensional or all-dimensional symbolic identities: those follow from the displayed integrations. The numerical values are approximations only.

## Relationship to prior work
Saroglou [1, Conjecture 1.6] proposed that, among centrally symmetric three-dimensional convex bodies, the maximum over directions of precisely the section-square-root quotient used here is minimized at ellipsoids. Saroglou [1, Theorem 1.4] identifies the right circular double cone in its *axial* direction as the equality case for a separate sharp lower bound involving the second projection body. At that axial direction the present quotient is only \(F_3(C_3;e_d)=3/2\), whereas the ellipsoid value is \(3\pi^2/16\); evaluating a genuinely oblique direction is essential. Theorem 1.5 of [1] involves the same sectional expression as a lower bound on a different projection-body invariant, but does not supply the bisector profile or exact benchmark proved here.

Saroglou [2] establishes extremal projection-body *volumes* for certain cones and double cones; that is a different functional and does not itself imply an evaluation of the section-root integral. An equivalent historical calculation of inclined sections cannot be excluded without further full-text comparison of the broader cone literature.

## Limitations
This result does not prove Saroglou's conjecture for arbitrary centrally symmetric bodies, does not characterize maximizing directions for double cones, and does not assert any sharp gap over all nonellipsoids. The universal statement here is restricted to the affine family of circular double cones and to a specific direction. The all-dimensional beta identity is proved, but a comparison against Euclidean balls in every higher dimension is not asserted. The claim of originality is subject to possible prior equivalent inclined-cone section identities.

## References
[1] C. Saroglou, *On the shape of a convex body with respect to its second projection body*, arXiv:1409.4347, first publicly submitted 2014-09-15, Conjecture 1.6, Theorems 1.4–1.5 and Section 5. https://arxiv.org/abs/1409.4347

[2] C. Saroglou, *Volumes of projection bodies of some classes of convex bodies*, Mathematika 57 (2011), 329–353, DOI 10.1112/S0025579311001860. https://doi.org/10.1112/S0025579311001860
