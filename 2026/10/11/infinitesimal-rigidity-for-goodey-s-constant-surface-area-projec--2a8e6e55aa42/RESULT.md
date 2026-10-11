# Infinitesimal rigidity for Goodey's constant-surface-area projection problem
## Finding
Let
\[
B^4\subset\mathbb R^4
\]
be the unit ball. For
\[
f\in C^2(S^3),
\]
put
\[
h_{\varepsilon,f}(v)=1+\varepsilon f(v).
\]
For every fixed \(f\), this is the support function of a smooth strictly convex body \(K_{\varepsilon,f}\) whenever \(|\varepsilon|\) is sufficiently small.

For
\[
u\in S^3,
\]
let
\[
\mathcal S_f(u)
=
\left.
\frac{d}{d\varepsilon}
\operatorname{Area}_2\!\left(
\partial(K_{\varepsilon,f}|u^\perp)
\right)
\right|_{\varepsilon=0},
\]
where the projected body is three-dimensional. For
\[
E\in G(4,2),
\]
let
\[
\mathcal A_f(E)
=
\left.
\frac{d}{d\varepsilon}
\operatorname{Area}_2(K_{\varepsilon,f}|E)
\right|_{\varepsilon=0}.
\]

Then the two first variations are
\[
\mathcal S_f(u)
=
2\int_{S^3\cap u^\perp}f(v)\,d\omega_2(v)
\]
and
\[
\mathcal A_f(E)
=
\int_{S^3\cap E}f(v)\,d\omega_1(v).
\]

Therefore, for any
\[
f,g\in C^2(S^3),
\]
\[
\mathcal S_f(u)=\mathcal S_g(u)
\quad\text{for every }u\in S^3
\]
implies
\[
\mathcal A_f(E)=\mathcal A_g(E)
\quad\text{for every }E\in G(4,2).
\]

In the language of the 2009 open problem, the noninjective Grassmann Radon transform
\[
C(G(4,2))\longrightarrow C(G(4,3))
\]
becomes injective when restricted to the tangent range of planar projection-area functions at the ball.

More precisely, the kernel of the first surface-projection data is exactly the odd perturbations:
\[
\mathcal S_f\equiv0
\quad\Longleftrightarrow\quad
f(-v)=-f(v).
\]
Every such perturbation also satisfies
\[
\mathcal A_f\equiv0.
\]
Thus the ambient Radon-kernel obstruction identified in the open problem is absent to first order at the ball.

## Assumptions and scope
All support functions are taken with respect to the origin. The sphere \(S^3\) has radius \(1\). The measures \(d\omega_2\) and \(d\omega_1\) are the ordinary surface and arclength measures on the corresponding great \(2\)-sphere and great circle.

For a smooth support function \(h\) on \(S^3\), strict convexity of the associated body is equivalent to positive definiteness of
\[
\nabla_{S^3}^2h+h\,g_{S^3}.
\]
At
\[
h\equiv1
\]
this tensor is the identity. Hence every fixed \(C^2\) direction \(f\) gives a strictly convex body for all sufficiently small \(|\varepsilon|\).

The conclusion is an infinitesimal statement at the ball. It does not prove the full nonlinear implication in Problem 4, nor does it rule out a counterexample whose first nonzero discrepancy occurs at quadratic or higher order.

## Proof
Orthogonal projection restricts support functions. Thus the support function of
\[
K_{\varepsilon,f}|E
\]
on the great circle
\[
S^3\cap E
\]
is simply
\[
1+\varepsilon f|_{S^3\cap E}.
\]

For a planar convex body with \(C^2\) support function \(h\), the area formula is
\[
\operatorname{Area}_2
=
\frac12
\int_{S^1}
\left(h^2-(h')^2\right)\,d\theta.
\]
Substituting
\[
h=1+\varepsilon f
\]
and differentiating at \(\varepsilon=0\) gives
\[
\mathcal A_f(E)
=
\int_{S^3\cap E}f\,d\omega_1.
\tag{1}
\]

Now fix
\[
u\in S^3.
\]
The projection
\[
K_{\varepsilon,f}|u^\perp
\]
is a three-dimensional convex body whose support function on the equatorial sphere
\[
S^3\cap u^\perp\cong S^2
\]
is again the restriction of \(1+\varepsilon f\).

For a smooth strictly convex body in \(\mathbb R^3\), the surface-area density in support coordinates is
\[
\det\!\left(\nabla_{S^2}^2h+hI\right).
\]
At
\[
h=1+\varepsilon f,
\]
\[
\nabla_{S^2}^2h+hI
=
I+\varepsilon\left(\nabla_{S^2}^2f+fI\right).
\]
The derivative of the determinant at the identity is the trace, so
\[
\left.
\frac{d}{d\varepsilon}
\det\!\left(\nabla_{S^2}^2h+hI\right)
\right|_{\varepsilon=0}
=
\Delta_{S^2}f+2f.
\]
Integrating over the closed sphere kills the Laplacian term. Therefore
\[
\mathcal S_f(u)
=
2\int_{S^3\cap u^\perp}f\,d\omega_2.
\tag{2}
\]

It remains to determine the kernel of the transform in (2). Define the equatorial Funk transform on \(S^3\) by
\[
(Ff)(u)
=
\int_{S^3\cap u^\perp}f\,d\omega_2.
\]
By the Funk--Hecke theorem, on spherical harmonics of degree \(\ell\),
\[
F
=
4\pi
\frac{C_\ell^1(0)}{C_\ell^1(1)}
\]
times the identity. Here \(C_\ell^1\) is the Gegenbauer polynomial with parameter \(1\). The elementary identity
\[
C_\ell^1(\cos t)
=
\frac{\sin((\ell+1)t)}{\sin t}
\]
gives
\[
C_\ell^1(0)
=
\sin\!\left(\frac{(\ell+1)\pi}{2}\right).
\]
Also,
\[
C_\ell^1(1)=\ell+1.
\]
Hence the Funk multiplier vanishes exactly for odd \(\ell\), and it is nonzero for every even \(\ell\).

Therefore
\[
Ff=0
\]
if and only if all even spherical-harmonic components of \(f\) vanish, which is equivalent to
\[
f(-v)=-f(v).
\tag{3}
\]

Now suppose
\[
\mathcal S_f=\mathcal S_g.
\]
Applying (2) to
\[
q=f-g
\]
gives
\[
Fq=0.
\]
By (3), \(q\) is odd. Every great circle
\[
S^3\cap E
\]
is invariant under the antipodal map, so the integral of \(q\) around that circle vanishes. Equation (1) then yields
\[
\mathcal A_f(E)-\mathcal A_g(E)
=
\int_{S^3\cap E}q\,d\omega_1
=
0
\]
for every
\[
E\in G(4,2).
\]
This proves the implication.

The same argument says geometrically that the derivative of the planar projection-area map has a range on which the Grassmann Radon transform in Problem 4 is injective: a tangent projection-area function in the ambient Radon kernel must already be zero.

## Verification
The supplied `verify.py` is replayed from the packaged source.

It verifies symbolically that for a \(2\times2\) matrix perturbation
\[
I+\varepsilon M,
\]
the coefficient of \(\varepsilon\) in the determinant is
\[
\operatorname{tr}M.
\]
This is the algebraic step behind the three-dimensional surface-area variation.

It also generates the Gegenbauer polynomials \(C_\ell^1\) by their exact recurrence and checks the closed identities
\[
C_{2m}^1(0)=(-1)^m,
\qquad
C_{2m+1}^1(0)=0
\]
over a regression range. The universal identity used in the proof is established analytically from
\[
C_\ell^1(\cos t)=\frac{\sin((\ell+1)t)}{\sin t};
\]
the finite checks are not used as an infinite proof.

Finally, the checker verifies the planar support-area first variation on a trigonometric polynomial symbolically and confirms that every odd Fourier mode has zero great-circle average.

## Relationship to prior work
Problem 4 of the 2009 Banach Center Open Problem Session asks whether equality of the surface areas of all three-dimensional orthogonal projections of two convex bodies in \(\mathbb R^4\) forces equality of the areas of all their two-dimensional projections. The problem explicitly notes that the relevant Radon transform
\[
C(G(4,2))\to C(G(4,3))
\]
is not injective on the ambient function space and identifies the restricted nature of projection-area functions as the central issue.

Goodey's 2009 survey develops the projection-function and Grassmann-Radon framework underlying that question and records primary MSC \(52A20\). It discusses the role of spherical harmonics and transform kernels in geometric determination problems, but does not state the tangent-range theorem above.

Goodey's 1998 paper proves that Radon transforms of projection functions determine centrally symmetric bodies and polytopes under broad hypotheses. Its full harmonic-analysis proof describes the kernels of Grassmann Radon transforms on irreducible components. That global theorem does not imply the present differential statement for arbitrary asymmetric perturbations: the first-order premise annihilates the even part of an arbitrary support perturbation, while the surviving odd part is simultaneously invisible to the planar projection-area differential.

Targeted searches for a ball linearization of Problem 4, first variations of its two projection data sets, tangent-range injectivity, and the corresponding Funk-transform formulation did not locate the displayed theorem.

## Limitations
This result is first-order only. It does not establish local nonlinear uniqueness near the ball.

Odd support perturbations are invisible to both data sets at first order, so a possible nonlinear obstruction can begin at second order. No second-order classification is claimed.

The theorem is specialized to the four-dimensional ball and the pair of projection invariants appearing in Problem 4. It does not assert the analogous tangent-range implication for every dimension and every intrinsic-volume index.

The harmonic ingredients are classical, and an equivalent tangent-space observation may exist implicitly in older geometric-tomography literature even though the inspected sources and targeted searches did not state it.

## References
1. *Open Problem Session*, Banach Center Publications 84 (2009), 217--222, Problem 4.
2. P. Goodey, *The determination of convex bodies from the size and shape of their projections and sections*, Banach Center Publications 84 (2009), 13--30. DOI: 10.4064/bc84-0-1.
3. P. Goodey, *Radon transforms of projection functions*, Mathematical Proceedings of the Cambridge Philosophical Society 123 (1998), 159--168. DOI: 10.1017/S0305004197001928.
