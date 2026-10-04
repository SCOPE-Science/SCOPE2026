# The uniform Akima interpolant has sharp monotone range defect \(2/27\)
## Finding
Consider the original Akima cubic interpolation rule on a uniform grid
\[
x_j=jh,
\qquad h>0,
\]
applied to a bi-infinite nondecreasing scalar data sequence
\[
0\le y_j\le M.
\]
Write the secant slopes as
\[
\delta_j=\frac{y_{j+1}-y_j}{h}\ge0.
\]
At an interior knot, the Akima derivative is
\[
m_i=
\frac{w_-\delta_{i-1}+w_+\delta_i}{w_-+w_+},
\qquad
w_-=|\delta_{i+1}-\delta_i|,
\qquad
w_+=|\delta_{i-1}-\delta_{i-2}|,
\]
when the denominator is nonzero; in the zero-weight case use the standard limiting convention
\[
m_i=\frac{\delta_{i-1}+\delta_i}{2}.
\]
Let \(A_h y\) denote the resulting piecewise cubic Hermite interpolant.

Then the exact global range envelope over all such monotone bounded data is
\[
-\frac{2M}{27}
\le
(A_h y)(x)
\le
\frac{29M}{27}
\]
for every admissible data sequence and every interior evaluation point. The constants are sharp as the infimum and supremum over the class. Equivalently,
\[
\inf_{y,x}\frac{(A_hy)(x)}{M}=-\frac{2}{27},
\qquad
\sup_{y,x}\frac{(A_hy)(x)}{M}=\frac{29}{27}.
\]
Thus the worst possible undershoot or overshoot is exactly
\[
\frac{2M}{27}\approx0.074074M.
\]
The constant is independent of the grid spacing.

A local derivative lemma drives the result. For any four nonnegative secants \(a,b,c,d\), the Akima weighted slope between \(b\) and \(c\) satisfies
\[
0\le m(a,b,c,d)\le\frac{a+b+c+d}{2}.
\]
Consequently every Akima knot derivative for data in \([0,M]\) obeys
\[
0\le h m_i\le\frac{M}{2}.
\]

The sharp lower constant is approached by the monotone six-point family, with \(M=h=1\),
\[
y_0=0,
\quad y_1=\varepsilon,
\quad y_2=2\varepsilon,
\quad y_3=4\varepsilon,
\quad y_4=\frac12+2\varepsilon,
\quad y_5=1,
\]
continued constantly outside these six knots, where
\[
0<\varepsilon<\frac18.
\]
On the segment from \(y_2\) to \(y_3\), the endpoint Akima derivatives are
\[
m_2=\varepsilon,
\qquad
m_3=\frac12-2\varepsilon,
\]
and at the local coordinate \(t=2/3\),
\[
(A_1y)(2+t)
=
\frac{104\varepsilon-2}{27}
\longrightarrow
-\frac{2}{27}
\qquad(\varepsilon\downarrow0).
\]
Horizontal reversal followed by the vertical complement \(y\mapsto M-y\) yields the matching upper sharpness.

The sign failure persists with strictly positive data. Taking \(\varepsilon=1/104\) in the preceding family and applying the vertical affine transformation
\[
z_j=\frac1{100}+\frac{99}{100}y_j
\]
gives the strictly positive increasing active values
\[
\frac1{100},
\quad
\frac{203}{10400},
\quad
\frac{151}{5200},
\quad
\frac5{104},
\quad
\frac{109}{208},
\quad
1.
\]
The Akima interpolant on the same interior segment satisfies exactly
\[
(A_1z)(2+2/3)=-\frac{2}{75}<0.
\]

## Assumptions and scope
The statement uses the original one-dimensional Akima derivative rule on an equally spaced grid and concerns interior cubic segments. Describing a bi-infinite bounded monotone sequence removes endpoint conventions; the sharp witnesses can equivalently be embedded into an arbitrarily long finite data set away from its boundaries.

The result is scalar and concerns the full global data range \([0,M]\), not monotonicity on each individual interval. It does not apply to modified Akima variants, monotonicity-limited Akima methods, nonuniform grids, bivariate extensions, or endpoint extrapolation rules.

The universal inequalities are written non-strictly. Sharpness only requires the witness family to approach the endpoints; no endpoint-attainment claim is needed.

## Proof
First prove the derivative lemma. Let
\[
w=|d-c|,
\qquad
v=|b-a|.
\]
If \(w+v>0\), then
\[
m=\frac{wb+vc}{w+v}.
\]
The elementary inequalities
\[
2b\le a+b+v,
\qquad
2c\le c+d+w
\]
give
\[
2(wb+vc)
\le
w(a+b)+v(c+d)+2wv.
\]
Since
\[
c+d\ge w,
\qquad
a+b\ge v,
\]
we have
\[
w(c+d)+v(a+b)-2wv
\ge
w^2+v^2-2wv
=(w-v)^2\ge0.
\]
Therefore
\[
2(wb+vc)\le(a+b+c+d)(w+v),
\]
and hence
\[
m\le\frac{a+b+c+d}{2}.
\]
If \(w+v=0\), then \(a=b\) and \(c=d\); the standard Akima convention gives
\[
m=\frac{b+c}{2}=\frac{a+b+c+d}{4},
\]
so the same bound holds. Nonnegativity is immediate in both cases.

Apply this lemma at knot \(x_i\). The four secants used there telescope over four consecutive grid cells:
\[
h(\delta_{i-2}+\delta_{i-1}+\delta_i+\delta_{i+1})
=
y_{i+2}-y_{i-2}
\le M.
\]
Thus
\[
0\le h m_i\le\frac M2.
\]

On the cell \([x_i,x_{i+1}]\), put \(t=(x-x_i)/h\). The Hermite representation is
\[
(A_hy)(x)
=
H_{00}(t)y_i+H_{01}(t)y_{i+1}
+hH_{10}(t)m_i+hH_{11}(t)m_{i+1},
\]
where
\[
H_{00}=(1+2t)(1-t)^2,
\qquad
H_{01}=t^2(3-2t),
\]
\[
H_{10}=t(1-t)^2,
\qquad
H_{11}=-t^2(1-t).
\]
For \(0\le t\le1\), the first two basis functions are nonnegative and sum to one, \(H_{10}\ge0\), and \(H_{11}\le0\). Hence
\[
(A_hy)(x)
\ge
-\frac M2 t^2(1-t)
\ge
-\frac{2M}{27},
\]
because
\[
\max_{0\le t\le1}t^2(1-t)=\frac4{27}
\]
at \(t=2/3\). Similarly,
\[
(A_hy)(x)
\le
M+\frac M2 t(1-t)^2
\le
M+\frac{2M}{27},
\]
since
\[
\max_{0\le t\le1}t(1-t)^2=\frac4{27}
\]
at \(t=1/3\).

For the sharpness family, the five active secants are
\[
\varepsilon,
\quad
\varepsilon,
\quad
2\varepsilon,
\quad
\frac12-2\varepsilon,
\quad
\frac12-2\varepsilon.
\]
When \(0<\varepsilon<1/8\), the Akima weights give
\[
m_2=\varepsilon,
\qquad
m_3=\frac12-2\varepsilon.
\]
Substitution into the Hermite formula at \(t=2/3\) yields
\[
\frac{104\varepsilon-2}{27}.
\]
This approaches the lower bound. Reversal-complement symmetry gives the upper bound. The strict-positive witness follows because the Akima construction is equivariant under vertical affine maps with positive scale.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It checks the Akima derivative lemma over an exhaustive integer test box, while the universal proof remains the analytic inequality above.

It reconstructs the sharpness family for several rational \(\varepsilon\), verifies the exact formula
\[
(A_1y)(2+2/3)=\frac{104\varepsilon-2}{27},
\]
and verifies the transformed strictly positive witness and its exact value \(-2/75\).

It also checks the Hermite basis signs at a dense rational grid and the exact extremal values
\[
t^2(1-t)=\frac4{27}\quad\text{at }t=2/3,
\qquad
 t(1-t)^2=\frac4{27}\quad\text{at }t=1/3.
\]
Finite enumeration is corroborative only; the range theorem is proved for all admissible data by the derivative lemma and Hermite-basis inequalities.

## Relationship to prior work
Akima introduced the local cubic interpolation method in 1970, with knot derivatives determined from four neighboring secants. That construction is prior work. Later expositions record that monotone input data need not remain monotone under the original Akima interpolant.

Fried and Zietz explicitly compared cubic-spline and Akima fitting and reported that Akima interpolation can significantly overshoot when the data change abruptly. Thus the qualitative existence of overshoot is prior work and is not part of the novelty claim.

Fritsch and Butland developed a completely local cubic Hermite method that preserves monotonicity of monotone data. Their full text makes the shape-preservation target explicit, and its primary classification is \(65D05\). Their method modifies the derivative selection rather than quantifying the worst violation of the original Akima rule.

The present result solves a different sharp extremal problem for the original uniform-grid Akima rule: it gives the exact global range defect \(2/27\), proves the derivative half-variation lemma that controls every data set, constructs a sharp family, and shows that strictly positive monotone data can still produce a negative interpolated value.

## Limitations
The proof uses equal grid spacing. On a nonuniform grid, the four secants are weighted by different horizontal scales and the same telescoping half-variation bound does not directly apply.

The original Akima paper itself was not recovered as a verified full-text copy during the literature check. Its bibliographic record and abstract were inspected, and the defining derivative formula was cross-checked against a detailed technical exposition. This access limitation is retained as an originality risk rather than used as evidence of noncoverage.

Akima interpolation has a large engineering and graphics literature. A specialized source may contain the same \(2/27\) range constant under an overshoot-factor or Hermite-slope formulation not found by the searches performed here.

## References
1. Hiroshi Akima, *A New Method of Interpolation and Smooth Curve Fitting Based on Local Procedures*, Journal of the ACM 17 (1970), 589--602, DOI: 10.1145/321607.321609.
2. Jerrold Fried and S. Zietz, *Curve fitting by spline and Akima methods: possibility of interpolation error and its suppression*, Physics in Medicine and Biology 18 (1973), 550--558, DOI: 10.1088/0031-9155/18/4/306.
3. F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM Journal on Scientific and Statistical Computing 5 (1984), 300--304, DOI: 10.1137/0905021.
