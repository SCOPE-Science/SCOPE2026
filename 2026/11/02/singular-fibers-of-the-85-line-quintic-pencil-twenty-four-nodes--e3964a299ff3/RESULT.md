# Singular fibers of the 85-line quintic pencil: twenty-four nodes and an ordinary quadruple point

## Finding

Consider the pencil of quintic surfaces in \(\mathbb P^3_{\mathbb C}\)
\[
X_t=V(F_t),\qquad
F_t=(z-w)(x^4-3y^4)-6(z+w)x^2y^2+zw(w^3-tz^3),
\quad t\in\mathbb C.
\]
It is the explicit quintic pencil investigated by Yu and Zhu in connection with smooth quintic surfaces containing eighty-five lines. The affine smoothness criterion \(t\notin\{0,1\}\) was proved by Yu and Zhu (Lemma 3.1). The new classification is the **complete singularity basket and its topological and resolution invariants** at those two boundary parameters:

1. For \(t\notin\{0,1\}\), \(X_t\) is smooth.
2. At \(t=0\), \(X_0\) has precisely one singular point, \(P=[0:0:1:0]\). It is an ordinary quadruple point with smooth projectivized tangent cone
   \[
   Q=V(x^4-6x^2y^2-3y^4+w^4)\subset\mathbb P^2.
   \]
   Its Milnor number is \(27\). The blow-up at \(P\) resolves the singularity, with exceptional smooth genus-three quartic \(E\) satisfying \(E^2=-4\) and discrepancy \(-2\).
3. At \(t=1\), \(X_1\) has precisely **twenty-four ordinary double points** (type \(A_1\)), grouped into three sets of eight according to \(w/z\in\{1,\omega,\omega^2\}\), where \(\omega^2+\omega+1=0\). All are on the affine chart \(z=1\); their complete equations are
   \[
   \begin{array}{ll}
   w=1,\ x=0,\ y^4=-1 &(4\text{ points}),\\
   w=1,\ y=0,\ x^4=3 &(4\text{ points}),\\
   w=\rho,\ 4y^4=\rho^2,\ x^2=(\rho-\rho^2)y^2,
      &\rho\in\{\omega,\omega^2\}\quad(8\text{ points for each }\rho).
   \end{array}
   \]
   These points have nondegenerate quadratic tangent cones.

The topological Euler characteristics of the two singular fibers are
\[
\chi_{\mathrm{top}}(X_0)=28,\qquad
\chi_{\mathrm{top}}(X_1)=31,
\]
compared with \(\chi_{\mathrm{top}}(X_t)=55\) for a smooth quintic surface. If the pencil is compactified over \(\mathbb P^1\), its fiber at \(t=\infty\) is the nonreduced divisor \(4\{z=0\}+\{w=0\}\); thus the complete bad-fiber support in the compactified base is \(\{0,1,\infty\}\).

## Assumptions and scope

All assertions are over \(\mathbb C\), for the displayed homogeneous equation in the indicated coordinates. A singular point is a common projective zero of all four partial derivatives of \(F_t\). An ordinary quadruple point means an isolated multiplicity-four surface hypersurface singularity with smooth degree-four projectivized tangent cone. An ordinary double point means a nondegenerate quadratic singularity of a complex surface. The Euler characteristic is that of the underlying complex analytic space. The compactified pencil has homogeneous base parameters \([s:u]\) and equation \(sF_0-u z^4w=0\).

## Proof

### Step 1: Exhaust all projective critical points

The four partial derivatives are
\[
\begin{aligned}
(F_t)_x&=4x\bigl(x^2(z-w)-3y^2(z+w)\bigr),\\
(F_t)_y&=-12y\bigl(y^2(z-w)+x^2(z+w)\bigr),\\
(F_t)_z&=x^4-3y^4-6x^2y^2+w^4-4tz^3w,\\
(F_t)_w&=-x^4+3y^4-6x^2y^2+4zw^3-tz^4.
\end{aligned}
\]
By Euler's identity, simultaneous vanishing of the partials already implies \(F_t=0\).

If \(x=y=0\), then \((F_t)_z=w^4-4tz^3w\) and \((F_t)_w=4zw^3-tz^4\). If \(zw\ne0\), these would give \(w^3=4tz^3\) and \(4w^3=tz^3\), hence \(15tz^3=0\), a contradiction unless \(t=w=0\). The chart \(z=0\) gives \((F_t)_z=w^4\ne0\). Therefore the only singular point with \(x=y=0\) is \(P=[0:0:1:0]\) at \(t=0\).

If \(x=0\), \(y\ne0\), the equation \((F_t)_y=0\) gives \(z=w\). Neither can vanish, since then \((F_t)_z=-3y^4\ne0\). Substituting \(z=w\ne0\) into the remaining derivatives gives \(5(1-t)z^4=0\) and, when \(t=1\), \(y^4=-z^4\). These yield exactly four points. Likewise \(y=0\), \(x\ne0\) yields \(z=w\ne0\), \(t=1\), \(x^4=3z^4\), hence four further points.

Finally suppose \(xy\ne0\). The first two partial equations force \(z-w\ne0\) and \(z+w\ne0\), because otherwise both vanish and \(z=w=0\), which is ruled out by the last two derivatives. Set \(h=(z-w)/(z+w)\). Multiplication of the two equations gives \(h^2=-3\), while either equation gives \(x^2=-hy^2\). Hence \(x^4-3y^4=-6y^4\) and \(x^2y^2=-hy^4\), so that the first two summands in \(F_t\) cancel. Thus \(F_t=zw(w^3-tz^3)\). Since \(h^2=-3\) precludes \(zw=0\), writing \(\rho=w/z\) gives \(\rho^2+\rho+1=0\) and \(t=\rho^3=1\). On \(z=1\), \(h=\rho^2-\rho\), and \((F_t)_z=0\) becomes \(4y^4=\rho^2\); also \(x^2=(\rho-\rho^2)y^2\). For each of the two primitive cube roots \(\rho\), there are exactly four choices of \(y\) and two of \(x\), all distinct. This supplies sixteen points, and exhausts all cases.

### Step 2: Verify the singularity types

At \(t=1\), put \(z=1\). The affine equation is
\[
f(x,y,w)=(1-w)(x^4-3y^4)-6(1+w)x^2y^2+w(w^3-1).
\]
A direct exact differentiation shows that the determinant of its \(3\times3\) Hessian is \(3456\) at each of the eight points with \(w=1\), and \(3456\rho^2\) at each of the eight points with \(w=\rho\), for each \(\rho\in\{\omega,\omega^2\}\). Each determinant is nonzero. The complex analytic Morse lemma therefore identifies every singularity as an ordinary double point. The file `verify.py` checks these identities by reducing the exact Hessian determinant modulo the three sets of defining polynomial relations.

At \(t=0\), on \(z=1\) the local equation at \(P\) is
\[
f_0(x,y,w)=x^4-6x^2y^2-3y^4+w^4
-w(x^4+6x^2y^2-3y^4).
\]
The degree-four tangent cone polynomial \(Q=x^4-6x^2y^2-3y^4+w^4\) has gradient
\[
Q_x=4x(x^2-3y^2),\quad
Q_y=-12y(x^2+y^2),\quad
Q_w=4w^3.
\]
A common projective zero must satisfy \(w=0\). For \(xy\ne0\), it would require both \(x^2=3y^2\) and \(x^2=-y^2\), an impossibility; the cases \(x=0\) or \(y=0\) are equally impossible. Thus \(Q=0\) is a smooth plane quartic. The blow-up at the origin resolves the ordinary quadruple point; its exceptional curve is \(Q\) of genus \((4-1)(4-2)/2=3\), and has normal bundle \(\mathcal O_Q(-1)\), hence self-intersection \(-4\). Adjunction for blowing up a multiplicity-four hypersurface in a smooth threefold gives discrepancy \(2-4=-2\). Finally the ordinary-multiple-point Milnor formula gives \(\mu=(4-1)^3=27\). Equivalently, the three homogeneous partial derivatives of \(Q\) form a regular sequence of cubics whose quotient has dimension \(27\); the order-five terms do not change this Milnor number.

### Step 3: Euler characteristics and the fiber at infinity

The standard Chern-class formula for a smooth degree-\(d\) surface in \(\mathbb P^3\) is \(\chi_{\mathrm{top}}=d(d^2-4d+6)\). At \(d=5\) this equals \(55\). For an isolated hypersurface singularity of a complex surface, the change in Euler characteristic from a smoothing is its Milnor number. Consequently \(\chi_{\mathrm{top}}(X_0)=55-27=28\), and \(\chi_{\mathrm{top}}(X_1)=55-24=31\). The homogeneous pencil equation \(sF_0-u z^4w=0\) gives its fiber at \([s:u]=[0:1]\) as \(z^4w=0\), as claimed.

## Verification

Run `python verify.py` with SymPy installed. It checks homogeneity and all four gradient identities over \(\mathbb Q\), verifies exact vanishing of the affine polynomial and all its derivatives at the three families of singular points, and reduces the Hessian determinants to their claimed nonzero values modulo the corresponding zero-dimensional ideals. It additionally verifies the tangent-cone formula and the length-\(27\) standard-monomial basis of the homogeneous tangent-cone Jacobian algebra. Expected output begins with `VERIFY_OK`. These algebraic checks corroborate, but do not replace, the exhaustive case analysis or the standard singularity-theoretic theorems used above.

## Relationship to prior work

Yu and Zhu introduce the displayed quintic pencil to obtain smooth quintics with eighty-five lines and exhibit a member with Picard number forty-three (arXiv:2609.26862v1). **Their Lemma 3.1 already proves that the affine pencil is smooth exactly when \(t\notin\{0,1\}\); this smoothness criterion is not claimed as new.** Their complete accessible arXiv HTML manuscript, especially Section 3.1 and the later sections on lines and Picard groups, was inspected. It does not give the twenty-four-node count or the local ordinary-quadruple-point type, Milnor numbers, exceptional resolution, or the Euler characteristics derived here. The present contribution is these complete singularity baskets and associated invariants, not the exceptional parameter set. A secondary review reproduces the pencil equation. A separately published calculation of the incidence-graph spectrum of the eighty-five lines on the smooth \(t=-1/8\) fiber concerns different invariants and has no logical implication to the above singularity classification.

## Limitations

The result concerns this exact pencil in characteristic zero, not a general pencil of quintics or other finite characteristics. It classifies singularities of the surface fibers and their smoothings; it does not classify their limiting line schemes, monodromy representations, Néron–Severi lattices, or the singularities of the total threefold of the pencil. The original arXiv HTML text was inspected for overlap, although historical priority beyond the inspected sources remains provisional. An independent mathematical review has not been performed. No claim of exhaustive historical priority is made.

## References

1. X. Yu and Z. Zhu, *A smooth quintic surface with 85 lines and Picard number 43*, arXiv:2609.26862v1, first public September 22, 2026. https://arxiv.org/abs/2609.26862
2. *Literature Review: A smooth quintic surface with 85 lines and Picard number 43*, Moonlight; displays the defining pencil. https://www.themoonlight.io/en/review/a-smooth-quintic-surface-with-85-lines-and-picard-number-43
3. J. Milnor, *Singular Points of Complex Hypersurfaces*, Annals of Mathematics Studies 61, Princeton University Press, 1968. Standard isolated-hypersurface singularity and Milnor-fiber facts.
