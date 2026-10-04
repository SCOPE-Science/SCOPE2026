# Fixed-canonical majorization law for geometric genus of complete-intersection threefolds
## Finding
Fix integers
\[
c\ge2,
\qquad
S>c+4,
\]
and let
\[
X_{\mathbf d}\subset\mathbb P^{c+3}_{\mathbb C}
\]
be a smooth complete-intersection threefold of multidegree
\[
\mathbf d=(d_1,\ldots,d_c),
\qquad
d_i\ge2,
\qquad
\sum_i d_i=S.
\]
Write
\[
m=S-c-4>0.
\]
Thus
\[
K_{X_{\mathbf d}}\cong\mathcal O_{X_{\mathbf d}}(m),
\]
so fixing \(c\) and \(S\) fixes the canonical-polarization exponent.

The geometric genus is
\[
p_g(X_{\mathbf d})
=
1+
\frac{m}{48}
\left(\prod_i d_i\right)
\left(
m^2+\sum_i d_i^2-c-4
\right).
\]

Suppose two defining degrees satisfy
\[
a<b-1.
\]
Replacing them by
\[
(a,b)\longmapsto(a+1,b-1)
\]
never decreases \(p_g\). Equality occurs only in the following three balancing configurations, up to permutation:
\[
(2,5)\longmapsto(3,4),
\]
\[
(3,5)\longmapsto(4,4),
\]
and
\[
(2,2,4)\longmapsto(2,3,3).
\]

Therefore, among all multidegrees with fixed \(c\) and fixed \(S\), the geometric genus is minimized by the most unbalanced admissible tuple
\[
(2,\ldots,2,S-2c+2)
\]
and maximized by the most balanced tuple. If
\[
S=qc+r,
\qquad
0\le r<c,
\]
the latter is
\[
(\underbrace{q,\ldots,q}_{c-r},
\underbrace{q+1,\ldots,q+1}_{r}).
\]

The only nonunique extrema are the following low-sum cases:
\[
(c,S)=(2,7):
\qquad
p_g(2,5)=p_g(3,4)=6;
\]
\[
(c,S)=(2,8):
\qquad
p_g(2,6)=20,
\qquad
p_g(3,5)=p_g(4,4)=21;
\]
and
\[
(c,S)=(3,8):
\qquad
p_g(2,2,4)=p_g(2,3,3)=7.
\]

Thus, apart from these explicitly classified ties, geometric genus is strictly increased by every balancing step and is a strict discrete Schur-concave invariant on fixed-sum multidegrees.

## Assumptions and scope
The statement concerns smooth complex complete intersections of dimension three in ordinary projective space. Every defining degree is at least two.

The inequality
\[
S>c+4
\]
is exactly the general-type condition in this setting, because adjunction gives
\[
K_X\cong\mathcal O_X(S-c-4).
\]
The theorem is not asserted for the Fano or Calabi--Yau ranges, where the sign in the Riemann--Roch expression changes or vanishes.

The word "balanced" refers only to the defining-degree tuple at fixed codimension and fixed sum. No assertion is made about degenerations between the corresponding deformation families.

## Proof
Let
\[
D=\prod_i d_i.
\]
For a smooth complete-intersection threefold, the Lefschetz theorem gives
\[
h^{0,1}(X)=h^{0,2}(X)=0.
\]
Hence
\[
p_g=h^{0,3}=1-\chi(\mathcal O_X).
\]

Write
\[
k=c+4-S=-m.
\]
The standard complete-intersection characteristic-class formulas give
\[
c_1(X)=kH
\]
and
\[
p_1(X)=
\left(
c+4-\sum_i d_i^2
\right)H^2,
\]
where \(H\) is the hyperplane class. Since
\[
p_1=c_1^2-2c_2,
\]
we obtain
\[
2c_2=
\left(
m^2+\sum_i d_i^2-c-4
\right)H^2.
\]
Also
\[
\int_X H^3=D.
\]
Hirzebruch--Riemann--Roch for a threefold gives
\[
\chi(\mathcal O_X)=\frac1{24}\int_X c_1c_2.
\]
Substituting \(c_1=-mH\) yields
\[
p_g
=
1+
\frac{mD}{48}
\left(
m^2+\sum_i d_i^2-c-4
\right).
\]

Now fix \(c\) and \(S\), so \(m\) is constant. Choose two degrees
\[
a<b-1
\]
and put
\[
\delta=b-a-1>0.
\]
Let \(P\) be the product of the remaining defining degrees and set
\[
R=m^2+\sum_i d_i^2-c-4.
\]
Under the balancing move,
\[
ab\longmapsto(a+1)(b-1)=ab+\delta
\]
and
\[
R\longmapsto R-2\delta.
\]
Therefore the change in geometric genus is
\[
\Delta p_g
=
\frac{mP\delta}{48}
\left(
R-2ab-2\delta
\right).
\]

It remains to prove that the final factor is nonnegative and to classify equality. Put
\[
r=c-2,
\qquad
u=a-2,
\qquad
t=b-a-2.
\]
Write the remaining degrees as
\[
2+w_1,\ldots,2+w_r,
\qquad
w_j\ge0,
\]
and define
\[
W=\sum_j w_j.
\]
A direct expansion gives
\[
\begin{aligned}
R-2ab-2\delta
={}&
(r-1)(r+4)
+4u(r+u+t)
+2t(r+t+1)\\
&+2W(r+2u+t+2)
+W^2
+\sum_j w_j^2.
\end{aligned}
\]

If \(r\ge2\), this is strictly positive. If \(r=1\), every term is nonnegative and equality occurs only when
\[
u=t=W=0,
\]
which is exactly
\[
(2,2,4)\longmapsto(2,3,3).
\]

If \(r=0\), the general-type condition is
\[
2u+t\ge1,
\]
and the factor becomes
\[
-4+4u(u+t)+2t(t+1).
\]
It is nonnegative, with equality only for
\[
(u,t)=(0,1)
\quad\text{or}\quad
(u,t)=(1,0),
\]
which are exactly
\[
(2,5)\longmapsto(3,4)
\]
and
\[
(3,5)\longmapsto(4,4).
\]

Thus every balancing step is nondecreasing, with exactly the three equality types stated above.

Repeated balancing reaches the most balanced tuple. Reversing balancing steps until all but one degree equal two reaches
\[
(2,\ldots,2,S-2c+2).
\]
Hence these are respectively the global maximum and global minimum. The equality classification above shows that the only nonunique extrema are the three low-sum families listed in the finding.

## Verification
The bundled exact-integer checker verifies the closed formula in two independent ways: from the Chern-number expression above and from the coefficient of
\[
\frac{\prod_i(1-t^{d_i})}{(1-t)^{c+4}}
\]
in degree
\[
m=S-c-4,
\]
which equals
\[
h^0(X,K_X)=p_g.
\]

It then checks every admissible balancing move in a bounded multidegree box and verifies that the only equality types are the three proved symbolically above. Finally it enumerates fixed-sum families and confirms the balanced maximum, the one-heavy minimum, and exactly the three nonunique-extremum families.

The finite computations are regression evidence only. The theorem for all \(c\) and \(S\) follows from the displayed symbolic balancing identity.

## Relationship to prior work
Chen--Chen--Chen use the amplitude
\[
\alpha=\sum d_i-\sum a_i
\]
to organize weighted complete intersections and the Fano, Calabi--Yau, and general-type regimes; ordinary projective complete intersections are the special case with all ambient weights equal to one. Kotschick--Placini record, for smooth complete-intersection threefolds, the formulas
\[
h^{0,3}=1-\frac1{24}c_1c_2,
\qquad
c_1=(c+4-\sum d_i)H,
\qquad
p_1=(c+4-\sum d_i^2)H^2.
\]
These give the closed expression for \(p_g\) used here.

Recent work of Przyjalkowski studies positivity and lower bounds for geometric genus of smooth weighted complete intersections of general type. Its retrieved abstract does not state a fixed-codimension, fixed-amplitude majorization theorem, a balanced maximum, or the three equality exceptions above. The full text of that recent preprint was not available through the inspected source path, so a residual comparison risk remains.

Claim-specific searches for geometric-genus extrema, majorization, balanced multidegrees, and fixed canonical amplitude did not locate a source stating the present balancing law or the exact equality classification.

## Limitations
The theorem is specific to complex dimension three. In higher dimension, the holomorphic Euler characteristic involves higher Todd terms, and the same one-step factorization need not persist.

The result fixes both codimension and the sum of defining degrees. It does not compare complete intersections across different codimensions, even when their canonical classes have the same numerical exponent.

Only the general-type range is treated. The Calabi--Yau boundary has
\[
m=0
\]
and therefore constant geometric genus \(p_g=1\), while the Fano range has \(p_g=0\).

A residual literature risk remains because a current preprint on geometric-genus lower bounds for weighted complete intersections could contain a related inequality beyond what is visible in its abstract.

## References
Jheng-Jie Chen, Jungkai A. Chen, and Meng Chen, *On Quasismooth Weighted Complete Intersections*, arXiv:0908.1439, first submitted 11 August 2009; Journal of Algebraic Geometry 20 (2011), 239--262.

D. Kotschick and G. Placini, *Sasaki structures distinguished by their basic Hodge numbers*, Bulletin of the London Mathematical Society 54 (2022), 1962--1977. DOI: 10.1112/blms.12667.

V. Przyjalkowski, *Maximality of the Hodge level for smooth weighted complete intersections of general type*, arXiv:2609.11825, first submitted 10 September 2026.
