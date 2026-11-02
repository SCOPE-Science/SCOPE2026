# Exact field staircase, degeneracies, and correlations for anisotropic rook-graph Ising antiferromagnets

## Finding
For every integer \(m,n\ge 2\), every \(J_r,J_c>0\), and every real magnetic field \(h\), the labelled Ising antiferromagnet on the rectangular rook graph \(K_m\square K_n\) has an exact, finite, closed microcanonical energy and a complete combinatorial classification of its ground states. The number of distinct strict-field magnetization plateaux is
\[
\boxed{m+n-\gcd(m,n)+1}.
\]
All critical fields, exact labelled multiplicities (including coexistence), and the three pair-correlation orbits in each fixed-magnetization ground sector are determined below. The dependence on the greatest common divisor records a finite-size commensurability effect; no infinite-volume thermodynamic phase transition is asserted.

## Assumptions and scope
Let \(i=1,\ldots,m\) label rows and \(j=1,\ldots,n\) label columns. At each cell place \(s_{ij}\in\{-1,+1\}\). Each pair in one row interacts with strength \(J_r>0\), and each pair in one column with strength \(J_c>0\), counted once; there are no other edges. The Hamiltonian is
\[
H(s)=J_r\sum_{i=1}^m\sum_{1\le j<k\le n}s_{ij}s_{ik}+J_c\sum_{j=1}^n\sum_{1\le i<k\le m}s_{ij}s_{kj}-h\sum_{i,j}s_{ij}.
\]
All vertices are labelled and all statistical ensembles below are uniform over the specified finite set of configurations. Write \(K=|\{(i,j):s_{ij}=+1\}|\), \(0\le K\le mn\), and \(M=2K-mn\). Define the integers
\[
q_r=\lfloor K/m\rfloor,\ t_r=K-mq_r,\quad q_c=\lfloor K/n\rfloor,\ t_c=K-nq_c,
\]
\[
a=2q_r-n,\qquad b=2q_c-m.
\]
In particular, \(0\le t_r<m\) and \(0\le t_c<n\), with the evident interpretation at \(K=mn\).

## Proof
**1. Exact microcanonical energy and equality classification.** Let \(R_i=\sum_j s_{ij}\) and \(C_j=\sum_i s_{ij}\). The pair identity \(\sum_{j<k}s_{ij}s_{ik}=(R_i^2-n)/2\) and its column analogue give
\[
H(s)=\frac{J_r}{2}\sum_i(R_i^2-n)+\frac{J_c}{2}\sum_j(C_j^2-m)-h(2K-mn).
\]
Writing the positive-spin row degrees as \(r_i=(R_i+n)/2\), their sum is \(K\). If \(r_u\ge r_v+2\), moving a positive entry in this abstract degree multiset from \(u\) to \(v\) strictly lowers \(\sum_i(2r_i-n)^2\): the decrease is \(8(r_u-r_v-1)>0\). Thus every minimum of this row-degree objective has \(r_i\in\{q_r,q_r+1\}\), with exactly \(t_r\) higher rows. The corresponding statement holds for the columns, independently.

Crucially, the two lower bounds can be attained *simultaneously*. Consider the fractional \(m\)-by-\(n\) matrix all of whose entries are \(K/(mn)\). Every row sum is \(K/m\in[q_r,q_r+1]\), every column sum is \(K/n\in[q_c,q_c+1]\), and the total is exactly \(K\). The feasible network-flow polytope with entry bounds \(0\le x_{ij}\le1\), integral row and column lower/upper degree bounds, and total \(\sum x_{ij}=K\) has an integral point whenever it is nonempty, by total unimodularity of the bipartite incidence matrix (equivalently integral capacitated bipartite flow). Hence a \(0\)-\(1\) matrix with both balanced margin systems exists for each \(K\). Because both couplings are strictly positive, equality in the summed lower bound is *equivalent* to simultaneous balancing of the row and column degrees. Consequently the exact minimum at fixed \(K\) is
\[
\boxed{E_K=\frac{J_r}{2}\big[(m-t_r)a^2+t_r(a+2)^2-mn\big]+\frac{J_c}{2}\big[(n-t_c)b^2+t_c(b+2)^2-mn\big]-h(2K-mn).}
\]
Every and only spin matrix with the two balanced margin patterns is a minimizer at fixed \(K\).

**2. All magnetic plateaux and boundary sectors.** Direct subtraction, including both divisible and nondivisible cases, yields
\[
E_{K+1}-E_K=2(H_K-h),\quad H_K=J_r\big(2\lfloor K/m\rfloor-n+1\big)+J_c\big(2\lfloor K/n\rfloor-m+1\big),
\]
for \(K=0,\ldots,mn-1\). Because \(J_r,J_c>0\), the sequence \(H_K\) is nondecreasing, and increases strictly at each positive multiple of \(m\) or of \(n\); it is otherwise constant. Put
\[
\mathcal B=\{0,mn\}\cup\{K:0<K<mn,\ m\mid K\ \text{or}\ n\mid K\}=\{b_0<\cdots<b_L\}.
\]
Then \(H_{b_i}\), \(i=0,\ldots,L-1\), are the distinct critical fields in increasing order. Between critical fields there is one minimizing value \(K=b_i\), giving magnetization \(2b_i-mn\). At \(h=H_{b_i}\), *all* \(K\in\{b_i,b_i+1,\ldots,b_{i+1}\}\) minimize. Strict convexity between successive breakpoint blocks excludes any other ground sectors. Counting the multiples by inclusion-exclusion gives
\[
L+1=|\mathcal B|=m+n-\gcd(m,n)+1.
\]
This is an all-field classification, including \(h<0\), \(h=0\), and exact coexistence boundaries. At \(h>J_r(n-1)+J_c(m-1)\), all spins are positive; at the opposite extreme all are negative.

**3. Exact labelled multiplicities.** Let \(e_k(y_1,\ldots,y_n)\) be the \(k\)-th elementary symmetric polynomial, with \(e_0=1\). For a given \(K\), choose a canonical row-margin sequence \(\rho_i=q_r+1\) for \(1\le i\le t_r\) and \(\rho_i=q_r\) otherwise, and a canonical column-margin sequence \(\gamma_j=q_c+1\) for \(1\le j\le t_c\), \(\gamma_j=q_c\) otherwise. The exact count of labelled minimum-energy matrices in that sector is
\[
\boxed{G_{m,n}(K)=\binom m{t_r}\binom n{t_c}[y_1^{\gamma_1}\cdots y_n^{\gamma_n}]\prod_{i=1}^m e_{\rho_i}(y_1,\ldots,y_n).}
\]
This follows by selecting the high rows and columns and expanding the generating product for each row. No simple closed form for the general regular \(0\)-\(1\) matrix count is claimed. The full ground-state multiplicity at field \(h\) is exactly \(\sum_{K:E_K=\min_Q E_Q}G_{m,n}(K)\), with the minimizing sectors specified in item 2.

At the positive saturation boundary \(h=J_r(n-1)+J_c(m-1)\), the minority spins are precisely matchings of the complete bipartite graph on row and column indices, so the critical multiplicity specializes to the classical rook-number sum
\[
\sum_{k=0}^{\min(m,n)}\binom mk\binom nk\,k!.
\]
This matching formula is standard; the contribution here is its placement within the complete anisotropic field classification and the additional exact covariance law.

**4. Three exact correlation orbits.** Fix any \(K\) and average uniformly over its \(G_{m,n}(K)\) microcanonical ground configurations. By row and column permutation invariance, all sites have mean spin \(\mu=(2K-mn)/(mn)\), and any pair of distinct sites has one of three covariances: same row, same column, or different row *and* different column. Set
\[
v=1-\mu^2,\qquad w_r=\frac{4t_r(m-t_r)}{m^2},\qquad w_c=\frac{4t_c(n-t_c)}{n^2}.
\]
A row sum has variance \(w_r\), since it is one of the two values \(2q_r-n\) and \(2q_r-n+2\), with fractions \((m-t_r)/m\) and \(t_r/m\) across rows; similarly a column sum has variance \(w_c\). These identities give
\[
\boxed{C_{\rm row}=\frac{w_r-nv}{n(n-1)},\qquad C_{\rm col}=\frac{w_c-mv}{m(m-1)}.}
\]
Because total magnetization is fixed, the covariance of a chosen spin with the total is zero. Counting its \(n-1\) row neighbors, \(m-1\) column neighbors, and \((m-1)(n-1)\) remaining sites therefore gives
\[
\boxed{C_{\rm disjoint}=\frac{v-w_r/n-w_c/m}{(m-1)(n-1)}.}
\]
This is exact at each fixed \(K\), including fields where several \(K\) coexist; at coexistence it is a *conditional* covariance, and the unconditional mixed-sector covariance is obtained from the exact multiplicities and the law of total covariance. For the isotropic square case with all line margins equal, \(w_r=w_c=0\), so same-line covariance is \(-v/(n-1)\) and disjoint covariance \(v/(n-1)^2\).

**5. Worked unequal-arm example.** For \(m=3,n=4,J_r=1,J_c=2\), the breakpoint list is \(\mathcal B=(0,3,4,6,8,9,12)\) with critical fields \((-7,-5,-1,1,5,7)\). There are exactly seven strict-field magnetizations \((-12,-6,-4,0,4,6,12)\). Their labelled multiplicities are respectively \((1,24,36,90,36,24,1)\); at the six critical fields the full multiplicities are \((73,60,270,270,60,73)\).

## Verification
The accompanying executable \(\texttt{artifacts/verify.py}\) uses Python 3 and NumPy, with no network dependencies. It directly enumerates configurations and computes energies *edge by edge* on small boards, independently compares complete microcanonical dynamic-programming minima and counts with a separate binary-margin coefficient counter, checks all three covariance types through exact rational arithmetic, and tests the breakpoint-count identity at six rectangular sizes. Its actual output is embedded as \(\texttt{artifacts/check_output.txt}\). The direct-edge comparisons number 335; the independent microcanonical checks include full sectors on boards through \(5\times5\); the exact covariance comparisons number 39. Finite computations corroborate the analytic theorem and do not substitute for its all-size proof.

## Relationship to prior work
Magnetic plateaux in frustrated quantum magnets, including two-dimensional square, triangular and kagome geometries, are examined by Honecker, Schulenburg and Richter (2003). The present object is instead a classical binary Ising model on the finite complete-clique product \(K_m\square K_n\), with two independently tunable positive exchange strengths. Yu (2016) treats the Ising antiferromagnet on Archimedean lattices rather than this graph family. Dyer, Heinrich, Jerrum and Müller (2020) give general approximate partition-function computation and sampling on line graphs, with a discussion of maximum cut and local fields; their general results do not themselves state the exact balanced-margin field staircase, anisotropic threshold list, labelled multiplicities or three-orbit covariance. Canfield, Greenhill and McKay (2006), and the earlier matrix-enumeration literature they cite, cover enumeration of \(0\)-\(1\) matrices with given row and column sums; their general coefficient and asymptotic counting machinery is credited, not relabelled as new. Arbib and Guruswami's line-graph maximum-cut algorithms cover optimization more generally, without a verified exact multiparameter field-and-covariance formula in the inspected materials. The mathematical contribution assessed here is the *combined complete positive-anisotropy field classification and its conditional spatial covariance identities*, not the stand-alone balanced-array or rook-matching enumeration.

## Limitations
Only classical, labelled, binary spin configurations, uniform within-row and within-column positive couplings, and zero temperature are included. At critical fields, the covariance formula applies after conditioning on fixed magnetization. There is no claim of a nonzero-temperature transition, independent priority certification, a compact product formula for arbitrary binary-margin counts, or an extension to arbitrary line graphs or nonuniform site fields. A full primary historical survey, including inaccessible older max-cut sources, is not complete.

## References
1. A. Honecker, J. Schulenburg and J. Richter, *Magnetization plateaus in frustrated antiferromagnetic quantum spin models*, arXiv:cond-mat/0309425, first public 2003-09-18. https://arxiv.org/abs/cond-mat/0309425
2. U. Yu, *Ising antiferromagnet on the Archimedean lattices*, arXiv:1606.08191, first public 2016-06-27. https://arxiv.org/abs/1606.08191
3. E. R. Canfield, C. Greenhill and B. D. McKay, *Asymptotic enumeration of dense 0-1 matrices with specified line sums*, arXiv:math/0606496, first public 2006-06-20. https://arxiv.org/abs/math/0606496
4. M. Dyer, M. Heinrich, M. Jerrum and H. Müller, *Polynomial-time approximation algorithms for the antiferromagnetic Ising model on line graphs*, arXiv:2005.07944, first public 2020-05-16. https://arxiv.org/abs/2005.07944
5. V. Guruswami, *Maximum Cut on Line and Total Graphs*, Discrete Applied Mathematics (1999). https://doi.org/10.1016/S0166-218X(99)00056-6
