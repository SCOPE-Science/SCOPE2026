# A single weak link determines the exact rank and nullspace of quantum-ring average mixing

## Finding

**Theorem (one-bond-defect rank and kernel).** For each integer \(n\ge3\) and each real \(g\ge0\), let \(H_g\) be the symmetric \(n\)-by-\(n\) Hamiltonian on vertices \(0,\ldots,n-1\) with coupling one along the path edges \(\{j,j+1\}\) for \(0\le j<n-1\), coupling \(g\) on the closing edge \(\{0,n-1\}\), and zero diagonal. Let
\[
\widehat M_g=\lim_{T\to\infty}\frac1T\int_0^T \bigl(e^{itH_g}\circ e^{-itH_g}\bigr)\,dt,
\]
where \(\circ\) denotes entrywise multiplication. Set \(q=\lceil n/2\rceil\) and let \(R\) reverse the vertex labels, \((Rx)_j=x_{n-1-j}\). Then
\[
\operatorname{rank}\widehat M_g=
\begin{cases}
q,&g\ne1,\\
n,&g=1\text{ and }n\text{ odd},\\
n/2,&g=1\text{ and }n\text{ even}.
\end{cases}
\]
For all \(g\ne1\), the entire kernel is the reversal-antisymmetric subspace
\[
\ker\widehat M_g=\{x\in\mathbb R^n:Rx=-x\}.
\]
At \(g=1\), the kernel vanishes for odd \(n\); for even \(n\), it is the antipodal-antisymmetric subspace \(\{x:x_{j+n/2}=-x_j\text{ for }0\le j<n/2\}\).

There is an exact polynomial certificate for the nonunit-link case. Form the \(q\)-by-\(q\) diagonal even-moment matrix
\[
W(g)_{r,k}=(H_g^{2k})_{r,r}\qquad(0\le r,k<q).
\]
Then for *every* \(g\ge0\), including the unit link,
\[
\boxed{\det W(g)=(-1)^{q-1}(g^2-1)^{q-1}.}
\]
Thus every arbitrarily weak but nonzero defect \(g\ne1\) reduces average-mixing rank on odd rings by \((n-1)/2\), whereas on even rings it preserves rank \(n/2\) while changing its kernel from antipodal to reversal antisymmetry.

## Assumptions and scope

The Hamiltonian is real symmetric, has one *edge* perturbation (not a site potential), and all other edges have unit positive coupling. The theorem includes a severed link \(g=0\), positive weakened links \(0<g<1\), a perfect link \(g=1\), and enhanced links \(g>1\). The graph is a simple cycle for \(g>0\), except that its edges are weighted. The case \(n=2\), which would have coincident closing and path edges, is excluded. No bound is imposed on \(n\) or \(g\).

The average-mixing matrix is positive semidefinite and is the infinite-time Cesàro mean; this is not a statement about instantaneous uniform mixing or finite-time convergence rates. The characteristic eigenvalues of \(H_g\) can be irrational. All rank and nullspace assertions hold exactly.

## Proof

**1. Spectral reduction.** Let the distinct eigenvalues of \(H_g\) be \(\lambda_s\) with orthogonal projectors \(E_s\). Expanding the unitary evolution into projectors and averaging oscillatory cross terms gives the exact identity
\[
\widehat M_g=\sum_s E_s\circ E_s.
\]
If the spectrum is simple, write \(E_s=v_sv_s^{\mathsf T}\) for a real unit eigenvector. Put \(B_{j,s}=v_s(j)^2\). Then \(\widehat M_g=BB^{\mathsf T}\) and \(\operatorname{rank}\widehat M_g=\operatorname{rank}B\). Also, for each nonnegative integer \(k\),
\[
(H_g^{2k})_{j,j}=\sum_s\lambda_s^{2k}B_{j,s}.
\]
Consequently the moment matrix \(W(g)\), restricted to the indicated rows, has rank no larger than \(B\).

**2. Spectrum is simple away from a unit link.** Fix an eigenvalue \(\lambda\) and eigenvector \(v\). Define the polynomials \(u_{-1}=0\), \(u_0=1\), and \(u_{h+1}(\lambda)=\lambda u_h(\lambda)-u_{h-1}(\lambda)\). The eigenvalue recurrence at the ordinary path vertices gives, for \(1\le j\le n-1\),
\[
v_j=u_j(\lambda)v_0-g u_{j-1}(\lambda)v_{n-1}.
\]
The two endpoint equations therefore imply
\[
\bigl(1+gu_{n-2}(\lambda)\bigr)v_{n-1}-u_{n-1}(\lambda)v_0=0,
\]
\[
\bigl(u_{n-2}(\lambda)+g\bigr)v_0-\bigl(\lambda+gu_{n-3}(\lambda)\bigr)v_{n-1}=0.
\]
The pair \((v_0,v_{n-1})\) determines all of \(v\), so an eigenspace of dimension at least two would make *both* displayed linear forms vanish identically. In particular, \(1+gu_{n-2}(\lambda)=0\) and \(u_{n-2}(\lambda)+g=0\), forcing \(g^2=1\). Since \(g\ge0\), every \(g\ne1\) has simple spectrum.

**3. Reflection gives the upper rank bound.** For all \(g\), \(H_g\) commutes with vertex reversal \(R\). When \(g\ne1\), every real eigenvector has a definite reversal parity, \(Rv_s=\pm v_s\), by spectral simplicity. Hence its squared amplitudes satisfy \(B_{j,s}=B_{n-1-j,s}\). There are exactly \(q=\lceil n/2\rceil\) reflection orbits, so \(\operatorname{rank}\widehat M_g\le q\) and every reversal-antisymmetric vector lies in its kernel.

**4. Exact triangular even-moment certificate.** Write \(c_k=\binom{2k}{k}\). Because \(0\le k<q\) implies \(2k<n\), every closed length-\(2k\) walk around the ring has winding number zero: on the universal-cover line it consists of exactly \(k\) positive and \(k\) negative steps. Without a bond defect there are precisely \(c_k\) such walks from any vertex. Consider a representative vertex \(r\in\{0,\ldots,q-1\}\). The shortest closed walk from \(r\) that traverses the defective edge has length \(2r+2\) (possibly tied by the other route only at the most distant representative, where that length exceeds the moments considered). It follows that
\[
W(g)_{r,k}=c_k\quad\text{when }r\ge k,
\]
and, for \(0\le r<q-1\), the *unique* first defect-traversing walk at \(2r+2\) steps crosses and immediately retraces the closing edge; hence
\[
W(g)_{r,r+1}-c_{r+1}=g^2-1.
\]
Now replace each column \(k\ge1\) of \(W(g)\) by itself minus \(c_k\) times the first (all-ones) column. The bottom row becomes \((1,0,\ldots,0)\). Deleting this row and the first column leaves an upper-triangular \((q-1)\)-by-\((q-1)\) matrix with diagonal \(g^2-1\). Expansion along the bottom row yields
\[
\det W(g)=(-1)^{q-1}(g^2-1)^{q-1}.
\]
For \(g\ne1\), the moment matrix is invertible, so \(\operatorname{rank}B\ge q\). Combined with the reflection bound this proves rank exactly \(q\); the previously identified reversal-antisymmetric subspace has dimension \(n-q\) and is therefore the entire kernel.

**5. Unperturbed cycle boundary.** At \(g=1\), the exact average-mixing formula for the unweighted cycle, proved in Godsil's *Average Mixing of Continuous Quantum Walks*, Section 6, is
\[
\widehat M_1=\frac{n-1}{n^2}J+\frac1n I\quad(n\text{ odd}),
\]
\[
\widehat M_1=\frac{n-2}{n^2}J+\frac1n(I+P^{n/2})\quad(n\text{ even}),
\]
where \(J\) is the all-ones matrix and \(P\) cyclically shifts vertices. On an odd ring the second term makes the matrix positive definite. On an even ring \(I+P^{n/2}\) acts as two on antipodally symmetric vectors and as zero on antipodally antisymmetric vectors; the all-ones term vanishes on the latter. This gives rank \(n/2\) and exactly the stated kernel. The unperturbed formulas themselves are prior work, not claimed new. The severed-link \(g=0\) case is likewise compatible with Godsil's known path formula.

## Verification

The included `verify.py` uses exact rational arithmetic to reconstruct \(H_g^{2k}\), the moments, the triangular diagonal identities, and their determinant for each \(3\le n\le25\) and eight rational values of \(g\), including \(0\) and \(1\). It separately diagonalizes \(H_g\), groups any repeated eigenvalues into spectral projectors, constructs their Schur-square sum, and checks rank and reversal symmetry for \(3\le n\le18\) and seven real couplings. Execute `python verify.py` with Python 3 and NumPy. Observed result:

```text
VERIFY_OK exact_moment_profiles=184 independent_spectral_profiles=112 spectral_entries=14728 orders=3..25
```

The finite checks are corroborative; the recurrence, walk-counting, and spectral proofs above cover the infinite parameter family without numerical assumptions.

## Relationship to prior work

Godsil (2011), Sections 4 and 6, provides exact average mixing for the path and the *unperturbed* cycle, covering the boundary values \(g=0\) and \(g=1\) separately. Adamczak et al. (2007) treat quantum mixing in ordinary cycles and Abelian circulants, but the nonunit-link Hamiltonian is no longer circulant. Coutinho et al. (2018) give general commutant, projector, and rank machinery but not the bond-dependent exact rank or kernel. Godsil et al. (2017) study edge perturbations of strongly regular graphs for state transfer, which does not furnish a general cycle average-mixing rank theorem. Li and Wang (2015) study defects on an infinite line, with different geometry and observables. Coutinho et al. (2022) provide general spectral tools for exact quantum walk averages; this finding specializes to a structurally different weighted-ring question and supplies a new determinant witness.

The discrete moment determinant and the classification of the full nullspace for an arbitrary single nonunit edge are the distinct claims. The comparison does not assert exclusive priority; an unidentified stronger theorem for Jacobi-type cyclic matrices or symmetric spectral intensities may imply the result.

## Limitations

Only a single nonnegative real edge weight varies; arbitrary multiple defects, magnetic phases, and on-site potentials are not classified. The observation concerns Cesàro-average ranks, not the existence of perfect transfer, instantaneous mixing, or mixing-time estimates. The originality assessment is based on the specific primary sources inspected and available searchable records; it cannot exclude all related results. Independent mathematical review has not been performed.

## References

1. C. Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578, Sections 4 and 6 (path and unperturbed-cycle formulas).
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591, Sections 3–5 (commutant, rank, and automorphisms).
3. W. Adamczak, K. Andrew, L. Bergen, D. Ethier, P. Hernberg, J. Lin, C. Tamon, *Non-uniform mixing of quantum walk on cycles*, arXiv:0708.2096 (unweighted cycles and circulants).
4. C. Godsil, K. Guo, M. Kempton, G. Lippner, *State transfer in strongly regular graphs with an edge perturbation*, arXiv:1710.02181.
5. Z. J. Li and J. B. Wang, *Single-point position and transition defects in continuous time quantum walks*, arXiv:1502.04289 / Scientific Reports 5, 13585 (2015).
6. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public version, 2022-08-18; primary MSC 81P68).
