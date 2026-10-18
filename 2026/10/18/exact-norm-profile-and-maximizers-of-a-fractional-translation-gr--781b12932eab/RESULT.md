# Exact norm profile and maximizers of a fractional translation group with checkerboard weights

## Finding
For positive weights \(a,b\), define \(w_{2k}=a\) and \(w_{2k+1}=b\) for every \(k\in\mathbb Z\). Equip complex sequences with
\[
\|x\|_w^2=\sum_{n\in\mathbb Z}w_n|x_n|^2.
\]
For real \(t\), consider the fractional discrete translation of De Carli and Samad, initially on finitely supported sequences:
\[
(T_tx)_m=
\begin{cases}
\displaystyle\frac{\sin(\pi t)}{\pi}\sum_{n\in\mathbb Z}\frac{x_n}{m-n+t},&t\notin\mathbb Z,\\
(-1)^t x_{m+t},&t\in\mathbb Z.
\end{cases}
\]
Each \(T_t\) extends uniquely to a bounded operator on \(\ell^2(w)\). Put
\[
\beta=\frac{|a-b|}{2\sqrt{ab}}.
\]
The exact sharp operator norm, **for every \(t\in\mathbb R\)**, is
\[
\boxed{\|T_t\|_{\ell^2(w)\to\ell^2(w)}=
\sqrt{1+\beta^2\sin^2(\pi t/2)}+\beta|\sin(\pi t/2)|.}
\]
In particular, the logarithm of the norm equals \(\operatorname{arsinh}(\beta|\sin(\pi t/2)|)\). This is a sharp two-periodic profile, whose maximum is \(\sqrt{\max\{a/b,b/a\}}\). If \(a\ne b\), the group elements are isometries exactly at even integer parameters; at all other parameters their norm is greater than one despite spectral radius one. The norm is attained by nonzero weighted square-summable sequences for every \(t\). In the non-isometric case the maximizers are precisely the sequences whose folded Fourier transforms lie almost everywhere in the one-dimensional top singular subspace described below.

## Assumptions and scope
The domain is the bilateral lattice \(\mathbb Z\), the scalar field is \(\mathbb C\), the two weights are arbitrary fixed strictly positive real numbers, and the parameter is an arbitrary real number. The kernel formula at nonintegral parameters is first defined on finite-support sequences, where each output coordinate is a finite sum; the stated extension is in the weighted Hilbert-space norm. The definitions at integer and noninteger parameters agree by the Fourier multiplier representation below. The weights are precisely checkerboard-periodic, not arbitrary periodic, and no claim is made for general \(\ell^p\) norms.

## Proof
**1. Fourier multiplier and extension.** Choose \(\widehat{x}(\theta)=\sum_{n\in\mathbb Z}x_ne^{in\theta}\), with inverse \(x_n=(2\pi)^{-1}\int_0^{2\pi}\widehat{x}(\theta)e^{-in\theta}\,d\theta\). The bounded unimodular multiplier
\[
m_t(\theta)=e^{it(\pi-\theta)},\qquad 0<\theta<2\pi,
\]
has Fourier coefficient
\[
\frac1{2\pi}\int_0^{2\pi}m_t(\theta)e^{-ij\theta}\,d\theta
=\frac{\sin(\pi t)}{\pi(j+t)},\qquad t\notin\mathbb Z.
\]
At integer \(t\), it equals \((-1)^te^{-it\theta}\), giving exactly the prescribed integer shift. Thus \(T_t\) agrees on finite-support sequences with multiplier \(m_t\) and extends to a unitary operator on ordinary \(\ell^2(\mathbb Z)\). Since \(\min\{a,b\}\|x\|_2^2\le\|x\|_w^2\le\max\{a,b\}\|x\|_2^2\), the same maps extend boundedly to \(\ell^2(w)\). The multipliers show \(T_sT_t=T_{s+t}\), \(T_t^{-1}=T_{-t}\), and strong continuity in the weighted norm.

**2. Exact folding of the weighted metric.** Write \(u=(a+b)/2\), \(v=(a-b)/2\), so \(w_n=u+v(-1)^n\). For \(0<\theta<\pi\), set \(\Phi_x(\theta)=(\widehat{x}(\theta),\widehat{x}(\theta+\pi))^{\mathsf T}\). Parseval and the parity identity yield the exact integral
\[
\|x\|_w^2=\frac1{2\pi}\int_0^\pi\Phi_x(\theta)^*W\Phi_x(\theta)\,d\theta,
\qquad W=\begin{pmatrix}u&v\\v&u\end{pmatrix}.
\]
The matrix \(W\) is positive definite with eigenvalues \(a,b\) and determinant \(ab\). The Fourier transform followed by folding and multiplication by \(W^{1/2}\) is a unitary equivalence from \(\ell^2(w)\) to standard \(L^2((0,\pi);\mathbb C^2)\), up to the harmless overall normalization \((2\pi)^{-1/2}\).

**3. A constant two-by-two fiber.** For almost every \(0<\theta<\pi\),
\[
\begin{pmatrix}m_t(\theta)&0\\0&m_t(\theta+\pi)\end{pmatrix}
=m_t(\theta)D_t,
\qquad D_t=\operatorname{diag}(1,e^{-i\pi t}).
\]
Consequently \(T_t\) is unitarily equivalent to the multiplication operator by \(m_t(\theta)B_t\), where
\[
B_t=W^{1/2}D_tW^{-1/2}.
\]
Since the scalar phase has modulus one, its operator norm equals the largest singular value \(s\ge1\) of the *single constant matrix* \(B_t\). The determinant has modulus one. Direct multiplication using
\[
W^{-1}=\frac1{ab}\begin{pmatrix}u&-v\\-v&u\end{pmatrix}
\]
gives
\[
\operatorname{tr}(B_t^*B_t)
=\operatorname{tr}(W^{-1}D_t^*WD_t)
=\frac{2(u^2-v^2\cos(\pi t))}{ab}
=2+4\beta^2\sin^2(\pi t/2).
\]
The squared singular values are \(s^2\) and \(s^{-2}\); hence
\[
(s-s^{-1})^2=4\beta^2\sin^2(\pi t/2).
\]
Taking the nonnegative root and solving the quadratic \(s^2-2\beta|\sin(\pi t/2)|s-1=0\) yields the boxed formula for all real parameters, including integers and equal weights.

**4. Sharpness and equality.** Let \(E_t\subseteq\mathbb C^2\) be the eigenspace of \(B_t^*B_t\) for its largest eigenvalue. Choose any nonzero \(h\in L^2(0,\pi)\) and a fixed unit vector \(q\in E_t\). The folded transform \(\Phi_x(\theta)=h(\theta)W^{-1/2}q\) represents a nonzero sequence in \(\ell^2(w)\), and the equality \(\|T_tx\|_w=s\|x\|_w\) holds by pointwise singular-value equality. Conversely, the nonnegative pointwise deficit \(s^2\|W^{1/2}\Phi_x\|_2^2-\|B_tW^{1/2}\Phi_x\|_2^2\) integrates to zero only if \(W^{1/2}\Phi_x(\theta)\in E_t\) almost everywhere. If \(\beta|\sin(\pi t/2)|>0\), the two singular values are distinct, so \(E_t\) is one-dimensional; otherwise \(B_t\) is unitary and every vector is a maximizer.

**5. Structural consequences.** The scalar function \(r\mapsto\sqrt{1+r^2}+r\) is strictly increasing on nonnegative reals. Since \(|\sin(\pi t/2)|\) ranges from zero to one, the minimum and maximum and the precise isometry parameters follow. The endpoint \(t=1\) gives \(\|T_1\|_w=\sqrt{\max\{a/b,b/a\}}\), consistent with the shift's direct weight ratio. Similarity to the unweighted unitary multiplier preserves the spectrum and its spectral radius one; a bounded normal operator would have norm equal to spectral radius. Thus every non-isometric element is nonnormal in the weighted metric.

## Verification
The companion `verify.py` independently evaluates the two-by-two conjugated matrix, its singular values and determinant, and Fourier coefficients of the kernel for deterministic parameter families. Run `python verify.py` using Python 3 with no external dependencies. It prints `VERIFY_OK` after 1,880 finite numerical checks. The verification includes equal weights, odd/even integer parameters, highly unequal weights, and noninteger positive and negative parameters. The spectral and multiplier identities in the proof, not those finite tests, establish the theorem for all real parameters and infinite sequences.

## Relationship to prior work
De Carli and Samad [1] introduce this exact fractional discrete-translation group on unweighted \(\ell^2(\mathbb Z)\); their Theorems 4.1 and 4.5 prove the group law and unweighted isometry. They do not determine sharp weighted norms for checkerboard metrics. Ciaurri and collaborators [2] study weighted bounds for discrete Laplacian Riesz transforms and related discrete Hilbert operators, but their weighted boundedness statements do not supply this two-periodic, all-parameter group norm profile. Andersen [3] studies weighted inequalities for discrete Hilbert transforms, a directly relevant precursor with an accessible introductory excerpt; a full-text comparison was not completed, so equivalent hidden consequences of that work remain an originality risk. General finite-fiber/Floquet multiplier principles reduce a periodic-weighted norm to finite matrices, but the explicit continuous-parameter profile, norm-attainment structure and sharp oscillatory conditioning asserted here require the stated calculation and were not located in the compared source statements.

## Limitations
The proof is for the exact kernel and checkerboard weights only, with positive weights and complex square-summable sequences. It does not classify sharp norms for general periodic or nonperiodic weights, nor \(\ell^p\) spaces away from the Hilbert exponent. The general principle of matrix-valued fiber decomposition is classical, and bibliographic searches cannot certify priority; in particular the complete 1977 Andersen article and every possible general multirate theorem were not exhaustively compared. 
## References
[1] L. De Carli and G. Shaikh Samad, *One-parameter groups of operators and discrete Hilbert transforms*, arXiv:1506.03362v1 (first submitted 10 June 2015), https://arxiv.org/abs/1506.03362.

[2] Ó. Ciaurri, T. A. Gillespie, L. Roncal, J. L. Torrea, and J. L. Varona, *Harmonic Analysis associated with a discrete Laplacian*, arXiv:1401.2091 (first submitted 9 January 2014), https://arxiv.org/abs/1401.2091.

[3] K. F. Andersen, *Inequalities with Weights for Discrete Hilbert Transforms*, Canadian Mathematical Bulletin 20 (1977), 9–16, https://doi.org/10.4153/CMB-1977-002-2.
