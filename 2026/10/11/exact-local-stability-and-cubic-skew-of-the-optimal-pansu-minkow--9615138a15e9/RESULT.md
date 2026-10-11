# Exact local stability and cubic skew of the optimal Pansu-Minkowski sphere

## Finding

Let \(S_L\), with
\[
0<L\le \frac12,
\]
be the Pansu-Minkowski spheres introduced by Fogagnolo, Pinamonti, and Verzellesi in the first Heisenberg group, and set
\[
Q(L)=Q_{\mathrm{mink}}^{\mathbb H}(S_L).
\]
The source proves that \(S_{1/4}\) is the unique minimizer of this quotient inside the full Pansu-Minkowski family and that
\[
Q\!\left(\frac14\right)=(18\pi)^{1/3}.
\]

The local deficit has the exact expansion
\[
\boxed{
\frac{Q(L)}{(18\pi)^{1/3}}
=
1+(\pi^2-8)d^2
+\frac{2\pi}{3}(48-5\pi^2)d^3
+O(d^4),
\qquad
 d=L-\frac14.
}
\]
In particular,
\[
\boxed{
Q''\!\left(\frac14\right)
=2(18\pi)^{1/3}(\pi^2-8)>0,
}
\]
so the optimizer is nondegenerate along the complete one-parameter moduli of rotational area-constrained critical surfaces.

Equivalently, the exact sharp local quadratic stability constant is
\[
\boxed{
\lim_{L\to1/4}
\frac{Q(L)/(18\pi)^{1/3}-1}{(L-1/4)^2}
=\pi^2-8.
}
\]
The cubic term also detects a directional skew. Since
\[
48-5\pi^2<0,
\]
there exists \(\varepsilon>0\) such that
\[
\boxed{
Q\!\left(\frac14+t\right)
<
Q\!\left(\frac14-t\right)
\qquad
(0<t<\varepsilon).
}
\]
Thus the higher-\(L\) side of the optimal sphere has the smaller quotient among equal sufficiently small parameter displacements.

## Assumptions and scope

The family is the source's normalized Pansu-Minkowski family. The parameter range is
\[
0<L\le\frac12.
\]
The source identifies these surfaces as all rotationally invariant, closed, mean-convex critical points of total horizontal mean curvature under area-preserving non-characteristic variations, up to intrinsic dilations and vertical translations.

The statement concerns the Minkowski quotient restricted to this complete critical family. It is not a stability theorem for arbitrary nonsymmetric variations. Indeed, the source proves that Pansu-Minkowski spheres are unstable once the rotational-symmetry restriction is removed.

## Proof

The source introduces the reparameterization
\[
\ell=2\arccos\sqrt{1-2L},
\qquad
0<\ell\le\pi.
\]
Solving for \(L\) gives
\[
L=\frac{1-\cos\ell}{4}.
\]
The optimal parameter \(L=1/4\) corresponds to
\[
\ell=\frac\pi2.
\]

In this variable, the source's exact quotient formula is
\[
Q(\ell)
=
4(2\pi)^{1/3}
\frac{\sin\ell-\ell\cos\ell}
{\left(3\sin\ell+\frac13\sin(3\ell)-4\ell\cos\ell\right)^{2/3}}.
\]
Put
\[
u=\ell-\frac\pi2.
\]
Define
\[
A(u)=\sin\ell-\ell\cos\ell,
\qquad
B(u)=3\sin\ell+\frac13\sin(3\ell)-4\ell\cos\ell.
\]
Taylor expansion at \(u=0\) gives
\[
A(u)
=
1+\frac\pi2u+\frac12u^2-\frac\pi{12}u^3+O(u^4),
\]
and
\[
B(u)
=
\frac83+2\pi u+4u^2-\frac\pi3u^3+O(u^4).
\]
Since
\[
Q(0)=(18\pi)^{1/3},
\]
expanding the quotient yields
\[
\frac{Q(\ell)}{(18\pi)^{1/3}}
=
1+\frac{\pi^2-8}{16}u^2
+\frac{\pi(48-5\pi^2)}{96}u^3
+O(u^4).
\]

Now
\[
d=L-\frac14
=
\frac{\sin u}{4}
=
\frac u4-\frac{u^3}{24}+O(u^5),
\]
so inversion gives
\[
u=4d+\frac{32}{3}d^3+O(d^5).
\]
Substituting this into the previous expansion gives
\[
\frac{Q(L)}{(18\pi)^{1/3}}
=
1+(\pi^2-8)d^2
+\frac{2\pi}{3}(48-5\pi^2)d^3
+O(d^4).
\]

Because
\[
\pi^2-8>0,
\]
the quadratic term is strictly positive, proving nondegeneracy and the stated limit. Finally,
\[
48-5\pi^2<0.
\]
For equal displacements \(\pm t\), the even quadratic terms cancel, while the first unequal contribution is
\[
\frac{4\pi}{3}(48-5\pi^2)t^3<0.
\]
Hence
\[
Q\!\left(\frac14+t\right)-Q\!\left(\frac14-t\right)<0
\]
for all sufficiently small positive \(t\).

## Verification

The bundled checker starts from the source's exact \(\ell\)-formula, not from the displayed conclusion. It verifies symbolically that
\[
Q\!\left(\frac\pi2\right)=(18\pi)^{1/3},
\]
computes the normalized Taylor coefficients through cubic order, verifies the change of variables
\[
L-\frac14=\frac{\sin u}{4},
\]
and checks that the resulting coefficients are exactly
\[
\pi^2-8
\]
and
\[
\frac{2\pi}{3}(48-5\pi^2).
\]
It also verifies the two strict sign facts used in the interpretation.

No numerical experiment is used to infer the expansion or the sign conclusions. Decimal values may be printed by the checker only as diagnostics.

## Relationship to prior work

Fogagnolo, Pinamonti, and Verzellesi derive the exact Pansu-Minkowski family, compute its horizontal area and total horizontal mean curvature, obtain the exact quotient formula above, and prove that \(L=1/4\) is the unique minimizer in the family. Their proof establishes the sign of the first derivative after the \(\ell\)-reparameterization.

The inspected full text does not state the Hessian of the quotient at the optimum, the sharp local deficit coefficient \(\pi^2-8\), the cubic coefficient, or the resulting one-sided skew. The paper's second-variation stability theorem concerns the penalized total-mean-curvature functional under geometric variations; it is a different quadratic form from the scalar Hessian of the Minkowski quotient along the complete Pansu-Minkowski moduli.

Targeted searches for the exact coefficient, second derivative, local quotient stability, and the source identifier did not locate a prior statement of this expansion.

## Limitations

The result is local in the shape parameter \(L\). It does not provide the best global constant \(C\) in an inequality of the form
\[
Q(L)/(18\pi)^{1/3}-1\ge C(L-1/4)^2
\]
for the full interval \(0<L\le1/2\).

It also does not alter the source's instability result under unrestricted non-characteristic perturbations and does not prove existence of a global minimizer of the Minkowski quotient outside the rotational class.

The parameter \(L\) is the canonical source parameter for the classified family; the coefficient \(\pi^2-8\) is sharp for this parameterization. A different nonlinear coordinate on the one-dimensional moduli would transform the numerical Hessian in the expected way.

## References

1. Mattia Fogagnolo, Andrea Pinamonti, and Simone Verzellesi, *Unexpected phenomena for mean curvature functionals in the Heisenberg group*, arXiv:2605.29912v1, first submitted 28 May 2026.
2. Ana Hurtado and César Rosales, *Existence, characterization and stability of Pansu spheres in sub-Riemannian 3-space forms*, Calculus of Variations and Partial Differential Equations 54 (2015), 3183--3227.
