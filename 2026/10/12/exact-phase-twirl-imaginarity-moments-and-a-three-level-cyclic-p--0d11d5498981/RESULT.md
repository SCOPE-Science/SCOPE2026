# Exact phase-twirl imaginarity moments and a three-level cyclic-phase threshold

## Finding
For every integer \(d\ge2\), let \(\rho\) be a \(d\times d\) density matrix in a fixed reference basis. Independently choose \(\theta_j\) uniformly in \([0,2\pi)\) and put \(U_\theta=\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_d})\). Define \(\rho_\theta=U_\theta\rho U_\theta^\dagger\), its real part \(R_\theta=(\rho_\theta+\rho_\theta^T)/2\), and the purity-normalized real-sector statistic
\[
X_\theta=\frac{\operatorname{Tr}(R_\theta^2)}{P},\qquad P=\operatorname{Tr}(\rho^2)>0,\qquad S=\sum_j\rho_{jj}^2.
\]
The exact mean, variance, and third centered moment are
\[
\mathbb E X_\theta=\frac{P+S}{2P},\qquad
\operatorname{Var}(X_\theta)=\frac{1}{2P^2}\sum_{i<j}|\rho_{ij}|^4,
\]
\[
\mathbb E[(X_\theta-\mathbb EX_\theta)^3]
=\frac{3}{2P^3}\sum_{i<j<k}\operatorname{Re}(\rho_{ij}^2\rho_{jk}^2\rho_{ki}^2).
\]
The cubic statistic is identically zero in dimension \(d=2\), whereas it can have either sign for strictly positive density matrices in every \(d\ge3\), even when all entry magnitudes and the diagonal are held fixed.

## Assumptions and scope
All matrix transposes and real parts are taken in the same declared computational basis. \(\rho\) is Hermitian, positive semidefinite, and has unit trace. The diagonal phase variables are independent and Haar uniform on the circle; this is not the full Haar random-unitary ensemble. \(P\) and \(S\) are deterministic and unchanged by diagonal-unitary conjugation. \(X_\theta\in[0,1]\) is a normalized quadratic real-sector statistic, not the logarithm of that statistic. No claims are made about moments of \(-\log X_\theta\).

## Proof
Write \(z_j=e^{2i\theta_j}\), and define \(b_{ij}=\rho_{ij}^2\) for \(i\ne j\). The complex conjugation overlap is
\[
T_\theta=\operatorname{Tr}(\rho_\theta\rho_\theta^T)
=S+\sum_{i\ne j}b_{ij}z_i\overline z_j.
\]
Because \(\rho\) is Hermitian, \(b_{ji}=\overline{b_{ij}}\); hence \(T_\theta\) is real. Expanding \(R_\theta^2\) gives \(\operatorname{Tr}(R_\theta^2)=(P+T_\theta)/2\). Thus
\[
X_\theta-\mathbb EX_\theta=\frac{1}{2P}\sum_{i\ne j}b_{ij}z_i\overline z_j.
\]
Independence and uniformity imply \(\mathbb E\prod_j z_j^{a_j}=0\) unless every integer exponent \(a_j=0\). For the first moment no off-diagonal monomial survives. For the second, the only surviving ordered edge pairs are the two orientations of a single undirected edge. Consequently its unnormalized second centered moment is \(2\sum_{i<j}|b_{ij}|^2\), yielding the stated variance after division by \(4P^2\).

For three factors, every surviving monomial is a directed three-edge circulation on distinct vertices, i.e., one of the two cyclic orientations of a triangle. Each orientation contributes in \(3!=6\) orderings. For each unordered triangle \(\{i,j,k\}\), the contribution is therefore \(6b_{ij}b_{jk}b_{ki}+6\overline{b_{ij}b_{jk}b_{ki}}=12\operatorname{Re}(b_{ij}b_{jk}b_{ki})\). Division by \(8P^3\) gives the third-moment formula. In dimension two there are no triangles.

For sharpness of the dimension threshold, fix any \(d\ge3\) and \(0<\varepsilon<1/(2d)\). Let \(H_\pm\) be Hermitian with zero diagonal, with \((H_\pm)_{12}=(H_\pm)_{23}=1\), \((H_+)_{13}=1\) and \((H_-)_{13}=i\), their conjugate lower triangle, and every other entry zero. Set \(\rho_\pm=I_d/d+\varepsilon H_\pm\). Each row has total absolute off-diagonal weight at most \(2\varepsilon<1/d\), so strict diagonal dominance (or the quadratic-form estimate) proves \(\rho_\pm\) positive definite. They have equal diagonal entries and equal entrywise moduli. For both, \(P=1/d+6\varepsilon^2\), \(S=1/d\), and \(\operatorname{Var}X=3\varepsilon^4/(2P^2)\). But \(\rho_{12}^2\rho_{23}^2\rho_{31}^2\) equals \(+\varepsilon^6\) for one sign and \(-\varepsilon^6\) for the other, so the centered third moments equal \(+3\varepsilon^6/(2P^3)\) and \(-3\varepsilon^6/(2P^3)\), respectively.

## Verification
The standalone script `verify_phase.py` performs exhaustive character-balance checks for two- and three-edge monomials on \(3\), \(4\), and \(5\) vertices. It also enumerates all \(7^3\) assignments of seventh-root phases for each qutrit witness and compares the first three moments with the formulas. Seventh-root phases suffice for this finite-degree check because no nonzero Fourier exponent of degree at most three is a multiple of seven. Execution returned `VERIFY_OK`, including opposite signed cubic statistics. This exhaustive finite check is corroborative; the general proof is the torus-character argument above.

## Relationship to prior work
Aditya, Turkeshi, and Sierant establish an annealed Haar-random-circuit coherence–imaginarity relation and study quadratic resource observables [1]. The present theorem uses independent diagonal phases on an *arbitrary fixed density operator*, determines two higher centered moments of a normalized real-sector observable, and identifies the first phase-sensitive cyclic invariant. Guo et al. develop a geometric coherence–imaginarity resource decomposition [2]; that structural hierarchy is not a stated phase-twirl moment law. Related work on imaginarity of coherent superpositions studies the attainable conjugation overlaps rather than their random-phase third cumulant [3]. Standard Fourier character orthogonality is an ingredient here, not a novelty claim.

## Limitations
The phase twirl uses independent continuously uniform phases, not finite circuits, Markovian monitoring, or Haar-random global unitaries. The cubic formula is for the normalized quadratic statistic, not its logarithm. The result does not provide a higher-order joint distribution or a quantum computational advantage. Equivalent phase-moment formulas could occur implicitly in earlier Fourier or resource-theoretic literature; comparison against inaccessible full papers remains a priority risk.

## References
[1] S. Aditya, X. Turkeshi, and P. Sierant, *Equivalence of quantum resources under ergodic dynamics*, arXiv:2608.15197v1, first posted 2026-08-15.

[2] M.-L. Guo, N. Guan, B. Li, B. Hu, and S.-M. Fei, *Imaginarity as a Resource within Quantum Coherence: Geometric Decomposition and Operational Conversion*, arXiv:2607.14435v1 (2026).

[3] M. Xiao, D. Liu, and F. Shi, *Imaginarity of quantum superpositions*, Phys. Rev. A accepted paper, DOI:10.1103/7xk4-19hp (2026).
