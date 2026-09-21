# Sharp angle-variance profile for ideal tetrahedron volume

## Statement

Let \(\Delta\) be a nondegenerate ideal tetrahedron in \(\mathbb H^3\), and let
\(\alpha,\beta,\gamma\in(0,\pi)\) be the three dihedral angles incident to one
ideal vertex. Thus
\[
\alpha+\beta+\gamma=\pi.
\]
Write
\[
V(\alpha,\beta,\gamma)
 =\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma),
\qquad
\Lambda(t)=-\int_0^t\log|2\sin u|\,du,
\]
and let
\[
v_3=3\Lambda(\pi/3)
\]
be the volume of the regular ideal tetrahedron. Define the squared
dihedral-angle deviation
\[
Q=\left(\alpha-\frac{\pi}{3}\right)^2
 +\left(\beta-\frac{\pi}{3}\right)^2
 +\left(\gamma-\frac{\pi}{3}\right)^2.
\]
For a nondegenerate ideal tetrahedron,
\(0\le Q<2\pi^2/3\). Put
\[
r=\sqrt{\frac{Q}{6}}.
\]

### Theorem 1: exact fixed-\(Q\) extremal profile

For every ideal tetrahedron,
\[
\boxed{
V(\alpha,\beta,\gamma)
\le
2\Lambda\!\left(\frac{\pi}{6}+\sqrt{\frac{Q}{6}}\right).
}
\]
If \(Q=0\), equality holds exactly at the regular tetrahedron. If
\(0<Q<2\pi^2/3\), equality holds exactly, up to permutation, at
\[
\boxed{
\left(
\frac{\pi}{3}+2r,\,
\frac{\pi}{3}-r,\,
\frac{\pi}{3}-r
\right).
}
\]
Thus the maximum volume among ideal tetrahedra with prescribed squared
distance \(Q\) from the regular angle triple is attained by a unique
isosceles angle triple, modulo permutation.

Equivalently, with \(A=\Lambda(\pi/6)\), the exact angle-variance lower
envelope for the volume deficit is
\[
v_3-V
\ge
2\left[
A-\Lambda\!\left(\frac{\pi}{6}+\sqrt{\frac{Q}{6}}\right)
\right].
\]

### Corollary 2: sharp global quadratic stability

For every ideal tetrahedron,
\[
\boxed{
v_3-V(\alpha,\beta,\gamma)
\ge
\frac{3v_3}{2\pi^2}\,
Q.
}
\]
The coefficient
\[
\frac{3v_3}{2\pi^2}\approx 0.1542526273
\]
is the largest constant valid globally for all ideal tetrahedra. It is
asymptotically attained by the degenerating family
\[
(\alpha,\beta,\gamma)=(\pi-2\varepsilon,\varepsilon,\varepsilon),
\qquad
\varepsilon\downarrow0.
\]

Consequently, if \(\delta=v_3-V\), then
\[
Q\le \frac{2\pi^2}{3v_3}\,\delta,
\]
giving a global quantitative inverse to the classical fact that
near-maximal volume forces the dihedral angles toward \(\pi/3\).

Near the regular tetrahedron, the exact profile has the stronger local
expansion
\[
v_3-V_{\max}(Q)
=
\frac{Q}{2\sqrt3}
-\frac{4}{3}\left(\frac{Q}{6}\right)^{3/2}
+O(Q^2).
\]
Hence the local quadratic coefficient \(1/(2\sqrt3)\) is strictly larger
than the best global coefficient; the latter is forced by degeneration at
the boundary of angle space.

## Proof

### 1. Classical volume identities

The volume formula
\[
V(\alpha,\beta,\gamma)
=\Lambda(\alpha)+\Lambda(\beta)+\Lambda(\gamma)
\]
for \(\alpha+\beta+\gamma=\pi\) is classical. The Lobachevsky function is
odd and \(\pi\)-periodic, and satisfies the duplication identity
\[
\Lambda(2s)=2\Lambda(s)+2\Lambda(s+\pi/2).
\]
Because
\[
\Lambda(\pi-x)=-\Lambda(x),
\]
this gives, for \(0<s<\pi/2\),
\[
\Lambda(2s)+2\Lambda(\pi/2-s)=2\Lambda(s).
\]
Taking \(s=\pi/6\) yields
\[
v_3=3\Lambda(\pi/3)=2\Lambda(\pi/6)=2A.
\]

### 2. A maximizer at fixed \(Q\) has two equal angles

Fix \(Q\in(0,2\pi^2/3)\). The intersection of the closed angle simplex
with the sphere defined by this value of \(Q\) is compact. Any boundary
angle triple has volume \(0\): if one angle is \(0\), the other two sum
to \(\pi\), so their Lobachevsky terms cancel. On the other hand, the
isosceles triple displayed in Theorem 1 is interior and has positive
volume. Therefore a fixed-\(Q\) volume maximizer is interior.

At such a maximizer, Lagrange multipliers for the constraints
\[
\alpha+\beta+\gamma=\pi,\qquad
\sum_{\theta\in\{\alpha,\beta,\gamma\}}
\left(\theta-\frac{\pi}{3}\right)^2=Q
\]
give constants \(\lambda,\mu\) satisfying
\[
\Lambda'(\theta)
=
\lambda+2\mu\left(\theta-\frac{\pi}{3}\right)
\]
at each of the three angles. Hence all three angles solve one equation
\[
g(x)=c,\qquad
g(x)=\Lambda'(x)-2\mu x.
\]
Since
\[
g''(x)=\Lambda'''(x)=\csc^2x>0
\qquad (0<x<\pi),
\]
\(g\) is strictly convex. A horizontal line meets a strictly convex
function in at most two points, so at least two of
\(\alpha,\beta,\gamma\) are equal.

### 3. The two isosceles branches can be compared exactly

Write an isosceles angle triple as
\[
(2s,\pi/2-s,\pi/2-s),
\qquad 0<s<\pi/2.
\]
By the duplication identity,
\[
V=2\Lambda(s).
\]
Moreover,
\[
Q
=
\left(2s-\frac{\pi}{3}\right)^2
+2\left(\frac{\pi}{2}-s-\frac{\pi}{3}\right)^2
=
6\left(s-\frac{\pi}{6}\right)^2.
\]
Thus, if \(r=\sqrt{Q/6}\), the possible stationary branches are
\[
s=\frac{\pi}{6}\pm r
\]
whenever they lie in \((0,\pi/2)\).

For \(0<r<\pi/6\), both branches are feasible. Their ordering is governed
by
\[
D(r)
=
\Lambda\left(\frac{\pi}{6}+r\right)
-\Lambda\left(\frac{\pi}{6}-r\right).
\]
Since \(D(0)=0\) and
\[
\begin{aligned}
D'(r)
&=
\Lambda'\left(\frac{\pi}{6}+r\right)
+\Lambda'\left(\frac{\pi}{6}-r\right)\\
&=
-\log\!\left(
4\sin\left(\frac{\pi}{6}+r\right)
 \sin\left(\frac{\pi}{6}-r\right)
\right)\\
&=
-\log(1-4\sin^2r)>0,
\end{aligned}
\]
the \(+\) branch has strictly larger volume. For
\(r\ge\pi/6\), the \(-\) branch is no longer feasible. This proves the
exact profile and its equality statement.

### 4. The best global quadratic coefficient

Let
\[
a=\frac{\pi}{6},\qquad
b=\frac{\pi}{3},\qquad
f(r)=A-\Lambda(a+r),\qquad 0\le r\le b.
\]
Then
\[
f(0)=f'(0)=0,\qquad
f''(r)=\cot(a+r).
\]
On \([0,b]\), \(f''\) is nonnegative and decreasing. Therefore
\(f(r)/r^2\) is decreasing. Indeed,
\[
r^3\left(\frac{f(r)}{r^2}\right)'
=
rf'(r)-2f(r)
=
\int_0^r(2t-r)f''(t)\,dt,
\]
and pairing \(t\) with \(r-t\) gives
\[
rf'(r)-2f(r)
=
\int_0^{r/2}
(r-2t)\bigl[f''(r-t)-f''(t)\bigr]\,dt
\le0.
\]
Hence
\[
\frac{f(r)}{r^2}
\ge
\frac{f(b)}{b^2}
=
\frac{9A}{\pi^2},
\]
because \(\Lambda(\pi/2)=0\). Since the exact profile deficit is
\(2f(r)\) and \(Q=6r^2\),
\[
v_3-V
\ge
2f(r)
\ge
\frac{3A}{\pi^2}Q
=
\frac{3v_3}{2\pi^2}Q.
\]

For
\((\alpha,\beta,\gamma)=(\pi-2\varepsilon,\varepsilon,\varepsilon)\),
we have \(V\to0\) and \(Q\to2\pi^2/3\), so
\[
\frac{v_3-V}{Q}
\longrightarrow
\frac{3v_3}{2\pi^2}.
\]
No larger global coefficient can therefore hold.

Finally, Taylor expansion at \(a=\pi/6\), using
\[
\Lambda'(a)=0,\qquad
\Lambda''(a)=-\sqrt3,\qquad
\Lambda'''(a)=4,
\]
gives the stated local expansion.

## Relation to prior literature

The Lobachevsky-function formula for ideal tetrahedron volume is classical
and is presented by Milnor (1982) and in Thurston's notes. Standard
treatments prove that the regular ideal tetrahedron uniquely maximizes
volume. Haagerup--Munkholm (1981) proved the corresponding maximal-volume
statement for hyperbolic simplices in all dimensions.

Thurston's notes also record a qualitative near-maximality statement:
a simplex with volume close to \(v_3\) has all dihedral angles close to
\(60^\circ\). They additionally give an unspecified quadratic estimate in
a face-angle parameter for near-maximal finite simplices. The result here
is different: for ideal tetrahedra it gives the exact global volume
envelope at each prescribed squared dihedral-angle deviation \(Q\), the
equality family, and the best constant in the resulting global quadratic
dihedral-angle stability inequality.

Later work on angle structures and hyperbolic polyhedral metrics develops
the strict concavity and variational role of volume, while more recent
work gives volume formulas and rigidity results for broader classes of
generalized tetrahedra and polyhedral metrics. The searches underlying
this record did not locate the fixed-\(Q\) profile above, its equality
classification, or the sharp global coefficient
\(3v_3/(2\pi^2)\).

## Limitations

- The theorem concerns nondegenerate ideal tetrahedra in
  \(\mathbb H^3\); it is not asserted for finite, hyperideal, generalized,
  or higher-dimensional simplices.
- Stability is measured in Euclidean squared distance of the three
  dihedral angles from \((\pi/3,\pi/3,\pi/3)\). No optimal estimate is
  claimed here for cross-ratio distance, Hausdorff-type distance, or a
  moduli-space metric.
- The exact profile uses special three-dimensional Lobachevsky identities
  and does not automatically generalize to arbitrary ideal polyhedra or
  triangulated manifolds.
- Originality is to the best of our knowledge. Because the proof reduces
  to an elementary constrained inequality for the Lobachevsky function,
  an equivalent special-function formulation or folklore inequality may
  exist under terminology not located in the literature search.

## References

1. J. Milnor, *Hyperbolic geometry: the first 150 years*, Bulletin of the
   American Mathematical Society 6 (1982), 9--24.
   https://doi.org/10.1090/S0273-0979-1982-14958-8
2. W. P. Thurston, *The Geometry and Topology of Three-Manifolds*,
   Chapter 6, electronic edition.
   https://library.slmath.org/books/gt3m/PDF/6.pdf
3. U. Haagerup and H. J. Munkholm, *Simplices of maximal volume in
   hyperbolic n-space*, Acta Mathematica 147 (1981), 1--11.
   https://doi.org/10.1007/BF02392865
4. J. S. Purcell, *Hyperbolic Knot Theory*, Chapter 9: Volume and angle
   structures.
   https://users.monash.edu/~jpurcell/book/Ch09_AngleStruct.pdf
5. F. Luo, *Volume and angle structures on 3-manifolds*, Asian Journal of
   Mathematics 11 (2007), 555--566.
   https://doi.org/10.4310/AJM.2007.v11.n4.a2
6. F. Luo and T. Yang, *Volume and rigidity of hyperbolic polyhedral
   3-manifolds*, Journal of Topology 11 (2018), 1--29.
   https://doi.org/10.1112/topo.12046
7. N. Peyerimhoff, *Simplices of Maximal Volume or Minimal Total Edge
   Length in Hyperbolic Space*, Journal of the London Mathematical
   Society 66 (2002), 753--768.
   https://doi.org/10.1112/S0024610702003629
8. G. Belletti and T. Yang, *Asymptotics of quantum 6j-symbols and
   generalized hyperbolic tetrahedra*, Journal of Topology 18 (2025).
   https://doi.org/10.1112/topo.70033
