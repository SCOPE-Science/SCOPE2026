# Sharp saturation threshold for the generalized minimum von Neumann–Jordan constant of the regular octagon
## Finding
Let \(X_8=(\mathbb R^2,N_8)\), where
\[
N_8(s,t)=\max\left\{|s|,\ |t|,\ \frac{|s|+|t|}{\sqrt2}\right\}.
\]
Its unit ball is the regular octagon with vertices
\[
(\pm1,\pm(\sqrt2-1)),\qquad
(\pm(\sqrt2-1),\pm1).
\]

For the Liu–Din–Li constant \(C_{-\infty}(a,X)\),
\[
C_{-\infty}(a,X_8)=1
\quad\Longleftrightarrow\quad
a\ge\sqrt2.
\]
Equivalently, for the generalized James constant \(J(a,X)\) appearing in the same theory,
\[
J(a,X_8)=2
\quad\Longleftrightarrow\quad
a\ge\sqrt2.
\]
Hence the regular octagon has the exact saturation threshold
\[
a_*=\sqrt2,
\]
which is strictly smaller than the universal sufficient threshold \(a=2\).

## Assumptions and scope
All scalars are real. The parameter satisfies \(a\ge0\).

Liu, Din and Li define
\[
C_{-\infty}(a,X)
=
\sup
\min\left\{
\frac{\|x+y\|^2}{2\|x\|^2+\|y\|^2+\|z\|^2},
\frac{\|x-z\|^2}{2\|x\|^2+\|y\|^2+\|z\|^2}
\right\},
\]
where the supremum is over nonzero triples with
\[
a\|x\|>\|y-z\|.
\]
They also use
\[
J(a,X)=
\sup\left\{
\min\{\|x-z\|,\|x+y\|\}:
x,y,z\in B_X,\ a\|x\|>\|y-z\|
\right\}.
\]
Their Proposition 4 proves, for \(0\le a\le2\),
\[
C_{-\infty}(a,X)=1
\quad\Longleftrightarrow\quad
J(a,X)=2.
\]
Their Proposition 2 gives \(C_{-\infty}(a,X)=1\) for \(a>2\).

The new work is therefore the exact computation of the saturation threshold for \(J(a,X_8)\).

## Proof
Write \(r=\sqrt2-1\). The norm can equivalently be written as the maximum of the eight signed facet functionals
\[
\pm s,\quad
\pm t,\quad
\pm\frac{s+t}{\sqrt2},\quad
\pm\frac{s-t}{\sqrt2}.
\]

First determine the least possible value of \(N_8(y-z)\) under the two diameter equalities
\[
x,y,z\in B_{X_8},\qquad
N_8(x-z)=2,\qquad
N_8(x+y)=2.
\]

Because \(N_8(x-z)=2\), some signed facet functional \(f\) satisfies
\[
f(x)=1,\qquad f(z)=-1.
\]
Likewise, because \(N_8(x+y)=2\), some signed facet functional \(g\) satisfies
\[
g(x)=1,\qquad g(y)=1.
\]
If \(f=g\), then
\[
N_8(y-z)\ge f(y-z)=2.
\]

Suppose \(f\ne g\). Since both \(f(x)\) and \(g(x)\) equal \(1\), the two facets meet at a vertex of the octagon; hence they are adjacent. Dihedral symmetry reduces every ordered adjacent pair to
\[
f(s,t)=s,
\qquad
g(s,t)=\frac{s+t}{\sqrt2}.
\]
Then
\[
z=(-1,v),\qquad -r\le v\le r,
\]
and
\[
y=(u,\sqrt2-u),\qquad r\le u\le1.
\]
Therefore
\[
N_8(y-z)\ge |u+1|\ge 1+r=\sqrt2.
\]
Thus every triple satisfying the two diameter equalities obeys
\[
N_8(y-z)\ge\sqrt2.
\]

Equality is attained. Take
\[
x=(1,r),\qquad
y=(r,1),\qquad
z=(-1,r).
\]
Then
\[
N_8(x)=N_8(y)=N_8(z)=1,
\]
\[
N_8(x-z)=N_8(x+y)=2,
\]
and
\[
N_8(y-z)=\sqrt2.
\]

We now convert this geometric minimum into the generalized James threshold.

If \(a>\sqrt2\), the displayed triple is admissible and immediately gives \(J(a,X_8)=2\). At the endpoint \(a=\sqrt2\), the defining inequality is strict, so replace \(y\) by
\[
y_\varepsilon=(1-\varepsilon)y,\qquad 0<\varepsilon<1.
\]
Then \(y_\varepsilon\in B_{X_8}\),
\[
N_8(y_\varepsilon-z)<\sqrt2,
\]
and
\[
N_8(x+y_\varepsilon)\longrightarrow2
\]
as \(\varepsilon\downarrow0\), while \(N_8(x-z)=2\). Hence the supremum still equals \(2\):
\[
J(\sqrt2,X_8)=2.
\]

Conversely, suppose \(J(a,X_8)=2\). Choose admissible triples whose two displayed distances tend to \(2\). Compactness of \(B_{X_8}^3\) gives a convergent subsequence. Its limit satisfies
\[
N_8(x-z)=N_8(x+y)=2.
\]
The diameter equality forces \(N_8(x)=1\), and the limiting parameter constraint gives
\[
N_8(y-z)\le a.
\]
The geometric minimum just proved yields
\[
a\ge\sqrt2.
\]
Consequently
\[
J(a,X_8)=2
\quad\Longleftrightarrow\quad
a\ge\sqrt2.
\]

For \(0\le a\le2\), Liu–Din–Li Proposition 4 transfers this exactly to \(C_{-\infty}\). For \(a>2\), their Proposition 2 already gives the maximal value. Hence
\[
C_{-\infty}(a,X_8)=1
\quad\Longleftrightarrow\quad
a\ge\sqrt2.
\]

## Verification
The bundled `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt2)\). It constructs the eight vertices and eight signed supporting facets of the regular octagon, verifies the incidence pattern, and checks every ordered pair of facets that can be simultaneously tight at a point of the unit ball.

For each such pair it certifies, by a signed facet functional, the lower bound
\[
N_8(y-z)\ge\sqrt2
\]
between the relevant exposed faces, with the stronger bound \(2\) when the same facet is used twice. It also verifies the explicit equality triple above and the strict endpoint approximation algebraically. No floating-point sampling is used as a proof.

## Relationship to prior work
Liu, Din and Li introduced \(C_{-\infty}(a,X)\), proved the universal bounds, established the equivalence
\[
C_{-\infty}(a,X)=1\Longleftrightarrow J(a,X)=2
\]
for \(0\le a\le2\), and showed universal saturation for \(a>2\). Their concrete computations concern two Day–James planes and Hilbert spaces; the inspected full text contains no regular-octagon computation.

Yang and Wang computed a different invariant, the exponent-generalized two-variable constant \(C_{NJ}^{(p)}(X)\), on the regular octagon. Its definition has the exponent parameter \(p\) and two vectors, not the three-vector separation parameter \(a\) used by \(C_{-\infty}(a,X)\) and \(J(a,X)\). Thus their exact regular-octagon profile does not imply the present saturation threshold.

The result identifies the exact point where a later generalized minimum von Neumann–Jordan invariant reaches its maximal value on the canonical regular octagonal plane.

## Limitations
The result determines only the saturation set
\[
\{a\ge0:C_{-\infty}(a,X_8)=1\}=[\sqrt2,\infty).
\]
It does not give a closed formula for \(C_{-\infty}(a,X_8)\) on \(0\le a<\sqrt2\).

The proof is specific to the regular octagon. It does not classify saturation thresholds for all regular polygonal norms or all symmetric absolute norms.

Bibliographic and research-index searches cannot prove absolute novelty. The main residual risk is an equivalent generalized-James threshold hidden under different notation; no such statement was found in the inspected defining paper, the regular-octagon \(C_{NJ}^{(p)}\) paper, the checked public research records, or the direct exact-phrase searches.

## References
1. Q. Liu, A. Din and Y. Li, “Some aspects of generalized von Neumann-Jordan type constant,” AIMS Mathematics 6 (2021), 6309–6321, doi:10.3934/math.2021370. Publisher public date: 12 April 2021. Primary MSC: 46B20.
2. C. Yang and T. Wang, “Generalized von Neumann-Jordan constant \(C_{NJ}^{(p)}(X)\) for the regular octagon space,” Mathematical Inequalities & Applications 20 (2017), 483–490, doi:10.7153/mia-20-32.
