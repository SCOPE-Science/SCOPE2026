# Exact generalized roundness and Euclidean snowflake rank of crown graph metrics

## Finding
Let \(\operatorname{Cr}_n=K_{n,n}\setminus M\), where \(n\ge3\) and \(M\) is a perfect matching, with its unit-edge shortest-path metric \(d\). Its supremal negative-type exponent (equivalently, generalized roundness) is
\[
\wp(\operatorname{Cr}_n)=
\begin{cases}
1,&n=3,4,\\
\rho_n,&n\ge5,
\end{cases}
\]
where \(\rho_n\in(0,1)\) is the unique solution of
\[
(n-1)(2^{\rho_n}-1)=3^{\rho_n}.
\]
For every \(p\ge0\), form the \(2n\)-square matrix \(D_p\) with diagonal entries zero and off-diagonal entries \(d(u,v)^p\). The *sharp attained normalized negative-type gap* is
\[
\Gamma_n(p):=\min_{z\ne0,\;\sum_i z_i=0}
\frac{-z^\mathsf{T}D_pz}{\lVert z\rVert_2^2}
=\min\bigl\{n+3^p-1-(n-1)2^p,\;1+2^p-3^p\bigr\}.
\]
Consequently the path metric itself has \(1\)-negative type exactly when \(n\le4\). The first failure in this family occurs at \(n=5\) (ten vertices), and the bipartition sign vector gives the explicit violation
\[
z^\mathsf{T}D_1z=2n(n-4)>0\quad(n\ge5).
\]
For \(0\le p<\wp\), the snowflaked metric \(d^{p/2}\) requires Euclidean embedding dimension \(2n-1\). At the endpoint \(p=\wp\), the minimum dimension drops to \(3\) when \(n=3,4\), and to \(2n-2\) when \(n\ge5\).

The matching deletion strictly *increases* supremal negative type compared with the complete bipartite graph on the same two parts:
\[
\wp(\operatorname{Cr}_n)>\wp(K_{n,n})=\log_2\!\left(\frac{n}{n-1}\right).
\]
Writing \(N=n-1\), the improvement satisfies
\[
\wp(\operatorname{Cr}_n)-\wp(K_{n,n})
=\frac{\log3}{(\log2)^2N^2}+O(N^{-3})\qquad(n\to\infty).
\]

## Assumptions and scope
All graphs are finite, simple, unweighted, and connected. The crown graph has two labeled parts \(\{a_1,\ldots,a_n\}\), \(\{b_1,\ldots,b_n\}\), and edges \(a_ib_j\) exactly for \(i\ne j\). We require \(n\ge3\); the cases \(n=1,2\) are disconnected and have no finite shortest-path metric on all vertices. For \(p=0\), the power-distance matrix convention is that its diagonal is zero and all off-diagonal entries are one. Negative type means \(z^\mathsf{T}D_pz\le0\) for every real zero-sum vector \(z\). Strict negative type means strict inequality for every nonzero such vector. The least Euclidean dimension is for an *isometric* realization of \(d^{p/2}\), not an embedding of the graph's edges or an embedding up to distortion.

## Proof
**Step 1: distances.** Distinct vertices in the same part are distance \(2\), unmatched cross-part vertices are distance \(1\), and the matched pair \((a_i,b_i)\) has distance \(3\). The last statement uses any two distinct indices other than \(i\) to obtain a three-edge path, possible because \(n\ge3\); bipartiteness excludes length two and the missing matching excludes length one. With \(a=2^p\) and \(b=3^p\), the powered distance matrix in part order is
\[
D_p=\begin{pmatrix}
a(J-I)&J+(b-1)I\\
J+(b-1)I&a(J-I)
\end{pmatrix},
\]
where \(I\) and \(J\) are the identity and all-ones matrices of order \(n\).

**Step 2: complete zero-sum eigenspace decomposition.** The zero-sum subspace splits orthogonally as
\[
\begin{aligned}
H_0&=\operatorname{span}\{(\mathbf1,-\mathbf1)\},\\
H_+&=\{(v,v):\mathbf1^\mathsf{T}v=0\},\\
H_-&=\{(v,-v):\mathbf1^\mathsf{T}v=0\}.
\end{aligned}
\]
Their dimensions are \(1,n-1,n-1\). Direct multiplication with the block matrix gives, respectively, the eigenvalues
\[
\lambda_0=(n-1)a-n-b+1,
\quad\lambda_+=b-a-1,
\quad\lambda_-=1-a-b.
\]
Since \(\lambda_+-\lambda_-=2(b-1)\ge0\), the largest restricted eigenvalue is \(\max\{\lambda_0,\lambda_+\}\). The Rayleigh quotient yields the displayed exact gap, attained on \(H_0\) or \(H_+\). In particular the formula does not rely on approximate diagonalization.

**Step 3: exponent classification.** If \(p>1\), strict convexity of real powers gives \(3^p>2^p+1\); hence \(\lambda_+>0\). For \(0\le p\le1\), concavity gives \(3^p\le2^p+1\), so \(\lambda_+\le0\), while \(\lambda_-<0\). The remaining criterion \(\lambda_0\le0\) is exactly
\[
h(p):=\frac{2^p-1}{3^p}\le\frac1{n-1}.
\]
For \(0\le p\le1\),
\[
h'(p)=\frac{\log3-2^p\log(3/2)}{3^p}>0,
\]
because the numerator is at least \(\log(4/3)>0\). Since \(h(0)=0\) and \(h(1)=1/3\), the claimed two regimes follow, with uniqueness of \(\rho_n\). All restricted eigenvalues are strictly negative below the critical value, and at least one becomes zero at it; for any larger exponent one becomes positive.

**Step 4: equality directions and Euclidean dimensions.** At \(n=3\), only \(H_+\) is the critical kernel (dimension \(2\)); at \(n=4\), both \(H_0\) and \(H_+\) are critical (total dimension \(4\)); at \(n\ge5\), only \(H_0\) is the critical kernel (dimension \(1\)). For every \(p\le\wp\), the doubly centered matrix \(-\tfrac12 P D_p P\), with \(P=I-(2n)^{-1}\mathbf1\mathbf1^\mathsf{T}\), is a positive-semidefinite Gram matrix for squared distances \(d^p\). Its rank is the least possible isometric Euclidean dimension. The above nullities in the \((2n-1)\)-dimensional zero-sum subspace give exactly the claimed ranks. At \(p<\wp\), strict negative type makes the rank full, \(2n-1\).

**Step 5: comparison and asymptotics.** The published complete-bipartite formula gives \(q_n=\log_2(n/(n-1))<1\). At \(p=q_n\), we have \((n-1)(2^p-1)=1<3^p\), so the strict monotonicity in Step 3 shows \(q_n<\wp(\operatorname{Cr}_n)\). For \(n\ge5\), put \(N=n-1\), \(L=\log2\), \(B=\log3\). The defining equation \(N(e^{L\rho}-1)=e^{B\rho}\), expanded at \(\rho=0\), gives
\[
\rho=\frac1{NL}+\frac{B/L^2-1/(2L)}{N^2}+O(N^{-3}).
\]
Subtracting \(q_n=\log(1+1/N)/L\) proves the asserted gap asymptotic. This is an asymptotic consequence of the exact scalar equation, not a numerically extrapolated claim.

## Verification
Run `python3 verify_crown.py` with standard Python 3. The program constructs graph distances independently by breadth-first search and compares them with the asserted \(1,2,3\) pattern; checks the zero-sum quadratic identity using exact integer and rational arithmetic at \(p=0,1\); checks noninteger exponents numerically; checks critical eigenvalue multiplicities, strict witnesses, and the asymptotic comparison. A completed run yielded 3,256 distance checks, 9,240 exact quadratic checks, 27,720 noninteger-exponent quadratic checks, and 11 checks each of transitions, endpoint ranks, and comparison inequalities. These bounded checks corroborate the universally quantified proof and do not establish it independently.

## Relationship to prior work
Sánchez's 2011 paper gives the finite negative-type framework and the complete-bipartite formula. Here, removing the entire matched pairing changes cross-part distances to a third level and yields a different, explicitly diagonalized family with a new scalar threshold, a sharp spectral gap, and endpoint Euclidean ranks. Horak and coauthors (2010) study *four-point roundness*, particularly cycles, but four-point roundness is not the all-coefficient negative-type condition used here; their cycle results do not determine the crown family for arbitrary \(n\). The classical Deza–Maehara work develops general Euclidean metric-transform methods, potentially including stronger unrecognized formulations; the complete text was not available for a definitive implication comparison. General finite-matrix criteria make this family computable in principle, but do not themselves state the displayed all-parameter classification or the matching-deletion comparison.

## Limitations
The theorem applies only to shortest-path metrics of connected crown graphs and their power transforms. It does not classify arbitrary matching deletions, nonuniform edge weights, or Banach-space distortion. The sharp gap refers to the full real zero-sum coefficient space with the Euclidean coefficient normalization in the definition, and the Euclidean-dimension claim concerns isometric snowflake embeddings, not graph realizations with prescribed edge placements.

## References
1. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, publicly posted 2011-08-02. https://arxiv.org/abs/1108.0451
2. Matthew Horak, Eric LaRose, Jessica Moore, Michael Rooney, Hannah Rosenthal, *Roundness properties of graphs*, Involve **3** (2010), 67–91. https://msp.org/involve/2010/3-1/involve-v3-n1-p05-p.pdf
3. Michel Deza and Hiroshi Maehara, *Metric transforms and Euclidean embeddings*, Transactions of the American Mathematical Society **317** (1990), 661–671. https://doi.org/10.1090/S0002-9947-1990-0974513-6
4. Jiří Matoušek, *On the distortion required for embedding finite metric spaces into normed spaces*, Israel Journal of Mathematics **93** (1996), 333–344. https://doi.org/10.1007/BF02761110
