# Sharp area-constrained distortion gap on degenerating hyperbolic annuli

## Finding

Fix
\[
k>1,\qquad 0<\varepsilon<b<\infty.
\]
In the hyperbolic plane with geodesic polar metric
\[
g=dr^2+\sinh^2r\,d\theta^2,
\]
let
\[
\rho_k(r)=\operatorname{arccosh}(k\cosh r),
\]
and consider the annuli
\[
A_{\varepsilon,b}=\{(r,\theta):\varepsilon<r<b\},\qquad
A'_{\varepsilon,b}=\{(R,\Theta):\rho_k(\varepsilon)<R<\rho_k(b)\}.
\]
Consider orientation-preserving rotationally equivariant \(C^1\) diffeomorphisms, continuous with their differentials through the boundary, from the first annulus onto the second, agreeing pointwise on both boundary circles with
\[
F_0(r,\theta)=(\rho_k(r),\theta),
\]
and having *constant hyperbolic area Jacobian*
\[
J_hF\equiv k.
\]
The exact least maximal quasiconformal dilatation in this constrained class is
\[
\boxed{K_{\mathrm{area}}(k;\varepsilon,b)=\frac{k^2\cosh^2\varepsilon-1}{k\sinh^2\varepsilon}.}
\]
The radial map \(F_0\) attains this value. In fact every admissible map has the form
\[
F_\psi(r,\theta)=(\rho_k(r),\theta+\psi(r)),
\]
and the *complete sharp minimizer condition* is
\[
\boxed{\bigl(\sinh r\,\psi'(r)\bigr)^2
\le (K_0-q_k(r))(q_k(r)-K_0^{-1})\quad(\varepsilon\le r\le b),}
\]
where
\[
q_k(r)=\frac{k\sinh^2r}{k^2\cosh^2r-1},\qquad
K_0=K_{\mathrm{area}}=q_k(\varepsilon)^{-1}.
\]
The boundary condition means \(e^{i\psi(\varepsilon)}=e^{i\psi(b)}=1\). Nonzero smooth twists compactly supported in \((\varepsilon,b)\) satisfy the minimizer condition after sufficiently small scaling. Thus the optimal constrained map is not unique.

The same pointwise boundary data but **without** either the rotational equivariance or the area-Jacobian constraint has sharp quasiconformal cost
\[
\boxed{K_{\mathrm{free}}(k;\varepsilon,b)=
\frac{y(b)-y(\varepsilon)}{Y_k(b)-Y_k(\varepsilon)},}
\]
where
\[
y(r)=\log\tanh(r/2),\qquad
Y_k(r)=\log\tanh(\rho_k(r)/2)
=\frac12\log\frac{k\cosh r-1}{k\cosh r+1}.
\]
It satisfies
\[
1<K_{\mathrm{free}}<K_{\mathrm{area}}.
\]
For fixed \(k>1\) and fixed \(b>0\), the puncture limit \(\varepsilon\downarrow0\) has *different sharp blow-up scales*:
\[
K_{\mathrm{area}}\sim\frac{k^2-1}{k\varepsilon^2},\qquad
K_{\mathrm{free}}\sim\frac{\log(1/\varepsilon)}{L_{k,b}},
\]
\[
\boxed{\frac{K_{\mathrm{area}}}{K_{\mathrm{free}}}
\sim\frac{(k^2-1)L_{k,b}}{k\varepsilon^2\log(1/\varepsilon)},}
\]
with the strictly positive constant
\[
L_{k,b}=\frac12\log\frac{(k\cosh b-1)(k+1)}{(k\cosh b+1)(k-1)}.
\]
Finally, if \(k\) approaches one on the critical inner-radius scale
\[
k_\varepsilon=1+c\varepsilon^2,\qquad c\ge0\text{ fixed},
\]
then
\[
\lim_{\varepsilon\downarrow0}K_{\mathrm{area}}=1+2c,\qquad
\lim_{\varepsilon\downarrow0}K_{\mathrm{free}}=1,
\]
and hence the constrained-to-unconstrained distortion ratio tends to \(1+2c\).

## Assumptions and scope

The hyperbolic metric is normalized to sectional curvature \(-1\). Quasiconformal dilatation means the maximal ratio of the two singular values of the differential; multiplying the source or target metric by a pointwise conformal factor does not change that ratio. We use the modulus of the family of curves connecting the two boundary circles in the usual two-dimensional conformal sense. The free class consists of orientation-preserving quasiconformal homeomorphisms with pointwise trace \(F_0\) on both boundary circles and no other restrictions; the affine cylinder map in the proof realizes the infimum.

The constant-Jacobian constraint is imposed on the whole annulus. The boundary values of \(F_0\) force exactly the integration constant in the radial area equation, so there is no arbitrary prescribed radial profile hidden in the admissible class. Boundary twists may make full turns, but equality of boundary points requires their angles to be integer multiples of \(2\pi\).

The source's almost-symplectic radial stretch supplies the natural new geometric motivation and the explicit expression for \(\rho_k\). The theorem here distinguishes the **optimal constrained class**, the **unrestricted annular Teichmüller optimum**, and a sharp degeneration regime. No claim is made about minimization among non-equivariant maps that also have Jacobian \(k\).

## Proof

**Step 1: rigidity of the radial part under the area constraint.** Rotational equivariance of a degree-one oriented annular homeomorphism forces
\[
F(r,\theta)=(R(r),\theta+\psi(r)).
\]
The hyperbolic area form is
\[
dA_h=\sinh r\,dr\wedge d\theta.
\]
Therefore
\[
J_hF=\frac{\sinh R(r)R'(r)}{\sinh r}.
\]
If the Jacobian equals \(k\), integration yields
\[
\frac{d}{dr}\cosh R(r)=k\sinh r,
\qquad \cosh R(r)=k\cosh r+C.
\]
The inner boundary condition \(R(\varepsilon)=\rho_k(\varepsilon)\) forces \(C=0\). Hence
\[
R(r)=\rho_k(r)
\]
throughout the annulus; the outer boundary follows automatically.

**Step 2: the conformal-cylinder differential.** Introduce
\[
y=\log\tanh(r/2),\qquad x=\theta.
\]
Since \(dy/dr=1/\sinh r\), the hyperbolic metric is
\[
g=\sinh^2r\,(dy^2+dx^2).
\]
Likewise define \(Y=\log\tanh(R/2)\), \(X=\Theta\) in the target. The map \(F_\psi\) has cylinder differential
\[
D F_\psi=\begin{pmatrix}1&s\\0&q\end{pmatrix},
\qquad s=\frac{d\psi}{dy}=\sinh r\,\psi'(r),
\qquad q=\frac{dY}{dy}=\frac{\rho_k'(r)\sinh r}{\sinh\rho_k(r)}.
\]
Using \(\cosh\rho_k=k\cosh r\), we obtain the exact stretch factor
\[
q=q_k(r)=\frac{k\sinh^2r}{k^2\cosh^2r-1}.
\]
For \(k>1\), this satisfies \(0<q<1\). It is strictly increasing: with \(u=\cosh^2r>1\),
\[
q=k\frac{u-1}{k^2u-1},\qquad
\frac{dq}{du}=\frac{k(k^2-1)}{(k^2u-1)^2}>0.
\]
Thus \(q(\varepsilon)\) is the minimum, and
\[
K_0=q(\varepsilon)^{-1}
=\frac{k^2\cosh^2\varepsilon-1}{k\sinh^2\varepsilon}>1.
\]

**Step 3: sharp constrained minimax and all minimizers.** Let \(\sigma_1\ge\sigma_2>0\) be the Euclidean singular values of the conformal-cylinder matrix. Its determinant is \(q\), and its first column has length one. Therefore \(\sigma_1\ge1\), so its pointwise distortion obeys
\[
\mathcal K=\frac{\sigma_1}{\sigma_2}
=\frac{\sigma_1^2}{q}\ge\frac1q.
\]
Taking the supremum and approaching the inner boundary proves \(K(F_\psi)\ge K_0\) for every admissible map. For \(\psi=0\), the singular values are \(1\) and \(q\), so \(K(F_0)=K_0\).

Moreover,
\[
\mathcal K+\mathcal K^{-1}=
\frac{\operatorname{tr}((DF_\psi)^\mathsf{T}DF_\psi)}{\det DF_\psi}
=\frac{1+s^2+q^2}{q}.
\]
Since \(u+u^{-1}\) is strictly increasing on \([1,\infty)\), the inequality \(\mathcal K\le K_0\) is equivalent to
\[
s^2\le q(K_0+K_0^{-1})-1-q^2
=(K_0-q)(q-K_0^{-1}).
\]
This proves both the necessary and sufficient pointwise condition for a global minimizer (including boundary limits). On each compact interval strictly inside \((\varepsilon,b)\), the right side is strictly positive. Consequently any nonzero smooth \(\psi\) compactly supported there, multiplied by a sufficiently small positive scalar, defines another minimizer with the same pointwise boundary data, proving genuine nonuniqueness.

**Step 4: exact unrestricted optimum.** The conformal cylinders have widths
\[
\Delta y=y(b)-y(\varepsilon)>0,\qquad
\Delta Y=Y_k(b)-Y_k(\varepsilon)>0
\]
and common circumference \(2\pi\). Thus their connecting-curve moduli are \(2\pi/\Delta y\) and \(2\pi/\Delta Y\). Every quasiconformal annular homeomorphism with the prescribed boundary correspondence distorts moduli by at most its maximal dilatation. Since \(\Delta Y<\Delta y\), this yields
\[
K\ge\frac{\Delta y}{\Delta Y}.
\]
The affine map of conformal cylinders
\[
X=x,\qquad
Y=Y_k(\varepsilon)+\frac{\Delta Y}{\Delta y}(y-y(\varepsilon))
\]
attains the bound and matches both boundary circles pointwise. Hence
\[
K_{\mathrm{free}}=\frac{\Delta y}{\Delta Y}.
\]
Because \(\Delta Y=\int_{y(\varepsilon)}^{y(b)}q_k(r(y))\,dy\) and \(q_k\) is strictly increasing with values in \((0,1)\), its average \(\bar q=\Delta Y/\Delta y\) lies strictly between \(q_k(\varepsilon)\) and \(1\). Thus
\[
1<K_{\mathrm{free}}=\bar q^{-1}<q_k(\varepsilon)^{-1}=K_{\mathrm{area}}.
\]

**Step 5: two distinct puncture scales.** For fixed \(k>1\),
\[
\sinh\varepsilon\sim\varepsilon,\quad
K_{\mathrm{area}}=k+\frac{k^2-1}{k\sinh^2\varepsilon}
\sim\frac{k^2-1}{k\varepsilon^2}.
\]
Also
\[
y(\varepsilon)=\log\varepsilon-\log2+O(\varepsilon^2),
\]
while
\[
Y_k(\varepsilon)\longrightarrow
\frac12\log\frac{k-1}{k+1}
\]
remains finite. Consequently \(\Delta y\sim\log(1/\varepsilon)\), \(\Delta Y\to L_{k,b}>0\), and the stated \(K_{\mathrm{free}}\) and distortion-ratio asymptotics follow.

For the matched scaling \(k_\varepsilon=1+c\varepsilon^2\) with fixed \(c>0\), the exact formula gives
\[
K_{\mathrm{area}}=k_\varepsilon+
\frac{k_\varepsilon^2-1}{k_\varepsilon\sinh^2\varepsilon}\to1+2c.
\]
Meanwhile the inner target radius satisfies
\[
\rho_{k_\varepsilon}(\varepsilon)
=\varepsilon\sqrt{1+2c}+O(\varepsilon^3),
\]
so
\[
\Delta Y=\Delta y-\frac12\log(1+2c)+O(\varepsilon^2)
\]
and \(K_{\mathrm{free}}\to1\). If \(c=0\), the identity map makes both dilatations exactly one. This proves the full critical boundary-layer limit.

## Verification

The differential, Jacobian, monotonicity, singular-value and annulus-modulus identities were independently reconstructed from the polar metric. The constrained minimum and its equality condition are exact algebraic consequences of the singular values; no numerical minimization or finite exploration is used as a proof.

Direct high-precision calculations were also performed for \(k=2\), \(b=3\), and inner radii \(0.1\) and \(0.01\). They give respective constrained/free pairs \((151.5009984149,5.8371607168)\) and \((15001.5000100,10.4063303095)\), consistent with the inverse-square versus logarithmic separation. Tests with \(k=1+c\varepsilon^2\) and \(c=0.1,1,4\) agree with the predicted limits \(1+2c\).

All tests were performed from the closed expressions displayed in the proof; the numerical values are checks, not certificates of asymptotic statements. The result does not classify arbitrary non-equivariant constant-Jacobian minimizers.

## Relationship to prior work

Platis, *Extremality of hyperbolic spiral and stretch maps* (arXiv:2608.22897v1), defines the almost-symplectic radial stretch \(\rho_k(r)=\operatorname{arccosh}(k\cosh r)\), computes its local distortion and compares it qualitatively with unrestricted cylinder-affine quasiconformal interpolation. The inspected source results do not state minimax optimality in the entire area-preserving-up-to-scale rotationally equivariant class, all nonunique minimizers, or the divergent sharp puncture cost and critical boundary-layer law.

Platis, *Modulus of elementary domains in the hyperbolic plane* (arXiv:2512.00358), calculates connecting and separating moduli for circular hyperbolic annuli and supplies the conformal-cylinder perspective. This yields the classical unrestricted modulus bound, but contains no prescribed-constant-Jacobian minimizer classification or puncture-scale comparison. Older Euclidean spiral-stretch extremality and affine-additive group stretch papers concern different objective functionals or geometries, and do not imply this exact hyperbolic annular area-constraint theorem.

The originality distinction is **not** the existence of the particular almost-symplectic radial stretch or the known free annulus modulus formula. The new statement is the sharp constrained optimization over all rotationally equivariant constant-area-multiplier maps, the complete shearing minimizer locus, and the precise singular separation from the boundary-matched unrestricted optimum.

## Limitations

The constrained class is rotationally equivariant. A non-equivariant map with constant hyperbolic area Jacobian could in principle have different extremal behavior; no claim is made about that larger class.

The area multiplier is a positive real constant \(k>1\) with boundary circles fixed as specified. The puncture asymptotics hold with the outer radius \(b\) fixed. The matched-limit result covers \(k=1+c\varepsilon^2\) with fixed \(c\ge0\), not arbitrary two-parameter joint rates.

The sharp minimizer condition is pointwise and permits nontrivial interior twists; it does not claim uniqueness of an extremal map or uniqueness modulo isometries.

Some older spiral-stretch literature was accessible only through abstracts or bibliographic records. That is a residual priority risk, not evidence of an additional theorem beyond the compared material.

## References

1. I. D. Platis, *Extremality of hyperbolic spiral and stretch maps*, arXiv:2608.22897v1, first posted 24 August 2026.
2. I. D. Platis, *Modulus of elementary domains in the hyperbolic plane*, arXiv:2512.00358, first posted 29 November 2025, version 3 June 2026.
3. Z. M. Balogh, B. Bubani, and I. D. Platis, *Stretch maps on the affine-additive group*, Analysis and Mathematical Physics 15 (2025), article 61, DOI: 10.1007/s13324-025-01047-9.
4. Z. M. Balogh, K. Fässler, and I. D. Platis, *Modulus of curve families and extremality of spiral-stretch maps*, Journal d'Analyse Mathématique 113 (2011), DOI: 10.1007/s11854-011-0007-x.
