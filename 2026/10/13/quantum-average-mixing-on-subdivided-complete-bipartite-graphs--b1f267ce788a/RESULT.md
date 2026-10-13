# Quantum average mixing on subdivided complete bipartite graphs

## Finding

Let \(a,b\) be arbitrary positive integers. Start with the unweighted complete bipartite graph \(K_{a,b}\), and replace every edge with a two-edge path containing a new midpoint. Denote the resulting graph by \(X_{a,b}=S(K_{a,b})\). Its adjacency matrix \(H\), with original vertices ordered before the \(ab\) edge-midpoint vertices, generates the continuous-time walk \(U(t)=e^{itH}\). Define its Cesàro average mixing matrix by

\[
\widehat M_{a,b}=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ U(-t)\,dt.
\]

The complete rank classification is

\[
\boxed{\operatorname{rank}\widehat M_{a,b}=a+b+ab-\nu(a,b)},\qquad
\nu(a,b)=\begin{cases}
0,&s\ge3,\\
t+1,&s=2,\ t\ge3,\\
4,&s=t=2,\\
t-1,&s=1,\ t\ge3,\\
2,&s=1,\ t=2,\\
1,&s=t=1,
\end{cases}
\]
where \(s=\min\{a,b\}\) and \(t=\max\{a,b\}\). In particular, the Cesàro average mixing matrix of a subdivided complete bipartite graph is strictly positive definite **if and only if both original part sizes are at least three**.

In addition to the rank, the theorem gives a closed rational matrix expression and an explicit description of every kernel vector, including all small-part boundaries. The formula below applies to every positive pair \((a,b)\), whether or not \(a=b\).

## Assumptions and scope

The Hamiltonian is the *unweighted adjacency matrix* of the finite, simple, once-subdivided complete bipartite graph. The limit is uniform continuous-time Cesàro averaging, not a discrete-time Grover walk or the normalized adjacency/Laplacian walk. All eigenvalues and projectors are real and orthogonal. There are no asymptotic, genericity, primality, or parity restrictions on \(a,b\).

Let \(J_m=\mathbf1_m\mathbf1_m^{\mathsf T}\), \(D_m=I_m-J_m/m\), and \(S_m=D_m\circ D_m\) for each positive integer \(m\). In particular,
\[
S_m=\left(1-\frac2m\right)I_m+\frac1{m^2}J_m.
\]
For \(m=1\), this matrix is zero; for \(m=2\), it is \(J_2/4\); for \(m\ge3\), it is positive definite with eigenvalues \((m-1)/m\) on constants and \((m-2)/m\) on their orthogonal complement.

Identify the midpoint coordinates with arrays \(Z\in\mathbb R^{a\times b}\), vectorized by the first index and then the second. Write vectors on all graph vertices as \((x,y,Z)\), with \(x\in\mathbb R^a\) and \(y\in\mathbb R^b\). Define the following maps from the original part spaces to the full vertex space:
\[
C_a u=(u,\,0,\,(u_i/b)_{ij}),\qquad
C_b v=(0,\,v,\,(v_j/a)_{ij}).
\]
Define the nonnegative vector
\[
z=\left(\frac{b}{a(a+b)}\mathbf1_a,\ \frac{a}{b(a+b)}\mathbf1_b,\ \frac1{ab}\mathbf1_{ab}\right).
\]
The matrix acts on the real coordinate space \(\mathbb R^{a+b+ab}\); the following notation uses the same block order.

## Proof

### 1. Explicit projector decomposition

Let \(B\) be the unsigned original-vertex/edge incidence matrix of \(K_{a,b}\), so that
\[
H=\begin{pmatrix}0&B\\B^{\mathsf T}&0\end{pmatrix},\qquad
BB^{\mathsf T}=\begin{pmatrix}bI_a&J_{a\times b}\\J_{b\times a}&aI_b\end{pmatrix}.
\]
The positive squared singular values of \(B\) are \(a+b\) (multiplicity one), \(b\) (multiplicity \(a-1\)), and \(a\) (multiplicity \(b-1\)); a zero singular value occurs in the original-vertex space once. Multiplicities with value zero are omitted. The two nontrivial squared singular values coincide exactly when \(a=b\).

Choose a left unit vector for \(\sqrt{a+b}\) having entries \(\sqrt{b/[a(a+b)]}\) on the first part and \(\sqrt{a/[b(a+b)]}\) on the second part; its right unit vector is constant \(1/\sqrt{ab}\) on the midpoint coordinates. The corresponding two adjacency projectors, at eigenvalues \(\pm\sqrt{a+b}\), have Schur squares summing to \(zz^{\mathsf T}/2\).

For the singular value \(\sqrt b\) associated with the first-part contrast space, the left projector is \(D_a\) on the first part and the right projector is \(D_a\otimes J_b/b\) on the midpoint space. The sum of Schur squares of the two adjacency projectors at \(\pm\sqrt b\), considered as a separate singular sector, equals \(C_aS_aC_a^{\mathsf T}/2\). Likewise the \(\sqrt a\) sector contributes \(C_bS_bC_b^{\mathsf T}/2\).

The zero eigenspace is the orthogonal direct sum of the line generated on original vertices by \((\mathbf1_a,-\mathbf1_b)/\sqrt{a+b}\), and the midpoint subspace \(\operatorname{im}(D_a\otimes D_b)\). Consequently the zero adjacency projector has Schur square
\[
\begin{pmatrix}
J_{a+b}/(a+b)^2&0\\0&S_a\otimes S_b
\end{pmatrix}.
\]
When \(a=b\), the \(\pm\sqrt a\) and \(\pm\sqrt b\) projectors for the two contrast sectors must first be combined **at each common eigenvalue**. Their Schur cross products are supported on the midpoint block and jointly contribute precisely \((D_a\otimes D_b)/(ab)\). Without this correction, treating the coinciding sectors as distinct eigenvalues would be incorrect.

The infinite-time identity \(\widehat M=\sum_\theta E_\theta\circ E_\theta\), with one projector per *distinct* adjacency eigenvalue, therefore yields the universal rational formula
\[
\boxed{\begin{aligned}
\widehat M_{a,b}={}&
\begin{pmatrix}J_{a+b}/(a+b)^2&0\\0&S_a\otimes S_b\end{pmatrix}
+\frac12zz^{\mathsf T}
+\frac12C_aS_aC_a^{\mathsf T}
+\frac12C_bS_bC_b^{\mathsf T}\\
&+\mathbf1_{\{a=b\}}
\begin{pmatrix}0&0\\0&(D_a\otimes D_b)/(ab)\end{pmatrix}.
\end{aligned}}
\]
Every summand is positive semidefinite, including the resonance correction, because \(D_a\) and \(D_b\) are orthogonal projections. The formula is an exact expression for **every** entry, not merely a matrix-rank characterization.

### 2. Kernel of the positive decomposition

For a positive-semidefinite sum, a vector lies in its kernel exactly when it lies in the kernel of each summand. For \((x,y,Z)\), the conditions are:

\[
\begin{gathered}
\mathbf1_a^{\mathsf T}x+\mathbf1_b^{\mathsf T}y=0,\qquad
(S_a\otimes S_b)\operatorname{vec}(Z)=0,\\
z^{\mathsf T}(x,y,Z)=0,\\
x+\frac1b Z\mathbf1_b\in\ker S_a,\qquad
y+\frac1a Z^{\mathsf T}\mathbf1_a\in\ker S_b,\\
(D_a\otimes D_b)\operatorname{vec}(Z)=0\quad\text{if }a=b.
\end{gathered}
\]
The last condition is absent when the two part sizes differ.

If \(a,b\ge3\), both \(S_a\) and \(S_b\) are positive definite. Their tensor product forces \(Z=0\), and the two lifted terms then force \(x=y=0\). This proves strict positive definiteness for the full two-parameter interior.

It remains to determine, rather than merely bound, the kernels at the boundary. By symmetry we may assume \(a\le b\). All the following descriptions are exact.

- **\(a=2<b\)**: every kernel vector has \(y=0\), \(\mathbf1_2^{\mathsf T}x=0\), and \(Z_{1j}+Z_{2j}=0\) for every \(j\). The first-part contrast has dimension one and the midpoint column contrasts have dimension \(b\), so the nullity is \(b+1\). Conversely, each vector satisfying these conditions annihilates every displayed positive summand.
- **\(a=b=2\)**: the kernel comprises \(\mathbf1_2^{\mathsf T}x=\mathbf1_2^{\mathsf T}y=0\), together with midpoint arrays \(Z\) that are sums of a row-contrast constant along columns and a column-contrast constant along rows. Equivalently, \(\sum_{ij}Z_{ij}=0\) and \(D_2ZD_2=0\). The dimensions are one, one, and two, yielding nullity four. The extra equal-singular-value correction is essential to exclude the fourth midpoint contrast direction.
- **\(a=1,b\ge3\)**: identifying \(Z\) with a row vector of length \(b\), the kernel is precisely \(x=0\), \(y=-Z^{\mathsf T}\), and \(Z\mathbf1_b=0\). Its dimension is \(b-1\).
- **\(a=1,b=2\)**: the kernel consists of \(x=0\), with \(y\) and the midpoint row \(Z\) independently orthogonal to \(\mathbf1_2\); its dimension is two.
- **\(a=b=1\)**: the graph is the three-vertex path, and the kernel is the line \(\{(x,-x,0):x\in\mathbb R\}\).

For example, when \(a=1,b\ge3\), the lifted second-part condition first gives \(y=-Z^{\mathsf T}\), while the original-constant condition gives \(x=Z\mathbf1_b\). Substitution into \(z^{\mathsf T}(x,y,Z)=0\) reduces it to \(Z\mathbf1_b=0\), establishing the stated form. The other cases follow by the stated eigenspace descriptions of \(S_1\) and \(S_2\) and, at \(a=b=2\), by the additional contrast-projector condition.

Subtracting the resulting nullities from the total vertex number \(a+b+ab\) proves the rank table. There are no missing degenerate or repeated-eigenvalue cases.

## Verification

An accompanying standalone Python/SymPy checker reconstructs the incidence adjacency matrix independently and obtains all spectral projectors from rational Lagrange interpolation in \(H^2\). For each positive squared adjacency eigenvalue \(\lambda\), let \(R_\lambda\) be the projector of \(H^2\) at \(\lambda\). Then the aggregate Schur squares at \(\pm\sqrt\lambda\) equal
\[
\frac12\left(R_\lambda\circ R_\lambda+\frac{(HR_\lambda)\circ(HR_\lambda)}\lambda\right).
\]
The zero sector is treated separately. This calculation *automatically handles* coinciding singular values and is algorithmically independent of the closed formula. For nine graph pairs, the script checks every matrix entry exactly against the closed expression, confirms row sums, and computes exact ranks for all instances of at most fifteen vertices. The successful run yielded:

`VERIFY_OK exact_pairs=9 exact_entries=1131 3_3_order=15 2_3_rank=7 1_3_rank=5`

Reproduce with `python verify_exact.py` after installing SymPy. This finite check supports the algebra but is not an exhaustive proof for all positive integers; the proof above supplies the unrestricted statement.

## Relationship to prior work

The general Schur-square identity, rationality and exact-computation framework for average mixing are due to Godsil (2013) and Coutinho–Baptista–Godsil–Spier–Werner (2022/2023). The commutant/rank viewpoint is due to Coutinho–Godsil–Guo–Zhan (2018). None of the relevant sections inspected in these sources states the two-parameter once-subdivided-biclique rank or kernel classification.

Chen's 2023 thesis, *Bipartite Quantum Walks and the Hamiltonian*, contains the usual subdivision-incidence adjacency spectral relations, but studies a **different discrete-time bipartite/Grover walk** when discussing average mixing. Its incidence-spectrum construction is compatible with the preliminary eigenvalue calculation here; it does not furnish this continuous-time adjacency Cesàro rank classification.

A related prior result treats the subdivision of the complete graph \(S(K_n)\), rather than \(S(K_{a,b})\). Those are different graph families; the two-parameter full-rank threshold and boundary kernels do not follow as special cases of the complete-graph formula. In contrast, the path cases \(S(K_{1,1})\) and \(S(K_{1,2})\) fall within the long-known path calculation, and are included for completeness rather than separately claimed as new.

## Limitations

The result concerns only once-subdivided **complete bipartite** graphs with the unweighted **adjacency** Hamiltonian and uniform continuous-time Cesàro averaging. It makes no assertion about subdivisions of arbitrary bipartite graphs, weighted couplings, normalized-Laplacian dynamics, mixing rates, or instantaneous uniform mixing. The general spectral-projector framework is known; the distinct contribution here is the complete structural two-parameter rank and kernel transition with an explicit rational formula. Literature searching and source inspections cannot exclude an equivalent formula hidden in broader published spectral literature; independent expert verification has not been performed.

## References

1. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public posting 2022-08-18); SIAM Journal on Applied Algebra and Geometry 7 (2023), 567–584; https://arxiv.org/abs/2208.08971; DOI:10.1137/22M1521262.
2. C. D. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578; Journal of Combinatorial Theory, Series A 120 (2013), 1649–1662; https://arxiv.org/abs/1103.2578.
3. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591; Electronic Journal of Combinatorics 25 (2018), P4.14; https://arxiv.org/abs/1709.03591.
4. Q. Chen, *Bipartite Quantum Walks and the Hamiltonian*, University of Waterloo thesis (2023), chapters 4–6; https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/4fe72fad-a681-474c-ae1e-8f9749dc0d98/content.
