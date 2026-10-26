# Complete stiffness-disorder pinning criterion for freely terminated mass-dimer chains

## Finding
Fix an integer \(N\ge2\). Consider \(N\) consecutive mechanical dimers with freely terminated endpoints, each comprising two positive point masses \(\alpha_i,\beta_i\) linked by an internal spring \(a_i>0\). The right mass of dimer \(i\) is linked to the left mass of dimer \(i+1\) by an independently variable spring \(b_i>0\), for \(1\le i<N\). There are no other springs.

Let \(\lambda_1(\mathbf b)<\cdots<\lambda_{2N}(\mathbf b)\) denote the ordered squared normal-mode frequencies (with \(\lambda_1=0\)). Define the isolated-dimer optical squared frequencies
\[
\Omega_i^2=a_i\left(\frac1{\alpha_i}+\frac1{\beta_i}\right).
\]
The following are equivalent:

1. A positive eigenvalue remains constant on a nonempty open subset of the positive inter-dimer stiffness domain \((0,\infty)^{N-1}\).
2. At some positive coupling vector, a positive eigenvalue has **all** \(N-1\) partial derivatives with respect to the couplings equal to zero.
3. The local optical frequencies coincide: \(\Omega_1^2=\cdots=\Omega_N^2=\Lambda>0\).

When these equivalent conditions hold, **for every** \(\mathbf b\in(0,\infty)^{N-1}\), the number \(\Lambda\) is the **simple \((N+1)\)-st squared eigenfrequency**, \(\lambda_{N+1}(\mathbf b)=\Lambda\). Its complete displacement profile, up to a nonzero scalar, is
\[
 u_{A_1}=1,\qquad
 u_{B_i}=-\frac{\alpha_i}{\beta_i}\,u_{A_i},\qquad
 u_{A_{i+1}}=u_{B_i}\quad(1\le i<N).
\]
Thus every inter-dimer spring has zero extension and the entire mode shape, not merely its frequency, is independent of every positive inter-dimer spring stiffness. In the uniform mass case \(\alpha_i=\alpha\), \(\beta_i=\beta\), the left-coordinate amplitudes equal \(u_{A_i}=(-\alpha/\beta)^{i-1}\), giving explicit exponential localization towards the left if \(\alpha<\beta\), towards the right if \(\alpha>\beta\), and no exponential localization if \(\alpha=\beta\).

## Assumptions and scope
Displacements are real and scalar, oscillations are linear, springs are nearest-neighbour Hookean elements, all masses and all springs are strictly positive, and the two terminal masses are free. The \(2N\)-component displacement \(u\) obeys the generalized eigenproblem
\[
 K(\mathbf b)u=\lambda M u,\qquad
 M=\operatorname{diag}(\alpha_1,\beta_1,\ldots,\alpha_N,\beta_N),
\]
where \(K\) is the weighted path-graph stiffness matrix: its quadratic form is
\[
 u^{\mathsf T}K(\mathbf b)u=
 \sum_{i=1}^{N}a_i(u_{A_i}-u_{B_i})^2+
 \sum_{i=1}^{N-1}b_i(u_{B_i}-u_{A_{i+1}})^2.
\]
The derivative condition refers to the smoothly ordered simple eigenvalue branches. A fixed eigenvalue means fixed **squared** frequency; the corresponding positive angular frequency is \(\sqrt\Lambda\). The assertion is exact for any finite \(N\) and arbitrary positive, not necessarily small, coupling changes.

## Proof
**1. Simplicity and differentiability.** Conjugating the pencil by \(M^{-1/2}\) gives a real symmetric tridiagonal matrix with nonzero off-diagonal entries \(-a_i/\sqrt{\alpha_i\beta_i}\) and \(-b_i/\sqrt{\beta_i\alpha_{i+1}}\). Such an irreducible Jacobi matrix has simple real eigenvalues. Every \(\lambda_j(\mathbf b)\) therefore varies differentiably with the positive spring parameters. Its lowest eigenvalue is the simple translational mode \(\lambda_1=0\).

**2. A complete sensitivity identity.** If \(u_j\) is the real eigenvector of the \(j\)-th branch normalized by \(u_j^{\mathsf T}M u_j=1\), differentiate the generalized eigenproblem. Hellmann–Feynman differentiation and \(\partial K/\partial b_i=(e_{B_i}-e_{A_{i+1}})(e_{B_i}-e_{A_{i+1}})^{\mathsf T}\) give
\[
 \frac{\partial\lambda_j}{\partial b_i}
 =(u_{j,B_i}-u_{j,A_{i+1}})^2\ge0.
\]
Thus all such derivatives vanish precisely when every inter-dimer spring is unstretched. Constancy on a nonempty open set implies simultaneous vanishing at any interior point, proving implication 1 to 2.

**3. Necessity.** If the positive-mode derivatives all vanish, \(u_{B_i}=u_{A_{i+1}}\) at every inter-dimer bond. Consequently the external spring forces vanish and the eigenproblem restricts within every dimer to
\[
 a_i(u_{A_i}-u_{B_i})=\lambda\alpha_i u_{A_i},\qquad
 a_i(u_{B_i}-u_{A_i})=\lambda\beta_i u_{B_i}.
\]
A nonzero component in any dimer forces that dimer onto its positive optical eigenvalue \(a_i(1/\alpha_i+1/\beta_i)\), with \(u_{B_i}=-(\alpha_i/\beta_i)u_{A_i}\). No dimer can be identically zero: if one were, the zero-extension equalities and the positive internal springs would successively force every adjacent dimer to vanish, contradicting \(u\ne0\). Therefore every dimer is nonzero, and \(\lambda=\Omega_i^2\) for every \(i\). This proves 2 to 3.

**4. Sufficiency and exact robustness.** If all \(\Omega_i^2=\Lambda\), set \(u_{A_1}=1\), take \(u_{B_i}=-(\alpha_i/\beta_i)u_{A_i}\), and set \(u_{A_{i+1}}=u_{B_i}\) recursively. Each local pair satisfies its own optical equations at \(\Lambda\), while every inter-dimer spring contributes exactly zero force regardless of the size of \(b_i>0\). Hence \(K(\mathbf b)u=\Lambda Mu\) for **all** coupling vectors, with one unchanged eigenvector. In particular, 3 implies 1.

**5. Exact ordinal and uniqueness.** The constructed eigenvector has no zero entries. Its sign changes occur exactly once across each internal dimer spring because \(u_{A_i}u_{B_i}<0\), and never across an inter-dimer spring because \(u_{B_i}=u_{A_{i+1}}\). Thus there are exactly \(N\) sign changes along the entire ordered chain. The discrete Sturm oscillation theorem for a real Jacobi matrix with strictly negative off-diagonals identifies it as the \((N+1)\)-st eigenvector in ascending eigenvalue order. Irreducibility gives simplicity. For uniform mass ratios the recurrence reduces to the geometric profile claimed above. This completes all equivalences and conclusions.

## Verification
The standalone program `verify.py` constructs the full finite generalized eigenproblem directly and compares its sorted eigenpairs with the exact formulas. Its deterministic run checked 900 random heterogeneous tuned chains for the pinned eigenvalue, its unique spectral index, its eigenvector and zero inter-dimer strain, and further compared 900 large independent spring-parameter changes, 900 local optical detunings, and 900 central finite-difference evaluations of the Hellmann–Feynman identity. A separate 100-case test verified the uniform geometric envelope. All 5,500 categorized tests passed. The maximum normalized residual observed for an exact constructed mode was below \(10^{-15}\), and the maximum recorded finite-difference derivative discrepancy below \(2.6\times10^{-8}\). These finite tests are consistency checks; the universal assertion for all positive parameters follows from the analytic proof, not from numerical sampling.

## Relationship to prior work
Wallis (1957) established the classical finite alternating-mass, uniform-spring surface-vibration phenomenon for free ends. Allein and collaborators (2023) analyzed the mass-dimer edge state using higher-order strain coordinates and described the role of hidden chiral symmetry. Vishwakarma and collaborators (2025) investigated symmetry-preserving disorder and robust spinner-lattice boundary states. These results explain the periodic or symmetry-constrained setting; the statement here addresses the full independent \((N-1)\)-parameter cone of inter-dimer stiffnesses while allowing arbitrary heterogeneous positive masses and in-cell stiffnesses, and proves a necessary-and-sufficient criterion and exact modal index. Lecomte (2014) studied disturbed spring–mass spectral root and zero loci in a different model. The general Hellmann–Feynman and Jacobi oscillation tools used here are standard and are not claimed as new.

## Limitations
The model excludes grounding springs, damping, long-range bonds, multi-dimensional motions, nonlinearity, and clamped boundaries. Couplings must stay positive: if any inter-dimer spring vanishes, the Jacobi matrix becomes reducible and simplicity can fail. The invariant mode's eigenvalue need not be uniformly separated from neighbouring eigenvalues as stiffnesses vary, and localization is not guaranteed for arbitrary heterogeneous mass ratios. The theorem does not assert a bulk topological invariant or experimental immunity to mass or in-cell spring errors. Historical priority of the complete heterogeneous criterion may require further scrutiny because not every relevant older article was accessible in full.

## References
1. R. F. Wallis, “Effect of Free Ends on the Vibration Frequencies of One-Dimensional Lattices,” *Physical Review* 105, 540 (1957); https://doi.org/10.1103/PhysRev.105.540.
2. F. Allein et al., “Strain topological metamaterials and revealing hidden topology in higher-order coordinates,” *Nature Communications* 14, 6633 (2023); https://doi.org/10.1038/s41467-023-42321-3.
3. U. Vishwakarma et al., “Edge states with hidden topology in spinner lattices,” *Communications Physics* 8, 83 (2025); https://doi.org/10.1038/s42005-025-01981-x.
4. C. Lecomte, “Zero and root loci of disturbed spring–mass systems,” *Proceedings of the Royal Society A* 470, 20130751 (2014); https://doi.org/10.1098/rspa.2013.0751.
5. V. Meunier, “Topological edge and domain-wall phonons in the mass-dimerized diatomic chain,” arXiv:2610.23300v1 (2026); https://arxiv.org/abs/2610.23300.
