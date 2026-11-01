# Complete exact-degree harmonic sampling spectrum of the regular 24-cell

## Finding
Let \(X\subset S^3\) be the 24 normalized roots of type \(D_4\): all vectors obtained by permuting \((\pm1,\pm1,0,0)/\sqrt2\). For each integer \(\ell\ge0\), the evaluation map \(E_\ell\) takes all complex spherical harmonics of **exact degree** \(\ell\) on \(S^3\) to their 24 values on \(X\). Its rank is
\[
\operatorname{rank}E_\ell=
\begin{cases}
1,4,9,8,11,12,10,12,12,12,11&\text{at degrees }\ell=0,1,\ldots,10\text{ respectively},\\
12&\ell\ge11.
\end{cases}
\]
In particular, interpolation onto the 12-dimensional parity-compatible data space first becomes possible at degree \(5\), fails again at degree \(6\), succeeds at degrees \(7,8,9\), fails at degree \(10\), and succeeds for every degree \(\ell\ge11\).

A stronger result determines every singular value. Write \(U_\ell\) for the degree-\(\ell\) Chebyshev polynomial of the second kind, normalized by \(U_\ell(1)=\ell+1\). Put \(w_\ell=U_\ell(1/2)\) and \(c_\ell=U_\ell(0)\). The scaled zonal Gram matrix \(G_\ell=(U_\ell(\langle x,y\rangle))_{x,y\in X}\) has at least twelve zero eigenvalues, forced by antipodal parity. Its other twelve eigenvalues, counting zeros, are as follows.

For **even** \(\ell\), there are three levels:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
2(\ell+1)+16w_\ell+6c_\ell&1\\
2(\ell+1)-8w_\ell+6c_\ell&2\\
2(\ell+1)-2c_\ell&9
\end{array}
\]
For **odd** \(\ell\), there are two levels:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
2(\ell+1)+8w_\ell&4\\
2(\ell+1)-4w_\ell&8
\end{array}
\]
The twelve-dimensional parity-reduced Gram matrices satisfy the **exact recurrence** \(M_{\ell+12}=M_\ell+24I_{12}\) in a fixed ordering of antipodal representatives. For a spherical-harmonic basis orthonormal under normalized probability surface measure, \(E_\ell E_\ell^*=(\ell+1)G_\ell\); consequently the nonzero singular values of \(E_\ell\) are the square roots of \(\ell+1\) times the positive eigenvalues above.

## Assumptions and scope
The points of \(X\) are distinct; each antipodal pair is retained once for the twelve-dimensional quotient and twice for the original evaluation map. The dimension of the exact-degree harmonic space on \(S^3\) is \((\ell+1)^2\). An assignment \(f:X\to\mathbb C\) is parity-compatible in degree \(\ell\) when \(f(-x)=(-1)^\ell f(x)\). Surjectivity refers to all assignments satisfying this parity relation; it does not concern interpolation by sums of multiple degrees.

## Proof
**Step 1: Addition formula and parity reduction.** The spherical addition formula in four ambient dimensions gives the zonal reproducing kernel \((\ell+1)U_\ell(\langle x,y\rangle)\) for a degree-\(\ell\) orthonormal harmonic basis with respect to normalized surface measure. Thus \(G_\ell\) is a positive-semidefinite scalar multiple of the evaluation Gram matrix and has the same rank. Choose one unit representative \(r_i\) from each antipodal pair, for \(1\le i\le12\). The identity \(U_\ell(-t)=(-1)^\ell U_\ell(t)\) shows that \(G_\ell\) annihilates the parity-incompatible half of \(\mathbb C^{24}\). On the compatible half, its matrix in the natural pair basis is
\[
M_\ell=\bigl(2U_\ell(\langle r_i,r_j\rangle)\bigr)_{1\le i,j\le12}.
\]
These are precisely the twelve possibly nonzero eigenvalues of \(G_\ell\).

**Step 2: Orthogonality and signed-incidence matrices.** For distinct root lines, the inner product of representatives belongs to \(\{0,\pm\tfrac12\}\). Define \(B_{ij}=1\) when \(i\ne j\) and the lines are orthogonal, \(A=J-I-B\), and define \(S_{ij}=2\langle r_i,r_j\rangle\) for \(i\ne j\) with \(S_{ii}=0\). The twelve lines divide into three blocks of four: for each partition of the four coordinate positions into two unordered pairs, take the two signed lines supported on each pair. Each block is mutually orthogonal, and two lines from different blocks are nonorthogonal. Hence \(B\) is the adjacency matrix of three disjoint complete graphs on four vertices. Its eigenvalues are \(3\) on the three-dimensional block-constant space and \(-1\) on the nine-dimensional blockwise zero-sum space. On the global constants \(A\) has eigenvalue \(8\); on the two-dimensional block-contrast subspace it has eigenvalue \(-4\); and on the nine-dimensional blockwise zero-sum subspace it has eigenvalue \(0\).

Write \(W\) for the twelve-by-four matrix whose rows are the representatives \(r_i\). Coordinate sign symmetry gives \(W^*W=3I_4\). Since \(S+2I_{12}=2WW^*\), the signed matrix \(S\) has eigenvalue \(4\) with multiplicity four and \(-2\) with multiplicity eight. This identity also proves \(S^2=2S+8I_{12}\) without numerical diagonalization.

**Step 3: Exact spectra.** The values \(w_\ell=U_\ell(1/2)\) lie in \(\{-1,0,1\}\) and repeat every six degrees. The values \(c_\ell=U_\ell(0)\) repeat every four degrees, equaling zero for odd degrees and \((-1)^{\ell/2}\) for even degrees. If \(\ell\) is odd, the signs at opposite half-inner-products produce
\[
M_\ell=2(\ell+1)I_{12}+2w_\ell S.
\]
The two stated odd-degree levels follow from the spectrum of \(S\). If \(\ell\) is even, signs agree and
\[
M_\ell=2(\ell+1)I_{12}+2w_\ell A+2c_\ell B.
\]
The simultaneous three-sector decomposition of \(A,B\) gives the even-degree levels, with multiplicities \(1,2,9\). The periodicity of \(w_\ell,c_\ell\), together with the changing diagonal term, yields \(M_{\ell+12}=M_\ell+24I_{12}\).

**Step 4: Zero levels and all degrees.** Substitution for degrees zero through ten gives ranks \(1,4,9,8,11,12,10,12,12,12,11\). For odd \(\ell\ge5\), both eigenvalue expressions are at least \(2(\ell+1)-8>0\). For even \(\ell\ge12\), the three are bounded below by \(2(\ell+1)-22>0\), \(2(\ell+1)-14>0\), and \(2(\ell+1)-2>0\), respectively. Thus all twelve compatible directions occur from degree eleven onward. Every rank statement, including the infinitely many degrees beyond the finite table, follows.

## Verification
The accompanying self-contained Python file `verify_spectrum.py` reconstructs the twelve root lines using integer coordinates, checks the three orthogonality blocks, verifies \(S^2=2S+8I_{12}\), constructs exact Chebyshev matrices, compares all closed-form spectral coefficients for degrees \(0\) through \(47\), and checks the twelve-degree recurrence and the rank table. Run `python3 verify_spectrum.py` from the directory containing this file. This finite computation checks the displayed identities; the preceding algebraic proof and strict lower bounds establish the infinite assertion.

## Relationship to prior work
Cohn, Conway, Elkies, and Kumar describe the regular 24-cell as the \(D_4\) root system and study its spherical-code energy and deformations, not an exact-degree sampling rank table. General spherical-design and Gegenbauer addition formulas are classical. Hirao, Nozaki, and Tasaka establish the 24-cell's harmonic-index design property in degrees \(2,4,10\) and, in later work, determine the complete harmonic strength of the binary tetrahedral group, an orthogonal realization of the same 24 points. The zero constant Fourier mode at degrees \(2,4,10\) is therefore known. The present formulas retain every parity-compatible Fourier direction, including the separate two-dimensional deficit at degree \(6\), and give all evaluation eigenvalues and the affine twelve-step recurrence. These rank and conditioning statements do not follow from knowledge of the constant-mode harmonic strength alone.

## Limitations
The classification applies to the regular \(D_4\) configuration, not to all 24-point spherical five-designs or to deformations of the 24-cell. No claim is made about independent external validation or a classification of all equivalent formulations in representation-theoretic literature. Classical branching rules for the binary tetrahedral group are a possible alternate derivation of the rank part, while the complete scaled zonal eigenvalue formulas are the specific objects established here.

## References
1. H. Cohn, J. H. Conway, N. D. Elkies, A. Kumar, *The D4 Root System Is Not Universally Optimal*, arXiv:math/0607447, first public version July 19, 2006; *Experimental Mathematics* 16 (2007), 313–320.
2. M. Hirao, H. Nozaki, K. Tasaka, *Spherical designs and modular forms of the D4 lattice*, arXiv:2303.09000, first public version March 16, 2023; *Research in Number Theory* 9 (2023), 77.
3. M. Hirao, H. Nozaki, K. Tasaka, *Spherical designs for finite quaternionic unit groups and their applications to modular forms*, arXiv:2507.01358, first public version July 2, 2025.
4. P. Delsarte, J. M. Goethals, J. J. Seidel, *Spherical codes and designs*, *Geometriae Dedicata* 6 (1977), 363–388.
