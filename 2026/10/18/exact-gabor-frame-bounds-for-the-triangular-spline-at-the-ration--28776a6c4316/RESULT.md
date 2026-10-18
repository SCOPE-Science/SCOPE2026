# Exact Gabor frame bounds for the triangular spline at the rational near-critical sequence

## Finding
Let \(g(x)=(1-|x|)_+\) be the unit-height triangular (second-order cardinal B-spline) window. For each integer \(m\ge2\), put \(a=1\) and \(b=m/(m+1)\). The optimal lower and upper Gabor frame bounds on \(L^2(\mathbb R)\) are, respectively,
\[
\boxed{A_m=\frac{2(m^2-1)}{m^3},\qquad B_m=\frac{m+1}{m}.}
\]
In particular, the sharp spectral condition number is
\[
\boxed{\frac{B_m}{A_m}=\frac{m^2}{2(m-1)}}
\]
and the sharp near-critical law is \(A_m/(1-b)\to2\) as \(m\to\infty\). The formulas hold simultaneously for **every** integer \(m\ge2\), with no numerical extrapolation.

## Assumptions and scope
The Gabor system is \(\{e^{2\pi i kbx}g(x-n):k,n\in\mathbb Z\}\), with unnormalized unit-height window \(g\). Bounds mean the largest possible \(A_m\) and smallest possible \(B_m\) such that
\[
A_m\|f\|_2^2\le\sum_{n,k\in\mathbb Z}|\langle f,e^{2\pi ikb\cdot}g(\cdot-n)\rangle|^2\le B_m\|f\|_2^2
\]
for every \(f\in L^2(\mathbb R)\). We use the convention \((t)_+=\max\{t,0\}\); expressions for a.e. \(x\) suffice for the frame operator. No simultaneous change of the translation parameter is allowed.

## Proof
**1. Exact Walnut matrix and finite chains.** Let \(h=1/m\), \(L=1/b=1+h\). The compact support of the tent permits the standard Walnut identity
\[
(Sf)(x)=\frac1b\sum_{\ell\in\mathbb Z}C_\ell(x)f(x-\ell L),\qquad
C_\ell(x)=\sum_{n\in\mathbb Z}g(x-n)g(x-n-\ell L).
\]
It follows directly from the absolutely finite contributions after Poisson summation in modulation, first for compactly supported test functions and then by bounded extension. Since \(2L>2\), terms with \(|\ell|\ge2\) vanish. If \(u=\{x\}\in[0,1)\),
\[
 C_0(x)=(1-u)^2+u^2=:D(u),\quad C_1(x)=(1-u)(u-h)_+=:E(u),\quad C_{-1}(x)=C_1(x+L).
\]
For each \(\tau\in[0,1)\), \(n\in\mathbb Z\), define \(x_j=(\tau/m)+n+jL\) for \(j=0,\ldots,m-1\) and \(u_j=(j+\tau)/m\). These points, indexed by \((n,\tau,j)\), parameterize the real line without overlap apart from null boundaries. The shifts by \(L\) connect only successive \(j\)'s: the left edge vanishes because \(E(u_0)=0\), while the right edge vanishes because \(E(u_m)=E(u_0)=0\) after periodic reduction. Thus \(S\) is a direct integral of identical finite chains, each scaled by \(1/b\). The real symmetric \(m\times m\) fiber matrix \(M_m(\tau)\) is tridiagonal with entries
\[
 D_j=\frac{(m-j-\tau)^2+(j+\tau)^2}{m^2},\qquad
 e_j=\frac{(j+\tau-1)(m-j-\tau)}{m^2}\quad(1\le j\le m-1),
\]
where \(e_j\) connects sites \(j-1\) and \(j\). Hence the frame bounds equal \(b^{-1}\) times the essential infimum of the smallest eigenvalue and essential supremum of the largest eigenvalue of \(M_m(\tau)\).

**2. Sharp upper bound.** All entries of \(M_m(\tau)\) are nonnegative. For interior rows, the exact identity
\[
D(u)+E(u)+E(u+h)=1-h
\]
holds whenever \(h\le u\le1-h\). The first row has sum \(D(u_0)+E(u_0+h)=1-u_0+u_0^2-hu_0\le1\); the last row has sum at most \(1\). Therefore \(\|M_m(\tau)\|_{\ell^2\to\ell^2}\le1\) by the symmetric nonnegative row-sum bound. At \(\tau=0\), the first site is isolated, with \(D_0=1\) and \(e_1=0\). By eigenvalue continuity, the essential supremum over \(\tau\in[0,1)\) is exactly \(1\). Thus \(B_m=1/b\).

**3. Uniform sharp lower bound by a positive ground state.** Let \(J_m(\tau)\) be obtained from \(M_m(\tau)\) by conjugation with \(\operatorname{diag}(1,-1,1,-1,\ldots)\). Its diagonal remains \(D_j\), and its off-diagonals are \(-e_j\). Set \(\mu_m=2(m-1)/m^2\). For \(0<\tau<1\) take the strictly positive vector normalized by \(v_0=1\) and
\[
\frac{v_{j+1}}{v_j}=\frac{m-j-\tau-1}{j+\tau}\quad(0\le j<m-1).
\]
These are gamma-binomial weights up to normalization; denominators and numerators are strictly positive in the specified range. Direct substitution using the displayed rational formulas yields
\[
(J_m(\tau)-\mu_mI)v
=\frac1{m^2}\big((1-\tau)^2v_0,0,\ldots,0,\tau^2v_{m-1}\big)^T.
\]
For completeness, the interior cancellation follows algebraically from
\[
 D_j-\mu_m-e_j\frac{j-1+\tau}{m-j-\tau}-e_{j+1}\frac{m-j-\tau-1}{j+\tau}=0
\]
for \(1\le j\le m-2\), with the two stated endpoint remainders. The ground-state transform now gives the exact quadratic-form decomposition, for every \(y\in\mathbb C^m\),
\[
\begin{split}
\langle y,(J_m(\tau)-\mu_mI)y\rangle={}&
\sum_{j=1}^{m-1}e_jv_{j-1}v_j\left|\frac{y_j}{v_j}-\frac{y_{j-1}}{v_{j-1}}\right|^2\\
&+\frac{(1-\tau)^2}{m^2}|y_0|^2+\frac{\tau^2}{m^2}|y_{m-1}|^2\ge0.
\end{split}
\]
Since \(J_m(\tau)\) is unitarily conjugate to \(M_m(\tau)\), every fiber eigenvalue is at least \(\mu_m\). The strict positive endpoint terms also show strict inequality for interior phases.

**4. Attainment as a spectral edge.** At \(\tau=0\), take \(v_0=0\) and \(v_j=\binom{m-2}{j-1}\) for \(1\le j\le m-1\). Direct substitution gives \(J_m(0)v=\mu_mv\), including \(m=2\). Continuity of the finite matrices shows the essential infimum of their smallest eigenvalues is exactly \(\mu_m\), so \(A_m=\mu_m/b=2(m^2-1)/m^3\). Dividing the two sharp bounds proves the claimed condition number; \(1-b=1/(m+1)\) gives \(A_m/(1-b)=2(m+1)^2(m-1)/m^3\to2\). Because the edge fibers occur only at a phase-null set, optimal constants are not claimed to be attained by an individual nonzero signal in \(L^2\).

## Verification
Run `python3 verify_frame_bounds.py` using the standalone script supplied alongside this note. With exact `fractions.Fraction` arithmetic, the program checks the direct Walnut coefficients, the gamma-binomial ratio identities and endpoint eigenvectors, positive-definite LDL pivots, and row-sum bounds for all integers \(2\le m\le28\) at five interior rational phases per \(m\); the output is in `verify_frame_bounds_output.txt`. The reported 1,091 finite checks are supplementary; the proof above establishes every integer \(m\ge2\) algebraically, not by enumeration.

## Relationship to prior work
Atindehou, Frederick, Kouagou, and Okoudjou (arXiv:1806.05614, first submitted June 14, 2018) establish broad qualitative frame regions for the second-order B-spline, including the parameters \(a=1\) and \(b<1\), but do not compute the exact optimal frame bounds along the present increasing-denominator sequence. Kloos and Stöckler (arXiv:1311.7359, section 5 and Remark 5.4) prove analytic lower estimates for symmetric exponential splines, including the ordinary triangular spline as a limiting case, and discuss linear approach to critical density; those displayed estimates are not the exact present spectral edge. Ghosh and Selvan (arXiv:2310.01141) settle distinct non-frame obstructions, not sharp frame bounds for this family. Buck, Frederick, Okoudjou, and Stangl (arXiv:2603.16986, sections 4–5) analyze spectra of truncated Gabor Gram blocks and estimate finite-section bounds; their results do not imply the exact positive infinite-frame bounds displayed here. Janssen (1996) develops Zak/Gram representations and calculations, without the present family formula. Two other related published analyses give exact frame bounds for the tent on different integer-oversampling curves (fixed density \(1/2\) and \(1/q\) near modulation spacing above \(2\)); neither covers \(a=1\), \(b=m/(m+1)\). The novelty assessed here is the simultaneous exact lower and upper sharp constants, not merely frame membership or qualitative linear decay.

## Limitations
Only the unit-height order-two B-spline, translation step exactly \(1\), and modulation steps \(m/(m+1)\) for integers \(m\ge2\) are treated. The theorem does not claim sharp bounds at arbitrary rational \(b\), all \(a\), other spline orders, or uniform noise robustness. A potentially older unindexed equivalent expression in polyphase, Ron--Shen, or Jacobi-matrix terminology remains a literature-overlap risk; independent scientific validation has not been performed.

## References
1. A. G. D. Atindehou, C. Frederick, Y. B. Kouagou, and K. A. Okoudjou, *On the frame set of the second-order B-spline*, arXiv:1806.05614v1 (June 14, 2018), https://arxiv.org/abs/1806.05614 .
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), section 5 and Remark 5.4, https://arxiv.org/pdf/1311.7359 .
3. R. Ghosh and A. A. Selvan, *Obstructions for Gabor frames of the second order B-spline*, arXiv:2310.01141 (2023), https://arxiv.org/pdf/2310.01141 .
4. M. Buck, C. Frederick, K. Okoudjou, and A. Stangl, *On the structure of the Gram matrix for Gabor systems generated by B-splines*, arXiv:2603.16986 (2026), https://arxiv.org/pdf/2603.16986 .
5. A. J. E. M. Janssen, *Some Weyl–Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, https://nuhagphp.univie.ac.at/janssen/data/p071.pdf .
6. D. E. Walnut, *Continuity properties of the Gabor frame operator*, Journal of Mathematical Analysis and Applications 165 (1992), 479–504.
