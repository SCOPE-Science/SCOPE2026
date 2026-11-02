# Sharp Schur norms for partially flipped diagonal sign matrices

## Finding
For integers \(n\ge 1\) and \(0\le k\le n\), let \(M_{n,k}\) denote the real symmetric \(n\times n\) sign matrix with all entries \(+1\), except that its first \(k\) diagonal entries are \(-1\). Let \(S_{n,k}(A)=M_{n,k}\circ A\), acting on complex matrices with their spectral operator norm. Its exact operator norm is
\[
\|S_{n,k}\|=\begin{cases}
1,&k=0,\\
1,&n=k=1,\\
3-4/k,&n=k\ge2,\\
1+\dfrac{k}{1+\sqrt{2k}},&1\le k<n,\quad k\le5,\\
3-4/k,&6\le k<n.
\end{cases}
\]
In particular, for \(k\ge2\), adjoining one all-positive row and column to the \(k\times k\) diagonal sign reflection strictly raises the Schur norm for \(2\le k\le5\), but **never** for \(k\ge6\). Adding further all-positive rows/columns has no additional effect. The strict raising statement also holds at \(k=1\), where the unextended multiplier norm is \(1\) and the extended norm is \(\sqrt2\).

The theorem gives explicit matching lower-bound contractions and positive-semidefinite Gram certificates for every size, without relying on numerical optimization.

## Assumptions and scope
All matrices are over \(\mathbb C\). The domain and codomain of the Schur map are both \(B(\mathbb C^n)\), equipped with \(\|A\|_{\mathrm{op}}\), and \(\|S_{n,k}\|=\sup_{\|A\|_{\mathrm{op}}\le1}\|M_{n,k}\circ A\|_{\mathrm{op}}\). We do not use normalized Schatten norms. The real symbol has the same stated multiplier norm on complex matrices because the upper bound holds over \(\mathbb C\), while the lower witness is real symmetric.

Write \(J_k\) for the all-one matrix and \(\mathbf1_k\) for its all-one vector. When \(k=n\), \(M_{k,k}=J_k-2I_k\). When \(n>k\), all \(n-k\) unflipped rows are identical (and likewise the columns), allowing reduction to exactly one unflipped coordinate.

## Proof
**1. Two elementary multiplier estimates.** Suppose \(M=M^*\) and a real symmetric matrix \(P\) has diagonal \(T\) everywhere and satisfies \(P\pm M\succeq0\). Then \(Q^\pm=(P\pm M)/2\) are Gram matrices of vectors \(v_i^\pm\). Put \(x_i=(v_i^+,v_i^-)\) and \(y_i=(v_i^+,-v_i^-)\). Thus \(\langle x_i,y_j\rangle=M_{ij}\) and \(\|x_i\|=\|y_i\|=\sqrt{T}\). With \(Ve_j=e_j\otimes y_j\) and \(We_i=e_i\otimes x_i\), the identity \(S_M(A)=W^*(A\otimes I)V\) gives \(\|S_M\|\le T\). This directly proves the needed Gram-factorization bound.

Conversely, for any nonnegative unit vector \(u\), set \(B=\operatorname{diag}(u)M\operatorname{diag}(u)\). Take the real symmetric contraction \(A=\operatorname{sgn}(B)\), defining its sign as zero on its nullspace. Then
\[
\|S_M\|\ge u^\top(M\circ A)u=\operatorname{tr}(BA)=\operatorname{tr}|B|.
\]
Both estimates are valid for the complex operator norm.

**2. Exact norm on the fully flipped core.** For \(k\ge2\), choose \(u=k^{-1/2}\mathbf1_k\). The matrix \(\operatorname{diag}(u)M_{k,k}\operatorname{diag}(u)\) has eigenvalue \((k-2)/k\) once and \(-2/k\) with multiplicity \(k-1\). Its trace norm is \(3-4/k\). For the matching upper bound set \(T=3-4/k\) and \(P=2I_k+(T-2)J_k\); then \(P+M_{k,k}=(T-1)J_k\succeq0\), while \(P-M_{k,k}=4I_k+(T-3)J_k\succeq0\), the latter having eigenvalues \(4\) on the zero-sum subspace and \(0\) on constants. For \(k=1\) the multiplier acts by a sign and has norm \(1\).

**3. Lower bound with one unflipped coordinate.** For \(n=k+1\), choose a unit vector with its first \(k\) coordinates equal to \(\sqrt{a/k}\) and its last equal to \(\sqrt{1-a}\), \(0\le a\le1\). In the centered subspace of the first \(k\) coordinates, the matrix \(B\) from step 1 has eigenvalue \(-2a/k\), repeated \(k-1\) times. On the span of the constant vector and the new coordinate it is
\[
\begin{pmatrix}a(1-2/k)&\sqrt{a(1-a)}\\\sqrt{a(1-a)}&1-a\end{pmatrix}.
\]
Its determinant is \(-2a(1-a)/k\); therefore the witness gives
\[
F_k(a)=\frac{2(k-1)}k a+\sqrt{1+\frac{4a}k-\frac{4(2k-1)}{k^2}a^2}.
\]
For \(1\le k\le5\), elementary differentiation gives an admissible maximizer
\[
a_k=\frac{k+(k-1)\sqrt{2k}}{2(2k-1)}\in[0,1],
\qquad F_k(a_k)=1+\frac{k}{1+\sqrt{2k}}.
\]
For \(k\ge6\), the critical point lies above \(1\), the function is increasing on \([0,1]\), and \(F_k(1)=3-4/k\). The \(k=1\) formula yields \(a_1=1/2\) and \(\sqrt2\).

**4. Matching upper certificate for one unflipped coordinate.** If \(k=1\), the two-by-two sign matrix has eigenvalues \(\pm\sqrt2\), so \(P=\sqrt2 I_2\) satisfies \(P\pm M_{2,1}\succeq0\).

For \(k\ge2\), define the candidate \(T\) by the displayed theorem, put \(s=T-1\), and let \(v=(k-1)s/k\) for \(2\le k\le5\), or \(v=1\) for \(k\ge6\). Set
\[
P=\begin{pmatrix}
2I_k+(T-2)J_k&v\mathbf1_k\\
v\mathbf1_k^{\top}&T
\end{pmatrix}.
\]
Its diagonal is exactly \(T\). On the first-block zero-sum subspace, the eigenvalues of \(P+M\) and \(P-M\) are \(0\) and \(4\), respectively. On the remaining two-dimensional subspace, their matrices are
\[
\begin{pmatrix}k(T-1)&\sqrt{k}(v+1)\\\sqrt{k}(v+1)&T+1\end{pmatrix},\qquad
\begin{pmatrix}k(T-3+4/k)&\sqrt{k}(v-1)\\\sqrt{k}(v-1)&T-1\end{pmatrix}.
\]
When \(2\le k\le5\), both determinants vanish identically after substituting \(s=k/(1+\sqrt{2k})\) and \(v=(k-1)s/k\), and each diagonal entry is nonnegative (notably \(T\ge3-4/k\)). Thus both matrices are positive semidefinite. When \(k\ge6\), take \(T=3-4/k\) and \(v=1\); the second matrix is diagonal with entries \(0,T-1\), while the first has determinant \(k(T^2-5)\ge0\) and positive diagonal. The Gram estimate in step 1 supplies matching upper bounds.

**5. Additional unflipped coordinates do not alter the norm.** For \(n>k+1\), the symbol has several identical unflipped rows and columns. A Gram factorization for \(M_{k+1,k}\) can be extended by repeating the Gram vectors of its unflipped coordinate, without changing their maximum norm. Thus \(\|S_{n,k}\|\le\|S_{k+1,k}\|\); compression of a matrix input to any \(k+1\) principal coordinates gives the reverse inequality. The case \(k=0\) is the all-one symbol and is the identity multiplier.

This completes the proof for every allowed integer pair \((n,k)\).

## Verification
The provided standalone checker `verify_schur.py` evaluates the exact candidate constants, lower sign witnesses, and smallest eigenvalues of both proposed Gram certificate matrices for \(1\le k\le100\). It also checks the fully flipped core and the strict-increase/stabilization split. In the recorded run it passed 895 finite numerical assertions. The infinite-size conclusion is proved above, not inferred from those tests. To reproduce, run `python verify_schur.py` with NumPy installed.

## Relationship to prior work
Schur's norm/factorization theory and the Grothendieck–Haagerup characterization are classical; Davidson and Donsig, *Norms of Schur Multipliers* (2005/2007), establish general theory and exact formulas for certain transitive symmetry classes. The core-only matrix \(J_k-2I_k\) is circulant and its value \(3-4/k\) already follows from Mathias's circulant formula (1993); that core formula is **not** claimed as new. Holbrook, Johnston and Schoch, *Real Schur norms and Hadamard matrices* (first public 2022), develop general numerical semidefinite methods and list small-order spectral values that include several of the present constants; those low-dimensional numerical observations are not claimed as new either. Christensen's matrix-factorization work (2022; 2025) gives broad general methods, and Levene (2013) studies zero–one idempotent multipliers rather than their signed reflections.

The contribution assessed here is the **explicit all-size closed formula for a partially flipped diagonal**, the sharp change at six flipped coordinates, the duplication invariance, and elementary matching optimal witnesses and Gram certificates. These go beyond a generic SDP characterization or a list of small numerical instances. A prior equivalent all-size specialization remains possible and has not been ruled out by exhaustive literature coverage.

## Limitations
The symbol has a single set of identical negative diagonal signs and is \(+1\) elsewhere. This theorem does not treat arbitrary sign matrices, irregular off-diagonal flips, Schatten norms other than the spectral norm, or infinite operator matrices. The new priority claim is qualified by the possibility of an unlocated equivalent formulation in older multiplier literature, especially general matrix-completion results. Independent mathematical validation has not been performed.

## References
- J. Holbrook, N. Johnston and J.-P. Schoch, *Real Schur norms and Hadamard matrices*, arXiv:2206.02863 (first submitted 2022-06-06), *Linear and Multilinear Algebra* 72 (2024), 1967–1984.
- K. Davidson and A. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073 (2005), *Illinois Journal of Mathematics* 51 (2007).
- E. Christensen, *Norm optimal factorizations of scalar and block matrices*, arXiv:2211.00591 (2022).
- E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670 (2025).
- R. H. Levene, *Norms of idempotent Schur multipliers*, arXiv:1302.4849 (2013).
- R. Mathias, *The Hadamard operator norm of a circulant and applications* (1993), as cited in the Schur norm literature.
