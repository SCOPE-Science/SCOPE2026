# Discrete log-concavity exactly controls partial-transpose inertia in a canonical qubit–qudit simplex
## Finding
For every integer \(n\ge 2\), set
\[
|\psi_k\rangle=\frac{|0,k+1\rangle-|1,k\rangle}{\sqrt2},\qquad 0\le k\le n-2,
\]
in \(\mathbb C^2\otimes\mathbb C^n\). For strictly positive probabilities \(p_0,\ldots,p_{n-2}\), define
\[
\rho_p=\sum_{k=0}^{n-2}p_k|\psi_k\rangle\langle\psi_k|,
\qquad p_{-1}=p_{n-1}=0.
\]
Let \(L,E,V\) be the numbers of indices \(k\in\{0,\ldots,n-2\}\) for which, respectively,
\[
p_k^2>p_{k-1}p_{k+1},\qquad
p_k^2=p_{k-1}p_{k+1},\qquad
p_k^2<p_{k-1}p_{k+1}.
\]
Then the partial transpose of \(\rho_p\) has exact inertia
\[
(\nu_+,\nu_0,\nu_-)=(n+1+V,E,L).
\]
Consequently it has the maximal possible \(n-1\) negative eigenvalues exactly when the augmented positive weight sequence is strictly log-concave at every displayed index. In particular the normalized binomial weights
\[
p_k=2^{-(n-2)}\binom{n-2}{k}
\]
give an elementary closed-form maximal-inertia state in every \(2\otimes n\) dimension, whereas any normalized positive geometric progression has exactly two negative eigenvalues and \(n-3\) zero eigenvalues when \(n\ge3\).

Thus, on this natural diagonal simplex, the number of negative partial-transpose eigenvalues is a discrete-curvature statistic of the probability weights. The endpoint inequalities are automatic because of the zero boundary convention; the interior inequalities are precisely strict log-concavity.

## Assumptions and scope
The result concerns the diagonal mixtures of the displayed nearest-neighbor antisymmetric vectors only. The weights are strictly positive, normalized by \(\sum_{k=0}^{n-2}p_k=1\), and partial transposition is taken on the qubit factor. Transposing the other factor gives the same spectrum.

The vectors span the \(2\otimes n\) specialization of standard maximal completely-entangled/NPT-subspace constructions. Cubitt, Montanaro, and Winter give explicit maximal Schmidt-rank subspaces; Johnston later proves that a maximal NPT subspace exists and that the universal negative-eigenvalue bound is tight. The statement here is finer: it classifies the entire inertia of this diagonal family directly from its weights.

## Proof
Partial transposition on the first factor gives
\[
\rho_p^\Gamma
=\frac12\sum_{k=0}^{n-2}p_k\left(
|0,k+1\rangle\langle0,k+1|
+|1,k\rangle\langle1,k|
-|1,k+1\rangle\langle0,k|
-|0,k\rangle\langle1,k+1|
\right).
\]
After reordering the product basis, there are two positive singleton blocks, with eigenvalues \(p_0/2\) and \(p_{n-2}/2\), together with \(n-1\) independent \(2\times2\) blocks
\[
B_k=\frac12
\begin{pmatrix}
p_{k-1}&-p_k\\
-p_k&p_{k+1}
\end{pmatrix},
\qquad 0\le k\le n-2.
\]
Their eigenvalues are
\[
\lambda_{k,\pm}
=\frac14\left(
p_{k-1}+p_{k+1}
\pm
\sqrt{(p_{k-1}-p_{k+1})^2+4p_k^2}
\right).
\]
Every block has strictly positive trace, while
\[
\det B_k=\frac14\left(p_{k-1}p_{k+1}-p_k^2\right).
\]
Therefore \(B_k\) has one positive and one negative eigenvalue exactly when \(p_k^2>p_{k-1}p_{k+1}\); one positive and one zero eigenvalue exactly at equality; and two positive eigenvalues exactly when \(p_k^2<p_{k-1}p_{k+1}\). Summing all block contributions gives
\[
\nu_-=L,\qquad \nu_0=E,\qquad \nu_+=2+L+E+2V=n+1+V.
\]

Rana's theorem bounds the number of negative eigenvalues of a \(2\otimes n\) partial transpose by \(n-1\), and Johnston proves this bound is globally attainable. In the present family, attaining \(n-1\) is therefore equivalent to \(L=n-1\), namely strict log-concavity of the augmented weights.

For the binomial choice, put \(N=n-2\). At each interior index \(1\le k\le N-1\),
\[
\frac{\binom{N}{k}^2}{\binom{N}{k-1}\binom{N}{k+1}}
=
\frac{(N-k+1)(k+1)}{k(N-k)}>1.
\]
The endpoint inequalities are strict because \(p_{-1}=p_{n-1}=0\), so the inertia is
\[
(n+1,0,n-1).
\]
For a positive geometric progression, every interior index satisfies \(p_k^2=p_{k-1}p_{k+1}\), while the two endpoint inequalities remain strict. Thus, for \(n\ge3\), its inertia is
\[
(n+1,n-3,2).
\]

## Verification
The bundled `verify_inertia.py` reconstructs the partial transpose entry-by-entry over exact rational arithmetic, checks the stated block decomposition, and verifies the determinant-sign classification. It also checks the binomial and geometric corollaries for a range of dimensions using exact integers and fractions. These finite replays are consistency checks only; the all-\(n\) result follows from the analytic block decomposition and determinant argument above.

## Relationship to prior work
Cubitt, Montanaro, and Winter construct maximal subspaces with prescribed lower Schmidt rank, including the maximal completely-entangled case. Rana proves the universal upper bound on partial-transpose negative-eigenvalue counts. Johnston proves global tightness and gives a semidefinite-programming construction of a state attaining the bound, while also exhibiting a maximal NPT subspace. The 2019 non-\(m\)-positive-dimension framework recasts the maximal count as a property of the transpose map.

None of those inspected statements classifies the inertia of the diagonal nearest-neighbor mixture by local inequalities among its probabilities. In particular, existence of some maximal-inertia state does not imply that strict log-concavity is necessary and sufficient inside this simplex, nor does it imply the geometric-progression zero-mode boundary.

## Limitations
The theorem does not classify arbitrary states supported on the same subspace, coherent mixtures in the displayed basis, or \(m\otimes n\) systems with \(m>2\). It concerns inertia, not the magnitudes of the negative eigenvalues or the negativity. An obscure or poorly indexed source could conceivably contain the same diagonal-family observation; targeted searches and the closest full-text sources inspected did not locate one.

## References
1. T. S. Cubitt, A. Montanaro, A. Winter, *On the dimension of subspaces with bounded Schmidt rank*, arXiv:0706.0705; J. Math. Phys. 49, 022107 (2008).
2. S. Rana, *Negative eigenvalues of partial transposition of arbitrary bipartite states*, arXiv:1304.6775; Phys. Rev. A 87, 054301 (2013).
3. N. Johnston, *Non-Positive Partial Transpose Subspaces Can be as Large as Any Entangled Subspace*, arXiv:1305.0257; Phys. Rev. A 87, 064302 (2013).
4. N. Johnston, B. Lovitz, D. Puzzuoli, *The Non-m-Positive Dimension of a Positive Linear Map*, arXiv:1906.04517; Quantum 3, 172 (2019).
