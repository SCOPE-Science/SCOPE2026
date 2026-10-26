# Metric-to-complex-linear rigidity of weighted cubes in finite trace-class matrix spaces

## Finding
Fix an integer \(n\ge3\), weights \(w_1,\ldots,w_n>0\), and positive integers \(p,q\). The weighted Boolean cube \(Q_w=\{0,1\}^n\) carries the metric
\[
d_w(\varepsilon,\delta)=\sum_{i:\varepsilon_i\ne\delta_i} w_i.
\]
Write \(\|X\|_1=\operatorname{Tr}(X^*X)^{1/2}\) for the Schatten trace norm on \(M_{p,q}(\mathbb C)\). Every isometric embedding \(F:Q_w\to M_{p,q}(\mathbb C)\), without any linearity or normality assumption, has the form
\[
F(\varepsilon)=A_0+U\sum_{i=1}^{n}\varepsilon_iH_i,
\tag{1}
\]
where \(A_0\in M_{p,q}(\mathbb C)\), \(U:\mathbb C^q\to\mathbb C^p\) is a partial isometry, and each \(H_i\in M_q(\mathbb C)\) is positive semidefinite and nonzero, with
\[
\operatorname{Tr}H_i=w_i,\qquad H_iH_j=0\ \ (i\ne j),\qquad
\operatorname{supp}H_i\le U^*U.
\tag{2}
\]
Conversely all data satisfying (2) give an isometric map (1). Moreover,
\[
L(z_1,\ldots,z_n)=U\sum_i z_iH_i
\quad\text{satisfies}\quad
\|L(z)\|_1=\sum_i w_i|z_i|
\quad(z\in\mathbb C^n).
\tag{3}
\]
Thus every metric embedding is the restriction of a **complex-linear** isometry, not just a real-affine one. Existence in rectangular matrices is characterized exactly by
\[
Q_w\hookrightarrow (M_{p,q}(\mathbb C),\|\cdot\|_1)
\quad\Longleftrightarrow\quad \min\{p,q\}\ge n.
\tag{4}
\]
Every embedding satisfies \(\operatorname{rank}(F(\mathbf1)-F(\mathbf0))=\sum_i\operatorname{rank}H_i\ge n\). In the sharp square case \(p=q=n\), there are unitaries \(V,W\in M_n(\mathbb C)\) such that
\[
F(\varepsilon)=A_0+V\operatorname{diag}(w_1\varepsilon_1,\ldots,w_n\varepsilon_n)W^*.
\tag{5}
\]
No different nonlinear configurations occur.

## Assumptions and scope
The domain contains **all** \(2^n\) vertices and **all** weighted Hamming distances, and the coordinate weights are strictly positive. The target comprises arbitrary complex rectangular matrices. The partial isometry \(U\) has initial projection \(Q=U^*U\), and the support of a positive matrix is its range projection. The extension (3) is linear over \(\mathbb C\) and uses the weighted complex \(\ell_1\) norm. Only exact isometries are classified. The cases with fewer than three coordinates are excluded from the novelty claim because even-cycle special cases have already been studied.

## Proof
**Step 1: Equality in a trace-norm metric segment.** Let \(A=B+C\in M_{p,q}(\mathbb C)\), with \(\|A\|_1=\|B\|_1+\|C\|_1\). Write the canonical polar decomposition \(A=U|A|\), with \(U^*U\) the support of \(|A|\). Since \(\operatorname{Re}\operatorname{Tr}(U^*A)=\|A\|_1\), duality gives
\[
\operatorname{Re}\operatorname{Tr}(U^*B)=\|B\|_1,
\qquad \operatorname{Re}\operatorname{Tr}(U^*C)=\|C\|_1.
\]
If \(B=V|B|\) and \(v_j\) are unit eigenvectors of \(|B|\) with positive eigenvalues \(s_j\), then
\[
\sum_j s_j \operatorname{Re}\langle Uv_j,Vv_j\rangle
=\sum_j s_j.
\]
Every summand is at most \(s_j\), and equality forces \(Uv_j=Vv_j\) and \(v_j\in\operatorname{ran}(U^*U)\). Consequently \(B=U|B|\), with \(|B|\) supported under \(U^*U\). The same holds for \(C\), and \(|A|=|B|+|C|\). In particular, **every point on the trace-norm metric segment from zero to \(A\)** has the form \(UH\), where \(0\le H\le|A|\).

**Step 2: All vertices share one positive cone.** Translate so \(F(\mathbf0)=0\); write \(A=F(\mathbf1)\) and \(W=\sum_i w_i=\|A\|_1\). For every vertex \(\varepsilon\),
\[
\|F(\varepsilon)\|_1+\|A-F(\varepsilon)\|_1
=d_w(\mathbf0,\varepsilon)+d_w(\varepsilon,\mathbf1)=W.
\]
Step 1 supplies the **same** polar partial isometry \(U\) and a positive matrix \(H_\varepsilon\) satisfying
\[
F(\varepsilon)=UH_\varepsilon,\quad
0\le H_\varepsilon\le|A|,\quad
\operatorname{Tr}H_\varepsilon=\sum_{i:\varepsilon_i=1}w_i.
\tag{6}
\]
Because \(U\) is isometric on the common right-support subspace,
\[
\|H_\varepsilon-H_\delta\|_1
=\|F(\varepsilon)-F(\delta)\|_1
=d_w(\varepsilon,\delta).
\tag{7}
\]

**Step 3: Singleton supports are orthogonal.** Let \(P_i=H_{e_i}\), so \(P_i\ge0\) and \(\operatorname{Tr}P_i=w_i>0\). For distinct \(i,j\), (7) gives
\[
\|P_i-P_j\|_1=w_i+w_j=\operatorname{Tr}P_i+\operatorname{Tr}P_j.
\]
For positive \(P,Q\), this equality holds if and only if their supports are orthogonal. To see the nontrivial direction, norm \(P-Q\) by the self-adjoint contraction \(S=\operatorname{sgn}(P-Q)\). Equality forces both \(\operatorname{Tr}(SP)=\operatorname{Tr}P\) and \(\operatorname{Tr}((-S)Q)=\operatorname{Tr}Q\), hence \(S=I\) on \(\operatorname{ran}P\) and \(S=-I\) on \(\operatorname{ran}Q\). These eigenspaces are orthogonal. Thus \(P_iP_j=0\) when \(i\ne j\).

**Step 4: Every higher vertex is the sum of its atoms.** For any \(\varepsilon\) with active index set \(I=\{i:\varepsilon_i=1\}\), (6) and (7) give, for \(i\in I\),
\[
\|H_\varepsilon-P_i\|_1
=\sum_{j\in I\setminus\{i\}}w_j
=\operatorname{Tr}(H_\varepsilon-P_i).
\]
Because \(H_\varepsilon-P_i\) is Hermitian, trace norm equals its trace precisely when it is positive semidefinite. Hence \(H_\varepsilon\ge P_i\). Let \(E_i\) be the support projection of \(P_i\). These projections are mutually orthogonal. Therefore
\[
\operatorname{Tr}H_\varepsilon
\ge\sum_{i\in I}\operatorname{Tr}(E_iH_\varepsilon E_i)
\ge\sum_{i\in I}\operatorname{Tr}P_i
=\operatorname{Tr}H_\varepsilon.
\]
All inequalities are equalities. Positivity forces \(H_\varepsilon\) to have no support outside \(E=\sum_{i\in I}E_i\); for each \(i\in I\), the positive matrix \(D_i=H_\varepsilon-P_i\) has \(E_iD_iE_i=0\), hence \(D_iE_i=0\). Thus \(H_\varepsilon E_i=P_i\), and
\[
H_\varepsilon=\sum_{i\in I}P_i.
\]
Substituting into (6) proves the **complete representation** (1), with \(H_i=P_i\). Conversely, the orthogonal positive blocks make every difference trace norm equal its weighted Hamming distance.

**Step 5: Matrix-size threshold, complex extension, and sharp rigidity.** Orthogonality of the nonzero supports yields
\[
n\le\sum_i\operatorname{rank}H_i
=\operatorname{rank}\left(\sum_iH_i\right)
=\operatorname{rank}A\le\min\{p,q\}.
\]
When \(\min\{p,q\}\ge n\), choose orthonormal left and right families \((u_i)\subset\mathbb C^p\), \((v_i)\subset\mathbb C^q\) and put \(F(\varepsilon)=A_0+\sum_i w_i\varepsilon_i u_iv_i^*\); this attains (4). Because the blocks \(H_i\) have orthogonal supports, for all complex \(z_i\) the singular values of \(U\sum_i z_iH_i\) comprise those of \(|z_i|H_i\) over the blocks, giving (3). At \(p=q=n\), the \(n\) positive blocks must each have rank one; choosing their right unit vectors and corresponding left polar vectors gives the two unitaries in (5). This is a full classification, not merely an existence construction.

## Verification
The packaged `checker.py` uses deterministic seed `20261019` and NumPy to construct complex rectangular partial isometries and mutually orthogonal positive blocks, including genuinely higher-rank positive blocks. It checks all pairwise distances of sampled weighted cubes, together with exhaustive exact-integer diagonal witnesses for dimensions three through eight. Run `python checker.py` with NumPy installed. The reference execution passed **104,261 finite diagnostics**. These confirm only finite constructions; the necessity, universality and rigidity follow from Steps 1–5.

## Relationship to prior work
Jiao, Luo and Wu prove optimal-order metric-cotype scaling for the entire Schatten trace class and motivate exact finite-metric questions, but their general inequality neither forces every weighted cube isometry to be affine nor determines its rectangular matrix-size threshold. Xu, Zhang and Liu study existence and nonexistence of **complex-linear** isometric embeddings between Schatten-type spaces for various exponents; the classification here instead starts with a finite **nonlinear metric** map and forces a uniquely determined complex-linear extension with positive disjoint supports. Berleant and collaborators study isometries of weighted graphs into *Hamming graphs*, which are different targets. A previously known exact even-cycle trace-norm size obstruction also supplies the unweighted cube's lower bound by restriction to an isometric cycle; therefore **the bare unweighted bound is not asserted as new**. The further weighted, rectangular and every-embedding rigidity statements are the substantive distinctions.

## Limitations
No claim is made about approximate isometries, distortion below or above one, arbitrary finite graphs, nonbinary products, or Schatten exponents other than one. This is an exact finite-metric theorem. The special two-coordinate square is omitted from the novelty claim, and the unweighted size obstruction is not independently new. An older general theorem on trace-class equality or metric-to-linear extension might subsume the result under another terminology; the searches described in the accompanying review did not identify such coverage. Finite computations do not establish these infinite families of claims. Independent priority and proof review have not been performed.

## References
1. Y. Jiao, S. Luo, and L. Wu, *The Sharp Scale Inequality for the Schatten Trace Class*, arXiv:2610.21445v1, first public 2026-10-15, https://arxiv.org/abs/2610.21445.
2. Y. Xu, W. Zhang, and Q. Liu, *Further Results on the Isometric Embeddability of \(S_q^m\) into \(S_p^n\)*, arXiv:2609.37504v1, https://arxiv.org/html/2609.37504.
3. J. Berleant, K. Sheridan, A. Condon, V. Vassilevska Williams, and M. Bathe, *Isometric Hamming embeddings of weighted graphs*, arXiv:2112.06994v2, https://arxiv.org/html/2112.06994v2.
4. M. Junge, A. M. Kubicki, C. Palazuelos, and D. Pérez-García, *Geometry of Banach Spaces: A New Route Towards Position Based Cryptography*, Commun. Math. Phys. 394 (2022), 625–678, https://doi.org/10.1007/s00220-022-04407-9.
