# Exact two-block entanglement length for injective Pauli matrix-product states

## Finding
For every strictly positive probability vector \(p=(p_0,p_1,p_2,p_3)\), define the translation-invariant infinite-chain matrix-product state with four physical levels and virtual bond dimension two by the tensor matrices
\[
M_0=\sqrt{p_0}I_2,\quad M_1=\sqrt{p_1}X,\quad M_2=\sqrt{p_2}Y,\quad M_3=\sqrt{p_3}Z.
\]
Here \(X,Y,Z\) are the standard Pauli matrices. Set
\[
\lambda_x=p_0+p_1-p_2-p_3,\qquad
\lambda_y=p_0-p_1+p_2-p_3,\qquad
\lambda_z=p_0-p_1-p_2+p_3.
\]
For **every** pair of nonempty, finite, disjoint contiguous physical blocks \(A,C\) separated by exactly \(L\geq1\) traced-out sites, their reduced density operator satisfies the following three-way equivalence:
\[
\rho_{AC}\text{ is separable across }A|C
\quad\Longleftrightarrow\quad
\rho_{AC}^{T_C}\succeq0
\quad\Longleftrightarrow\quad
|\lambda_x|^L+|\lambda_y|^L+|\lambda_z|^L\leq1.
\]
When the strict reverse inequality holds, \(\rho_{AC}\) is nonpositive under partial transposition (NPT), regardless of either block's positive length. Therefore the smallest separation at which *all* such pairs are separable is exactly
\[
L_*(p)=\min\{L\in\mathbb N_{\geq1}:|\lambda_x|^L+|\lambda_y|^L+|\lambda_z|^L\leq1\}.
\]
This minimum is finite. In the isotropic subfamily \(p_0=(1+3s)/4\), \(p_1=p_2=p_3=(1-s)/4\), \(0<s<1\), it is
\[
L_*(s)=\left\lceil\frac{\log3}{-\log s}\right\rceil,
\qquad L_*(s)\sim\frac{\log3}{1-s}\quad(s\uparrow1).
\]
Thus the exact separation threshold diverges while the states converge locally to the product chain \(|0\rangle^{\otimes\infty}\).

## Assumptions and scope
The on-site Hilbert space is \(\mathbb C^4\); the auxiliary space is \(\mathbb C^2\). All four \(p_j\) are **strictly** positive and sum to one. Each tensor matrix \(M_j\) is as displayed. The infinite-state convention is the thermodynamic limit of normalized periodic-trace matrix-product states; equivalently, local density matrices are the fixed-point contractions of the canonical transfer channel
\[
\mathcal E(B)=\sum_{j=0}^3 M_j B M_j^\dagger.
\]
This channel is bistochastic, with left fixed point \(I_2\) and normalized right fixed point \(R=I_2/2\). Strict positivity gives \(|\lambda_x|,|\lambda_y|,|\lambda_z|<1\), hence a unique primitive fixed point and the stated infinite-chain limit. The conclusion applies to finite block lengths \(n=|A|\geq1\), \(m=|C|\geq1\), and every integer separator length \(L\geq1\). Physical sites beyond the two blocks, on both sides, are traced out. Nothing is asserted about arbitrary disconnected unions or finite-chain boundary corrections.

## Proof
**1. Transfer and injectivity.** Direct Pauli conjugation gives
\[
\mathcal E(I_2)=I_2,\qquad
\mathcal E(X)=\lambda_x X,\quad
\mathcal E(Y)=\lambda_y Y,\quad
\mathcal E(Z)=\lambda_z Z.
\]
Each eigenvalue has modulus strictly smaller than one: for example \(\lambda_x=1-2(p_2+p_3)>-1\) and \(\lambda_x=-1+2(p_0+p_1)<1\); similarly for the others. The channel is therefore primitive. For a physical word \(\mathbf a=(a_1,\dots,a_n)\) define \(M_{\mathbf a}=M_{a_1}\cdots M_{a_n}\), and a linear embedding
\[
\Gamma_n:\mathbb C^2\otimes\mathbb C^2\longrightarrow(\mathbb C^4)^{\otimes n},\quad
\Gamma_n|u,v\rangle=\sum_{\mathbf a}(M_{\mathbf a})_{uv}|\mathbf a\rangle.
\]
Every \(\Gamma_n\) has column rank four: for each \(j\in\{0,1,2,3\}\), the word consisting of one \(j\) and \(n-1\) zeros yields a nonzero multiple of the corresponding Pauli basis matrix. Thus \(\Gamma_n\) admits a linear left inverse \(H_n\) satisfying \(H_n\Gamma_n=I_4\), for all \(n\geq1\).

**2. Exact two-block tensor contraction.** The reduced matrix elements are
\[
\langle\mathbf a,\mathbf c|\rho_{AC}|\mathbf b,\mathbf d\rangle
=\operatorname{tr}\!\left[M_{\mathbf a}\,\mathcal E^L\!\left(M_{\mathbf c}(I_2/2)M_{\mathbf d}^\dagger\right)M_{\mathbf b}^\dagger\right].
\]
Introduce virtual legs \(A_o,A_i,C_i,C_o\), each two-dimensional. On the two *inner* legs set the output-first Choi operator
\[
\widetilde J_L=\sum_{u,v=0}^1\mathcal E^L(|u\rangle\langle v|)_{A_i}\otimes|u\rangle\langle v|_{C_i}.
\]
Writing \(\Omega_L=I_{A_o}\otimes\widetilde J_L\otimes(I_{C_o}/2)\), with the displayed ordering of tensor legs, the foregoing matrix elements give the **exact identity**
\[
\rho_{AC}=(\Gamma_n\otimes\Gamma_m)\,\Omega_L\,(\Gamma_n\otimes\Gamma_m)^\dagger.
\]
Here \(\Gamma_n\) groups \(A_o,A_i\) and \(\Gamma_m\) groups \(C_i,C_o\). This is an operator identity, not an approximation or an asymptotic estimate. Conversely,
\[
\Omega_L=(H_n\otimes H_m)\,\rho_{AC}\,(H_n\otimes H_m)^\dagger.
\]
Positive local congruences in either direction preserve separability across the two grouped block legs. They also preserve positivity under partial transposition in the forward and inverse directions, since the transposed local congruence is still a congruence. Tracing out \(A_o,C_o\) recovers \(\widetilde J_L\) up to a positive scalar, and tensoring with their identity factors adds no entanglement. Consequently
\[
\rho_{AC}\text{ separable (respectively PPT)}
\quad\Longleftrightarrow\quad
\widetilde J_L\text{ separable (respectively PPT)}.
\]

**3. Exact qubit criterion.** The operator \(\widetilde J_L\) differs only by swapping its two tensor factors from the usual Choi operator of \(\mathcal E^L\). It is a positive two-qubit operator. Two-qubit PPT is equivalent to separability, and the Choi operator is separable exactly when its channel is entanglement breaking. The channel \(\mathcal E^L\) remains a unital Pauli-diagonal qubit channel, with Bloch multipliers \(\lambda_x^L,\lambda_y^L,\lambda_z^L\). The established unital-qubit entanglement-breaking criterion [Ruskai, Theorem 4] is
\[
|\lambda_x|^L+|\lambda_y|^L+|\lambda_z|^L\leq1.
\]
Combining the two equivalences completes the classification, including equality. A failed inequality makes the two-qubit Choi operator NPT; the two-sided local inverses preserve this failure, so \(\rho_{AC}\) is NPT as claimed.

**4. Sharp length and product boundary.** Since \(|\lambda_j|<1\), their absolute powers tend to zero and the minimum \(L_*\) exists. In the isotropic family, each multiplier is \(s\), so the condition reduces to \(3s^L\leq1\), giving the ceiling expression. Finally \(-\log s\sim1-s\) as \(s\uparrow1\). All tensor matrices other than \(M_0\) converge to zero and \(M_0\) converges to \(I_2\); every fixed finite physical reduced state therefore converges to \(|0\rangle\langle0|^{\otimes k}\), while \(L_*\) diverges.

## Verification
The included `verify.py` independently constructs finite-block density matrices from the canonical transfer channel, constructs their virtual-filter recoveries using pseudoinverses, and compares the recovered operator to the explicit output-first Choi factorization. It checks positivity, trace one, and the sign of the minimum partially transposed eigenvalue for six strictly positive probability vectors and separator lengths \(1\) through \(8\) with one-site blocks; it additionally checks two-site versus one-site blocks. **Fifty-seven finite-dimensional tests passed.** These tests corroborate the tensor contractions and are not used as a substitute for the proof for all parameters and lengths. To run: `python verify.py`, with Python 3 and NumPy installed.

## Relationship to prior work
Ferydouni, Jackson and Scalet (2026) show that primitive transfer maps are eventually entanglement breaking and obtain a **sufficient** finite uniform separability length for normal matrix-product states. The theorem above gives, for an explicit strictly injective Pauli-tensor family, a **necessary-and-sufficient** criterion, NPT witnesses before the threshold, an exact all-block length, and its near-product divergence. It does not improve their general theorem or claim to resolve their separate transverse-Ising discussion. The physical-to-virtual embedding and the existence of local left inverses are established facts about injective MPS; the exact construction here makes the correspondence two-sided for the target reduced state. Ruskai's unital-qubit channel octahedron is a known theorem used as an ingredient, not a newly discovered channel criterion. Literature on eventually entanglement-breaking maps addresses channel powers independently of their realization as arbitrary-size physical chain marginals.

## Limitations
The result is restricted to the four-level Pauli MPS with strictly positive tensor weights, finite contiguous blocks, and a single contiguous separator. It does not treat general physical dimension, arbitrary injective MPS, disjoint unions, or a quantitative bound on a parent-Hamiltonian spectral gap as \(s\uparrow1\). The divergence occurs as the strict-positivity condition approaches a **noninjective endpoint**; no uniform-gap claim is made. The exact octahedron channel criterion and injective-block left inverses are established prior methods, so the specific family classification is the relevant potential contribution. Priority outside inspected sources is not certified.

## References
1. R. Ferydouni, T. Jackson, and S. O. Scalet, *Entanglement Sudden Death in Gapped Ground States*, arXiv:2610.17038v1 (first public 2026-10-12), https://arxiv.org/abs/2610.17038.
2. M. B. Ruskai, *Qubit Entanglement Breaking Channels*, arXiv:quant-ph/0302032 (2003), Theorem 4, https://arxiv.org/abs/quant-ph/0302032.
3. D. Sauerwein, A. Molnár, J. I. Cirac, and B. Kraus, *Matrix Product States: Entanglement, symmetries, and state transformations*, arXiv:1901.07448 (2019), https://arxiv.org/abs/1901.07448.
4. M. Rahaman, S. Jaques, and V. I. Paulsen, *Eventually Entanglement Breaking Maps*, arXiv:1801.05542 (2018), https://arxiv.org/abs/1801.05542.
