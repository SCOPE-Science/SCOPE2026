# Complete overlap-code classification of moving two-digit holes

## Finding

Fix an integer \(b\ge 3\), a digit alphabet \(D=\{0,\ldots,b-1\}\), and an arbitrary infinite sequence of moving forbidden pairs \(w_k=(u_k,v_k)\in D^2\), indexed by \(k\ge0\). Let \(N_n(w)\) be the number of \(n\)-letter words extendible to an infinite sequence \((d_j)_{j\ge1}\) satisfying \((d_{k+1},d_{k+2})\ne(u_k,v_k)\) for every \(k\ge0\). Define the binary temporal overlap code
\[
\delta_k(w)=\mathbf1_{\{v_k=u_{k+1}\}},\qquad
H_b(t)=\begin{pmatrix}b&1\\-1&-t\end{pmatrix} \quad(t\in\{0,1\}).
\]
Then \(N_1=b\) and, for all integers \(n\ge2\),
\[
N_n(w)=(b,1)\left(\prod_{k=0}^{n-3}H_b(\delta_k(w))\right)
\begin{pmatrix}b\\-1\end{pmatrix},
\]
where the product is the identity when \(n=2\). Moreover, for any two moving-hole schedules \(w,\widetilde w\),
\[
\bigl(N_n(w)=N_n(\widetilde w)\ \text{for all }n\ge1\bigr)
\quad\Longleftrightarrow\quad
\bigl(\delta_k(w)=\delta_k(\widetilde w)\ \text{for all }k\ge0\bigr).
\]
Every infinite binary code occurs: choose \(u_k=0\), and \(v_k=0\) for \(\delta_k=1\) and \(v_k=1\) for \(\delta_k=0\). Thus the binary code is a *complete invariant* of every finite prefix-survival count, even for nonperiodic moving holes.

For the base-\(b\) projection of the survivor sequences into \([0,1]\), the existing dimension theorem of Kong–Sun–Wang yields
\[
\dim_H K_w=\liminf_{n\to\infty}\frac{\log N_n(w)}{n\log b},\qquad
\dim_P K_w=\limsup_{n\to\infty}\frac{\log N_n(w)}{n\log b}.
\]
In particular, equal overlap codes force equal Hausdorff and packing dimensions, although the actual forbidden pairs may differ at every time.

If the overlap code is periodic with a positive period \(p\), then both dimensions coincide and equal
\[
\frac{\log\lambda}{p\log b},\qquad
C=H_b(\delta_0)\cdots H_b(\delta_{p-1}),\qquad
\lambda=\frac{\operatorname{tr}C+
\sqrt{(\operatorname{tr}C)^2-4\det C}}2.
\]
This is valid even when the original forbidden-pair schedule itself is not periodic. At code period \(2\), the dimension has exactly three values, in strictly increasing order for \(m=\delta_0+\delta_1\in\{0,1,2\}\), given by the above root with
\[
\begin{array}{c|c|c}
m&\operatorname{tr} C&\det C\\\hline
0&b^2-2&1\\
1&b^2-2&1-b\\
2&b^2-1&(b-1)^2
\end{array}.
\]
These period-two values are special cases of previously available periodic-pattern spectral frameworks; the new statement is the *necessary-and-sufficient classification of all infinite moving schedules by their complete finite-prefix censuses*, together with its uniform rank-two reduction.

## Assumptions and scope

The alphabet has at least three digits, there is exactly one forbidden adjacent pair at each time, and the pairs may be chosen with no stationarity, periodicity, or regularity. The survivor set consists of **all-time** survivors, not trajectories avoiding the hole only eventually. All counts are extendible prefix counts: since each admissible prefix admits at least \(b-1\) choices for the next letter, every locally admissible finite word extends indefinitely. The geometric conclusions concern the homogeneous base-\(b\) projection, not an inhomogeneous iterated-function system. The cited source supplies the dimension-to-prefix-growth theorem; the rank-two and exact-code-classification assertions are established below.

## Proof

**1. Full transfer matrix and rank-two factorization.** Let \(\mathbf1\in\mathbb R^b\) be the all-ones column and \(e_j\) the \(j\)-th coordinate vector. The allowed consecutive-digit transition matrix at time \(k\) is
\[
A_k=\mathbf1\mathbf1^{T}-e_{u_k}e_{v_k}^{T}
=U_kV_k^{T},\quad
U_k=[\mathbf1,e_{u_k}],\quad
V_k=[\mathbf1,-e_{v_k}].
\]
There is one forbidden entry and all other entries equal one. The number of admissible \(n\)-prefixes is \(\mathbf1^T A_0\cdots A_{n-2}\mathbf1\) for \(n\ge2\). Direct multiplication gives
\[
\mathbf1^TU_0=(b,1),\quad
V_k^TU_{k+1}=\begin{pmatrix}b&1\\-1&-\delta_k\end{pmatrix},\quad
V_{n-2}^T\mathbf1=\begin{pmatrix}b\\-1\end{pmatrix}.
\]
Associativity yields the claimed formula, including the empty-product case \(N_2=b^2-1\).

**2. Necessity of the entire overlap code.** Write
\(R_j=(b,1)\prod_{k=0}^{j-1}H_b(\delta_k)=(a_j,c_j)\), with \(R_0=(b,1)\). Its update is
\[
a_{j+1}=ba_j-c_j,\qquad c_{j+1}=a_j-\delta_jc_j.
\]
Inductively \(a_j>c_j>0\): the inequalities hold at \(j=0\), while \(c_{j+1}\ge a_j-c_j>0\), and
\[
a_{j+1}-c_{j+1}=(b-1)a_j-(1-\delta_j)c_j>0.
\]
If two schedules have equal overlap bits through index \(j-1\), they share \(R_j\). Their next counts are \(N_{j+3}=R_jH_b(\delta_j)(b,-1)^T\). Switching \(\delta_j\) from zero to one increases this count by precisely \(c_j>0\). Therefore equality of all counts forces the next bit to agree. Induction proves the converse direction; the forward direction follows from the matrix product. The explicit all-zero-first-digit construction realizes every binary code, proving the asserted completeness.

**3. Periodic-code dimension.** Suppose \(\delta\) has period \(p\). Replace the possibly nonperiodic holes by their periodic representative \(w_k=(0,0)\) when \(\delta_k=1\), and \(w_k=(0,1)\) when \(\delta_k=0\); part 2 guarantees identical prefix counts. Let \(P=A_0\cdots A_{p-1}\) for this representative. For \(b\ge3\), any product of two allowed-transition matrices has all entries positive: each intermediate digit must avoid at most two exclusions, leaving at least one admissible choice. Therefore \(P\) is primitive (for \(p=1\), \(P^2>0\)); Perron–Frobenius theory gives the exponential prefix growth \(\rho(P)^{1/p}\). Since \(A_k=U_kV_k^T\), the nonzero eigenvalues of \(P\) are those of
\[
(V_{p-1}^{T}U_0)(V_0^TU_1)\cdots(V_{p-2}^{T}U_{p-1})
=H_b(\delta_{p-1})H_b(\delta_0)\cdots H_b(\delta_{p-2}).
\]
Cyclic permutation does not change this product's nonzero eigenvalues, so \(\rho(P)=\rho(C)=\lambda\). Perron dominance makes \(\lambda\) the larger real root of the quadratic characteristic polynomial of \(C\). The cited homogeneous moving-hole dimension formula turns the prefix-growth rate into the stated Hausdorff and packing dimensions.

**4. Two-period trichotomy.** Matrix multiplication gives the three trace/determinant pairs in the table. At \(m=0\) and \(m=1\), traces coincide while the determinant decreases from \(1\) to \(1-b\), so the Perron root increases. At \(m=2\), write the first-mixed root as \(\lambda_1\); it exceeds \(b^2-2>b(b-1)\) for \(b\ge3\). The monic characteristic polynomial at \(m=2\), evaluated at \(\lambda_1\), equals \(b(b-1)-\lambda_1<0\), so its larger root exceeds \(\lambda_1\). This proves strict increase. The order of overlap bits, not only their frequency, matters at longer periods: for period-four codes \(1100\) and \(1010\), the traces are respectively \(b^4-4b^2+2b+1\) and \(b^4-4b^2+2b+2\), while determinants are both \((b-1)^2\), hence the dimensions differ.

## Verification

Run the supplied standalone Python file `check.py` with a standard Python 3 interpreter. It exhaustively enumerates all moving-pair sequences of lengths needed for \((b,n)=(3,3),(3,4),(4,3)\), compares direct survivor counts with both transfer formulas, tests finite binary-code identifiability, and checks period-two Perron roots against full transition products. The period-four trace identities can separately be checked by direct symbolic multiplication; that computation is not a proof dependency. The finite tests verify boundary indexing and algebra; the universal if-and-only-if theorem and dimension limits are proved analytically above.

## Relationship to prior work

Kong, Sun, and Wang (arXiv:2505.02336v2), Theorem 1.1 and Lemma 2.3, establish the homogeneous moving-hole dimensions using the full forbidden-word transition matrices. Their Theorem 1.8 treats periodic blocks of progressively overlapping and totally distinct holes. In particular its periodic-pattern framework overlaps the period-two corollary here, for which no independent originality is asserted. The new contribution is the exact rank-two formula for **every** arbitrary two-letter moving-hole schedule and the converse assertion that its whole prefix census uniquely recovers its complete binary temporal overlap code; neither is stated or established by the cited dimension/periodic-block theorems.

Kong, Li, Ma, and Simon (arXiv:2610.31128v1), especially its Introduction and Theorem 1.1, extend moving-hole dimension theory to inhomogeneous IFS and pressure settings. Their general pressure characterization is not a necessary-and-sufficient finite-prefix-count invariant in the present homogeneous subfamily. Cheriyath and Agarwal (arXiv:1905.11767v5) study correlation polynomials and escape rates for **fixed** finite collections of forbidden words, not the arbitrary time-indexed single forbidden bigram studied here. Existing dimension theorems, Perron–Frobenius theory, and transfer-matrix counting are used and credited; the claimed novelty is their universal exact overlap-code classification.

## Limitations

The theorem is restricted to exactly one moving forbidden word of length two, and to homogeneous base-\(b\) geometry with \(b\ge3\); it does not give analogous classifications for longer words or multiple simultaneous holes. Equal prefix counts do not imply homeomorphism, conjugacy, or equality of the actual survivor subsets. The source-based historical comparison is not exhaustive: a general theorem about products of rank-one perturbed all-ones matrices or time-dependent forbidden words could subsume the rank-two classification. No independent mathematical or historical-priority audit has been performed.

## References

1. D. Kong, K. Li, C.-Y. Ma, K. Simon, *Open dynamics with a moving hole: inhomogeneous IFS and exponential separation condition*, arXiv:2610.31128v1 (first public 2026-10-22), https://arxiv.org/html/2610.31128v1.
2. D. Kong, B. Sun, Z. Wang, *Open dynamical systems with a moving hole*, arXiv:2505.02336v2 (initial preprint 2025-05-05), https://arxiv.org/html/2505.02336v2.
3. H. Cheriyath, N. Agarwal, *Subshifts of Finite Type with a Hole*, arXiv:1905.11767v5 (initial preprint 2019-05-28), https://arxiv.org/html/1905.11767v5.
