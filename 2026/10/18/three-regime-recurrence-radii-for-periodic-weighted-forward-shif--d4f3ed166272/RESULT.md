# Three-regime recurrence radii for periodic weighted forward shifts and a nonconvex critical phase

## Finding
For a strictly positive \(q\)-periodic weight sequence \((w_j)_{j\ge0}\), let the unilateral weighted forward shift on complex \(\ell_2(\mathbb N_0)\) be \(W e_j=w_j e_{j+1}\). Put \(\gamma=(\prod_{j=0}^{q-1}w_j)^{1/q}\), and set \(c_0=1\), \(c_{j+1}=c_jw_j/\gamma\). Then \(c_{j+q}=c_j\), and the base-point syndetic recurrence radius defined below obeys the complete trichotomy
\[
\delta_*(x)=\begin{cases}
\|x\|_2,&0<\gamma<1,\\
\displaystyle\left(\|x\|_2^2+\min_{0\le r<q}\sum_{j\ge0}|x_j|^2(c_{j+r}/c_j)^2\right)^{1/2},&\gamma=1,\\
+\infty,&\gamma>1\text{ and }x\ne0,\\
0,&\gamma>1\text{ and }x=0.
\end{cases}
\]
At \(\gamma=1\), the recurrence class \(AP_\delta(W)=\{x:\delta_*(x)\le\delta\}\) is a finite union of closed centered Hilbert ellipsoids; it need not be convex, **even when \(W\) is similar to the unilateral isometry**. Explicitly, for \((w_{2j},w_{2j+1})=(1/2,2)\), the vectors
\[
A=\tfrac45 e_0+\tfrac15 e_1,\qquad B=\tfrac35 e_0+\tfrac{\sqrt{14}}{10}e_1
\]
belong to \(AP_1(W)\), but \((A+B)/2\) does not. Hence the recurrence radius of a power-bounded Hilbert-space operator need not be a seminorm.

## Assumptions and scope
Here \(q\ge1\) is a fixed integer, \(w_j>0\) for all indices, and \(w_{j+q}=w_j\). The underlying space is complex \(\ell_2(\mathbb N_0)\), and \(e_j\) are its standard basis vectors. A set \(R\subset\mathbb N\) is *syndetic* if some integer \(N\) exists such that every block of \(N\) consecutive positive integers meets \(R\). For \(\delta\ge0\), define
\[
AP_\delta(W)=\bigl\{x:\text{for every }\varepsilon>0,\ \{n\ge1:\|W^n x-x\|_2<\delta+\varepsilon\}\text{ is syndetic}\bigr\},
\qquad\delta_*(x)=\inf\{\delta\ge0:x\in AP_\delta(W)\}.
\]
The infinity convention applies to an empty infimum. Finite unions of ellipsoids above are exact sublevel descriptions: for each residue \(r\), the quadratic inequality \(\|x\|_2^2+\sum_j |x_j|^2(c_{j+r}/c_j)^2\le\delta^2\) specifies one ellipsoid (possibly an infinite-dimensional Hilbert ellipsoid). The value of \(\gamma\) depends only on the period product and not on the chosen period's origin.

## Proof
**1. Periodic similarity reduction.** Since \(\prod_{j=0}^{q-1}w_j=\gamma^q\), the positive sequence \((c_j)\) is \(q\)-periodic. Its minimum and maximum over one period are positive and finite. With \(D e_j=c_j e_j\) and \(Se_j=e_{j+1}\), both \(D\) and \(D^{-1}\) are bounded and
\[
W=\gamma DSD^{-1},\qquad W^n e_j=\gamma^n(c_{j+n}/c_j)e_{j+n}.
\]
Thus every \(x=(x_j)\in\ell_2\) satisfies the exact identity
\[
\|W^nx\|_2^2=\gamma^{2n}\sum_{j\ge0}|x_j|^2(c_{j+n}/c_j)^2.
\]
The ratios inside the sum are bounded above and below uniformly in both indices.

**2. Subcritical and supercritical regimes.** If \(\gamma<1\), the displayed identity gives \(\|W^n\|\le C\gamma^n\to0\). Consequently \(\|W^nx-x\|\to\|x\|\); all sufficiently large times return within every tolerance larger than \(\|x\|\), whereas at any smaller tolerance there are only finitely many return times. Therefore \(\delta_*(x)=\|x\|\). If \(\gamma>1\) and \(x\ne0\), the lower ratio bound gives \(\|W^nx\|\ge c\gamma^n\|x\|\to\infty\); then no finite tolerance admits infinitely many return times, hence \(\delta_*(x)=+\infty\). At \(x=0\), every iterate vanishes and the radius is zero.

**3. Critical regime.** Suppose \(\gamma=1\). Along indices \(n\equiv r\pmod q\), the squared orbit norm is the constant quadratic form
\[
Q_r(x)=\sum_{j\ge0}|x_j|^2(c_{j+r}/c_j)^2.
\]
Moreover \(W^nx=DS^nD^{-1}x\rightharpoonup0\): the unilateral isometry \(S^n\) converges weakly to zero and multiplication by fixed bounded operators preserves weak convergence. It follows along each residue class that
\[
\lim_{\substack{n\to\infty\\n\equiv r\ (\mathrm{mod}\ q)}}\|W^nx-x\|_2^2=\|x\|_2^2+Q_r(x).
\]
Let \(b(x)=\min_{0\le r<q}(\|x\|^2+Q_r(x))^{1/2}\). When \(\delta\ge b(x)\), choose a minimizing residue; for any \(\varepsilon>0\), every sufficiently large time in that residue satisfies \(\|W^nx-x\|<\delta+\varepsilon\). The tail of a residue class is syndetic, so \(x\in AP_\delta(W)\). When \(\delta<b(x)\), choose \(\varepsilon>0\) with \(\delta+\varepsilon<b(x)\); the preceding finitely many residue limits show that all sufficiently large \(n\) fail the return inequality. The return set is finite, hence not syndetic. This establishes the claimed equivalence and exact radius.

**4. Nonconvexity at criticality.** Set \(q=2\) with alternating weights \((1/2,2)\). Then \((c_0,c_1)=(1,1/2)\), and for \(x=xe_0+ye_1\) one obtains
\[
\delta_*(x)^2=\min\left\{2(|x|^2+|y|^2),\ \tfrac54|x|^2+5|y|^2\right\}.
\]
For \(A=(4/5,1/5)\), the second expression equals \(1\) and the first is \(34/25>1\). For \(B=(3/5,\sqrt{14}/10)\), the first expression equals \(1\), while the second equals \(23/20>1\). With \(M=(A+B)/2=(7/10,(2+\sqrt{14})/20)\), the two expressions are respectively
\[
\tfrac{107+2\sqrt{14}}{100}>1,\qquad\tfrac{67+4\sqrt{14}}{80}>1.
\]
Thus \(A,B\in AP_1(W)\) and \(M\notin AP_1(W)\). As \(W=DSD^{-1}\) with \(D=\mathrm{diag}(1,1/2,1,1/2,\ldots)\), this nonconvexity holds for an operator similar to an isometry and with \(\sup_n\|W^n\|\le2\). Scaling the witness produces a nonconvex \(AP_\delta(W)\) for every \(\delta>0\). A homogeneous seminorm has convex sublevel sets, so \(\delta_*\) is not a seminorm here.

## Verification
The standalone `verify.py` reproduces the exact rational–radical witness inequalities, validates the finite residue formula against direct shift iterates for several periodic weights and vectors, and checks the three growth regimes. These finite calculations are supplementary: the all-vector, all-period proof relies on the periodic similarity identity and weak convergence, not numerical testing.

## Relationship to prior work
Alshammari and Benchiheb (2026) introduce the base-point \(\delta\)-almost-periodic classes and recurrence radius, prove general lower semicontinuity under power-boundedness, and analyze vanishing orbits and some weighted **backward** shifts. Their vanishing-orbit theorem supplies the \(\gamma<1\) regime but not the \(\gamma=1\) minimum-over-phases formula or the convexity obstruction. The present result classifies all strictly positive periodic **forward** weights; its distinctive conclusion is the nonconvex critical phase despite similarity to an isometry. Standard weighted-shift similarity explains the periodic diagonal reduction but does not alone establish its implications for the recent base-point syndetic radius.

## Limitations
This theorem assumes strictly positive periodic weights on \(\ell_2\); it does not classify nonperiodic weight sequences, phase-varying complex weights or Banach \(\ell_p\) spaces. The explicit nonconvex example demonstrates failure in general, not a characterization of which critical periodic weights yield convex sublevels. Public priority is not independently certified; relevant earlier recurrence or weighted-shift results may contain related formulations. Finite checker output is not a proof of infinite-dimensional statements.

## References
1. H. O. Alshammari and O. Benchiheb, “δ-Almost Periodic Vectors for Bounded Linear Operators: Geometric and Dynamical Structure,” *Journal of Function Spaces* **2026**, Article 9920770, published May 12, 2026. DOI: 10.1155/jofs/9920770.
2. F. Bayart and É. Matheron, *Dynamics of Linear Operators*, Cambridge Tracts in Mathematics 179, Cambridge University Press, 2009. (General background on shifts and linear dynamics.)
