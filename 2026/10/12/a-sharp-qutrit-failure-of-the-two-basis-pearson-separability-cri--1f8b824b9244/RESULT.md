# A sharp qutrit failure of the two-basis Pearson separability criterion

## Finding

For local dimensions \(d\ge2\), let two local projective observables on each party have mutually unbiased eigenbases, and define the Pearson coefficient of simultaneous local outcomes, whenever both marginal variances are nonzero, by
\[
\operatorname{Corr}_{\rho}(X,Y)=\frac{\operatorname{Tr}(\rho X\otimes Y)-\operatorname{Tr}(\rho_A X)\operatorname{Tr}(\rho_B Y)}{\sqrt{\operatorname{Var}_{\rho_A}(X)\operatorname{Var}_{\rho_B}(Y)}}.
\]
The proposed separability criterion \(|\operatorname{Corr}(A,B)|+|\operatorname{Corr}(C,D)|\le1\) holds for **every separable two-qubit state** and every pair of local mutually unbiased rank-one projective measurements. It **fails already for two qutrits**, even for a classical-classical state supported on two orthogonal product vectors, with standard equally spaced eigenvalue labels. Thus the smallest nontrivial local dimension allowing a separable false positive is exactly \(3\). The violation persists for explicit full-rank classical-classical states.

In the computational qutrit basis put
\[
A=\operatorname{diag}(-1,0,1),\quad \omega=e^{2\pi i/3},\quad F_{jk}=\omega^{jk}/\sqrt3\quad (j,k\in\{0,1,2\}),\quad C=FAF^\dagger.
\]
Let both parties use \(A\) in the first setting and \(C\) in the second. Define
\[
|\psi\rangle=(2|0\rangle-|1\rangle)/\sqrt5,\qquad |\phi\rangle=(|0\rangle+2|1\rangle+2|2\rangle)/3,
\]
and
\[
\rho=\tfrac12|\psi\psi\rangle\langle\psi\psi|+\tfrac12|\phi\phi\rangle\langle\phi\phi|.
\]
The exact correlations are
\[
\operatorname{Corr}_\rho(A,A)=\frac{17}{33},\qquad \operatorname{Corr}_\rho(C,C)=\frac{841}{1394},\qquad \frac{17}{33}+\frac{841}{1394}=\frac{51451}{46002}=1+\frac{5449}{46002}>1.
\]

## Assumptions and scope

On each local qutrit, \(A\) and \(C\) are nondegenerate Hermitian observables with eigenvalues \(-1,0,1\). Their eigenbases are mutually unbiased because every entry of \(F\) has squared modulus \(1/3\). Relabeling the eigenvalues as \(0,1,2\) changes neither Pearson coefficient: the transformation is affine with positive slope. All four local outcome variances appearing in the displayed witness are strictly positive. The two local subsystems have dimension \(3\); the qubit protection statement allows arbitrary local projective measurements whose two bases on each side are mutually unbiased, arbitrary separable mixtures and arbitrary (nonconstant) dichotomic eigenvalue assignments.

The two vectors satisfy \(\langle\psi|\phi\rangle=(2-2)/(3\sqrt5)=0\), and are normalized. Therefore \(\rho\) is not just separable: in a common orthonormal local basis extending \(\{|\psi\rangle,|\phi\rangle\}\), it is diagonal on product basis vectors and has zero quantum discord on either side (classical-classical).

## Proof

**Exact qutrit calculation.** For the two pure preparations the relevant local moments are

| Observable | Preparation | \(\langle O\rangle\) | \(\langle O^2\rangle\) |
|---|---|---:|---:|
| \(A\) | \(|\psi\rangle\) | \(-4/5\) | \(4/5\) |
| \(A\) | \(|\phi\rangle\) | \(1/3\) | \(5/9\) |
| \(C\) | \(|\psi\rangle\) | \(2/5\) | \(8/15\) |
| \(C\) | \(|\phi\rangle\) | \(-8/9\) | \(26/27\) |

They follow directly from the displayed normalized vectors and \(C=FAF^\dagger\); in particular, the phase \(\omega\) is a primitive cube root of unity. For a two-point mixture of identical product preparations, the two-party covariance of an observable \(O\) is \((\langle O\rangle_\psi-\langle O\rangle_\phi)^2/4\). Its local marginal variance is the average of the two second moments minus the square of the average first moment. Hence
\[
\begin{aligned}
\operatorname{Cov}_\rho(A,A)&=289/900,&\operatorname{Var}_{\rho_A}(A)&=187/300,\\
\operatorname{Cov}_\rho(C,C)&=841/2025,&\operatorname{Var}_{\rho_A}(C)&=1394/2025.
\end{aligned}
\]
Symmetry makes the Bob variances identical. Dividing establishes the two claimed rational Pearson coefficients and their strict sum. Positivity and separability require no numerical eigenvalue test: \(\rho\) is an explicit convex mixture of two product rank-one projectors.

**No qubit false positives.** Every pair of nondegenerate qubit mutually unbiased eigenbases corresponds, after an affine change of outcome scale, to two orthogonal Bloch axes. For any separable two-qubit state, write
\[\rho=\sum_k p_k\rho_k^A\otimes\rho_k^B,\qquad \rho_k^A=\tfrac12(I+\boldsymbol a_k\cdot\boldsymbol\sigma),\quad \rho_k^B=\tfrac12(I+\boldsymbol b_k\cdot\boldsymbol\sigma).\]
Here \(p_k\ge0\), \(\sum_kp_k=1\), and the Bloch vectors have norms at most \(1\). Let \(\boldsymbol a=\sum_kp_k\boldsymbol a_k\), \(\boldsymbol b=\sum_kp_k\boldsymbol b_k\). Let \(\boldsymbol u_1,\boldsymbol u_2\) be orthonormal axes for Alice and \(\boldsymbol v_1,\boldsymbol v_2\) orthonormal axes for Bob. If both average Bloch vectors have norm below \(1\), weighted classical Cauchy–Schwarz gives
\[
\sum_{j=1}^{2}|\operatorname{Corr}_{\rho}(\boldsymbol u_j\cdot\boldsymbol\sigma,\boldsymbol v_j\cdot\boldsymbol\sigma)|
\le\left[\sum_{j=1}^2\frac{\operatorname{Var}_p(\boldsymbol a_k\cdot\boldsymbol u_j)}{1-(\boldsymbol a\cdot\boldsymbol u_j)^2}\right]^{1/2}
\left[\sum_{j=1}^2\frac{\operatorname{Var}_p(\boldsymbol b_k\cdot\boldsymbol v_j)}{1-(\boldsymbol b\cdot\boldsymbol v_j)^2}\right]^{1/2}.
\]
Since \(1-(\boldsymbol a\cdot\boldsymbol u_j)^2\ge1-|\boldsymbol a|^2\) and orthogonality gives
\[
\sum_{j=1}^2\operatorname{Var}_p(\boldsymbol a_k\cdot\boldsymbol u_j)
\le\sum_kp_k|\boldsymbol a_k-\boldsymbol a|^2
=\sum_kp_k|\boldsymbol a_k|^2-|\boldsymbol a|^2
\le1-|\boldsymbol a|^2,
\]
the first bracket is at most \(1\), and so is the second. If an average Bloch vector has norm \(1\), every vector in its convex decomposition coincides, the joint state is product on that side and all defined Pearson covariances vanish. This completes the qubit bound for all separable states, proving that \(d=3\) is the minimum dimension for the counterexample.

**Full-rank persistence.** For \(\varepsilon=1/100\), the state
\[\rho_\varepsilon=(1-\varepsilon)\rho+\varepsilon I_9/9\]
is full rank (all eigenvalues at least \(\varepsilon/9\)) and remains classical-classical because both summands are diagonal in the same local product basis. Directly,
\[
\operatorname{Corr}_{\rho_\varepsilon}(A,A)=\frac{955317}{1872917},\qquad
\operatorname{Corr}_{\rho_\varepsilon}(C,C)=\frac{926431}{1549731},
\]
whose sum is strictly above \(1\). More generally strictness and positive variance imply persistence in a neighborhood of the two-point preparation within the separable-state family.

## Verification

Run `python verify.py` with SymPy installed. It constructs \(F\), the observables, all nine-by-nine density-matrix operators and the two covariance ratios from exact rational/radical arithmetic. It checks normalization, the mutually unbiased property, Hermiticity, orthogonality of the product preparations, each moment in the table, the exact threshold excess and the full-rank noisy witness. Expected output:

`VERIFY_OK MUB=passed separable_decomposition=passed Pearson_A=17/33 Pearson_C=841/1394 excess=5449/46002 full_rank=passed`

The all-qubit bound follows from the analytic Bloch-vector inequalities just proved, not from finite numerical testing.

## Relationship to prior work

Maccone, Bruß and Macchiavello (arXiv:1408.6851, Section on Pearson correlation) explicitly **conjectured** that a sum above \(1\) detects entanglement for arbitrary local dimension; the source presented random-state tests rather than a general separability proof. Jebarathinam, Home and Sinha (arXiv:1909.01372) analyzed Pearson coefficients for specified entangled and noisy two-qutrit families, not the above arbitrary classical-classical mixtures. Sadana, Kanjilal, Home and Sinha (arXiv:2201.06188, Section III.C and Appendix C) repeated the universal conjecture and verified it on restricted state families. None of these inspected statements entails or contains the explicit separable violation derived here.

Wang, Wang and Chen (arXiv:2608.03828) described a two-branch classical-classical mechanism violating a **mutual-information** complementary-correlation conjecture and related conditional-probability bounds. That is a different functional: mutual-information sums do not imply Pearson coefficient sums in general. For their stated qutrit two-branch source and the present standard computational/Fourier observable labels, the corresponding absolute Pearson coefficients evaluate to \(3/25\) and \(9/11\), with sum \(258/275<1\), so that particular construction does not itself supply the present Pearson violation. Complete access to their manuscript was unavailable, leaving an explicit residual literature risk.

## Limitations

The result is an existential, sharp **dimension** threshold, not the optimal amount of violation in dimension three or any higher dimension. It does not disprove the established mutual-information separability criterion or settle the unrelated Pearson-product conjecture. The published literature may contain an equivalent counterexample under a different observable convention; a negative database search is not mathematical proof of priority. The claims concern ideal projective measurements with nonzero variances and the explicitly stated outcome labeling.

## References

1. L. Maccone, D. Bruß and C. Macchiavello, *Complementarity and correlations*, arXiv:1408.6851 (first public 2014-08-28), Phys. Rev. Lett. **114**, 130401 (2015), DOI:10.1103/PhysRevLett.114.130401.
2. C. Jebarathinam, D. Home and U. Sinha, *Pearson correlation coefficient as a measure for certifying and quantifying high-dimensional entanglement*, arXiv:1909.01372, Phys. Rev. A **101**, 022112 (2020), DOI:10.1103/PhysRevA.101.022112.
3. S. Sadana, S. Kanjilal, D. Home and U. Sinha, *Relating an entanglement measure with statistical correlators for two-qudit mixed states using only a pair of complementary observables*, arXiv:2201.06188 (2022).
4. J. Wang, Q. Wang and K. Chen, *When complementary measurements count the same classical bit twice: counterexamples to CQC, ECQC, and complementarity-based certification*, arXiv:2608.03828 (2026). This source treats principally the mutual-information functional; complete source access for detailed Pearson comparisons was unavailable.
