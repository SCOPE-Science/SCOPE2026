# Exact dyadic basins and oscillating directional densities for equilateral farthest projections

## Finding
For the farthest-orthogonal-projection map on the **three complete supporting lines** of a unit equilateral triangle, the recurrent set consists of exactly three fixed side midpoints and two primitive period-three orbits. Every point converges to one of the two three-cycles, unless it belongs to the following explicit countable exceptional set, in which case it reaches a midpoint in finitely many steps.

In the unit arclength parameterization of any oriented supporting line, let \(t\in\mathbb R\) increase from one triangle vertex at \(t=0\) to the next at \(t=1\). Write \(p=t-1/2\). The fixed-point basin on that line is exactly
\[
\{p=0\}\;\cup\;\bigl\{p=\pm(2^m-\tfrac12):m=0,1,2,\ldots\bigr\}.
\]
Every other point converges toward the positive-orientation three-cycle (the three points with \(t=2/3\)) if and only if
\[
\operatorname{sgn}(p)=(-1)^{m(|p|)},\qquad
m(r)=\min\{m\in\mathbb Z_{\ge0}:r+\tfrac12\le 2^m\}.
\]
The remaining nonexceptional points converge toward the negative-orientation three-cycle (the three points with \(t=1/3\)). The orientation names refer to decreasing or increasing supporting-line index, respectively.

A measurable consequence is **nonexistence of a directional basin density**. On any one of the three parameter rays \(p=r>0\), let \(B_+\) comprise those \(r\) whose trajectory approaches the \(t=2/3\) three-cycle, and let \(\lambda\) be arclength. Then
\[
D(R)=\frac{\lambda(B_+\cap(0,R))}{R},\qquad
\liminf_{R\to\infty}D(R)=\frac13,\qquad
\limsup_{R\to\infty}D(R)=\frac23.
\]
In particular, every individual initial condition has an asymptotic periodic orbit, but the relative prevalence of its attracting three-cycle on a growing **one-sided** segment never settles. All invariant Borel probability measures on the union of complete lines are precisely the convex combinations of the three midpoint Dirac masses and the two uniform measures on the three-cycles.

## Assumptions and scope
Let \(V_0=(0,0)\), \(V_1=(1,0)\), \(V_2=(1/2,\sqrt3/2)\) and \(L_i\) be the complete line through \(V_i,V_{i+1}\), with indices interpreted modulo three. Write
\[
x(i,t)=V_i+t(V_{i+1}-V_i),\qquad t\in\mathbb R.
\]
The phase space \(X=L_0\cup L_1\cup L_2\) is a subset of the Euclidean plane, not the bounded triangle boundary. For a point on one supporting line, compare the Euclidean distances to its orthogonal projections onto the other two supporting lines, and move to the *farther projection*. If the distances are tied, the point is declared fixed. At triangle vertices the two possible line descriptions produce the same image, so this defines a single-valued map \(T:X\to X\). Convergence to a three-cycle means distance to that finite orbit tends to zero, with the corresponding cyclic phase.

## Proof
**1. Global piecewise-affine normal form.** At \(x(0,t)=(t,0)\), the distances to \(L_1\) and \(L_2\) are respectively \(\sqrt3|1-t|/2\) and \(\sqrt3|t|/2\). Orthogonal projection onto \(L_1\) has \(L_1\)-parameter \((1-t)/2\), while projection onto \(L_2\) has \(L_2\)-parameter \(1-t/2\). Rotation by \(2\pi/3\) establishes the same expressions for every \(i\). Thus
\[
T(i,t)=
\begin{cases}
(i+1,(1-t)/2),&t<1/2,\\
(i,t),&t=1/2,\\
(i-1,1-t/2),&t>1/2,
\end{cases}
\]
with indices modulo three. For \(p=t-1/2\ne0\), the new centered parameter is
\[
p'=-\frac p2+\frac{\operatorname{sgn}(p)}4,
\]
and the line index increases by one when \(p<0\) and decreases by one when \(p>0\). The midpoint \(p=0\) is fixed. The same geometric point can have two descriptions only at a vertex, \(t=0\) or \(t=1\), and both descriptions map to the same opposite midpoint.

**2. Exact entrance time and exceptional set.** If \(|p|>1/2\), then \(p'\) changes sign and the radius \(r=|p|\) evolves by \(r'=r/2-1/4\). As long as these outer steps occur, \(r_n+1/2=2^{-n}(r_0+1/2)\). The least \(m\ge0\) at which \(r_m\le1/2\) is therefore exactly \(m(r_0)\) in the Finding. After \(m\) outer steps,
\[
r_m=2^{-m}(r_0+\tfrac12)-\tfrac12\in(0,1/2],
\qquad \operatorname{sgn}(p_m)=(-1)^m\operatorname{sgn}(p_0).
\]
The endpoint \(r_m=1/2\) occurs precisely if \(r_0=2^m-1/2\). Its next image is the midpoint. Together with \(p_0=0\), these and only these initial points eventually reach a midpoint. In particular, all other points eventually enter the ordinary bounded side segments \(0<t<1\).

**3. Convergence, full periodic census, and basins.** On the inner region \(0<|p|<1/2\), the sign stays constant under iteration. Writing that sign as \(s\in\{-1,1\}\), the iterates satisfy for every \(k\ge0\)
\[
p_{m+k}=\frac{s}{6}+(-\tfrac12)^k\left(p_m-\frac{s}{6}\right).
\]
Consequently the three points \((i,2/3)\), one on each line, form a primitive three-cycle with decreasing line indices, and the three points \((i,1/3)\) form the other with increasing indices. All nonexceptional trajectories converge exponentially after their finite outer entrance time, with limiting sign \(s=(-1)^m\operatorname{sgn}(p_0)\). No other recurrent or periodic points are possible: every nonexceptional noncycle point has centered parameter converging strictly to \(s/6\), outer points first fall into the inner region, and exceptional points terminate at a midpoint. The fixed points are exactly the three midpoints.

**4. Exact directional basin lengths.** On the positive-centered ray \(p=r>0\), the \(t=2/3\) cycle is selected exactly on the open dyadic shells with even \(m(r)\). The first shell is \((0,1/2)\); for integers \(m\ge1\), shell \(m\) is
\[
I_m=(2^{m-1}-\tfrac12,\;2^m-\tfrac12),
\qquad \lambda(I_m)=2^{m-1}.
\]
Shell endpoints are exceptional and have zero arclength. Summing the even-indexed shell lengths through \(m=2k\) gives, for each integer \(k\ge1\),
\[
\lambda\bigl(B_+\cap(0,4^k-\tfrac12)\bigr)=\frac23 4^k-\frac16.
\]
The immediately following odd shell adds no positive-cycle basin length. Hence the two endpoint fractions are
\[
D(4^k-\tfrac12)=\frac{\frac23 4^k-\frac16}{4^k-\frac12}
\longrightarrow\frac23,\qquad
D(2\cdot4^k-\tfrac12)=\frac13.
\]
Inside any even shell \(D(R)\) increases (only positive-cycle length is added), while inside an odd shell it decreases (none is added). The extrema on successive endpoint shells therefore converge to \(2/3\) and \(1/3\), proving the precise limsup and liminf. The negative-centered ray exchanges the two cycle labels. By reflection symmetry, the plus and minus basins have equal length on each **symmetric** centered interval; the density failure concerns one-sided rays only.

**5. Invariant probabilities.** Every nonperiodic point has an orbit that eventually enters a strict-contraction branch and approaches a periodic orbit without recurring to its starting point. The recurrent set thus consists of the nine points of the two three-cycles and three midpoints. Poincaré recurrence for any invariant Borel probability on \(X\) implies that it assigns mass one to this finite recurrent set. Its invariance forces equal weights around each three-cycle, while each fixed midpoint may have arbitrary nonnegative mass. This yields exactly the five-extreme-point simplex of invariant probabilities stated above.

## Verification
The accompanying `verify.py` uses only Python's standard library. In oblique coordinates whose exact Gram matrix has entries \(1,1,1/2\), it compares literal orthogonal projections, the selected farthest target and the piecewise affine formula at \(6147\) rational starting locations spanning all three complete lines. It checks the predicted basins by \(135\) exact iterations per location, both three-cycle equations, all dyadic exceptional points through exponent \(15\), and the two shell-proportion identities for exponents up to \(19\). Execute `python3 verify.py`; it prints `CHECK_OK 6147 exact geometric projection and basin tests; exact dyadic endpoints and two cycle equations`. These are finite rational diagnostics, not an infinite proof of the global assertions.

## Relationship to prior work
Everett's original farthest-projection model, Definition 2.1, and its qualitative convergence theorem are established prior work. The full-three-line setting and tie convention are inherited directly. A subsequent exact classification of primitive period-three cycles for **all** triangle shapes already implies existence and uniqueness of the two equilateral three-cycles, and proves their local attraction. Neither earlier result states or implies the full equilateral basin partition, the countable dyadic fixed-point preimages, or the exact divergent directional basin-density law. A related work on **prescribed cyclic compositions** of projections does not use Everett's state-dependent farthest-choice rule, so cannot substitute for the dyadic phase calculation. The present finding is the joint global basin and directional frequency classification, not the existence of the two three-cycles itself.

## Limitations
The conclusions are for three **complete equilateral supporting lines**, not for general triangles or arbitrary finite edges; the directional density uses arclength in one fixed oriented **half-ray**. No asymptotic density is claimed for a symmetric two-sided truncation, where symmetry gives a different answer. The result is an exact solvable case, not a general theorem on piecewise contractions. The existence of an unindexed equivalent result, or details not included in other published treatments of the same map, remains a publication-priority risk. Independent mathematical audit has not been performed.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* **18** (2020 issue), 183–192, DOI `10.1080/1726037X.2020.1847765`, publisher verified online publication **January 7, 2021**; lawful author manuscript arXiv `2408.16019v1` (posted August 26, 2024). The publisher's online date, not issue date or manuscript upload, determines the public-source date.
2. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, published mathematical record, October 2026, `https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`.
3. Samuel Everett, *A Geometric Dynamical System with Relation to Polygonal Billiards*, arXiv `2112.02207v1` (2021), especially its prescribed-composition formulation.
