# Exact binomial spectral-gap statistics for the planar twisted baker map

## Finding

Let \(F:[-1,1]\times[0,1]\to[-1,1]\times[0,1]\) be the piecewise-affine twisted baker map of Saiki, Takahasi and Yorke,
\[
F(x,y)=\begin{cases}(1+2x,y),&x<0,\\(1-2y,x),&x\ge0.\end{cases}
\]
For each integer \(n\ge1\), consider the \(2^n-1\) isolated points fixed by \(F^n\) outside the fixed face \(\{x=-1\}\), choosing such a point uniformly. Let \(J_n\) denote its return Jacobian and let \(\lambda_1,\lambda_2\) be its two eigenvalues (with multiplicity). Define the nonnegative multiplier gap
\[
H_n=\frac{\bigl|\log|\lambda_1|-\log|\lambda_2|\bigr|}{\log2}.
\]
Exactly \(2^{n-1}\) points have a nonreal conjugate pair, all with \(H_n=0\). The other \(2^{n-1}-1\) points have two real eigenvalues. Among these real-spectrum points the **signed coordinate-exponent gap** \(D_n\), defined by the difference of the powers of two on the two diagonal entries of \(J_n\), obeys the complete exact count
\[
\#\{D_n=n-2k\}=\binom{n-1}{k}-\mathbf 1_{\{k=0\}},\qquad k=0,1,\ldots,n-1.
\]
For real spectrum, \(H_n=|D_n|\). Thus the formula specifies the complete finite-\(n\) distribution of the absolute multiplier gap, including ties and multiplicities. In particular, as \(n\to\infty\),
\[
\frac{H_n}{\sqrt n}\ \Longrightarrow\ \tfrac12\delta_0+\tfrac12\mathcal L(|Z|),\qquad Z\sim N(0,1).
\]
Conditioning on a real return spectrum removes the zero-atom contribution and yields the folded-normal limit \(\mathcal L(|Z|)\). Equivalently, typical iterate-normalized Lyapunov-multiplier differences are of order \(n^{-1/2}\) even though exceptional periodic points have order-one differences.

## Assumptions and scope

The theorem treats the **planar** map, not the higher-dimensional generalization. A point fixed by \(F^n\) can have smaller prime period; no primitivity assumption is made. The face \(\{x=-1\}\) consists of non-isolated fixed points and is deliberately excluded. The source proves unique symbolic representation by all \(n\)-letter words over \(\{L,R\}\) except the all-\(L\) word; there are no periodic points on the switching line \(x=0\). The spectral gap uses eigenvalue **moduli**. The signed gap \(D_n\) is used only for diagonal (real-spectrum) return matrices; it is not claimed to be a spectral splitting in the nonreal case.

## Proof

Set
\[
J_L=\begin{pmatrix}2&0\\0&1\end{pmatrix},\qquad J_R=\begin{pmatrix}0&-2\\1&0\end{pmatrix}.
\]
Fix a symbolic word \(w_1\cdots w_n\), let \(p_j\) be the number of letters \(R\) among the first \(j\) letters, and put \(s_j=(-1)^{p_j}\) for \(j=0,\dots,n\). Each Jacobian factor is a signed permutation times a one-coordinate doubling. Each letter \(R\) interchanges which original coordinate appears in the first current coordinate, and a letter \(L\) leaves that label unchanged. For the \(j\)-th step, the doubled original coordinate is the first one exactly when \(s_j=1\), and the second one exactly when \(s_j=-1\): for \(L\) this follows from \(s_j=s_{j-1}\); for \(R\) the doubling takes the previous **second** coordinate and the labels switch, so the same final-sign convention holds.

Consequently, if \(a\) and \(b\) count the doubling factors received by the original first and second coordinates, then
\[
a+b=n,\qquad a-b=\sum_{j=1}^{n}s_j=:D(w).
\]
If the twist count \(p_n\) is even, the product has no net coordinate permutation, its diagonal entries are \((-1)^{p_n/2}2^a\) and \((-1)^{p_n/2}2^b\), and their multiplier gap in units of \(\log2\) is \(|D(w)|\). If \(p_n\) is odd, the product is anti-diagonal and its determinant is \(2^n>0\). Because the product of its off-diagonal entries equals \(-2^n\), its eigenvalues are \(\pm i2^{n/2}\), so the modulus gap is exactly zero. Therefore even and odd twist counts coincide exactly with real and nonreal return spectra.

The change of variables \(w\mapsto(s_1,\ldots,s_n)\) is a bijection from binary words to sign sequences: \(w_j=R\) precisely if \(s_j\ne s_{j-1}\), with \(s_0=1\). Having an even number of \(R\) letters is equivalent to \(s_n=1\). With this last sign fixed, the first \(n-1\) signs can be chosen independently, and
\[
D(w)=1+\sum_{j=1}^{n-1}s_j.
\]
For \(k\) negative signs the value is \(n-2k\), giving \(\binom{n-1}{k}\) words. The all-\(L\) word is the unique forbidden word, has \(k=0\), and contributes the indicated subtraction. Exactly half of all binary words have odd twist count and none of those is all-\(L\); this gives \(2^{n-1}\) nonreal return spectra and \(2^{n-1}-1\) real spectra.

Finally, uniform signs \(s_1,\ldots,s_{n-1}\) satisfy the classical central limit theorem,
\[
\frac{1+\sum_{j=1}^{n-1}s_j}{\sqrt n}\Longrightarrow N(0,1).
\]
Removing one out of \(2^{n-1}\) even-parity words does not alter this weak limit. The continuous absolute-value map yields a folded normal for the real spectra, while every odd-parity word has gap zero and the two parity classes have asymptotic weights one half. Their mixture gives the claimed limit.

## Verification

The embedded standalone `check_spectral_gap.py` exhaustively multiplies the integer Jacobian matrices for all non-all-left binary words at lengths \(1\le n\le12\), compares exact diagonal/anti-diagonal shapes, checks the signed gap formula and verifies all binomial multiplicities. Its success output is `CHECK_OK`. Those finite computations check the combinatorial bookkeeping, not the infinite-dimensional or asymptotic statement: the analytical proof establishes every \(n\) and the limit.

## Relationship to prior work

Saiki, Takahasi and Yorke introduced the map, its symbolic coding, the twist-number spectral distinction, qualitative non-uniform periodic expansion, and periodic-point equidistribution (Theorems A–D; Lemmas 2.1–2.6; Appendix A of the cited paper). Their Section 2.3 counts the **number of right-branch visits modulo the dimension**, not the resulting two-coordinate stretch imbalance. This finding distinguishes its output: the exact *full multiplier-gap distribution* and the half-normal/zero-atom asymptotic, rather than simply real-versus-complex eigenvalue proportions. The two-state sign transformation is the additional argument needed beyond the established parity count; ordinary Bernoulli coding alone does not specify eigenvalue-gap statistics until the cocycle is analyzed.

## Limitations

No claim is made for prime-period-only sampling, higher dimensions, or joint spatial/derivative fluctuations. The general central limit theorem for sums of independent signs is classical; the statement specific to this dynamical system is the exact identification of its periodic Jacobian exponents with that sign sum. Publication priority beyond inspected literature remains open to independent verification.

## References

1. Y. Saiki, H. Takahasi, and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304v1 (first submitted 9 February 2022), revised arXiv:2202.04304v3 (13 January 2023), *Nonlinearity* 36 (2023), 1776–1788. https://arxiv.org/abs/2202.04304; complete author text: https://arxiv.org/html/2202.04304v3.
2. Classical de Moivre–Laplace central limit theorem for independent fair signs, used only after the explicit symbol-to-sign bijection.
