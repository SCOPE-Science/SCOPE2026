# Sharp Ehrhart sign transitions for joins with lattice segments

## Finding

Let the join of full-dimensional lattice polytopes \(P\subset\mathbb R^p\) and \(Q\subset\mathbb R^q\) mean the lattice polytope
\[
P*Q=\operatorname{conv}\bigl((P,0_q,0)\cup(0_p,Q,1)\bigr)\subset\mathbb R^{p+q+1}.
\]
An Ehrhart polynomial is *coefficientwise nonnegative* if every coefficient in its ordinary monomial expansion is nonnegative. The following two statements give sharp low-dimensional sign boundaries for joins of two coefficientwise positive factors.

**Segment--segment theorem.** For integers \(a,b\ge1\), put \(T_{a,b}=[0,a]*[0,b]\). Its Ehrhart polynomial is
\[
L_{T_{a,b}}(t)=\frac{ab}{6}t^3+\frac{a+b}{2}t^2+
\frac{6+3a+3b-ab}{6}t+1.
\]
Thus it has a negative coefficient exactly when \((a-3)(b-3)>15\). Among these joins, the minimum normalized lattice volume \(6\operatorname{vol}_3(T_{a,b})\) is **49**, attained exactly at \((a,b)=(7,7)\). In particular, dimension three is the smallest possible dimension of an Ehrhart-nonpositive join of two Ehrhart-positive lattice polytopes.

**Polygon--segment theorem.** Let \(P\subset\mathbb R^2\) be any full-dimensional lattice polygon with Euclidean area \(A>0\), boundary lattice-point count \(B\ge3\), and interior lattice-point count \(I\ge0\). Let \(b\ge1\) be an integer and \(J_{P,b}=P*[0,b]\). Then
\[
\begin{aligned}
L_{J_{P,b}}(t)={}&\frac{Ab}{12}t^4+
\frac{4A+Bb}{12}t^3+
\frac{(6-b)A+3B+6b}{12}t^2\\
&+\frac{2A+(3-b)B+6b+12}{12}t+1.
\end{aligned}
\]
Consequently, \(J_{P,b}\) is coefficientwise nonnegative **if and only if**
\[
(b-6)A\le3B+6b
\quad\text{and}\quad
(b-3)B\le2A+6b+12.
\]
These conditions give the exact sign pattern of every coefficient for every polygon and every positive integer segment length.

Two universal cutoffs are sharp. First, **every** lattice polygon joins Ehrhart-positively with every segment of length \(1\le b\le4\), whereas at \(b=5\) this fails, for example for
\[
P=\operatorname{conv}\{(0,0),(39,0),(0,1)\},
\quad (A,B,I)=(39/2,41,0).
\]
Here the linear coefficient is \(-1/12\). Among all \(b=5\) polygon--segment joins having a negative Ehrhart coefficient, the minimum normalized four-dimensional volume is **195**, attained by this example.

Second, a polygon--segment join can have **both** its linear and quadratic coefficients strictly negative if and only if \(b\ge8\) *in the existential sense* (for each such \(b\), at least one polygon has both coefficients negative). The single rectangle
\[
P=[0,37]\times[0,4]
\]
works for every \(b\ge8\); at \(b=8\) its linear and quadratic coefficients are \(-9/2\) and \(-1/6\), respectively. Therefore dimension four is the smallest dimension in which a join of two Ehrhart-positive lattice polytopes can have two negative Ehrhart coefficients.

## Assumptions and scope

All segments have **integer positive** lattice lengths, all polygons are full-dimensional convex lattice polygons, and lattice-point enumeration uses the ambient standard integer lattice. For a \(d\)-dimensional lattice polytope, normalized volume means \(d!\) times Euclidean volume. The claims concern ordinary Ehrhart coefficients, not the nonnegative \(h^*\)-coefficients. Endpoints at which a coefficient vanishes are included in the nonnegative class.

The segment--segment conclusion applies to all possible two-factor lattice joins of dimension three with both factors positive-dimensional. Joins with a point do not yield a smaller-dimensional counterexample, since every lattice polytope of dimension at most two has a nonnegative Ehrhart polynomial.

## Proof

**1. Counting integral height layers.** For a join \(P*[0,b]\) and each integer \(t\ge0\), the last coordinate of a lattice point in \(t(P*[0,b])\) is some \(j\in\{0,\ldots,t\}\). The remaining coordinates range independently over \((t-j)P\cap\mathbb Z^p\) and the \(bj+1\) integers in \([0,bj]\). Hence the exact count is
\[
L_{P*[0,b]}(t)=\sum_{j=0}^{t}L_P(t-j)(bj+1).
\]
No generic-position or smoothness assumptions enter this identity.

**2. Two segments and minimum volume.** Take \(L_{[0,a]}(s)=as+1\) in the layer count. Summing the elementary powers of \(j\) gives the displayed cubic. The two leading coefficients and constant term are positive, so negativity is equivalent to \(ab>3a+3b+6\), or \((a-3)(b-3)>15\). This forces \(a,b\ge4\). Put \(u=a-3\), \(v=b-3\). Then \(uv\ge16\), and AM--GM yields
\[
ab=uv+3(u+v)+9\ge16+6\sqrt{16}+9=49.
\]
Equality requires \(u=v=4\), namely \(a=b=7\), whose linear coefficient is \(-1/6\). The normalized volume equals \(ab\) by the leading Ehrhart coefficient. Every one- or two-dimensional lattice polytope has a nonnegative Ehrhart polynomial (the two-dimensional case follows from Pick's theorem), proving the dimension-minimal assertion.

**3. Polygon phase diagram.** Pick's theorem gives \(L_P(s)=As^2+(B/2)s+1\) and \(2A=2I+B-2\). Inserting this quadratic into the exact layer count and applying the standard sums of \(j\), \(j^2\), and \(j^3\) gives the displayed quartic. Its degree-four, degree-three, and constant coefficients are always positive. Thus exactly the two stated inequalities characterize coefficientwise nonnegativity, including equality boundaries.

For \(b\le4\), the quadratic coefficient has numerator \((6-b)A+3B+6b>0\). By Pick's relation the linear numerator becomes \(2I+(4-b)B+6b+10>0\). The displayed triangle has \(B=41\) and \(I=0\); at \(b=5\) its linear numerator is \(2I-B+40=-1\), proving sharpness. More generally, if a \(b=5\) join has a negative coefficient, then necessarily \(B>2I+40\). Thus \(2A=2I+B-2\ge4I+39\ge39\), and its normalized join volume \(2Ab\) is at least \(195\), with equality for the triangle.

For \(b\le6\), the quadratic coefficient is positive. At \(b=7\), simultaneous negativity would require both \(A>3B+42\) and \(A<2B-27\), impossible because \(B>0\). At \(b=8\), the rectangle \([0,37]\times[0,4]\) has \(A=148\), \(B=82\), giving both negative coefficients. For this same rectangle, at arbitrary \(b\) the numerators of the quadratic and linear coefficients are respectively \(1134-142b\) and \(554-76b\), both strictly decreasing in \(b\); hence they stay negative for every integer \(b\ge8\). Finally, every Ehrhart polynomial of degree at most three has positive leading, second-leading, and constant coefficients, leaving room for at most one negative coefficient. This proves the stated minimal dimension for two negative coefficients.

## Verification

The standalone file `join_sign_checker.py` performs independent exact-arithmetic checks using integer height-layer enumerations and rational Lagrange interpolation rather than symbolic substitution of the displayed formulas. It compares the resulting monomial coefficients for 3,388 finite parameter cases, independently enumerates small lattice triangles, and checks all three boundary witnesses. Run it as `python3 join_sign_checker.py`; the verified result was `LATTICE_JOIN_SIGN_PHASE_OK cases= 3388`.

These finite computations test the formulas but are not used as proofs for infinitely many polygons or segment lengths. The infinite parameter statements follow from the layer-count identity, Pick's theorem, and the sign arguments above.

## Relationship to prior work

Liu, Tao, and Xin (2026) established that Ehrhart positivity need not survive a lattice join and gave a general construction using a factor of dimension at least four. Their paper also records the standard multiplicativity of Ehrhart series under joins. The present result determines exact low-dimensional positivity regions, the smallest normalized-volume three-dimensional negative join, and two independent sharp segment-length cutoffs. The published existence result, without these new low-dimensional computations and inequalities, does not itself state those extremal values.

Castillo, Liu, Nill, and Paffenholz (2018) established negative Ehrhart coefficients in dimension three and simultaneous maximal negativity in higher dimensions for smooth-polytope constructions. The statements here concern **joins of Ehrhart-positive factors**, with exact boundary conditions; no claim is made that general three- or four-dimensional Ehrhart negativity was unknown.

## Limitations

The classification covers joins having one segment factor and other factor of dimension at most two; it is not a positivity classification for arbitrary higher-dimensional joins. The smallest-volume assertion \(49\) concerns joins of positive-dimensional lattice factors in dimension three, **not** all non-Ehrhart-positive three-dimensional lattice polytopes. The volume \(195\) assertion concerns the segment length \(b=5\), not all four-dimensional joins. The sharp \(b=8\) two-negative threshold is existential in the polygon variable, not a claim that every polygon has two negative coefficients for \(b\ge8\). Historical priority remains subject to broader expert literature review.

## References

- F. Liu, S. Tao, and G. Xin, *Ehrhart Theory of the Join of Two Lattice Polytopes*, arXiv:2606.18794, first posted June 17, 2026; in particular Proposition 1.2 and Section 2.
- F. Castillo, F. Liu, B. Nill, and A. Paffenholz, *Smooth polytopes with negative Ehrhart coefficients*, arXiv:1704.05532, 2018 version; Theorem 1.2.
- M. Beck and S. Robins, *Computing the Continuous Discretely*, second edition, Springer, 2015 (Ehrhart series and Pick's theorem).
