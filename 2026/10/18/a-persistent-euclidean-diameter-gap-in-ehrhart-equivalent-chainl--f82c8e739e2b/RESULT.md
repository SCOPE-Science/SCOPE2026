# A persistent Euclidean diameter gap in Ehrhart-equivalent chainlink sections

## Finding
For every integer \(m\ge 3\), set
\[
\mathbf a_m=(2m+2,2m,2m+1),\qquad \ell=m,
\]
and define the chainlink polytope
\[
\mathrm{CL}(\mathbf a_m,\ell)=\bigl\{x\in\mathbb R^3:\ 0\le x_i\le a_i,\quad x_i-x_{i+1}\le a_i-\ell\ (i\bmod 3)\bigr\}.
\]
Its two complementary plane sections are
\[
P_m=\mathrm{CL}(\mathbf a_m,m)\cap\{x_1+x_2+x_3=2m\},\qquad
Q_m=\mathrm{CL}(\mathbf a_m,m)\cap\{x_1+x_2+x_3=4m+3\}.
\]
They have the same Ehrhart quasipolynomial, by the established complementary-section theorem [1], but their **ordinary intrinsic Euclidean diameters** obey the new exact identities
\[
\boxed{\operatorname{diam}(P_m)^2=\frac{7m^2}{2}+5m+2},\qquad
\boxed{\operatorname{diam}(Q_m)^2=\frac{7m^2}{2}+\frac{11m}{2}+\frac72}.
\]
Thus
\[
\boxed{\operatorname{diam}(Q_m)^2-\operatorname{diam}(P_m)^2=\frac{m+3}{2}>0},
\quad
\boxed{\lim_{m\to\infty}\bigl(\operatorname{diam}(Q_m)-\operatorname{diam}(P_m)\bigr)=\frac{1}{2\sqrt{14}}}.
\]
In particular, these Ehrhart-equivalent polygonal sections are never Euclidean-congruent, and their unscaled diameter difference does not vanish as their size tends to infinity.

## Assumptions and scope
The parameter \(m\) is an integer at least \(3\). All distances use the standard Euclidean metric of the ambient \(\mathbb R^3\), restricted to the respective two-dimensional section planes. The lengths \(2m,2m+1,2m+2\) are consecutive and the link number \(\ell=m\) saturates the permitted inequality \(2\ell\le\min_i a_i\). The slicing heights are complementary since \(\sum_i a_i=6m+3\). The assertion concerns diameter, not graph diameter, inradius, or minimum enclosing sphere.

## Proof
**Step 1: Ehrhart equivalence.** The complementary-section theorem for chainlink polytopes [1, Theorem 4.8] applies because \(2m=\min_i a_i\). Its two complementary integer heights are \(2m\) and \(6m+3-2m=4m+3\). Thus the sections have the same Ehrhart quasipolynomial. This equivalence is an established result and is not asserted as new.

**Step 2: Exact vertex census.** Put \((x,y,z)=(x,y,t-x-y)\). The section at any height \(t\) is cut out in the \((x,y)\)-plane by exactly the following nine inequalities:
\[
\begin{gathered}
-x\le0,\quad x\le2m+2,\quad -y\le0,\quad y\le2m,\\
x+y\le t,\quad -x-y\le2m+1-t,\\
x-y\le m+2,\quad x+2y\le t+m,\quad -2x-y\le m+1-t.
\end{gathered}
\]
The following tables list all six distinct extreme points of each polygon when \(m\ge3\). Triples are given in ambient coordinates; the columns can be verified by pairwise intersections of the nine supporting lines. The associated symbolic certificate `CHECK.py` proves that the listed points satisfy all nine inequalities for every \(m\ge3\), and that every other pairwise line intersection violates an inequality for the entire same parameter range. This is an exhaustive analytic vertex census, not finite sampling.

| Vertex | Coordinates in \(P_m\) |
|---|---|
| \(L_1\) | \(\bigl(0,3m/2,m/2\bigr)\) |
| \(L_2\) | \(\bigl(0,m-1,m+1\bigr)\) |
| \(L_3\) | \(\bigl(m+2,0,m-2\bigr)\) |
| \(L_4\) | \(\bigl((m-1)/2,0,(3m+1)/2\bigr)\) |
| \(L_5\) | \(\bigl((3m+2)/2,(m-2)/2,0\bigr)\) |
| \(L_6\) | \(\bigl(m,m,0\bigr)\) |

| Vertex | Coordinates in \(Q_m\) |
|---|---|
| \(H_1\) | \(\bigl(2m+2,m,m+1\bigr)\) |
| \(H_2\) | \(\bigl(2m+2,(3m+1)/2,(m+1)/2\bigr)\) |
| \(H_3\) | \(\bigl(m+3,2m,m\bigr)\) |
| \(H_4\) | \(\bigl(m/2+1,2m,3m/2+2\bigr)\) |
| \(H_5\) | \(\bigl(3m/2+2,m/2,2m+1\bigr)\) |
| \(H_6\) | \(\bigl(m,m+2,2m+1\bigr)\) |

**Step 3: Exhaustive diameter comparisons.** In a convex polygon, a diametral pair can be taken among its vertices: fixing one point, the Euclidean distance to it is convex and maximized at some vertex, and the argument can be repeated for the other point. For \(P_m\), the pairs \((L_1,L_5)\) and \((L_2,L_5)\) both have squared distance \(7m^2/2+5m+2\). For \(Q_m\), the pair \((H_2,H_4)\) has squared distance \(7m^2/2+11m/2+7/2\). Subtracting each competing pairwise squared distance from the corresponding proposed maximum yields a polynomial that, after writing \(u=m-3\), has only nonnegative rational coefficients. The exact polynomials are generated and checked in `CHECK.py`; hence they are nonnegative for all \(u\ge0\). The witness pairs attain equality, proving the two diameter formulas for every integer \(m\ge3\).

**Step 4: Persistent separation.** Direct subtraction gives the squared-diameter gap \((m+3)/2\). Rationalizing the difference of square roots gives
\[
\operatorname{diam}(Q_m)-\operatorname{diam}(P_m)
=\frac{(m+3)/2}{\sqrt{7m^2/2+11m/2+7/2}+\sqrt{7m^2/2+5m+2}}
\longrightarrow\frac{1}{2\sqrt{14}}.
\]
This proves the stated strictly positive limiting gap and noncongruence.

## Verification
The standalone exact-arithmetic script `CHECK.py` requires Python 3 and SymPy. Execute `python CHECK.py` from the directory containing it. It symbolically enumerates all \(33\) pairwise intersections of nonparallel supporting lines at each height, certifies six and only six feasible vertices for every \(m\ge3\), checks every one of the \(15\) squared vertex distances per section by polynomial coefficient positivity, and checks both diameter witnesses and the asymptotic limit. No floating-point tolerance or bounded integer census is used.

## Relationship to prior work
Kantarcı Oğuz, Özel, and Ravichandran [1] introduced chainlink polytopes and proved complementary sections share an Ehrhart quasipolynomial. Their displayed example at link number \(2\), lengths \((6,4,5)\), and heights \(4,11\) is the boundary case \(m=2\) of the present parametrization; that example is expressly not claimed as new. The contribution here is a complete, uniform Euclidean-diameter calculation for every \(m\ge3\), including a nonzero asymptotic absolute separation. The source's Ehrhart identity alone does not provide the diameter values: Ehrhart-equivalent polygons need not have equal Euclidean diameters.

## Limitations
No assertion is made for arbitrary chain compositions, link numbers, or heights. The proof does not classify all possible metric discrepancies between Ehrhart-equivalent chainlink sections. The earlier paper supplies the lattice-point equivalence; the only newly proved geometric assertion is the explicit diameter pair and its persistent gap. The bibliographic comparison does not exclude an unindexed equivalent computation, and independent mathematical validation has not been performed.

## References
[1] E. Kantarcı Oğuz, C. Y. Özel, M. Ravichandran, *Chainlink Polytopes and Ehrhart-Equivalence*, arXiv:2211.08382v1 (first public posting 2022-11-15), especially Definition 3.1, Theorem 4.8, and Figure 2. https://arxiv.org/html/2211.08382v1

[2] Mathematical Subject Classification 2020, 52B20 (lattice polytopes in convex geometry). https://mathscinet.ams.org/msc/msc2020.html?t=52B20
