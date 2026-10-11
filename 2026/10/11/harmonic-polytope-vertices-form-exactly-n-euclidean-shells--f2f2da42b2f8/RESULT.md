# Harmonic-polytope vertices form exactly n Euclidean shells
## Finding
Let
\[
n\ge2,
\]
and let
\[
H_{n,n}\subset\mathbb R^n\times\mathbb R^n
\]
be the harmonic polytope of Ardila and Escobar in its standard coordinate realization.

Put
\[
C_n=\frac{n(n+1)}2+1,
\qquad
\mu_n=\frac{C_n}{n}
=
\frac{n+1}{2}+\frac1n,
\tag{1}
\]
and define
\[
c_n=(\mu_n\mathbf1,\mu_n\mathbf1).
\tag{2}
\]

The vertices of \(H_{n,n}\) lie on exactly \(n\) concentric Euclidean spheres centered at \(c_n\). More precisely, if a vertex is indexed by a fine harmonic triple
\[
(k;\pi_1,\pi_2)
\]
and
\[
b=
\#\{j\ne k:
j\text{ precedes }k\text{ in both }\pi_1\text{ and }\pi_2\},
\tag{3}
\]
then
\[
0\le b\le n-1
\]
and its squared distance from \(c_n\) is
\[
\boxed{
\rho_{n,b}^2
=
\frac{n(n^2-1)}6
+
\frac{2(n-1)}n
+
2b.
}
\tag{4}
\]

Every value
\[
b=0,1,\ldots,n-1
\]
occurs. The number of vertices on shell \(b\) is
\[
\boxed{
M_{n,b}
=
\frac{n!}{b!}
\sum_{r=b}^{n-1}
r!(n+b-1-r)!.
}
\tag{5}
\]
Thus the shell squares form an arithmetic progression with common difference \(2\).

The unique minimum enclosing Euclidean sphere of \(H_{n,n}\) has center \(c_n\) and radius
\[
\boxed{
R_n
=
\sqrt{
\frac{(n^2-1)(n^2+12)}{6n}
}.
}
\tag{6}
\]
Its contact set is exactly the outer shell
\[
b=n-1.
\]
That shell consists of precisely
\[
\boxed{
n((n-1)!)^2
}
\tag{7}
\]
vertices, characterized by the condition that \(k\) is last in both \(\pi_1\) and \(\pi_2\).

## Assumptions and scope
The metric is the Euclidean metric inherited from
\[
\mathbb R^n\times\mathbb R^n.
\]
The realization is exactly the coordinate realization in the primary source.

The result is stated for \(n\ge2\). The case \(n=1\) is a point and is metrically degenerate.

The phrase “shell” means the intersection of the vertex set with a Euclidean sphere centered at \(c_n\). No assertion is made about the distribution of non-vertex boundary points on these spheres.

## Proof
The primary source proves that the vertices are indexed by fine harmonic triples
\[
\tau=(k;\pi_1,\pi_2)
\]
and have coordinates
\[
v_\tau
=
e_k+f_k+
(\pi_1^{-1},0)
+
(0,\pi_2^{-1}).
\tag{8}
\]
Here a permutation inverse is regarded as its position vector in
\[
\{1,\ldots,n\}^n.
\]

The same source gives the two affine equations
\[
\sum_i x_i=C_n,
\qquad
\sum_i y_i=C_n,
\tag{9}
\]
so the point in (2) is the uniform point of the affine hull.

Let
\[
p=\pi_1^{-1}(k),
\qquad
q=\pi_2^{-1}(k).
\tag{10}
\]
In the source's proof of the vertex count, the \(n-1\) labels distinct from \(k\) are partitioned into three classes:
\[
a=
\#\{\text{before }k\text{ in }\pi_1,\ \text{after }k\text{ in }\pi_2\},
\]
\[
b=
\#\{\text{before }k\text{ in both permutations}\},
\]
and
\[
c=
\#\{\text{after }k\text{ in }\pi_1,\ \text{before }k\text{ in }\pi_2\}.
\tag{11}
\]
The harmonic condition excludes a label that is after \(k\) in both permutations. Therefore
\[
a+b+c=n-1.
\tag{12}
\]
The positions of \(k\) are
\[
p=a+b+1,
\qquad
q=b+c+1,
\]
and hence
\[
p+q=n+1+b.
\tag{13}
\]

For any permutation position vector
\[
u=(u_1,\ldots,u_n),
\]
write
\[
\bar u_i=u_i-\frac{n+1}{2}.
\]
The standard identity
\[
\sum_{i=1}^n\bar u_i^2
=
\frac{n(n^2-1)}{12}
\tag{14}
\]
is independent of the permutation.

Consider the first \(n\)-coordinate block of \(v_\tau-c_n\). It is
\[
\bar u+e_k-\frac1n\mathbf1.
\]
Because
\[
\sum_i\bar u_i=0,
\qquad
\left\|e_k-\frac1n\mathbf1\right\|^2
=
1-\frac1n,
\]
its squared norm is
\[
\frac{n(n^2-1)}{12}
+
1-\frac1n
+
2\left(p-\frac{n+1}{2}\right).
\tag{15}
\]
The second block has the analogous expression with \(q\). Adding them and using (13) gives
\[
\|v_\tau-c_n\|^2
=
\frac{n(n^2-1)}6
+
2-\frac2n
+
2b,
\]
which is (4).

Every \(b\in\{0,\ldots,n-1\}\) occurs: choose nonnegative
\[
a,c
\]
with
\[
a+c=n-1-b
\]
and order the three source classes arbitrarily inside their permitted regions. Since the right side of (4) increases by exactly \(2\) when \(b\) increases by \(1\), the \(n\) shells are distinct.

For the multiplicity, fix \(b\). The source's enumeration gives, for fixed \(a,b,c\),
\[
n
\binom{n-1}{a,b,c}
(a+b)!\,c!\,a!\,(b+c)!
\tag{16}
\]
fine harmonic triples. Summing (16) over
\[
a+c=n-1-b
\]
and simplifying yields
\[
M_{n,b}
=
\frac{n!}{b!}
\sum_{a=0}^{n-1-b}
(a+b)!(n-1-a)!.
\]
The substitution
\[
r=a+b
\]
gives exactly (5).

The largest shell is \(b=n-1\). Substituting that value into (4) gives
\[
R_n^2
=
\frac{n(n^2-1)}6
+
2n-\frac2n
=
\frac{(n^2-1)(n^2+12)}{6n},
\]
which proves the radius formula in (6). Formula (5) gives
\[
M_{n,n-1}=n((n-1)!)^2.
\]
When \(b=n-1\), equations (12) force
\[
a=c=0,
\]
so \(k\) is last in both permutations. Conversely that condition gives \(b=n-1\). This proves the contact-set characterization.

It remains to prove that the outer common sphere is genuinely minimum enclosing and uniquely centered.

Average all outer-shell vertices with equal weights. Fix \(k\). Over all permutations ending in \(k\), the coordinate \(k\) in the first block of (8) is
\[
n+1,
\]
while each other coordinate has average
\[
\frac{1+\cdots+(n-1)}{n-1}
=
\frac n2.
\]
Averaging next over the \(n\) choices of \(k\), every coordinate has mean
\[
\frac1n(n+1)
+
\frac{n-1}{n}\frac n2
=
\frac{n+1}{2}+\frac1n
=
\mu_n.
\]
The same argument applies to the second block. Hence the barycenter of the entire outer shell is exactly \(c_n\).

Let \(Q\) be any candidate center. Averaging squared distances over the outer shell gives the parallel-axis identity
\[
\frac1{M_{n,n-1}}
\sum_{v\text{ outer}}
\|v-Q\|^2
=
R_n^2+\|Q-c_n\|^2.
\tag{17}
\]
Therefore some outer-shell vertex has distance at least
\[
\sqrt{R_n^2+\|Q-c_n\|^2}.
\]
At \(Q=c_n\), all vertices of the polytope have distance at most \(R_n\), with equality exactly on the outer shell. If
\[
Q\ne c_n,
\]
equation (17) forces a strictly larger required radius. Thus (6) is the unique minimum enclosing sphere and its contact set is exactly the outer shell.

## Verification
The proof is symbolic for every \(n\ge2\).

The source-dependent ingredients were checked directly in the primary full text and PDF page image: the characterization of fine harmonic triples, the three-class \(a,b,c\) decomposition used in the vertex count, the exact vertex formula (8), and the affine equations (9).

The accompanying `verify.py` independently enumerates all fine harmonic triples for
\[
2\le n\le5.
\]
It checks the harmonic condition, the shell index \(b\), the exact squared-radius formula, and every shell multiplicity. It also verifies the source total vertex count and the outer-shell barycenter. These finite checks are corroborative only.

## Relationship to prior work
Ardila and Escobar give the complete vertex and facet descriptions of the harmonic polytope and compute its volume through mixed volumes and bipartite graph edge polytopes. Their paper does not state a Euclidean circumradius, a minimum enclosing sphere, or a radial shell decomposition of the harmonic-polytope vertices.

Ardila's later bipermutahedron paper proves that the harmonic polytope is a Minkowski summand of the bipermutahedron with exact Minkowski quotient \(2\). That statement concerns support functions and deformation cones; it does not determine Euclidean vertex radii or minimum enclosing balls.

The shell parameter \(b\) already occurs implicitly in the source's enumeration as the number of labels preceding \(k\) in both permutations. The new point is that this purely order-theoretic statistic is exactly an affine coordinate for squared Euclidean radius:
\[
\rho_{n,b+1}^2-\rho_{n,b}^2=2.
\]
This also turns the extreme order condition “\(k\) last in both permutations” into the complete contact set of the minimum enclosing sphere.

Targeted published-result and literature searches under “harmonic polytope”, “circumradius”, “minimum enclosing sphere”, “vertex norm”, “vertex shells”, “fine harmonic triple”, and “Minkowski quotient” did not locate a theorem implying (4)--(7).

## Limitations
The result is specific to the standard Ardila--Escobar realization and its inherited Euclidean metric.

It gives the radial shell distribution and the minimum enclosing sphere, but not the full pairwise distance distribution, John ellipsoid, or Löwner ellipsoid.

The exact vertex formula in the primary source makes the shell calculation accessible once the correct statistic \(b\) is isolated. An independently rediscovered version under different metric terminology remains a residual originality risk.

## References
1. Federico Ardila and Laura Escobar, *The harmonic polytope*, arXiv:2006.03078, first public version 2020-06-04; Selecta Mathematica 27 (2021), article 91, DOI 10.1007/s00029-021-00687-6.
2. Federico Ardila, *The bipermutahedron*, arXiv:2008.02295, first public version 2020-08-05; Combinatorial Theory 2(3) (2022), article 1.
