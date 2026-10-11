# Exact \(\mu_p\) profile of the regular octagonal Banach plane
## Finding
Let
\[
X_8=(\mathbb R^2,N_8),
\qquad
N_8(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\}.
\]
For the Gastinel--Joly generalized rectangular constant
\[
\mu_p(X)
=
\sup_{\substack{x,y\in S_X\\x\perp_B y\\\lambda\ge0}}
\frac{(1+\lambda^p)^{1/p}}{\|x+\lambda y\|},
\qquad p\ge1,
\]
one has the complete profile
\[
\boxed{
\mu_p(X_8)
=
\max\left\{
\left(1+[2(\sqrt2-1)]^p\right)^{1/p},
\frac{\left(1+(2\sqrt2)^p\right)^{1/p}}{1+\sqrt2}
\right\}.
}
\tag{1}
\]

The sharper underlying statement is the exact denominator profile
\[
d_8(\lambda)
:=
\inf_{\substack{x,y\in S_{X_8}\\x\perp_B y}}
N_8(x+\lambda y)
=
\max\left\{
1,
\sqrt2-1+\frac{\lambda}{\sqrt2},
\lambda-(\sqrt2-1)
\right\}
\tag{2}
\]
for every \(\lambda\ge0\). Equivalently, with \(a=\sqrt2-1\),
\[
d_8(\lambda)=
\begin{cases}
1,&0\le\lambda\le2a,\\[4pt]
a+\lambda/\sqrt2,&2a\le\lambda\le2\sqrt2,\\[4pt]
\lambda-a,&\lambda\ge2\sqrt2.
\end{cases}
\tag{3}
\]
A single Birkhoff-orthogonal pair realizes (2) for every parameter:
\[
x=(-a,1),
\qquad
y=(1,0).
\tag{4}
\]

At \(p=1\), (1) gives
\[
\mu_1(X_8)=2\sqrt2-1,
\]
recovering the ordinary rectangular constant. At the opposite endpoint,
\[
\lim_{p\to\infty}\mu_p(X_8)=4-2\sqrt2.
\]
Thus the generalized family has two competing extremal scales rather than the single formula \(2^{1/p}\) occurring for the regular hexagonal norm in the defining literature.

## Assumptions and scope
All spaces and scalars are real. Birkhoff--James orthogonality is
\[
x\perp_B y
\quad\Longleftrightarrow\quad
\|x+\tau y\|\ge\|x\|
\quad\text{for every }\tau\in\mathbb R.
\]
Put
\[
r=\sqrt2,
\qquad
a=r-1,
\qquad
b=2-r.
\]
The regular octagonal unit ball has vertices
\[
(1,a),\ (a,1),\ (-a,1),\ (-1,a)
\]
and their negatives. Its facet functionals are the signed coordinate functionals and the four signed diagonal functionals
\[
\frac{(\pm1,\pm1)}{r}.
\]

The statement computes the exact generalized rectangular constant for every exponent \(p\ge1\), not merely a numerical value at one exponent. Formula (2) is stronger: it determines the smallest possible denominator at every scale \(\lambda\ge0\).

## Proof
Fix \(\lambda\ge0\). By the dihedral symmetry of the regular octagon, a norming functional witnessing a Birkhoff-orthogonal pair may be moved into the sector between
\[
f_0=(0,1)
\quad\text{and}\quad
f_1=\frac{(1,1)}{r}.
\]
There are two boundary cases and one interior case.

First suppose the witnessing functional is \(f_0\). Then
\[
x=(s,1),
\qquad |s|\le a,
\]
and a unit vector in \(\ker f_0\) is \(y=(\varepsilon,0)\), with \(\varepsilon\in\{-1,1\}\). Hence
\[
N_8(x+\lambda y)=N_8(s+\varepsilon\lambda,1).
\]
For \(q\ge0\),
\[
N_8(q,1)=\max\left\{1,q,\frac{q+1}{r}\right\}.
\]
The smallest possible value of \(|s+\varepsilon\lambda|\) is
\[
q_0=\max\{0,\lambda-a\}.
\]
Therefore the exact minimum in this boundary class is
\[
\max\left\{1,\lambda-a,\frac{\lambda-a+1}{r}\right\}
=
\max\left\{1,\lambda-a,a+\frac{\lambda}{r}\right\},
\tag{5}
\]
where the last identity uses
\[
\frac{1-a}{r}=a.
\]
The fixed choice in (4) attains (5) for every \(\lambda\ge0\). The other boundary functional \(f_1\) is equivalent by an octagonal isometry.

Now suppose the witnessing functional lies strictly between \(f_0\) and \(f_1\). The exposed point is then the common vertex
\[
x=(a,1).
\]
A unit vector in the kernel can be written, after choosing its sign, as
\[
y=(u,-v),
\qquad
u:=u\ge v\ge0,
\qquad
N_8(u,-v)=1.
\]
The regular-octagon radial geometry gives
\[
u\ge\frac1r.
\tag{6}
\]
Indeed, either the vertical facet is active and \(u=1\), or the southeast diagonal facet is active and \(u+v=r\), which together with \(u\ge v\) gives \(u\ge r/2=1/r\).

Three independent lower bounds now hold. Birkhoff orthogonality gives
\[
N_8(x+\lambda y)\ge1.
\tag{7}
\]
The first coordinate and (6) give
\[
N_8(x+\lambda y)\ge a+\lambda u
\ge a+\frac{\lambda}{r}.
\tag{8}
\]
Finally choose a norming functional \(g\) for \(y\). If the vertical facet is active, take \(g=(1,0)\), so \(g(x)=a\). If the diagonal facet is active, take
\[
g=\frac{(1,-1)}{r},
\]
so
\[
g(x)=\frac{a-1}{r}=-a.
\]
Thus in all cases \(g(x)\ge-a\), and
\[
N_8(x+\lambda y)
\ge g(x+\lambda y)
=\lambda+g(x)
\ge\lambda-a.
\tag{9}
\]
Equations (7)--(9) give the right-hand side of (2). Since the fixed pair (4) attains that bound, (2) follows.

The switch points in (3) are obtained from
\[
1=a+\frac{\lambda}{r}
\quad\Longleftrightarrow\quad
\lambda=2a,
\]
and
\[
a+\frac{\lambda}{r}=\lambda-a
\quad\Longleftrightarrow\quad
\lambda=2r.
\]

It remains to optimize the numerator of \(\mu_p\) against (3). Since suprema over \((x,y)\) and \(\lambda\) commute,
\[
\mu_p(X_8)
=
\sup_{\lambda\ge0}
\frac{(1+\lambda^p)^{1/p}}{d_8(\lambda)}.
\tag{10}
\]
On \([0,2a]\), the denominator is \(1\), so the quotient is increasing and its maximum is
\[
A_p=
\left(1+[2a]^p\right)^{1/p}.
\tag{11}
\]
On \([2a,2r]\), write
\[
h_p(\lambda)
=
\frac{r(1+\lambda^p)^{1/p}}{\lambda+b}.
\]
Its logarithmic derivative has the sign of
\[
b\lambda^{p-1}-1.
\tag{12}
\]
For \(p=1\), this is negative. For \(p>1\), it changes sign at most once, from negative to positive. Hence \(h_p\) has no interior maximum; its maximum occurs at one of the two endpoints.

On \([2r,\infty)\), the logarithmic derivative of
\[
\frac{(1+\lambda^p)^{1/p}}{\lambda-a}
\]
has the sign of
\[
-a\lambda^{p-1}-1<0,
\]
so the maximum occurs at \(\lambda=2r\), with value
\[
B_p=
\frac{\left(1+(2r)^p\right)^{1/p}}{1+r}.
\tag{13}
\]
Combining (11)--(13) proves (1).

## Verification
The proof is analytic. Its critical nonstandard step is the complete support-functional reduction leading to the exact denominator profile (2).

The bundled `verify.py` reconstructs the octagonal norm and its two canonical support sectors. It checks the fixed equality pair against (2) on a deterministic parameter grid; checks the boundary support family and the interior vertex/kernel family against the lower envelope; verifies the two switch points; and compares direct one-variable optimization with (1) for a representative list of exponents.

These finite checks are reproducibility aids only. They do not replace the continuum support-functional argument or the derivative analysis in the proof.

## Relationship to prior work
Baronti, Casini and Papini revisit the Gastinel--Joly family \(\mu_p\), state its definition, and prove structural characterizations and general bounds. Their paper explicitly computes
\[
\mu_p(X)=2^{1/p}
\]
for the regular hexagonal norm, while its final section gives upper estimates for \(\ell_p\) spaces. Full-text searches for “octagon” and “octagonal” return no occurrence, and the inspected paper contains no regular-octagonal calculation.

A 2024 paper by Xie, Fu and Li titled “Generalized rectangular constant in Banach spaces” was also inspected because its title is potentially confusable with \(\mu_p\). That paper explicitly recalls \(\mu_p\) as background, then introduces different two-parameter quantities \(\mu(X,a)\) and \(\mu'(X,a)\). Its full text does not supply the exponent profile (1).

The ordinary value
\[
\mu_1(X_8)=2\sqrt2-1
\]
is already a special case available from a separate exact computation. Formula (1) is not a routine restatement of that endpoint: the optimizer changes between the two intrinsic scales
\[
\lambda=2(\sqrt2-1)
\quad\text{and}\quad
\lambda=2\sqrt2,
\]
and the all-\(p\) result rests on the stronger denominator profile (2).

The closest public result found for the same generalized rectangular family is an exact computation of \(\mu_4\) on the smooth plane \(\ell_4^2\), a different space with a different Birkhoff-orthogonality equation. Nearby regular-octagon results concern von Neumann--Jordan, angle-modulus, Ptolemy, and other constants and do not imply (1) or (2).

## Limitations
The theorem concerns the Euclidean regular octagonal norm and does not give the generalized rectangular profile for arbitrary regular polygons or arbitrary affine images of the octagon.

Formula (1) is stated as the maximum of two explicit branches. No claim is made here about a closed elementary expression for the unique exponent, if any, at which those two branches cross.

Bibliographic and semantic searches cannot prove absolute novelty. Older literature on rectangular constants may contain equivalent calculations under another normalization or notation, although the defining modern full text, the later similarly titled full text, targeted web searches, and the public research index did not expose such a formula.

## References
1. M. Baronti, E. Casini and P. L. Papini, “Revisiting the rectangular constant in Banach spaces,” *Bulletin of the Australian Mathematical Society* 105 (2022), 124–133, doi:10.1017/S0004972721000253. First published online 26 April 2021.
2. H. Xie, Y. Fu and Y. Li, “Generalized rectangular constant in Banach spaces,” *Analysis Mathematica* 50 (2024), 667–681, doi:10.1007/s10476-024-00034-9. First published online 3 July 2024.
