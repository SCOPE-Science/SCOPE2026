# Sharp monotone range defect of uniform four-point cubic Lagrange interpolation
## Finding
Let four equally spaced nodes be
\[
x_{j-1}=x_j-h,\qquad x_j,\qquad x_{j+1}=x_j+h,\qquad x_{j+2}=x_j+2h,
\]
with \(h>0\), and let their data satisfy
\[
0\le y_0\le y_1\le y_2\le y_3\le M,
\qquad M>0.
\]
Let \(P\) be the unique polynomial of degree at most three interpolating these four values, and restrict it to the central cell \([x_j,x_{j+1}]\). Then the exact range over all admissible data and all points of that cell is
\[
-\frac{\sqrt3}{27}M
\le
P(x)
\le
\left(1+\frac{\sqrt3}{27}\right)M.
\]
Both constants are sharp.

After the normalized change of variable
\[
t=\frac{x-x_j}{h}\in[0,1],
\]
the lower equality is attained by
\[
(y_0,y_1,y_2,y_3)=(0,0,0,M)
\]
at
\[
t=\frac1{\sqrt3},
\]
and the upper equality is attained by
\[
(y_0,y_1,y_2,y_3)=(0,M,M,M)
\]
at
\[
t=1-\frac1{\sqrt3}.
\]
Thus the exact worst undershoot or overshoot is
\[
\frac{\sqrt3}{27}M
\approx 0.06415003M,
\]
about \(6.415\%\) of the full data range.

The defect is not caused only by repeated or zero samples. For
\[
(y_0,y_1,y_2,y_3)
=
(\varepsilon M,2\varepsilon M,3\varepsilon M,M),
\]
which is strictly positive and strictly increasing whenever \(0<\varepsilon<1/3\), one has
\[
\frac{P(x_j+h/\sqrt3)}{M}
=
2\varepsilon+\frac{13\sqrt3}{27}\varepsilon-\frac{\sqrt3}{27}.
\]
Hence this interpolated value is negative whenever
\[
0<\varepsilon<\frac{\sqrt3}{54+13\sqrt3}
=
\frac{18\sqrt3-13}{803}.
\]
In particular, \(\varepsilon=1/100\) gives
\[
\frac{P(x_j+h/\sqrt3)}{M}
=
\frac{18-29\sqrt3}{900}<0.
\]

## Assumptions and scope
The theorem concerns the ordinary degree-three Lagrange polynomial through four consecutive equally spaced scalar samples, evaluated only on the central cell between the two middle nodes. The affine normalization by \(h\) shows that the constant is independent of mesh spacing.

The data are assumed nondecreasing and globally bounded in \([0,M]\). No smooth underlying function is assumed. The theorem bounds the interpolated values; it does not assert that the cubic itself is monotone on the central cell.

No claim is made for nonuniform nodes, higher-degree Lagrange interpolation, endpoint cells using a one-sided four-point stencil, cubic splines, or cubic Hermite rules with independently chosen derivatives.

## Proof
Normalize the nodes to
\[
-1,\quad 0,\quad 1,\quad 2
\]
and write \(t\in[0,1]\) for the central-cell coordinate. The four Lagrange basis polynomials are
\[
L_0(t)=-\frac{t(t-1)(t-2)}6,
\]
\[
L_1(t)=\frac{(t+1)(t-1)(t-2)}2,
\]
\[
L_2(t)=-\frac{t(t+1)(t-2)}2,
\]
and
\[
L_3(t)=\frac{t(t-1)(t+1)}6.
\]
Thus
\[
P(t)=L_0(t)y_0+L_1(t)y_1+L_2(t)y_2+L_3(t)y_3.
\]

Introduce nonnegative increments
\[
a=y_0,\qquad d_0=y_1-y_0,\qquad d_1=y_2-y_1,\qquad d_2=y_3-y_2.
\]
They satisfy
\[
a,d_0,d_1,d_2\ge0,
\qquad
a+d_0+d_1+d_2\le M.
\]
Using \(L_0+L_1+L_2+L_3=1\), rewrite the interpolant as
\[
P(t)=a+q_0(t)d_0+q_1(t)d_1+q_2(t)d_2,
\]
where
\[
q_0(t)=1-L_0(t)
=1+\frac{t(t-1)(t-2)}6,
\]
\[
q_1(t)=L_2(t)+L_3(t)
=\frac{t(t+1)(5-2t)}6,
\]
and
\[
q_2(t)=L_3(t)
=\frac{t(t-1)(t+1)}6.
\]
On \([0,1]\),
\[
q_0(t)\ge1,
\qquad
q_2(t)\le0.
\]
Moreover
\[
1-q_1(t)
=
\frac{(t-2)(t-1)(2t+3)}6\ge0,
\]
while the displayed factorization of \(q_1\) shows \(q_1(t)\ge0\). Hence
\[
q_0(t)\ge1\ge q_1(t)\ge0\ge q_2(t).
\]

For fixed \(t\), \(P(t)\) is a linear functional on the simplex of admissible increments. Its minimum is therefore obtained by placing the entire available variation \(M\) on \(d_2\), and its maximum by placing it on \(d_0\):
\[
\min P(t)=M q_2(t),
\qquad
\max P(t)=M q_0(t).
\]
The corresponding data are exactly \((0,0,0,M)\) and \((0,M,M,M)\).

The lower defect factor is
\[
-q_2(t)
=
\frac{t(1-t)(1+t)}6
=
\frac{t-t^3}{6}.
\]
Its derivative is
\[
\frac{1-3t^2}{6},
\]
so its unique interior maximum occurs at \(t=1/\sqrt3\). At that point
\[
-q_2(t)=\frac{\sqrt3}{27}.
\]
The upper defect is the reflected same function:
\[
q_0(t)-1
=
\frac{t(1-t)(2-t)}6
=
-q_2(1-t).
\]
It therefore has the same maximum \(\sqrt3/27\), attained at \(t=1-1/\sqrt3\). This proves the sharp two-sided range.

For the strictly increasing witness, substitute
\[
a=d_0=d_1=\varepsilon M,
\qquad
d_2=(1-3\varepsilon)M
\]
into the increment formula and set \(t=1/\sqrt3\). Exact simplification gives the displayed expression
\[
2\varepsilon+\frac{13\sqrt3}{27}\varepsilon-\frac{\sqrt3}{27},
\]
whose sign yields the stated threshold.

## Verification
The accompanying `verify.py` uses exact rational polynomial arithmetic. It reconstructs the four Lagrange basis polynomials, checks partition of unity, derives \(q_0,q_1,q_2\), and verifies the factorization of \(1-q_1\).

It checks that the two defect cubics are reflections of one another, verifies the exact derivative equation for their interior extremum, and evaluates the extremal value in the quadratic field \(\mathbb Q(\sqrt3)\) as \(\sqrt3/27\).

The checker also verifies the closed formula for the strictly increasing witness at \(t=1/\sqrt3\) and the exact negativity of the choice \(\varepsilon=1/100\). The optimization over all admissible monotone data is analytic: it follows from the coefficient ordering and linear optimization over the increment simplex, not from finite enumeration.

## Relationship to prior work
Fritsch and Carlson derived necessary and sufficient conditions for a cubic Hermite segment to be monotone and used them to build a shape-preserving piecewise cubic interpolant. Their work establishes that ordinary cubic interpolation rules can violate monotonicity and that avoiding extraneous bumps is a substantive interpolation objective.

Berzins studied polynomial interpolation on evenly spaced meshes from the viewpoint of oscillation, positivity, and data-boundedness. He explicitly formulates Lagrange interpolation on equal grids and develops adaptive divided-difference limiting so that each local polynomial remains between its endpoint data and is monotone. Those bounded adaptive polynomials differ from the unmodified four-point Lagrange cubic analyzed here.

Revers surveyed Lagrange interpolation on equally spaced nodes, principally emphasizing convergence, divergence, and limiting behavior as polynomial degree grows. The present result instead solves the finite local extremal problem for the unmodified four-node cubic on its central cell.

## Limitations
The result is a local four-node theorem. It does not bound a global high-degree equispaced interpolant or a piecewise scheme that changes stencils from cell to cell.

Monotone data alone do not force the interpolating cubic to be monotone; the theorem quantifies only its sharp global range defect on the central cell.

The equal-grid assumption is essential to the stated constant. Nonuniform node ratios change the Lagrange coefficients and their negative extrema.

A small-degree coefficient identity equivalent to the constant may exist in older interpolation tables or textbook treatments without being framed as a monotone-data range theorem.

## References
1. F. N. Fritsch and R. E. Carlson, *Monotone Piecewise Cubic Interpolation*, SIAM Journal on Numerical Analysis 17 (1980), 238--246, DOI: 10.1137/0717021.
2. M. Berzins, *Adaptive Polynomial Interpolation on Evenly Spaced Meshes*, SIAM Review 49 (2007), 604--627, DOI: 10.1137/050625667.
3. Michael Revers, *A Survey on Lagrange Interpolation Based on Equally Spaced Nodes*, in Advanced Problems in Constructive Approximation, International Series of Numerical Mathematics 142 (2002), 153--163, DOI: 10.1007/978-3-0348-7600-1_12.
