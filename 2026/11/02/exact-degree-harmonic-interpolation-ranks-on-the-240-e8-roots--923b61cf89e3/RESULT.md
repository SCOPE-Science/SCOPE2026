# Exact-degree harmonic interpolation ranks on the 240 E8 roots

## Finding
Let \(X\subset S^7\) be the 240 unit vectors of the \(E_8\) root system. For each integer \(\ell\ge0\), evaluate all complex spherical harmonics of **exact** degree \(\ell\) at these points. The ranks of this map \(E_\ell\) are

\[
\begin{array}{c|rrrrrrrrrrr}
\ell&0&1&2&3&4&5&6&7&8&9&10\\\hline
\operatorname{rank}E_\ell&1&8&35&112&84&112&119&120&120&120&119.
\end{array}
\]

For every integer \(\ell\ge11\), the rank equals \(120\). Since the points form 120 antipodal pairs, 120 is the maximal possible rank at every exact degree. The first parity-compatible full interpolation occurs at degree \(7\), fails again at degree \(10\), and becomes permanent at degree \(11\).

More precisely, put \(D_\ell=\binom{\ell+5}{5}\), \(w_\ell=C_\ell^{(3)}(1/2)/D_\ell\), and \(c_\ell=C_\ell^{(3)}(0)/D_\ell\), with the standard Gegenbauer normalization \(C_\ell^{(3)}(1)=D_\ell\). The normalized reproducing-kernel matrix on 120 antipodal representatives has the following *complete* spectrum, including multiplicities:

\[
\begin{array}{c|c|c}
\ell\text{ parity}&\text{eigenvalue}&\text{multiplicity}\\\hline
\text{even}&1+56w_\ell+63c_\ell&1\\
\text{even}&1+8w_\ell-9c_\ell&35\\
\text{even}&1-4w_\ell+3c_\ell&84\\
\text{odd}&1+28w_\ell&8\\
\text{odd}&1-2w_\ell&112.
\end{array}
\]

## Assumptions and scope
All roots are *unit* vectors and all Gram matrices use the zonal kernel \(C_\ell^{(3)}(\langle x,y\rangle)/C_\ell^{(3)}(1)\). The exact-degree harmonic space on \(S^7\) is complexified but the rank is the same over the reals. There are no positive weights or mixed harmonic degrees. An assignment at degree \(\ell\) is *parity-compatible* when its values at opposite roots obey \(f(-x)=(-1)^\ell f(x)\). Full interpolation means surjectivity onto this 120-dimensional data space, not arbitrary independent data at all 240 roots.

Use the following exact coordinate model, scaled by \(1/\sqrt8\): the 112 vectors obtained by putting two entries equal to \(\pm2\) and all other entries zero, and the 128 sign vectors \((\pm1,\dots,\pm1)\) with an even number of minus signs. The 240 vectors occur in antipodal pairs. Select one member of each pair by requiring its first nonzero coordinate to be positive; write these 120 unit representatives as the rows of \(R\).

## Proof
**Step 1: three inner products and the finite spectral algebra.** Every two distinct representatives have inner product in \(\{-1/2,0,1/2\}\). Define a 120-by-120 unsigned adjacency matrix \(A\) by \(A_{ij}=1\) precisely for \(i\ne j\) and \(|\langle r_i,r_j\rangle|=1/2\), and a signed matrix \(S\) by \(S_{ii}=0\), \(S_{ij}=2\langle r_i,r_j\rangle\) for distinct indices. Direct exact root counting yields

\[
A\mathbf1=56\mathbf1,\qquad A^2=32I+4A+24J,
\]

so \(A\) has eigenvalues \(56,8,-4\) with multiplicities \(1,35,84\), respectively. In particular the complementary orthogonality graph has strongly regular parameters \((120,63,30,36)\). The root representatives also form a tight frame: \(R^{\mathsf T}R=15I_8\). Therefore \(S=2(RR^{\mathsf T}-I_{120})\) has eigenvalues \(28\) with multiplicity \(8\) and \(-2\) with multiplicity \(112\). These identities can be reconstructed from the explicit coordinates, without a numerical eigensolver.

**Step 2: the zonal Gram matrix.** Spherical harmonic addition and the parity identity \(C_\ell^{(3)}(-t)=(-1)^\ell C_\ell^{(3)}(t)\) give

\[
G_\ell=\begin{cases}
(1-c_\ell)I+(w_\ell-c_\ell)A+c_\ell J,&\ell\text{ even},\\
I+w_\ell S,&\ell\text{ odd}.
\end{cases}
\]

Substitution of the spectral decompositions from Step 1 gives exactly the five eigenvalue formulas in the finding. Because this is a reproducing-kernel Gram matrix, its rank equals the evaluation rank. There are exactly 120 columns up to antipodal parity, so nothing else contributes to the rank.

**Step 3: exact low degrees.** The Gegenbauer generating function gives

\[
\sum_{\ell\ge0}C_\ell^{(3)}(1/2)z^\ell
=(1-z+z^2)^{-3}=(1+z)^3(1+z^3)^{-3}.
\]

Thus if \(\ell=3k+r\) with \(r\in\{0,1,2\}\), then

\[
C_\ell^{(3)}(1/2)=
\begin{cases}(-1)^k(k+1),&r=0,\\
3(-1)^k\binom{k+2}{2},&r=1,2.
\end{cases}
\]

Likewise \(C_{2k}^{(3)}(0)=(-1)^k\binom{k+2}{2}\), while \(C_{2k+1}^{(3)}(0)=0\). Inserting these integers into the eigenvalues gives the displayed rank sequence through degree \(10\). In particular at degree \(10\) the eigenvalue in the one-dimensional constant sector vanishes, while the other two even sectors are positive.

**Step 4: the infinite tail.** We prove positivity of all the eigenvalues for every integer degree at least \(11\), rather than extrapolating a finite table. The generating functions yield

\[
|C_\ell^{(3)}(1/2)|\le(\ell+6)^2/6,\qquad
|C_{2k}^{(3)}(0)|=\binom{k+2}{2}\le(2k+4)^2/8.
\]

For odd \(\ell\ge11\), both eigenvalues are at least \(1-28(\ell+6)^2/(6D_\ell)\), which is positive since \(D_{11}/17^2=4368/289>14/3\) and \(D_\ell/(\ell+6)^2\) strictly increases with \(\ell\). For even \(\ell\ge12\), all three eigenvalues are at least

\[
1-\frac{56|C_\ell^{(3)}(1/2)|+63|C_\ell^{(3)}(0)|}{D_\ell}
\ge1-\frac{413(\ell+6)^2}{24D_\ell}>0.
\]

The final inequality holds at degree \(12\), since \(D_{12}=6188>413\cdot18^2/24\), and persists by the same monotonicity. This monotonicity follows from the exact identity

\[
(\ell+6)^3-(\ell+1)(\ell+7)^2=3\ell^2+45\ell+167>0,
\]

using \(D_{\ell+1}/D_\ell=(\ell+6)/(\ell+1)\). Hence no later rank defect exists.

## Verification
Run `python3 verify_e8_harmonics.py` from the directory containing this result and the standalone checker. It constructs all 240 roots in exact integer coordinates, checks every pair in the 120-line graph, verifies the strongly regular and tight-frame identities, compares each entry of the Gram matrix to the spectral formulas for degrees \(0\) through \(48\), reproduces both independent Gegenbauer coefficient formulas, checks every claimed low-degree rank, and confirms the two base inequalities for the infinite-degree proof. A successful run prints `E8_INTERPOLATION_CHECK_OK`. No unverified floating-point diagonalization is used, and the checker is corroboration rather than a substitute for the analytic tail argument.

## Relationship to prior work
The \(E_8\) 240-root configuration and its spherical \(7\)-design property are classical; Cohn and Kumar study its sharp universal energy optimality. Bannai, Okuda and Tagami explicitly identify this configuration (and its 120-point antipodal half) as a harmonic-index-\(10\) design. That fact already explains a degree-\(10\) vanishing *constant-sector* harmonic moment; it is not claimed as new. Schmidt determines the strongly regular orthogonality graph of the 120 \(E_8\) root lines. The present result determines the **complete exact-degree interpolation ranks, multiplicities, and permanent recovery threshold**, not merely a vanishing harmonic moment or the graph adjacency spectrum. It combines root-line graph algebra, parity-sensitive reproducing kernels, and explicit coefficient bounds; no inspected source stated the full rank sequence or its infinite tail.

## Limitations
This is a classification of one canonical 240-point spherical configuration, not a theorem about all root systems or arbitrary perturbed configurations. The graph and harmonic-index components are established background. An equivalent derivation in older association-scheme or representation-theoretic literature may exist; literature checking was bounded. No independent mathematical audit has been performed. The exact-arithmetic checker tests degrees only through \(48\); the analytic inequalities, not those tests, prove all higher degrees.

## References
- H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, arXiv:math/0607446 (first posted 2006-07-19), especially the table of sharp configurations and the background on positive-definite ultraspherical expansions.
- R. Coulangeon, *Spherical designs and zeta functions of lattices*, arXiv:math/0611735 (2006), sections on root-lattice spherical designs.
- E. Bannai, T. Okuda, and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101 (2013), the \(E_8\) harmonic-index-\(10\) example and Gegenbauer-kernel definitions.
- J. Zhu et al., *More on spherical designs of harmonic index t*, arXiv:1507.05373 (2015), general harmonic-index design framework.
- S. Schmidt, *Quantum isomorphic strongly regular graphs from the E8 root system*, arXiv:2209.14906 (2022), the 120-root-line orthogonality graph and its parameters.
