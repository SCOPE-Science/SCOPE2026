# A locked two-cycle and a sharp persistence transition in an absolute-value memristor map

## Finding

Consider the fixed-point-free map on the **entire real plane**
\[
F_{\alpha,\beta}(x,y)=\bigl(\alpha\cos x+\beta(|y|-1)x,\ y+x\bigr),\qquad \alpha>0,\quad\beta>0.
\]
For a prime-period-two orbit, count the unordered pair of its two points once. Define
\[
\beta_c=\frac4{4-\pi},\qquad \ell_\beta=2\left(1-\frac1\beta\right)\quad(\beta>1).
\]
If \(1<\beta<\beta_c\), put
\[
A_+(\beta)=\frac{\beta\ell_\beta^2}{2\cos\ell_\beta}.
\]
Then **the total number of geometrically distinct prime-period-two orbits is**
\[
N_2(\alpha,\beta)=
\begin{cases}
0,&0<\beta\le1,\\
2,&1<\beta<\beta_c\text{ and }0<\alpha<A_+(\beta),\\
1,&1<\beta<\beta_c\text{ and }\alpha=A_+(\beta),\\
0,&1<\beta<\beta_c\text{ and }\alpha>A_+(\beta),\\
2,&\beta\ge\beta_c\text{ and }\alpha>0.
\end{cases}
\]
The transition is particularly rigid: at \(\beta=\beta_c\), one of the two orbits is **independent of \(\alpha\)**,
\[
(\pi/2,-\pi/4)\ \longleftrightarrow\ (-\pi/2,\pi/4).
\]
For \(\beta>\beta_c\), the two orbits persist for every forcing magnitude, although one changes its sign itinerary. Their itinerary-change threshold is
\[
A_-(\beta)=\frac{\beta\ell_\beta^2}{-2\cos\ell_\beta}.
\]
Both finite thresholds diverge toward the persistence transition with the same sharp pole:
\[
A_\pm(\beta)\sim\frac{\pi^2\beta_c^3}{16|\beta-\beta_c|}
\quad\text{as }\beta\to\beta_c\text{ from their respective sides}.
\]

There is also a **complete sharp sink criterion for the smooth sign-crossing two-cycle**. For \(\beta>1\) set
\[
S_\beta=\sin\ell_\beta+\frac{\cos\ell_\beta}{\ell_\beta}.
\]
The crossing orbit (when both ordinate coordinates are strictly nonzero and of opposite sign) is locally attracting exactly when
\[
1<\beta<2,\qquad
0<\alpha<\min\left\{A_+(\beta),\frac{\sqrt2(2-\beta)}{S_\beta}\right\}.
\]
Its return Jacobian cannot be Schur stable for \(\beta\ge2\). The positive-ordinate two-cycle has a real two-step multiplier exceeding one wherever its derivative exists, so it never attracts locally. At the crossing/same-sign itinerary boundary the map is nonsmooth, and no differentiable stability assertion is made.

## Assumptions and scope

All variables are real, and the full, unbounded state space is \(\mathbb R^2\); \(\alpha>0\), \(\beta>0\). A two-cycle is a pair \(z_0\ne z_1\) with \(F(z_0)=z_1\) and \(F(z_1)=z_0\). A locally attracting smooth two-cycle means both eigenvalues of its two-step derivative have modulus strictly below one. Numerical approximations are illustrations only. No assumption of a compact invariant attractor, hyperchaos, or physical implementation is used.

## Proof

**1. Exact reduction and fixed-point exclusion.** A fixed point would have \(x=0\) from its second-coordinate equation, but its first-coordinate equation would require \(\alpha=0\), contrary to the hypotheses. For a two-cycle, the sum of the two changes in the second coordinate must vanish. Write its two first coordinates as \(u,-u\) with \(u>0\), and its two points as
\[
(u,v),\qquad (-u,v+u).
\]
The two first-coordinate equations are equivalent to
\[
\alpha\cos u=u(\beta-1-\beta|v|)
=u(1-\beta+\beta|v+u|).
\]
Consequently,
\[
|v|+|v+u|=\ell_\beta.
\tag{1}
\]
No solution exists when \(\beta\le1\). For \(\beta>1\), the triangle inequality gives \(0<u\le\ell_\beta<2\). Set \(t=v+u/2\). Equation (1) becomes
\[
2\max\{|t|,u/2\}=\ell_\beta.
\tag{2}
\]
The following cases are exhaustive, and substituting into either first-coordinate equation is also sufficient.

**2. All branches and exact counting.** If \(0<u<\ell_\beta\), equation (2) forces \(t=\ell_\beta/2\) or \(t=-\ell_\beta/2\).

* At \(t=\ell_\beta/2\) (both ordinates positive), \(v=(\ell_\beta-u)/2\) and
\[
\alpha\cos u=\frac{\beta u^2}2.
\tag{3}
\]
The only possible interval is \(0<u<\min\{\ell_\beta,\pi/2\}\). The function \(\beta u^2/(2\cos u)\) increases strictly from zero to \(A_+(\beta)\) if \(\ell_\beta<\pi/2\), and from zero to infinity if \(\ell_\beta\ge\pi/2\). Thus this branch gives at most one orbit, and it exists throughout \(\alpha>0\) when \(\beta\ge\beta_c\).

* At \(t=-\ell_\beta/2\) (both ordinates negative), \(v=-(\ell_\beta+u)/2\) and
\[
\alpha\cos u=-\frac{\beta u^2}2.
\tag{4}
\]
Hence this branch is possible only when \(\ell_\beta>\pi/2\), with \(\pi/2<u<\ell_\beta<2\). The function \(\beta u^2/(-2\cos u)\) is strictly decreasing on this interval: its derivative has the sign of \(-[2\cos u+u\sin u]\), and \(g(u)=2\cos u+u\sin u\) is decreasing yet positive there, because \(g'(u)=u\cos u-\sin u<0\) and \(g(2)=2(\cos2+\sin2)>0\). It runs from infinity down to \(A_-(\beta)\). There is exactly one such orbit for \(\alpha>A_-(\beta)\), and none below or at this threshold.

If \(u=\ell_\beta\), equation (2) permits \(-\ell_\beta/2\le t\le\ell_\beta/2\). The equation then fixes \(t\) **uniquely**:
\[
t=\frac{\alpha\cos\ell_\beta}{\beta\ell_\beta},\qquad
v=t-\frac{\ell_\beta}2.
\tag{5}
\]
It exists iff \(|\alpha\cos\ell_\beta|\le\beta\ell_\beta^2/2\). For \(\beta<\beta_c\) that is \(\alpha\le A_+(\beta)\); for \(\beta>\beta_c\) it is \(\alpha\le A_-(\beta)\); and for \(\beta=\beta_c\) it always holds with \(t=0\). Equality at either threshold is a **single orbit**, not two: it is the shared endpoint of (3) or (4) and (5). This exhausts all possibilities and gives the displayed census. At \(\ell_\beta=\pi/2\), (5) yields the parameter-independent orbit shown above.

**3. Sharp pole.** Since \(\ell_{\beta_c}=\pi/2\) and
\[
\ell_\beta=\frac\pi2+\frac{2}{\beta_c^2}(\beta-\beta_c)+O((\beta-\beta_c)^2),
\]
we have \(|\cos\ell_\beta|\sim2|\beta-\beta_c|/\beta_c^2\). Substitution into \(A_\pm\) yields the asserted coefficient \(\pi^2\beta_c^3/16\).

**4. Sharp smooth linear stability.** Away from \(y=0\),
\[
DF_{\alpha,\beta}(x,y)=
\begin{pmatrix}
-\alpha\sin x+\beta(|y|-1)&\beta x\operatorname{sgn}(y)\\
1&1
\end{pmatrix}.
\]
On the strictly positive-ordinate branch, write \(B=\beta u>0\), \(h=\beta u/2+\alpha\sin u>0\). The two successive Jacobians are
\[
J_1=\begin{pmatrix}-1-h&B\\1&1\end{pmatrix},\qquad
J_2=\begin{pmatrix}-1+h&-B\\1&1\end{pmatrix}.
\]
The characteristic polynomial of \(J_2J_1\) has value
\[
\det(I-J_2J_1)=-B(B+2h)<0.
\]
As it tends to positive infinity for large positive arguments, it has a real root strictly greater than one.

For the strict sign-crossing orbit, \(u=\ell_\beta\) and \(|t|<\ell_\beta/2\). Put \(B=\beta\ell_\beta=2(\beta-1)\) and \(h=\alpha S_\beta\), where \(S_\beta>0\) on \(0<\ell_\beta<2\) (the function \(\ell\sin\ell+\cos\ell\) is positive on that interval). The two Jacobians become
\[
J_1=\begin{pmatrix}-1-h&-B\\1&1\end{pmatrix},\qquad
J_2=\begin{pmatrix}-1+h&-B\\1&1\end{pmatrix},
\]
so the return matrix has
\[
T=\operatorname{tr}(J_2J_1)=2-2B-h^2,\qquad
D=\det(J_2J_1)=(B-1)^2-h^2.
\]
For a real quadratic \(z^2-Tz+D\), both roots are strictly inside the unit disk exactly when \(1-T+D>0\), \(1+T+D>0\), and \(1-D>0\). Here these are
\[
B^2>0,\qquad (2-B)^2-2h^2>0,\qquad B(2-B)+h^2>0.
\tag{6}
\]
For \(0<B<2\) they reduce to \(h^2<(2-B)^2/2\). For \(B=2\) the middle condition fails. For \(B>2\), the second and third would require simultaneously \(h^2<(B-2)^2/2\) and \(h^2>B(B-2)\), which is impossible. In the only possible sink regime \(1<\beta<2\), the strict crossing orbit exists for \(\alpha<A_+(\beta)\); inserting \(h=\alpha S_\beta\) into (6) gives the asserted necessary-and-sufficient criterion. At equality of the spectral inequality and inside the smooth crossing regime a multiplier is \(-1\); this says nothing by itself about nonlinear period-four bifurcation. At \(|t|=\ell_\beta/2\), one ordinate is zero and this Jacobian argument is deliberately not applied.

## Verification

A reproducible standalone program, `check_fpfm2.py`, evaluates every explicit branch at 75-decimal precision over eleven \(\beta\) values and several forcing magnitudes, including both exact itinerary-boundary parameters. It checks both map iterations, period-two nondegeneracy, orbit counts, the parameter-locked cycle, exact Jacobian identities and the Schur criterion. It reports **882 passed high-precision conditions** in the supplied version. This is a finite implementation check; the exhaustiveness and sharpness of the infinite claims are consequences of the symbolic branch argument above, not of numeric sampling.

## Relationship to prior work

Almatroud and Pham, *Building Fixed Point-Free Maps with Memristor*, *Mathematics* **11** (2023), 1319, Section 4, Equation (8), introduce precisely the \(|y|-1\) memory law, give a parameter example and an iterative attractor plot, but do not state a prime-two census, an all-forcing persistence transition, a locked orbit or a sharp sink boundary. Their Section 3 studies a **different** map using \(y^2-1\).

Ramadoss et al., *Constructing non-fixed-point maps with memristors*, *European Physical Journal Plus* **137** (2022), 211, study a related absolute-value memristance \(|y|-1\), but their NFP2 first coordinate adds a **constant nonzero bias** instead of the cosine forcing \(\alpha\cos x\); their claimed construction and numerical explorations do not provide this theorem for the present FPFM2. Additional published work on two-dimensional memristor cosine maps uses different couplings. An exact census for one map is not an automatic corollary of results for the others.

## Limitations

This classification concerns **only least-period-two orbits** of the full-plane FPFM2 family and their specified linear stability, not longer cycles, chaotic attractor basins, global attraction, nonlinear stability of an eigenvalue-modulus-one boundary, random-number-generation performance or physical realizability. Stability derivatives are not asserted at ordinates equal to zero. A complete search of unpublished or unindexed earlier calculations is impossible; publication priority remains subject to external scrutiny. No independent audit or external mathematical validation has been performed.

## References

1. O. A. Almatroud and V.-T. Pham, *Building Fixed Point-Free Maps with Memristor*, **Mathematics** 11 (2023), 1319, published 2023-03-09, DOI: 10.3390/math11061319, Section 4, Eq. (8). Open full-text URL: https://www.mdpi.com/2227-7390/11/6/1319 .
2. J. Ramadoss, A. Ouannas, V. K. Tamba, G. Grassi, S. Momani and V.-T. Pham, *Constructing non-fixed-point maps with memristors*, **European Physical Journal Plus** 137 (2022), 211, DOI: 10.1140/epjp/s13360-022-02433-z, especially Table 1 (NFP2). Open institutional-author PDF: https://eacademic.ju.edu.jo/S.Momani/Lists/Published%20Research/Attachments/421/PAPER_387.pdf .
3. *Dynamical Analysis of Two-Dimensional Memristor Cosine Map*, **Frontiers in Physics** (2022), DOI: 10.3389/fphy.2022.911144. Distinct cosine-memory coupling; https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2022.911144/full .
