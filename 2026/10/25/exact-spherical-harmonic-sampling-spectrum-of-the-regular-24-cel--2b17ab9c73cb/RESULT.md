# Exact spherical-harmonic sampling spectrum of the regular 24-cell

## Finding
Let \(X\subset S^3\) be the 24 normalized \(D_4\) roots \((\pm e_i\pm e_j)/\sqrt2\), \(1\le i<j\le4\). For each integer \(\ell\ge0\), let \(\mathcal H_\ell\) be the degree-\(\ell\) spherical harmonics, with the probability-surface-measure \(L^2(S^3)\) inner product. Define the evaluation operator \(E_\ell:\mathcal H_\ell\to\mathbb C^{24}\) by \((E_\ell f)(x)=f(x)/\sqrt{24}\) for \(x\in X\).

Put \(n=\ell+1\), \(a_\ell=U_\ell(1/2)\), and \(b_\ell=U_\ell(0)\), with \(U_\ell\) the Chebyshev polynomial of the second kind. The **complete** spectrum, including multiplicities, of \(E_\ell E_\ell^*\) consists of \(n/24\) times the following five numbers, with fixed multiplicities \(1,2,9,4,8\), respectively:

\[
\begin{array}{c|ccccc}
 &1&2&9&4&8\\\hline
\ell\text{ even}&2n+16a_\ell+6b_\ell&2n-8a_\ell+6b_\ell&2n-2b_\ell&0&0\\
\ell\text{ odd}&0&0&0&2n+8a_\ell&2n-4a_\ell.
\end{array}
\]

All eigenvalues are nonnegative. The exact ranks for \(\ell=0,1,\ldots,10\) are
\[
(1,4,9,8,11,12,10,12,12,12,11).
\]
For **every** \(\ell\ge11\) the rank is \(12\), the full space of antipodally even (for even \(\ell\)) or antipodally odd (for odd \(\ell\)) data on \(X\). The sharp eventual-surjectivity threshold is therefore \(11\), although degrees \(5,7,8,9\) already have full parity rank. In particular, even degree \(10\) retains a one-dimensional sampling obstruction despite \(\dim\mathcal H_{10}=121\). For large \(\ell\), the 12 nonzero singular values obey \(\sigma^2(E_\ell)/(\ell+1)^2=1/12+O(1/\ell)\), uniformly across spectral branches.

## Assumptions and scope
Coordinates are in \(\mathbb R^4\); the roots have Euclidean norm \(1\). Each antipodal pair is counted as two distinct sample points. The sphere measure is normalized to total mass \(1\). Complex spherical harmonics use the Hermitian inner product and have dimension \((\ell+1)^2\). The listed eigenvalues are those of the **24-by-24 sample Gram matrix**, not those of \(E_\ell^*E_\ell\) acting on the larger harmonic space; nonzero spectra coincide.

## Proof
The addition theorem on \(S^3\) states that the reproducing kernel of \(\mathcal H_\ell\) is \(K_\ell(x,y)=nU_\ell(x\cdot y)\). Hence \(E_\ell E_\ell^*=(n/24)M_\ell\), where \((M_\ell)_{x,y}=U_\ell(x\cdot y)\).

Let \(I\) be the identity, \(R\) the antipodal permutation matrix, \(B\) the adjacency matrix for inner product \(1/2\), and \(C\) that for inner product \(0\). For distinct roots, all inner products are \(-1,-1/2,0,1/2\). Directly counting the 24 explicit roots gives
\[
R^2=I,\quad RB=BR,\quad RC=C,\quad
B^2=8I+3B+4C+RB,\quad
C^2=6(I+R)+4C,\quad BC=3(B+RB).
\]
These are finite exact identities, independently reproducible by the supplied checker. Their proof requires only counting intermediate vertices for a representative of each of the five possible inner products; signed-coordinate permutations act transitively on each relation.

Set \(P_e=(I+R)/2\), \(P_o=(I-R)/2\). On \(P_e\mathbb C^{24}\), \(C\) has eigenvalues \(6\) (multiplicity \(3\)) and \(-2\) (multiplicity \(9\)), by its displayed quadratic relation and zero trace. Since \(BC=6B\) on this space, \(B\) vanishes on the \(-2\)-eigenspace of \(C\). On the three-dimensional \(C=6\) eigenspace, \(B\) has eigenvalues \(8\) on constants (multiplicity \(1\)) and \(-4\) (multiplicity \(2\)), using the quadratic for \(B\) and its zero trace on the even space. On \(P_o\mathbb C^{24}\), \(C=0\) and \(B^2=8I+2B\), so \(B\) has eigenvalues \(4\) (multiplicity \(4\)) and \(-2\) (multiplicity \(8\)), again from the zero trace. This proves the five pairwise orthogonal common eigenspaces with multiplicities \((1,2,9,4,8)\).

Chebyshev parity gives \(U_\ell(-t)=(-1)^\ell U_\ell(t)\). Therefore
\[
M_\ell=n(I+(-1)^\ell R)+a_\ell(B+(-1)^\ell RB)+b_\ell C.
\]
Applying this identity to the five eigenspaces proves the entire spectral table. The explicit values \(a_\ell=(2/\sqrt3)\sin((\ell+1)\pi/3)\in\{-1,0,1\}\) and \(b_\ell=\sin((\ell+1)\pi/2)\in\{-1,0,1\}\) give the displayed low-degree ranks by substitution. For odd \(\ell\ge5\), \(n\ge6\) and both active eigenvalues are strictly positive (the cases \(\ell=5\) and later are checked by the period-six values of \(a_\ell\)). For even \(\ell\ge12\), \(n\ge13\) makes the three active eigenvalues strictly positive by \(|a_\ell|\le1\), \(|b_\ell|\le1\). Degree \(10\) fails full rank, proving sharpness of the eventual cutoff \(11\). The three active even and two active odd eigenvalues equal \(2n+O(1)\), proving the stated normalized asymptotic.

## Verification
Execute `python verify_spectrum.py` with SymPy installed. The program constructs all 24 vertices in exact arithmetic, checks the association identities and all five orthogonal spectral projectors with their multiplicities, and independently evaluates the complete Chebyshev matrix for degrees \(0\) through \(48\). Its output is in `CHECKS.txt`. These finite tests are consistency checks; the all-degree theorem follows from the analytic addition theorem, parity, and exact matrix algebra above.

## Relationship to prior work
Cohn–Conway–Elkies–Kumar (2006, arXiv:math/0607447) study the 24-cell as a spherical code and record its pair-distance distribution. Hirao–Nozaki–Tasaka (2023, arXiv:2303.09000) prove the normalized root system is a spherical harmonic-index \(\{2,4,10\}\)-design and analyze its arithmetic harmonic strength. Their design vanishing results predict some constant-vector zero eigenvalues in the current table, including the degree-ten defect, and are explicitly **not** claimed as new. The present claim concerns the *complete operator spectrum*, all other parity-sensitive rank defects, the sharp eventual surjectivity cutoff, and normalized high-degree conditioning. Classical addition theorems and association schemes provide the framework; the full 24-cell five-branch computation and its interpolation consequences are the specific contributions assessed here.

## Limitations
This is an explicit spectral classification for the fixed regular 24-cell, not a classification of all 24-point spherical designs, general root systems, or stability under perturbations. The result does not imply an exact cubature formula at degrees above the established design strength. The spectral calculation uses standard representation/scheme techniques and could potentially be implied by an older tabulation of the complete 24-cell association-scheme eigenmatrix; the corresponding publication-priority risk remains.

## References
1. H. Cohn, J. H. Conway, N. D. Elkies and A. Kumar, *The \(D_4\) root system is not universally optimal*, arXiv:math/0607447, first version 19 July 2006, especially the inner-product distribution.
2. M. Hirao, H. Nozaki and K. Tasaka, *Spherical designs and modular forms of the \(D_4\) lattice*, arXiv:2303.09000, especially Sections 3–4 and 8.
3. P. Delsarte, J.-M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, for the classical harmonic addition and design framework (not claimed to have been inspected in full).
