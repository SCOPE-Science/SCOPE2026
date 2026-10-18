# An exact singular-value coefficient and noncommutative residue for the Cesàro–shift commutator

## Finding
For the classical discrete Cesàro operator \(C\) and the forward unilateral shift \(S\) on complex \(\ell_2(\mathbb N_0)\), let \(K=CS-SC\). If \(s_n(K)\) are the nonincreasing singular values, starting at \(n=1\), then
\[
\boxed{\lim_{n\to\infty}n^2s_n(K)=\kappa
=\frac{\Gamma(1/4)^2}{2\pi\Gamma(3/4)^2}
=1.393203929685676859\ldots.}
\]
The sharp rank-\(n\) approximation rate follows: \(\inf_{\operatorname{rank}F<n}\|K-F\|=s_n(K)\sim\kappa n^{-2}\). More notably, \(|K|^{1/2}\) is Dixmier measurable: in the usual normalization every Dixmier trace satisfies
\[
\boxed{\operatorname{Tr}_{\omega}(|K|^{1/2})
=A_*:=\frac{\Gamma(1/4)}{\sqrt{2\pi}\Gamma(3/4)}
=1.180340599016096226\ldots.}
\]

## Assumptions and scope
Here \((Cx)_n=(n+1)^{-1}\sum_{j=0}^{n}x_j\), \(Se_j=e_{j+1}\), and \(|K|=(K^*K)^{1/2}\). No regularity hypothesis on input vectors beyond square summability is imposed. The singular counting function is \(N_K(t)=\#\{n\ge1:s_n(K)>t\}\) for \(t>0\). The claimed result is specific to the discrete operator \(K\); it is not a general asymptotic for all Rhaly matrices or all Toeplitz commutators. Dixmier traces refer to normalized singular-value logarithmic means of positive operators in \(\mathcal L^{1,\infty}\).

## Proof
**1. Exact matrix.** Direct subtraction gives \(K_{ij}=-[i(i+1)]^{-1}\) if \(i\ge1\) and \(0\le j<i\), and zero otherwise. Put \(A=-K\), \(a_i=[i(i+1)]^{-1}\). Thus \(A_{ij}=a_i\mathbf1_{j<i}\) and \(\|A\|_{S_2}^2=\sum_{i\ge1}ia_i^2<\infty\), so \(A\) is compact. The signs of \(K\) do not affect its singular values.

**2. Singular spectrum of a constant-weight block.** Denote by \(L_h\) the \(h\)-square inclusive lower-triangular all-ones matrix. Its inverse is the first-difference matrix. Diagonalizing the resulting tridiagonal matrix gives, for \(1\le j\le h\),
\[
s_j(L_h)=\frac{1}{2\sin((2j-1)\pi/(4h+2))}.
\]
For an \(m\)-square *strict* lower triangle, the nonzero singular values are precisely those of \(L_{m-1}\). If the positive row weights on such a block lie between \(a_{\min}\) and \(a_{\max}\), each nonzero singular value of the weighted block is bounded between the corresponding singular values of \(a_{\min}L_{m-1}\) and \(a_{\max}L_{m-1}\). In particular, for fixed \(0<p<1\), the estimate \(s_j(L_h)\le c h/j\) gives \(\|L_h\|_{S_p}^p\le c_p h\).

**3. Uniform far-tail bound.** Fix \(1/2<p<1\), and for an integer \(J\ge1\) let \(A_J=P_{[J,\infty)}AP_{[J,\infty)}\). Partition indices \(j\ge J\) into dyadic intervals \(I_k=[2^kJ,2^{k+1}J)\). The part of \(A_J\) inside a diagonal interval has Schatten-\(p\) quasi-norm to the \(p\)-th power at most \(c_p(2^kJ)^{1-2p}\), by the preceding block estimate and \(a_i\le(2^kJ)^{-2}\). For each interval the entries in earlier columns form one rank-one block; its operator norm is at most \(c(2^kJ)^{-1}\), so its Schatten-\(p\) contribution is at most \(c_p(2^kJ)^{-p}\). The Schatten quasi-triangle inequality \(\|U+V\|_{S_p}^p\le\|U\|_{S_p}^p+\|V\|_{S_p}^p\), followed by the convergent dyadic sums, yields
\[
\|A_J\|_{S_p}^p\le C_pJ^{1-2p}.
\tag{1}
\]
The remaining cross-block map from columns below \(J\) into rows at or above \(J\) has rank one. Thus, for \(0<\eta<1\),
\[
N_{P_{[J,\infty)}A}(\eta t)
\le1+C_p(\eta t)^{-p}J^{1-2p}.
\tag{2}
\]

**4. Central block counting.** Set \(R=t^{-1/2}\) and fix \(0<\varepsilon<M<\infty\). The rows below \(\varepsilon R\) contribute rank at most \(\varepsilon R+1\). By (2), the rows at and above \(MR\) contribute at most \(1+C_p\eta^{-p}M^{1-2p}R\) singular values above \(\eta t\), up to harmless integer rounding. In the central region \([\varepsilon R,MR)\), partition row/column indices into finitely many consecutive geometric blocks with maximum-to-minimum index ratio at most \(1+\delta\). The off-diagonal-block entries of \(A\) have rank at most the number of blocks: for each row block they are proportional to the vector of ones over its earlier columns. Their number is independent of \(R\), for fixed \(\varepsilon,M,\delta\).

For a block whose indices satisfy \(i/R\to x>0\), the row weights obey \(a_i/t\to x^{-2}\), uniformly up to the \((1+\delta)^2\) geometric variation. The explicit singular values in step 2 show that the fraction of the block's singular values larger than \(t\) converges, between bounds tending together as \(\delta\downarrow0\), to
\[
F(x)=\frac{2}{\pi}\arcsin\!\left(\min\left\{1,\frac{1}{2x^2}\right\}\right).
\tag{3}
\]
Equivalently, \(F(x)\) is the fraction of angular parameters \(0<\theta<\pi\) for which \(x^2<1/[2\sin(\theta/2)]\). The number of indices per infinitesimal interval \(dx\) equals \(R\,dx\), so Riemann summation over the geometric blocks and then \(\delta\downarrow0\) gives \(R\int_\varepsilon^M F(x)\,dx+o(R)\) central singular values above \(t\). This statement is made rigorous by using thresholds \((1\pm\eta)t\) and the standard singular-value inequality \(N_{U+V}(s+t)\le N_U(s)+N_V(t)\), with the reverse bound obtained by exchanging \(U\) and \(U+V\).

Let \(R\to\infty\), then \(\delta,\eta,\varepsilon\downarrow0\), and finally \(M\uparrow\infty\). The discarded low-row fraction is at most \(\varepsilon\), while the high-row fraction is \(O_p(\eta^{-p}M^{1-2p})\), which vanishes because \(p>1/2\). Continuity and integrability of \(F\), including \(F(x)=O(x^{-2})\) as \(x\to\infty\), yield
\[
\lim_{t\downarrow0}t^{1/2}N_A(t)
=\int_0^\infty F(x)\,dx=:A_*.
\tag{4}
\]

**5. Evaluation and inversion.** Tonelli's theorem applied to the equivalent angular characterization of \(F\) gives
\[
A_*=\frac{2}{\pi}\int_0^{\pi/2}\frac{d\theta}{\sqrt{2\sin\theta}}
=\frac{\Gamma(1/4)}{\sqrt{2\pi}\,\Gamma(3/4)}.
\]
Monotone inversion of (4) gives \(s_n(A)\sim A_*^2n^{-2}\), hence the first boxed formula.

**6. Noncommutative residue.** The singular values of \(|K|^{1/2}\) are \(s_n(K)^{1/2}\sim A_*/n\). Consequently
\[
\lim_{N\to\infty}\frac{1}{\log(1+N)}
\sum_{n=1}^N s_n(|K|^{1/2})=A_*.
\]
Ordinary convergence of these logarithmic means entails measurability and the stated common value for every normalized Dixmier trace.

## Verification
The matrix identity can be checked entrywise directly. The inclusive triangular singular-value formula follows from the tridiagonal first-difference eigenproblem and is valid for each finite block. The dyadic estimate (1) and rank-one cross-block decomposition give an analytic, dimension-independent control of the omitted infinite tail. Finite truncations are useful diagnostics only: at increasing ranks their \(n^2s_n\) values approach the predicted \(1.393203929685676859\ldots\), but the convergence theorem follows from the counting proof, not the numerical checks. The angular integral has the exact beta-function evaluation in step 5.

## Relationship to prior work
Sang's 2026 article places the Cesàro operator in a Toeplitz algebra and studies its operator-algebraic context, without stating this commutator's exact singular-value limit. Bellavita–Dellepiane–Stylogiannis study compactness and Schatten classes of Rhaly matrices and do not state the claimed specific sharp coefficient or residue. Bellavita–Stylogiannis give a discrete Mellin–Toeplitz calculus and Hilbert–Schmidt commutator inclusions, without a singular-value Weyl coefficient for \(CS-SC\). Previously published bounds for the *same* discrete commutator yield only two-sided \(s_n(K)\asymp n^{-2}\) estimates and the \(p=1/2\) Schatten boundary; those facts do not imply a numerical limit or Dixmier measurability. The present claim supplies the missing exact coefficient, with a direct counting proof.

## Limitations
This is an exact theorem for the particular classical discrete Cesàro/shift commutator. No uniform extension to arbitrary row weights is proved. Generic Birman–Solomyak/Toeplitz spectral-asymptotic principles and older weighted-Volterra theory might subsume some aspects under a reformulation; no priority over all possible general spectral-asymptotic formulations is asserted. The proof uses finite triangular spectra only as ingredients of an analytic counting limit and does not identify individual finite-section eigenvalues with the infinite singular values.

## References
1. Yuanqi Sang, *The Cesàro Operator is in the Toeplitz Algebra*, arXiv:2608.25740, first submitted August 26, 2026.
2. Carlo Bellavita, Eugenio Dellepiane, Georgios Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930, first submitted March 27, 2025.
3. Carlo Bellavita and Georgios Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453, first submitted September 8, 2026.
4. Vu Kim Tuan and Rudolf Gorenflo, *Asymptotics of singular values of Volterra integral operators*, Numerical Functional Analysis and Optimization 17 (1996), 453–461. Different continuous integral operators; cited as a possible related asymptotic framework, not as a verification of the discrete constant.
