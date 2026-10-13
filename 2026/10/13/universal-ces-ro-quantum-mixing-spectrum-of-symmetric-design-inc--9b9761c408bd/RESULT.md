# Universal Cesàro quantum-mixing spectrum of symmetric-design incidence graphs

## Finding
Let \(\mathcal D\) be any symmetric \(2\)-\((v,k,\lambda)\) design with \(v\ge3\), \(2\le k\le v-1\), and incidence matrix \(B\) of order \(v\). Equivalently, its incidence graph is a connected regular bipartite graph with exactly four distinct adjacency eigenvalues. Define \(s=\sqrt{k-\lambda}\), \(c=(v-2)/(2v)\), and \(d=|v-2k|/(2vs)\). The continuous-time adjacency quantum walk on its \(2v\)-vertex incidence graph has infinite-time average mixing matrix with **complete multiset of eigenvalues**
\[
\operatorname{Spec}(\widehat M)=\{1^{[1]},\ 0^{[1]},\ (c+d)^{[v-1]},\ (c-d)^{[v-1]}\}.
\]
Brackets on an eigenvalue indicate multiplicity, and coincident values have multiplicities added. In particular, for every nontrivial symmetric design \(2\le k\le v-2\),
\[
\operatorname{rank}\widehat M=2v-1,\qquad
\ker\widehat M=\operatorname{span}\{(\mathbf1_v,-\mathbf1_v)\},\qquad
\gamma=c-d>0,
\]
where \(\gamma\) is the smallest positive eigenvalue. For the boundary design \(k=v-1\) (whose incidence graph is the crown graph), the rank is \(v\); the positive eigenvalues are \(1\) and \((v-2)/v\), the latter with multiplicity \(v-1\). The trace is always \(v-2+2/v\), independent of \(k\) and \(\lambda\). All average transition probabilities are given by the explicit matrix in the proof.

For any finite projective plane of order \(q\ge2\), taking \(v=q^2+q+1\), \(k=q+1\), \(\lambda=1\) gives rank \(2q^2+2q+1\) on \(2q^2+2q+2\) vertices and the exact smallest positive eigenvalue
\[
\frac{q^2+q-1}{2(q^2+q+1)}-
\frac{q^2-q-1}{2(q^2+q+1)\sqrt q}.
\]
The result does not require the projective plane to be Desarguesian or the design to be transitive.

## Assumptions and scope
A symmetric \(2\)-\((v,k,\lambda)\) design has \(v\) points and \(v\) blocks, each point belonging to \(k\) blocks and every pair of distinct points contained in \(\lambda\) blocks; every block also has size \(k\). All incidence entries are in \(\{0,1\}\). The design parameter equation is \(k(k-1)=\lambda(v-1)\). The incidence graph has points and blocks as two disjoint vertex sets and joins precisely incident pairs. The quantum Hamiltonian is the **unweighted adjacency matrix**
\[
A=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},
\quad U(t)=\exp(itA),\quad
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ\overline{U(t)}\,dt.
\]
The result covers every such design for integers \(v\ge3\) and \(2\le k\le v-1\), including the smallest case \(v=3,k=2,\lambda=1\). No simplicity of adjacency eigenvalues, automorphism transitivity, or prime-power hypothesis is assumed. The disconnected case \(k=1\), the complete bipartite case (three distinct eigenvalues), non-symmetric designs, and alternative Hamiltonians are excluded.

## Proof
**1. The design and singular-value identities.** Write \(J=\mathbf1_v\mathbf1_v^{\mathsf T}\), \(E=J/v\), \(C=I-E\), \(s^2=k-\lambda\), and \(D=B-kE\). The symmetric-design identities give
\[
B\mathbf1_v=B^{\mathsf T}\mathbf1_v=k\mathbf1_v,
\qquad BB^{\mathsf T}=B^{\mathsf T}B=s^2I+\lambda J,
\]
with \(k^2=s^2+\lambda v\). The second identity for columns follows also from the singular-value decomposition: the first identity and invertibility imply that the singular values of \(B\) are \(k\) once and \(s\) on the common orthogonal complements. Thus
\[
D\mathbf1_v=D^{\mathsf T}\mathbf1_v=0,\quad
DD^{\mathsf T}=D^{\mathsf T}D=s^2C,\quad CD=DC=D.
\]
Since \(k\ge2\), the parameter equation forces \(\lambda\ge1\), so \(0<s<k\). Therefore \(A\) has exactly the four eigenvalues \(\pm k\) (each once) and \(\pm s\) (each with multiplicity \(v-1\)).

**2. All four orthogonal spectral projectors.** Direct multiplication using the identities above verifies that the projectors for eigenvalues \(\pm k\) and \(\pm s\), respectively, are
\[
P_{\pm k}=\frac12\begin{pmatrix}E&\pm E\\\pm E&E\end{pmatrix},\qquad
P_{\pm s}=\frac12\begin{pmatrix}C&\pm D/s\\\pm D^{\mathsf T}/s&C\end{pmatrix}.
\]
They are pairwise orthogonal idempotents, sum to the identity, and satisfy \(AP_{\pm k}=\pm kP_{\pm k}\) and \(AP_{\pm s}=\pm sP_{\pm s}\). Hence they exhaust the spectrum, including the high-multiplicity eigenspaces. No eigenvalue collision is being silently separated.

**3. The exact probability matrix.** For a finite real symmetric Hamiltonian, averaging the exponential spectral expansion eliminates terms between unequal eigenvalues and yields \(\widehat M=\sum_\theta P_\theta\circ P_\theta\), where \(\circ\) denotes entrywise multiplication. Adding the four Schur squares above produces
\[
\widehat M=\begin{pmatrix}X&Y\\Y^{\mathsf T}&X\end{pmatrix},\qquad
X=\frac{v-2}{2v}I+\frac1{v^2}J,
\quad Y=\alpha B+\beta J,
\]
where
\[
\alpha=\frac{v-2k}{2v(k-\lambda)},\qquad
\beta=\frac{k^2+k-\lambda}{2(k-\lambda)v^2}.
\]
Thus the average return probability is \((v^2-2v+2)/(2v^2)\), distinct same-side vertices have average transition probability \(1/v^2\), and cross-side probabilities are \(\alpha+\beta\) on incident pairs and \(\beta\) otherwise. This also establishes the trace formula. From \(k^2=s^2+\lambda v\), one checks \(X\mathbf1_v=Y\mathbf1_v=\mathbf1_v/2\), so the global constant and the bipartition-sign vectors have eigenvalues \(1\) and \(0\).

**4. The remaining \(2(v-1)\) modes.** On \(\mathbf1_v^\perp\oplus\mathbf1_v^\perp\), \(J\) vanishes and \(B=D\) has every singular value equal to \(s\). Consequently \(\widehat M\) acts there as
\[
\begin{pmatrix}cI&\alpha D\\\alpha D^{\mathsf T}&cI\end{pmatrix},
\]
whose eigenvalues are \(c+|\alpha|s\) and \(c-|\alpha|s\), each of multiplicity \(v-1\). This proves the complete spectrum, with \(|\alpha|s=d\). The displayed eigenvalues plus the two constant-sector eigenvalues account for all \(2v\) dimensions.

**5. Kernel and sharp positivity boundary.** If \(2\le k\le v-2\), then \(|v-2k|\le v-4\) and \(s^2=k-\lambda\ge1\), whence
\[
c-d=\frac{v-2-|v-2k|/s}{2v}
\ge\frac{v-2-(v-4)}{2v}=\frac1v>0.
\]
Therefore exactly one zero eigenvector remains, the bipartition sign vector, and the lower spectral value \(c-d\) is the smallest positive eigenvalue because \(c+d<1\). The bound \(c-d\ge1/v\) holds for all nontrivial designs (and is separate from the exact sharp value).

If \(k=v-1\), the missing incidences form a permutation matrix \(P=J-B\), while \(s=1\) and \(d=c\). Here the kernel can be written exactly as \(\{(u,-P^{\mathsf T}u):u\in\mathbb R^v\}\), of dimension \(v\), and the nonzero spectrum is \(1\) once and \((v-2)/v\) with multiplicity \(v-1\). This includes \(v=3\), whose incidence graph is the six-cycle.

**6. Equivalence with the four-eigenvalue bipartite regular class.** Conversely, let \(G\) be a connected \(k\)-regular bipartite graph with exactly four distinct adjacency eigenvalues. Its two color classes each have \(v\) vertices, and its biadjacency matrix \(B\) is square. Bipartite symmetry and connected regularity give adjacency eigenvalues \(\pm k,\pm s\) with \(0<s<k\); the high singular value \(k\) is simple. Hence \(BB^{\mathsf T}=s^2 I+(k^2-s^2)J/v\). Diagonal entries are \(k\), so all off-diagonal entries equal the integer \(\lambda=k-s^2\). Thus any two points occur together in exactly \(\lambda\) blocks, and \(B\) is the incidence matrix of a symmetric design. This establishes the asserted equivalence without presupposing distance regularity.

## Verification
Run the standalone standard-library script `verify.py` with `python3 verify.py`. It constructs five cyclic symmetric designs with parameters \((v,k,\lambda)=(3,2,1),(4,3,2),(7,3,1),(11,5,2),(13,4,1)\), checks the design and projector identities using exact rational arithmetic, reconstructs the average-mixing matrix independently from grouped spectral Schur squares, verifies the closed block formula and its annihilating spectral polynomial, and computes exact ranks by Gaussian elimination. Expected output begins with `VERIFY_OK exact_designs=5` and ends with ranks `3:3,4:4,7:13,11:21,13:25`. These finite cases corroborate, but do not prove, the general argument.

## Relationship to prior work
Godsil (2011/2013) established the general Cesàro projector-Schur-square identity, positivity, and rationality, together with formulas for other graph families. Coutinho, Godsil, Guo, and Zhan (2017/2018) related average-mixing rank to projection onto the adjacency commutant. Coutinho, Baptista, Godsil, Spier, and Werner (first posted 2022) developed exact algebraic procedures for computing arbitrary integral-Hamiltonian quantum walks. Abiad, Dalfó, and Fiol (2013) characterized regular bipartite four-eigenvalue graphs as distance-regular, consistent with the incidence-design equivalence proved directly above. The present statement is the complete **parameter-uniform Cesàro spectrum and rank/positivity boundary** for that class; it does not claim any of the general projector methods or the classical symmetric-design spectrum as new.

## Limitations
The theorem concerns the infinite-time Cesàro average, not instantaneous mixing, finite observation times, or independently randomized-time sampling. The small positive spectral mode can shrink with the design parameters. It makes no statement about non-symmetric designs or about uniform mixing in the usual sense. There may be an unlocated general association-scheme result that implies the formula; a targeted primary-literature comparison did not establish universal novelty. Finite verifier cases are not a substitute for the proof. Independent mathematical audit has not been performed.

## References
- C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578v1 (2011), Journal of Combinatorial Theory A 120 (2013), 1649–1662. https://arxiv.org/abs/1103.2578
- G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (2017), Electronic Journal of Combinatorics 25 (2018), P4.14. https://arxiv.org/abs/1709.03591
- G. Coutinho, P. Ferreira Baptista, C. Godsil, T. Jung Spier, R. Werner, *Irrational Quantum Walks*, arXiv:2208.08971v1 (first posted 2022-08-18), SIAM Journal on Applied Algebra and Geometry 7 (2023), 567–584. https://arxiv.org/abs/2208.08971
- A. Abiad, C. Dalfó, M. A. Fiol, *Algebraic characterizations of regularity properties in bipartite graphs*, European Journal of Combinatorics 34 (2013), 1223–1231. https://doi.org/10.1016/j.ejc.2013.05.006
- P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (2023). https://arxiv.org/abs/2308.16378
