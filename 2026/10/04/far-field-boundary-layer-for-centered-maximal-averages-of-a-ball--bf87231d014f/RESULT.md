# Far-field boundary layer for centered maximal averages of a ball

## Finding

Let \(n\ge4\), let \(U=B(0,1)\subset\mathbb R^n\), and define the centered Hardy--Littlewood maximal function
\[
M_c\mathbf 1_U(x)
=
\sup_{\rho>0}
\frac{|U\cap B(x,\rho)|}{\omega_n\rho^n},
\]
where \(\omega_k\) denotes the volume of the Euclidean unit ball in \(\mathbb R^k\).

For \(R>1\), put
\[
x_R=Re_1,\qquad B_R=R+1,
\]
and let \(\rho_R\) be any radius attaining the supremum at \(x_R\). Define
\[
c_n
=
\left(
\frac{n\omega_n}
{2^{(n-1)/2}\omega_{n-1}}
\right)^{2/(n-1)}
\]
and
\[
\kappa_n
=
\frac{n(n-1)}{n+1}c_n.
\]
Then
\[
B_R-\rho_R
=
c_n B_R^{-2/(n-1)}(1+o(1)),
\]
and
\[
M_c\mathbf 1_U(x_R)
=
B_R^{-n}
\left[
1+\kappa_n B_R^{-(n+1)/(n-1)}
+o\!\left(B_R^{-(n+1)/(n-1)}\right)
\right]
\]
as \(R\to\infty\).

Equivalently, the far-field maximizing averaging ball clips a vanishing spherical cap from \(U\), and the cap depth has the exact boundary-layer scale \(B_R^{-2/(n-1)}\).

## Assumptions and scope

The result concerns the Euclidean centered Hardy--Littlewood maximal operator and the characteristic function of the Euclidean unit ball. The dimension restriction \(n\ge4\) is intentional: the motivating paper gives an explicit closed formula for \(M_c\mathbf 1_U\) in dimension three, whereas in arbitrary dimension it gives the underlying two-ball intersection formula.

No statement is made here about arbitrary radial inputs, arbitrary convex bodies, uncentered maximal functions, or finite-\(R\) uniqueness of the maximizing radius. The asymptotic conclusion holds for every choice of maximizing radius.

## Proof

For fixed \(R>1\), radii \(\rho<R-1\) miss \(U\), while for \(\rho\ge R+1\) the whole unit ball is contained and the average equals \(\rho^{-n}\), which is decreasing. Hence a maximizing radius exists in
\[
[R-1,R+1].
\]
Write
\[
B=R+1,\qquad
\delta=B-\rho\in[0,2].
\]
Let \(L_R(\delta)\) be the part of \(U\) missed by \(B(Re_1,B-\delta)\). Then
\[
\frac{|U\cap B(Re_1,B-\delta)|}
{\omega_n(B-\delta)^n}
=
B^{-n}
\left(1-\frac{L_R(\delta)}{\omega_n}\right)
\left(1-\frac{\delta}{B}\right)^{-n}.
\]

We first obtain the small-cap asymptotic uniformly in the regime relevant to maximization. Use coordinates
\[
y=-e_1+(u,z),
\qquad
0\le u\le2,
\qquad
z\in\mathbb R^{n-1}.
\]
The unit ball condition is
\[
|z|^2\le2u-u^2.
\]
A point is outside the averaging ball exactly when
\[
(B-u)^2+|z|^2>(B-\delta)^2,
\]
or
\[
|z|^2
>
2B(u-\delta)-u^2+\delta^2.
\]
For \(0\le u<\delta\), the entire unit-ball cross-section is missed. The two cross-section boundaries meet at
\[
u_*
=
\frac{2B\delta-\delta^2}{2(B-1)}
=
\delta+O\!\left(\frac{\delta}{R}\right).
\]
Thus the fully missed spherical cap \(0\le u\le\delta\) supplies the main term, while the transition strip \(\delta\le u\le u_*\) has width \(O(\delta/R)\).

Put
\[
q=\frac{n+1}{2}.
\]
The cap volume is
\[
\omega_{n-1}
\int_0^\delta
(2u-u^2)^{(n-1)/2}\,du
=
C_n\delta^q
\left(1+O(\delta)\right),
\]
where
\[
C_n
=
\frac{2^{(n+1)/2}\omega_{n-1}}{n+1}.
\]
The transition strip contributes
\[
O\!\left(\frac{\delta^q}{R}\right).
\]
Consequently
\[
L_R(\delta)
=
C_n\delta^q
\left(1+O(\delta)+O(R^{-1})\right)
\]
whenever \(\delta=o(1)\).

Let
\[
a_n=\frac{C_n}{\omega_n}.
\]
For \(\delta=o(1)\),
\[
\left(1-\frac{L_R(\delta)}{\omega_n}\right)
\left(1-\frac{\delta}{B}\right)^{-n}
=
1+\frac{n\delta}{B}
-a_n\delta^q
+o\!\left(\frac{\delta}{B}+\delta^q\right).
\]

A maximizing \(\delta_R=B-\rho_R\) must satisfy \(\delta_R\to0\). Indeed, if \(\delta\) stays bounded below by a positive number, then in the far-field limit the missed cap has a fixed positive volume fraction, whereas \(\delta=0\) gives the full-ball average \(B^{-n}\).

Now introduce the boundary-layer scale
\[
\delta=tB^{-2/(n-1)}.
\]
Since
\[
q-1=\frac{n-1}{2},
\]
the two leading corrections have the same order:
\[
\frac{\delta}{B}
\asymp
\delta^q
\asymp
B^{-(n+1)/(n-1)}.
\]
Uniformly for \(t\) in compact subsets of \([0,\infty)\),
\[
B^{(n+1)/(n-1)}
\left[
B^n
\frac{|U\cap B(Re_1,B-\delta)|}
{\omega_n(B-\delta)^n}
-1
\right]
\longrightarrow
G_n(t),
\]
where
\[
G_n(t)=nt-a_nt^q.
\]

The maximizer cannot have \(t\to0\), because \(G_n\) is positive at its positive maximizer. It cannot have \(t\to\infty\): the elementary cap lower bound \(L_R(\delta)\ge c\,\delta^q\) makes the negative cap term dominate \(n\delta/B\) once
\[
\delta B^{2/(n-1)}\to\infty.
\]
Hence maximizing scaled parameters remain in a compact subset of \((0,\infty)\), and the uniform limit reduces the problem to maximizing \(G_n\).

The function \(G_n\) has a unique positive maximizer \(c_n\), determined by
\[
a_nq\,c_n^{q-1}=n.
\]
Since
\[
a_nq
=
2^{(n-1)/2}\frac{\omega_{n-1}}{\omega_n},
\]
this gives
\[
c_n
=
\left(
\frac{n\omega_n}
{2^{(n-1)/2}\omega_{n-1}}
\right)^{2/(n-1)}.
\]
Therefore
\[
\delta_R
=
c_nB^{-2/(n-1)}(1+o(1)).
\]

Finally,
\[
G_n(c_n)
=
nc_n-\frac{n}{q}c_n
=
\frac{n(n-1)}{n+1}c_n
=
\kappa_n.
\]
Substitution into the scaled expansion proves the asserted asymptotic for \(M_c\mathbf 1_U(x_R)\).

## Verification

The proof is analytic. The critical checks are:

1. the exact cross-section inequalities for the two balls;
2. the crossing point
\[
u_*=\frac{2B\delta-\delta^2}{2(B-1)};
\]
3. the cap coefficient
\[
C_n=\frac{2^{(n+1)/2}\omega_{n-1}}{n+1};
\]
4. the balance
\[
\delta/B\asymp\delta^{(n+1)/2},
\]
which forces the exponent \(2/(n-1)\);
5. the unique maximizer of the limiting profile \(G_n(t)=nt-a_nt^{(n+1)/2}\).

Numerical quadrature was used only as a stress test, not as evidence for the infinite-dimensional statement. For \(n=4\), for example, the predicted optimizer constant is approximately \(1.4053918332\), and direct numerical maximization for \(R=200\) gives a scaled ratio within about \(2.2\%\) of one; the discrepancy decreases as \(R\) grows.

## Relationship to prior work

Solyanik's recent paper studies the centered maximal operator in every dimension, proves noninjectivity, gives an explicit formula for \(M_c\mathbf 1_U\) in \(\mathbb R^3\), and derives a general incomplete-beta formula for intersections of two Euclidean balls. The present result takes the higher-dimensional unit-ball intersection geometry in a different direction: it asymptotically solves the radius optimization problem in every dimension \(n\ge4\), including the exact boundary-layer exponent and leading constants.

The literature searches also covered centered Hardy--Littlewood maximal constants, indicator-ball behavior, maximizing-radius formulations, and far-field asymptotics. No located statement gave the higher-dimensional optimizer law or the two-term maximal-value asymptotic above.

The full primary text of the motivating preprint could not be retrieved in this run despite bounded attempts through the preprint endpoint, open-access mirrors, and institutional retrieval. Its primary abstract and detailed public review were inspected, and targeted searches for the proposed asymptotic returned no matching statement. This access limitation is retained as an originality risk rather than treated as evidence of novelty.

## Limitations

The theorem is asymptotic as \(R\to\infty\) and does not provide a uniform finite-\(R\) error bound. It does not prove uniqueness of \(\rho_R\) for each finite \(R\).

Dimension three is excluded because the motivating source already supplies an explicit formula for the full unit-ball maximal function there. The result does not claim that the same constants persist for other convex bodies or other radial profiles.

The inaccessible full text of the motivating preprint leaves a residual literature-comparison risk: an equivalent higher-dimensional asymptotic could conceivably appear in a part of that paper not visible through the retrieved materials.

## References

1. A. Solyanik, *On the Central Maximal Function in \(\mathbb R^n\)*, arXiv:2609.27687v1, 2026.
2. A. D. Melas, *The best constant for centered Hardy--Littlewood maximal inequality*, Ann. of Math. 157 (2003), 647--688.
3. P. Ivanisvili and S. Zbarsky, *Centered Hardy--Littlewood maximal operator on the real line: Lower bounds*, C. R. Math. Acad. Sci. Paris 357 (2019), 339--344.
