# A universal one-defect Schur norm law for Hadamard matrices

## Finding
Let \(H\) be any real Hadamard matrix of order \(n\ge 2\): all entries are signs and \(HH^{\mathsf T}=nI\). Change the sign of **exactly one** entry to obtain \(B\). For the Schur multiplier \(S_B(A)=B\circ A\) on \(M_n(\mathbb C)\) with its usual spectral operator norm, the exact induced norm is
\[
\boxed{\|S_B\|=\gamma_n:=\frac{(n-2)\sqrt n+2(n-1)\sqrt{n+2}}{3n-2}=\sqrt n-\frac{2}{n\sqrt n+(n-1)\sqrt{n+2}}.}
\]
The value depends only on the order, not on the Hadamard equivalence class, the location of the changed entry, or the original sign. A real orthogonal matrix attains the norm. The exact loss from the sharp Hadamard value \(\sqrt n\) is positive and asymptotic to \(n^{-3/2}\). The order-four specialization \((2+3\sqrt6)/5\) is **previously known**; the all-order formula and the common construction of matching lower and upper witnesses are the findings assessed here.

## Assumptions and scope
The claim holds for every actually existing real Hadamard matrix; it does not assume existence in every multiple-of-four order. Matrices carry the (unnormalized) Euclidean spectral norm \(\|A\|=\sup_{\|x\|_2=1}\|Ax\|_2\). The Schur norm is \(\sup_{A\ne0}\|B\circ A\|/\|A\|\), with arbitrary complex test matrices. Entrywise permutations and independent row/column sign changes preserve this norm. The case \(n=2\) is elementary: a one-entry flip produces a rank-one sign matrix, whose Schur multiplier is an isometry of operator norm one; the formula also gives one. Hence the proof below assumes \(n\ge4\), the only other possible Hadamard orders.

## Proof
**1. Normal form and invariant decomposition.** Permute the changed entry to the first row and column. Multiply rows and columns of the original \(H\) by signs to arrange its first row and column equal to \(+1\), without moving the defect. The changed matrix has the form
\[
B=\begin{pmatrix}-1&\mathbf1^{\mathsf T}\\ \mathbf1&C\end{pmatrix},
\qquad C\mathbf1=C^{\mathsf T}\mathbf1=-\mathbf1,
\qquad CC^{\mathsf T}=C^{\mathsf T}C=nI-\mathbf1\mathbf1^{\mathsf T}.
\]
Here \(C\) has order \(n-1\). Put \(u=\mathbf1/\sqrt{n-1}\) and \(W=u^\perp\). With respect to \(\mathbb Re_1\oplus\mathbb Ru\oplus W\), the matrix \(B\) preserves these summands as a two-dimensional block and its complementary block:
\[
J=\begin{pmatrix}-1&\sqrt{n-1}\\\sqrt{n-1}&-1\end{pmatrix},
\qquad C_W^{\mathsf T}C_W=nI_W.
\]
The restriction \(C_W\) need not be symmetric; its singular values are all \(\sqrt n\). The block \(J\) is invertible for \(n\ge4\).

**2. A sharp lower bound.** Choose \(0<b<1/(n-1)\), set \(t=1-(n-1)b\), and define the probability diagonal \(D=\operatorname{diag}(\sqrt t,\sqrt b,\ldots,\sqrt b)\). In the same splitting, \(M=DBD\) acts on the first two modes as
\[
K=\begin{pmatrix}-t&\sqrt{(n-1)tb}\\\sqrt{(n-1)tb}&-b\end{pmatrix}
\]
and on \(W\) as \(bC_W\). Since \(\det K=-(n-2)tb<0\), the sum of absolute eigenvalues of \(K\) is
\[
R(b)=\sqrt{(t-b)^2+4(n-1)tb}=\sqrt{1+2(n-2)b-(n-2)(3n-2)b^2}.
\]
Consequently
\[
\|DBD\|_* = F(b):=(n-2)\sqrt n\,b+R(b).
\]
This is a lower bound for \(\|S_B\|\). Indeed, take a real orthogonal polar factor \(A\) of the invertible real matrix \(M\), chosen to satisfy \(\operatorname{tr}(A^{\mathsf T}M)=\|M\|_*\). For the unit vector \(v=(\sqrt t,\sqrt b,\ldots,\sqrt b)\),
\[
\|S_B\|\ge\|B\circ A\|\ge v^{\mathsf T}(B\circ A)v=\operatorname{tr}(A^{\mathsf T}DBD)=F(b).
\]
Differentiation gives \(F'(b)=(n-2)[\sqrt n+(1-(3n-2)b)/R(b)]\). Its zero in the allowed interval is
\[
b_* =\frac{1+2\sqrt{n/(n+2)}}{3n-2},\qquad t_*=1-(n-1)b_*>0.
\]
One may verify \((3n-2)b_*-1=\sqrt n R(b_*)\); the derivative changes from positive to negative there, since \(R\) is strictly concave on the interval. Substitution yields \(F(b_*)=\gamma_n\) as displayed above.

**3. A matching positive Gram factorization.** With \(b=b_*\), \(t=t_*\), and \(R=R(b_*)\), define a real symmetric operator \(X\) by declaring its two-dimensional block on \(\mathbb Re_1\oplus\mathbb Ru\) to be
\[
X_2=\frac1R\begin{pmatrix}
t+(2n-3)b&-(t+b)\sqrt{n-1}\\
-(t+b)\sqrt{n-1}&b+(2n-3)t
\end{pmatrix}
\]
and its block on \(W\) to be \(\sqrt n\,I_W\). More conceptually, if \(D_2=\operatorname{diag}(\sqrt t,\sqrt b)\), then \(X_2=D_2^{-1}|K|D_2^{-1}\); this proves \(X\) is strictly positive. The identity \(K|K|^{-1}K=|K|\), together with \(C_W^{\mathsf T}C_W=nI_W\), gives exactly
\[
B^{\mathsf T}X^{-1}B=X.
\]
The diagonal in the original vertex basis has two kinds of entries:
\[
X_{11}=\frac{t+(2n-3)b}{R},\quad
X_{ii}=\frac{b+(2n-3)t+(n-2)\sqrt n\,R}{(n-1)R}\ (2\le i\le n).
\]
Their difference is \((n-2)[(3n-2)b-1-\sqrt n R]/((n-1)R)=0\) at \(b=b_*\). Hence every diagonal entry equals a common \(\gamma\). Since \(X=D^{-1}|DBD|D^{-1}\), its weighted diagonal trace satisfies \(\gamma=\operatorname{tr}(D^2X)=\|DBD\|_*=F(b_*)=\gamma_n\).

For each \(i,j\), put \(x_i=X^{1/2}e_i\) and \(y_j=X^{-1/2}Be_j\). Then
\[
B_{ij}=\langle x_i,y_j\rangle,\quad
\|x_i\|_2^2=X_{ii}=\gamma_n,\quad
\|y_j\|_2^2=(B^{\mathsf T}X^{-1}B)_{jj}=\gamma_n.
\]
The Schur factorization inequality therefore yields \(\|S_B\|\le\sup_i\|x_i\|_2\sup_j\|y_j\|_2=\gamma_n\), valid on complex matrices too. Combined with the lower bound, this proves exact equality and the existence of a real orthogonal norm witness.

**4. Exact deficit.** Rationalizing the sharp constant yields \(\sqrt n-\gamma_n=2/[n\sqrt n+(n-1)\sqrt{n+2}]>0\), which is \(n^{-3/2}+O(n^{-5/2})\) as \(n\to\infty\) along existing Hadamard orders.

## Verification
The standalone Python 3 program `verify_hadamard.py` constructs independent Sylvester Hadamard matrices of orders \(4,8,16,32\) and Paley Hadamard matrices of orders \(12,20\). Using double-precision NumPy, it compares the formula against the trace-norm lower witness, checks positive definiteness, diagonal equality and the full Gram identity \(B^{\mathsf T}X^{-1}B=X\), and tests further probability-weight perturbations. It also checks the exact radical identity over integer orders \(4\) to \(200\). A successful replay reported **521 supplementary assertions**. These finite checks do not establish the general result; the algebraic argument above is the proof. Run `OPENBLAS_NUM_THREADS=1 python verify_hadamard.py` with NumPy installed.

## Relationship to prior work
Holbrook, Johnston and Schoch, *Real Schur norms and Hadamard matrices* (public preprint 2022-06-06), prove \(\|S_H\|=\sqrt n\) for Hadamard sign matrices and characterize equality. Their explicit \(4\times4\) class \(M_8\) is equivalent to a one-entry-flipped Hadamard matrix and has the **already-known** value \((2+3\sqrt6)/5\); the order-four instance is therefore not new. Their general semidefinite approach calculates individual finite norms but does not, in the inspected text, assert the uniform formula above for every existing Hadamard order. Davidson and Donsig give the classical Schur-factorization equivalences and exact calculations for other symmetric patterns; Cowen and collaborators give general optimization algorithms and factorizations for Hadamard (entrywise) multipliers. Christensen studies optimal Schur factorizations more generally. These methods are background, not claimed as new. A separate older article titled *Norms of Hadamard Multipliers* by Cowen, Dritschel and Penney was not inspected in full; implicit or explicit earlier coverage remains a historical-priority risk.

## Limitations
The theorem is conditional on existence of the initial Hadamard matrix and treats **exactly one** changed entry. It does not give an exact law for two or more defects, non-Hadamard starting matrices, or arbitrary sign patterns. The one-entry defect value at order four was previously published. The present review is not independent validation and cannot eliminate the possibility of equivalent results elsewhere in the older literature. Numerical verification is supplementary only.

## References
- J. Holbrook, N. Johnston, J.-P. Schoch, *Real Schur norms and Hadamard matrices*, arXiv:2206.02863, first arXiv posting June 6, 2022. Full text: https://www.njohnston.ca/wp-content/uploads/2023/05/real_schur_norms_hadamard_matrices.pdf .
- K. R. Davidson, A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073 (2005).
- C. C. Cowen, P. A. Ferguson, D. K. Jackman, E. A. Sexauer, C. Vogt, H. J. Woolf, *Finding Norms of Hadamard Multipliers*, lawful full text: https://www.math.purdue.edu/~cowen/Downloads/HadNorm.pdf .
- E. Christensen, *Unique Matrix Factorizations Associated to Bilinear Forms and Schur Multipliers*, arXiv:2309.17092 (2023).
- C. C. Cowen, M. A. Dritschel, R. C. Penney, *Norms of Hadamard Multipliers* (1994), identified as a plausibly related older source; full text not examined.
