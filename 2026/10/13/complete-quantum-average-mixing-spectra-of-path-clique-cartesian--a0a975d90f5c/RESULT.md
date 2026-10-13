# Complete quantum average-mixing spectra of path–clique Cartesian strips

## Finding
Let \(G_{m,q}=P_m\square K_q\) be the unweighted Cartesian product of a path on \(m\ge2\) vertices with a complete graph on \(q\ge2\) vertices. Let \(\widehat M(G_{m,q})\) be the infinite-time average mixing matrix of the adjacency-generated continuous-time quantum walk. Set \(L=m+1\), \(r=\lceil m/2\rceil\), \(f=\lfloor m/2\rfloor\), let \(J_a\) be the all-ones matrix, and let \(F_m\) reverse the path coordinates. Define
\[
B_m=\frac{2J_m+I_m+F_m}{2L},\qquad
C_q=\left(1-\frac2q\right)I_q+\frac{2}{q^2}J_q.
\]
**Theorem.** For all integers \(m,q\ge2\), the following are exact identities and full multisets of eigenvalues, including all multiplicities.

**(i) Clique width \(q\ge3\).** There are no cross-sector adjacency eigenvalue coincidences, and
\[
\widehat M(G_{m,q})=B_m\otimes C_q.
\]
Writing \(\beta_q=(q-2)/q\), the average-mixing eigenvalues (value, multiplicity) are
\[
(1,1),\quad (1/L,r-1),\quad (\beta_q,q-1),\quad (\beta_q/L,(r-1)(q-1)),\quad(0,qf).
\]
If two displayed positive numerical values coincide, their multiplicities are added. In particular \(\operatorname{rank}\widehat M(G_{m,q})=q\lceil m/2\rceil\).

**(ii) Ladder width \(q=2\).** Put
\[
P_\pm=\frac12\begin{pmatrix}1&\pm1\\\pm1&1\end{pmatrix},\qquad
(w_m)_x=\frac2L\sin\!\left(\frac{\pi x}{3}\right)\sin\!\left(\frac{2\pi x}{3}\right)
\quad(1\le x\le m).
\]
Then
\[
\widehat M(G_{m,2})=B_m\otimes P_++\mathbf1_{\{3\mid L\}}w_mw_m^{\mathsf T}\otimes P_-.
\]
If \(3\mid L\), \(\|w_m\|^2=3/(2L)\). Its complete eigenvalue multiset is \((1,1)\), \((1/L,r-1)\), \((3/(2L),1)\) if \(3\mid L\), and zero with multiplicity \(2m-r-\mathbf1_{\{3\mid L\}}\). In particular
\[
\operatorname{rank}\widehat M(G_{m,2})=\left\lceil\frac m2\right\rceil+\mathbf1_{\{3\mid(m+1)\}}.
\]
Hence the ladder graph has exactly one isolated rank revival whenever \(m\equiv2\pmod3\). For example, \(P_5\square K_2\) has rank \(4\) on \(10\) vertices.

## Assumptions and scope
All graphs are finite, simple, unweighted and undirected. \(P_m\) has edges between consecutive coordinates \(1,\ldots,m\); \(K_q\) has unit off-diagonal adjacency entries. The Hamiltonian is the ordinary adjacency matrix (not the Laplacian). For any adjacency matrix \(A\), put \(U(t)=e^{itA}\) and
\[
\widehat M=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ\overline{U(t)}\,dt,
\]
with \(\circ\) denoting the Hadamard product. Each entry of the limit exists because it is a finite trigonometric sum. Tensor factors are ordered path first, clique second.

## Proof
**1. Spectral projectors.** The path has pairwise distinct eigenvalues and normalized eigenvectors
\[
\lambda_j=2\cos\left(\frac{\pi j}{L}\right),\qquad
v_j(x)=\sqrt{\frac2L}\sin\left(\frac{\pi jx}{L}\right),\qquad1\le j,x\le m.
\]
Write \(E_j=v_jv_j^{\mathsf T}\). The complete graph has eigenvalues \(q-1\) and \(-1\) with orthogonal projectors \(Q_+=J_q/q\) and \(Q_-=I_q-J_q/q\). Thus its product Hamiltonian has eigenvalues \(\lambda_j+q-1\) on \(E_j\otimes Q_+\) and \(\lambda_j-1\) on \(E_j\otimes Q_-\). Coincidences within either sector require identical \(j\).

**2. Exhaustive cross-sector coincidences.** A cross-sector coincidence requires \(\lambda_j-\lambda_k=q\). Each path eigenvalue is an algebraic integer in the real cyclotomic field, and every algebraic conjugate has absolute value strictly below \(2\). Applying any field embedding to the displayed equation, and using \(-2<\sigma(\lambda_k),\sigma(\lambda_j)<2\), forces \(q<4\). For \(q=3\), the algebraic integer \(\alpha=\lambda_j-1\) has every conjugate strictly between \(0\) and \(1\), contradicting that its nonzero norm is an integer. For \(q=2\), the same \(\alpha\) has all conjugates strictly between \(-1\) and \(1\), so its integral norm forces \(\alpha=0\). Therefore \(\lambda_j=1\), \(\lambda_k=-1\), equivalently \(j=L/3\), \(k=2L/3\), which occur precisely when \(3\mid L\). These are the only collisions. (The argument uses the absolute norm of an algebraic integer in its number field, and makes no inference from merely sampling finitely many path orders.)

**3. Average-mixing projector formula.** If \(A=\sum_\theta\theta R_\theta\), then Fourier integration of \(U(t)\circ\overline{U(t)}\) gives
\[
\widehat M=\sum_\theta R_\theta\circ R_\theta.
\]
In the absence of cross-sector coincidences this becomes
\[
\left(\sum_{j=1}^{m}E_j\circ E_j\right)\otimes
\left(Q_+\circ Q_+ +Q_-\circ Q_-\right)=B_m\otimes C_q.
\]
The clique identity follows directly from \(Q_+=J_q/q\). To see the path identity, expand \(v_j(x)^2v_j(y)^2\) using \(\sin^2 z=(1-\cos(2z))/2\) and sum over \(j=1,\ldots,L-1\) using root-of-unity orthogonality. The result is \((2+\mathbf1_{x=y}+\mathbf1_{x+y=L})/(2L)\), exactly \((B_m)_{xy}\). This includes the central fixed point when \(m\) is odd.

When \(q=2\) and \(3\mid L\), the two distinct product sectors with the common eigenvalue zero merge into the projector \(E_{L/3}\otimes Q_-+E_{2L/3}\otimes Q_+\) (or vice versa according to ordering). The additional Hadamard cross term is
\[
2(E_{L/3}\circ E_{2L/3})\otimes(Q_+\circ Q_-)=w_mw_m^{\mathsf T}\otimes P_-,
\]
since \(2(Q_+\circ Q_-)=P_-\) and \((E_{L/3}\circ E_{2L/3})_{xy}=w_m(x)w_m(y)\). For \(3\mid L\), \(w_m(x)=0\) on multiples of \(3\), and its square equals \(9/(4L^2)\) elsewhere; among \(1,\ldots,L-1\), exactly \(2L/3\) indices are not multiples of \(3\). Hence \(\|w_m\|^2=3/(2L)\).

**4. Spectrum and ranks.** The reversal-symmetric subspace of \(\mathbb R^m\) has dimension \(r\), contains \(\mathbf1_m\), and has \(B_m\)-eigenvalues \(1\) on constants and \(1/L\) on its orthogonal complement. The reversal-antisymmetric subspace has dimension \(f\) and eigenvalue zero. The matrix \(C_q\) has eigenvalue \(1\) on constants and \((q-2)/q\) on its \((q-1)\)-dimensional orthogonal complement. Tensoring proves (i). For \(q=2\), \(P_+\) and \(P_-\) are orthogonal and the two summands act on disjoint sectors, so their spectra union without cancellation. The rank-one correction has eigenvalue \(\|w_m\|^2=3/(2L)\) in the \(P_-\) sector, completing (ii).

## Verification
The accompanying executable `verify.py` (Python 3 with NumPy and SymPy) reconstructs adjacency matrices directly from graph edges, constructs their spectral projectors from independently determined eigenvectors/eigenvalues, and compares the entire average-mixing matrices and spectra to the formulas. Exact rational calculations cover six small parameter pairs and \(494\) entries; additional double-precision checks cover \(85\) pairs with \(2\le m\le18\), \(2\le q\le6\), including the resonant cases. The observed maximum absolute matrix discrepancy is about \(1.32\times10^{-15}\). These are supplementary checks; the proof above applies to every pair of allowed integers.

## Relationship to prior work
The general Hadamard-square spectral-projector formula and the explicit path average-mixing matrix appear in Godsil, *Average mixing of continuous quantum walks* (arXiv:1103.2578). Lo et al., *Mixing of Quantum Walk on Circulant Bunkbeds* (arXiv:quant-ph/0509059), Section 5, already examine the **same Cartesian-product objects** \(P_m\square C\) for circulant \(C\), including complete graphs as circulants. Their result concerns asymptotic **average uniform mixing** for fixed factor sizes, using eigenfunction expansions; it does not give this complete fixed-graph average-mixing spectrum, the explicit rank formula, or the isolated ladder resonance. Baptista, Coutinho and Marques, *Unexpected Averages of Mixing Matrices* (arXiv:2308.16378), Section 5, study general Cartesian products and obtain a trace-covariance relation, but not the present matrix and spectral identities. Coutinho et al., *Irrational quantum walks* (arXiv:2208.08971), develop exact average-mixing methods, motivating exact graph-family calculations.

## Limitations
This is a classification for adjacency-generated walks only, on \(P_m\square K_q\) with \(m,q\ge2\); weighted/Laplacian variants and other graph products are not covered. The result uses known spectral/projector ingredients, and an equivalent deduction might exist in less readily indexed graph-product literature. No independent external audit is claimed.

## References
1. P. Lo, S. Rajaram, D. Schepens, D. Sullivan, C. Tamon and J. Ward, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059v1 (2005), especially Section 5, https://arxiv.org/pdf/quant-ph/0509059.
2. C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578, https://arxiv.org/abs/1103.2578.
3. P. Baptista, G. Coutinho and V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (2023), Section 5, https://arxiv.org/html/2308.16378v1.
4. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier and R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first publicly available 2022-08-18), https://arxiv.org/abs/2208.08971.
