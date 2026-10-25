# Radial rigidity and the sharp spectral gap for polyanalytic disk concentration

## Finding
Let \(m\ge1\), \(0<R<1\), and let \(w:(0,1)\to(0,\infty)\) be measurable, positive almost everywhere, with \(0<\int_0^1w(s)\,ds<\infty\). Put \(d\mu_w(z)=\pi^{-1}w(|z|^2)\,dA(z)\), and let \(\mathcal A_m^2(w)\) be the closure in \(L^2(\mu_w)\) of polyanalytic polynomials of order at most \(m\) (polynomials satisfying \(\partial_{\bar z}^{m}f=0\)). For standard locally comparable radial weights this agrees with the usual full weighted polyanalytic Bergman space. Denote by \(C_R\) the compression of multiplication by \(\mathbf1_{\{|z|^2<R\}}\) to this space.

**Angular spectral domination theorem.** For nonnegative angular frequency \(k\), let \(\lambda_1(k)\ge\cdots\ge\lambda_m(k)\) denote the eigenvalues of the disk-concentration form on \(z^k\mathcal P_{m-1}(|z|^2)\), in decreasing order, with repetitions allowed in the notation. Every eigenvalue is strictly between zero and one, and for each \(j=1,\ldots,m\),
\[
\lambda_j(k+1)<\lambda_j(k)\qquad(k\ge0).
\]
For negative frequency \(-h\), \(1\le h\le m-1\), the \((m-h)\)-dimensional block is spectrally dominated, eigenvalue by eigenvalue, by the positive frequency \(+h\) block. Consequently **every maximizing function for centered-disk concentration is radial**, and the optimal constant is the largest eigenvalue of the finite \(m\times m\) radial moment pencil. This holds for every such positive radial weight, without a monotonicity assumption on \(w\).

**Explicit bianalytic theorem.** In the unweighted case \(w\equiv1\) and \(m=2\), put
\[
T_k(R)=(k+2)^2R^{k+1}-2(k+1)(k+3)R^{k+2}+(k+2)^2R^{k+3},
\]
\[
\Lambda_k^{\pm}(R)=\frac{T_k(R)\pm\sqrt{T_k(R)^2-4R^{2k+4}}}{2}\quad(k\ge0).
\]
The complete spectrum, including the zero accumulation point, is
\[
\sigma(C_R)=\{0,R^2\}\cup\{\Lambda_k^+(R),\Lambda_k^-(R):k\ge0\}.
\]
The largest and second-largest eigenvalues, both simple, are exactly \(\Lambda_0^+(R)\) and \(\Lambda_1^+(R)\). For every nonzero bianalytic \(f\),
\[
\int_{|z|^2<R}|f(z)|^2\,\frac{dA(z)}\pi
\le\Lambda_0^+(R)\int_{|z|<1}|f(z)|^2\,\frac{dA(z)}\pi,
\]
with equality precisely for scalar multiples of
\[
U_R(z)=\Lambda_0^+(R)-R^2-2(\Lambda_0^+(R)-R)|z|^2.
\]
Let \(\Pi_R\) be orthogonal projection onto \(\mathbb C U_R\). The following **sharp global stability estimate** has best possible positive coefficient \(\Delta(R)=\Lambda_0^+(R)-\Lambda_1^+(R)\):
\[
\int_{|z|^2<R}|f|^2\,\frac{dA}\pi
\le\Lambda_0^+(R)\|f\|_2^2-\Delta(R)\|f-\Pi_Rf\|_2^2.
\]
Equality in this stability inequality occurs exactly on the two-dimensional span of \(U_R\) and
\[
V_R(z)=z\bigl[2(\Lambda_1^+(R)-R^3)-3(\Lambda_1^+(R)-R^2)|z|^2\bigr].
\]
The gap has the two different sharp endpoint scales
\[
\Delta(R)=4R+O(R^2)\quad(R\downarrow0),\qquad
\Delta(R)=\tfrac34(1-R)^3+O((1-R)^4)\quad(R\uparrow1).
\]

## Assumptions and scope
The coordinate \(R\) is the **squared** Euclidean radius, not the ordinary radius. The domain for \(m\)-analytic functions is \(\mathbb D=\{|z|<1\}\); no analyticity is assumed for the weight. The arbitrary-weight domination conclusion concerns the **full** polyanalytic space, not just its orthogonal true-polyanalytic summand. All global bianalytic closed formulas and endpoint constants above assume unweighted normalized area measure. The zero in the displayed spectrum is its accumulation point, not a nonzero-eigenvector eigenvalue. Other spectral values can collide for exceptional radii; simplicity is claimed only for the two largest ones.

For each angular frequency \(k\ge0\), its quotient for a polynomial \(P\) of degree at most \(m-1\) is
\[
Q_k(P)=\frac{\int_0^R s^k|P(s)|^2w(s)\,ds}{\int_0^1 s^k|P(s)|^2w(s)\,ds}.
\]
At negative frequency \(-h\), the same formula uses exponent \(h\) but restricts the polynomial degree to at most \(m-h-1\). These are genuine finite-dimensional quotients because the weight is positive almost everywhere. The sharp arbitrary-weight constant is the top generalized eigenvalue of the pair
\[
H_{ij}(R)=\int_0^R s^{i+j}w(s)\,ds,\qquad G_{ij}=\int_0^1s^{i+j}w(s)\,ds
\quad(0\le i,j<m).
\]

## Proof
**1. Fourier-sector decomposition.** Every polyanalytic polynomial of order at most \(m\) is a sum of terms \(z^a\bar z^b\) with \(b<m\). Angular Fourier projection therefore yields the mutually orthogonal sectors \(z^kP(|z|^2)\), \(k\ge0\), \(\deg P\le m-1\), and \(\bar z^hP(|z|^2)\), \(1\le h\le m-1\), \(\deg P\le m-h-1\). Angular orthogonality applies both to the full norm and to the cutoff form. Taking the closure of the polyanalytic polynomial span yields the Hilbert direct sum of these sectors by definition.

**2. Strict size bias.** Fix a nonzero polynomial \(P\) of degree at most \(m-1\) and any \(k\ge0\). Let \(\nu\) be the probability measure proportional to \(s^k|P(s)|^2w(s)\,ds\). Because \(w>0\) almost everywhere and a nonzero polynomial has only finitely many zeros, both \((0,R)\) and \((R,1)\) have positive \(\nu\)-mass. Thus
\[
\operatorname{Cov}_{\nu}(s,\mathbf1_{(0,R)}(s))
=\nu(0,R)\nu(R,1)
\bigl(\mathbb E_\nu[s\mid s<R]-\mathbb E_\nu[s\mid s>R]\bigr)<0.
\]
Dividing \(\mathbb E_\nu[s\mathbf1_{(0,R)}]\) by \(\mathbb E_\nu[s]\) proves \(Q_{k+1}(P)<Q_k(P)\). On the compact projective space of nonzero polynomials of bounded degree, the positive difference \(Q_k-Q_{k+1}\) has a strictly positive minimum \(\delta_{k,m,R,w}\). The Courant–Fischer minimax principle applied on the same polynomial vector space then gives \(\lambda_j(k+1)\le\lambda_j(k)-\delta_{k,m,R,w}<\lambda_j(k)\) for every index.

**3. Negative-sector comparison.** In frequency \(-h\), multiplication of \(P(s)\) by \(\bar z^h\) has the same radial energy distribution as multiplication by \(z^h\). Its polynomial space \(\mathcal P_{m-h-1}\) is contained in the positive-frequency \(+h\) polynomial space \(\mathcal P_{m-1}\). Minimax gives \(\lambda_j(-h)\le\lambda_j(+h)<\lambda_j(0)\) for every available index, proving that only radial functions can attain the top eigenvalue. The radial space is finite-dimensional, hence its largest eigenvalue is attained.

**4. Bianalytic block spectrum.** Now set \(m=2\), \(w=1\). In the basis \(z^k,z^k|z|^2\) of the \(+k\) sector, the full and cutoff Gram matrices are
\[
G_k=\begin{pmatrix}\frac1{k+1}&\frac1{k+2}\\\frac1{k+2}&\frac1{k+3}\end{pmatrix},\qquad
H_k(R)=\begin{pmatrix}\frac{R^{k+1}}{k+1}&\frac{R^{k+2}}{k+2}\\\frac{R^{k+2}}{k+2}&\frac{R^{k+3}}{k+3}\end{pmatrix}.
\]
Direct inversion shows \(\operatorname{tr}(G_k^{-1}H_k)=T_k(R)\). Factoring the powers of \(R\) by rows and columns gives \(\det(H_k)/\det(G_k)=R^{2k+4}\). Hence the generalized eigenvalues are precisely \(\Lambda_k^\pm(R)\). They are distinct for \(0<R<1\), because the cutoff matrix cannot be a scalar multiple of the full matrix (the conditional mean of \(s\) below \(R\) is strictly smaller than its global mean). The negative angular sector is \(\mathbb C\bar z\), with eigenvalue \(R^2\). Also \(T_k(R)\to0\) exponentially as \(k\to\infty\), proving compactness and completing the spectral description.

**5. Exact top-two separation.** For \(k=0\) and \(k=1\), evaluate the characteristic polynomials \(p_k(x)=x^2-T_k(R)x+R^{2k+4}\) at \(x=R^2\):
\[
p_0(R^2)=-4R^3(1-R)^2<0,\qquad p_1(R^2)=-8R^4(1-R)^2<0.
\]
Thus \(\Lambda_0^-(R)<R^2<\Lambda_0^+(R)\) and \(\Lambda_1^-(R)<R^2<\Lambda_1^+(R)\). Step 2 implies \(\Lambda_0^+>\Lambda_1^+>\Lambda_k^+\) for all \(k\ge2\), while all other eigenvalues are smaller than \(\Lambda_1^+\). The top two are therefore simple and in angular frequencies zero and one, respectively. Solving the first row of each generalized eigenvector equation gives \(U_R\) and \(V_R\) exactly as stated; these vectors are nonzero for \(0<R<1\). Spectral expansion gives the stability inequality, sharpness and its complete equality space.

**6. Gap asymptotics.** Directly expanding the quadratic formulas at \(R=0\) gives \(\Lambda_0^+=4R+O(R^2)\) and \(\Lambda_1^+=9R^2+O(R^3)\). At \(R=1-\varepsilon\), direct substitution in \(p_k\), selecting the larger eigenvalue, yields \(\Lambda_0^+=1-\varepsilon^3/4+O(\varepsilon^4)\) and \(\Lambda_1^+=1-\varepsilon^3+O(\varepsilon^4)\). Subtraction proves the stated gap limits.

## Verification
Run `python check.py` in a Python environment with SymPy, NumPy and SciPy. The checker exactly simplifies the block trace and determinant formulas for ten angular indices; tests the characteristic inequalities at seven rational squared radii; independently diagonalizes the generalized moment matrices; verifies 36 Jacobi-weighted spectral monotonicity regimes for polyanalytic orders two through four; tests 1,000 deterministic random bianalytic coefficient packets; and checks the two cubic edge coefficients symbolically. A successful run prints the assertion count. These finite checks do not certify the infinite-dimensional or all-weight claims; the preceding minimax/size-bias and algebraic arguments supply those proofs.

## Relationship to prior work
Barrera-Castelán, Maximenko and Ramos-Vazquez (arXiv:2009.14301, first public version 2020-09-29), Sections 5, 7 and 8, establish Fourier-sector decomposition and matrix representations of radial Toeplitz operators on weighted polyanalytic Bergman spaces. Their Proposition 8.5 includes general integral matrix blocks, which supply a foundation for the present calculation and already imply the un-ordered block matrices. The additional conclusions here are the **strict angular ordering for every positive radial weight and every polyanalytic order**, the identity of the two leading eigenvalues of the unweighted bianalytic disk-cutoff operator, and its **sharp global gap and equality classification**. These are not asserted in the inspected sections of that work.

Maximenko and Tellería-Romero (arXiv:1905.00978, first public version 2019-05-02), Sections 5–6, develop analogous radial matrix representations in Gaussian polyanalytic Fock spaces, a different ambient domain and measure. The Fock analysis does not imply the present fixed-unit-disk moment ordering or the bianalytic spectral gap. Earlier analytic (order-one) radial Toeplitz spectral results also do not establish the coupling within higher-order angular blocks.

## Limitations
The strict ordering uses a **centered initial radial interval**; it need not hold for annuli or arbitrary disconnected radial windows. Positive almost-everywhere weight is essential to the strict covariance argument. The all-order result identifies the top eigenspace as radial but does not assert its dimension for arbitrary weights and orders. The explicit two-branch spectrum, top-two classification and endpoint constants are proved only for unweighted order two. Prior matrix representations make the algebraic calculation accessible; independent priority verification against all older literature has not been performed.

## References
1. R. M. Barrera-Castelán, E. A. Maximenko and G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces*, arXiv:2009.14301, submitted 2020-09-29, Sections 5, 7–8. https://arxiv.org/abs/2009.14301
2. E. A. Maximenko and A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978, submitted 2019-05-02, Sections 5–6. https://arxiv.org/abs/1905.00978
