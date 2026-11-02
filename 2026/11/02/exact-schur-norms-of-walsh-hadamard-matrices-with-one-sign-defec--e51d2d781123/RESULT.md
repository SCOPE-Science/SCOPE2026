# Exact Schur norms of Walsh–Hadamard matrices with one sign defect

## Finding
For every integer \(d\ge3\), put \(N=2^d\). On the binary vector space \(V=\mathbb F_2^d\), let \(H_{xy}=(-1)^{\langle x,y\rangle}\), and change only its \((0,0)\) entry from \(+1\) to \(-1\) to obtain \(M\). For complex \(N\)-by-\(N\) matrices, write \(S_M(X)=M\circ X\), with the norm induced by the ordinary spectral operator norm on both sides.

Set \(s_N=\sqrt{N(N+2)}\) and \(t_N=2s_N-(2N+1)\). Then \(0<t_N<1\) and
\[
 \boxed{\|S_M\|=\sqrt N\,\frac{s_N-2}{2N-s_N}.}
\]
An optimizing pair for the dual trace-norm characterization consists of equal probability vectors with mass \(t_N/(t_N+N-1)\) at zero and mass \(1/(t_N+N-1)\) at every nonzero vector. In particular,
\[
 \sqrt N-\|S_M\|=N^{-3/2}+O(N^{-7/2})\qquad(N\to\infty\text{ through powers of two}).
\]
Thus a single flipped sign destroys exact Hadamard extremality but reduces the Schur multiplier norm by an exactly computable, asymptotically tiny amount. The same value holds for a single sign flip at any other location of \(H\), by row/column sign switchings and permutations.

## Assumptions and scope
The ambient norm is the complex matrix operator norm, not the entrywise norm, Hilbert–Schmidt norm, or the norm of the sign matrix as an operator. All entries of \(M\) belong to \(\{-1,1\}\). The displayed closed form is asserted for dyadic orders \(N\ge8\). The formulas and proof also evaluate orders two and four, but the order-four value is already represented in the published classification of small real sign matrices and is not claimed as a new result.

## Proof
**1. A dual characterization and concavity.** For every real matrix \(M\), operator-norm duality gives
\[
\|S_M\|=\max_{p,q\in\Delta_N}\left\|\operatorname{diag}(\sqrt p)M\operatorname{diag}(\sqrt q)\right\|_1,
\]
where \(\Delta_N\) is the probability simplex and \(\|\cdot\|_1\) is the nuclear norm. Indeed, write the matrix operator norm as a supremum of \(|u^*(M\circ X)v|\) over unit vectors \(u,v\), then maximize over \(\|X\|\le1\). The resulting nuclear norm has entries \(\overline u_iM_{ij}v_j\); diagonal phase conjugations eliminate all phases, leaving \(p_i=|u_i|^2\), \(q_j=|v_j|^2\).

Call the expression on the right \(F(p,q)\). It equals the matrix fidelity
\[
\operatorname{Tr}\sqrt{A^{1/2}BA^{1/2}},\quad A=\operatorname{diag}(p),\quad B=M\operatorname{diag}(q)M^T.
\]
It is jointly concave in \((p,q)\). For positive-definite \(A,B\), this follows from the variational formula
\[
\operatorname{Tr}\sqrt{A^{1/2}BA^{1/2}}=
\inf_{Z>0}\frac12\bigl(\operatorname{Tr}(AZ)+\operatorname{Tr}(BZ^{-1})\bigr).
\]
For fixed \(Z\), the right-hand expression is affine in \((A,B)\), and an infimum of affine functions is concave. The formula follows on substituting \(Y=A^{1/2}ZA^{1/2}\) and minimizing \(\operatorname{Tr}Y+\operatorname{Tr}((A^{1/2}BA^{1/2})Y^{-1})\) at its positive square root. Positive-semidefinite boundary cases follow by regularization and continuity.

**2. Two-orbit reduction.** For every \(L\in\mathrm{GL}(d,2)\), simultaneously permuting rows by \(x\mapsto Lx\) and columns by \(y\mapsto L^{-T}y\) preserves \(H\) and the defect at zero. Both actions have just two orbits, \(\{0\}\) and \(V\setminus\{0\}\). Average \((p,q)\) over these symmetries: joint concavity cannot decrease \(F\). Moreover, \(M=M^T\), so exchanging the two averaged vectors also preserves \(F\); taking their midpoint cannot decrease it. A global maximizer therefore has \(p=q\), with one mass at zero and a common mass on the remaining \(N-1\) points. Write those masses as \(p_0=t/(t+N-1)\) and \(p_x=1/(t+N-1)\) for \(x\ne0\), with \(t\ge0\); the one-point extreme case is obtained as \(t\to\infty\).

**3. Exact nuclear norm.** Scale \(D_p^{1/2}MD_p^{1/2}\) by \(t+N-1\), and denote the resulting symmetric matrix by \(C\). Its \((0,0)\) entry is \(-t\), its entries joining zero to nonzero indices are \(\sqrt t\), and its nonzero-index block is the corresponding Walsh submatrix \(K\). Walsh orthogonality gives
\[
\sum_{z\ne0}K_{xz}K_{yz}=N\mathbf1_{x=y}-1,\qquad
\sum_{z\ne0}K_{xz}=-1\quad(x,y\ne0).
\]
Consequently \(CC^T\) has eigenvalue \(N\) with multiplicity \(N-2\), and on the span of the zero coordinate and the normalized all-ones vector on the remaining indices, it has matrix
\[
\begin{pmatrix}
 t(t+N-1)&-(t+1)\sqrt{t(N-1)}\\
 -(t+1)\sqrt{t(N-1)}&1+(N-1)t
\end{pmatrix}.
\]
The latter matrix has determinant \(t^2(N-2)^2\). Hence the sum of its two nonnegative square-root eigenvalues is \(\sqrt{t^2+(4N-6)t+1}\). It follows that
\[
F(t)=\frac{(N-2)\sqrt N+\sqrt{t^2+(4N-6)t+1}}{t+N-1}.
\]
This equality also holds by continuity at \(t=0\).

**4. Unique optimizing ratio.** For \(N>2\), differentiate \(F(t)\). Its derivative has the sign of
\[
2N-1-t-\sqrt N\sqrt{t^2+(4N-6)t+1}.
\]
This expression is strictly decreasing on \([0,\infty)\), positive at zero and negative for large \(t\), so has exactly one zero. Squaring the defining equation (whose two sides are positive at the root) yields
\[
t^2+2(2N+1)t-(4N-1)=0,
\]
with positive root \(t_N=2\sqrt{N(N+2)}-(2N+1)\). Direct substitution into \(F(t)\) yields the boxed closed form. Elementary squaring shows \(0<t_N<1\) for \(N\ge4\). The asymptotic difference follows by expanding \(\sqrt{1+2/N}\) in the closed form; more precisely, it begins \(N^{-3/2}+\tfrac34N^{-7/2}\).

**5. Location invariance.** For a flipped entry \((a,b)\), translate the row index by \(a\) and the column index by \(b\). The transformed Walsh entries differ from \(H\) only by signs depending separately on their row and column, and a global sign. These switchings do not change a Schur multiplier norm, because they amount to diagonal unitary multiplications on input/output. The flipped entry is transported to \((0,0)\), so its norm is the same.

## Verification
Run `python3 CHECK.py` with Python 3.10 or later (standard library only). The program verifies Walsh orthogonality in small orders, compares the reduced closed form with direct Jacobi-eigenvalue nuclear norms, checks strict local optimality, tests non-symmetric random weights, and checks asymptotic inequalities. It reports 560 passing assertions. Finite numerical tests do not establish the all-dimensional theorem; Steps 1–5 above are the proof.

## Relationship to prior work
Holbrook, Johnston, and Schoch (arXiv:2206.02863v1, posted 2022-06-06) prove the general \(\sqrt N\) upper bound for sign-matrix Schur multiplier norms, characterize its equality via Hadamard matrices, and calculate small sign-matrix classes; the order-four special value occurs there. Their discussion does not provide the displayed exact norm and optimizer for a one-entry defect in all dyadic orders. Davidson and Donsig (arXiv:math/0506073v1) give foundational Schur multiplier norm and symmetry results, including exact computations under transitive actions. Their transitive-action formula does not immediately apply to this two-orbit defect pattern; the concavity-and-two-orbit argument above supplies the missing reduction. Christensen (arXiv:2505.24670v2) gives an implicit variational characterization for every self-adjoint Schur multiplier, applicable to this symmetric matrix, but does not evaluate the Walsh single-defect family or its sharp asymptotic. An equivalent formula in differently phrased factorization, matrix-balancing or near-Hadamard literature cannot be ruled out without further independent literature review.

## Limitations
The claim is specific to Sylvester/Walsh Hadamard matrices, a single defect, complex operator-norm Schur multipliers, and powers of two. It does not give exact norms for multiple simultaneous defects, arbitrary inequivalent Hadamard matrices, or other Schatten classes. Independently published confirmation of priority has not been established.

## References
- J. Holbrook, N. Johnston, J.-P. Schoch, *Real Schur norms and Hadamard matrices*, arXiv:2206.02863v1 (2022), https://arxiv.org/abs/2206.02863 .
- K. R. Davidson, A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073v1 (2005), https://arxiv.org/abs/math/0506073 .
- E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670v2 (2026 revision; originally posted 2025), https://arxiv.org/abs/2505.24670 .
