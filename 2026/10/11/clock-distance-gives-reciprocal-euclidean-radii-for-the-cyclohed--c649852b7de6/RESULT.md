# Clock distance gives reciprocal Euclidean radii for the cyclohedral Lipschitz–KR pair
## Finding
Let
\[
n\ge3
\]
and let
\[
H_0
=
\left\{
x\in\mathbb R^n:
\sum_{i=1}^n x_i=0
\right\}.
\tag{1}
\]
For distinct cyclic labels \(i,j\), let
\[
d(i,j)\in\{1,\ldots,n-1\}
\]
be the clockwise distance from \(i\) to \(j\).

Jevtić, Jelić, and Živaljević define the clock quasi-metric
\[
\rho(i,j)
=
d(i,j)\frac{n^2-n+1}{n}
-
\frac{d(i,j)(d(i,j)+1)}2.
\tag{2}
\]
Choose the zero-mean representative of the corresponding Lipschitz polytope:
\[
L_n
=
\left\{
x\in H_0:
x_i-x_j\le\rho(i,j)
\quad(i\ne j)
\right\}.
\tag{3}
\]
Its polar in \(H_0\) is the Kantorovich--Rubinstein polytope
\[
K_n
=
\operatorname{conv}
\left\{
\frac{e_i-e_j}{\rho(i,j)}:
i\ne j
\right\}
=
L_n^\circ.
\tag{4}
\]

For
\[
1\le d\le n-1,
\]
put
\[
\rho_d
=
d\frac{n^2-n+1}{n}
-
\frac{d(d+1)}2.
\tag{5}
\]

Then all \(n(n-1)\) facets of \(L_n\) split into exactly \(n-1\) strict Euclidean distance shells about the origin. For each \(d\), exactly \(n\) facets have distance
\[
\boxed{
\frac{\rho_d}{\sqrt2}.
}
\tag{6}
\]
Moreover
\[
\rho_1<\rho_2<\cdots<\rho_{n-1}.
\tag{7}
\]

Consequently the origin is the unique Euclidean incenter of \(L_n\), with
\[
\boxed{
r_{\mathrm{in}}(L_n)
=
\frac{\rho_1}{\sqrt2}
=
\frac{(n-1)^2}{n\sqrt2}.
}
\tag{8}
\]
Exactly the \(n\) clockwise-neighbor facets
\[
x_i-x_{i+1}\le\rho_1
\tag{9}
\]
are tangent to the insphere.

The polar \(K_n\) has the reciprocal radial-shell structure. For each \(d\), exactly \(n\) vertices have Euclidean norm
\[
\boxed{
\frac{\sqrt2}{\rho_d}.
}
\tag{10}
\]
The origin is the unique center of the minimum enclosing Euclidean ball of \(K_n\), with
\[
\boxed{
R_{\min}(K_n)
=
\frac{\sqrt2}{\rho_1}
=
\frac{n\sqrt2}{(n-1)^2}.
}
\tag{11}
\]
Exactly the \(n\) clockwise-neighbor vertices
\[
\frac{e_i-e_{i+1}}{\rho_1}
\tag{12}
\]
are contacts.

Thus this canonical polar realization satisfies the exact reciprocal identity
\[
\boxed{
r_{\mathrm{in}}(L_n)\,R_{\min}(K_n)=1.
}
\tag{13}
\]

## Assumptions and scope
The Euclidean metric is the one inherited by \(H_0\) from the standard orthonormal coordinates of \(\mathbb R^n\).

The Lipschitz polytope is naturally defined modulo additive constants. Equation (3) fixes the canonical zero-mean representative. The source proves that for the clock quasi-metric the resulting Lipschitz polytope is a cyclohedron and that its Kantorovich--Rubinstein polar is affinely isomorphic to the dual cyclohedron.

The metric assertions here concern this explicit quasi-metric realization. They are not invariants of the combinatorial cyclohedron, and they do not transfer through a general affine isomorphism.

The source quasi-metric is asymmetric. Hence the shells indexed by \(d\) and \(n-d\) need not coincide.

## Proof
For each ordered pair \(i\ne j\), the facet in (3) has normal
\[
e_i-e_j.
\]
This vector already lies in \(H_0\), and
\[
\|e_i-e_j\|=\sqrt2.
\tag{14}
\]
The origin has slack \(\rho(i,j)\), so its intrinsic Euclidean distance to that supporting hyperplane is
\[
\frac{\rho(i,j)}{\sqrt2}.
\tag{15}
\]

The source proves that the clock quasi-metric is strict and that its Kantorovich--Rubinstein polytope is a realization of the simplicial dual cyclohedron. The dual cyclohedron has one vertex for each proper oriented cyclic interval, hence the \(n(n-1)\) vectors in (4) are vertices; equivalently, all \(n(n-1)\) inequalities in (3) are facets.

For a fixed clock distance \(d\), there are exactly \(n\) ordered pairs. Thus (15) gives the shell multiplicities in (6).

It remains to order the shells. From (5),
\[
\begin{aligned}
\rho_{d+1}-\rho_d
&=
\frac{n^2-n+1}{n}-(d+1)\\
&=
n-1+\frac1n-(d+1).
\end{aligned}
\tag{16}
\]
For
\[
1\le d\le n-2,
\]
the right side is at least
\[
\frac1n>0.
\]
This proves (7). At \(d=1\),
\[
\rho_1
=
\frac{n^2-n+1}{n}-1
=
\frac{(n-1)^2}{n}.
\tag{17}
\]

Equation (15) now shows that the origin-centered ball of radius (8) lies in \(L_n\), with exactly the \(d=1\) facets tangent.

To prove that no translated ball is larger, suppose a ball of radius \(r\) centered at
\[
c\in H_0
\]
lies in \(L_n\). The \(n\) clockwise-neighbor facets imply
\[
c_i-c_{i+1}
\le
\rho_1-r\sqrt2
\qquad
(1\le i\le n),
\tag{18}
\]
with cyclic indices. Summing (18) gives
\[
0
\le
n(\rho_1-r\sqrt2),
\]
hence
\[
r\le\frac{\rho_1}{\sqrt2}.
\tag{19}
\]
Thus (8) is the global inradius.

If equality holds in (19), then every right side in (18) is zero. Every left side is therefore nonpositive and their sum is zero, so
\[
c_1=c_2=\cdots=c_n.
\]
Because
\[
c\in H_0,
\]
we get
\[
c=0.
\]
This proves uniqueness of the incenter.

For the polar, a vertex whose clock distance is \(d\) is
\[
v_{ij}
=
\frac{e_i-e_j}{\rho_d},
\]
so
\[
\|v_{ij}\|
=
\frac{\sqrt2}{\rho_d}.
\tag{20}
\]
Strict increase of \(\rho_d\) gives the strict radial shells in (10), with the largest radius attained exactly at \(d=1\). Hence the ball centered at the origin with radius (11) contains every vertex and therefore all of \(K_n\).

Finally write
\[
v_i
=
\frac{e_i-e_{i+1}}{\rho_1}.
\]
The \(n\) outer-shell vertices satisfy
\[
\sum_{i=1}^n v_i=0.
\tag{21}
\]
For any proposed center \(y\in H_0\),
\[
\frac1n\sum_{i=1}^n\|v_i-y\|^2
=
R_{\min}(K_n)^2+\|y\|^2.
\tag{22}
\]
Therefore some \(v_i\) is at distance at least the square root of the right side. If
\[
y\ne0,
\]
that distance is strictly larger than (11). Thus the origin is the unique minimum-enclosing center, and its contacts are exactly the \(d=1\) vertices. Equation (13) follows immediately.

## Verification
The arbitrary-\(n\) argument is symbolic.

The primary full text was checked at the definition of the Lipschitz and Kantorovich--Rubinstein polar pair, the cyclohedral realization theorem, the irredundancy argument, the clock-distance definition, and the explicit quasi-metric formula. The source proves that the quasi-metric is strict and that the resulting Lipschitz polytope is a cyclohedron.

A closely related full paper by Gordon and Petrov was also inspected. It develops face combinatorics of Lipschitz/Kantorovich--Rubinstein polytopes and proves that for a strict metric all normalized root generators are vertices. It does not state Euclidean inradius or circumradius formulas.

The accompanying `verify.py` checks \(3\le n\le100\) with exact rational arithmetic for the quasi-metric shells. It verifies strict shell ordering, shell multiplicities, the closed values of the nearest facet and farthest vertex shells, the reciprocal radius identity, and the telescoping zero barycenter of the \(n\) outer Kantorovich--Rubinstein vertices. The finite computation is corroborative only.

## Relationship to prior work
Jevtić, Jelić, and Živaljević prove that the cyclohedron occurs as the Lipschitz polar of a Kantorovich--Rubinstein polytope for the explicit clock quasi-metric (2). Their main results concern the cyclohedral combinatorial realization, root-polytope triangulations, nestohedral structure, and strict quasi-metric construction.

Gordon and Petrov study generic Lipschitz polytopes and their Kantorovich--Rubinstein duals, including face counts and admissible directed graphs. Their strictness criterion explains why normalized roots are genuine vertices.

Neither inspected full text states the Euclidean shell spectrum, a largest inscribed ball, or a minimum enclosing sphere for the clock realization.

There is a distinct standard simplex-sum nestohedral realization of the cyclohedron with a known Euclidean inradius. A general affine identification between that realization and \(L_n\) does not preserve Euclidean distances. The present formulas therefore concern a different realization singled out by optimal-transport geometry.

Targeted searches under “cyclohedron”, “Kantorovich--Rubinstein”, “clock quasi-metric”, “Lipschitz polytope”, “inradius”, “circumradius”, “minimum enclosing sphere”, and “facet-distance spectrum” did not locate a theorem implying (6)--(13).

## Limitations
The theorem concerns the explicit clock quasi-metric realization, not every geometric realization of the cyclohedron.

The minimum-enclosing statement concerns the polar Kantorovich--Rubinstein polytope in the standard \(H_0\) metric. It does not determine its inradius, nor the minimum-enclosing radius of \(L_n\).

The reciprocal identity (13) is consistent with polar duality once the origin-centered extremizers are identified; the nontrivial family-specific content is the strict clock-distance shell decomposition and the proofs that the origin is the unique optimizer on both sides.

A broader theorem about Euclidean radii of Lipschitz/Kantorovich--Rubinstein polytopes for cyclic quasi-metrics could subsume the result under different terminology. No such covering statement was located in the targeted comparisons.

## References
1. Filip D. Jevtić, Marija Jelić, and Rade T. Živaljević, *Cyclohedron and Kantorovich--Rubinstein polytopes*, arXiv:1703.06612, first public version 2017-03-20; *Arnold Mathematical Journal* 4 (2018), 99--125, DOI 10.1007/s40598-018-0083-4.
2. Joseph Gordon and Fedor Petrov, *Combinatorics of the Lipschitz polytope*, arXiv:1608.06848, first public version 2016-08-24; *Arnold Mathematical Journal* 3 (2017), 205--218, DOI 10.1007/s40598-017-0063-0.
