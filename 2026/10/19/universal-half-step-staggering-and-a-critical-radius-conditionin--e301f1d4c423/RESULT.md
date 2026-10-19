# Universal half-step staggering and a critical-radius conditioning law for two-ring holomorphic sampling

## Finding

**Theorem (universal angular design and Hardy transition).** Let \(n\ge2\), let \(c_0,\ldots,c_{2n-1}>0\), and let \(r,s>0\). In the \(2n\)-dimensional polynomial Hilbert space with orthonormal basis \(c_jz^j\), observe the normalized values at two regular \(n\)-gons of radii \(r,s\), with relative angular displacement \(\theta\). The complete Gram spectrum is the union of \(n\) explicitly diagonalizable two-by-two spectra below. **Simultaneously and uniquely modulo \(2\pi/n\), \(\theta=\pi/n\) maximizes the Gram determinant and the least Gram eigenvalue, minimizes the greatest Gram eigenvalue, and minimizes the squared singular-value condition number**, independently of every positive monomial weight and of both radii. This is optimization within the class of two regular \(n\)-gons, not among all arrangements of \(n\) points on each circle.

Define \(K(t)=\sum_{j=0}^{2n-1}c_j^2t^{2j}\), for \(t>0\), and, for \(0\le k<n\),
\[
T_k=\frac{n}{K(r)}\bigl(c_k^2r^{2k}+c_{k+n}^2r^{2k+2n}\bigr)+\frac{n}{K(s)}\bigl(c_k^2s^{2k}+c_{k+n}^2s^{2k+2n}\bigr),
\]
\[
D_k(\theta)=\frac{n^2c_k^2c_{k+n}^2(rs)^{2k}}{K(r)K(s)}\bigl(r^{2n}+s^{2n}-2(rs)^n\cos(n\theta)\bigr).
\]
Then the \(2n\) Gram eigenvalues, with multiplicities, are exactly
\[
\lambda_{k,\pm}(\theta)=\frac{T_k\pm\sqrt{T_k^2-4D_k(\theta)}}2,\qquad 0\le k<n.
\]
The measurement operator is invertible if and only if \(r^n\ne s^ne^{in\theta}\). In particular, every positive unequal-radius pair is invertible at every angle, while equal radii fail only when the polygons coincide.

**Hardy boundary-scale law.** Specialize to \(c_j=1\), \(s=1\), and \(0<r<1\). Put
\[
a_n=\frac{n(1-r^2)}{1-r^{2n}},\qquad \gamma_n=\frac{(1+r^n)^2}{2(1+r^{2n})},\qquad
L_{\pm}(u,\gamma)=\frac{1+u\pm\sqrt{(1-u)^2+4(1-\gamma)u}}2.
\]
At the optimal angle, the sharp squared singular-value condition number is
\[
\kappa_n^2=\frac{L_+(a_n,\gamma_n)}{L_-(a_nr^{2n-2},\gamma_n)}.
\]
For each **fixed** \(0<r<1\),
\[
\kappa_n^2\sim 2r^{-2n+2}\quad(n\to\infty).
\]
At the **critical radial scale** \(r_n=e^{-c/n}\), for every fixed \(c>0\),
\[
\lim_{n\to\infty}\kappa_n^2=\frac{L_+(a_c,\gamma_c)}{L_-(a_ce^{-2c},\gamma_c)},\qquad
a_c=\frac{2c}{1-e^{-2c}},\quad \gamma_c=\frac{(1+e^{-c})^2}{2(1+e^{-2c})}.
\]
This finite limit approaches \(1\) as \(c\downarrow0\), and is asymptotic to \(2e^{2c}\) as \(c\to\infty\).

## Assumptions and scope

The space consists of \(f(z)=\sum_{j=0}^{2n-1}a_jc_jz^j\), with complex coefficients and \(\|f\|^2=\sum_j|a_j|^2\). For \(\omega=e^{2\pi i/n}\), the sampling nodes are \(r\omega^\ell\) and \(se^{i\theta}\omega^\ell\), \(0\le\ell<n\). The normalized measurement matrix \(F_\theta\) has entries \((F_\theta)_{z,j}=c_jz^j/\sqrt{K(|z|)}\); the positive-semidefinite Gram matrix is \(G_\theta=F_\theta^*F_\theta\). The frame bounds are the minimum and maximum eigenvalues of \(G_\theta\), and \(\kappa_n^2=\lambda_{\max}/\lambda_{\min}\) at an invertible design. At a singular design, take \(\kappa_n^2=+\infty\). All optimizations hold for fixed \(n,r,s,\mathbf c\) as \(\theta\) varies. Coefficient positivity excludes degenerate monomial support.

The Hardy specialization means the degree-\((2n-1)\) polynomial subspace of \(H^2\), in which monomials have unit norm. It is not a claim about complete infinite-dimensional \(H^2\) sampling from finitely many points.

## Proof

**Step 1: Exact spectral decomposition.** Apply the normalized length-\(n\) discrete Fourier transform separately to the two ring blocks of \(F_\theta\), then group columns indexed by \(k\) and \(k+n\). Root-of-unity orthogonality \(\sum_{\ell=0}^{n-1}\omega^{\ell(j-k)}=n\mathbf 1_{j\equiv k\pmod n}\) yields an orthogonal direct sum of two-by-two matrices. Up to harmless unimodular row factors, its \(k\)-th block is
\[
B_k=\sqrt n\begin{pmatrix}
 c_kr^k/\sqrt{K(r)} & c_{k+n}r^{k+n}/\sqrt{K(r)}\\
 c_ks^k/\sqrt{K(s)} & c_{k+n}s^{k+n}e^{in\theta}/\sqrt{K(s)}
\end{pmatrix}.
\]
The trace and determinant of \(B_k^*B_k\) are exactly \(T_k\) and \(D_k(\theta)\); their characteristic roots give the stated spectrum, including repeated or zero values. The block determinant vanishes precisely when \(r^n=s^ne^{in\theta}\). Since \(r,s>0\), this is possible only for \(r=s\) and \(\theta\equiv0\pmod{2\pi/n}\), in which case all \(n\) blocks have rank one.

**Step 2: Simultaneous optimum and strict uniqueness.** With \(n,r,s,\mathbf c\) fixed, every \(T_k\) is constant, and \(D_k(\theta)\) is a strictly positive \(k\)-dependent multiple of
\[
\delta(\theta)=r^{2n}+s^{2n}-2(rs)^n\cos(n\theta).
\]
For a two-by-two positive-semidefinite matrix at fixed trace, increasing its determinant strictly raises its smaller eigenvalue and strictly lowers its larger eigenvalue, as is immediate from the quadratic-root formula. Thus raising \(\delta\) improves all \(n\) lower roots and all \(n\) upper roots strictly. Taking their global minimum and maximum preserves strict improvement; their positive ratio strictly improves as well. Furthermore \(\det G_\theta=\prod_{k=0}^{n-1}D_k(\theta)\), and every factor strictly increases. The unique maximum of \(\delta\) modulo \(2\pi/n\) occurs at \(\theta=\pi/n\). This proves all four objectives, including boundary singular cases and the independence of the weights.

**Step 3: Hardy blocks.** With \(c_j=1\) and \(s=1\), note \(K(1)=2n\) and \(K(r)=(1-r^{4n})/(1-r^2)\). At \(\theta=\pi/n\), each \(B_k^*B_k\) has trace \(1+u_k\) and determinant \(\gamma_nu_k\), where \(u_k=a_nr^{2k}\). The eigenvalues are \(L_\pm(u_k,\gamma_n)\). For \(0<r<1\), the number \(\gamma_n\) lies strictly between \(1/2\) and \(1\), and both eigenvalue branches increase strictly in \(u>0\). Indeed the square of the radical minus \((u+1-2\gamma_n)^2\) equals \(4\gamma_n(1-\gamma_n)>0\), so differentiating \(L_\pm\) shows strictly positive derivatives. Hence the largest eigenvalue is the \(k=0\) upper root, and the smallest is the \(k=n-1\) lower root, proving the exact condition-number identity.

**Step 4: Fixed-radius and boundary asymptotics.** For fixed \(0<r<1\), \(a_n\sim n(1-r^2)\), \(\gamma_n\to1/2\), and \(u_{n-1}=a_nr^{2n-2}\to0\). From the block characteristic equation, \(L_-(u,\gamma)=\gamma u/L_+(u,\gamma)\). Thus the smallest eigenvalue is asymptotic to \(a_nr^{2n-2}/2\), whereas the largest is asymptotic to \(a_n\), proving \(\kappa_n^2\sim2r^{-2n+2}\). If \(r_n=e^{-c/n}\), then \(a_n\to a_c\), \(\gamma_n\to\gamma_c\), and \(u_{n-1}\to a_ce^{-2c}\); continuity gives the claimed finite limit. As \(c\downarrow0\), all these limits tend to \(1\) and both relevant eigenvalues tend to \(1\). As \(c\to\infty\), \(a_c\sim2c\), \(\gamma_c\to1/2\), \(L_+(a_c,\gamma_c)\sim2c\), and \(L_-(a_ce^{-2c},\gamma_c)\sim ce^{-2c}\), giving the final \(2e^{2c}\) growth.

## Verification

The standalone `verify.py` reconstructs the original complex evaluation matrices, directly diagonalizes their Gram matrices, and compares with the independent two-by-two formula: 160 spectral comparisons for \(2\le n\le9\), including equal radii and radii exceeding one, have maximum absolute eigenvalue discrepancy \(5.78\times10^{-15}\). A second family of 480 angular optimization comparisons uses Bombieri monomial weights, checking the determinant and both extreme eigenvalues. Twelve fixed-radius asymptotic trials compare the scaled condition-number ratio with the analytic limit. These finite tests are corroboration, not proof of the infinite-dimensional-index statements.

## Relationship to prior work

Gröchenig and Ortega-Cerdà (2021, arXiv:2109.11825v1), in particular Section 1 and Theorem 1.1, establish the normalized-kernel polynomial-sampling framework and asymptotic Marcinkiewicz–Zygmund conditions, not the two-orbit exact finite spectra or fixed-radius phase optimization. Cruz, Massaneda, and Ortega-Cerdà (2024, arXiv:2405.19945v1), Section 1.4 and Theorems 3–5, study geometric conditions for polynomial interpolation and sampling with multiplicities, not the universal phase criterion or Hardy critical-radius transition. A 2010 MathOverflow question asks a harder **unrestricted** two-concentric-circle Fekete arrangement question; the present theorem addresses the regular-grid subfamily only and does not settle that global problem. Classical Vandermonde and Fourier-block diagonalization are prior mathematical tools, not new contributions.

## Limitations

The angular optimum is conditional on the nodes on **each** ring being a regular \(n\)-gon. It says nothing about optimizing the radii, the numbers of nodes assigned to each ring, or arbitrary angular configurations. The Hardy condition-number laws require individually normalized evaluations and the indicated radial regimes; they do not imply noise robustness uniformly in \(n\) at fixed interior radius. No independent scientific review has been performed, and an older equivalent general statement in kernel interpolation or cyclic-frame theory cannot be ruled out solely by the inspected literature.

## References

1. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz-Zygmund Inequalities for Polynomials in Fock Space*, arXiv:2109.11825v1 (2021-09-24), https://arxiv.org/html/2109.11825v1 .
2. C. A. Cruz, X. Massaneda, and J. Ortega-Cerdà, *Multiple sampling and interpolation in a space of polynomials*, arXiv:2405.19945v1 (2024-05-30), https://arxiv.org/html/2405.19945v1 .
3. *How to best distribute points on two concentric circles?*, MathOverflow question 21298 (2010), https://mathoverflow.net/questions/21298/how-to-best-distribute-points-on-two-concentric-circles .
