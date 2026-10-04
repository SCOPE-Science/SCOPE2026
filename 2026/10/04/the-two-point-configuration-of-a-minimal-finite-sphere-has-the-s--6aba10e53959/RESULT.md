# The two-point configuration of a minimal finite sphere has the same core
## Finding
For every integer \(n\ge 2\), let \(X_n=\mathbb{S}^{n}S^0\) be the \(2n+2\)-point minimal finite model of \(S^n\), written as levels \(L_i=\{(i,0),(i,1)\}\) for \(0\le i\le n\), with every point of \(L_i\) below every point of \(L_j\) when \(i<j\). Let \(F_2(X_n)=\{(x,y)\in X_n\times X_n:x\ne y\}\) have the induced product order. Then the subspace \(A_n=\{((i,0),(i,1)),((i,1),(i,0)):0\le i\le n\}\) is a strong deformation retract of \(F_2(X_n)\) and is its Stong core. More precisely, the \(4n(n+1)\) points whose two coordinates lie in different levels can be deleted in lexicographic order of their four labels, and each deletion is a down-beat-point deletion. The surviving poset \(A_n\) is isomorphic to \(X_n\). Consequently \(F_2(X_n)\simeq X_n\), so the ordered two-point configuration space of the minimal finite \(n\)-sphere is itself a finite model of \(S^n\).

In particular, although \(F_2(X_n)\) has
\[
(2n+2)(2n+1)
\]
points, its finite homotopy core has only \(2n+2\) points. The reduction removes exactly
\[
(2n+2)(2n+1)-(2n+2)=4n(n+1)
\]
points.

## Assumptions and scope
For \(n\ge 2\), write
\[
X_n=\{(i,\varepsilon):0\le i\le n,\ \varepsilon\in\{0,1\}\}
\]
with
\[
(i,\varepsilon)<(j,\delta)\quad\Longleftrightarrow\quad i<j.
\]
Thus the two points in each level are incomparable, and every point in a lower level is below every point in a higher level. This is the usual iterated non-Hausdorff suspension model of the sphere.

The ordered configuration space is the deleted product
\[
F_2(X_n)=\{(x,y):x,y\in X_n,\ x\ne y\}
\]
with the subspace order inherited from the product. Define the anti-diagonal level set
\[
A_n=\{((i,0),(i,1)),((i,1),(i,0)):0\le i\le n\}.
\]

## Proof
Order the points of \(X_n\) lexicographically by \((i,\varepsilon)\), and order the off-level points
\[
p=((i,a),(j,b)),\qquad i\ne j,
\]
lexicographically by \((i,a,j,b)\). Delete these off-level points in that order.

Fix the point currently being deleted. If \(i<j\), put
\[
c_p=((i,a),(i,1-a)).
\]
If \(j<i\), put
\[
c_p=((j,1-b),(j,b)).
\]
In either case \(c_p\in A_n\), \(c_p<p\), and \(c_p\) has level \(\min\{i,j\}\).

At the moment \(p\) is deleted, every surviving strict predecessor of \(p\) lies in \(A_n\). Indeed, a strict predecessor with first-coordinate level below \(i\) was deleted earlier because its first coordinate occurs earlier in the lexicographic order. A strict predecessor with the same first coordinate as \(p\) and a lower second-coordinate level was also deleted earlier. No different point in the same first-coordinate level can be below \(p\), because the two points of a level are incomparable.

Among the surviving core points below \(p\), the point \(c_p\) is the greatest one. Any core point at a level strictly below \(\min\{i,j\}\) lies below \(c_p\). At level \(\min\{i,j\}\), comparability with \(p\) forces the coordinate that attains the minimum level to agree with the corresponding coordinate of \(p\), which leaves exactly \(c_p\). Hence the strict lower set of \(p\) has greatest element \(c_p\), so \(p\) is a down beat point.

There are exactly \(4n(n+1)\) off-level points, so the process ends at \(A_n\). Beat-point deletion is a strong deformation retraction, hence the composite reduction is a strong deformation retraction
\[
F_2(X_n)\searrow A_n.
\]

Finally, at each level \(i\), the two points
\[
((i,0),(i,1)),\qquad ((i,1),(i,0))
\]
are incomparable, while every survivor at level \(i\) lies below every survivor at level \(j\) for \(i<j\). Therefore \(A_n\cong X_n\). The model \(X_n\) has no beat points: away from the extreme levels, each strict upper and lower set has two incomparable extremal points in the adjacent level; the same obstruction occurs on the only relevant side at the bottom and top levels. Thus \(A_n\) is the core.

## Verification
The accompanying `verify.py` reconstructs \(X_n\), \(F_2(X_n)\), the claimed lexicographic deletion sequence, and every beat witness directly from the definitions. For each \(2\le n\le 10\), it checks that every deleted point has the stated greatest strict predecessor at its deletion time, that the survivor set is exactly \(A_n\), that its order is exactly that of \(X_n\), and that it has no beat points.

A replay of the embedded verifier returned:
`VERIFY_OK n=2:points=30,deletions=24,core=6 ... n=10:points=462,deletions=440,core=22`.

The finite replay is a stress test, not the proof of the universal quantifier; the proof above establishes the statement for every \(n\ge2\).

## Relationship to prior work
Barmak and Minian identify the unique minimal finite model of \(S^n\) as the iterated non-Hausdorff suspension \(\mathbb{S}^nS^0\) with \(2n+2\) points. Their paper develops beat-point methods and minimal finite models but does not study deleted products or configuration spaces.

Kandola later studies topological complexity of these same minimal finite sphere models, including products and the diagonal in the motion-planning setting. The inspected full text does not state a homotopy reduction for the complement of the diagonal and contains no configuration-space or deleted-product theorem of the form proved here.

For the ordinary Hausdorff sphere, the projection \(F_2(S^n)\to S^n\) has contractible fiber and gives the familiar homotopy type \(F_2(S^n)\simeq S^n\). The present result is stronger at the finite-model level: it gives an explicit sequence of finite beat-point deletions and identifies the exact core.

## Limitations
The claim concerns ordered configurations of exactly two points and the minimal finite sphere model. It does not determine unordered quotients, configurations of three or more points, or configuration spaces of arbitrary finite models of spheres. The finite-space homotopy equivalence proved here should not be conflated with a homeomorphism of configuration spaces after geometric realization.

## References
Jonathan A. Barmak and Elias G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1, first posted 2006-11-06; Journal of Homotopy and Related Structures 2 (2007), 127-140.

Shelley Kandola, *The Topological Complexity of Finite Models of Spheres*, arXiv:1812.07604v1, first posted 2018-12-18.
