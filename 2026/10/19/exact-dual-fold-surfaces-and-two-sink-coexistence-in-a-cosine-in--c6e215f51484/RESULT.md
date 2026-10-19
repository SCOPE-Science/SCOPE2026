# Exact dual fold surfaces and two-sink coexistence in a cosine interval map

## Finding
Consider the Lawnik–Moysis–Volos cosine piecewise interval map, with parameters \(0<a,b,c<1\):
\[
F_{a,b,c}(x)=\begin{cases}
1-(1-a)\cos\!\left(\dfrac{\pi x}{2b}\right),&0\le x\le b,\\
c\cos\!\left(\dfrac{\pi(x-1)}{2(1-b)}\right),&b<x\le1.
\end{cases}
\]
For each \(b\in(0,1)\), define \(u_b\in(0,1)\) as the **unique** solution of
\[
\frac{\pi}{2}(1-bu_b)\sin\left(\frac{\pi u_b}{2}\right)
=b\cos\left(\frac{\pi u_b}{2}\right),
\]
and put
\[
A(b)=1-\frac{1-bu_b}{\cos(\pi u_b/2)},\qquad
C(b)=1-A(1-b).
\]
These are exact, well-defined, sharp fold surfaces satisfying
\[
0<A(b)<1-\frac2\pi,\qquad \frac2\pi<C(b)<1.
\]
The **complete fixed-point census** for all admissible triples is
\[
N(a,b,c)=N_L(a,b)+N_R(b,c),
\]
where
\[
N_L=\begin{cases}2,&a<A(b),\\1,&a=A(b),\\0,&a>A(b),\end{cases}
\qquad
N_R=\begin{cases}2,&c>C(b),\\1,&c=C(b),\\0,&c<C(b).\end{cases}
\]
In each strict two-root left phase the smaller fixed point is attracting and the larger repelling. In each strict two-root right phase the smaller fixed point is repelling and the larger attracting. Every fold fixed point has multiplier exactly \(+1\) and nonzero quadratic term; no fixed points lie at the switching point or endpoints.

Consequently, **four distinct hyperbolic fixed points, including two different attracting fixed points, exist exactly when**
\[
\boxed{a<A(b)\quad\text{and}\quad c>C(b).}
\]
This four-point phase is nonempty for **every** \(b\in(0,1)\), even arbitrarily near the endpoints. In particular, the exact rational parameter triple
\[
\boxed{(a,b,c)=\left(\frac1{100},\frac12,\frac{99}{100}\right)}
\]
has two attracting and two repelling fixed points. Conversely the fixed-point-free phase is exactly \(a>A(b)\) and \(c<C(b)\), with the equality cases covered by the census above.

Both thresholds are strictly increasing and obey the sharp endpoint laws
\[
A(b)=\frac{2b^2}{\pi^2}+O(b^4)\quad(b\downarrow0),\qquad
1-C(b)=\frac{2(1-b)^2}{\pi^2}+O((1-b)^4)\quad(b\uparrow1).
\]
Also \(A(b)\to1-2/\pi\) as \(b\uparrow1\), and \(C(b)\to2/\pi\) as \(b\downarrow0\).

## Assumptions and scope
The domain is exactly \([0,1]\) and \(a,b,c\) belong to the open unit interval. At \(x=b\) the map takes the **left** value \(F(b)=1\), whereas the right-hand limit is zero. It follows that \(x=b\) is never fixed; nor are \(x=0\) and \(x=1\), since their images are respectively \(a\) and \(c\). A fixed point is locally attracting when its derivative has modulus below one, and repelling when above one. Claims about periodic points and their stability are local only. No assertion is made about chaos or global attraction.

## Proof
**1. A unique threshold on the left.** Write \(u=x/b\in[0,1)\) and define
\[
h_b(u)=\frac{1-bu}{\cos(\pi u/2)}.
\]
For the left branch, the fixed-point equation is equivalent to \(h_b(u)=1-a\). Its derivative has numerator
\[
Q_b(u)=-b\cos\left(\frac{\pi u}{2}\right)
+\frac\pi2(1-bu)\sin\left(\frac{\pi u}{2}\right).
\]
The critical fact is the identity
\[
Q_b'(u)=\frac{\pi^2}{4}(1-bu)\cos\left(\frac{\pi u}{2}\right)>0
\qquad(0<u<1).
\]
Also \(Q_b(0)=-b<0\) and \(Q_b(1^-)=\pi(1-b)/2>0\). Thus there is exactly one critical point \(u_b\), a strict global minimum. Since \(h_b(0)=1\), \(h_b'(0)=-b<0\), and \(h_b(u)\to+\infty\) at the other endpoint, the minimum \(m_b=h_b(u_b)\) satisfies \(0<m_b<1\). Intersecting the graph with any level \(1-a\in(0,1)\) gives precisely two, one, or zero roots according as \(1-a>m_b\), equality, or \(1-a<m_b\). Setting \(A(b)=1-m_b\) gives the stated left census.

**2. The right threshold by reflection of the fixed-point equation.** Put \(s=(1-x)/(1-b)\in[0,1)\) on the right. The fixed-point condition is exactly
\[
c\cos\left(\frac{\pi s}{2}\right)=1-(1-b)s,
\quad\text{equivalently}\quad c=h_{1-b}(s).
\]
The same unimodal threshold analysis therefore gives zero, one, or two right roots according as \(c<m_{1-b}\), equality, or \(c>m_{1-b}\). Since \(m_{1-b}=1-A(1-b)\), this is the stated \(C(b)\). This is an identity of the *interior fixed-point equations*, not an assertion that the two discontinuous maps, including their different switching-point conventions, are globally conjugate.

**3. Stability and fold type.** Let \(G_L(x)=F_{a,b,c}(x)-x\) on the left and \(G_R(x)=F_{a,b,c}(x)-x\) on the right. Direct differentiation gives
\[
G_L''(x)=(1-a)\left(\frac\pi{2b}\right)^2
\cos\left(\frac{\pi x}{2b}\right)>0\quad(0<x<b),
\]
\[
G_R''(x)=-c\left(\frac\pi{2(1-b)}\right)^2
\cos\left(\frac{\pi(x-1)}{2(1-b)}\right)<0\quad(b<x<1).
\]
Both branches have **positive** first derivative in their interiors. Moreover \(G_L(0)=a>0\), \(G_L(b)=1-b>0\), while \(G_R(b^+)=-b<0\), \(G_R(1)=c-1<0\). In the two-root left regime strict convexity therefore forces \(G_L'<0\) at the smaller root and \(G_L'>0\) at the larger root; hence their multipliers lie respectively in \((0,1)\) and \((1,\infty)\). Strict concavity reverses this ordering on the right. At a threshold the sole root is interior, the corresponding \(G\) and \(G'\) vanish and \(G''\ne0\). Varying \(a\) or \(c\) respectively gives a nonzero parameter derivative. Thus both critical points are nondegenerate saddle-node folds with multiplier \(+1\), attracting on one side and repelling on the other.

**4. Parameter geometry and sharp endpoints.** If \(b_2>b_1\), then for every \(u>0\), \(h_{b_2}(u)<h_{b_1}(u)\); testing the minimum of the first function at the minimizing point for the second gives \(m_{b_2}<m_{b_1}\). Consequently \(A(b)\) is strictly increasing, and so is \(C(b)=1-A(1-b)\). The function \(h_1(u)=(1-u)/\cos(\pi u/2)\) decreases to \(2/\pi\) as \(u\uparrow1\), and \(h_b(u)>h_1(u)\) for \(b<1\) and \(u>0\). Therefore \(m_b>2/\pi\), giving \(A(b)<1-2/\pi\); taking the pointwise \(b\uparrow1\) limit proves \(m_b\to2/\pi\). As \(b\downarrow0\), the unique root of \(Q_b\) has the expansion \(u_b=4b/\pi^2+O(b^3)\) by the implicit function theorem at \((b,u)=(0,0)\). Substitution into \(h_b(u_b)\) gives \(m_b=1-2b^2/\pi^2+O(b^4)\), proving the two quadratic endpoint laws, the second by reflection.

**5. Existence at every breakpoint and a rational witness.** For any \(b\in(0,1)\), the strict inequalities \(A(b)>0\) and \(C(b)<1\) permit simultaneous choices \(0<a<A(b)\) and \(C(b)<c<1\); hence exactly four fixed points, two attracting, occur for every breakpoint. In the explicit triple \((1/100,1/2,99/100)\), the residual \(F(x)-x\) is positive at \(x=0\), negative at \(x=1/6\), positive at \(x=b\), negative just to the right of \(b\), positive at \(x=5/6\), and negative at \(x=1\). The two negative/positive interior signs are the same exact inequality
\[
\frac{99\sqrt3}{200}>\frac56,
\]
which follows by squaring the positive numbers: \(3\cdot297^2=264627>250000=500^2\). By strict convexity and concavity there are exactly two roots in each branch. The stability types follow from step 3.

## Verification
The accompanying standard-library program `verify.py` recomputes the unique fold numerically, checks its fixed-point and multiplier-one identities, confirms strict threshold monotonicity on a finite test grid, and independently counts sign-changing roots away from the fold. It passed **591 finite checks**; the explicit four-root witness uses an exact integer inequality. This finite program checks consistency only; all quantifiers over \(0<a,b,c<1\) and the endpoint asymptotics are established by the proof above. Source equation and switching convention were checked against the complete accessible primary paper.

## Relationship to prior work
Lawnik, Moysis, and Volos (2023), Equation (20), introduce the precise trigonometric two-branch map. Their Section 4.2 describes its convex/concave branch geometry but gives *numerical* plots of parameter regions lacking fixed points. Their general intersection criterion in Section 3 does not determine the exact three-parameter fold curves, the full fixed-point census, multiplier types, or the quadratic endpoint laws. A published complete phase diagram for the **different fractional-power** member of their family (Equation (15), with an additional exponent) gives a useful comparison but no implication for the present cosine thresholds: that power model has a geometric restriction on the breakpoint in its four-point regime, whereas the cosine family supports four fixed points for every breakpoint. A later paper by Lawnik and coauthors (2024) concerns separately constructed logistic/tent-derived maps, based on its accessible abstract; its full manuscript could not be inspected. No assertion of exhaustive publication priority is made.

## Limitations
The result describes fixed points, nondegenerate folds and their local stability only. No classification of higher-period orbits, entropy, invariant densities, chaoticity, full attraction basins, or security performance follows. The parameter boundaries \(a=0,1\), \(b=0,1\), \(c=0,1\) are excluded. A full-text priority comparison with the related 2024 follow-up was limited by document access, although the abstract describes different maps. A generic convexity lemma underlies the root count; the new object-specific content is the exact coupled parameter census, dual implicit critical surfaces, universal four-point attainability, and sharp corner scaling.

## References
1. Marcin Lawnik, Lazaros Moysis, Christos Volos, *A Family of 1D Chaotic Maps without Equilibria*, **Symmetry** 15 (2023), article 1311, DOI: 10.3390/sym15071311. First public date verified as 27 June 2023; full text, especially Sections 3 and 4.2, inspected.
2. Marcin Lawnik, Lazaros Moysis, Murilo S. Baptista, Christos Volos, *Discrete one-dimensional piecewise chaotic systems without fixed points*, **Nonlinear Dynamics** 112 (2024), 6679–6693, DOI: 10.1007/s11071-024-09349-6. Abstract inspected; accepted-manuscript PDF access unsuccessful.
3. *Complete fractional-power fixed-point phase diagram for a discontinuous interval family* (2026), publicly available mathematical research record e0bdfaa72c7e. Different member of the Lawnik–Moysis–Volos family, Equation (15); complete result text compared.
