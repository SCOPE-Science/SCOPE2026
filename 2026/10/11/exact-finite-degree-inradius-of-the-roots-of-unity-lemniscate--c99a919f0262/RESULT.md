# Exact finite-degree inradius of the roots-of-unity lemniscate

## Finding

For every integer
\[
n\ge1,
\]
consider the roots-of-unity polynomial
\[
p_n(z)=z^n-1
\]
and its strict filled lemniscate
\[
\Omega_n
=
\{z\in\mathbb C:|z^n-1|<1\}.
\]
Let
\[
\rho(p_n)
=
\sup\{R>0:\exists c\in\mathbb C,\ B(c,R)\subset\Omega_n\}.
\]

Set
\[
\alpha_n
=
\frac{\pi}{2(n+1)},
\qquad
q_n
=
(2\sin\alpha_n)^{1/n},
\qquad
H_n
=
q_n\sin\alpha_n.
\]
Then
\[
\rho(z^n-1)=H_n.
\]
Equivalently,
\[
\rho(z^n-1)
=
(2\sin\alpha_n)^{1/n}\sin\alpha_n.
\]

In the principal lobe, one largest disk has center
\[
c_n=q_n\cos\alpha_n
\]
and radius
\[
H_n.
\]
Rotating this disk by the \(n\)-th roots of unity gives largest disks in the other lobes.

The source had already proved the upper bound
\[
\rho(z^n-1)\le H_n
\]
from the exact vertical width of a lobe. The new point is that this width obstruction is attained at every finite degree.

The exact formula also gives
\[
\rho(z^n-1)
=
\frac{\pi}{2n}
\left[
1+\frac{\log(\pi/n)-1}{n}
+
O\!\left(\frac{(\log n)^2}{n^2}\right)
\right].
\]
Thus the canonical obstruction approaches the asymptotic coefficient
\[
\frac{\pi}{2}
\]
from below with a logarithmically enhanced second-order deficit.

## Assumptions and scope

The inradius uses open Euclidean disks and the strict sublevel set
\[
|p_n(z)|<1.
\]
The center is unrestricted.

The source proves that any disk contained in
\[
\Omega_n
\]
lies in one lobe and can be rotated into the principal lobe without changing its radius. It also proves that the principal lobe lies in the strip
\[
|\operatorname{Im}z|<H_n.
\]
Consequently no inscribed disk can have radius larger than
\[
H_n.
\]

The present argument supplies the matching disk inclusion. It determines the inradius of the particular model
\[
z^n-1.
\]
It does not prove that this polynomial minimizes the inradius among all admissible monic degree-\(n\) polynomials at each finite degree.

## Proof

The case
\[
n=1
\]
is immediate:
\[
\Omega_1=B(1,1).
\]
Here
\[
\alpha_1=\frac{\pi}{4},
\qquad
q_1=\sqrt2,
\qquad
c_1=1,
\qquad
H_1=1.
\]

Assume now
\[
n\ge2.
\]
Write
\[
\beta_n=\frac{\pi}{2n}.
\]
The source's direct expansion gives
\[
|r^ne^{in\theta}-1|<1
\quad\Longleftrightarrow\quad
r^n<2\cos(n\theta).
\]
Hence the principal lobe has boundary curve
\[
\gamma(\theta)
=
r(\theta)e^{i\theta},
\qquad
r(\theta)
=
(2\cos(n\theta))^{1/n},
\qquad
-\beta_n<\theta<\beta_n,
\]
together with the cusp at the origin.

Define
\[
\alpha=\alpha_n,
\qquad
q=q_n,
\qquad
c=c_n=q\cos\alpha,
\qquad
H=H_n=q\sin\alpha.
\]
Since
\[
0<c<2^{1/n},
\]
the point
\[
c
\]
lies inside the principal lobe.

For
\[
0<\theta<\beta_n,
\]
consider the squared distance from the proposed center to the boundary,
\[
D(\theta)
=
|r(\theta)e^{i\theta}-c|^2.
\]
Because
\[
\frac{r'(\theta)}{r(\theta)}
=
-\tan(n\theta),
\]
direct differentiation yields
\[
D'(\theta)
=
\frac{2r(\theta)}{\cos(n\theta)}
\left[
c\sin((n+1)\theta)
-
r(\theta)\sin(n\theta)
\right].
\]

The denominator and the trigonometric factors are positive on this interval. Introduce
\[
J(\theta)
=
\frac{r(\theta)\sin(n\theta)}
{\sin((n+1)\theta)}.
\]
Then
\[
\operatorname{sign}D'(\theta)
=
\operatorname{sign}(c-J(\theta)).
\]

A direct logarithmic differentiation of
\[
J
\]
shows that the sign of
\[
J'(\theta)
\]
is the sign of
\[
n\sin\theta\cos(n\theta)
-
\sin(n\theta)\cos\theta,
\]
or equivalently the sign of
\[
n\tan\theta-\tan(n\theta).
\]
The function
\[
x\longmapsto\frac{\tan x}{x}
\]
is strictly increasing on
\[
(0,\pi/2).
\]
Since
\[
0<\theta<n\theta<\pi/2,
\]
we obtain
\[
\tan(n\theta)>n\tan\theta.
\]
Therefore
\[
J'(\theta)<0.
\]

At
\[
\theta=\alpha,
\]
the identity
\[
n\alpha=\frac{\pi}{2}-\alpha
\]
gives
\[
r(\alpha)=q,
\qquad
\sin(n\alpha)=\cos\alpha,
\qquad
\sin((n+1)\alpha)=1.
\]
Thus
\[
J(\alpha)=q\cos\alpha=c.
\]
Because
\[
J
\]
is strictly decreasing,
\[
D'(\theta)<0
\quad\text{for}\quad
0<\theta<\alpha,
\]
and
\[
D'(\theta)>0
\quad\text{for}\quad
\alpha<\theta<\beta_n.
\]
Hence
\[
D
\]
has its unique minimum on the positive boundary arc at
\[
\theta=\alpha.
\]
By symmetry, the corresponding negative point is also minimizing.

At the minimizing point,
\[
D(\alpha)
=
q^2+q^2\cos^2\alpha
-
2q^2\cos^2\alpha
=
q^2\sin^2\alpha
=
H^2.
\]
The cusp at the origin is the endpoint limit of the same boundary arc and is no closer. Therefore the Euclidean distance from
\[
c
\]
to the boundary of the principal lobe is exactly
\[
H.
\]
It follows that
\[
B(c,H)
\]
is contained in the principal lobe.

The source's strip argument gives the reverse inequality
\[
\rho(z^n-1)\le H.
\]
Consequently
\[
\rho(z^n-1)=H.
\]

For the asymptotic expansion, write
\[
\alpha_n
=
\frac{\pi}{2(n+1)}.
\]
Then
\[
n\sin\alpha_n
=
\frac{\pi}{2}
\left(
1-\frac1n+O(n^{-2})
\right),
\]
and
\[
\log q_n
=
\frac1n\log(2\sin\alpha_n)
=
\frac{\log(\pi/n)}{n}
+
O\!\left(\frac1{n^2}\right).
\]
Therefore
\[
q_n
=
1+\frac{\log(\pi/n)}{n}
+
O\!\left(\frac{(\log n)^2}{n^2}\right).
\]
Multiplication yields
\[
nH_n
=
\frac{\pi}{2}
\left[
1+\frac{\log(\pi/n)-1}{n}
+
O\!\left(\frac{(\log n)^2}{n^2}\right)
\right],
\]
which is the claimed expansion.

## Verification

The critical finite-degree step is the exact distance minimization, not numerical sampling.

The derivative identity
\[
\frac{r'}r=-\tan(n\theta)
\]
was substituted directly into the derivative of
\[
D(\theta)
=
r(\theta)^2+c^2-2cr(\theta)\cos\theta.
\]
This reduces the sign of
\[
D'
\]
to comparison with
\[
J(\theta).
\]

The monotonicity of
\[
J
\]
uses only the elementary strict inequality
\[
\tan(n\theta)>n\tan\theta
\]
for
\[
0<\theta<\frac{\pi}{2n},
\]
which follows from strict increase of
\[
\tan x/x.
\]

At
\[
\theta=\alpha_n,
\]
all trigonometric identities are exact, and the squared distance simplifies exactly to
\[
H_n^2.
\]
Thus the disk inclusion is a continuum proof for every degree.

The asymptotic expansion follows from
\[
2\sin\alpha_n
=
\frac{\pi}{n+1}\operatorname{sinc}\alpha_n
\]
and ordinary Taylor expansions. The stated remainder is deliberately coarser than the available expansion and is uniform as
\[
n\to\infty.
\]

No finite enumeration, plot, or numerical optimizer is used as evidence for the exact inradius.

## Relationship to prior work

Erdős, Herzog, and Piranian used
\[
z^n-1
\]
in 1958 to show that the universal inverse-degree inradius coefficient cannot exceed
\[
\pi/2.
\]
Their formulation is asymptotic and does not state the exact finite-\(n\) inradius of the model.

Krishnapur, Lundberg, and Ramachandran later described the roots-of-unity configuration as the conjectural extremal model for the deterministic inradius problem while proving lower bounds for the universal inradius. Their work likewise does not provide the exact finite-degree model inradius.

Geng and Qiu proved the sharp asymptotic law
\[
nR_n\to\frac{\pi}{2}.
\]
For their upper obstruction they introduced the exact quantities
\[
\alpha_n,\ q_n,\ H_n
\]
and proved
\[
\rho(z^n-1)\le H_n
\]
by bounding the principal lobe inside a horizontal strip. Their argument then uses only
\[
nH_n\to\frac{\pi}{2}.
\]
The inspected source does not construct a disk of radius
\[
H_n
\]
or assert finite-degree equality.

The present result closes precisely that model-geometry gap: the strip bound is attained by an explicit disk whose two nearest boundary points occur at arguments
\[
\pm\alpha_n.
\]

## Limitations

The result determines the exact inradius only for the roots-of-unity polynomial
\[
z^n-1.
\]
It does not settle whether
\[
R_n=\rho(z^n-1)
\]
for any fixed
\[
n>1.
\]

No uniqueness claim is made for largest disk centers. The displayed centers and their rotations are explicit maximizers.

The literature comparison was targeted to the deterministic inradius problem, the roots-of-unity model, exact largest-inscribed-disk formulations, and the recent sharp asymptotic theorem. Older classical lemniscate literature can use different terminology, so an unindexed equivalent finite-degree calculation remains a residual risk.

## References

1. Y. Geng and D. Qiu, *From \(\log 2\) to \(\pi/2\): the sharp asymptotic inradius of polynomial lemniscates*, arXiv:2609.06461v1, first posted 6 September 2026.
2. P. Erdős, F. Herzog, and G. Piranian, *Metric properties of polynomials*, Journal d'Analyse Mathématique 6 (1958), 125–148, DOI: 10.1007/BF02790232.
3. M. Krishnapur, E. Lundberg, and K. Ramachandran, *On the area of polynomial lemniscates*, arXiv:2503.18270, first posted 24 March 2025.
