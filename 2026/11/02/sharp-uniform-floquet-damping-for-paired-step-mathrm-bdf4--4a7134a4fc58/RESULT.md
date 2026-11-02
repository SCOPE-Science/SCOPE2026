# Sharp uniform Floquet damping for paired-step \(\mathrm{BDF4}\)

## Finding

For every \(h>0\) and \(r>0\), apply the genuine variable-coefficient fourth-order backward differentiation formula (BDF4), obtained by differentiating the degree-four interpolant at the newest time node, to \(y'=0\) on the indefinitely repeated four-step mesh
\[
(h,rh,rh,h,h,rh,rh,h,\ldots).
\]
Let \(F_r\) be the four-step monodromy on the three independent backward differences (the constant solution is removed). Then the **sharp, ratio-independent Floquet estimate** is
\[
\rho(F_r)<\frac{1}{\sqrt{21}}\quad(r>0),\qquad
\sup_{r>0}\rho(F_r)=\frac{1}{\sqrt{21}}.
\]
In particular, each *fixed* paired-step periodic mesh is zero-stable even for arbitrarily large or small ratios, and every parasitic Floquet mode decays with modulus strictly below \(1/\sqrt{21}\) per four-step period. The supremum is approached only at singular ratio limits, \(r\to0\) or \(r\to\infty\), not attained at a positive finite ratio.

An exact cubic determines all three multipliers. Put \(t=r+r^{-1}\ge2\) and define
\[
\begin{aligned}
D(t)&=840t^4+8988t^3+35578t^2+61702t+39565,\\
A(t)&=112t^4+144t^3-2232t^2-6608t-4909,\\
B(t)&=40t^4+180t^3+210t^2+62t+95,\\
C(t)&=(2t+5)^2.
\end{aligned}
\]
The characteristic polynomial is exactly
\[
\boxed{\det(zI-F_r)=z^3-\frac{A(t)}{D(t)}z^2+\frac{B(t)}{D(t)}z-\frac{C(t)}{D(t)}.}
\]

## Assumptions and scope

The time steps are strictly positive, are taken in the displayed order, and repeat with period four; the overall scale \(h\) is arbitrary. The numerical scheme uses the genuine varying interpolation coefficients at each step (not frozen coefficients or a fixed-step BDF polynomial). Only the homogeneous test equation \(y'=0\), fixed periodic step ratios, the three parasitic differences, and their exact Floquet spectrum are addressed. A bound on Floquet eigenvalues does **not** assert a ratio-uniform bound on matrix norms, conditioning, forced-error response, arbitrary nonperiodic-grid stability, or stability for nonzero right-hand sides.

## Proof

Write \(h_n=t_n-t_{n-1}\), define \(d_0=0\) and \(d_j=\sum_{m=0}^{j-1}h_{n-m}\) for \(1\le j\le4\), and let \(\ell_j\) be the Lagrange cardinal polynomials for nodes \(-d_0,\ldots,-d_4\). The BDF4 equation on \(y'=0\) is \(\sum_{j=0}^4\alpha_j y_{n-j}=0\), with \(\alpha_j=\ell_j'(0)\). In particular, \(\alpha_0=\sum_{j=1}^4d_j^{-1}>0\), and \(\sum_{j=0}^4\alpha_j=0\).

Put \(e_n=y_n-y_{n-1}\). Eliminating the constant solution gives
\[
\alpha_0e_n=\sum_{j=1}^3\left(\sum_{i=j+1}^4\alpha_i\right)e_{n-j}.
\]
Thus \((e_n,e_{n-1},e_{n-2})^\mathsf T=T_n(e_{n-1},e_{n-2},e_{n-3})^\mathsf T\), where \(T_n\) is the three-by-three companion matrix with first row
\[
\left(\frac{\alpha_2+\alpha_3+\alpha_4}{\alpha_0},
\frac{\alpha_3+\alpha_4}{\alpha_0},
\frac{\alpha_4}{\alpha_0}\right)
\]
and subdiagonal ones. Multiply four such matrices for the periodic steps. Exact rational simplification gives the characteristic polynomial in the Finding. The polynomial depends on \(r\) only through \(t=r+r^{-1}\); the source reproducer checks this identity independently from the interpolation formula.

Let \(q=1/\sqrt{21}\). Scale \(z=q\zeta\). For the monic cubic \(\zeta^3+a\zeta^2+b\zeta+c\), the real Schur criterion is \(|c|<1\), \(1+a+b+c>0\), \(1-a+b-c>0\), and \(1-b+ac-c^2>0\). Here the four needed positive numerators, after multiplying by positive powers of \(D(t)\), are
\[
\begin{aligned}
P_1&=D-21\sqrt{21}\,C,\\
P_2&=D+21B-\sqrt{21}(A+21C),\\
P_3&=D+21B+\sqrt{21}(A+21C),\\
P_4&=D^2-21BD+441AC-9261C^2.
\end{aligned}
\]
All are **strictly positive** for \(t\ge2\). To make this an exact certificate, substitute \(u=t-2\ge0\). The coefficients of \(P_1\), in descending degree, are
\[
(840,15708,109666-84\sqrt{21},338750-756\sqrt{21},390625-1701\sqrt{21}).
\]
Those of \(P_2\) are
\[
(1680-112\sqrt{21},26208-1040\sqrt{21},156916-1404\sqrt{21},429932+9468\sqrt{21},456544+22408\sqrt{21}),
\]
and those of \(P_3\) are
\[
(1680+112\sqrt{21},26208+1040\sqrt{21},156916+1404\sqrt{21},429932-9468\sqrt{21},456544-22408\sqrt{21}).
\]
Every displayed coefficient is positive by \(4<\sqrt{21}<5\). Finally,
\[
\begin{split}
P_4=16(&273420t^7+4574262t^6+32337879t^5+125193286t^4\\
&+286533494t^3+387470109t^2+286403660t+89159200),
\end{split}
\]
which is positive for \(t\ge2\). The cubic Schur criterion therefore gives \(\rho(F_r)<q\) for every finite \(r>0\).

As \(r\to0\) or \(r\to\infty\), \(t\to\infty\) and the polynomial converges coefficientwise to
\[
z\left(z^2-\frac{2}{15}z+\frac{1}{21}\right).
\]
Its nonzero roots are a complex-conjugate pair of modulus exactly \(1/\sqrt{21}\); continuity of polynomial roots proves sharpness.

## Verification

Run `python VERIFY.py` with SymPy. It independently constructs the varying Lagrange coefficients, multiplies the four difference-state matrices, checks all three rational characteristic coefficients, verifies positivity of the four Schur numerators by exact coefficient inequalities, checks the singular limiting polynomial, and tests six rational step ratios. The exact positivity argument above, not the six finite samples, proves the all-ratio statement.

## Relationship to prior work

Classical variable-step BDF stability papers by Skeel–Jackson, Calvo–Lisbona–Montijano, Calvo–Grande–Grigorieff, and Grigorieff address general step variation and impose various ratio bounds. Wang–Ruuth derive variable-coefficient fourth-order formulas and report sufficient all-mesh restrictions, including an upper adjacent ratio bound of \(1.101\), rather than an exact sharp Floquet constant for this four-step paired block. That sufficient bound cannot cover the unbounded ratio family here. General periodic-matrix root tests are background tools, not the exact coefficient and positivity result claimed here. Completeness of historical specialist coverage is not established, since several earlier complete texts were inaccessible.

## Limitations

This is zero stability of the homogeneous fourth-order recurrence on the specified *fixed-periodic* meshes; it does not establish convergence on arbitrary varying grids or large-step stability for differential equations with nonzero right-hand side. The sharp constant is a spectral-radius bound per completed four-step period, not a uniform bound on \(\|F_r^k\|\) over simultaneous variation of \(r\) and \(k\). The scientific priority assessment is limited by the inaccessible complete texts of several historical BDF papers.

## References

- M. Calvo, T. Grande, R. D. Grigorieff, *On the zero stability of the variable order variable stepsize BDF-Formulas*, Numerische Mathematik 57 (1990), 39–50, DOI: 10.1007/BF01386395. Public author upload dated 2015-01-30.
- M. Calvo, F. Lisbona, J. Montijano, *On the Stability of Variable-Stepsize Nordsieck BDF Methods*, SIAM J. Numer. Anal. 24 (1987), 844–854, DOI: 10.1137/0724054. Online date 2006-07-14.
- D. Wang, S. J. Ruuth, *Variable Step-Size Implicit-Explicit Linear Multistep Methods for Time-Dependent Partial Differential Equations*, J. Comput. Math. 26 (2008), 838–855. https://global-sci.com/index.php/JCM/article/download/11917/23756/24986
- R. D. Skeel, L. W. Jackson, *The Stability of Variable-Stepsize Nordsieck Methods*, SIAM J. Numer. Anal. 20 (1983), 840–853, DOI: 10.1137/0720056.
- N. Guglielmi, M. Zennaro, *On the zero-stability of variable stepsize multistep methods: the spectral radius approach*, Numerische Mathematik 88 (2001), 445–458, DOI: 10.1007/s211-001-8010-0.
