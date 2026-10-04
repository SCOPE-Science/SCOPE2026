# Sharp inradius bound for triangles contained in a rectangle
## Finding
Let a rectangle have side lengths \(a\ge b>0\). For every nondegenerate Euclidean triangle \(T\) contained in the rectangle, with inradius \(r\),
\[
r\le \frac{ab}{a+\sqrt{a^2+4b^2}}.
\]
The constant is sharp. Equality is attained by taking a full side of length \(a\) as the base and the midpoint of the opposite side as the third vertex. When \(a=b\), this becomes \(r\le (\sqrt5-1)a/4\), the known sharp square bound.

## Assumptions and scope
The rectangle and triangle are Euclidean, the triangle is nondegenerate, and containment includes the boundary. Write \(h=b/a\), so \(0<h\le1\). Similarity lets us scale to the rectangle \([0,1]\times[0,h]\).

The standard containment reduction used for the square extends verbatim to a rectangle. First extend any interior triangle vertex along an incident side until it reaches the rectangle boundary; this only enlarges the triangle and cannot decrease its inradius. Once all three vertices are on the rectangle boundary, at least one rectangle side has no triangle vertex in its relative interior. Translate the triangle toward that side until a vertex on an adjacent side reaches a corner; this translation preserves the inradius and containment. Extend the two sides issuing from that corner to the rectangle boundary. If both extensions hit the same opposite edge, the resulting triangle lies in the corresponding corner half-rectangle triangle. Consequently it suffices to consider corner triangles
\[
O=(0,0),\qquad M=(1,y),\qquad N=(x,h),
\]
with \(0\le x\le1\) and \(0\le y\le h\).

## Proof
For the corner triangle put
\[
A=h-xy,
\]
so twice its area is \(A\), and put
\[
P=\sqrt{1+y^2}+\sqrt{x^2+h^2}+\sqrt{(1-x)^2+(h-y)^2}.
\]
Then \(r=A/P\).

We first exclude an interior maximum. At an interior critical point, vary \((x,y)\) in the direction \((1,-1)\). Along \((x+t,y-t)\), one has \(A''=2\). Since the first derivative of \(r\) vanishes at a critical point,
\[
\frac{r''}{r}=\frac{2}{A}-\frac{P''}{P}.
\]
Set
\[
u=\sqrt{1+y^2},\quad v=\sqrt{x^2+h^2},\quad p=1-x,\quad q=h-y,\quad w=\sqrt{p^2+q^2}.
\]
Direct differentiation gives
\[
P''=\frac1{u^3}+\frac{h^2}{v^3}+\frac{(p+q)^2}{w^3}.
\]
Because \(A\le h\le1\) and \(u\ge1\),
\[
A/u^3\le u.
\]
Because \(v\ge h\),
\[
Ah^2/v^3\le h^3/v^3\le1\le u.
\]
Finally,
\[
A=h(1-x)+x(h-y)=hp+xq\le vw
\]
by Cauchy--Schwarz, while \((p+q)^2\le2w^2\). Hence
\[
A\frac{(p+q)^2}{w^3}\le2v.
\]
Therefore
\[
AP''\le2u+2v<2(u+v+w)=2P,
\]
so \(r''>0\). Thus no interior critical point can be a local maximum, and a global maximum occurs on the boundary of the parameter rectangle.

On \(y=0\),
\[
r=\frac{h}{1+\sqrt{x^2+h^2}+\sqrt{(1-x)^2+h^2}}.
\]
Convexity and symmetry minimize the denominator at \(x=1/2\), giving
\[
r_L=\frac{h}{1+\sqrt{1+4h^2}}.
\]
On \(x=0\), convexity gives the maximum at \(y=h/2\):
\[
r_S=\frac{h}{h+\sqrt{4+h^2}}.
\]
For \(0<h\le1\),
\[
h+\sqrt{4+h^2}-1-\sqrt{1+4h^2}
=(1-h)\left(\frac{3(1+h)}{\sqrt{4+h^2}+\sqrt{1+4h^2}}-1\right)\ge0,
\]
because \(\sqrt{4+h^2}\le2+h\) and \(\sqrt{1+4h^2}\le1+2h\). Hence \(r_L\ge r_S\).

On \(x=1\), write \(t=h-y\). Then
\[
r=\frac{t}{\sqrt{1+h^2}+t+\sqrt{1+(h-t)^2}},
\]
and differentiation shows this is strictly increasing in \(t\); its maximum is therefore
\[
r_R=\frac{h}{1+h+\sqrt{1+h^2}}.
\]
The boundary \(y=h\) gives the same value. Moreover,
\[
h+\sqrt{1+h^2}\ge\sqrt{1+4h^2},
\]
so \(r_R\le r_L\). Thus the global maximum is \(r_L\). Rescaling by \(a\) yields
\[
r\le a\frac{b/a}{1+\sqrt{1+4(b/a)^2}}=\frac{ab}{a+\sqrt{a^2+4b^2}}.
\]
The triangle with vertices \((0,0)\), \((a,0)\), and \((a/2,b)\) attains this value, proving sharpness.

## Verification
The accompanying verifier recomputes the four boundary profiles, checks the algebraic comparison inequalities on exact rational grids, verifies the key Cauchy--Schwarz identity algebraically, and stress-tests the full two-parameter corner quotient on deterministic grids for many rational aspect ratios. These computations are supplemental: the quantified statement follows from the analytic saddle and boundary arguments above.

## Relationship to prior work
Abi-Khuzam and Barbara proved the sharp unit-square case and reduced that problem to corner triangles. Their theorem states \(r\le(\sqrt5-1)/4\) in the unit square, with equality attained by an isosceles triangle of side lengths \(1,\sqrt5/2,\sqrt5/2\). The result here gives the exact aspect-ratio profile for every rectangle. It is not obtained by anisotropic scaling of the square theorem, because such a scaling does not preserve Euclidean circles or inradii.

Searches for the exact formula, for maximum inradius of a triangle contained in a rectangle, and for rectangular generalizations of the square theorem found no statement implying this profile. The closest identified published source is the square theorem itself.

## Limitations
This result concerns rectangles only; it does not claim an analogous formula for general parallelograms or convex quadrilaterals. The literature comparison cannot rule out an unindexed or differently phrased prior occurrence. The public source records the benchmark paper in the April 2001 issue; the date field uses the issue-date convention \(2001\)-\(04\)-\(01\).

## References
1. F. F. Abi-Khuzam and R. Barbara, “A Sharp Inequality And The Inradius Conjecture,” Mathematical Inequalities & Applications 4(2) (2001), 323–326. DOI 10.7153/mia-04-30.
2. L. Funar, “Problem 6477,” American Mathematical Monthly 81 (1984), 588, as cited in the preceding paper.
