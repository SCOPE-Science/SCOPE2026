# A sharp-order E-versus-K row-selection gap for two-dimensional orthonormal frames

## Finding
Let \(N\ge 2\), and let \(U\in\mathbb R^{N\times2}\) satisfy \(U^{\mathsf T}U=I_2\). For a two-element set \(J\subseteq\{1,\ldots,N\}\), write \(B_J=U[J,:]\), and put \(\kappa(B_J)=\sigma_{\max}(B_J)/\sigma_{\min}(B_J)\) when \(B_J\) is invertible (and infinity otherwise). An **E-optimal** selection maximizes \(\sigma_{\min}(B_J)\); a **K-optimal** selection minimizes \(\kappa(B_J)\).

Every E-optimal selection is invertible and satisfies
\[
\kappa(B_J)\le \sqrt{2(N-1)}.
\]
Moreover, for every \(N\ge5\) there is an explicit orthonormal-column \(U_N\) for which **every** E-optimal selection has condition number exactly \(\sqrt{N-3}\), whereas a K-optimal selection has condition number \(1\). In particular, the worst possible multiplicative gap between E-optimal and K-optimal two-row selection grows at the sharp order \(\Theta(\sqrt N)\).

The statement concerns the condition number of a *row-restricted basis*. It does not challenge E-optimality as a criterion for maximizing the smallest singular value, and it does not assert that row conditioning alone controls every sketched Krylov error.

## Assumptions and scope
All matrices and row selections are real; the dimension of the column subspace is precisely two; exactly two **distinct, unweighted** coordinate rows are retained. The input basis has orthonormal columns. No generic-position, sparsity, randomness or finite-precision hypothesis is imposed. The construction has repeated rows but full column rank; its two-dimensional column space can also be realized as a second-order Krylov subspace for a suitable real linear operator and starting vector.

The comparison is invariant under a common positive rescaling of a selected two-row matrix. E- and K-optimality are **different** optimization criteria; in particular, choosing a tiny but isotropically balanced row pair can minimize conditioning while providing poor unscaled length preservation.

## Proof
**Universal bound.** Denote row \(i\) of \(U\) by \(r_i\in\mathbb R^2\), and select \(i\) maximizing \(\ell=\|r_i\|_2^2>0\). Let \(v\) be a unit vector perpendicular to \(r_i\). Since \(U^{\mathsf T}U=I_2\),
\[
\sum_{j\ne i}|r_jv|^2=\|Uv\|_2^2=1.
\]
Consequently, some \(j\ne i\) satisfies \(p=|r_jv|^2\ge1/(N-1)\). For the square matrix \(B\) with rows \(r_i,r_j\),
\[
\det(B^{\mathsf T}B)=\ell p,
\qquad \operatorname{tr}(B^{\mathsf T}B)=\ell+\|r_j\|_2^2\le2\ell.
\]
Writing the two positive eigenvalues of \(B^{\mathsf T}B\) as \(\lambda_-\le\lambda_+\), one gets
\[
\lambda_-\ge\frac{\lambda_-\lambda_+}{\lambda_-+\lambda_+}\ge\frac{\ell p}{2\ell}\ge\frac1{2(N-1)}.
\]
Therefore an E-optimal pair \(J_E\) satisfies \(\sigma_{\min}(B_{J_E})\ge[2(N-1)]^{-1/2}\). Because \(B_{J_E}\) is obtained by deleting rows from \(U\), \(\sigma_{\max}(B_{J_E})\le\|U\|_2=1\). Hence \(\kappa(B_{J_E})\le\sqrt{2(N-1)}\), uniformly over *all* E-optimal pairs.

**Constructed gap.** Fix \(N\ge5\) and define
\[
t=(4N-11)^{-1/2},\qquad a=2\sqrt{N-3}\,t.
\]
Let the \(N\) rows of \(U_N\), in order, be
\[
(a,0),\quad(0,2t),\quad(t,0),\quad(0,t),
\quad\underbrace{(0,2t),\ldots,(0,2t)}_{N-4\text{ additional rows}}.
\]
The columns are orthogonal, and their squared lengths equal \(a^2+t^2=(4N-11)t^2=1\) and \((4N-11)t^2=1\), respectively. Thus \(U_N^{\mathsf T}U_N=I_2\). Since \(a>2t>t\), every nonsingular two-row restriction selects one row on each coordinate axis. Its smaller singular value is at most \(2t\), and equality holds **only** by selecting \((a,0)\) together with one of the rows \((0,2t)\). Every E-optimal restriction therefore has singular values \(a,2t\) and condition number
\[
\kappa(B_{J_E})=\frac a{2t}=\sqrt{N-3}.
\]
But the pair of rows \((t,0)\) and \((0,t)\) forms \(tI_2\), which has condition number \(1\), the least possible value. Thus, if
\[
G_N=\sup_{U^{\mathsf T}U=I_2}\ \sup_{J_E\in\arg\max_{|J|=2}\sigma_{\min}(B_J)}\frac{\kappa(B_{J_E})}{\min_{|J|=2}\kappa(B_J)},
\]
then
\[
\sqrt{N-3}\le G_N\le\sqrt{2(N-1)}\quad (N\ge5),
\]
which proves the claimed sharp asymptotic order. The upper bound also holds for \(N=2,3,4\).

## Verification
The standalone `check.py` builds the explicit family, enumerates all unordered row pairs, verifies orthonormality, checks **every** E-optimal pair and confirms the K-optimal value. It also tests the universal inequality on independent randomly generated orthonormal-column frames. The exact proof above is independent of these finite experiments.

Reproduce with `python check.py` using Python 3 and NumPy. No input data files are required.

## Relationship to prior work
Bergermann (arXiv:2604.07158, 2026), Section 3.1 and Section 4, analyzes deterministic row-subset sketches for Krylov methods and motivates maximizing the least singular value of the sketched basis. The present result compares that **E-optimal criterion** with minimizing the spectral condition number and quantifies a sharp-order dimensional separation on orthonormal two-column inputs; Bergermann does not assert the two optimization problems coincide.

Drmač and Gugercin (arXiv:1505.00370, 2015), especially Section 2, develop Q-DEIM with bounds for the inverse of a selected orthonormal-basis submatrix. Avron and Boutsidis (arXiv:1201.0127, 2011), Sections 1 and 4, study minimization of selected-submatrix pseudoinverse norms and associated lower bounds. These control E-type quantities but do not by themselves compare *an E-optimal subset* to *a different K-optimal subset* for the same orthonormal frame. Ye and Zhou (DOI 10.1137/110850268, 2013) distinguish condition-number-optimal regression designs, but their polynomial-regression setting is not this unrestricted two-column row-selection extremal problem.

## Limitations
This gives a matching **order** rather than the exact best multiplicative constant or the exact finite-\(N\) supremum. It does not analyze DEIM or Q-DEIM's actual greedy output, randomized selection, the cost or precision of global row scaling, oversampling, or end-to-end Krylov accuracy. The large-gap examples have strongly nonuniform row leverage and can be recognized from their axis-aligned supports; the theorem does not imply the same gap on incoherent Fourier-type frames. Established distinctions between E- and K-optimal experimental designs mean that priority for their broad conceptual separation is not claimed. Possible unindexed prior formulations of this precise extremal comparison remain a bibliographic risk.

## References
1. K. Bergermann, *Deterministic sketching for Krylov subspace methods*, arXiv:2604.07158, first posted 2026-04-08. https://arxiv.org/abs/2604.07158
2. Z. Drmač and S. Gugercin, *A New Selection Operator for the Discrete Empirical Interpolation Method*, arXiv:1505.00370 (2015). https://arxiv.org/abs/1505.00370
3. H. Avron and C. Boutsidis, *Faster Subset Selection for Matrices and Applications*, arXiv:1201.0127 (2011). https://arxiv.org/abs/1201.0127
4. J. J. Ye and J. Zhou, *Minimizing the Condition Number to Construct Design Points for Polynomial Regression Models*, SIAM J. Optim. (2013), DOI:10.1137/110850268.
