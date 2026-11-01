# Sharp one-hole second-difference Fourier inequality and compulsory phase reversal

## Finding
Let \(L,R\ge1\) be integers and \(d=L+R+1\). For an analytic trigonometric polynomial \(P(e^{it})=\sum_{j=1}^{d}a_j e^{i(j-1)t}\) with the internal coefficient \(a_{L+1}=0\), the sharp estimate is
\[
\sum_{j=1}^{d}|a_j|\le \mathcal C_{L,R}\left(\frac{1}{2\pi}\int_0^{2\pi}|1-e^{it}|^4|P(e^{it})|^2\,dt\right)^{1/2}.
\]
Define, for each positive integer \(n\),
\[
S_n=\frac16\binom{n+4}{5},\qquad t_n=\frac{n(n+1)}{12},\qquad p_n=\frac{n(n+1)}{(n+2)(n+3)}.
\]
Then the exact best constant is
\[
\boxed{\mathcal C_{L,R}^2=S_L+S_R+\frac{p_Rt_L^2+p_Lt_R^2+2t_Lt_R}{1-p_Lp_R}.}
\]
Every nonzero equality case is a complex scalar multiple of one real polynomial whose coefficients before the hole are strictly positive and whose coefficients after the hole are strictly negative. Thus a forced internal Fourier-coefficient zero creates a compulsory relative phase of \(\pi\) between the two coefficient blocks, independently of their lengths.

## Assumptions and scope
The coefficients are arbitrary complex numbers; the sole constraint is the exact vanishing \(a_{L+1}=0\). Both blocks are nonempty, and the Fourier integral is normalized by \(1/(2\pi)\). Neither asymptotics nor an assumption on the remaining coefficients is required.

Set \(H_n=(h_{ij})_{1\le i,j\le n}\), where \(h_{ii}=6\), \(h_{i,i\pm1}=-4\), \(h_{i,i\pm2}=1\), and all other entries vanish. Let \(G_n=H_n^{-1}\), \(\mathbf1_n\) be the all-ones vector, and \(e_j\) be the corresponding coordinate vector. Introduce the strictly positive vectors
\[
U_{n,j}=\frac{j(j+1)(n+1-j)(n+2-j)}{24},\qquad
V_{n,j}=\frac{j(j+1)(n+1-j)}{(n+2)(n+3)},\quad 1\le j\le n.
\]
An explicit unique equality vector is \((x_1,\ldots,x_L,0,-y_1,\ldots,-y_R)\), up to nonzero complex scalar, where
\[
x_j=U_{L,j}+\frac{p_Rt_L+t_R}{1-p_Lp_R}V_{L,j},\qquad
 y_k=U_{R,k}+\frac{p_Lt_R+t_L}{1-p_Lp_R}V_{R,R+1-k}.
\]
For example, \(\mathcal C_{1,1}^2=2/5\) and \(\mathcal C_{2,2}^2=19/7\).

## Proof
**1. Fourier reduction and the one-hole matrix.** Extend the coefficient sequence by zero to all integers and let \((\Delta^2a)_j=a_j-2a_{j-1}+a_{j-2}\). Parseval makes the squared integral exactly \(\sum_{j=1}^{d+2}|(\Delta^2a)_j|^2\). The coefficient quadratic form of this energy is the Hermitian Toeplitz matrix with five diagonals \(6,-4,1\). Removing the row and column indexed by \(L+1\) yields two diagonal blocks \(H_L,H_R\) and precisely one inter-block matrix entry, equal to \(+1\), between the last left coefficient and the first right coefficient. Upon writing the right coefficients with a minus sign, the energy has Gram matrix
\[
M=\begin{pmatrix}H_L&-e_Le_1^{\mathsf T}\\-e_1e_L^{\mathsf T}&H_R\end{pmatrix}.
\]
This matrix is positive definite because it is a principal submatrix of the difference Gram matrix with an invertible diagonal sign conjugation.

**2. Positivity of the fourth-difference Green matrices.** Let \(B_n\) be the \((n+2)\)-by-\(n\) matrix with the three lower diagonals \(1,2,1\). The sign-alternation matrix \(E_n=\mathrm{diag}((-1)^1,\ldots,(-1)^n)\) satisfies \(K_n=E_nH_nE_n=B_n^{\mathsf T}B_n\). The matrix \(B_n\) factors into two rectangular lower bidiagonal matrices, each with nonnegative minors; hence every minor of \(B_n\) is nonnegative, and all minors of \(K_n\) are nonnegative by Cauchy--Binet. More precisely, consider a cofactor of \(K_n\) deleting row \(i\) and column \(j\), with \(i\le j\). In Cauchy--Binet take the intermediate row set \([n]\setminus\{i\}\). For the leading \(n\)-by-\(n\) lower-triangular submatrix \(B_n^0=(I+S)^2\), this term is
\[
\det B_n^0[\widehat i,\widehat i]\,\det B_n^0[\widehat i,\widehat j]
=1\cdot(j-i+1)>0.
\]
Indeed \(\det B_n^0=1\), and \(((B_n^0)^{-1})_{j,i}=(-1)^{j-i}(j-i+1)\) by the binomial series for \((I+S)^{-2}\); the complementary-minor identity gives the displayed minor. Symmetry handles \(i>j\). Consequently every cofactor minor of \(K_n\) is strictly positive. Cramer's rule implies \(K_n^{-1}\) has the checkerboard sign pattern and hence
\[
(G_n)_{ij}=(E_nK_n^{-1}E_n)_{ij}>0\qquad(1\le i,j\le n).
\]

**3. Two explicit Green responses.** Direct application of the five-point fourth-difference stencil gives
\[
H_nU_n=\mathbf1_n,\qquad H_nV_n=e_n.
\]
For the first identity, the defining quartic has zeros at \(-1,0,n+1,n+2\), so its fourth difference is identically one, including the boundary rows. For the second, the defining cubic has zeros at \(-1,0,n+1\), so all interior fourth differences vanish, and the extra endpoint truncation contributes one in the last row. The identities also hold directly for \(n=1,2\). By reflection, \(G_ne_1=(V_{n,n+1-j})_{j=1}^n\). Summing the quartic and reading endpoint entries yields
\[
\mathbf1_n^{\mathsf T}G_n\mathbf1_n=S_n,\qquad e_n^{\mathsf T}G_n\mathbf1_n=t_n,\qquad e_n^{\mathsf T}G_ne_n=p_n.
\]
Here \(0<p_n<1\) for every positive integer \(n\).

**4. The rank-one bridge.** The block Schur-complement identity, using \(p_Lp_R<1\), gives
\[
M^{-1}=\begin{pmatrix}
G_L+\frac{p_R}{1-p_Lp_R}G_Le_Le_L^{\mathsf T}G_L & \frac{G_Le_Le_1^{\mathsf T}G_R}{1-p_Lp_R}\\
\frac{G_Re_1e_L^{\mathsf T}G_L}{1-p_Lp_R} & G_R+\frac{p_L}{1-p_Lp_R}G_Re_1e_1^{\mathsf T}G_R
\end{pmatrix}.
\]
Every entry is strictly positive by Step 2. Taking the all-ones quadratic form and inserting the identities of Step 3 yields precisely the displayed formula for \(\mathcal C_{L,R}^2\). Multiplying this inverse by the all-ones vector gives the explicit positive components \(x_j,y_k\) in the statement.

**5. Sharpness and complete equality classification.** For arbitrary complex coefficient blocks in sign-flipped coordinates, select a phase vector \(\sigma\) with entries on the unit circle so that \(\sigma^*w=\|w\|_1\). Matrix Cauchy--Schwarz gives
\[
\|w\|_1^2\le(\sigma^*M^{-1}\sigma)(w^*Mw)
\le(\mathbf1^*M^{-1}\mathbf1)(w^*Mw).
\]
The second inequality holds because all entries of \(M^{-1}\) are positive. Equality in it forces all phases of \(\sigma\) to coincide; equality in Cauchy--Schwarz then forces \(w\) to be a complex scalar multiple of \(M^{-1}\mathbf1\). Conversely this vector attains equality. Restoring the minus sign on the right block gives the claimed strict phase reversal and uniqueness up to scalar.

## Verification
The standalone `verify.py` performs exact-rational checks of both Green responses, strict inverse-entry positivity for the first eighteen block lengths, and the closed-form two-block constant and optimizer positivity for all 64 block pairs with lengths between one and eight. These finite tests are reproducibility checks, not substitutes for the general positivity proof and Schur complement above. One can execute it using `python verify.py` after installing SymPy.

## Relationship to prior work
Hindov, Nitzan, Olsen, and Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences* (arXiv:2610.19010v1, 13 October 2026), compute the sharp **unconstrained** Fourier-coefficient \(\ell^1\)-to-weighted-\(L^2\) constant for every positive integer difference order, with discrete Landau extremizers. Their Theorem 1 does not impose a missing internal coefficient; their auxiliary real-rooted polynomial sign structures concern left inverses of the full difference operator. The present theorem determines instead the exact constrained sharp constant for a single arbitrary internal hole at second order, together with a compulsory relative phase change across the hole. The unrestricted sharp constant at this order and total length \(d\) is \(\binom{d+4}{5}/6\), which is generally strictly larger than the constrained value; it does not imply the formula or optimizer classification here. Yamagishi and Nagai (2022) analyze second-order discrete Dirichlet boundary problems for pointwise maxima, a distinct norm and boundary-value setup.

## Limitations
The result addresses precisely one missing **internal** coefficient and the second difference; it does not assert formulas for multiple holes, other difference orders, or other right-side norms. Published-literature searches and the inspected sources did not disclose an equivalent one-hole formula, but search incompleteness and a possible earlier implicit Green-function derivation remain originality risks. The formulas are exact for all stated finite lengths; no continuum asymptotic or Gabor-frame implication is claimed.

## References
1. R. Hindov, S. Nitzan, J.-F. Olsen, and E. Rydhe, *A sharp discrete Sobolev inequality and left inverses of higher order differences*, arXiv:2610.19010v1 (13 October 2026), https://arxiv.org/html/2610.19010v1.
2. H. Yamagishi and A. Nagai, *The best constant of discrete Sobolev inequality corresponding to a discrete bending problem of a string*, Saitama Math. J. 34 (2022), 19--46, https://www.rimath.saitama-u.ac.jp/research/pdf/smj34-2.pdf.
