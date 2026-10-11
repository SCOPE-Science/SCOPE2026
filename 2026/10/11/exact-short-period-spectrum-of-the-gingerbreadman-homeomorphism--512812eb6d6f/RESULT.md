# Exact short-period spectrum of the gingerbreadman homeomorphism

## Finding
Let \(F:\mathbb R^2\to\mathbb R^2\) be the gingerbreadman map
\[
F(x,y)=(1-y+|x|,x).
\]
Among positive integers \(p\le 11\), the **least periods** of its real periodic points are exactly
\[
\boxed{\{1,5,6,11\}}.
\]
Up to cyclic relabeling, there are **exactly two** distinct least-period-five orbits and **exactly two** distinct least-period-eleven orbits. The five-orbit itineraries, recorded as cyclic lists of first coordinates, are
\[
(-1,3,5,3,-1),\qquad(-1,1,3,3,1).
\]
Their respective return derivatives have determinant \(1\) and traces \(1\) and \(3\): the first is elliptic and the second hyperbolic. The eleven-orbit itineraries are
\[
\left(-\frac37,\frac57,\frac{15}7,\frac{17}7,\frac97,-\frac17,-\frac17,\frac97,\frac{17}7,\frac{15}7,\frac57\right)
\]
and
\[
\left(-\frac13,1,\frac73,\frac73,1,-\frac13,\frac13,\frac53,\frac73,\frac53,\frac13\right).
\]
Both eleven-orbits avoid the nonsmooth line \(x=0\), are hyperbolic, and have derivative traces \(-5\) and \(+5\), respectively. Their multipliers are \((\pm5\pm\sqrt{21})/2\), with the two signs chosen consistently with the trace.

## Assumptions and scope
All initial conditions are arbitrary points of \(\mathbb R^2\); the mapping is exact and no boundedness, nonzero-coordinate, or generic-position hypothesis is imposed. A periodic point of least period \(p\) is one for which \(F^p(x,y)=(x,y)\) and \(F^d(x,y)\ne(x,y)\) for every integer \(1\le d<p\). An orbit means the cyclic equivalence class of its \(p\) points. The statement classifies least periods only through \(11\), not the global period spectrum. The date-stamped source attached to this map is a 2006 public visualization; Devaney's founding study is known from 1984 but the precise day of its initial public appearance was not established.

## Proof
Write \((x_k,x_{k-1})\) for the state at step \(k\). Then
\[
x_{k+1}+x_{k-1}=1+|x_k|.
\]
For a proposed period \(p\) fix an arbitrary sign word \(s=(s_0,\dots,s_{p-1})\in\{-1,1\}^{p}\). On the associated closed orthant \(s_kx_k\ge0\), the periodicity equations are the **linear affine system**
\[
 x_{k+1}+x_{k-1}-s_kx_k=1,\qquad k\pmod p,
\]
with all subscripts interpreted modulo \(p\). The sign inequalities are necessary and sufficient: if they hold, \(s_kx_k=|x_k|\), so the linear system is exactly the nonlinear recurrence. At a zero coordinate both choices of sign are allowed, ensuring exhaustive coverage including branch boundaries.

The attached `verify_periods.py` enumerates all \(2^p\) sign words for each \(1\le p\le11\). Its rational row reduction solves each affine linear system, including inconsistent and singular ones. For a nonempty affine solution space \(x=x^{(0)}+\sum_j t_jv^{(j)}\), it determines **exactly**, by rational Fourier–Motzkin elimination, whether the \(p\) sign inequalities have a common real solution. Fourier–Motzkin elimination is exact: when eliminating one variable, each pair of lower and upper affine bounds must satisfy the corresponding cross-multiplied inequality, and if no opposing bound exists the variable can be chosen on the unbounded side. Iterating this operation is equivalent to projection of the original non-strict polyhedron, including all boundary cases.

The exhaustive rational census is:

| Proposed period \(p\) | Sign words admitting a periodic point | Feasible singular sign words | Distinct isolated least-\(p\) orbits |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 1 | 0 | 0 |
| 3 | 1 | 0 | 0 |
| 4 | 1 | 0 | 0 |
| 5 | 11 | 0 | 2 |
| 6 | 13 | 7 | 1 |
| 7 | 1 | 0 | 0 |
| 8 | 1 | 0 | 0 |
| 9 | 1 | 0 | 0 |
| 10 | 11 | 0 | 0 |
| 11 | 23 | 0 | 2 |

The column of isolated orbits deliberately excludes non-isolated affine families; it is **not** an asserted count of all period-six orbits. For periods \(3\) and \(9\), singular affine equations occur but none of their singular sign words is feasible. At periods \(5\) and \(11\) every feasible sign word has a unique rational solution, so listing and deduplicating their cyclic rotations is exhaustive. At period \(10\), the feasible words produce only the fixed point and the two period-five orbits; at periods \(2,3,4,7,8,9\) they produce only the fixed point \((1,1)\). A least-period-six witness is the orbit beginning at \((1/2,1/4)\), whose consecutive states are
\[
(1/2,1/4),(5/4,1/2),(7/4,5/4),(3/2,7/4),(3/4,3/2),(1/4,3/4).
\]
These six points are distinct and the next iterate returns to the first. Thus the least-period set is precisely the announced set.

Finally, on a state with first coordinate nonzero the Jacobian is \(A_s=\begin{pmatrix}s&-1\\1&0\end{pmatrix}\), with determinant \(1\). Multiplying the exact matrices along the four listed isolated cycles gives, in the same order as their display above, the five-cycle return matrices
\[
\begin{pmatrix}0&-1\\1&1\end{pmatrix},\quad
\begin{pmatrix}2&1\\1&1\end{pmatrix}
\]
and the eleven-cycle return matrices
\[
\begin{pmatrix}-4&-3\\-1&-1\end{pmatrix},\quad
\begin{pmatrix}2&1\\5&3\end{pmatrix}.
\]
Their traces and eigenvalue types follow from the characteristic polynomial \(\lambda^2-\operatorname{tr}(A)\lambda+1\). All of the listed cycles have strictly nonzero first coordinates, so these derivatives are well defined.

## Verification
Run `python3 verify_periods.py` with Python 3 and no external packages. The program prints the census, exact rational cyclic representatives, their integer return matrices, and `CERT_OK` only after assertions for the four allowed least periods, the two exact five- and eleven-orbit counts, period-six witness, and eleven-cycle trace. Its arithmetic uses `fractions.Fraction` throughout linear algebra and feasibility checks; there are no floating-point or tolerance tests. The finite exhaustive proof depends on the displayed reduction from periodicity to finitely many rational linear feasibility problems, not on visual experiments. The attached `certificate_output.txt` reproduces the actual checker output.

## Relationship to prior work
Devaney introduced the gingerbreadman model in 1984 (DOI below). A later exact study of the general Lozi difference equation by Abu-Saris and Al-Jubouri (2009), whose full text was inspected, specializes to this map at \(\alpha=1,\beta=-1,\gamma=1\); it derives general periodicity criteria and classifies periods two and three but does not give this finite full-spectrum census or the eleven-cycle multipliers. MathWorld lists the well-known outer five-cycle \((-1,3,5,3,-1)\); the second, hyperbolic five-cycle displayed here is a distinct global orbit and should not be mistaken for a cyclic rotation of that listed orbit. MathWorld's wording could be understood as confined to the five peripheral hexagonal regions rather than as a global classification. Recent work by Cima, Gasull, Mañosa, and Mañosas treats a **different** two-absolute-value dissipative planar family and does not imply the present conservative-map census.

## Limitations
No claim is made about least periods exceeding \(11\), the complete period-six families, global invariant sets, or chaos. A finite sign-word census proves this finite statement only; it cannot establish absence of any longer orbit. The founding 1984 article was identified but its complete text was not accessible in the checked sources; an unindexed equivalent earlier low-period census remains a residual originality risk. In metadata, the exact public-source calendar date refers to a verifiably dated 2006 map visualization, not to the first appearance of Devaney's 1984 paper, whose exact first-public day was not established.

## References
1. R. L. Devaney, *A Piecewise Linear Model for the Zones of Instability of an Area Preserving Map*, Physica D **10** (1984), 387–393, DOI: 10.1016/0167-2789(84)90187-8.
2. R. M. Abu-Saris and N. K. Al-Jubouri, *On the Periodicity of Lozi's Equation*, Communications in Applied Analysis **13** (2009), 47–56, https://www.acadsol.eu/en/articles/13/1/6.pdf.
3. E. W. Weisstein, *Gingerbreadman Map*, MathWorld, https://mathworld.wolfram.com/GingerbreadmanMap.html.
4. C. Rocchini, *Gingerbreadman chaotic map (color by cycle size)*, publicly posted 2006-12-20, https://commons.wikimedia.org/wiki/File:Gingerbreadman_map.png.
5. A. Cima, A. Gasull, V. Mañosa, and F. Mañosas, *Invariant Graphs and Dynamics of a Family of Continuous Piecewise Linear Planar Maps*, Qualitative Theory of Dynamical Systems (2025), DOI: 10.1007/s12346-025-01221-1.
