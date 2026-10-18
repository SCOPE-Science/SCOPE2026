# Sharp quasi-Schatten decay of the Cesàro–shift commutator

## Finding

Let \(C\) be the classical discrete Cesàro operator on \(\ell^2(\mathbb N_0)\) and \(S\) the forward unilateral shift. The nonzero commutator \(K=CS-SC\) has singular values satisfying two-sided, absolute-constant estimates

\[
0<c\le m^2s_m(K)\le C_0<\infty \qquad(m\ge1).
\]

Consequently, for every real \(p>0\),

\[
K\in\mathcal S_p\quad\Longleftrightarrow\quad p>\tfrac12,
\]

and \(K\in\mathcal S_{1/2,\infty}\setminus\mathcal S_{1/2}\). Here \(\mathcal S_{1/2,\infty}\) means the weak singular-value ideal \(\sup_{m\ge1}m^2s_m(K)<\infty\). In particular \(K\) is trace class with trace zero. The critical exponent is sharp; this is a two-sided asymptotic order, not a claim of an exact leading numerical constant.

## Assumptions and scope

The Hilbert space is the complex sequence space \(H=\ell^2(\mathbb N_0)\) with orthonormal basis \((e_n)_{n\ge0}\). The operators are

\[
(Cx)_n=\frac1{n+1}\sum_{k=0}^n x_k,\qquad Se_k=e_{k+1}.
\]

The Cesàro operator is bounded on \(H\), and \(S\) is an isometry. Singular values \(s_m\) are listed in nonincreasing order with multiplicities and index \(m\ge1\). For \(p>0\), \(\mathcal S_p\) denotes the compact operators with \(\sum_m s_m^p<\infty\); for \(p<1\) this is a quasi-Banach ideal.

Matrix multiplication gives, for \(n,k\ge0\),

\[
\langle Ke_k,e_n\rangle=
\begin{cases}
-\bigl(n(n+1)\bigr)^{-1},&n\ge1,\ 0\le k<n,\\
0,&\text{otherwise}.
\end{cases}
\]

The first row vanishes, and the nonzero entries occupy the strict lower triangle.

## Proof

**1. Dyadic decomposition.** Write \(I_j=\{2^j,\ldots,2^{j+1}-1\}\) and \(m_j=2^j\) for \(j\ge0\). Let \(P_j\) project onto the coordinates in \(I_j\), and \(Q_j\) onto \(\{0,\ldots,2^j-1\}\). Partition the matrix into

\[
K=B+R,\qquad B=\bigoplus_{j\ge0}P_jKP_j,
\qquad R=\sum_{j\ge0}P_jKQ_j.
\]

The decomposition is exact: each nonzero entry of \(K\) has either both indices in the same dyadic block or its column lies strictly before the row block. For \(n\in I_j\), put \(a_n=1/(n(n+1))\), so that \(P_jKP_j=-D_jJ_{m_j}\), where \(D_j\) is diagonal with entries \(a_n\) and \(J_m\) is the strictly lower-triangular \(m\)-square matrix with all lower entries equal to one. Since \(m_j\le n\le2m_j-1\),

\[
\frac1{4m_j^2}\le a_n\le\frac1{m_j^2}.
\]

**2. Exact finite-block singular values.** Delete the zero first row and zero last column of \(J_m\). The remaining \((m-1)\)-square matrix \(L_{m-1}\) has all entries on and below the diagonal equal to one; hence their nonzero singular values coincide. Its inverse is the first-difference matrix \(D\) with diagonal entries one and subdiagonal entries minus one. The matrix \(D^*D\) has diagonal \((2,\ldots,2,1)\) and adjacent off-diagonal entries minus one. Solving its discrete sine eigenvalue recurrence, including the free right endpoint, gives exactly

\[
s_k(L_r)=\frac{1}{2\sin\!\left(\frac{(2k-1)\pi}{4r+2}\right)},
\qquad 1\le k\le r.
\]

(The formula also holds for \(r=1\); direct substitution gives its unique singular value one.) Elementary bounds on \(\sin\theta\) for \(0<\theta<\pi/2\) and the standard singular-value ideal inequalities for invertible diagonal multipliers yield absolute constants \(c_1,C_1>0\) with

\[
\frac{c_1}{m_jk}\le s_k(P_jKP_j)\le\frac{C_1}{m_jk},
\qquad 1\le k<m_j,
\]

and one further zero singular value per block. For example \(c_1=1/20\) and \(C_1=1\) are valid.

**3. Global counting for the diagonal blocks.** For \(t>0\), define \(N_B(t)=\#\{k:s_k(B)>t\}\). By the preceding inequalities,

\[
N_B(t)\le\sum_{j\ge0}\min\left\{m_j,\frac{C_1}{m_jt}\right\}
\le C_2 t^{-1/2}\quad(0<t\le t_0).
\]

The last inequality follows by splitting the dyadic sum at \(m_j\asymp t^{-1/2}\), using a geometric series on either side. For the reverse inequality, for every sufficiently small \(t\) select a dyadic integer \(m_j\) between \((16\sqrt t)^{-1}\) and \((8\sqrt t)^{-1}\). Then at least \(\lfloor m_j/2\rfloor\) entries in this block satisfy

\[
s_k(P_jKP_j)\ge\frac1{20m_jk}\ge\frac1{10m_j^2}>t,
\qquad 1\le k\le\lfloor m_j/2\rfloor.
\]

Thus \(c_2t^{-1/2}\le N_B(t)\le C_2t^{-1/2}\) for all sufficiently small \(t>0\), and inversion of this distribution function yields \(s_m(B)\asymp m^{-2}\) for all sufficiently large \(m\). The remaining finitely many indices are positive because arbitrarily many diagonal blocks have nonzero singular values; adjust the constants to obtain the bounds for all \(m\ge1\).

**4. Inter-block remainder.** Each \(R_j=P_jKQ_j\) has rank one and obeys

\[
\|R_j\|=\sqrt{m_j}\left(\sum_{n=m_j}^{2m_j-1}a_n^2\right)^{1/2}\le m_j^{-1}=2^{-j}.
\]

The partial sum \(\sum_{j<J}R_j\) has rank at most \(J\), while the remaining operator norm is bounded by \(\sum_{j\ge J}2^{-j}=2^{1-J}\). By the finite-rank characterization of approximation numbers,

\[
s_{J+1}(R)\le2^{1-J}\qquad(J\ge0).
\]

Thus \(R\in\mathcal S_p\) for every \(p>0\), and its singular values decay exponentially.

**5. Perturbation transfer and threshold.** For compact operators the Ky Fan inequality is

\[
s_{a+b-1}(U+V)\le s_a(U)+s_b(V),\qquad a,b\ge1.
\]

Applying it first to \(K=B+R\) and then to \(B=K-R\), and using the exponential remainder bounds, yields \(s_m(K)\asymp m^{-2}\). Specifically, \(s_{2m-1}(K)\le s_m(B)+s_m(R)=O(m^{-2})\), whereas \(s_{2m-1}(B)\le s_m(K)+s_m(R)\) gives \(s_m(K)\ge c m^{-2}\) for all sufficiently large \(m\). The finitely many remaining positive singular values can be absorbed into the constants: \(K\) has infinite rank by the lower bound on \(B\) and the superpolynomial bound on \(R\). Finally \(\sum m^{-2p}\) converges exactly when \(p>1/2\). Because \(K\in\mathcal S_1\), its trace is the sum of its diagonal matrix entries, all zero. This proves the claim.

## Verification

A standalone standard-library checker, `verify_commutator.py`, reconstructs exact rational finite sections of \(CS-SC\), verifies the strict-lower-triangle formula, checks that each strict block reduces to a smaller inclusive lower-triangular matrix, and verifies the first-difference inverse and its exact tridiagonal Gram matrix for every dimension from 2 through 29. It also checks the finite trigonometric singular-value moment identity against the known Frobenius norm. Run `python3 verify_commutator.py` to obtain `CESARO_SHIFT_QUASI_SCHATTEN_FINITE_IDENTITIES_OK dimensions=28`. These finite checks do not certify the counting estimates or infinite-dimensional result; those are established by the proof above.

## Relationship to prior work

Bellavita, Dellepiane, and Stylogiannis [1] develop Schatten theory of terraced/Rhaly matrices. Their Theorems 1.3 and 5.8 establish the general membership classification for \(1<q<\infty\), and their concluding discussion explicitly leaves \(0<q\le1\) without a complete classification. Their Section 6 introduces difference-generated strict triangular matrices \(A_c\). The present \(K\) is precisely the special choice with \(c_n=1/(n+1)\), so this paper is a substantive comparison, not a claim of a new object. The new assertion is the two-sided, individually indexed singular-value estimate and consequent sharp endpoint in that very specialization. The qualitative estimates and one-way general quasi-Schatten condition of [1] do not imply this endpoint.

Bellavita and Stylogiannis [2] show that the Cesàro operator belongs to the Toeplitz algebra's commutator ideal and construct a discrete Mellin calculus with Hilbert–Schmidt multiplication defects for sampled-ratio matrices. This establishes important algebraic context but does not give \(s_m([C,S])\asymp m^{-2}\); the shift \(S\) is not one of their sampled-ratio kernels. Classical approximation-number results for continuous Hardy/Volterra integral operators [3] concern continuous, non-atomic models and do not directly determine the lattice saturation and critical exponent for this discrete matrix. Searches for the exact commutator, its difference-generated Rhaly form, aliases, quasi-Schatten orders and stronger covering classifications found no direct published implication. This does not exclude unindexed results or unnoticed applications of older abstract theorems.

## Limitations

The theorem concerns one canonical commutator of the discrete Cesàro operator on \(\ell^2(\mathbb N_0)\), not arbitrary Rhaly matrices, arbitrary Toeplitz commutators or other \(\ell^p\) spaces. It determines the two-sided order, not the existence or value of \(\lim_{m\to\infty}m^2s_m(K)\). The bibliographic comparison does not amount to an independent originality certificate. The analytic arguments and numerical checks have not received independent mathematical audit.

## References

[1] Carlo Bellavita, Eugenio Dellepiane, Georgios Stylogiannis, *Boundedness, compactness and Schatten class for Rhaly matrices*, arXiv:2503.21930 (first publicly submitted 2025-03-27), https://arxiv.org/abs/2503.21930 . Relevant primary full-text material: Theorems 1.3, 5.5, 5.7, 5.8; Section 6, including Lemma 6.2; Section 7.

[2] Carlo Bellavita, Georgios Stylogiannis, *A discrete Mellin calculus in the Toeplitz algebra*, arXiv:2609.09453 (2026), https://arxiv.org/abs/2609.09453 . Relevant primary full-text material: Introduction, Theorems 1.1–1.2, Sections 2–4 and the Toeplitz mechanism.

[3] W. D. Evans, D. J. Harris, J. Lang, *The Approximation Numbers of Hardy-Type Operators on Trees*, Proc. London Math. Soc. 83 (2001), 390–418, https://doi.org/10.1112/plms/83.2.390 . Continuous-model comparison only.
