# Sharp multi-exponential radius asymptotics for negative Dirichlet optimal approximants

## Finding
For \(s>0\) put \(\mathcal D_{-s}=\{f(z)=\sum_{j=0}^{\infty}f_jz^j:\sum_{j\ge0}|f_j|^2(j+1)^{-s}<\infty\}\). Let \(M_s\) be the smallest possible modulus of a zero of any nonconstant-degree optimal polynomial approximant to \(1/f\), over all \(f\in\mathcal D_{-s}\) with \(f(0)\ne0\) and all approximation degrees. Then
\[
\boxed{M_s=2(2/3)^{s/2}\left(1-\frac12(8/9)^s+\frac38(64/81)^s-\frac12(20/27)^s+O((512/729)^s)\right),\quad s\to\infty.}
\]
The remainder has an absolute bound \(C(512/729)^s\) for sufficiently large \(s\), independent of \(s\). In particular, \(M_s/(2(2/3)^{s/2})\to1\), sharpening the earlier universal zero-free lower bound \((2/3)^{s/2}\) by an asymptotically exact factor of two.

For **first-degree** optimal approximants with generating polynomials of degree at most one and two, respectively, the restricted radii are exactly
\[
 M_s^{(1)}=2(2/3)^{s/2},\qquad M_s^{(2)}=\frac{2(2/3)^{s/2}}{\sqrt{1+(8/9)^s}}.
\]
The gap between the best first-degree approximant obtained with a quadratic generator and the unrestricted universal radius has the sharp additional scale
\[
\boxed{M_s^{(2)}-M_s=2(2/3)^{s/2}\left(\frac12(20/27)^s+O((512/729)^s)\right).}
\]
Thus the first influence of the third nonzero Jacobi edge, not captured by quadratic generators, occurs at the separate exponential scale \((20/27)^s\).

Finally, the extremizing normalized coefficient vector concentrates asymptotically equally on its first two coordinates. This gives a structural description of the generators associated with the smallest possible approximant zeros.

## Assumptions and scope
The parameter \(s\) is real, strictly positive, and tends to infinity; the norm uses the *specific* coefficient weights \((j+1)^{-s}\). An optimal polynomial approximant of degree \(n\ge1\) to \(1/f\) is a polynomial \(q\) of degree at most \(n\) minimizing \(\|qf-1\|_s\). The minimizer exists uniquely whenever \(f\ne0\). The radius takes the infimum over zeros of all such approximants for all \(f\) with nonzero constant term. The source's Jacobi reduction ensures this infimum is attained for \(s>0\).

The restricted radii \(M_s^{(d)}\) take the infimum **only over first-degree optimal polynomial approximants** to \(1/f\), with \(f\) a polynomial of degree at most \(d\) and with nonzero constant term. We do not claim the same restricted radii for arbitrary higher-degree approximants. In particular, the unrestricted reduction of a higher-degree zero to a linear approximant changes the generating function and need not preserve its degree.

## Proof
**1. Jacobi reduction and normalization.** Put \(\omega_j=(j+1)^{-s}\) and, for \(f=\sum f_jz^j\), set \(v_j=f_j\sqrt{\omega_{j+1}}\). Then
\[
\|zf\|_s^2=\sum_{j\ge0}|v_j|^2,\qquad
\langle f,zf\rangle_s=\sum_{j\ge0}a_jv_{j+1}\overline{v_j},\qquad
a_j=\sqrt{\frac{\omega_{j+1}}{\omega_{j+2}}}=\left(\frac{j+3}{j+2}\right)^{s/2}.
\]
The first-degree approximant has its single zero at \(\|zf\|_s^2/\langle f,zf\rangle_s\) when the denominator is nonzero. The standard reduction of zeros of higher-degree approximants to degree-one zeros (Bénéteau et al., 2016, Theorem 2.1 and Theorem 4.2; Bénéteau--Centner, 2021, Section 4.1) consequently gives
\[
M_s=\frac2{\|J_s\|},\qquad (J_s)_{j,j+1}=(J_s)_{j+1,j}=a_j,
\]
with all diagonal entries zero. This reduction also follows directly by maximizing twice the adjacent-coefficient quadratic form above over nonnegative sequences. Every vector in \(\ell^2\) defines a valid \(f\in\mathcal D_{-s}\), because \(\omega_j/\omega_{j+1}\le2^s\). The top Jacobi eigenvector has positive first coordinate, so the restriction \(f(0)\ne0\) is preserved.

Normalize by \(A=(3/2)^{s/2}\), writing \(H_s=J_s/A\), and introduce
\[
b=(8/9)^{s/2},\qquad c=(5/6)^{s/2},\qquad d=(4/5)^{s/2}.
\]
The first edges of \(H_s\) are \(1,b,c,d\), followed by decreasing positive edges. Define \(\lambda_s=\|H_s\|\); then \(M_s=2/(A\lambda_s)\).

**2. Isolation of the top eigenvalue.** Separate the first two coordinates from the tail indexed by \(2,3,\ldots\). Let \(T_s\) be the self-adjoint tridiagonal adjacency on that tail, whose first edge is \(c\) and all of whose subsequent edges are at most \(c\). Hence \(\|T_s\|\le2c\). For \(s\ge16\), \(2c<1/2\). The Rayleigh quotient of the first two coordinates already gives \(\lambda_s\ge1\). Since \(b>0\), a test vector with a small positive third component gives \(\lambda_s>1\). The upper spectrum of \(H_s\) outside \([-\|T_s\|,\|T_s\|]\) is characterized, by the Schur complement, by the scalar equation
\[
\lambda-\frac1\lambda=b^2m_s(\lambda),\qquad
m_s(\lambda)=\langle e_2,(\lambda I-T_s)^{-1}e_2\rangle,
\quad\lambda>1.
\]
The left side strictly increases and the right side strictly decreases for real \(\lambda>1\); the latter is positive. There is exactly one solution, which is the top eigenvalue. Bipartite symmetry gives negative eigenvalues in opposite pairs, so its positive value is indeed the operator norm. The inequality \(\|H_s\|\le1+b+2c\) and the Schur complement also imply \(\lambda_s\to1\) and, more precisely, \(\lambda_s-1=O(b^2)\).

**3. Resolvent expansion and scale ordering.** Since the tail graph is bipartite, its odd closed-walk moments vanish. The diagonal Neumann expansion for every \(\lambda\ge1\) yields
\[
m_s(\lambda)=\lambda^{-1}+c^2\lambda^{-3}+O(c^4),
\]
where the bound is uniform for all sufficiently large \(s\), since \(\|T_s\|\le2c<1/2\). Substituting in the eigenvalue equation gives
\[
\lambda_s^2
=1+b^2+b^2c^2\lambda_s^{-2}+O(b^2c^4)
=1+b^2+b^2c^2+O(b^4c^2+b^2c^4).
\]
Here \(b^4c^2=(160/243)^s\) and \(b^2c^4=(50/81)^s\), both bounded by \((512/729)^s=b^6\), because \(160/243<512/729\) and \(50/81<512/729\). Therefore
\[
\lambda_s^2=1+b^2+b^2c^2+O(b^6).
\]
Expanding \((\lambda_s^2)^{-1/2}\) to the first four distinct exponential scales gives
\[
\frac1{\lambda_s}
=1-\frac12b^2+\frac38b^4-\frac12b^2c^2+O(b^6).
\]
Indeed the bases are strictly ordered \(8/9>64/81>20/27>512/729\), and every omitted mixed term has an exponential base at most \(512/729\). Multiplication by \(2/A\) proves the main formula.

**4. Exact finite-degree cutoffs for linear approximants.** For first-degree optimal approximants, restricting \(f\) to degree at most \(d\) restricts the Jacobi Rayleigh quotient to its first \(d+1\) coordinates. The \(2\times2\) and \(3\times3\) compressions have largest eigenvalues \(A\) and \(A\sqrt{1+b^2}\), respectively, proving the two exact formulas. Since
\[
(1+b^2)^{-1/2}=1-\frac12b^2+\frac38b^4+O(b^6),
\]
subtracting the unrestricted expansion proves
\[
M_s^{(2)}-M_s=(2/A)\left(\frac12b^2c^2+O(b^6)\right).
\]
Positivity of the leading coefficient and the strict inequality \(20/27>512/729\) show the deficit is genuinely positive for all sufficiently large \(s\).

**5. Concentration of the extremizer.** Choose the unique positive unit eigenvector \(u^{(s)}\) for \(\lambda_s\). Its first two equations give \(u_0=u_1/\lambda_s\), and the remaining equations give
\[
(u_2,u_3,\ldots)=b\,u_1(\lambda_s I-T_s)^{-1}e_2.
\]
The uniform resolvent bound yields \(\sum_{j\ge2}|u_j|^2=O(b^2)|u_1|^2\). Since \(\lambda_s=1+O(b^2)\), normalization implies \(|u_0|^2=|u_1|^2=1/2+O(b^2)\), while the total tail mass is \(O(b^2)\). The inverse coefficient transformation \(f_j=u_j/\sqrt{\omega_{j+1}}\) realizes this vector by an actual analytic generating function. This proves the claimed localization.

## Verification
A standalone Python/SciPy checker constructs the weighted Jacobi finite sections, normalizes by the first edge, and computes the largest eigenvalue with symmetric tridiagonal routines. It compares the four-scale formula at \(s=16,20,24,30,36,44,52,64,80,100\), checks the known exact Bergman value at \(s=1\), and checks four-site truncation errors at four large parameters. All 25 programmed assertions passed. These finite computations are illustrations and consistency tests, not proofs for infinitely many \(s\) or an infinite operator. The proof above supplies the uniform remainder estimate.

The numerical checker needs Python 3, NumPy, and SciPy. Run `python checker.py` from the extracted package directory; the included output records its actual execution. The checker uses a finite truncation and does not claim exact certification of the infinite spectrum.

## Relationship to prior work
Bénéteau, Khavinson, Liaw, Seco, and Simanek (first public arXiv version June 28, 2016), Sections 4 and 5.3, established the Jacobi norm reduction, the Bergman special case, and the universal negative-index lower bound \((2/3)^{s/2}\). They explicitly observed that the precise norm for negative indices other than the Bergman case was unknown. Bénéteau and Centner (first public February 2, 2021), Section 4.1 and Open Question 1, documented the missing values and extremal generators. These spectral identities and the open question are treated as prior results, not novel contributions.

The contribution here is limited to the **large-negative-exponent regime**: the leading optimal constant, three explicitly separated corrections, a sharp low-degree approximation gap, and eigenvector localization. A comparison of published mathematical records found no known statement implying all of these expansions; it is not a proof that equivalent older results do not exist.

## Limitations
The result does not calculate the exact optimal radius for a fixed general negative Dirichlet exponent, solve the corresponding open question globally, or classify extremizing analytic functions at finite parameter. It does not claim that all zeros of the same approximant realize the bound. The finite-section checker cannot exclude effects beyond its truncation; the analytic tail estimate addresses this in the proof. Older spectral perturbation work may contain an equivalent expansion, which would affect the novelty assessment.

## References
1. C. Bénéteau and R. Centner, *A survey of optimal polynomial approximants, applications to digital filter design, and related open problems*, arXiv:2102.01725v1 (first public February 2, 2021), especially Section 4.1 and Open Question 1. https://arxiv.org/html/2102.01725v1
2. C. Bénéteau, D. Khavinson, C. Liaw, D. Seco and B. Simanek, *Zeros of optimal polynomial approximants: Jacobi matrices and Jentzsch-type theorems*, arXiv:1606.08615 (first public June 28, 2016), especially Theorems 4.2, 5.1, 5.3, and Section 5.3. https://arxiv.org/abs/1606.08615
3. R. Cheng, W. T. Ross and D. Seco, *Zeros of optimal polynomial approximants in \(\ell_A^p\)*, arXiv:2104.08014 (first public April 16, 2021). Different coefficient-norm family and parameter; cited for context, not as a direct comparison theorem. https://arxiv.org/abs/2104.08014
