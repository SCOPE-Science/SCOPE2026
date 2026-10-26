# A two-block spectral formula and rank-one attainment frontier for rectified matrix approximation

## Finding

Let \(m,n\ge 1\) and let \(X\in\mathbb R_{\ge0}^{m\times n}\). For an entrywise rectifier \(\rho(t)=\max\{t,0\}\), consider the global rank-one Frobenius problem
\[
E_1(X)=\inf_{u\in\mathbb R^m,\,v\in\mathbb R^n}\|X-\rho(uv^{\mathsf T})\|_F^2.
\]
For any row set \(I\subseteq[m]\) and column set \(J\subseteq[n]\), write \(I^c,J^c\) for their complements. Denote by \(\sigma_1(B)\) the largest singular value of a rectangular matrix \(B\), defined to be zero when either dimension is zero. Then the infimum is always attained and satisfies the **exact finite spectral optimization formula**
\[
\boxed{ E_1(X)=\|X\|_F^2-\max_{I\subseteq[m],\,J\subseteq[n]}\left(\sigma_1(X_{I,J})^2+\sigma_1(X_{I^c,J^c})^2\right). }
\]
More strongly, the set of all output matrices \(\{\rho(uv^{\mathsf T}):u\in\mathbb R^m,v\in\mathbb R^n\}\) is closed, despite the possible unboundedness of its parameter factors.

Consequently every finite-dimensional Frobenius ReLU matrix-decomposition problem with latent rank at most one admits a minimizer. In ambient size \(\min\{m,n\}\le2\), the problem admits a minimizer **at every allowed rank**: rank zero or one is covered above, while rank at least \(\min\{m,n\}\) represents the nonnegative input exactly. In view of an existing nonattainment example of rank two and size three by three [1], both the ambient dimension and latent rank of that example are minimal for possible Frobenius nonattainment. For the identity matrix, \(E_1(I_n)=\max\{n-2,0\}\).

## Assumptions and scope

The data matrix is arbitrary entrywise nonnegative real and finite; the dimensions are positive integers. The objective is squared Frobenius distance after entrywise ReLU, with **no** sign restrictions or regularization on the two factors and latent rank **at most one**. Empty row or column subsets, zero matrices, multiple leading singular vectors, and zero factors are included. The closedness assertion itself does not require nonnegative data because it concerns only the feasible output set. This statement concerns global optimal values, not the behavior of a particular iterative solver.

## Proof

**1. Exact sign-partition representation.** For each pair of sets \(I\subseteq[m]\), \(J\subseteq[n]\), let \(\mathcal C_{I,J}\) be the set of matrices \(Y\ge0\) such that
\[
Y_{I,J^c}=0,\quad Y_{I^c,J}=0,\quad
\operatorname{rank}(Y_{I,J})\le1,\quad
\operatorname{rank}(Y_{I^c,J^c})\le1.
\]
Given arbitrary real factors \(u,v\), choose \(I=\{i:u_i\ge0\}\) and \(J=\{j:v_j\ge0\}\). The cross rectangles of \(uv^{\mathsf T}\) are nonpositive, so its ReLU is zero there. The two diagonal rectangles are nonnegative outer products and thus have rank at most one. Hence every rectified outer product belongs to some \(\mathcal C_{I,J}\).

Conversely, given \(Y\in\mathcal C_{I,J}\), each nonnegative rank-at-most-one diagonal rectangle admits a factorization by nonnegative vectors: \(Y_{I,J}=ab^{\mathsf T}\) and \(Y_{I^c,J^c}=cd^{\mathsf T}\), with zero factors allowed. Define \(u_I=a\), \(u_{I^c}=-c\), \(v_J=b\), and \(v_{J^c}=-d\). Both cross rectangles of \(uv^{\mathsf T}\) are nonpositive, so \(\rho(uv^{\mathsf T})=Y\). Therefore
\[
\{\rho(uv^{\mathsf T}):u,v\}=\bigcup_{I,J}\mathcal C_{I,J}.
\]

**2. Closedness and attainment.** Every \(\mathcal C_{I,J}\) is closed: nonnegativity and prescribed zero entries are closed conditions, and rank at most one is described by the vanishing of all two-by-two minors. There are finitely many pairs of subsets. Their union is closed. The squared Frobenius distance from a finite matrix to this nonempty closed set attains its minimum, because its bounded sublevel sets are compact in the finite-dimensional output space. This does not assert that the set of minimizing factor pairs is compact.

**3. Spectral optimization on one rectangle.** For a nonnegative rectangular matrix \(B\), the minimum of \(\|B-Z\|_F^2\) over \(Z\ge0\) of rank at most one is
\[
\|B\|_F^2-\sigma_1(B)^2.
\]
The ordinary best-rank-one theorem gives the lower bound. To attain it with \(Z\ge0\), select nonnegative left and right unit singular vectors for the top singular value. Such vectors exist by the nonnegative-entry structure of \(B\): one may take a nonnegative unit maximizer for the quadratic form of \(B^{\mathsf T}B\), then use its nonnegative image under \(B\), handling \(B=0\) separately. The resulting scaled outer product attains equality.

**4. Pairwise decoupling.** In the fixed cone \(\mathcal C_{I,J}\), the two diagonal rank-one blocks can be chosen independently, while the cross rectangles are forced to zero. Thus its minimum squared error equals
\[
\|X\|_F^2-\sigma_1(X_{I,J})^2-\sigma_1(X_{I^c,J^c})^2.
\]
Maximization over the finitely many choices of \((I,J)\) yields the claimed formula. A minimizing factor pair can be obtained constructively by taking nonnegative leading singular vectors of the two winning rectangles and inserting opposite signs on the complementary row and column factors as in step 1. This proves attainment even if some leading singular vectors are not unique.

**5. Sharp dimension-and-rank frontier.** If the permitted latent rank is zero, the zero output is attainable. At rank one, steps 1--4 apply. If the permitted latent rank is at least \(\min\{m,n\}\), take the latent matrix equal to \(X\), whose ReLU is \(X\), for zero error. When \(\min\{m,n\}\le2\), these cases exhaust nonnegative integer ranks. The rank-two, three-by-three failure given in [1, Proposition 2.1] shows this cannot be extended in general to the next rank/dimension. For \(I_n\), the spectral square of a submatrix selected by \((I,J)\) is one exactly when \(I\cap J\ne\varnothing\), otherwise zero. Both paired blocks can contribute one iff \(n\ge2\); since \(\|I_n\|_F^2=n\), the stated identity follows.

## Verification

The accompanying standalone script `verify_rank_one_relu.py` exhaustively enumerates binary matrices of sizes one by one, one by four, two by two, and two by three, then checks structured identity matrices and seeded nonnegative matrices through size four by four. For each case, it exhaustively enumerates the row and column sign partitions, constructs nonnegative leading singular-vector factors on each selected pair of rectangles, rebuilds the signed outer product, rectifies it, and compares its residual to the exact spectral objective. It also checks the explicit two-by-two parameter family from [2]. This is a reproducibility and algebraic-consistency check; the universal assertion rests on the proof, not finite enumeration.

## Relationship to prior work

Seraghiti, Vandaele, and Gillis [1] show that Frobenius ReLU matrix decomposition is NP-hard even at latent rank one, and produce a nonattained infimum at latent rank two on a three-by-three matrix. Neither fact supplies the above **rank-one global optimum**, output-set closedness, or minimal nonattainment frontier. There is no conflict with NP-hardness: maximizing the paired singular-value score can itself require combinatorial exploration over exponentially many sign partitions.

Gillis, Porcelli, and Seraghiti [2, Section 3] distinguish the direct ReLU objective from its latent surrogate: they exhibit a rank-one **latent** nonattainment and show direct ReLU attainment for that **specific** small example, explicitly leaving general direct-model well-posedness unsettled. The result here settles the rank-one case for arbitrary dimensions, without asserting higher-rank well-posedness. Saul's early latent-model treatment [3] and the later subzero-completion work [4] concern related low-rank structures, but the inspected material does not establish the stated global spectral formula.

## Limitations

The finite spectral expression is not claimed to yield a polynomial-time algorithm and does not invalidate the existing NP-hardness result. Closedness of the rectified rank-one **outputs** does not imply boundedness of their real factor preimages. The formula is proved only for nonnegative inputs; for signed data, attainment via closedness survives but the nonnegative singular-vector argument for the formula need not apply. Rank two and higher can fail to attain a minimum, as in [1]. No claims are made about local optimization, random instances, or numerical conditioning of SVD-based enumeration.

## References

[1] G. Seraghiti, A. Vandaele, and N. Gillis, *The ReLU Matrix Decomposition: NP-Hardness, Ill-Posedness, and ReLU-Rank*, arXiv:2610.22255v1 (first publicly posted 2026-10-15), https://arxiv.org/html/2610.22255v1 .

[2] N. Gillis, M. Porcelli, and G. Seraghiti, *An extrapolated and provably convergent algorithm for nonlinear matrix decomposition with the ReLU function*, arXiv:2503.23832v1 (2025), https://arxiv.org/html/2503.23832v1 .

[3] L. K. Saul, *A Nonlinear Matrix Decomposition for Mining the Zeros of Sparse Data*, SIAM Journal on Mathematics of Data Science 4 (2022), 431--463, https://doi.org/10.1137/21M1405769 .

[4] L. K. Saul et al., *Subzero matrix completion for sparse data analysis: large-scale learning of latent low-rank structure*, arXiv:2608.21607v1 (2026), https://arxiv.org/html/2608.21607v1 .
