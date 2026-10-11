# Three barriers determine the Euclidean inradius of rational-linear-precision prismatoids
## Finding
Let
\[
a,a',b,b',l\in\mathbb Z_{>0},
\qquad
d\in\mathbb Z_{\ge0},
\qquad
a'\le a,
\qquad
b'\le b.
\]
Consider the three-dimensional prismatoid introduced by Davies, Duarte, Portakal, and Sorea,
\[
P=
l\,\operatorname{conv}\!\left(
T_{a,b,d}\times\{0\},
T_{a',b',d}\times\{1\}
\right)
\subset\mathbb R^3,
\tag{1}
\]
where \(T_{a,b,d}\) is their trapezoidal Newton polytope.

Put
\[
A=a+db,
\qquad
A'=a'+db',
\qquad
\Delta_A=A-A',
\qquad
\Delta_b=b-b',
\tag{2}
\]
and
\[
N_A=\sqrt{1+d^2+\Delta_A^2},
\qquad
N_b=\sqrt{1+\Delta_b^2}.
\tag{3}
\]

Then the Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}(P)
=
l\min\!\left\{
\frac12,\,
\frac{b}{1+\Delta_b+N_b},\,
\frac{A}{1+d+\Delta_A+N_A}
\right\}.
}
\tag{4}
\]

Writing
\[
r=r_{\mathrm{in}}(P),
\]
the complete set of incenters is
\[
\boxed{
\begin{aligned}
\operatorname{Cent}(P)=
\bigl\{(s,t,v):\;&
s\ge r,\quad t\ge r,\quad v\ge r,\quad v\le l-r,\\
&
t+\Delta_bv\le bl-rN_b,\\
&
s+dt+\Delta_Av\le Al-rN_A
\bigr\}.
\end{aligned}
}
\tag{5}
\]

In particular,
\[
\boxed{(r,r,r)}
\tag{6}
\]
is always an incenter.

At the canonical center (6), the three coordinate facets are always tangent. The other tangencies are controlled by exactly three competing barriers:
\[
\frac l2,
\qquad
\frac{bl}{1+\Delta_b+N_b},
\qquad
\frac{Al}{1+d+\Delta_A+N_A}.
\tag{7}
\]
The first corresponds to the upper facet, the second to the back facet, and the third to the right facet. If two or three barrier values tie, the corresponding facet families are tangent simultaneously.

## Assumptions and scope
The realization and coordinates are exactly those used for the prismatoid family in the source. The metric is the standard Euclidean metric of \(\mathbb R^3\).

The strict positivity of
\[
a,a',b,b',l
\]
ensures the two displayed bases are genuine trapezoids and the prismatoid is full-dimensional with the six source facets. The parameter \(d\) may vanish.

No affine invariance is asserted. In particular, rational linear precision and lattice equivalence do not determine Euclidean inradius.

The formula concerns the six-facet prismatoids in the source family. Degenerations in which a top or side facet collapses require deleting the redundant inequality before interpreting tangency, although the limiting numerical expression can still be taken when appropriate.

## Proof
The source gives the six facet-distance functions
\[
h_1=s,
\qquad
h_2=t,
\qquad
h_3=v,
\tag{8}
\]
\[
h_4=Al-s-dt-\Delta_Av,
\tag{9}
\]
\[
h_5=bl-t-\Delta_bv,
\qquad
h_6=l-v.
\tag{10}
\]
Thus
\[
P=\{(s,t,v):h_i(s,t,v)\ge0,\ 1\le i\le6\}.
\tag{11}
\]

The inward facet normals are
\[
n_1=(1,0,0),\quad
n_2=(0,1,0),\quad
n_3=(0,0,1),
\tag{12}
\]
\[
n_4=(-1,-d,-\Delta_A),
\quad
n_5=(0,-1,-\Delta_b),
\quad
n_6=(0,0,-1).
\tag{13}
\]
Therefore
\[
\|n_1\|=\|n_2\|=\|n_3\|=\|n_6\|=1,
\quad
\|n_4\|=N_A,
\quad
\|n_5\|=N_b.
\tag{14}
\]

A radius-\(\rho\) Euclidean ball centered at
\[
c=(s,t,v)
\]
is contained in \(P\) exactly when every normalized facet clearance is at least \(\rho\). Equations (8)--(14) give
\[
s\ge\rho,\qquad
t\ge\rho,\qquad
v\ge\rho,
\tag{15}
\]
\[
Al-s-dt-\Delta_Av\ge\rho N_A,
\tag{16}
\]
\[
bl-t-\Delta_bv\ge\rho N_b,
\qquad
l-v\ge\rho.
\tag{17}
\]

Because
\[
d,\Delta_A,\Delta_b\ge0,
\]
the left sides of (16) and the first inequality in (17) weakly increase when any of \(s,t,v\) is decreased. Hence, if some center satisfies (15)--(17), then the diagonal center
\[
(\rho,\rho,\rho)
\]
also satisfies them.

Therefore a radius \(\rho\) is feasible if and only if the diagonal center is feasible. Substituting
\[
s=t=v=\rho
\]
into (16)--(17) yields exactly
\[
2\rho\le l,
\tag{18}
\]
\[
(1+\Delta_b+N_b)\rho\le bl,
\tag{19}
\]
and
\[
(1+d+\Delta_A+N_A)\rho\le Al.
\tag{20}
\]
The largest feasible \(\rho\) is the minimum of the three right-hand ratios, proving (4).

Finally, after \(r\) is fixed at its optimal value, a point is an incenter exactly when a radius-\(r\) ball centered there satisfies all six normalized facet inequalities. Rewriting (15)--(17) at \(\rho=r\) gives precisely (5).

The tangency statement follows by evaluating the six normalized clearances at the canonical center \((r,r,r)\). The coordinate-facet clearances are all exactly \(r\), while each of the remaining three equals \(r\) exactly when its corresponding barrier in (7) is active.

## Verification
The proof is symbolic for the full stated parameter range.

The source-dependent inputs were checked directly in the open-access full text: the family is the convex hull of two trapezoids, dilated by \(l\); Proposition 3.2 gives the six linear facet-distance functions; and Notation 3.2 gives the corresponding six facet normals.

The accompanying `verify.py` checks several hundred deterministic positive integer parameter choices. It independently solves the four-variable Chebyshev linear program for
\[
(s,t,v,\rho)
\]
by enumerating active constraint sets and Gaussian elimination, and compares the resulting optimum with (4). It also checks that (5) is exactly the shifted-facet feasibility system. These finite computations are corroborative only.

## Relationship to prior work
Davies, Duarte, Portakal, and Sorea introduced the higher-dimensional rational-linear-precision family and isolated the prismatoids (1) as a structured three-dimensional subfamily. Their analysis uses the six facet-distance functions to construct Horn pairs and to study primitive collections of the normal fan.

The source does not state a Euclidean inradius, largest-inscribed-ball, or Chebyshev-center theorem. The metric normalization is additional: the two slanted facet functions must be divided by the Euclidean norms
\[
N_A
\quad\text{and}\quad
N_b.
\]

The resulting optimization has an exact monotonicity collapse. Although a generic six-facet Chebyshev problem has four variables, every feasible center at radius \(\rho\) can be pushed coordinatewise to \((\rho,\rho,\rho)\) without decreasing any upper-facet clearance. This converts the entire family into the three-barrier formula (4), while (5) retains the full nonuniqueness information for optimal centers.

Targeted searches under “rational linear precision prismatoid”, “multinomial staged tree polytope”, “inradius”, “largest inscribed ball”, “Chebyshev center”, and “trapezoidal frustum” did not locate a theorem implying (4)--(5).

## Limitations
The theorem covers the full-dimensional six-facet prismatoids of the source family, not arbitrary prismatoids.

It does not determine the minimum enclosing sphere, John or Löwner ellipsoids, or radii for the higher-dimensional multinomial staged-tree polytopes.

The proof uses the monotone sign pattern of the three source upper facets. A general prismatoid need not admit the same diagonal reduction.

A broader theorem on Chebyshev centers of monotone H-polytopes could subsume the calculation under different terminology. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Isobel Davies, Eliana Duarte, Irem Portakal, and Miruna-Ştefana Sorea, *Families of Polytopes with Rational Linear Precision in Higher Dimensions*, arXiv:2109.08151, first public version 2021-09-16; *Foundations of Computational Mathematics* 23 (2023), 2151--2202, DOI 10.1007/s10208-022-09583-7.
