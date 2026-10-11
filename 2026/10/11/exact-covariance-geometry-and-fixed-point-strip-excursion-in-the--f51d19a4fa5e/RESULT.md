# Exact covariance geometry and fixed-point-strip excursion in the Bogdanov map
## Finding
Consider the Bogdanov map
\[
Y=(1+\varepsilon)y+kx(x-1)+\mu xy,
\qquad
X=x+Y,
\]
where \((X,Y)\) denotes the image of \((x,y)\).

Let \(\nu\) be any compactly supported invariant Borel probability measure. Then
\[
\boxed{\mathbb E_\nu[y]=0}
\]
and the two coordinate fluctuations obey the exact covariance law
\[
\boxed{
\operatorname{Cov}_\nu(x,y)
=
\frac12\operatorname{Var}_\nu(y)
}.
\]
The parameters enter through a second exact stationary balance:
\[
\boxed{
k\,\mathbb E_\nu[x(x-1)]
+
\frac{\mu}{2}\operatorname{Var}_\nu(y)
=
0
}.
\]

In the supercritical-Hopf sign regime
\[
k>0,\qquad \mu<0,
\]
this becomes the fixed-point-strip moment law
\[
\boxed{
\mathbb E_\nu\!\left[
\left(x-\frac12\right)^2
\right]
=
\frac14
-
\frac{\mu}{2k}\operatorname{Var}_\nu(y)
}.
\]
The two fixed points of the map are
\[
(0,0),\qquad (1,0).
\]
The variance
\[
\operatorname{Var}_\nu(y)
\]
vanishes exactly when \(\nu\) is supported on those two fixed points. Therefore every other compact stationary state satisfies
\[
\boxed{
\mathbb E_\nu\!\left[
\left(x-\frac12\right)^2
\right]
>
\frac14
}
\]
and consequently assigns positive mass to the strict exterior of the fixed-point strip:
\[
\boxed{
\nu\{x<0\ \text{or}\ x>1\}>0
}.
\]

The covariance law also gives a parameter-independent sharp inequality:
\[
\boxed{
\operatorname{Var}_\nu(x)
\ge
\frac14\operatorname{Var}_\nu(y)
}.
\]
If
\[
\operatorname{Var}_\nu(y)>0,
\]
equality is dynamically rigid. It forces
\[
y=2(x-m)
\quad\text{almost surely},
\qquad
m=\mathbb E_\nu[x].
\]
At the image point the same relation holds, while
\[
X=x+Y.
\]
Combining the two relations gives
\[
\boxed{
Y=-y,
\qquad
X-m=-(x-m)
}
\]
almost surely. Hence a second iterate returns the state:
\[
\boxed{
T^2(x,y)=(x,y)
}
\]
almost surely.

Thus every ergodic invariant measure with positive \(y\)-variance that is not supported on a two-cycle obeys
\[
\boxed{
\operatorname{Var}_\nu(x)
>
\frac14\operatorname{Var}_\nu(y)
}
\]
and
\[
\boxed{
0<
\operatorname{Corr}_\nu(x,y)
<
1
}.
\]
In fact
\[
\operatorname{Corr}_\nu(x,y)
=
\frac12
\sqrt{
\frac{\operatorname{Var}_\nu(y)}
{\operatorname{Var}_\nu(x)}
}.
\]

## Assumptions and scope
The result concerns the classical planar quadratic Bogdanov map
\[
X=x+Y,
\qquad
Y=(1+\varepsilon)y+kx(x-1)+\mu xy.
\]
Compact support is used only to guarantee the first and second moments required by the proof.

No ergodicity assumption is needed for the exact mean, covariance, parameter balance, or fixed-point-strip excursion. Ergodicity is used only to state the equality case as a single two-cycle rather than a possible invariant mixture of period-at-most-two orbits.

The classical full-text source explains that \(\mu<0\) produces the supercritical Hopf branch at the origin, while \(k>0\) selects the fixed point at the origin as the one undergoing the bifurcation. The strict fixed-point-strip statement is therefore aligned with the parameter orientation used to generate attracting invariant circles and their later complicated dynamics.

The earliest checked day-resolved public full-text source is the preprint posted on 22 February 1994. A later quadratic-map study that treats the Bogdanov family lists \(37D45\) first in its Mathematics Subject Classification; that classification is used here.

## Proof
Write the map as
\[
T(x,y)=(X,Y).
\]
Invariance means that
\[
(X,Y)
\]
has the same distribution as
\[
(x,y).
\]

Because
\[
X-x=Y,
\]
stationarity of the first coordinate gives
\[
0
=
\mathbb E[X-x]
=
\mathbb E[Y].
\]
By invariance,
\[
\mathbb E[Y]=\mathbb E[y],
\]
so
\[
\mathbb E[y]=0.
\]

Now use stationarity of the second moment of \(x\):
\[
0
=
\mathbb E[X^2-x^2]
=
2\mathbb E[xY]+\mathbb E[Y^2].
\]
Since
\[
\mathbb E[Y^2]=\mathbb E[y^2],
\]
we have
\[
\mathbb E[xY]
=
-\frac12\mathbb E[y^2].
\]

Next use stationarity of the mixed moment:
\[
\mathbb E[XY]
=
\mathbb E[xy].
\]
Since
\[
XY=(x+Y)Y=xY+Y^2,
\]
we obtain
\[
\mathbb E[xy]
=
\mathbb E[xY]+\mathbb E[y^2]
=
\frac12\mathbb E[y^2].
\]
Because
\[
\mathbb E[y]=0,
\]
this is exactly
\[
\operatorname{Cov}(x,y)
=
\frac12\operatorname{Var}(y).
\]

Taking expectations in the \(Y\)-equation and using
\[
\mathbb E[Y]=\mathbb E[y]=0
\]
gives
\[
k\,\mathbb E[x(x-1)]
+
\mu\,\mathbb E[xy]
=
0.
\]
Substitution of the covariance identity yields
\[
k\,\mathbb E[x(x-1)]
+
\frac{\mu}{2}\operatorname{Var}(y)
=
0.
\]

For
\[
k>0,\qquad \mu<0,
\]
complete the square:
\[
x(x-1)
=
\left(x-\frac12\right)^2-\frac14.
\]
Hence
\[
\mathbb E\!\left[
\left(x-\frac12\right)^2
\right]
=
\frac14
-
\frac{\mu}{2k}\operatorname{Var}(y).
\]

Suppose
\[
\operatorname{Var}(y)=0.
\]
Since
\[
\mathbb E[y]=0,
\]
we have
\[
y=0
\]
almost surely. Invariance then gives
\[
Y=0
\]
almost surely. The \(Y\)-equation reduces to
\[
0=kx(x-1).
\]
For \(k>0\), the support is therefore contained in
\[
x\in\{0,1\}.
\]
Both points
\[
(0,0),\qquad (1,0)
\]
are fixed. Conversely, every probability measure supported on these two fixed points is invariant and has zero \(y\)-variance.

Thus every invariant measure not supported on the two fixed points has
\[
\operatorname{Var}(y)>0.
\]
When \(\mu<0\), the centered-square identity then gives
\[
\mathbb E\!\left[
\left(x-\frac12\right)^2
\right]>\frac14.
\]
If the support were contained in
\[
0\le x\le1,
\]
the pointwise inequality
\[
\left(x-\frac12\right)^2\le\frac14
\]
would contradict the strict expectation. Hence there is positive invariant mass in
\[
x<0
\quad\text{or}\quad
x>1.
\]

Finally, positive semidefiniteness of the covariance matrix gives
\[
\operatorname{Cov}(x,y)^2
\le
\operatorname{Var}(x)\operatorname{Var}(y).
\]
Using
\[
\operatorname{Cov}(x,y)
=
\frac12\operatorname{Var}(y)
\]
gives
\[
\operatorname{Var}(x)
\ge
\frac14\operatorname{Var}(y).
\]

Assume
\[
\operatorname{Var}(y)>0
\]
and equality holds. Equality in Cauchy–Schwarz forces
\[
x-m=\frac12y
\]
almost surely, where
\[
m=\mathbb E[x].
\]
The same relation holds at the image point:
\[
X-m=\frac12Y.
\]
Since
\[
X=x+Y,
\]
we have
\[
x-m+Y=\frac12Y.
\]
Using
\[
x-m=\frac12y
\]
gives
\[
Y=-y.
\]
It follows that
\[
X-m
=
-\frac12y
=
-(x-m).
\]
Applying the same argument at the next iterate returns both centered coordinates. Hence
\[
T^2=\mathrm{id}
\]
almost surely on the invariant state.

An ergodic probability for a transformation whose square is the identity almost surely is supported on one orbit of cardinality at most two. Since the variance is nonzero, it is a two-cycle. This proves the strict inequality and strict correlation bound for every other ergodic nondegenerate state.

## Verification
The packaged checker uses only the Python standard library and exact rational arithmetic.

It verifies the stationary moment algebra generated by
\[
X=x+Y,
\]
including
\[
\mathbb E[xy]
=
\frac12\mathbb E[y^2],
\]
the parameter balance
\[
k\,\mathbb E[x(x-1)]
+
\frac{\mu}{2}\mathbb E[y^2]
=
0,
\]
and the fixed-point-strip square completion.

It also checks the covariance-determinant inequality algebraically and verifies that the equality-line relation
\[
x-m=\frac12y
\]
together with
\[
X=x+Y
\]
and the same image relation forces
\[
(X-m,Y)=(-(x-m),-y).
\]

The stored output in `verification_output.txt` is `VERIFY_OK`.

No finite orbit enumeration, floating-point trajectory, or numerical bifurcation diagram is used as proof.

## Relationship to prior work
The classical Bogdanov-map paper derives
\[
X=x+Y,
\qquad
Y=y+\varepsilon y+kx(x-1)+\mu xy
\]
from an Euler discretization of the Bogdanov vector field. It develops the fixed points, Hopf and period-doubling bifurcations, mode locking, Arnold tongues, homoclinic tangles, and chaos. Its complete searchable text contains no occurrence of `moment`, `variance`, `covariance`, `invariant measure`, or `average`.

That paper also records the sign distinction relevant here: at the origin the Hopf bifurcation is supercritical for
\[
\mu<0.
\]
The present fixed-point-strip excess is therefore a global stationary constraint in the same sign regime in which an attracting invariant circle is born.

A later study of homoclinic zones for quadratic maps treats the Bogdanov family explicitly and studies exponentially thin chaotic parameter zones near Bogdanov–Takens homoclinic bifurcation. Its stated results concern splitting and parameter-zone widths, not invariant-measure moments.

Modern applied work uses the Bogdanov map to model dissipative optical resonators and continues to analyze fixed points, Lyapunov behavior, and chaotic parameter regions. Those studies do not implication-wise provide the universal covariance identity or the period-two equality classification proved here.

The accepted claim does not re-claim the known fixed points, bifurcation diagram, area-preserving limit, or existence of chaotic regimes. It is an all-invariant-measures second-order law derived from the shear relation
\[
X=x+Y
\]
and the quadratic update.

## Limitations
The theorem supplies exact first- and second-moment constraints but does not determine an invariant density, entropy, Lyapunov exponents, or basin geometry.

The strict fixed-point-strip excursion uses
\[
k>0,\qquad \mu<0.
\]
The covariance identity itself holds for all real parameters for which a compactly supported invariant probability measure exists.

The equality classification concerns the covariance determinant. It does not classify the location or stability of all two-cycles; it only proves that equality can occur nowhere else when
\[
\operatorname{Var}(y)>0.
\]

The historical journal article appeared before the checked preprint, but the structured date uses the earliest checked day-resolved public full-text source rather than inventing a day for an incompletely resolved earlier record.

Because the stationary calculation is short, a differently phrased equivalent identity could remain in unindexed literature.

## References
1. D. K. Arrowsmith, J. H. E. Cartwright, A. N. Lansbury, and C. M. Place, “The Bogdanov Map: Bifurcations, Mode Locking, and Chaos in a Dissipative System,” International Journal of Bifurcation and Chaos 3, 803–842 (1993), DOI 10.1142/S021812749300074X; public preprint arXiv:chao-dyn/9402006.
2. V. Gelfreich and V. Naudot, “Width of the Homoclinic Zone in the Parameter Space for Quadratic Maps,” Experimental Mathematics 18, 409–427 (2009), DOI 10.1080/10586458.2009.10129058; preprint arXiv:0805.0324.
3. V. Aboites, D. Liceaga, R. Jaimes-Reátegui, and J. H. García-López, “Bogdanov Map for Modelling a Phase-Conjugated Ring Resonator,” Entropy 21, 384 (2019), DOI 10.3390/e21040384.
