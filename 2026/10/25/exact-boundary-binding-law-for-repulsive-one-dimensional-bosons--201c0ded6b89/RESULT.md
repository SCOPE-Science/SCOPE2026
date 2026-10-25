# Exact boundary binding law for repulsive one-dimensional bosons

## Finding

Consider the repulsive Lieb–Liniger Hamiltonian
\[
H_N=-\sum_{i=1}^{N}\partial_{x_i}^{2}+2g\sum_{i<j}\delta(x_i-x_j),\qquad g>0,
\]
on the bosonic half-line \(x_i\ge0\), with attractive Robin condition
\(\partial_{x_i}\Psi|_{x_i=0}=-\kappa\Psi\). For every integer \(N\ge2\) and
\(\kappa>(N-1)g\), define the ordered coordinates
\(x_{(1)}\le\cdots\le x_{(N)}\) and
\[
\Psi_N=C_N\exp\!\left[-\sum_{j=1}^{N}(\kappa-(j-1)g)x_{(j)}\right].
\]
This is an exact, strictly positive ground state with energy
\[
E_N=-\sum_{j=0}^{N-1}(\kappa-jg)^2.
\]
The state is square-integrable exactly when the last exponent is positive,
\(\kappa>(N-1)g\). The energy gap to the \((N-1)\)-particle boundary cluster is
\[
\Delta_N=E_{N-1}-E_N=(\kappa-(N-1)g)^2,
\]
and the mean outermost interparticle gap is
\[
\mathbb E[x_{(N)}-x_{(N-1)}]=\frac{1}{2(\kappa-(N-1)g)}.
\]
Thus the last-particle binding energy vanishes quadratically while the outer gap
scale diverges inversely as the boundary-string threshold is approached from above.

## Assumptions and scope

The kinetic coefficient is normalized to one, the pair interaction is the repulsive
contact potential \(2g\delta\) with \(g>0\), and all particles are identical bosons
on \([0,\infty)\). The boundary condition is Robin with attractive parameter
\(\kappa>0\). The claim concerns the explicit fully boundary-bound state and its
normalizability threshold; it does not classify every possible excited state or
assert a complete spectrum for arbitrary boundary parameters.

## Proof

Work first in the ordered chamber
\(0<x_1<\cdots<x_N\), and set \(a_j=\kappa-(j-1)g\). Away from collision
hyperplanes, \(\Psi_N=C_Ne^{-\sum_j a_jx_j}\) satisfies the free Schrödinger
equation with energy \(-\sum_j a_j^2\). At the boundary \(x_1=0\),
\(\partial_{x_1}\Psi_N=-a_1\Psi_N=-\kappa\Psi_N\), so the Robin condition holds.
At a contact \(x_j=x_{j+1}\), the symmetric continuation of the chamber wavefunction
has ordered-side derivative difference
\[
(\partial_{x_{j+1}}-\partial_{x_j})\Psi_N
=(a_j-a_{j+1})\Psi_N=g\Psi_N,
\]
which is the contact condition for the Hamiltonian with coefficient \(2g\). By bosonic symmetry, the Robin condition at the boundary holds for every labeled coordinate. Therefore the wavefunction is an exact eigenfunction.

For normalization, use gap coordinates \(y_1=x_1\) and
\(y_k=x_k-x_{k-1}\) for \(k\ge2\). Then
\[
\sum_{j=1}^{N}a_jx_j=\sum_{k=1}^{N}A_ky_k,\qquad
A_k=\sum_{j=k}^{N}a_j=(N-k+1)\left(\kappa-\frac{g(N+k-2)}{2}\right).
\]
The integral over the ordered chamber is \(\prod_{k=1}^{N}(2A_k)^{-1}\), so the full
symmetric state is normalized by
\[
C_N=\left(\frac{\prod_{k=1}^{N}2A_k}{N!}\right)^{1/2}.
\]
All \(A_k\) are positive precisely when \(\kappa>(N-1)g\); at equality
\(A_N=0\) and the norm diverges. Moreover,
\(E_{N-1}-E_N=a_N^2=(\kappa-(N-1)g)^2>0\), so this eigenvalue lies below the
threshold formed by an \((N-1)\)-particle boundary cluster and one free particle.
Its strictly positive wavefunction identifies it as the ground state by positivity
improvement of the Schrödinger semigroup. The gap variable \(y_N\) has normalized
exponential density \(2A_Ne^{-2A_Ny_N}\), giving mean \(1/(2A_N)\).

## Verification

The proof uses the differential equation in each collision-free chamber, the Robin
condition, and the exact contact jump. The normalization is evaluated analytically
in independent gap coordinates. No numerical extrapolation is used. The threshold
statement is about this explicit state: non-normalizability at equality does not,
by itself, classify all other spectral states.

## Relationship to prior work

Caudrelier and Crampe developed coordinate Bethe-ansatz equations for repulsive
one-dimensional contact-interacting bosons with a tunable impurity, including
half-line boundary cases; their paper studies one- and two-particle examples and
presents the general \(N\)-particle equations. The material inspected does not
state the explicit \(N\)-body positive Robin-boundary cluster, its closed energy sum,
or the final-gap law derived here. Gaudin's earlier boundary-energy work treats a
hard-wall box rather than this attractive Robin half-line. De Nardis, Krajenbrink,
Le Doussal, and Thiery classify boundary strings for the attractive-bulk
Lieb–Liniger gas, a different sign of the bulk interaction.

## Limitations

The result is for a continuum half-line and a single Robin boundary, not a finite
box, full-line transmitting defect, or lattice Bose–Hubbard model. The proof gives
the exact positive fully bound state when \(\kappa>(N-1)g\); it does not provide a
complete classification of excited states or of all possible bound states below
that parameter threshold. The boundary-cluster comparison uses the standard
cluster threshold for a free particle separating from the remaining boundary-bound
cluster. Independent review remains outstanding.

## References

1. V. Caudrelier and N. Crampe, “Exact results for the one-dimensional many-body
   problem with contact interaction: Including a tunable impurity,” arXiv:cond-mat/0501110
   (first posted 6 January 2005); *Reviews in Mathematical Physics* 19 (2007), 349–370.
   DOI: 10.1142/S0129055X07002973.
2. M. Gaudin, “Boundary Energy of a Bose Gas in One Dimension,” *Physical Review A*
   4 (1971), 386. DOI: 10.1103/PhysRevA.4.386.
3. J. De Nardis, A. Krajenbrink, P. Le Doussal, and T. Thiery, “Delta-Bose gas on a
   half-line and the KPZ equation: boundary bound states and unbinding transitions,”
   arXiv:1911.06133 (2019).
