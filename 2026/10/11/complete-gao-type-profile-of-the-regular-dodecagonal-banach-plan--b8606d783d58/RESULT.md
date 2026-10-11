# Complete Gao-type profile of the regular dodecagonal Banach plane
## Finding
Let \(X_{12}=(\mathbb R^2,N_{12})\), where
\[
N_{12}(s,t)=
\max\left\{
|s|,\ |t|,\
\left|\frac{\sqrt3s+t}{2}\right|,\
\left|\frac{s+\sqrt3t}{2}\right|,\
\left|\frac{-s+\sqrt3t}{2}\right|,\
\left|\frac{-\sqrt3s+t}{2}\right|
\right\}.
\]
Its unit ball is a Euclidean regular dodecagon circumscribed about the Euclidean unit circle.

For \(1\le p<\infty\), define the Gao-type constant
\[
c_{\mathrm{NJ}}^{(p)}(X)
=
\inf_{x,y\in S_X}
\frac{\|x+y\|^p+\|x-y\|^p}{2^p}.
\]
Put
\[
r=2-\sqrt3.
\]
Then
\[
c_{\mathrm{NJ}}^{(1)}(X_{12})=1.
\]
For \(1<p\le2\), put
\[
q_p=r^{1/(p-1)}.
\]
The exact value is
\[
c_{\mathrm{NJ}}^{(p)}(X_{12})
=
\frac{1+q_p^p}{(1+r q_p)^p}.
\]
For \(2\le p<\infty\),
\[
c_{\mathrm{NJ}}^{(p)}(X_{12})
=
2\left(\frac{1+\sqrt3}{4}\right)^p.
\]
At \(p=2\), both formulas give
\[
c_{\mathrm{NJ}}^{(2)}(X_{12})
=
\frac{2+\sqrt3}{4}.
\]
Thus \(p=2\) is the exact transition between a local adjacent-edge extremizer and the balanced coordinate extremizer.

## Assumptions and scope
All scalars are real. The exponent satisfies \(1\le p<\infty\).

The result concerns the Gao-type lower generalized von Neumann--Jordan constant, not the upper generalized von Neumann--Jordan constant. The normalization is the circumscribed regular dodecagon above; linear isometries preserve the constant.

The proof uses two geometric facts about \(X_{12}\). First,
\[
\cos\left(\frac{\pi}{12}\right)\|z\|_2
\le
N_{12}(z)
\le
\|z\|_2.
\]
Second, if \(x,y\in S_{X_{12}}\) and
\[
B=N_{12}(x-y)\le\frac12,
\]
then, with
\[
A=N_{12}(x+y),
\]
one has
\[
A+rB\ge2.
\]

## Proof
Write
\[
c=\cos\left(\frac{\pi}{12}\right),
\qquad
r=2-\sqrt3.
\]
For any \(x,y\in S_{X_{12}}\), set
\[
A=N_{12}(x+y),
\qquad
B=N_{12}(x-y).
\]

Because the dodecagonal facet normals are spaced by \(30^\circ\),
\[
c\|z\|_2\le N_{12}(z)\le\|z\|_2.
\]
Hence \(\|x\|_2,\|y\|_2\ge1\), and the Euclidean parallelogram identity gives
\[
A^2+B^2
\ge
c^2\bigl(\|x+y\|_2^2+\|x-y\|_2^2\bigr)
=
2c^2\bigl(\|x\|_2^2+\|y\|_2^2\bigr)
\ge
4c^2
=
2+\sqrt3.
\tag{1}
\]

We next prove the local sharp inequality. Replacing \(y\) by \(-y\) swaps \(A\) and \(B\), so when needed we may assume \(B\le A\). Suppose
\[
B\le\frac12.
\]
The distance, in \(N_{12}\), between two nonincident closed edges of the unit dodecagon is at least
\[
2r=4-2\sqrt3>\frac12.
\]
Indeed, after dihedral reduction to one fixed edge, the five possible cyclic edge separations \(2,3,4,5,6\) admit signed supporting functionals whose minima on the two edge products are respectively
\[
2r,\quad \sqrt3-1,\quad 1+r,\quad \sqrt3,\quad 2.
\]
Thus \(x\) and \(y\) lie on the same edge or on adjacent edges.

If they lie on the same edge, a common supporting functional gives \(A=2\), so \(A+rB\ge2\).

For adjacent edges, dihedral symmetry and interchange of \(x,y\) reduce to
\[
x=(1,s),\qquad -r\le s\le r,
\]
and
\[
y=(u,2-\sqrt3u),\qquad \sqrt3-1\le u\le1.
\]
Put
\[
v=2-\sqrt3u-s\ge0.
\]
Then
\[
B\ge v,
\]
while two signed facets give
\[
A\ge1+u
\]
and
\[
A\ge
\frac{4+\sqrt3-\sqrt3u-v}{2}.
\]
Write \(\delta=1-u\). If
\[
v\ge\frac{\delta}{r},
\]
then
\[
A+rB\ge1+u+rv\ge2.
\]
If instead
\[
v\le\frac{\delta}{r},
\]
then
\[
A+rB
\ge
2+\frac{\sqrt3}{2}\delta+\left(r-\frac12\right)v
\ge2,
\]
because
\[
\frac{\sqrt3}{2}
+
\frac{r-\frac12}{r}
=0.
\]
Therefore
\[
B\le\frac12
\quad\Longrightarrow\quad
A+rB\ge2.
\tag{2}
\]

Now let \(1<p\le2\), and assume \(B\le A\). If \(B\le1/2\), (2) implies
\[
A^p+B^p
\ge
\min_{0\le t\le1/2}
\bigl((2-rt)^p+t^p\bigr).
\]
The unique critical point satisfies
\[
\frac{t}{2-rt}=r^{1/(p-1)}=q_p.
\]
Thus
\[
t_p=\frac{2q_p}{1+r q_p},
\qquad
2-rt_p=\frac{2}{1+r q_p}.
\]
Since \(q_p\le r\) for \(p\le2\), and
\[
4r=1+r^2,
\]
one has \(t_p\le1/2\). Hence
\[
\frac{A^p+B^p}{2^p}
\ge
\frac{1+q_p^p}{(1+r q_p)^p}.
\tag{3}
\]

If instead \(B\ge1/2\), use (1). Put \(U=A^2\), \(V=B^2\). On the line
\[
U+V=2+\sqrt3,
\qquad
\frac14\le V\le\frac{2+\sqrt3}{2},
\]
the function
\[
U^{p/2}+V^{p/2}
\]
is concave because \(p/2\le1\). Its minimum is therefore at an endpoint. The more unequal endpoint is
\[
B=\frac12,
\qquad
A=\frac{2+\sqrt3}{2},
\]
and gives the smaller \(p\)-sum for \(1\le p\le2\). This endpoint also satisfies
\[
A+rB=2,
\]
so its value is no smaller than the minimum in (3). Thus (3) is the global lower bound.

It is attained. For \(1<p\le2\), set
\[
t=t_p
\]
and define
\[
x=\bigl(1,r(1-2t)\bigr),
\qquad
y=\bigl(1-rt,r+\sqrt3rt\bigr).
\]
Since \(0\le t\le1/2\), these points lie on two adjacent unit edges. Direct substitution gives
\[
N_{12}(x)=N_{12}(y)=1,
\]
\[
N_{12}(x-y)=t,
\qquad
N_{12}(x+y)=2-rt.
\]
This proves the first branch. At \(p=1\), the triangle inequality gives
\[
A+B\ge2,
\]
and equality is attained by \(x=y\), so \(c_{\mathrm{NJ}}^{(1)}(X_{12})=1\).

For \(p\ge2\), (1) and the two-coordinate power-mean inequality yield
\[
A^p+B^p
\ge
2^{1-p/2}(A^2+B^2)^{p/2}
\ge
2^{1-p/2}(2+\sqrt3)^{p/2}.
\]
After division by \(2^p\),
\[
c_{\mathrm{NJ}}^{(p)}(X_{12})
\ge
2\left(\frac{1+\sqrt3}{4}\right)^p.
\]
For
\[
x=(1,0),\qquad y=(0,1),
\]
both are unit vectors and
\[
N_{12}(x+y)=N_{12}(x-y)=\frac{1+\sqrt3}{2}.
\]
Therefore equality holds and the second branch follows.

## Verification
The bundled `verify.py` performs exact symbolic checks in \(\mathbb Q(\sqrt3)\). It reconstructs all twelve vertices and facets, verifies the edge incidence pattern, and checks the five dihedral nonincident-edge separation certificates used to justify the local reduction.

It also verifies the algebraic identities
\[
r(2+\sqrt3)=1,
\qquad
4r=1+r^2,
\qquad
\frac{\sqrt3}{2}+\frac{r-\frac12}{r}=0,
\]
the adjacent-edge extremizer family, and the balanced \(p\ge2\) pair. The calculus minimization and the concavity/power-mean steps are analytic arguments stated explicitly in the proof; no finite experiment is used as an infinite proof.

## Relationship to prior work
Ahmad, Xie, Bi and Li introduced the lower generalized constant \(c_{\mathrm{NJ}}^{(p)}\), established its universal bounds, and computed the \(\ell_1^2\) endpoint example. Zuo, Huang, Huang and Wang then developed a general absolute-normalized-norm method, gave comparison bounds and several exact examples, and explicitly noted that exact values for further concrete absolute norms remain a natural problem.

The inspected 2022 full text contains no dodecagonal or regular-polygon computation. Its general comparison theorem supplies bounds, not the two-branch formula above. Its exact lower-bound criterion is for the classical exponent \(p=2\); the present result determines every \(1\le p<\infty\), identifies the nonlinear adjacent-edge branch for \(1<p<2\), and proves that the extremizer changes at \(p=2\).

The closest public research records concern upper or differently parameterized von Neumann--Jordan profiles, mostly on the regular octagon. Those statements do not imply this lower Gao-type profile on the regular dodecagon.

## Limitations
The result is specific to the regular dodecagonal plane. It does not provide a formula for every regular \(2n\)-gonal norm, nor does it classify all absolute normalized norms whose Gao-type profile changes extremizer at \(p=2\).

The originality search cannot prove absolute uniqueness. An equivalent calculation under a different polygonal normalization or notation remains a residual bibliographic risk. The \(p=2\) value by itself is not the novelty claim; it is the junction of the complete all-\(p\) profile.

## References
1. A. Ahmad, H. Xie, J. Bi and Y. Li, “Some von Neumann-Jordan type and Gao type constants related to minimum in Banach spaces,” Research and Communications in Mathematics and Mathematical Sciences 14 (2022), 121–134. Published online 27 September 2022.
2. Z. Zuo, Y. Huang, H. Huang and J. Wang, “The Gao-Type Constant of Absolute Normalized Norms on \(\mathbb R^2\),” Mathematics 10 (2022), 4591, doi:10.3390/math10234591. Published 4 December 2022; primary MSC 46B20.
