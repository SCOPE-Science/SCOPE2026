# Sharp modular-distance defect for Loewner's torus inequality

## Result

Let \(G\) be a Riemannian metric on the two-torus \(T^2\). Let
\[
G=f^2G_0
\]
be its conformal representation relative to the unit-area flat metric \(G_0\) in the same conformal class, and let
\[
\operatorname{Var}(f)
=\int_{T^2}\left(f-\int_{T^2} f\,d\mu_0\right)^2d\mu_0 .
\]
Write
\[
\mathcal M=\operatorname{PSL}(2,\mathbb Z)\backslash\mathbb H
\]
for the modular orbifold with the quotient of the Poincare metric
\(ds^2=(dx^2+dy^2)/y^2\). Let \(E\in\mathcal M\) be the equilateral
(Eisenstein) conformal class, represented by
\[
\rho=\frac12+i\frac{\sqrt3}{2},
\]
and put
\[
d=d_{\mathcal M}([G_0],E).
\]

Define \(d_0=\log\sqrt3\) and
\[
\Phi(d)=
\begin{cases}
\displaystyle
\frac{2\sqrt3\,e^d}{3+e^{2d}}-\frac{\sqrt3}{2},
&0\le d\le d_0,\\[1.2ex]
\displaystyle
\frac{\sqrt3\cosh d+\sqrt{3\cosh^2d-4}}2-\frac{\sqrt3}{2},
&d\ge d_0.
\end{cases}
\]

Then
\[
\boxed{
\operatorname{area}(G)-\frac{\sqrt3}{2}\operatorname{sys}(G)^2
\ge
\operatorname{Var}(f)+
\Phi(d)\operatorname{sys}(G)^2 .
}
\]

The function \(\Phi\) is pointwise sharp: for every \(d\ge0\) there is a
flat torus at modular distance \(d\) from the equilateral class for which
equality holds.

In particular,
\[
\Phi(d)=\frac{\sqrt3}{4}d-\frac{\sqrt3}{8}d^2+O(d^3)
\qquad(d\downarrow0).
\]
Thus the classical Loewner defect separates into two quantitative pieces:
an \(L^2\) conformal-factor defect and an explicit sharp conformal-modulus
defect. Near the equilateral class, the latter is linear in modular
hyperbolic distance.

## Starting point in the literature

Horowitz, K. U. Katz and M. G. Katz proved the conformal-class refinement
\[
\operatorname{area}(G)-(\operatorname{Im}\tau)\operatorname{sys}(G)^2
\ge \operatorname{Var}(f)
\tag{1}
\]
for the reduced modular parameter
\[
\tau=x+iy,\qquad |x|\le\frac12,\qquad |\tau|\ge1.
\]
Their proof records \(y\ge\sqrt3/2\), with equality at the Eisenstein
class, and obtains the usual isosystolic-defect inequality by discarding
the extra amount \(y-\sqrt3/2\).

The new point here is to identify the **best possible value of that
discarded amount from the intrinsic modular distance to the extremal
conformal class**, globally and in closed form.

## Modular geometry lemma

Let
\[
\mathcal F=\left\{x+iy:\ |x|\le\frac12,\ x^2+y^2\ge1,\ y>0\right\}.
\]
For \(\tau=x+iy\in\mathcal F\), let
\[
d=d_{\mathcal M}([\tau],[\rho]).
\]
Then
\[
y-\frac{\sqrt3}{2}\ge\Phi(d),
\tag{2}
\]
and the bound is sharp for every \(d\ge0\).

### Proof

The standard half-domain
\[
\mathcal F_+=\left\{x+iy\in\mathcal F:0\le x\le\frac12\right\}
\]
is a \((2,3,\infty)\) hyperbolic reflection chamber with order-three vertex
\(\rho\). The standard modular tessellation shows that on
\(\mathcal F_+\) the quotient distance to the equilateral class is
\(d_{\mathbb H}(\tau,\rho)\). Reflection \(x\mapsto-x\) preserves the
distance to the modular orbit of the equilateral point, so it suffices to
work in \(\mathcal F_+\).

Set
\[
b=\frac{\sqrt3}{2},\qquad \rho=\frac12+ib.
\]
The hyperbolic distance formula gives
\[
\cosh d_{\mathbb H}(x+iy,\rho)
=
\frac{(x-\frac12)^2+y^2+b^2}{2by}.
\tag{3}
\]
For fixed \(y\), the right-hand side increases with
\(\frac12-x\). Therefore the largest distance attainable at height \(y\)
inside \(\mathcal F_+\) occurs at the smallest allowed \(x\).

For \(b\le y\le1\), the constraint \(x^2+y^2\ge1\) gives
\(x\ge\sqrt{1-y^2}\). Hence the extremal point lies on the unit-circle
boundary. Write it as
\[
\tau=e^{i\theta},\qquad \frac{\pi}{3}\le\theta\le\frac{\pi}{2}.
\]
The unit semicircle is a hyperbolic geodesic, so
\[
d=\int_{\pi/3}^{\theta}\frac{dt}{\sin t}
=\log\!\left(\sqrt3\tan\frac{\theta}{2}\right).
\]
Solving for \(y=\sin\theta\) yields
\[
y=
\frac{2\sqrt3\,e^d}{3+e^{2d}},
\qquad
0\le d\le\log\sqrt3.
\tag{4}
\]

For \(y\ge1\), the smallest allowed \(x\) is \(0\). At \(\tau=iy\),
equation (3) becomes
\[
\cosh d=\frac{y^2+1}{\sqrt3\,y}.
\]
Solving the quadratic and taking \(y\ge1\) gives
\[
y=
\frac{\sqrt3\cosh d+\sqrt{3\cosh^2d-4}}{2},
\qquad
d\ge\log\sqrt3.
\tag{5}
\]
The two formulas meet at \(y=1\) and \(d=\log\sqrt3\). Since the
boundary choices used above maximize the distance available at each
height, equations (4)--(5) are exactly the minimum possible height at
fixed quotient distance. Subtracting \(b\) proves (2).

Equality in (2) is realized on the unit-circle boundary for
\(0\le d\le\log\sqrt3\), and on the imaginary axis for
\(d\ge\log\sqrt3\). \(\square\)

## Proof of the theorem

For a reduced parameter \(\tau=x+iy\), (1) gives
\[
\operatorname{area}(G)-y\operatorname{sys}(G)^2
\ge\operatorname{Var}(f).
\]
Therefore
\[
\operatorname{area}(G)-\frac{\sqrt3}{2}\operatorname{sys}(G)^2
\ge
\operatorname{Var}(f)
+
\left(y-\frac{\sqrt3}{2}\right)\operatorname{sys}(G)^2.
\]
Applying the modular geometry lemma proves the displayed theorem.

For sharpness, choose one of the boundary conformal classes realizing
equality in (2), and take \(G\) to be any constant multiple of its
unit-area flat metric. Then \(f\) is constant, so
\(\operatorname{Var}(f)=0\), and the shortest lattice vector in the
reduced normalization has squared length \(1/y\). Consequently
\[
\operatorname{area}(G)-\frac{\sqrt3}{2}\operatorname{sys}(G)^2
=
\left(y-\frac{\sqrt3}{2}\right)\operatorname{sys}(G)^2,
\]
which is exactly \(\Phi(d)\operatorname{sys}(G)^2\).

Finally, expansion of the first branch at \(d=0\) gives
\[
\Phi(d)=\frac{\sqrt3}{4}d-\frac{\sqrt3}{8}d^2
-\frac{7\sqrt3}{48}d^3+O(d^4).
\]

## What is and is not claimed

The theorem is an exact refinement of Loewner's inequality in terms of
the Poincare quotient distance on the modular orbifold. It does not claim
that modular hyperbolic distance is the only useful notion of distance
between metrics, nor does it give a Gromov--Hausdorff, Lipschitz, or
Sobolev distance to an equilateral flat metric for a nonflat torus.

The pointwise sharpness statement concerns the coefficient as a function
of the conformal-class distance: flat tori realize equality for every
distance. The variance term remains the established conformal-factor
defect from the 2009 theorem.

## Literature check and relation to prior work

1. C. Horowitz, K. U. Katz, M. G. Katz,
   *Loewner's torus inequality with isosystolic defect*,
   J. Geom. Anal. 19 (2009), 796--808.
   arXiv:0803.0690; DOI: 10.1007/s12220-009-9090-y.
   Theorem 4.1 gives (1), and Section 3 uses the standard modular
   fundamental domain. The paper does not state a defect in terms of
   hyperbolic distance in moduli space.

2. J. Eyll,
   *Stability of Systolic Inequalities for the Möbius Strip and Klein
   Bottle*, J. Geom. Anal. 35 (2025), article 365.
   DOI: 10.1007/s12220-025-02197-9; arXiv:2502.13715.
   This gives modern stability estimates for other classical systolic
   inequalities and explicitly discusses conformal-class and
   conformal-factor defects, but it does not give the torus
   modular-distance formula above.

3. M. G. Katz and S. Sabourau,
   *Nonpositively Curved Surfaces are Loewner*,
   J. Geom. Anal. 34 (2024), article 291.
   DOI: 10.1007/s12220-024-01732-4.
   This develops Loewner-type bounds for nonpositively curved surfaces,
   rather than a quantitative modular-distance refinement for the torus.

Searches through current literature using combinations of “Loewner torus”,
“isosystolic defect”, “hyperbolic distance”, “modular surface”, “Hermite
invariant”, “hexagonal lattice”, “equilateral torus”, and “stability” did
not locate the piecewise sharp function \(\Phi\), or an equivalent theorem
bounding the Loewner defect by the modular hyperbolic distance to the
Eisenstein class.

Originality is therefore asserted **to the best of our knowledge**.
Residual risk remains from unindexed or differently phrased literature,
especially work in the geometry of numbers where the same elementary
modular optimization could appear as a stability statement for the
two-dimensional Hermite invariant.

## Reproducibility notes

The only external input to the proof is the conformal-class inequality
(1). The remaining calculation uses the standard hyperbolic distance
formula
\[
\cosh d_{\mathbb H}(z,w)
=1+\frac{|z-w|^2}{2\,\operatorname{Im}z\,\operatorname{Im}w}
\]
and the standard modular fundamental domain. The branch point can be
checked directly:
\[
d_0=\operatorname{arcosh}\frac{2}{\sqrt3}
=\log\sqrt3.
\]
