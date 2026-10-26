# Exact parity law for canonical finite Cantor Fourier determinants

## Finding
For every integer \(b\ge3\) and depth \(n\ge1\), a canonical binary-digit family of \(2^n\) Fourier frequencies on the depth-\(n\) two-digit Cantor grid has a **completely explicit Gram determinant**. Its normalized Fourier matrix \(A_n^{(b)}\) satisfies
\[
|\det A_n^{(b)}|=\begin{cases}
1,&b\text{ even},\\
\left[\cos\left(\frac{\pi}{2b}\right)\right]^{(n-1)2^{n-1}},&b\text{ odd}.
\end{cases}
\]
Thus the even-base matrices are unitary, whereas the odd-base matrices remain invertible but have exponentially decaying geometric-mean singular value. In the odd case the geometric mean of the Gram eigenvalues is exactly \(\cos(\pi/(2b))^{n-1}\), and the smallest Gram eigenvalue is no greater than this value.

## Assumptions and scope
Take \(b\in\mathbb Z\), \(b\ge3\), and \(n\in\mathbb Z\), \(n\ge1\). For each binary word \(\eta=(\eta_1,\ldots,\eta_n)\), set
\[
x_\eta=2\sum_{j=1}^{n}\eta_j b^{-j}.
\]
These are the distinct support points of the uniform depth-\(n\) atomic approximation to the two-digit \(\{0,2\}\) Cantor measure. For each binary word \(\delta=(\delta_0,\ldots,\delta_{n-1})\), choose the **candidate spectral-digit frequencies**
\[
\lambda_\delta=\frac b4\sum_{k=0}^{n-1}\delta_k b^k.
\]
Define the square matrix (rows indexed by \(\eta\), columns by \(\delta\)) by
\[
A_n^{(b)}(\eta,\delta)=2^{-n/2}\exp(2\pi i\lambda_\delta x_\eta).
\]
These real frequencies are allowed even when they are not integers. The determinant is independent of row and column order up to phase, so only its absolute value is asserted. The discrete measure is \(2^{-n}\sum_\eta\delta_{x_\eta}\); it is not the limiting continuous Cantor measure.

## Proof
Write \(F_n=2^{n/2}A_n^{(b)}\) for the unnormalized matrix, with \(F_1=\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\). Fix \(n\ge2\), put \(F=F_{n-1}\), and split spatial and frequency words as \(\eta=(a,\eta')\), \(\delta=(d,\delta')\), where \(a,d\in\{0,1\}\). The definitions yield
\[
x_{(a,\eta')}=\frac{2a+x_{\eta'}}b,
\qquad \lambda_{(d,\delta')}=\frac b4d+b\lambda_{\delta'}.
\]
Set \(D=\operatorname{diag}_{\eta'}(e^{\pi i x_{\eta'}/2})\) and \(C=\operatorname{diag}_{\delta'}(e^{4\pi i\lambda_{\delta'}})\). Direct multiplication of the four phase factors gives the exact block identity
\[
F_n=\begin{pmatrix}F&DF\\FC&-DFC\end{pmatrix}.
\]
If \(b\) is even, the numbers \(4\lambda_{\delta'}=b\sum_k\delta'_k b^k\) are even integers, so \(C=I\). Subtracting the first block row from the second, one finds
\[
|\det F_n|=|\det F|^2\,2^{2^{n-1}}.
\]
If \(b\) is odd, \(C_{\delta',\delta'}=(-1)^{\sum_k\delta'_k}\). Let \(P\) be the permutation matrix exchanging the first binary spatial digit of \(\eta'\). Since the spatial shift is \(\pm2/b\), for every frequency \(\lambda_{\delta'}\) one has
\[
e^{2\pi i\lambda_{\delta'}(\pm2/b)}=(-1)^{\sum_k\delta'_k}.
\]
Therefore \(FC=PF\), exactly. Permuting the lower block rows by \(P\) and subtracting the upper block row gives
\[
|\det F_n|=|\det F|^2|\det(D+PDP)|.
\]
Each diagonal entry of \(D+PDP\) is the sum of two unit phases corresponding to spatial words whose first digits are opposite. The two phases differ by \(\pi/b\), so each sum has modulus \(2\cos(\pi/(2b))\). There are \(2^{n-1}\) such entries; hence
\[
|\det F_n|=|\det F|^2\left(2\cos\frac{\pi}{2b}\right)^{2^{n-1}}
\qquad(b\text{ odd}).
\]
Since \(F_n=2^{n/2}A_n^{(b)}\) has \(2^n\) rows, cancellation of the powers of two yields the two recurrences
\[
|\det A_n^{(b)}|=|\det A_{n-1}^{(b)}|^2\times
\begin{cases}1,&b\text{ even},\\
\cos(\pi/(2b))^{2^{n-1}},&b\text{ odd}.
\end{cases}
\]
With \(|\det A_1^{(b)}|=1\), induction gives the claimed formula because \(2(n-2)2^{n-2}+2^{n-1}=(n-1)2^{n-1}\).

Let \(G_n=(A_n^{(b)})^*A_n^{(b)}\). It is positive definite by the nonzero determinant formula, its eigenvalues are positive, and \(\det G_n=|\det A_n^{(b)}|^2\). For odd \(b\) their geometric mean is \((\det G_n)^{1/2^n}=\cos(\pi/(2b))^{n-1}\). Their minimum is at most this mean. For even \(b\), each column of \(A_n^{(b)}\) has norm one and the determinant has absolute value one. Equality in Hadamard's determinant inequality then forces the columns to be orthonormal, proving unitarity.

## Verification
An accompanying dependency-free Python script constructs the complex sampling matrices directly and compares their Gaussian-elimination log-determinants with the closed form at 35 base-depth pairs: \(b\in\{3,4,5,6,7,9,10\}\), \(1\le n\le5\). It separately checks 54 parity-block cases for \(3\le b\le11\), \(1\le n\le6\). These finite calculations are supplementary: the block determinant argument proves the identities for every specified base and depth.

## Relationship to prior work
The motivating study of de Dios Pont, Liehr and Taylor (arXiv:2607.08656, first posted July 9, 2026) proves that limiting odd-base Cantor measures have no Fourier frame. Its discussion of unsuccessful candidate frequency towers includes digits proportional to \(\sum\varepsilon_j 3^j\); that observation is particularly close to the **choice of frequencies** here. However, the limiting infinite-frame impossibility does not provide the exact finite sampling determinant, and the paper's analyzed candidate tower acts on a different finite-scale subspace. The present finding establishes the exact determinant of one specifically declared finite atomic measurement design, not an alternative proof of the limiting theorem. Standard even-base Hadamard-pair constructions and almost-Parseval-frame towers motivate the comparison but do not determine this odd-base determinant formula.

## Limitations
The determinant formula applies only to the explicitly displayed discrete grids and spectral-digit frequency sets. It is not an optimality assertion over all frequency sets, not a classification of all frames for the limiting measure, and not a sharp formula for the **least** singular value. In particular, exponential decay of the geometric mean does not determine the full singular spectrum. Historical priority outside the examined sources is not completely excluded. No independent external scientific validation has been performed.

## References
1. J. de Dios Pont, L. Liehr and M. A. Taylor, *Cantor measures with odd base do not admit Fourier frames*, arXiv:2607.08656 (first public version July 9, 2026).
2. C.-K. Lai and Y. Wang, *Non-spectral fractal measures with Fourier frames*, Journal of Fractal Geometry **4** (2017), 305–327, DOI:10.4171/JFG/52.
3. D. E. Dutkay, J. Haussermann and C.-K. Lai, *Hadamard triples generate self-affine spectral measures*, Transactions of the American Mathematical Society (2018).
