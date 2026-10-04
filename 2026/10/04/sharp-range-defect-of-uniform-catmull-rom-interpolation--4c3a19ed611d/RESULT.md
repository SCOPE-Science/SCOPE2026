# Sharp range defect of uniform Catmull–Rom interpolation
## Finding
Let
\[
0\le y_0\le y_1\le y_2\le y_3\le M,
\qquad M>0,
\]
and let \(P_\sigma(t)\), \(0\le t\le1\), be the cubic Hermite segment from \(y_1\) to \(y_2\) with cardinal slopes
\[
m_1=\sigma(y_2-y_0),
\qquad
m_2=\sigma(y_3-y_1),
\qquad
0\le\sigma\le\frac12.
\]
The standard uniform Catmull–Rom segment is the endpoint \(\sigma=1/2\). Then the exact range over all monotone data is
\[
-\frac{4\sigma}{27}M
\le
P_\sigma(t)
\le
\left(1+\frac{4\sigma}{27}\right)M.
\]
Both constants are sharp.

The lower bound is attained by
\[
(y_0,y_1,y_2,y_3)=(0,0,0,M)
\]
at \(t=2/3\). The upper bound is attained by
\[
(y_0,y_1,y_2,y_3)=(0,M,M,M)
\]
at \(t=1/3\).

Consequently the ordinary uniform Catmull–Rom rule has the exact sharp range defect
\[
-\frac{2}{27}M
\le
P_{1/2}(t)
\le
\frac{29}{27}M.
\]
Thus monotone samples confined to \([0,M]\) can generate an undershoot or overshoot equal to exactly \(2M/27\), about \(7.407\%\) of the full data range.

If the cardinal slope is written in Kochanek–Bartels tension form
\[
\sigma=\frac{1-\tau}{2},
\qquad
0\le\tau\le1,
\]
the exact defect amplitude is
\[
\frac{2(1-\tau)}{27}M.
\]
It therefore decreases linearly with tension and vanishes only at \(\tau=1\).

The failure is not an artifact of repeated or zero-valued samples. For every \(\sigma>0\), choose
\[
(y_0,y_1,y_2,y_3)
=
(\varepsilon M,2\varepsilon M,3\varepsilon M,M).
\]
These data are strictly positive and strictly increasing whenever \(0<\varepsilon<1/3\), and
\[
\frac{P_\sigma(2/3)}{M}
=
\frac{2\bigl((6\sigma+37)\varepsilon-2\sigma\bigr)}{27}.
\]
Hence the interpolant is negative at \(t=2/3\) whenever
\[
0<\varepsilon<
\frac{2\sigma}{6\sigma+37}.
\]
For standard Catmull–Rom, any \(0<\varepsilon<1/40\) gives a strictly increasing positive four-point data set with a negative interpolated value.

## Assumptions and scope
The theorem concerns one scalar uniform cardinal cubic segment and exact real arithmetic. The four samples are ordered and bounded, and the central segment uses the displayed symmetric cardinal slopes.

No claim is made for centripetal or chordal parameterizations, nonuniform knot spacings, vector-valued curve containment, monotonicity-filtered tangents, rational splines, or other shape-preserving modifications. The parameter \(\sigma\) is restricted to \(0\le\sigma\le1/2\), the interval connecting zero cardinal slope to the standard uniform Catmull–Rom slope.

The bounds concern the full global data interval \([0,M]\). They do not assert a bound relative only to the two central values \(y_1,y_2\).

## Proof
Write the cubic Hermite basis as
\[
h_{00}=2t^3-3t^2+1,
\quad
h_{10}=t^3-2t^2+t,
\]
\[
h_{01}=-2t^3+3t^2,
\quad
h_{11}=t^3-t^2.
\]
Then
\[
P_\sigma(t)
=
h_{00}y_1+h_{10}m_1+h_{01}y_2+h_{11}m_2.
\]

Introduce nonnegative increments
\[
a=y_0,\qquad
d_0=y_1-y_0,\qquad
d_1=y_2-y_1,\qquad
d_2=y_3-y_2.
\]
They satisfy
\[
a,d_0,d_1,d_2\ge0,
\qquad
a+d_0+d_1+d_2\le M.
\]
Direct substitution gives
\[
P_\sigma(t)
=
a+q_0(t)d_0+q_1(t)d_1+q_2(t)d_2,
\]
where
\[
q_0(t)=1+\sigma t(1-t)^2,
\]
\[
q_1(t)
=
t\left[
\sigma+(1-\sigma)t(3-2t)
\right],
\]
and
\[
q_2(t)=-\sigma t^2(1-t).
\]

For \(0\le t\le1\),
\[
q_0(t)\ge1,
\qquad
q_2(t)\le0.
\]
Also \(q_1(t)\ge0\). To bound it above, factor
\[
1-q_1(t)
=
(1-t)
\left[
1+(1-\sigma)t(1-2t)
\right].
\]
The bracket is a concave quadratic in \(t\). Its endpoint values are \(1\) and \(\sigma\), so it is nonnegative throughout \([0,1]\). Hence
\[
0\le q_1(t)\le1.
\]

At a fixed \(t\), \(P_\sigma\) is a linear functional on the simplex of admissible increments. Because only \(q_2\) can be negative, the minimum is obtained by assigning the entire available variation \(M\) to \(d_2\):
\[
\min P_\sigma(t)
=
-\sigma M t^2(1-t).
\]
Similarly, \(q_0\) is the largest coefficient: \(q_0\ge1\ge q_1\ge q_2\). Therefore the maximum is obtained by assigning the entire variation \(M\) to \(d_0\):
\[
\max P_\sigma(t)
=
M\left[1+\sigma t(1-t)^2\right].
\]

The two scalar shape factors satisfy
\[
\max_{0\le t\le1} t^2(1-t)=\frac4{27},
\qquad
\max_{0\le t\le1} t(1-t)^2=\frac4{27}.
\]
Indeed,
\[
\frac{d}{dt}\left[t^2(1-t)\right]
=
t(2-3t),
\]
so the interior maximizer is \(t=2/3\), while
\[
\frac{d}{dt}\left[t(1-t)^2\right]
=
(1-t)(1-3t),
\]
so the interior maximizer is \(t=1/3\). This proves the sharp two-sided bound and its extremizers.

For the strictly increasing witness, substitution of
\[
(\varepsilon M,2\varepsilon M,3\varepsilon M,M)
\]
at \(t=2/3\) gives
\[
P_\sigma(2/3)
=
\frac{2M}{27}
\left[
(6\sigma+37)\varepsilon-2\sigma
\right],
\]
which yields the stated threshold.

## Verification
The accompanying `verify.py` uses exact rational polynomial arithmetic. It reconstructs the Hermite segment from the four samples, changes variables to the four nonnegative increments, and verifies the three coefficient polynomials \(q_0,q_1,q_2\) exactly.

It verifies the factorization of \(1-q_1\), the derivative factorizations of both extremal cubic shape factors, their exact values \(4/27\) at \(1/3\) and \(2/3\), the standard Catmull–Rom bounds \(-2/27\) and \(29/27\), and the formula for the strictly increasing positive witness.

The checker verifies algebraic identities. The optimization over every admissible data vector and every \(t\in[0,1]\) is established analytically by the sign and concavity arguments in the proof.

## Relationship to prior work
Barry and Goldman studied a class of Catmull–Rom splines and their recursive evaluation, establishing the method family and its shape-parameter context. That construction is prior work.

Fritsch and Butland give a local monotone piecewise cubic Hermite method for monotone data. Their work establishes that enforcing monotonicity through modified local slopes is a classical interpolation objective. It is not the operator analyzed here.

Most directly, Huang, Han, and Gong state that original Catmull–Rom interpolation can overshoot and thereby violate global stability, while a monotonic modification avoids that failure. The qualitative existence of overshoot is therefore prior work and is not claimed here.

The present result solves the sharp bounded-data extremal problem for the unmodified uniform cardinal segment. It identifies the exact worst undershoot and overshoot over all monotone four-point data, gives the extremizing data and locations, quantifies the entire tension path \(0\le\sigma\le1/2\), and shows that strict positivity and strict increase do not remove the sign failure.

## Limitations
The result is local and scalar. It does not give sharp bounds for a complete nonuniform spline, multidimensional curve geometry, or adaptive tangent-selection rules.

Catmull–Rom and cubic Hermite interpolation have large computer-graphics and approximation-theory literatures. An equivalent \(2/27\) constant may exist under a kernel-norm, overshoot-factor, or cardinal-basis formulation not located in the checked searches. The closest overshoot paper inspected at full accessible abstract level establishes the qualitative instability but does not state the sharp constant there.

Full-text institutional retrieval was attempted for the most directly relevant Catmull–Rom papers after open-access searches did not provide usable full text, but the retrieval service was unavailable in this review. This access limitation is retained as an originality risk rather than used as evidence of noncoverage.

## References
1. Phillip J. Barry and Ronald N. Goldman, *A Recursive Evaluation Algorithm for a Class of Catmull–Rom Splines*, Proceedings of SIGGRAPH 1988, 199--204, DOI: 10.1145/54852.378511.
2. F. N. Fritsch and J. Butland, *A Method for Constructing Local Monotone Piecewise Cubic Interpolants*, SIAM Journal on Scientific and Statistical Computing 5 (1984), 300--304, DOI: 10.1137/0905021.
3. Zhanpeng Huang, Liang Han, and Guanghong Gong, *A Local Adaptive Catmull–Rom to Reduce Numerical Dissipation of Semi-Lagrangian Advection*, Computer Animation and Virtual Worlds 26 (2015), 141--146, DOI: 10.1002/cav.1559; first published online October 11, 2013.
