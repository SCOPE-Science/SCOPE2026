# Sharp monotone range defect of four-point degree-one Floater–Hormann interpolation
## Finding
Consider the degree-one Floater–Hormann rational interpolant through four equally spaced samples. By affine rescaling of the abscissa it is enough to use the nodes
\[
0,1,2,3.
\]
For data
\[
0\le y_0\le y_1\le y_2\le y_3\le M,
\]
let \(R[y](x)\) denote the Floater–Hormann interpolant with blending degree \(d=1\).

There is an exact sharp constant
\[
\delta=0.18441311642853\ldots
\]
such that
\[
-\delta M
\le
R[y](x)
\le
(1+\delta)M
\qquad
(0\le x\le3)
\]
for every bounded nondecreasing data vector. The constant \(\delta\) is the unique positive root of
\[
15\delta^4+30\delta^3+671\delta^2+656\delta-144=0.
\]

The bound is attained. Let \(\tau\) be the unique root in \((0,1)\) of
\[
\tau^4-6\tau^3+29\tau^2-60\tau+24=0.
\]
Then
\[
\tau=0.516232808495147\ldots
\]
and for the monotone step data
\[
(y_0,y_1,y_2,y_3)=(0,0,M,M)
\]
one has
\[
R[y](\tau)=-\delta M,
\qquad
R[y](3-\tau)=(1+\delta)M.
\]
Thus the undershoot and overshoot are symmetric and both sharp.

The sign failure persists for strictly positive, strictly increasing data. At \(x=1/2\), the barycentric basis coefficients are
\[
\left(\frac{15}{38},\frac{15}{19},-\frac5{19},\frac3{38}\right).
\]
Hence
\[
(y_0,y_1,y_2,y_3)
=
\left(\frac{M}{100},\frac{2M}{100},\frac{98M}{100},\frac{99M}{100}\right)
\]
gives
\[
R[y](1/2)=-\frac4{25}M<0.
\]

## Assumptions and scope
The result is for the original Floater–Hormann construction with blending degree \(d=1\) on four consecutive equally spaced nodes. Translation and positive rescaling of the node spacing do not change the dimensionless defect \(\delta\).

The theorem concerns the range of the interpolated values for bounded monotone data. It does not claim that the rational interpolant is monotone between nodes, and it does not classify other blending degrees or longer node sets.

This is the first genuinely rational uniform \(d=1\) four-node configuration considered here. The result is not a statement about the polynomial limit \(d=n\), nor about the Berrut case \(d=0\).

## Proof
For four unit-spaced nodes and \(d=1\), the Floater–Hormann barycentric weights are proportional to
\[
(-1,2,-2,1).
\]
Writing
\[
D(x)=x^2-3x+6
=
\left(x-\frac32\right)^2+\frac{15}{4}>0,
\]
the four cardinal functions are
\[
\ell_0(x)
=
-\frac{(x-1)(x-2)(x-3)}{D(x)},
\]
\[
\ell_1(x)
=
\frac{2x(x-2)(x-3)}{D(x)},
\]
\[
\ell_2(x)
=
-\frac{2x(x-1)(x-3)}{D(x)},
\]
\[
\ell_3(x)
=
\frac{x(x-1)(x-2)}{D(x)}.
\]
They sum to one and
\[
R[y](x)=\sum_{j=0}^3\ell_j(x)y_j.
\]

Introduce monotone increments
\[
d_0=y_0,
\qquad
d_1=y_1-y_0,
\qquad
d_2=y_2-y_1,
\qquad
d_3=y_3-y_2,
\qquad
s=M-y_3.
\]
Then
\[
d_0,d_1,d_2,d_3,s\ge0,
\qquad
d_0+d_1+d_2+d_3+s=M,
\]
and
\[
R[y](x)
=
d_0+c_1(x)d_1+c_2(x)d_2+c_3(x)d_3,
\]
where
\[
c_1(x)=\frac{x(x^2-5x+8)}{D(x)},
\]
\[
c_2(x)=-\frac{x(x-4)(x-1)}{D(x)},
\]
\[
c_3(x)=\frac{x(x-2)(x-1)}{D(x)}.
\]
The slack variable \(s\) has coefficient zero. Therefore, at each fixed \(x\), the exact image of the monotone-data simplex is
\[
M\left[
\min\{0,1,c_1(x),c_2(x),c_3(x)\},
\max\{0,1,c_1(x),c_2(x),c_3(x)\}
\right].
\]

On the left cell \(0\le x\le1\), the coefficients \(c_1\) and \(c_3\) lie in \([0,1]\), while
\[
c_2(x)=-g(x),
\qquad
g(x)=\frac{x(4-x)(1-x)}{D(x)}\ge0.
\]
Thus the left-cell undershoot is exactly \(\max g\). Differentiation gives
\[
g'(x)
=
\frac{q(x)}{D(x)^2},
\]
with
\[
q(x)=x^4-6x^3+29x^2-60x+24.
\]
Furthermore
\[
q'(x)=4x^3-18x^2+58x-60,
\]
\[
q''(x)=12x^2-36x+58.
\]
On \([0,1]\), \(q''(x)\ge34>0\), so \(q'\) is increasing; since \(q'(1)=-16\), one has \(q'<0\) throughout the interval. Hence \(q\) is strictly decreasing from
\[
q(0)=24
\]
to
\[
q(1)=-12,
\]
and has a unique zero \(\tau\in(0,1)\). Therefore
\[
\delta=g(\tau)
\]
is the unique left-cell maximum.

The reflection identity
\[
c_2(3-x)=1-c_2(x)
\]
shows that the right cell \([2,3]\) has sharp upper value \(1+\delta\).

It remains only to check that the middle cell cannot dominate this defect. Put \(x=1+t\), \(0\le t\le1\). There the only coefficients outside \([0,1]\) are \(c_3<0\) and \(c_1>1\), with equal reflected magnitude
\[
f(t)=\frac{t(1-t^2)}{t^2-t+4}.
\]
Since
\[
t(1-t^2)\le\frac{2}{3\sqrt3}
\]
and
\[
t^2-t+4\ge\frac{15}{4},
\]
one has
\[
f(t)\le\frac{8}{45\sqrt3}.
\]
But
\[
\delta\ge g(1/2)=\frac7{38}
>
\frac{8}{45\sqrt3}.
\]
Hence the global defect is the edge-cell value \(\delta\).

Finally, eliminating \(\tau\) from
\[
q(\tau)=0,
\qquad
\delta D(\tau)=\tau(4-\tau)(1-\tau)
\]
gives
\[
15\delta^4+30\delta^3+671\delta^2+656\delta-144=0.
\]
This polynomial has exactly one positive root by Descartes' rule of signs, so it characterizes \(\delta\) uniquely.

## Verification
The accompanying `verify.py` reconstructs the uniform \(d=1\) Floater–Hormann weights directly from the published weight formula, checks the rational cardinal functions at exact rational points, and verifies the monotone-increment coefficient identities.

It brackets the unique critical point \(\tau\) and the algebraic defect \(\delta\) with rational interval arithmetic, verifies
\[
g(1/2)=\frac7{38},
\]
and checks the exact strictly increasing witness
\[
R[y](1/2)=-\frac4{25}M.
\]
It also verifies the exact polynomial relation satisfied by the numerical defect bracket.

The global optimization over all real \(x\in[0,3]\) and all bounded monotone data is proved analytically above; the finite replay is corroborative rather than exhaustive.

## Relationship to prior work
Floater and Hormann introduced the pole-free barycentric rational family, defined it as a blend of local degree-\(d\) polynomial interpolants, proved that the denominator has no real zeros, and derived the barycentric weights. Their full text explicitly gives the \(d=1\) weight formula and, for equally spaced nodes, the general uniform-grid formula. These construction, pole-freeness, polynomial-reproduction, and approximation-order results are prior work.

Bos, De Marchi, Hormann, and Klein later analyzed the Lebesgue function and conditioning of Floater–Hormann interpolation on equidistant nodes. Conditioning and Lebesgue growth are likewise prior work.

The present result asks a different shape question: the exact image of the bounded monotone data cone for the smallest four-node uniform \(d=1\) rational stencil. Targeted searches under monotonicity, shape preservation, range preservation, overshoot, positive data, and barycentric-coordinate terminology did not locate a theorem giving the exact \(18.4413\ldots\%\) defect, the algebraic sharp constant, or the strict monotone sign-reversal witness.

The original Floater–Hormann full text contains no occurrence of the terms `monoton`, `shape`, `overshoot`, or `range` in the inspected searchable text. Its denominator-positivity theorem concerns absence of poles and does not make the cardinal coefficients nonnegative.

## Limitations
Only four equally spaced nodes with blending degree \(d=1\) are classified. Longer stencils and other blending degrees can have different cardinal-coefficient geometry.

Range preservation and monotonicity are different properties. The theorem gives the exact worst violation of the data range; it does not classify where the derivative of the interpolant changes sign.

The shape-preserving rational-interpolation literature is broader than the sources inspected here. A specialized paper could contain an equivalent four-node calculation under different terminology; this is the main residual originality risk.

## References
1. Michael S. Floater and Kai Hormann, *Barycentric Rational Interpolation with No Poles and High Rates of Approximation*, Numerische Mathematik 107 (2007), 315--331, DOI: 10.1007/s00211-007-0093-y. Author-hosted full text inspected.
2. Len Bos, Stefano De Marchi, Kai Hormann, and Georges Klein, *On the Lebesgue Constant of Barycentric Rational Interpolation at Equidistant Nodes*, Numerische Mathematik 121 (2012), 461--471, DOI: 10.1007/s00211-011-0442-8. Public repository record dated December 18, 2011.
