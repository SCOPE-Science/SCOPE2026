# Rigidity and exact inverse conditioning for perfectly balanced Fourier sampling on circular arc unions

## Finding

For every integer \(k\ge 2\) and \(0<\rho<1\), consider the \(k\)-dimensional analytic Fourier band \(\mathcal P_k=\operatorname{span}\{1,z,\ldots,z^{k-1}\}\) in normalized \(L^2(\mathbb T)\). Restrict its energy to a measurable union \(E\) of \(r\) mutually disjoint, nondegenerate circular arcs of total normalized length \(\rho\). Perfectly conditioned restriction means that the restriction Gram matrix equals \(\rho I_k\).

**Rigidity.** Perfect conditioning requires \(r\ge k\). At the sharp component count \(r=k\), it occurs precisely for the rotated configurations
\[
E_{\phi}=\bigcup_{j=0}^{k-1}\left[\phi+\frac{2\pi j}{k},\,\phi+\frac{2\pi(j+\rho)}{k}\right]\pmod{2\pi},
\]
where boundary points are immaterial. Thus all component lengths equal \(2\pi\rho/k\), and their starting points are equally spaced.

**Exact infinitesimal inverse stability.** Fix one such configuration. Change its starting and ending angles by real amounts \(u_j\) and \(v_j\), respectively. Fix the total measure to first order and quotient common rotation by using the orthogonal gauge
\[
\sum_{j=0}^{k-1}u_j=\sum_{j=0}^{k-1}v_j=0.
\]
With the usual Euclidean norm on \(\mathbb R^{2k-2}\), and the Euclidean norm of the complex vector of the first \(k-1\) Fourier moments, the real Jacobian has squared singular values
\[
\boxed{\quad s_{\pm}^2=\frac{k}{4\pi^2}\bigl(1\pm|\cos(\pi\rho)|\bigr),\quad}
\]
each of real multiplicity \(k-1\). When \(\rho=1/2\), the two values coincide and the common squared singular value has multiplicity \(2k-2\). Since \(0<\rho<1\), both singular values are positive. The sharp local linear condition number is
\[
\boxed{\quad\kappa_{\mathrm{lin}}(\rho)=\sqrt{\frac{1+|\cos(\pi\rho)|}{1-|\cos(\pi\rho)|}}.\quad}
\]
Remarkably, this number is independent of the number of arcs. It equals one if and only if \(\rho=1/2\).

## Assumptions and scope

An arc is a proper, nondegenerate connected subarc of \(\mathbb T\), and distinct components are separated by positive-length gaps. The measure on \(\mathbb T\) is \(d\theta/(2\pi)\), the Fourier characters \(e^{ij\theta}\) are orthonormal, and
\[
c_m(E)=\frac1{2\pi}\int_Ee^{-im\theta}\,d\theta.
\]
The restriction matrix is \(G_{ij}=c_{j-i}(E)\), indexed by \(0\le i,j<k\); the transpose sign convention is immaterial to eigenvalues. Perfect conditioning means all singular values of the restriction operator \(\mathcal P_k\to L^2(E)\) are equal, equivalently \(G=\rho I_k\) since \(\operatorname{tr}G=k\rho\). Endpoint perturbations are small enough that arcs remain ordered, positive in length, and disjoint. The Jacobian statement is about the fixed-area tangent space modulo rotations, not an assertion of global noise stability or uniqueness for sets with more than \(k\) arcs.

## Proof

### 1. Fourier conditions and component threshold

Since the Gram matrix has constant diagonal \(\rho\), it equals \(\rho I_k\) precisely when \(c_m(E)=0\) for \(m=1,\ldots,k-1\). Write the arc starting and ending angles as \(\alpha_j<\beta_j\), with cyclic ordering, and set \(a_j=e^{-i\alpha_j}\), \(b_j=e^{-i\beta_j}\). Direct integration yields, for every positive integer \(m\),
\[
2\pi i m\,c_m(E)=\sum_{j=1}^r(a_j^m-b_j^m).
\]
If \(r<k\), the first \(r\) such power sums agree. Newton's identities then show that the monic polynomials \(\prod_{j=1}^r(z-a_j)\) and \(\prod_{j=1}^r(z-b_j)\) have identical coefficients and hence the same multiset of roots. However, the starting and ending endpoints of disjoint nondegenerate arcs are disjoint, a contradiction. Thus \(r\ge k\).

### 2. Equality rigidity with exactly \(k\) arcs

For \(r=k\), let \(A(z)=\prod_{j=1}^k(z-a_j)\) and \(B(z)=\prod_{j=1}^k(z-b_j)\). Equality of power sums through order \(k-1\) implies, again by Newton's identities, that \(A\) and \(B\) have identical coefficients of \(z^{k-1},\ldots,z\). Their constant coefficients are unequal, since otherwise the polynomials and the endpoint sets would coincide. For a monic polynomial whose roots all lie on \(\mathbb T\), the coefficients satisfy the self-inversive relation \(p_j=p_0\overline{p_{k-j}}\), where \(p_j\) denotes the coefficient of \(z^j\). Applying this identity to \(A\) and \(B\), their unequal constants and equal intermediate coefficients force every common intermediate coefficient to vanish. Therefore
\[
A(z)=z^k-a^k,\qquad B(z)=z^k-b^k
\]
for suitable \(|a|=|b|=1\). Each endpoint set is a regular \(k\)-gon. Since the arc starting and ending points alternate around the circle, the two polygons differ by a fixed rotation \(\ell\), with \(0<\ell<2\pi/k\). Consequently each component has the same length \(\ell\). The total occupancy gives \(k\ell/(2\pi)=\rho\), so \(\ell=2\pi\rho/k\). Conversely these arcs have \(c_m(E)=0\) for \(1\le m<k\) by the geometric-sum identity, proving the rigidity assertion.

### 3. Exact Jacobian and its spectrum

At an equal-arc configuration use \(\alpha_j^0=\phi+2\pi j/k\) and \(\beta_j^0=\alpha_j^0+\ell\), where \(\ell=2\pi\rho/k\). Differentiating the endpoint integral gives
\[
\delta c_m=\frac1{2\pi}\sum_{j=0}^{k-1}e^{-im(\phi+2\pi j/k)}\bigl(e^{-im\ell}v_j-u_j\bigr),
\qquad 1\le m<k.
\]
The area tangent condition is \(\sum_j(v_j-u_j)=0\). A common rotation adds one constant to every \(u_j\) and \(v_j\), so it has a unique representative in the gauge \(\sum u_j=\sum v_j=0\). This gauge is the orthogonal complement to the constant vectors in both real endpoint blocks.

Let \(\widehat u_m=k^{-1/2}\sum_j e^{-2\pi imj/k}u_j\), and similarly \(\widehat v_m\). Parseval gives \(\|u\|_2^2+\|v\|_2^2=\sum_{m=1}^{k-1}(|\widehat u_m|^2+|\widehat v_m|^2)\), while
\[
\delta c_m=\frac{\sqrt k}{2\pi}e^{-im\phi}\bigl(e^{-im\ell}\widehat v_m-\widehat u_m\bigr).
\]
Because \(u,v\) are real, \(\widehat u_{k-m}=\overline{\widehat u_m}\) and likewise for \(v\). For each non-Nyquist pair \(m,k-m\), the squared output energy is determined by the complex \(2\times2\) matrix
\[
M_m=\begin{pmatrix}-1&e^{-im\ell}\\-1&e^{i(k-m)\ell}\end{pmatrix}
\]
acting on \((\widehat u_m,\widehat v_m)\), apart from a common factor \(k/(4\pi^2)\). Its Gram matrix has diagonal entries two and off-diagonal entries whose modulus is \(2|\cos(k\ell/2)|\). Hence the eigenvalues are \(2(1\pm|\cos(k\ell/2)|)\). The real input energy for this conjugate pair has an extra factor of two. Thus each pair contributes the two squared real singular values \(k(1\pm|\cos(\pi\rho)|)/(4\pi^2)\), each twice as a real eigenvalue. If \(k\) is even, the Nyquist frequency \(m=k/2\) is real; its \(2\times2\) real Gram matrix has diagonal one and off-diagonal \(-\cos(\pi\rho)\), giving the same two values once each. Altogether each value has multiplicity \(k-1\); at \(\rho=1/2\) they merge. Both are strictly positive for \(0<\rho<1\).

### 4. Sharp nonlinear first-order stability

Let \(F\) be the first \(k-1\) complex moment map on the local gauge chart around the equal-arc design. It is real analytic, \(F(0)=0\), and its real Jacobian \(J\) is invertible by Step 3. For every fixed \(k,\rho\), Taylor's theorem yields
\[
\|F(h)-Jh\|_2\le C_{k,\rho}\|h\|_2^2
\]
for sufficiently small endpoint displacement \(h\) in the gauge. Therefore
\[
s_-\|h\|_2-C_{k,\rho}\|h\|_2^2\le\|F(h)\|_2\le s_+\|h\|_2+C_{k,\rho}\|h\|_2^2.
\]
Both leading constants are sharp because their singular directions exist. The inverse function theorem gives a smooth local inverse from the first \(k-1\) complex moments to the endpoint chart, with sharp infinitesimal condition number \(s_+/s_-\).

## Verification

The accompanying standalone Python/NumPy script constructs the real Jacobian in an orthonormal basis of mean-zero endpoint perturbations. For every integer \(k\) from two through thirteen and six occupancies per integer, it compares the entire numerical singular spectrum to the two predicted values with multiplicities. It also independently compares an analytic differential against symmetric finite differences of the exact arc Fourier integrals. All 144 tests passed. These finite diagnostics support—but do not replace—the universal analytical proof above. The exact singular spectrum follows from Fourier orthogonality, the real conjugacy pairing, and elementary two-by-two Gram calculations.

## Relationship to prior work

Courtney, *Unions of arcs from Fourier partial sums* (2010), proves a global reconstruction theorem when \(k\) positive Fourier moments and the mean are provided for a union of at most \(k\) arcs, using finite Blaschke products; its Section 4 gives endpoint reconstruction. The present rigidity concerns the restricted zero-moment pattern through only order \(k-1\), but the substantial quantitative contribution is the closed spectrum of the *linearized inverse* at the uniquely balanced configuration, not recovery from the full moment data. Huang, *A Wiener-type theorem for arcs in the unit circle* (first public version 2024), treats reconstruction of arc measures from Fourier-series limits and does not formulate this finite-component isometric restriction or local endpoint singular-spectrum problem. Batenkov and Yomdin (2011, 2013) formulate local conditioning and recovery in general Prony systems and piecewise-smooth Fourier inversion. Their stated models and local-accuracy bounds provide broad foundational coverage of endpoint inversion, but the examined results do not give the two-level singular spectrum of the particular fixed-area, conjugate-paired circular-arc map here. The present claim is limited to this precise specialization rather than general Prony inversion.

## Limitations

This gives optimality and rigidity for perfectly conditioned restriction at the minimal number of components, not a universal comparison among all masks with more components. Sharp local constants are for Euclidean endpoint perturbations, fixed normalized area and removal of global rotation; changing the weighting of endpoint errors or Fourier measurements changes the singular spectrum. Uniformity in \(k\), a global inverse Lipschitz bound, arbitrary nonsymmetric designs, and noisy nonlocal recovery are not asserted. Priority beyond the inspected sources remains a possible limitation; independent validation has not been performed.

## References

1. D. Courtney, *Unions of arcs from Fourier partial sums*, New York Journal of Mathematics **16** (2010), 235–243. First arXiv version 2010-02-03, arXiv:1002.0639; full paper https://nyjm.albany.edu/j/2010/16-11v.pdf.
2. H. Huang, *A Wiener-type theorem for arcs in the unit cirle*, arXiv:2407.19424v1, first publicly submitted 2024-07-28; https://arxiv.org/abs/2407.19424.
3. D. Batenkov and Y. Yomdin, *On the accuracy of solving confluent Prony systems*, arXiv:1106.1137v1 (2011); https://arxiv.org/abs/1106.1137.
4. D. Batenkov and Y. Yomdin, *Local and global geometry of Prony systems and Fourier reconstruction of piecewise-smooth functions*, arXiv:1301.1187v1 (2013); https://arxiv.org/abs/1301.1187.
