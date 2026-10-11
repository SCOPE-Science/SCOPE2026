# Sharp chord-imbalance envelope for the isosceles Dunkl--Williams integrand
## Finding
Let \(X\) be a real Banach space and let \(x,y\in S_X\) with \(x\ne\pm y\). Define the Fu--Xie--Li unit-pair integrand
\[
\Phi_X(x,y)
=
\frac{\|x+y\|+\|x-y\|}{2}
\left\|
\frac{x+y}{\|x+y\|}
-
\frac{x-y}{\|x-y\|}
\right\|
\]
and its sum/difference chord-imbalance ratio
\[
\rho(x,y)
=
\frac{\min\{\|x+y\|,\|x-y\|\}}
{\max\{\|x+y\|,\|x-y\|\}}
\in(0,1].
\]

For every fixed \(0<r\le1\), the exact universal envelope is
\[
\boxed{
\sup_{\substack{X,\ x,y\in S_X,\ x\ne\pm y\\ \rho(x,y)=r}}
\Phi_X(x,y)
=
2+r-r^2
=
\frac94-\left(r-\frac12\right)^2
}.
\]
The supremum ranges over all real Banach spaces of dimension at least two, and it is attained already in \(\ell_\infty^2\).

Consequently, the sharp universal estimate \(DW_I(X)\le9/4\) has the exact stability law
\[
\Phi_X(x,y)\ge\frac94-\delta
\quad\Longrightarrow\quad
\left|\rho(x,y)-\frac12\right|\le\sqrt{\delta}.
\]
No smaller right-hand side depending only on \(\rho\) is possible.

There is also a complete pairwise equality criterion. An admissible pair \(x,y\) attains
\[
\Phi_X(x,y)=\frac94
\]
if and only if there is \(\sigma\in\{-1,1\}\) such that
\[
\|x+\sigma y\|=2,
\qquad
\|x-\sigma y\|=1,
\qquad
\|3\sigma y-x\|=3.
\]

## Assumptions and scope
All scalar fields are real. The result concerns the unit-pair representation of the Dunkl--Williams constant related to isosceles orthogonality. Fu, Xie and Li proved
\[
DW_I(X)
=
\sup_{\substack{x,y\in S_X\\x\ne\pm y}}
\Phi_X(x,y).
\]
The present statement refines the later sharp bound \(DW_I(X)\le9/4\) by conditioning on the intrinsic chord ratio \(\rho\).

The equality criterion is a criterion for an individual admissible pair. It does not assert that every Banach space with supremum \(DW_I(X)=9/4\) contains a pair at which the supremum is attained.

## Proof
Fix \(x,y\in S_X\), \(x\ne\pm y\). Replacing \(y\) by \(-y\) leaves \(\Phi_X(x,y)\) unchanged and interchanges the two chord lengths. Hence assume
\[
a=\|x+y\|\ge b=\|x-y\|>0,
\qquad
r=\frac ba.
\]
Put
\[
u=x+y,
\qquad
v=x-y.
\]
Then
\[
\Phi_X(x,y)
=
\frac{a+b}{2ab}\|bu-av\|.
\]
Since
\[
bu-av
=
b(u-v)+(b-a)v,
\]
the triangle inequality and \(u-v=2y\) give
\[
\|bu-av\|
\le
2b+(a-b)b.
\]
Therefore
\[
\Phi_X(x,y)
\le
\frac{a+b}{2a}(2+a-b)
=
\frac{1+r}{2}\bigl(2+a(1-r)\bigr).
\]
Because \(a\le2\),
\[
\Phi_X(x,y)
\le
(1+r)(2-r)
=
2+r-r^2
=
\frac94-\left(r-\frac12\right)^2.
\tag{1}
\]

It remains to show that (1) is sharp for every \(r\). Work in
\[
X=\ell_\infty^2.
\]
For \(0<r\le1\), take
\[
x_r=(1,1-2r),
\qquad
y=(1,1).
\]
Both are unit vectors and \(x_r\ne\pm y\). Moreover,
\[
\|x_r+y\|_\infty=2,
\qquad
\|x_r-y\|_\infty=2r,
\]
so
\[
\rho(x_r,y)=r.
\]
The normalized sum and difference are
\[
\frac{x_r+y}{\|x_r+y\|_\infty}
=
(1,1-r),
\qquad
\frac{x_r-y}{\|x_r-y\|_\infty}
=
(0,-1).
\]
Their distance is
\[
\|(1,2-r)\|_\infty=2-r.
\]
Hence
\[
\Phi_{\ell_\infty^2}(x_r,y)
=
(1+r)(2-r)
=
2+r-r^2.
\]
This proves the exact fixed-\(r\) envelope.

For the global equality criterion, continue under \(a\ge b\). Equality
\[
\Phi_X(x,y)=\frac94
\]
forces equality at every step in the chain
\[
\Phi_X(x,y)
\le
\frac{1+r}{2}\bigl(2+a(1-r)\bigr)
\le
(1+r)(2-r)
\le
\frac94.
\]
The last equality gives
\[
r=\frac12.
\]
Since \(r<1\), equality in the middle step forces
\[
a=2,
\]
and hence
\[
b=1.
\]
Equality in the first triangle estimate is then exactly
\[
\|bu-av\|
=
3.
\]
With \(a=2\) and \(b=1\),
\[
bu-av
=
(x+y)-2(x-y)
=
3y-x,
\]
so the remaining condition is
\[
\|3y-x\|=3.
\]
If initially \(\|x-y\|\ge\|x+y\|\), replace \(y\) by \(-y\). Thus the sign-symmetric criterion is precisely
\[
\|x+\sigma y\|=2,\qquad
\|x-\sigma y\|=1,\qquad
\|3\sigma y-x\|=3
\]
for some \(\sigma\in\{-1,1\}\).

Conversely, these three equalities make every inequality above an equality, so they imply
\[
\Phi_X(x,y)=\frac94.
\]

## Verification
The proof is analytic and uses only the Fu--Xie--Li unit-pair representation, the triangle inequality, and the unit-sphere bound
\[
\|x\pm y\|\le2.
\]

The bundled `verify.py` uses exact rational arithmetic. It checks the \(\ell_\infty^2\) sharpness family for every rational
\[
r=\frac pq
\]
with \(1\le p\le q\le80\), verifies the exact value
\[
\Phi_{\ell_\infty^2}(x_r,y)=2+r-r^2,
\]
and checks the global equality witness at \(r=1/2\). These finite checks are reproducibility aids only; the continuum statement and the equality criterion are proved symbolically above.

## Relationship to prior work
Sain, Ghosh and Paul studied isosceles orthogonality and geometric constants in normed spaces; their article was published online on 1 September 2022 and has primary MSC 46B20.

Fu, Xie and Li introduced \(DW_I(X)\), proved the unit-pair representation used here, and computed
\[
DW_I(\ell_\infty^2)=\frac94.
\]
They conjectured that \(9/4\) should be the optimal universal upper bound.

A later public result proved the conjecture. Its proof contains the upper estimate
\[
\Phi_X(x,y)
\le
2+r-r^2
\]
as an intermediate step and then maximizes over \(r\), obtaining \(9/4\). That prior result explicitly makes no classification of equality cases.

The present statement does not re-claim the global \(9/4\) theorem. Its new content is that the intermediate polynomial is the exact best possible envelope at every fixed chord ratio, together with the resulting sharp stability law and the complete criterion for pairwise attainment of \(9/4\). The one-parameter family in \(\ell_\infty^2\) proves pointwise optimality for every \(0<r\le1\).

## Limitations
The equality criterion classifies attaining pairs, not spaces whose supremum equals \(9/4\) without attainment.

The profile is universal with respect to the single scalar parameter \(\rho\). It does not classify the finer geometry of all pairs that attain the fixed-\(\rho\) envelope when \(\rho\ne1/2\).

The upper polynomial itself occurs in the proof of the previously published sharp global bound. The novelty claimed here is only its pointwise optimality for every chord ratio, the induced sharp stability statement, and the equality-pair classification.

Bibliographic and semantic searches cannot logically exclude every unindexed duplication. A mathematically equivalent equality classification may be stated elsewhere in different notation.

## References
1. D. Sain, S. Ghosh and K. Paul, “On isosceles orthogonality and some geometric constants in a normed space,” *Aequationes Mathematicae* 97 (2023), 147–160, doi:10.1007/s00010-022-00909-y. Published online 1 September 2022.
2. Y. Fu, H. Xie and Y. Li, “The Dunkl-Williams constant related to the Singer orthogonality and red isosceles orthogonality in Banach spaces,” *Filomat* 37 (2023), no. 17, 5601–5622, doi:10.2298/FIL2317601F. Primary MSC 46B20.
3. “Sharp universal bound for the isosceles Dunkl–Williams constant,” public research record, identifier published-finding corpus:3662102e718b (2026).
