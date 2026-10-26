# Reentrant Galerkin heat-kernel signs on periodic one-dimensional meshes

## Finding
For the continuous-time, **consistent-mass** linear finite-element semidiscretization of unit-diffusivity heat flow on a uniform periodic one-dimensional mesh with \(n\ge6\) cells of length \(\ell>0\), let \(P_n(t)=\exp(-tM_n^{-1}K_n)\). For any node \(i\), the transition coefficient to node \(i+3\) (indices modulo \(n\)) has the **reentrant sign pattern**
\[
(P_n(t))_{i,i+3}>0\quad\text{for all sufficiently small }t>0,
\qquad (P_n(\ell^2/3))_{i,i+3}<-0.0069,
\qquad (P_n(t))_{i,i+3}>0\quad\text{for all sufficiently large }t.
\]
Thus one positive entry becomes negative at an intermediate time before becoming positive again, for **every** finite mesh size \(n\ge6\). No entry has such a positive-to-negative-to-positive evolution on the corresponding meshes with \(n=3,4,5\); six is the least possible mesh size.

The six-cell case also has an exact complete positivity-time classification. Let \(\alpha\) be the unique root of
\[
H(x)=x^8+x^6+x^4-2x^3+x^2-2x+1=0
\]
in \((1/2,3/5)\). Then
\[
P_6(t)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad
 t=0\ \text{ or }\ t\ge-\frac{5\ell^2}{6}\log\alpha.
\]
Numerically the positive threshold is \(0.5007038252835888\ldots\ell^2\). The distance-three entry on this six-node mesh has exactly two positive-time zeros, approximately \(0.125202111021650\ell^2\) and \(0.500703825283589\ell^2\).

## Assumptions and scope
The physical domain is a circle of circumference \(n\ell\), partitioned into \(n\ge3\) equal intervals, with periodic continuous piecewise-affine nodal functions, diffusion coefficient one, and no mass lumping. The nodal mass and stiffness matrices are
\[
 M_n=\frac{\ell}{6}(4I+A_n),\qquad K_n=\frac1\ell(2I-A_n),
\]
where \(A_n\) is adjacency of the simple \(n\)-cycle; this convention is valid also for \(n=3\). The matrix \(P_n(t)\) maps initial nodal values to values at time \(t\). Its entries are real, symmetric, and row-sum one, but not necessarily nonnegative. Write \(s=t/\ell^2\) and \(p_{n,j}(s)=(P_n(s\ell^2))_{0,j}\). By translation symmetry, the entry depends only on cyclic displacement \(j\).

The result does not concern fully discrete backward-Euler or Runge–Kutta updates, Dirichlet boundaries, nonuniform meshes, or nonconstant diffusivity.

## Proof
**1. Spectrum and the small-time sign.** Put
\[
Q_n=-\ell^2M_n^{-1}K_n=6I-36(4I+A_n)^{-1};\qquad P_n(s\ell^2)=e^{sQ_n}.
\]
The real eigenvalues of \(Q_n\) are
\[
-6\frac{1-\cos(2\pi k/n)}{2+\cos(2\pi k/n)},\qquad 0\le k<n,
\]
and lie in \([-12,0]\). Define \(r=2-\sqrt3\in(0,1)\). The infinite-line inverse of \(4I+A\) has coefficients \((-r)^{|j|}/(2\sqrt3)\), as checked by its three-term recurrence and the equation at the origin. Periodization gives, for \(1\le j<n\),
\[
((4I+A_n)^{-1})_{0,j}
=\frac{(-r)^j+(-r)^{n-j}}{2\sqrt3\,[1-(-r)^n]}.
\]
At displacement three this expression is strictly negative for every \(n\ge6\): for even \(n\) both numerator terms are negative; for odd \(n\ge7\) its numerator is \(-r^3+r^{n-3}<0\). Therefore \((Q_n)_{0,3}>0\). The analytic expansion \(p_{n,3}(s)=s(Q_n)_{0,3}+O(s^2)\) proves strict positivity for all sufficiently small positive \(s\). Every positive-time kernel tends to \(J/n\), since zero is a simple eigenvalue and all other eigenvalues of \(Q_n\) are negative. This proves strict eventual positivity.

**2. A uniform negative witness at the fixed time \(s=1/3\).** This step is an infinite-family proof combining finite exact arithmetic with an analytic tail bound. Let \(T_{21}(z)=\sum_{k=0}^{21}z^k/k!\). The real spectral interval \(\sigma(Q_n/3)\subset[-4,0]\), Taylor's theorem, and the spectral theorem give the entrywise error bound
\[
\left|\left(e^{Q_n/3}-T_{21}(Q_n/3)\right)_{0,3}\right|
\le \frac{4^{22}}{22!}<1.566\cdot10^{-8}.
\]
The accompanying self-contained exact-rational code `verify_semigroup.py` computes \((T_{21}(Q_n/3))_{0,3}\) for **every integer** \(6\le n\le50\), verifying strictly \(<-7/1000\) in all 45 cases and \(<-73/10000\) at \(n=50\). The inverse matrices are obtained by an integer recurrence and an exact two-by-two solve; all subsequent computations use rational convolutions. The finite checker by itself is **not** asserted to prove the case \(n>50\).

For the infinite lattice, introduce the analytic Laurent symbol
\[
F(z)=\exp\!\left(\frac{1}{3}\left[6-\frac{36}{4+z+z^{-1}}\right]\right),
\qquad 2-\sqrt3<|z|<2+\sqrt3.
\]
Write its Laurent coefficients as \(c_j\). On either circle \(|z|=2\) or \(|z|=1/2\), \(|4+z+z^{-1}|\ge3/2\), hence \(|F(z)|\le e^{10}<3^{10}\). Cauchy's coefficient estimates therefore imply \(|c_j|\le3^{10}2^{-|j|}\). Discrete Fourier sampling and absolute convergence give the exact periodization identity
\[
p_{n,3}(1/3)=\sum_{m\in\mathbb Z}c_{3+mn}.
\]
Consequently, for all \(n\ge50\),
\[
|p_{n,3}(1/3)-c_3|
\le\frac{3^{10}(8+1/8)}{2^n-1}
\le\frac{3^{10}(8+1/8)}{2^{50}-1}<4.262\cdot10^{-10}.
\]
Comparison of any \(n\ge51\) with the already exact-rational checked \(n=50\) gives an error \(<2\cdot4.262\cdot10^{-10}\), on top of the Taylor remainder. The \(-73/10000\) witness at \(n=50\) therefore implies \(p_{n,3}(1/3)<-7/1000\) for every \(n\ge51\). Combining with the 45 finite cases yields the advertised uniform \(-0.0069\) bound for every \(n\ge6\).

**3. Exact positivity horizon for six nodes.** For \(n=6\), the distinct dimensionless nonzero eigenvalues of \(-Q_6\) are \(6/5,6,12\). Write \(x=e^{-6s/5}\in(0,1)\). Discrete Fourier inversion gives, for distances one, two, and three,
\[
\begin{aligned}
6p_{6,1}(s)&=1+x-x^5-x^{10},\\
6p_{6,2}(s)&=1-x-x^5+x^{10},\\
6p_{6,3}(s)&=1-2x+2x^5-x^{10}=(1-x^2)H(x).
\end{aligned}
\]
The diagonal entry is positive at every time by the spectral representation. The distance-one entry is positive at every \(s>0\) since its numerator equals \((1-x^5)+x(1-x^9)\).

The distance-two numerator factors as \((x-1)(x^9+x^8+x^7+x^6+x^5-1)\). The factor in parentheses is strictly increasing and has exactly one root \(\gamma\in(3/4,4/5)\), so the distance-two entry becomes nonnegative precisely for \(x\le\gamma\). The polynomial \(H\) has **exactly two** roots in \((0,1)\): indeed, under \(x=y/(1+y)\),
\[
(1+y)^8H\!\left(\frac{y}{1+y}\right)
=y^8-4y^7-12y^6-10y^5+6y^4+18y^3+15y^2+6y+1,
\]
whose coefficient sequence has exactly two sign changes, so Descartes' rule bounds its positive roots by two. The values \(H(1/2)>0\), \(H(3/5)<0\), \(H(4/5)<0\), and \(H(9/10)>0\) supply two distinct roots \(\alpha\in(1/2,3/5)\) and \(\beta\in(4/5,9/10)\). Therefore \(p_{6,3}\) is positive for \(x\in(\beta,1)\), negative for \(x\in(\alpha,\beta)\), and positive for \(x\in(0,\alpha)\). Since \(\alpha<\gamma<\beta\), the matrix is entrywise nonnegative at positive time precisely when \(x\le\alpha\), giving the claimed threshold. At \(s=0\) it equals the identity.

**4. Minimality of six nodes.** At \(n=3\) the sole off-diagonal entry is \((1-e^{-6s})/3>0\). At \(n=4\), distance one has kernel \((1-e^{-12s})/4>0\), while distance two has kernel \((1-2y+y^4)/4\) with \(y=e^{-3s}\); the factorization \((y-1)(y^3+y^2+y-1)\) shows exactly one positive-time zero, crossing from negative to positive. At \(n=5\), put \(\varphi=(1+\sqrt5)/2\), \(a=(60-18\sqrt5)/11\), \(b=(60+18\sqrt5)/11\), and \(u=e^{-as}\), \(\kappa=b/a>\varphi^2\). The distance-one kernel is \([1+\varphi^{-1}u-\varphi u^\kappa]/5>0\). The distance-two kernel is \([1-\varphi u+\varphi^{-1}u^\kappa]/5\); its bracket is strictly convex in \(u\in(0,1)\), equals one at \(u=0\), equals zero at \(u=1\), and has strictly positive derivative at \(u=1\). Hence it has one other zero and crosses just once as \(s\) increases. None of these smaller meshes has an initially positive entry that later turns negative.

## Verification
Run `python3 verify_semigroup.py` using only Python's standard library. The script checks the exact cyclic inverse recurrence; evaluates the degree-21 exponential Taylor coefficient in exact rational arithmetic for all \(6\le n\le50\); verifies the two independent rational margins; checks the transformed root-count polynomial and bracket signs; and checks exact rational inequalities for the Taylor remainder and Cauchy alias bound. Its finite loop is combined with the **proved analytic bound** to cover all larger \(n\); no inference from numerical experiments to arbitrary mesh sizes is made. Approximate roots and times are only supplementary decimal representations of uniquely specified algebraic roots.

## Relationship to prior work
The classical finite-element positivity literature establishes failure of semidiscrete standard-Galerkin positivity at small times and discusses eventual positivity. Jin, Lazarov, Thomée and Zhou (2015, especially Theorems 3.1–3.2) provide such context while studying subdiffusion. The present statement identifies the **same individual matrix entry** as initially positive, then negative at a universal dimensionless time, then eventually positive for **all periodic lengths**; it also gives a six-node exact operator horizon and proves the minimal mesh size for this entrywise sign reentrance. Those conclusions are not consequences of a generic small-time failure or eventual-positivity theorem. The 2010 work on fully discrete \(\theta\)-methods studies a different propagation operator. A published note on the spectral-cardinality threshold for **operator positivity-time sets** analyzes a different property, and a note on backward-Euler-filtered Crank–Nicolson treats a lumped-mass lattice and a composition of rational stepping maps; neither implies an entrywise sign reversal for the consistent-mass exponential semigroup. Comparison with an exact 2015 heat-equation paper was limited by access to its full text, so unrecognized stronger coverage remains a residual risk.

## Limitations
The all-size theorem guarantees **at least** two positive-time zeros of one matrix entry when \(n\ge7\), not uniqueness of those zeros or a closed positivity threshold for arbitrary \(n\). The complete threshold and exact two-root count are established only for \(n=6\). The certificate uses a finite exact-rational computation whose full range and analytic completion are specified, not an external formal proof. No independent scientific validation is claimed. Full-text priority comparison against Chatzipantelidis, Horváth and Thomée (2015) remains incomplete because the author-hosted PDF was inaccessible during this investigation.

## References
1. B. Jin, R. Lazarov, V. Thomée, Z. Zhou, *On Nonnegativity Preservation in Finite Element Methods for Subdiffusion Equations*, first posted 2015-10-09, arXiv:1510.02825, https://arxiv.org/abs/1510.02825 .
2. P. Chatzipantelidis, Z. Horváth, V. Thomée, *On Preservation of Positivity in Some Finite Element Methods for the Heat Equation*, Computational Methods in Applied Mathematics 15 (2015), 417–437, https://doi.org/10.1515/cmam-2015-0018 .
3. V. Thomée, L. B. Wahlbin, *On the Existence of Maximum Principles in Parabolic Finite Element Equations*, Mathematics of Computation 77 (2008), 11–19, https://doi.org/10.1090/S0025-5718-07-02021-2 .
4. A. H. Schatz, V. Thomée, L. B. Wahlbin, *On Positivity and Maximum-Norm Contractivity in Time Stepping Methods for Parabolic Equations*, Computational Methods in Applied Mathematics 10 (2010), 421–443, https://doi.org/10.2478/cmam-2010-0025 .
