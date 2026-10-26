# Orthogonal row mixing reverses mean-square stability of geometrically smoothed Kaczmarz momentum

## Finding

Two invertible real systems with the **same normal matrix** and the **same signed-mean iteration** can have opposite mean-square convergence behavior under randomized Kaczmarz with geometrically smoothed momentum (KGSM). This occurs at the same admissible parameters, with exact rational positive-definite growth and decay certificates.

Set
\[
A=\begin{pmatrix}\frac12&0\\0&\frac{\sqrt3}{2}\end{pmatrix},\qquad
Q=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad B=QA.
\]
Both systems are solved with zero right-hand side, and row \(i\) is sampled independently at every step with probability proportional to its squared Euclidean norm. For either matrix, run KGSM with mass \(M=1\), geometric smoothing \(\beta=2/3\), and auxiliary initial condition \(y_0=0\). For the initial error \(x_0=e_1\):

* On \(A\), the expected squared iterate error is exponentially **unbounded**. More precisely, for every integer \(k\ge0\),
\[
\max\{\mathbb E\|x_k\|_2^2,\mathbb E\|x_{k+1}\|_2^2\}\ge
\frac1{41}\left(\frac{101}{100}\right)^k.
\]
* On \(B\), every initial error \(x_0\in\mathbb R^2\) satisfies the explicit **mean-square contraction**
\[
\mathbb E\|x_k\|_2^2\le\frac{34}{5}\left(\frac{527}{532}\right)^k\|x_0\|_2^2.
\]

Yet \(A^{\mathsf T}A=B^{\mathsf T}B=\operatorname{diag}(1/4,3/4)\), so both have the same singular values \(1/2\) and \(\sqrt3/2\). Their expected augmented iterates follow exactly the same stable linear recurrence. An orthogonal change of the *equation rows*, with no change to the normal matrix, reverses second-moment stability.

## Assumptions and scope

KGSM on a consistent system \(Cx=0\), with each row \(a_i^{\mathsf T}\ne0\), is defined by
\[
 x_{k+1}=x_k-\frac{a_{i_k}a_{i_k}^{\mathsf T}}{\|a_{i_k}\|_2^2}x_k+My_k,\qquad
 y_{k+1}=\beta y_k+(1-\beta)(x_{k+1}-x_k),
\]
where independent indices have probabilities \(\mathbb P(i_k=i)=\|a_i\|_2^2/\|C\|_F^2\). We take \(M=1\), \(\beta=2/3\), and \(y_0=0\). These parameters lie in the original KGSM ranges \(0\le M\le1\), \(0\le\beta<1\).

Writing \(P_i=a_ia_i^{\mathsf T}/\|a_i\|_2^2\) and \(z_k=(x_k,y_k)\), the exact one-step matrix is
\[
 z_{k+1}=H(P_{i_k})z_k,\qquad
 H(P)=\begin{pmatrix}I-P&I\\-P/3&I\end{pmatrix}.
\]
The result holds in exact real arithmetic. For any prescribed solution \(x_*\), the same claims hold after translating to \(Cx=Cx_*\) and taking initial error \(x_0-x_*\).

## Proof

**Common normal matrix and signed mean.** The row vectors of \(A\) have squared lengths \(1/4\) and \(3/4\), so its normalized row projectors are the two coordinate projectors, chosen with these respective probabilities. Both rows of \(B\) have squared length \(1/2\); their normalized directions are
\[
 u_\pm=\left(\frac12,\pm\frac{\sqrt3}{2}\right)^{\mathsf T},
\]
chosen equally. The average projector in both cases is
\[
 G=\mathbb E P_i=\begin{pmatrix}1/4&0\\0&3/4\end{pmatrix}.
\]
Consequently \(\mathbb E z_{k+1}=H(G)\mathbb E z_k\) for either system. The two coordinate blocks of \(H(G)\) are
\[
 F_g=\begin{pmatrix}1-g&1\\-g/3&1\end{pmatrix},\qquad g\in\{1/4,3/4\}.
\]
They each have nonreal conjugate eigenvalues, with squared spectral radii \(5/6\) and \(1/2\), respectively. Thus both signed means tend to zero at a geometric rate, despite the second-moment separation below.

**An expanding second-moment certificate for \(A\).** Start with \(x_0=e_1\). Its second coordinate and corresponding auxiliary component stay zero. For the first coordinate, write \(v_k=(x_{k,1},y_{k,1})^{\mathsf T}\). With probability \(3/4\), its row is *not* selected, and with probability \(1/4\), it *is* selected. The respective update matrices are
\[
 H_0=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
 H_1=\begin{pmatrix}0&1\\-1/3&1\end{pmatrix}.
\]
Let \(W=\operatorname{diag}(1/10,1)\). Direct rational multiplication yields
\[
 \frac34H_0^{\mathsf T}WH_0+\frac14H_1^{\mathsf T}WH_1-W
 =\begin{pmatrix}1/360&-1/120\\-1/120&1/10\end{pmatrix}.
\]
Subtracting \(W/100\) gives
\[
 D=\begin{pmatrix}2/1125&-1/120\\-1/120&9/100\end{pmatrix}.
\]
Here \(D_{11}>0\) and \(\det D=163/1800000>0\), hence \(D\succ0\). Conditional expectation therefore gives
\[
 \mathbb E[v_{k+1}^{\mathsf T}Wv_{k+1}]\ge
 \frac{101}{100}\,\mathbb E[v_k^{\mathsf T}Wv_k].
\]
Iterating from \(v_0=(1,0)^{\mathsf T}\) gives
\[
 \mathbb E[v_k^{\mathsf T}Wv_k]\ge\frac1{10}\left(\frac{101}{100}\right)^k.
\]

Moreover, from \(x_{k+1,1}=(1-I_k)x_{k,1}+y_{k,1}\), with \(I_k\in\{0,1\}\),
\[
 \mathbb E[v_k^{\mathsf T}Wv_k]\le\frac{21}{10}\mathbb E x_{k,1}^2+2\mathbb E x_{k+1,1}^2
 \le\frac{41}{10}\max\{\mathbb E x_{k,1}^2,\mathbb E x_{k+1,1}^2\}.
\]
Combining the two bounds proves the claimed exponential lower bound for adjacent iterate errors.

**A contracting second-moment certificate for \(B\).** Reorder the augmented vector as \(w_k=(x_{k,1},y_{k,1},x_{k,2},y_{k,2})^{\mathsf T}\). Write \(\widehat H_\pm\) for \(H(u_\pm u_\pm^{\mathsf T})\) in this order. Define the explicit rational symmetric matrix
\[
 C=\begin{pmatrix}
 34/5&-39/10&0&0\\
 -39/10&384/5&0&0\\
 0&0&26/5&-31/10\\
 0&0&-31/10&88/5
 \end{pmatrix}.
\]
Its two diagonal \(2\times2\) blocks have positive first diagonals \(34/5,26/5\) and positive determinants \(50703/100,8191/100\), so \(C\succ0\). Exact expansion, with the \(\sqrt3\) terms cancelling between the two row choices, gives
\[
 \frac12\widehat H_+^{\mathsf T}C\widehat H_+
 +\frac12\widehat H_-^{\mathsf T}C\widehat H_-=C-I_4.
\]
Therefore \(C\succeq I_4\), and with \(V_k=\mathbb E[w_k^{\mathsf T}Cw_k]\),
\[
 V_{k+1}=V_k-\mathbb E\|w_k\|_2^2
 \le\left(1-\frac1{\operatorname{tr} C}\right)V_k
 =\frac{527}{532}V_k.
\]
For \(y_0=0\), \(V_0\le(34/5)\|x_0\|_2^2\), while \(\mathbb E\|x_k\|_2^2\le V_k\). This proves the displayed mean-square contraction for all \(x_0\).

## Verification

The included `verify.py` uses exact symbolic arithmetic to reconstruct the orthogonal row mixing, the two normalized sampling laws, both positive-definite certificate identities, the exact determinants, and the signed-mean eigenvalue discriminants. Run with Python 3 and SymPy 1.14.0 using `python verify.py`. Its completion message is `VERIFY_OK` followed by a description of the tests. No simulation, finite enumeration, or floating-point spectral approximation is used to prove the infinite-time claims.

## Relationship to prior work

Alderman, Luikart, and Marshall [1] introduced KGSM and established the signed-mean error formula along singular-vector directions. The identical signed means in the present construction are consistent with that theorem. Their analysis does not establish the asserted mean-square equivalence—or stability—under orthogonal row mixing.

The previously published *Exact mean-square stability frontier and a signed-mean blind spot in KGSM* [2] classifies the separate uniform orthonormal model \(A=I_2\). It expressly does not classify nonorthogonal systems or nonuniform row probabilities. Our two matrices have unequal singular values, one frame uses nonuniform sampling, and the second uses non-coordinate row projectors. Its uniform-frame stability classification therefore does not imply the paired opposite-stability conclusion.

The classic randomized Kaczmarz mean-square contraction [3] concerns the unaccelerated method. Other stochastic heavy-ball convergence analyses [4] impose different momentum recurrences or furnish sufficient conditions; those conclusions do not imply this exact same-Gram stability reversal.

## Limitations

The phenomenon is proved for the specified two-dimensional pair, exact norm-squared row sampling, \(M=1\), \(\beta=2/3\), and exact arithmetic. It is not a complete stability classification for arbitrary frames or parameters, nor an assertion of samplewise divergence. Signed-mean stability and mean-square stability are different properties. While the linear-system objective is the same after row rotation, sampling the transformed equations changes the distribution of the random projection matrices.

## References

1. S. J. Alderman, R. W. Luikart, N. F. Marshall, *Randomized Kaczmarz with Geometrically Smoothed Momentum*, arXiv:2401.09415v1 (first public 2024-01-17), especially equation (9), Theorem 1.1, and Remark 1.1. https://arxiv.org/html/2401.09415
2. *Exact mean-square stability frontier and a signed-mean blind spot in KGSM*, published mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-mean-square-stability-frontier-and-a-signed-mean-blind-spo--e15c00248209
3. T. Strohmer, R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, Journal of Fourier Analysis and Applications 15 (2009), 262–278.
4. N. Loizou, P. Richtárik, *Momentum and Stochastic Momentum for Stochastic Gradient, Newton, Proximal Point and Subspace Descent Methods*, arXiv:1712.09677 (2017).
