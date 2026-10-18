# Sharp angular zero-inclusion thresholds and inversion asymmetry on complex \(\ell_p^2\)

## Finding
For every \(1<p<\infty\), put \(\alpha=(p-1)/p\). Let the invertible upper-triangular matrix
\[
T=\begin{pmatrix}a&b\\0&d\end{pmatrix},\qquad a,d\in\mathbb C\setminus\{0\},\quad b\in\mathbb C,
\]
act on complex \(\ell_p^2\). Its spatial numerical range is \(W_p(T)=\{J_p(x)(Tx):\|x\|_p=1\}\), where \(J_p(x)(y)=\sum_{j=1}^2|x_j|^{p-2}\overline{x_j}y_j\) for unit \(x\); the convention at a zero coordinate is zero.

Write \(A=|a|\), \(D=|d|\), and
\[
c=\frac{\operatorname{Re}(a\overline d)}{AD}\in[-1,1],\quad
z_p(c)=\frac{(p-2)c+\sqrt{(p-2)^2c^2+4(p-1)}}2,
\]
\[
h_p(c)=\frac{\sqrt{z_p(c)^2+2cz_p(c)+1}}{z_p(c)^\alpha},\qquad
B_p(a,d)=A^\alpha D^{1-\alpha}h_p(c).
\]
Here \(h_p(-1)=0\), and the formula extends continuously to both endpoints.

**Exact simultaneous-zero classification:**
\[
\boxed{0\in W_p(T)\quad\Longleftrightarrow\quad |b|\ge B_p(a,d),}
\]
\[
\boxed{0\in W_p(T^{-1})\quad\Longleftrightarrow\quad |b|\ge B_p(d,a).}
\]
If \(c>-1\), the two strictly positive critical off-diagonal magnitudes satisfy the **angle-independent inversion law**
\[
\boxed{\frac{B_p(a,d)}{B_p(d,a)}=\left(\frac AD\right)^{(p-2)/p}.}
\]
Consequently, zero belongs to exactly one of the two ranges if and only if \(p\ne2\), \(A\ne D\), \(c>-1\), and
\[
\min\{B_p(a,d),B_p(d,a)\}\le |b|<\max\{B_p(a,d),B_p(d,a)\}.
\]
At \(c=-1\), both critical magnitudes vanish and zero belongs to both ranges for every \(b\). For fixed \(p,A,D\), the common angular factor \(h_p(c)\) is strictly increasing from zero at \(c=-1\) to \(p/(p-1)^\alpha\) at \(c=1\); thus the width of the one-sided inclusion interval is strictly increasing with the relative diagonal-phase cosine whenever \(p\ne2\) and \(A\ne D\).

**Two-dimensional dichotomy:** The complex space \(\ell_p^2\) has the simultaneous zero inclusion property for *all* invertible operators if and only if \(p=2\). For each \(p\ne2\), an explicit counterexample is
\[
T_p=\begin{pmatrix}1&2h_p(0)\\0&4i\end{pmatrix},\qquad h_p(0)=\frac{\sqrt p}{(p-1)^{(p-1)/(2p)}}.
\]
Exactly one of \(W_p(T_p)\) and \(W_p(T_p^{-1})\) contains zero. At \(p=4\), the especially simple matrix \(T=\begin{psmallmatrix}1&2\\0&4i\end{psmallmatrix}\) satisfies \(0\in W_4(T)\) but \(0\notin W_4(T^{-1})\), with the first inclusion witnessed by \(x=5^{-1/4}(\sqrt2,-(1+i)/\sqrt2)\).

## Assumptions and scope
All scalar spaces and matrices are complex; \(1<p<\infty\), and \(a,d\ne0\). The operators act on the canonical coordinate norm \(\ell_p^2\), not on arbitrary equivalent norms. The equalities concern **membership of zero in spatial numerical ranges**, not convex hulls or numerical radii, and include threshold equality. No classification of general nontriangular matrices is claimed.

## Proof
For unit \(x=(u,v)\) with both coordinates nonzero, let \(r=|u|/|v|>0\) and \(\phi=\arg(v)-\arg(u)\). Directly from the unique norming functional,
\[
J_p(x)(Tx)=\frac{ar^p+d+br^{p-1}e^{i\phi}}{1+r^p}.
\]
If one coordinate vanishes, the pairing is respectively \(a\) or \(d\), hence is nonzero. For \(b\ne0\), cancellation is possible for some \(r,\phi\) precisely when
\[
|b|=F_p(r):=\frac{|ar^p+d|}{r^{p-1}}.
\]
The continuous nonnegative function \(F_p\) diverges as \(r\downarrow0\) and as \(r\uparrow\infty\); therefore its image is exactly \([\min F_p,\infty)\). The same statement remains valid for \(b=0\): the minimum is zero exactly when \(a/d\) is negative real, in which case the diagonal terms can cancel.

Set \(s=r^p\), so \(F_p(r)=|as+d|/s^\alpha\). Substitute \(s=(D/A)z\). Then
\[
F_p(r)^2=A^{2\alpha}D^{2(1-\alpha)}\frac{z^2+2cz+1}{z^{2\alpha}}.
\]
The derivative of the last positive function has the sign of
\[
z^2-(p-2)cz-(p-1).
\]
This quadratic is negative at zero, has positive leading coefficient and a single positive root \(z_p(c)\), giving the **global** and unique minimizer \(z=z_p(c)\). In particular \(\min F_p=B_p(a,d)\), yielding the first boxed criterion, including equality and antipodal diagonals.

The inverse is
\[
T^{-1}=\begin{pmatrix}1/a&-b/(ad)\\0&1/d\end{pmatrix}.
\]
Its diagonal cosine is again \(c\); the first criterion applied to the inverse reads
\[
\frac{|b|}{AD}\ge A^{-\alpha}D^{-(1-\alpha)}h_p(c),
\]
which is equivalent to \(|b|\ge D^\alpha A^{1-\alpha}h_p(c)=B_p(d,a)\). For \(c>-1\), \(h_p(c)>0\), so division gives the angle-independent ratio. For \(c=-1\), the two minima are zero and both include zero. For \(c>-1\), the thresholds coincide exactly when \(p=2\) or \(A=D\); otherwise the one-sided interval includes its smaller endpoint and excludes the larger endpoint, since each individual zero criterion is non-strict.

To prove the angular assertion, for fixed \(z>0\) the expression \((z^2+2cz+1)/z^{2\alpha}\) is strictly increasing in \(c\). More precisely, at its unique minimizer the envelope derivative equals \(2z_p(c)^{1-2\alpha}>0\) whenever \(-1<c<1\). The endpoint calculations are \(z_p(-1)=1\) and \(z_p(1)=p-1\), giving \(h_p(-1)=0\) and \(h_p(1)=p/(p-1)^\alpha\). Continuity completes strict monotonicity on \([-1,1]\).

For \(p\ne2\), set \(a=1,d=4i\), so \(c=0\). The two thresholds are \(4^{1/p}h_p(0)\) and \(4^{(p-1)/p}h_p(0)\), which are distinct; their geometric mean equals \(2h_p(0)\). This proves that \(T_p\) has zero in exactly one of the ranges. Conversely \(\ell_2^2\) is Hilbert: if \(T\) is invertible and \(\langle Tx,x\rangle=0\), set \(y=Tx/\|Tx\|\); then \(\langle T^{-1}y,y\rangle=0\), and the same argument interchanging \(T,T^{-1}\) gives the equivalence for all invertible operators.

Finally, for \(p=4\), \(a=1,d=4i,b=2\), with \(x=5^{-1/4}(\sqrt2,-(1+i)/\sqrt2)\), the unnormalized numerator is \(4+4i-4(1+i)=0\). Moreover \(h_4(0)=2/3^{3/8}\), hence \(B_4(1,4i)=2\sqrt2/3^{3/8}<2<B_4(4i,1)=4\sqrt2/3^{3/8}\), proving the claimed strict reverse noninclusion.

## Verification
The entire classification is established by an exact cancellation reduction, a uniquely minimizing positive quadratic root, and explicit inversion. The formula includes all phase and boundary cases. The separate standalone Python checker `angular_zero_check.py` independently calculates the scalar minimum by numerical minimization across a parameter grid, checks the inversion ratio and angular monotonicity, and checks the explicit complex witness. It is a finite diagnostic, not a substitute for the proof. The displayed \(p=4\) witness is also verified symbolically in the proof.

## Relationship to prior work
Bračič and Diogo introduced the simultaneous zero inclusion property and established an explicit triangular membership criterion on \(\ell_1^2\) (their Proposition 3.5), along with finite-dimensional examples and operator classes. The present classification concerns the smooth, complex \(\ell_p^2\) scale \(1<p<\infty\) and distinguishes the diagonal-phase dependence and the inverse threshold asymmetry; it does not reassert their \(\ell_1\) theorem.

Ghosh's October 2026 work connects the simultaneous zero inclusion property with Birkhoff–James orthogonality symmetry and characterizes smooth almost locally uniformly rotund Hilbert spaces of dimension at least three. The explicit two-dimensional classification here is not an immediate application of that dimensional result. Its full proof was not accessible during the comparison, so a more general unrecognized implication remains a priority risk.

The published planar triangular-shear numerical-abscissa result gives the real aligned-diagonal positive threshold \(p A^\alpha D^{1-\alpha}/(p-1)^\alpha\), agreeing with the \(c=1\) slice of the present threshold. This real slice is **not** presented as novel here. That work treats dissipativity for negative real diagonals, rather than the full complex-angle law, the inverse comparison, and the exact two-dimensional simultaneous-zero dichotomy.

## Limitations
The proof gives zero membership, not the full shape of \(W_p(T)\); for complex Banach spaces this numerical range need not be convex. The angle-independent ratio applies only where \(c>-1\), because both thresholds are zero at antipodal diagonal phases. The result is restricted to triangular operators for the quantitative formulas and to canonical \(\ell_p^2\) for the global dichotomy. Publication-priority risk remains from possible older equivalent formulas in spatial numerical-range or complex dissipativity literature and from incomplete access to the full 2026 motivating preprint. No independent external audit has been performed.

## References
1. Souvik Ghosh, *On the simultaneous zero inclusion property and characterization of Inner product space*, arXiv:2610.13378v1, first submitted October 9, 2026; https://arxiv.org/abs/2610.13378.
2. Janko Bračič and Cristina Diogo, *Simultaneous zero inclusion property for spatial numerical ranges*, Journal of Mathematical Analysis and Applications 449 (2017), 1413–1423, https://doi.org/10.1016/j.jmaa.2017.01.001.
3. *Exact \(L^p\) contractivity phase diagram for planar triangular shears*, public mathematical note, October 11, 2026; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-l-p-contractivity-phase-diagram-for-planar-triangular-shea--6e17594aec7a.
