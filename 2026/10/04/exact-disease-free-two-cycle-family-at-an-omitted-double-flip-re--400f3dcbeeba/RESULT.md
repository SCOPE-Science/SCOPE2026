# Exact disease-free two-cycle family at an omitted double-flip resonance in a discrete SIR map

## Finding

Consider the Euler-discretized SIR map
\[
F(x,y)=
\left(
x+h(A-dx-\lambda xy),
\ y+h(\lambda xy-(d+r)y)
\right),
\]
with
\[
A>0,\qquad d>0,\qquad r>0,\qquad h>0,\qquad \lambda>0.
\]
Its disease-free fixed point is
\[
E_0=\left(\frac{A}{d},0\right).
\]

The source states that this disease-free fixed point does not produce a codimension-two bifurcation. That blanket exclusion misses an exact double-\(-1\) resonance in the same two-parameter plane used by the paper.

At
\[
h=\frac{2}{d},
\qquad
\lambda=\frac{dr}{A},
\]
both disease-free multipliers equal \(-1\). The corresponding Jacobian is
\[
J(E_0)=
\begin{pmatrix}
-1&-\frac{2r}{d}\\
0&-1
\end{pmatrix},
\]
so it is a nontrivial Jordan block.

The nonlinear disease-free dynamics are exactly solvable. Since \(y=0\) is invariant, at
\[
h=\frac{2}{d}
\]
the susceptible coordinate satisfies
\[
x_{n+1}
=
\frac{2A}{d}-x_n.
\]
Therefore every point with
\[
0<x<\frac{2A}{d},
\qquad
x\ne\frac{A}{d},
\]
lies on an exact positive disease-free two-cycle. Parameterizing the family by
\[
x_{\pm}=\frac{A}{d}\pm u,
\qquad
0<|u|<\frac{A}{d},
\]
gives
\[
(x_+,0)\longleftrightarrow(x_-,0).
\]

At the double-resonance value
\[
\lambda=\frac{dr}{A},
\]
the two-step transverse multiplier of this cycle is
\[
q(u)
=
1-\left(\frac{2ru}{A}\right)^2.
\]
The other Floquet multiplier is exactly \(1\), reflecting the continuum of neighboring two-cycles. Consequently every member with
\[
0<|u|<
\min\!\left\{
\frac{A}{d},
\frac{A}{\sqrt2\,r}
\right\}
\]
is transversely attracting but cannot be asymptotically stable as an isolated cycle.

A concrete admissible witness is
\[
A=1,\qquad
d=\frac15,\qquad
r=\frac3{10},\qquad
\lambda=\frac3{50},\qquad
h=10.
\]
Then
\[
\mathcal R_0
=
\frac{A\lambda}{d(d+r)}
=
\frac35<1,
\]
\[
E_0=(5,0),
\qquad
J(E_0)=
\begin{pmatrix}
-1&-3\\
0&-1
\end{pmatrix},
\]
and
\[
(6,0)\longleftrightarrow(4,0)
\]
is an exact disease-free period-two orbit with transverse two-step multiplier
\[
q(1)=\frac{16}{25}.
\]

Thus the omitted disease-free point is a transverse codimension-two linear \(1{:}2\) resonance, but its nonlinear unfolding is degenerate in a mathematically informative way: the boundary map becomes an exact involution and carries a full continuum of period-two states.

## Assumptions and scope

The result concerns the reduced two-dimensional map printed as equation (1.4) in the source. All parameters are positive.

For the general double-resonance formula, the value
\[
\lambda=\frac{dr}{A}
\]
must lie in whatever admissible incidence-rate range is imposed in a particular application. The explicit witness satisfies the source's frequently used restrictions
\[
0<d<1,\qquad 0<r<1,\qquad 0<\lambda<1.
\]

The finding is about the disease-free fixed point and its disease-free boundary dynamics. It does not alter the source's separate calculations for the endemic equilibrium \(E_1\), including its \(1{:}2\), \(1{:}3\), and \(1{:}4\) resonance formulas.

The phrase “codimension-two” is used in the source's own intersection sense: two independent multiplier-\(-1\) conditions meet transversely in the \((h,\lambda)\) parameter plane. Because a continuum of exact two-cycles is present, the point is not asserted to satisfy every generic nondegeneracy coefficient used for an isolated strong-resonance normal form.

## Proof

At the disease-free fixed point,
\[
E_0=\left(\frac{A}{d},0\right),
\]
the Jacobian is upper triangular:
\[
J(E_0)
=
\begin{pmatrix}
1-hd&-\frac{hA\lambda}{d}\\
0&1+h\left(\frac{A\lambda}{d}-d-r\right)
\end{pmatrix}.
\]
Hence the two multipliers are
\[
\mu_1=1-hd
\]
and
\[
\mu_2
=
1+h\left(\frac{A\lambda}{d}-d-r\right).
\]

The condition
\[
\mu_1=-1
\]
is
\[
h=\frac{2}{d}.
\]
The condition
\[
\mu_2=-1
\]
is
\[
h=
\frac{2d}{d(d+r)-A\lambda},
\]
when the denominator is positive.

The two conditions coincide exactly when
\[
\frac{2}{d}
=
\frac{2d}{d(d+r)-A\lambda},
\]
which reduces to
\[
A\lambda=dr.
\]
Thus the intersection is
\[
h=\frac{2}{d},
\qquad
\lambda=\frac{dr}{A}.
\]
At this point
\[
J(E_0)
=
\begin{pmatrix}
-1&-\frac{2r}{d}\\
0&-1
\end{pmatrix}.
\]
Because
\[
r>0,
\]
the off-diagonal entry is nonzero, so the double multiplier is a single Jordan block rather than the scalar matrix \(-I\).

The source uses \(h\) and \(\lambda\) as its two perturbation parameters. Define
\[
\phi_1(h,\lambda)=\mu_1+1
\]
and
\[
\phi_2(h,\lambda)=\mu_2+1.
\]
At the intersection,
\[
\nabla\phi_1=(-d,0)
\]
and
\[
\nabla\phi_2=
\left(
-d,\frac{2A}{d^2}
\right).
\]
Therefore
\[
\det
\begin{pmatrix}
-d&0\\
-d&\frac{2A}{d^2}
\end{pmatrix}
=
-\frac{2A}{d}\ne0.
\]
The two multiplier-\(-1\) loci intersect transversely, so the linear resonance has codimension two in that parameter plane.

The epidemiological threshold at the intersection is
\[
\mathcal R_0
=
\frac{A\lambda}{d(d+r)}
=
\frac{r}{d+r}<1.
\]
Thus the resonance occurs in the source's disease-free existence regime.

For the nonlinear statement, set
\[
y=0.
\]
The second component then remains zero. At
\[
h=\frac{2}{d},
\]
the first component becomes
\[
x_{n+1}
=
x_n+\frac{2}{d}(A-dx_n)
=
\frac{2A}{d}-x_n.
\]
Applying the map twice gives
\[
x_{n+2}=x_n.
\]
Every positive pair
\[
x_{\pm}
=
\frac{A}{d}\pm u,
\qquad
0<|u|<\frac{A}{d},
\]
is therefore an exact disease-free two-cycle.

It remains to compute the transverse multiplier. Along \(y=0\), the derivative in the \(y\)-direction is
\[
m(x)
=
1+h(\lambda x-d-r).
\]
At the double-resonance parameters,
\[
h=\frac{2}{d},
\qquad
\lambda=\frac{dr}{A},
\]
one obtains
\[
m(x_+)
=
-1+\frac{2ru}{A},
\]
and
\[
m(x_-)
=
-1-\frac{2ru}{A}.
\]
The transverse two-step multiplier is therefore
\[
q(u)
=
m(x_+)m(x_-)
=
1-\left(\frac{2ru}{A}\right)^2.
\]

The derivative of the two-step disease-free map is exactly \(1\), so the other Floquet multiplier is \(1\). The transverse condition
\[
|q(u)|<1
\]
is equivalent, for \(u\ne0\), to
\[
|u|<\frac{A}{\sqrt2\,r}.
\]
Combining it with positivity of both susceptible values gives the stated range.

For the explicit witness,
\[
A=1,\quad d=\frac15,\quad r=\frac3{10},
\]
the resonance formulas give
\[
\lambda=\frac3{50},
\qquad
h=10,
\qquad
E_0=(5,0).
\]
The boundary involution is
\[
x\longmapsto10-x,
\]
so \(6\) and \(4\) form a two-cycle. Its one-step transverse factors are
\[
-\frac25
\]
and
\[
-\frac85,
\]
whose product is
\[
\frac{16}{25}.
\]

## Verification

The bundled `verify.py` uses exact rational arithmetic. It checks the explicit parameter witness, the threshold value, the double-\(-1\) Jacobian, the nonzero parameter-transversality determinant, the exact two-cycle
\[
(6,0)\longleftrightarrow(4,0),
\]
and its transverse multiplier
\[
\frac{16}{25}.
\]

It also checks symbolically, using direct algebra encoded with rational substitutions, that the two multiplier-\(-1\) curves meet at the claimed parameter values.

The infinite family of disease-free two-cycles is not inferred from finite computation. It follows identically from the affine boundary map.

## Relationship to prior work

Liu, Liu, and Liu (2021), DOI 10.3934/math.2022187, study exactly this Euler-discretized SIR map. They define codimension-two bifurcations as intersections of codimension-one conditions in a two-parameter plane, choose \(h\) and \(\lambda\) as perturbation parameters, and then state that the disease-free fixed point produces no codimension-two bifurcation before concentrating on strong resonances at the endemic fixed point. The exact calculation above gives a disease-free counterexample to that blanket statement.

Hu, Teng, and Zhang (2013), DOI 10.1016/j.matcom.2013.08.008, study the same discrete SIR map. Their local-stability theorem for the disease-free equilibrium already identifies the two separate nonhyperbolicity curves
\[
h=\frac{2}{d}
\]
and
\[
h=
\frac{2d}{d(d+r)-A\lambda}.
\]
Therefore the location of their intersection is algebraically implicit in that earlier work and is not claimed here as an independently new parameter formula. Their inspected analysis does not identify the intersection as a disease-free codimension-two resonance, derive the exact boundary involution, or give the two-cycle transverse multiplier.

Suo and Ge (2025), DOI 10.1080/10236198.2025.2525863, analyze a broader discrete SIR model with an unfixed incidence function. Their full text gives complete disease-free topological types; in the bilinear special case, their table again contains the double-\(-1\) disease-free parameter combination. Their codimension-two normal-form analysis is nevertheless explicitly carried out at the endemic fixed point. The inspected text does not derive the exact disease-free two-cycle continuum or its transverse Floquet multiplier.

The contribution here is therefore deliberately narrow: it is a source-specific correction plus an exact nonlinear boundary classification at the omitted point, not a claim that the multiplier intersection itself was absent from all earlier stability theory.

## Limitations

The resonance is degenerate because the disease-free boundary becomes an exact involution. The result does not claim the generic isolated \(1{:}2\) normal form used for the endemic equilibrium.

The continuum of period-two states is a feature of the Euler-discretized map at the critical step
\[
h=\frac{2}{d}.
\]
It is not a periodic-orbit prediction for the underlying continuous-time SIR differential equation.

The result concerns the reduced \((x,y)\) dynamics used by the source. It does not classify the recovered component of the unreduced three-compartment discretization for arbitrary initial recovered population.

## References

1. X. Liu, P. Liu, Y. Liu, “The existence of codimension-two bifurcations in a discrete-time SIR epidemic model,” AIMS Mathematics 7 (2022), 3360–3378. DOI: 10.3934/math.2022187. First published 30 November 2021.
2. Z.-Y. Hu, Z. Teng, L. Zhang, “Stability and bifurcation analysis in a discrete SIR epidemic model,” Mathematics and Computers in Simulation 97 (2014), 80–93. DOI: 10.1016/j.matcom.2013.08.008.
3. J. Suo, Y. Ge, “Resonance and bifurcations of the discrete SIR model with unfixed incidence rate,” Journal of Difference Equations and Applications 31 (2025), 1287–1313. DOI: 10.1080/10236198.2025.2525863.
