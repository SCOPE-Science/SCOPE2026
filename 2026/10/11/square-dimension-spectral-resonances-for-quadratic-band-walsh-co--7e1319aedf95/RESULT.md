# Square-dimension spectral resonances for quadratic-band Walsh concentration on Hamming shells

## Finding

For integers \(n\ge5\) and \(2\le k\le n-2\), equip the Boolean cube \(\Omega_n=\{-1,1\}^n\) with uniform probability measure. Let \(V_{\le2}\) be the degree-at-most-two Walsh subspace, of dimension \(1+n+\binom n2\), and let \(P_{\le2}\) be its orthogonal projection. The fixed-weight Hamming shell is
\[
X_{n,k}=\{x\in\Omega_n:\#\{i:x_i=-1\}=k\}.
\]
Study the self-adjoint Walsh spatial-concentration operator
\[
C_{n,k}=\left.P_{\le2}M_{\mathbf1_{X_{n,k}}}P_{\le2}\right|_{V_{\le2}}.
\]
Set \(t=(n-2k)^2\), \(w=2^{-n}\binom nk\), and
\[
\begin{aligned}
a_0&=\frac{t^2-2t+3n^2-2n}{2n(n-1)},\\
a_1&=\frac{(n^2-t)(t+n-2)}{n(n-1)(n-2)},\\
a_2&=\frac{(n^2-t)((n-2)^2-t)}{n(n-1)(n-2)(n-3)}.
\end{aligned}
\]
The **complete concentration spectrum** has three positive levels and a universal nullspace:
\[
\boxed{\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
w a_0&1\\
w a_1&n-1\\
w a_2&n(n-3)/2\\
0&n+1
\end{array}}
\]
Coincident levels are combined. Thus the shell-restriction map has rank \(\binom n2\) for every interior shell, independently of its radius. More surprisingly, **all pairwise coincidences of the positive eigenvalues are classified by an elementary arithmetic resonance**:

* \(a_0=a_1\) exactly when \(n=r^2+1\) for an integer \(r\ge2\) and \(\lvert n-2k\rvert\in\{r-1,r+1\}\), subject to the stated interior-shell range. For \(r\ge3\) this gives four genuine radii in every dimension \(n=r^2+1\); in dimension five only the two central radii remain.
* \(a_1=a_2\) exactly when \(n\) is odd and \(k\in\{(n-1)/2,(n+1)/2\}\).
* \(a_0=a_2\) exactly for \((n,k)=(5,2),(5,3),(6,3)\).

The only triple coincidence is \((n,k)=(5,2)\) or \((5,3)\), in which case all nonzero concentration eigenvalues equal \(1/2\). The nontrivial integer-square spectral crossings persist in arbitrarily large dimensions; they are not numerical accidents in small Hamming cubes.

## Assumptions and scope

The theorem is for the **binary** cube and the complete Walsh bandwidth \(\le2\), sampled on one exact Hamming-weight shell with \(2\le k\le n-2\). It uses the uniform probability normalization on the cube. The shell multiplier is an indicator, not normalized surface measure. End shells \(k=0,1,n-1,n\), larger bandwidths, and nonbinary Hamming schemes are outside the asserted formula. Classification of collisions concerns equality of the three specified positive eigenvalue levels; it is not a statement about accidental degeneracy within an irreducible eigenspace.

## Proof

**1. Compression to an explicit Gram kernel.** For \(I\subseteq[n]\), write \(\chi_I(x)=\prod_{i\in I}x_i\). These are orthonormal on \(\Omega_n\). Nonzero eigenvalues of \(C_{n,k}\) equal those of the finite shell Gram matrix
\[
G(x,y)=2^{-n}\sum_{|I|\le2}\chi_I(x)\chi_I(y),\qquad x,y\in X_{n,k}.
\]
If \(r=\#\{i:x_i=y_i=-1\}=\lvert S_x\cap S_y\rvert\), the Hamming distance is \(2(k-r)\). Put \(c=n-4k\). Summing Walsh characters of degrees zero, one and two gives
\[
\begin{aligned}
2^nG(x,y)&=1+(c+4r)+\frac{(c+4r)^2-n}{2}\\
&=A+B r+16\binom r2,\\
A&=1+c+\frac{c^2-n}{2},\qquad B=12+4c.
\end{aligned}
\]
Consequently, the shell Gram operator is a linear combination of three incidence Gram matrices: the constant matrix, \(B_1B_1^{\mathsf T}\), and \(B_2B_2^{\mathsf T}\), where \((B_d)_{S,U}=\mathbf1_{U\subseteq S}\) for \(\lvert U\rvert=d\). This explicitly reduces the problem to the degree-two Johnson incidence algebra.

**2. Exact rank and three invariant spaces.** The image of \(B_2\) contains constants and all point-indicator functions on the \(k\)-slice: summing \(\mathbf1_{\{i,j\}\subseteq S}\) over \(j\ne i\) gives \((k-1)\mathbf1_{i\in S}\), while the sum over all pairs is \(\binom k2\). The columns of \(B_2\) are independent for \(2\le k\le n-2\). Indeed, if \(\sum_{i<j\in S}c_{ij}=0\) on every \(k\)-set, compare sets obtained by exchanging a fixed \(i\) and \(j\) over all \((k-1)\)-subsets avoiding them. The vanishing of these equal-size subset sums forces \(c_{ia}=c_{ja}\) for every \(a\notin\{i,j\}\). Symmetry then forces all \(c_{ij}\) to be equal; the original identity makes that common value zero. Thus \(\operatorname{rank}B_2=\binom n2\). The shell functions decompose orthogonally into constants of dimension \(1\), a point-standard sector of dimension \(n-1\), and a quadratic sector of dimension \(\binom n2-n=n(n-3)/2\). All three are contained in the image of \(B_2\). The Gram kernel vanishes on its orthogonal complement. Therefore \(G\) has \(\binom n2\) positive eigenvalues; the original operator on the \(1+n+\binom n2\)-dimensional bandwidth has \(n+1\) zero eigenvalues.

**3. Eigenvalues on the three sectors.** On the constant sector, the squared mean of a Walsh character on the uniform \(k\)-slice equals \(1\) for degree zero, \((n-2k)^2/n^2\) for each degree-one coordinate, and \(((n-2k)^2-n)^2/[n^2(n-1)^2]\) for each degree-two pair. The constant eigenvalue is consequently
\[
\lambda_0=2^{-n}\binom nk\left(1+\frac{t}{n}+\frac{(t-n)^2}{2n(n-1)}\right)=w a_0.
\]
The matrix \(B_1B_1^{\mathsf T}\) acts on point-standard functions by \(\binom{n-2}{k-1}\), and kills the quadratic sector. To compute the remaining action, examine \(B_2^{\mathsf T}B_2\) on pair-coordinate arrays. Its entries for coincident pairs, pairs sharing one vertex, and disjoint pairs are, respectively,
\[
A_*=\binom{n-2}{k-2},\quad B_*=\binom{n-3}{k-3},\quad C_*=\binom{n-4}{k-4},
\]
with binomial coefficients outside their range interpreted as zero. On arrays \(u_{ij}=a_i+a_j\), \(\sum_i a_i=0\), the adjacency sums for overlapping and disjoint pairs have multipliers \(n-4\) and \(-(n-3)\). Hence the point-standard eigenvalue of \(B_2B_2^{\mathsf T}\) is
\[
A_*+(n-4)B_*-(n-3)C_*=(k-1)\binom{n-3}{k-2}.
\]
On pair arrays with zero row sums \(\sum_{j\ne i}u_{ij}=0\), the two adjacency multipliers are \(-2\) and \(1\). Hence the quadratic eigenvalue is
\[
A_*-2B_*+C_*=\binom{n-4}{k-2}.
\]
Combining the coefficient \(B=12+4(n-4k)\) of \(r\) and coefficient \(16\) of \(\binom r2\) yields
\[
\begin{aligned}
\lambda_1&=2^{-n}\left[4(n-4k+3)\binom{n-2}{k-1}+16(k-1)\binom{n-3}{k-2}\right]=w a_1,\\
\lambda_2&=2^{4-n}\binom{n-4}{k-2}=w a_2.
\end{aligned}
\]
All three are positive on the stipulated interior range. The constants, point-standard and quadratic sectors are orthogonal, so the displayed spectrum and multiplicities follow without unverified diagonalization assumptions.

**4. Arithmetic classification of all crossings.** Cancelling positive denominators in the rational formulas gives the exact factorizations
\[
\begin{aligned}
a_0-a_1&=\frac{(t-n)^2-4(n-1)}{2(n-1)(n-2)},\\
a_1-a_2&=\frac{(n^2-t)(t-1)}{n(n-1)(n-3)},\\
a_0-a_2&=\frac{(n-4)t^2+(2n+4)t+n(n-2)(n-6)}{2n(n-2)(n-3)}.
\end{aligned}
\]
Because \(t=(n-2k)^2\) and \(2\le k\le n-2\), the middle numerator vanishes exactly at \(t=1\), i.e. the two central radii in odd dimension. The final numerator is positive for \(n\ge7\); checking \(n=5,6\) gives precisely the stated exceptional radii. For the first equality, \((t-n)^2=4(n-1)\). Since \(t\equiv n\pmod2\), \((t-n)/2\) is integral, so \(n-1=r^2\) for some integer \(r\ge2\), and then \(t=n\pm2r=(r\pm1)^2\). The converse is immediate, with the shell range determining which radii occur. The only possible triple equality follows by intersecting these classifications and is realized exactly at the two central shells for \(n=5\). This exhausts all cases for the stated infinite family.

## Verification

The standard-library checker `verify.py` constructs the exact shell Gram kernel from Walsh characters and verifies the proposed three eigenvalues on explicit constant, point-standard, and quadratic test vectors, *for every shell* \(2\le k\le n-2\) and every \(5\le n\le11\) (35 cases). It also verifies the full trace identity and integer-arithmetic collision classification for 123,752 pairs through dimension 500 using exact rational arithmetic. Its execution result begins `VERIFY_OK eigenpair_cases=35 arithmetic_collision_cases=123752`. These checks corroborate the complete algebraic proof; they do not replace the infinite-domain argument. Reproduce with `python3 verify.py` in any standard Python 3 environment.

## Relationship to prior work

Srinivasan (arXiv:1001.0280v1, 2010) constructs the orthogonal symmetric Jordan chains of the Boolean algebra and block-diagonalizes the full binary Hamming Terwilliger algebra, supplying a powerful generic framework for related radial operators. Filmus (arXiv:1406.0142v1, 2014) develops an orthogonal Johnson-slice basis and squared norms with respect to exchangeable measures; it supplies the relevant rank decomposition and incidence-algebra context. Both are strong **methodological antecedents**. Their inspected results do not directly state the present degree-two Walsh-band shell-compression eigenvalues with the fixed probability normalization, nor classify the exceptional **square-dimension spectral collisions**. Those arithmetic resonance conditions, not the general existence of a Johnson eigenbasis, are the distinctive statement here.

The full-text comparison also considered finite Slepian concentration methods for spherical domains, which concern different spatial and harmonic settings. Published work on exact Walsh frequency supports and Turán bounds on a weight-two Hamming shell addresses distinct operators. An earlier finite-cube concentration result for weighted halfspaces concerns a halfspace indicator, not a single exact Hamming level; the degree-two Hamming primitive projection endpoint calculation concerns the global projection norm, not fixed-weight restriction eigenvalues.

## Limitations

The spectrum is specialized to degree \(\le2\) and a **single interior Hamming shell**. For more general bandlimits, there are more Johnson sectors and the arithmetic crossing loci are not classified here. The work does not claim discovery of the general Johnson spectral decomposition, the Gelfand–Tsetlin basis, or the eigenvalues of arbitrary Terwilliger-algebra matrices: those structures are established prior literature. Although targeted comparison identified no directly stated square-dimension resonance, an implicit derivation via pre-existing general block formulas cannot be excluded as a residual novelty risk. The arithmetic spectral collision is proved within the stated model, and the rank theorem is independent of finite verification. No independent external audit has been performed.

## References

1. M. K. Srinivasan, *Symmetric chains, Gelfand–Tsetlin chains, and the Terwilliger algebra of the binary Hamming scheme*, arXiv:1001.0280v1, first public 2010-01-02. https://arxiv.org/abs/1001.0280
2. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142v1, first public 2014-06-01; Electron. J. Combin. 23 (2016), P1.23. https://arxiv.org/abs/1406.0142
3. A. W. Harrow, A. Kolla, and L. J. Schulman, *Dimension-free \(L_2\) maximal inequality for spherical means in the hypercube*, Theory Comput. 10 (2014), 55–75. https://doi.org/10.4086/toc.2014.v010a003
4. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Rev. 48 (2006), 504–536. https://doi.org/10.1137/S0036144504445765
