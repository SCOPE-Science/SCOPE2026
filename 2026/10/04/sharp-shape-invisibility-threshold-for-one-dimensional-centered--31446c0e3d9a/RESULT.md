# Sharp shape-invisibility threshold for one-dimensional centered maximal fibers

## Finding

Let \(0<\delta<1/2\) and \(0<m<2\delta\). Define
\[
E_\delta=(-1-\delta,-\delta)\cup(\delta,1+\delta),
\qquad
\rho_c=1-2\delta+m,
\]
and, for a measurable \(h\), put \(F_h=\mathbf 1_{E_\delta}+h\).

Assume
\[
\operatorname{supp}h\subset(-\delta,\delta),\qquad
0\le h\le \rho_c\ \text{a.e.},\qquad
\int_{\mathbb R}h(t)\,dt=m.
\]
Then the centered Hardy--Littlewood maximal function
\[
M_cF_h(x)=\sup_{r>0}\frac1{2r}\int_{x-r}^{x+r}F_h(t)\,dt
\]
does not depend on the shape of \(h\). Writing
\[
x_{\delta,m}=\frac{1+3\delta+m\delta}{1+m},
\]
one has
\[
M_cF_h(x)=
\begin{cases}
\displaystyle
1-\frac{\delta-m/2}{1+\delta-|x|},
& |x|\le\delta,\\[8pt]
1,
& \delta<|x|<1+\delta,\\[6pt]
\displaystyle\frac1{2(|x|-\delta)},
&1+\delta\le |x|\le x_{\delta,m},\\[10pt]
\displaystyle\frac{2+m}{2(|x|+1+\delta)},
&|x|>x_{\delta,m}.
\end{cases}
\]

Moreover, the cap \(\rho_c\) is sharp for universal fixed-mass shape-invisibility. For every
\[
\rho_c<\rho\le1,
\]
there are measurable \(h_0,h_1\), both supported in \((-\delta,\delta)\), satisfying
\[
0\le h_j\le\rho,\qquad \int h_j=m,
\]
such that
\[
M_cF_{h_0}\ne M_cF_{h_1}.
\]

Thus, below the exact amplitude threshold, each fixed-mass slice contains an infinite-dimensional convex family on which \(M_c\) is constant, while immediately above that threshold the universal shape-invariance breaks.

## Assumptions and scope

The theorem concerns the one-dimensional centered Hardy--Littlewood maximal operator on nonnegative integrable functions. The perturbation is confined to the central gap between two unit-height towers, its total mass is fixed, and the pointwise amplitude is controlled. The result does not claim a classification of all fibers of \(M_c\), nor does it claim that every perturbation above the threshold changes the maximal function. The sharpness statement is universal: once the allowed amplitude exceeds \(\rho_c\), one can find two admissible shapes of the same mass with different maximal functions.

The class below threshold is nonempty because
\[
\frac{m}{2\delta}\le 1-2\delta+m=\rho_c.
\]
Indeed, after multiplying by \(2\delta\), this is equivalent to
\[
m(1-2\delta)\le 2\delta(1-2\delta),
\]
which follows from \(m\le2\delta\) and \(0<\delta<1/2\).

## Proof

It is enough to prove the formula for \(x\ge0\), because reflection sends an admissible perturbation \(h\) to the equally admissible perturbation \(t\mapsto h(-t)\).

First suppose \(0\le x\le\delta\). Set
\[
r_0=\delta+x,\qquad
r_1=1+\delta-x,\qquad
r_2=1+\delta+x.
\]
For \(0<r\le r_0\), the interval \((x-r,x+r)\) meets at most one tower. Its tower contribution has length at most \(r\), while the remaining contribution has density at most \(\rho_c\). Hence
\[
\frac1{2r}\int_{x-r}^{x+r}F_h
\le \frac{1+\rho_c}{2}
=1-\delta+\frac m2.
\]
For \(r_0\le r\le r_1\), the averaging interval contains the whole central gap and stays inside the two outer tower endpoints. Its tower contribution has length \(2r-2\delta\), and the entire perturbation contributes mass \(m\). Therefore
\[
A(x,r):=\frac1{2r}\int_{x-r}^{x+r}F_h
=
1-\frac{\delta-m/2}{r}.
\]
Since \(m<2\delta\), this is strictly increasing in \(r\). At \(r=r_1\), its value is at least its value at \(r=1\), namely \(1-\delta+m/2\), so no radius below \(r_0\) gives a larger average.

For \(r_1\le r\le r_2\), the right tower is fully included, the left tower is included only partially, and the whole perturbation is still included. Thus
\[
A(x,r)
=
\frac12+\frac{1-\delta+m-x}{2r}.
\]
The numerator \(1-\delta+m-x\) is at least
\[
1-2\delta+m=\rho_c>0,
\]
so this expression decreases with \(r\). For \(r\ge r_2\), the total mass \(2+m\) is fixed and the average decreases as \(r\) grows. Hence the maximum is attained at \(r_1\), giving the first line of the formula.

If \(\delta<x<1+\delta\), then \(x\) lies in the interior of the right tower. Since \(0\le F_h\le1\), arbitrarily small centered intervals give average \(1\), and no average can exceed \(1\). Hence \(M_cF_h(x)=1\).

Now let \(x\ge1+\delta\), and put
\[
r_1=x-\delta,\qquad r_2=x+1+\delta,
\qquad
k=\frac{1+m}{1+2\delta}.
\]
At \(r_1\), the averaging interval contains exactly the whole right tower and no perturbation mass, so
\[
A(x,r_1)=\frac1{2(x-\delta)}.
\]
At \(r_2\), it contains the full support, so
\[
A(x,r_2)=\frac{2+m}{2(x+1+\delta)}.
\]

For \(r_1\le r\le x+\delta\), the right tower is fully contained, the left tower is absent, and only a portion of the perturbation can appear. Since \(h\le\rho_c\),
\[
N(r):=\int_{x-r}^{x+r}F_h
\le 1+\rho_c(r-r_1).
\]
The inequality
\[
\rho_c\le k
\]
is equivalent to
\[
1-2\delta+m
\le
\frac{1+m}{1+2\delta},
\]
and the difference between the right- and left-hand sides is
\[
\frac{2\delta(2\delta-m)}{1+2\delta}>0.
\]
Consequently,
\[
N(r)\le1+k(r-r_1).
\]

For \(x+\delta\le r\le r_2\), the perturbation and the right tower are fully included, while the left tower enters at unit density. Hence
\[
N(r)=2+m-(r_2-r).
\]
Because \(m<2\delta\), one has \(k<1\), so
\[
N(r)
\le
2+m-k(r_2-r)
=
1+k(r-r_1).
\]
Thus throughout \([r_1,r_2]\),
\[
A(x,r)
\le
\frac{k}{2}+\frac{1-kr_1}{2r}.
\]
The right-hand side is monotone, or constant, as a function of \(r\), and it agrees with the true averages at both endpoints. Therefore no interior radius beats both endpoint values:
\[
M_cF_h(x)
=
\max\left\{
\frac1{2(x-\delta)},
\frac{2+m}{2(x+1+\delta)}
\right\}.
\]
The two endpoint expressions are equal exactly when
\[
x=x_{\delta,m}
=
\frac{1+3\delta+m\delta}{1+m}.
\]
Also
\[
x_{\delta,m}-(1+\delta)
=
\frac{2\delta-m}{1+m}>0.
\]
This gives the third and fourth lines of the formula.

It remains to prove sharpness of the amplitude threshold. Let \(\rho_c<\rho\le1\). Define the constant perturbation
\[
h_0(t)=\frac{m}{2\delta}\,\mathbf 1_{(-\delta,\delta)}(t).
\]
Its amplitude is at most \(\rho_c\), so the preceding formula applies and gives
\[
M_cF_{h_0}(\delta)
=
1-\delta+\frac m2
=
\frac{1+\rho_c}{2}.
\]

Choose \(a>0\) so small that \(a<m/\rho\), and set
\[
c=\frac{m-\rho a}{2\delta-a}.
\]
Because \(m\le2\delta\rho\), one has \(0\le c\le\rho\). Define
\[
h_1(t)=
\begin{cases}
c,&-\delta<t<\delta-a,\\
\rho,&\delta-a<t<\delta,\\
0,&\text{otherwise}.
\end{cases}
\]
Then \(0\le h_1\le\rho\), \(\operatorname{supp}h_1\subset(-\delta,\delta)\), and \(\int h_1=m\). For every \(0<r<a\), the interval \((\delta-r,\delta+r)\) consists of a left half on which \(h_1=\rho\) and a right half lying in the unit-height tower. Hence
\[
\frac1{2r}\int_{\delta-r}^{\delta+r}F_{h_1}(t)\,dt
=
\frac{1+\rho}{2}
>
\frac{1+\rho_c}{2}
=
M_cF_{h_0}(\delta).
\]
Therefore \(M_cF_{h_1}(\delta)>M_cF_{h_0}(\delta)\), proving sharpness.

Finally, the below-threshold fiber is infinite-dimensional. The perturbation
\[
h_\ast=\frac{m}{2\delta}\mathbf 1_{(-\delta,\delta)}
\]
lies strictly below \(\rho_c\) when \(m<2\delta\). Any sufficiently small bounded zero-mean perturbation \(q\) supported in \((-\delta,\delta)\) preserves both the mass and the inequalities \(0\le h_\ast+q\le\rho_c\). The zero-mean subspace of \(L^\infty(-\delta,\delta)\) is infinite-dimensional, so a whole infinite-dimensional convex neighborhood inside that affine subspace belongs to one maximal-function fiber.

## Verification

The proof uses only interval geometry and affine bounds on the numerator of a centered average. The supplementary script `verify_shape_threshold.py` checks the algebraic identities exactly with rational arithmetic and exhaustively evaluates the centered maximal function for several rational piecewise-constant perturbations. For a step function, between consecutive radii at which an interval endpoint meets a step discontinuity, the numerator is affine in the radius, so the normalized average is monotone or constant; checking those critical radii is exact for the finite step examples.

The finite checks are supplementary. They do not replace the general proof above.

## Relationship to prior work

Solyanik, arXiv:2609.27687v1, proves noninjectivity of the centered Hardy--Littlewood maximal operator in every dimension. In one dimension, his Theorem 1 treats
\[
h=\epsilon\mathbf 1_I,
\qquad |I|=\epsilon,
\qquad 0<\epsilon\le\frac14,
\]
inside a gap of half-width \(\epsilon\), and obtains an explicit maximal-function formula independent of the position of \(I\). In two dimensions, Remark 2 observes a broader same-total-mass invariance for sufficiently small perturbations supported in a central disk.

The present result identifies, in the one-dimensional two-tower geometry, the full arbitrary-shape fixed-mass regime controlled only by mass and amplitude, gives the exact profile for every \(0<\delta<1/2\) and \(0<m<2\delta\), and determines the exact universal amplitude threshold
\[
\rho_c=1-2\delta+m.
\]
The necessity statement is not a restatement of the source construction: once the cap exceeds \(\rho_c\), a boundary-loaded perturbation breaks shape-invisibility at the tower edge.

As a concrete specialization, taking \(m=\delta^2\) shows that the source's one-dimensional mechanism is covered whenever the perturbation amplitude obeys
\[
\delta\le1-2\delta+\delta^2,
\]
that is,
\[
\delta\le\frac{3-\sqrt5}{2}.
\]
This improves the displayed sufficient range \(\delta\le1/4\) for the universal-shape argument, while the theorem here addresses a larger class than translated indicator bumps.

Ephremidze's earlier uniqueness work concerns one-sided maximal operators. It does not supply a fixed-mass fiber classification for the centered operator.

## Limitations

The threshold is sharp for universal shape-invisibility within the stated two-tower, fixed-mass model. The result does not classify perturbations above threshold that may still happen to share a maximal function, and it does not assert that the same threshold persists in higher dimensions or for different backgrounds.

The primary source was inspected in full for the one-dimensional construction and the planar same-mass remark. Targeted literature searches did not locate the exact threshold \(\rho_c=1-2\delta+m\) or this one-dimensional arbitrary-shape formula, but absence from searched sources is not a proof of global novelty.

## References

1. A. Solyanik, *On the Central Maximal Function in \(\mathbb R^n\)*, arXiv:2609.27687v1, first posted 2026-09-23.
2. L. Ephremidze, *On the Uniqueness Property of Various Maximal Operators*, RIMS Kôkyûroku Bessatsu B22 (2010), 137--144.
