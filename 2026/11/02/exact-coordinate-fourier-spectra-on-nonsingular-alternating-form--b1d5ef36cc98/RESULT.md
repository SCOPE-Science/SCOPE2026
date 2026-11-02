# Exact coordinate Fourier spectra on nonsingular alternating forms and a dimension-eight transition

## Finding
Let \(q\ge2\) be any prime power and let \(d\ge6\) be even. On the set \(\Omega_{d,q}\) of nonsingular alternating \(d\times d\) matrices over \(\mathbb F_q\), equipped with uniform probability measure, consider the constant function and one nontrivial additive coordinate character for each of the \(E=\binom d2\) strict upper-triangular positions:
\[
f_0(A)=1,\qquad f_{ij}(A)=\psi(t_{ij}A_{ij})\quad(1\le i<j\le d),\qquad t_{ij}\in\mathbb F_q^\times.
\]
Here \(\psi\) is any nontrivial additive character. All choices of the nonzero \(t_{ij}\) have the same Gram spectrum. Define
\[
U=q^{d-1}-1,\quad V=q^{d-3}-1,\quad a=-\frac1U,\quad b=\frac1{UV},\quad E=\frac{d(d-1)}2,
\]
\[
\lambda_0=1+2(d-2)a+\binom{d-2}{2}b,\quad
\lambda_1=1+(d-4)a-(d-3)b,\quad
\lambda_2=1-2a+b,
\]
\[
\mu_\pm=\frac{1+\lambda_0\pm\sqrt{(1-\lambda_0)^2+4Ea^2}}2.
\]
Then the complete spectrum of the \((E+1)\)-by-\((E+1)\) normalized Gram matrix is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\mu_-&1\\
\mu_+&1\\
\lambda_1&d-1\\
\lambda_2&d(d-3)/2
\end{array}.
\]
All the eigenvalues are strictly positive, so the displayed characters are linearly independent on \(\Omega_{d,q}\). The smallest eigenvalue is always \(\mu_-\). The largest eigenvalue undergoes a universal, strict transition independent of the field:
\[
\lambda_{\max}=\begin{cases}\lambda_2,&d=6,\\\mu_+,&d\ge8\text{ even}.
\end{cases}
\]
Consequently the sharp squared Riesz condition number is \(\lambda_2/\mu_-\) in dimension six and \(\mu_+/\mu_-\) in every even dimension at least eight. Its upper and lower equality spaces are given explicitly below. The transition holds for all prime powers, including characteristic two.

## Assumptions and scope
An alternating matrix has zero diagonal and satisfies \(A_{ji}=-A_{ij}\); in characteristic two, the zero-diagonal condition is retained. Nonsingular means invertible over \(\mathbb F_q\). The norm of a coefficient vector is its ordinary Euclidean \(\ell^2\)-norm, and the function inner product is the average over \(\Omega_{d,q}\), without extra scaling. The Fourier family has exactly one selected nonzero-frequency character on each strict upper-triangular coordinate, plus the constant; no claim is made for all \(q-1\) frequency labels per coordinate or for arbitrary frequency masks. Restricting to \(d\ge6\) isolates the first dimensions in which the full-rank alternating locus is not the complement of the rank-two locus inside the whole alternating-form space.

## Proof
**1. Character moments from random symplectic bases.** Fix a nondegenerate alternating form \(\omega\) on \(\mathbb F_q^d\). Every nonsingular alternating form is a \(\operatorname{GL}_d(\mathbb F_q)\)-congruence of \(\omega\), and every form has the same number of congruence preimages. Thus a uniform \(A\in\Omega_{d,q}\) has the joint distribution \(A_{ij}=\omega(v_i,v_j)\), where \((v_1,\ldots,v_d)\) is a uniform ordered basis.

Put \(t=\omega(v_1,v_2)\). With \(v_1\ne0\) fixed, \(v_2\) is uniform outside \(\langle v_1\rangle\). The probability of \(t=0\) is \((q^{d-1}-q)/(q^d-q)\), whereas every fixed nonzero \(t\) has probability \(q^{d-1}/(q^d-q)\). Since \(\sum_{t\ne0}\psi(t)=-1\),
\[
\mathbb E\,\psi(\omega(v_1,v_2))=-\frac1{q^{d-1}-1}=a.
\]
For four independent vectors, condition on \(v_1,v_2,v_3\). Writing \(W_3=\langle v_1,v_2,v_3\rangle\), complete character orthogonality on \(\mathbb F_q^d\) and on \(W_3\) gives
\[
\mathbb E_{v_4}\psi(-\omega(v_3,v_4))
=-\frac{1}{q^{d-3}-1}\,\mathbf1_{\{v_3\perp\langle v_1,v_2\rangle\}}.
\]
Indeed, \(v_4\) ranges over the \(q^d-q^3\) vectors outside \(W_3\), and the excluded subspace contributes \(q^3\) exactly when the functional vanishes on \(W_3\), otherwise zero. Conditional on \(t=0\), the probability that \(v_3\) lies in \(\langle v_1,v_2\rangle^\perp\) is \((q^{d-2}-q^2)/(q^d-q^2)\). Conditional on \(t\ne0\), it is \((q^{d-2}-1)/(q^d-q^2)\). Substitution of the displayed distribution of \(t\) shows
\[
\mathbb E\bigl[\psi(t)\mathbf1_{\{v_3\perp\langle v_1,v_2\rangle\}}\bigr]=-\frac1{q^{d-1}-1}.
\]
Combining the two conditioning steps yields
\[
\mathbb E\,\psi(A_{12}-A_{34})=\frac1{(q^{d-1}-1)(q^{d-3}-1)}=b.
\]
The congruence group is transitive on alternating coefficient forms of each given even rank. A nonzero coordinate coefficient has rank two; the difference of two coordinate coefficients has rank two when the coordinate edges share one vertex and rank four when they are disjoint. Nonzero multipliers \(t_{ij}\) do not affect these ranks. Accordingly every constant-to-coordinate Gram entry equals \(a\), and every pair of distinct coordinate columns has Gram entry \(a\) for intersecting edges and \(b\) for disjoint edges. All diagonal entries are one. These character averages are real in every characteristic.

**2. Exact diagonalization.** Index the \(E\) coordinate columns by edges of the complete graph on \(d\) vertices. If \(A_J\) is the adjacency matrix of the Johnson graph \(J(d,2)\) (intersecting edges), and \(A_D\) the disjointness adjacency matrix, the coordinate block is
\[
G_{\rm edge}=I_E+aA_J+bA_D.
\]
Let \(M\) be the unsigned vertex-edge incidence matrix. The identities \(M^TM=2I_E+A_J\) and \(MM^T=(d-2)I_d+\mathbf1\mathbf1^T\) show that the edge space is the orthogonal sum of its uniform line, a vertex-contrast space of dimension \(d-1\), and \(\ker M\) of dimension \(E-d=d(d-3)/2\). On these spaces \(A_J\) has eigenvalues \(2(d-2)\), \(d-4\), and \(-2\), respectively. Since \(A_D=\mathbf1\mathbf1^T-I_E-A_J\), the last two spaces have Gram eigenvalues \(\lambda_1\) and \(\lambda_2\). The uniform edge vector has Gram value \(\lambda_0\) and couples to the constant function with coefficient \(a\sqrt E\). Hence the remaining block is
\[
K=\begin{pmatrix}1&a\sqrt E\\a\sqrt E&\lambda_0\end{pmatrix}
\]
and has eigenvalues \(\mu_\pm\). This proves the complete spectrum and multiplicities. The eigenvalue \(\lambda_1\) has equality vectors \(w_{ij}=x_i+x_j\) with \(\sum_i x_i=0\); \(\lambda_2\) has equality vectors satisfying \(\sum_{j\ne i}w_{ij}=0\) for every vertex; \(\mu_\pm\) have the corresponding two eigendirections in the span of the constant and uniform-edge coefficient vectors.

**3. Positivity and sharp extremizers.** All off-diagonal Gram entries have absolute value at most \(1/U\), because \(V\ge1\). There are \(E\) off-diagonal entries in each row of the full matrix. For even \(d\ge6\), \(U\ge2^{d-1}-1>\binom d2=E\). Thus the Gram matrix is strictly diagonally dominant with positive diagonal. As it is Hermitian, it is positive definite. Moreover \(\lambda_0-\lambda_1=-d/U+d(d-3)/(2UV)<0\), since \(V\ge d-3\), and \(\lambda_1<1<\lambda_2\). The smaller eigenvalue of \(K\) is strictly below \(\lambda_0\) and the larger strictly above one. Therefore \(\mu_-<\lambda_1<\lambda_2\), and the only candidates for the largest eigenvalue are \(\lambda_2\) and \(\mu_+\).

To compare them, let \(p(z)=(z-1)(z-\lambda_0)-Ea^2\), the characteristic polynomial of \(K\). Direct substitution and factorization give the exact identity
\[
p(\lambda_2)=\frac{d-1}{2U^2V^2}\left((8-d)V^2-2(d-6)V-(d-4)\right).
\]
Because \(\lambda_2>1>\mu_-\), this quantity is positive exactly when \(\lambda_2>\mu_+\), and negative exactly when \(\lambda_2<\mu_+\). When \(d=6\), the bracket is \(2(V^2-1)>0\), since \(V\ge7\). When \(d=8\), it is \(-4(V+1)<0\); when \(d\ge10\), each displayed term is negative. No equality occurs. This proves the universal dimension-eight transition and all stated sharp bounds, including the equality spaces. 

## Verification
Run `python3 checks/check_alternating.py` using only the Python standard library. The checker enumerates nonsingular alternating matrices by exact modular Pfaffians over the prime fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) in dimension four, and over \(\mathbb F_2\) in dimension six. For every case it computes all coordinate and pairwise coordinate-frequency character moments from exact integer zero counts, not from the predicted Gram matrix. Its 183 moment identities and associated trace/determinant and crossover polynomial checks pass. The dimension-four tests are extra boundary diagnostics outside the theorem's main range. The proof above covers every prime-power field and every even dimension at least six; finite enumeration alone cannot establish that universal statement.

## Relationship to prior work
Delsarte and Goethals (1975) developed the alternating-bilinear-form association scheme; its eigenmatrix contains rank-sensitive character-sum data that underlie the first step of the proof. The Johnson-graph decomposition is classical. The novel question isolated here is the full Gram spectrum of the specific constant-plus-one-frequency-per-coordinate frame **on the nonsingular alternating orbit**, and the exact, field-independent crossing of its optimal upper Riesz mode. This is not a theorem about all eigenvalues of the ambient association scheme.

De Seguins Pazzis (arXiv:1507.06213, 2015) studies affine spaces of bounded-rank alternating matrices, not restriction of additive characters to the full-rank locus. Existing coordinate-frame calculations for the rank-two Plücker cone treat decomposable bivectors; in dimensions at least six that cone is not the complementary full-rank orbit because intermediate ranks exist. Coordinate-Walsh frames on binary symplectic **groups** concern invertible transformations preserving a fixed form rather than the entire congruence orbit of nonsingular forms. The displayed formulas and sharp comparison were not found in the inspected materials or indexed exact-claim searches. The historical full text of the 1975 article was not accessible, so an equivalent older implication remains a scientific priority risk.

## Limitations
No claim is made that the displayed functions span all of \(L^2(\Omega_{d,q})\), that all \(q-1\) frequency labels per edge have this spectrum, or that the family is optimal among arbitrary frequency selections. The only sharp optimization is identification of spectral extrema within the explicitly stated family. The 1975 foundational paper is known bibliographically but its complete text was not available for this comparison; the result consequently has bounded, not exhaustive, originality verification. No independent validation has been performed.

## References
1. P. Delsarte and J.-M. Goethals, “Alternating bilinear forms over GF(q),” *Journal of Combinatorial Theory, Series A* **19** (1975), 26–50, DOI:10.1016/0097-3165(75)90090-4.
2. C. de Seguins Pazzis, “Affine spaces of symmetric or alternating matrices with bounded rank,” arXiv:1507.06213, first version 22 July 2015, https://arxiv.org/abs/1507.06213.
3. K.-U. Schmidt, “Symmetric bilinear forms over finite fields with applications to coding theory,” arXiv:1410.7184 (2014), https://arxiv.org/abs/1410.7184 (related symmetric-form scheme, not the nonsingular alternating orbit).
4. “Sharp coordinate Fourier spectrum on the finite-field Plücker cone,” published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-coordinate-fourier-spectrum-on-the-finite-field-pl-cker-co--91dfe0fce2d0 (rank-two, not full-rank alternating forms).
5. “Complete coordinate Walsh-frame spectrum on binary symplectic groups,” published research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-complete-coordinate-walsh-frame-spectrum-on-binary-symplectic-gr--c844347e16db (different underlying group).
