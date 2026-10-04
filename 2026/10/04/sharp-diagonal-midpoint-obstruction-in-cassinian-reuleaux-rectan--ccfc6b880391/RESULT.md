# Sharp diagonal-midpoint obstruction in Cassinian Reuleaux rectangles
## Finding
Let \(0<a<1\), put \(s=\sqrt{1+a^2}\), and let the four rectangle vertices be
\[
A=(-1,-a),\quad B=(1,-a),\quad C=(1,a),\quad D=(-1,a).
\]
Write \(K(U,V;q)=\{X:|X-U|\,|X-V|\le q\}\). The filled Cassinian Reuleaux rectangle determined by these four vertices is
\[
E_a=K(A,B;4as)\cap K(C,D;4as)\cap K(A,D;4s)\cap K(B,C;4s).
\]
Every three-corner triple has distance product
\[
\Delta_a^3=(2)(2a)(2s)=8as.
\]
Define
\[
c=2^{1/3}-1,\qquad
\alpha=\frac{c}{\sqrt{1-c^2}}=0.269172544981613\ldots .
\]
For every
\[
\frac1{\sqrt{15}}\le a<\alpha,
\]
there is an explicit boundary point \(P_a\in E_a\) such that the triple consisting of \(P_a\) and two opposite corners has distance product strictly larger than \(\Delta_a^3\). Consequently
\[
d_3(E_a)>\Delta_a
\]
throughout this entire aspect-ratio interval. For this specific diagonal-midpoint witness the threshold is sharp: equality occurs at \(a=\alpha\), and the witness falls below the corner value for \(a>\alpha\).

Thus the corner value that controls the Reuleaux square does not control the whole Reuleaux-rectangle family. This is an obstruction to extending the square proof by keeping the four corner triples as the global \(3\)-diameter candidates. It does not by itself decide whether the affected sets might nevertheless have constant \(3\)-diameter at a larger value.

## Assumptions and scope
The construction uses the filled regions bounded by the four Cassinian ovals that appear in the Reuleaux-square construction and in Question 6.2 of Hästö--Ibragimov--Minda. For a bounded planar set \(E\),
\[
d_3(E)=\sup_{X,Y,Z\in E}\bigl(|X-Y|\,|Y-Z|\,|Z-X|\bigr)^{1/3}.
\]
Only the interval \(1/\sqrt{15}\le a<\alpha\) is asserted to have the strict diagonal-midpoint obstruction. No assertion is made here about the exact value of \(d_3(E_a)\), about constant \(3\)-diameter itself, or about parameters outside this interval.

The source paper has primary MSC \(51M04\). The publicly accessible accepted manuscript carries the date June 15, 2010; this is the dated public-manuscript evidence used for the source date here, rather than the later journal issue date.

## Proof
Set
\[
r=\frac{a}{s}\in(0,1),\qquad q=4as,
\]
and, whenever \(4as\ge1\), define
\[
u=\sqrt{4as-1},\qquad P_a=(0,u-a).
\]
The point \(P_a\) lies on the Cassinian boundary determined by the lower two corners, because
\[
|P_a-A|^2=|P_a-B|^2=1+(u)^2=4as=q,
\]
so \(|P_a-A|\,|P_a-B|=q\).

The condition \(P_a\) to be on the upper half of this boundary, and hence inside the opposite horizontal Cassinian constraint, is \(u-a\ge0\). This is equivalent to
\[
4as-1\ge a^2
\iff 4a\ge s
\iff a\ge\frac1{\sqrt{15}}.
\]
For such \(a\),
\[
|P_a-C|^2=|P_a-D|^2=1+(u-2a)^2=q-4a(u-a)\le q,
\]
so the opposite horizontal constraint is satisfied. The two vertical-pair products are
\[
|P_a-A|\,|P_a-D|=|P_a-B|\,|P_a-C|
=\sqrt{q\bigl(q-4a(u-a)\bigr)}\le q<4s,
\]
because \(a<1\). Hence \(P_a\in E_a\).

Now use the opposite corners \(A\) and \(C\). Since
\[
|A-C|=2s,\qquad |P_a-A|^2=q,\qquad |P_a-C|^2=q-4a(u-a),
\]
the squared ratio of the product of the three distances in \((A,C,P_a)\) to the corner product \(\Delta_a^3=2q\) is
\[
\left(\frac{|A-C|\,|A-P_a|\,|C-P_a|}{\Delta_a^3}\right)^2
=\frac{s^2\bigl(q-4a(u-a)\bigr)}{q}.
\]
Writing everything in terms of \(r=a/s\), one has
\[
a=\frac{r}{\sqrt{1-r^2}},\quad s=\frac1{\sqrt{1-r^2}},\quad
u=\frac{\sqrt{r^2+4r-1}}{\sqrt{1-r^2}},
\]
and direct simplification gives
\[
\left(\frac{|A-C|\,|A-P_a|\,|C-P_a|}{\Delta_a^3}\right)^2
=\frac{1+r-\sqrt{r^2+4r-1}}{1-r^2}.
\]
For \(r\ge1/4\), both sides in the next squaring step are nonnegative, so this quantity is greater than \(1\) exactly when
\[
r+r^2>\sqrt{r^2+4r-1}.
\]
Squaring and factoring yields
\[
(r+r^2)^2-(r^2+4r-1)
=(r-1)\bigl((r+1)^3-2\bigr).
\]
Because \(r<1\), the product is positive exactly when
\[
r<2^{1/3}-1=c.
\]
The map \(a\mapsto a/\sqrt{1+a^2}\) is strictly increasing. Its value at \(a=1/\sqrt{15}\) is \(1/4\), and solving \(a/\sqrt{1+a^2}=c\) gives \(a=\alpha\). Therefore the strict obstruction holds precisely for this witness on
\[
\frac1{\sqrt{15}}\le a<\alpha.
\]
At \(a=\alpha\) the ratio is \(1\), while for \(a>\alpha\) it is below \(1\).

As an exact rationally anchored example, take \(a=69/260\). Then \(s=269/260\) and \(r=69/269\). The inequalities
\[
\frac14<\frac{69}{269}<2^{1/3}-1
\]
follow respectively from \(276>269\) and
\[
338^3=38614472<38930218=2\cdot269^3.
\]
Thus this single explicit member already has \(d_3(E_a)>\Delta_a\).

## Verification
The accompanying `verify.py` checks the exact polynomial factorization, the conversion of the lower endpoint to \(r=1/4\), and the integer inequalities for the rational example \(a=69/260\). These checks are redundant with the displayed proof; no finite sampling is used to justify the interval statement.

A separate numerical diagnostic gives
\[
\alpha=0.269172544981613\ldots,
\]
and for \(a=69/260\) the squared product ratio is approximately \(1.020645150198\), comfortably above \(1\). The numerical values are not proof inputs.

## Relationship to prior work
Hästö, Ibragimov and Minda introduce constant \(3\)-diameter, prove their Cassinian Reuleaux square has constant \(3\)-diameter, and then ask in Question 6.2 whether the analogous Reuleaux rectangles on \((\pm1,\pm a)\) always have constant \(3\)-diameter. In the square proof, the common product of every three-corner triple is the target global \(3\)-diameter, so checking whether that corner value continues to dominate is a natural first implication to test.

The finding here does not contradict the possibility that some affected Reuleaux rectangles have constant \(3\)-diameter at a larger value. It proves the narrower and exact statement that the square's corner-controlled value fails on a sharp interval for the explicit diagonal-midpoint witness.

A later paper by Ibragimov and Le studies \(n\)-diameters of planar sets of ordinary constant width and cites the 2012 \(3\)-diameter work, but its objects and extremal problem are different; searches of that full text found no Cassinian Reuleaux rectangle analysis and no implication covering the present threshold.

## Limitations
This result does not compute the full \(3\)-diameter of \(E_a\), does not classify the global maximizing triples, and does not settle Question 6.2. The upper endpoint is sharp only for the stated diagonal-midpoint/opposite-corner witness. Literature searches cannot exclude unindexed or differently phrased prior work.

The source-date evidence is the exact date printed on the publicly accessible accepted manuscript; an earlier public-posting timestamp was not established during the literature check.

## References
1. P. Hästö, Z. Ibragimov, D. Minda, “Convex Sets of Constant Width and 3-Diameter,” accepted-manuscript copy dated June 15, 2010; later published in Houston Journal of Mathematics 38(2) (2012), 421–443. Public manuscript: https://www.problemsolving.fi/pp/transdiamFinal.pdf . Primary MSC \(51M04\).
2. Z. Ibragimov, T. Le, “The \(n\)-diameter of planar sets of constant width,” Involve 5(3) (2012), 327–338, DOI 10.2140/involve.2012.5.327.
