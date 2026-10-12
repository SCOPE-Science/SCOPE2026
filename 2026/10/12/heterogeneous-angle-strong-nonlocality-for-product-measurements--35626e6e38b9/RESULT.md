# Heterogeneous-angle strong nonlocality for product measurements
## Finding
For every integer \(w\ge 2\), choose angles
\[
0<\theta_i<\frac{\pi}{2},\qquad \sum_{i=1}^w\theta_i=\frac{\pi}{2}.
\]
At site \(i\), let \(\mathcal Z_i\) be the computational-basis projective measurement and let \(\mathcal U_i\) be the projective measurement in the rotated basis
\[
|u_i\rangle=\cos\theta_i|0\rangle+\sin\theta_i|1\rangle,\qquad
|u_i^\perp\rangle=\sin\theta_i|0\rangle-\cos\theta_i|1\rangle.
\]
Define the two product measurements \(\mathcal Z=\bigotimes_i\mathcal Z_i\) and \(\mathcal U=\bigotimes_i\mathcal U_i\). Then \(\mathcal Z\) and \(\mathcal U\) are perfectly distinguishable with one global use, without an ancilla, but they are not perfectly distinguishable by any finite-round LOCC protocol across any nontrivial bipartition, even when all sites on each side are allowed arbitrary joint quantum operations.

Equivalently, the equal-angle strong-nonlocality construction \(\theta_i=\pi/(2w)\) is one point of a full positive \(w-1\)-dimensional simplex of strongly nonlocal product-measurement pairs.

## Assumptions and scope
The statement concerns a single use of the distributed product measurement, with arbitrary local ancillas and arbitrary finite-round LOCC processing across a chosen bipartition. The outcome labels at each site are fixed consistently between the computational and rotated measurements. The strict inequalities \(\theta_i>0\) are essential to the all-bipartition conclusion: they ensure that every proper nonempty subset has total rotation strictly between \(0\) and \(\pi/2\).

No claim is made about infinite-round LOCC, separable operations strictly larger than finite-round LOCC, noisy discrimination, or the optimal success probability away from the hyperplane \(\sum_i\theta_i=\pi/2\).

## Proof
Use the parity probe
\[
|\Psi_w\rangle=\frac{1}{\sqrt{2^{w-1}}}\sum_{|x|\,\mathrm{even}}(-1)^{|x|/2}|x\rangle.
\]
Under \(\mathcal Z\), only even-parity outcome strings occur.

For the rotated measurement, let \(y\in\{0,1}^w\) denote an outcome string, where \(y_i=0\) selects \(|u_i\rangle\) and \(y_i=1\) selects \(|u_i^\perp\rangle\), and put \(r=|y|\) and \(\Theta=\sum_i\theta_i\). Since \((-1)^{|x|/2}=i^{|x|}\) on even-weight strings, the even-parity projection of the product expansion gives
\[
\langle u_{1,y_1}\otimes\cdots\otimes u_{w,y_w}|\Psi_w\rangle
=\frac{1}{\sqrt{2^{w-1}}}\cos\!\left(\Theta-\frac{r\pi}{2}\right).
\]
Indeed, the two parity-projected generating products are \((-i)^r e^{i\Theta}\) and \(i^r e^{-i\Theta}\). At \(\Theta=\pi/2\), the displayed amplitude vanishes for every even \(r\) and has modulus \(2^{-(w-1)/2}\) for every odd \(r\). Thus \(\mathcal U\) has only odd-parity outcomes on the same probe. The two outcome supports are disjoint, proving global perfect discrimination.

It remains to prove the obstruction across an arbitrary bipartition \(S|S^c\), where \(S\) is nonempty and proper. Put
\[
\Theta_S=\sum_{i\in S}\theta_i,\qquad
U_S=\bigotimes_{i\in S}U_{\theta_i}.
\]
Positivity of all angles and \(\sum_i\theta_i=\pi/2\) give \(0<\Theta_S<\pi/2\). The eigenvalues of \(U_S\) are
\[
\exp\!\left(i\sum_{i\in S}\varepsilon_i\theta_i\right),\qquad \varepsilon_i\in\{-1,1}.
\]
Hence every eigenvalue of the Hermitian part \(H_S=(U_S+U_S^\dagger)/2\) is
\[
\cos\!\left(\sum_{i\in S}\varepsilon_i\theta_i\right)>0,
\]
because the absolute value of the phase is at most \(\Theta_S<\pi/2\). Therefore \(H_S\) is positive definite. The necessary condition for perfect one-use discrimination of a computational-basis projective measurement from its unitary-rotated basis, proved in arXiv:2610.02032v1, would require a density operator \(\rho\) with \(\operatorname{Tr}(\rho U_S)=0\). Taking real parts would give \(\operatorname{Tr}(\rho H_S)=0\), impossible because \(H_S>0\). Thus the two local measurement possibilities on side \(S\) cannot be perfectly distinguished by any joint probe. The same argument applies to \(S^c\).

The finite-round LOCC argument from the same source now applies without symmetry assumptions. Whichever laboratory acts first, its local indistinguishability forces at least one branch that occurs under both global hypotheses and leaves nonorthogonal residual states. Conditioned on that branch, the other laboratory also has a common branch with nonorthogonal residual states. Fidelity is multiplicative on the resulting tensor-product residual states and monotone under subsequent quantum channels, so no finite continuation can make the two hypotheses orthogonal. Therefore perfect finite-round LOCC discrimination is impossible across \(S|S^c\). Since the bipartition was arbitrary, the pair is strongly nonlocal across every bipartition.

## Verification
The analytic proof has two independent components: an exact parity-amplitude identity controlled only by the total angle \(\Theta\), and a local obstruction controlled by every proper subset sum \(\Theta_S\). The attached verifier evaluates the parity amplitudes directly from the state coefficients for several heterogeneous angle tuples and checks the closed formula. It also enumerates all sign choices for every proper subset and confirms positivity of the Hermitian-part eigenvalues. These finite checks corroborate, but do not replace, the proof for arbitrary \(w\) and arbitrary admissible angles.

## Relationship to prior work
Manna and Saha, arXiv:2610.02032v1, prove strong nonlocality for the homogeneous choice \(\theta_1=\cdots=\theta_w=\pi/(2w)\). Their global proof obtains the amplitude \(2^{-(w-1)/2}\cos(w\theta-r\pi/2)\), and their local obstruction uses positivity of the Hermitian part of \(U_\theta^{\otimes m}\) when \(m\theta<\pi/2\). The present result identifies the two quantities actually controlling those arguments: the global total angle \(\sum_i\theta_i\) and the proper-subset totals \(\sum_{i\in S}\theta_i\). This removes the equal-angle constraint and yields a full heterogeneous family.

Earlier work on single-shot measurement discrimination derives general criteria and optimal probabilities for projective measurements, while multiple-shot von Neumann measurement discrimination studies finite-query global strategies. Those frameworks do not state the all-bipartition heterogeneous simplex theorem proved here.

## Limitations
The theorem is an exact statement on the positive simplex \(\sum_i\theta_i=\pi/2\). It does not assert robustness under perturbing the total angle, though the local positive-definiteness obstruction itself persists while every proper subset sum remains below \(\pi/2\). It also does not classify all heterogeneous angle tuples giving global perfect discrimination, nor all possible strongly nonlocal product-measurement pairs.

## References
1. S. Manna and D. Saha, “Nonlocality without entanglement for multipartite quantum measurements,” arXiv:2610.02032v1 (2026).
2. S. Manna, S. Suresh, M. S. Kachhawaha, and D. Saha, “Single-shot Distinguishability and Anti-distinguishability of Quantum Measurements,” arXiv:2410.10632v1 (2024).
3. Z. Puchała, Ł. Pawela, A. Krawiec, R. Kukulski, and M. Oszmaniec, “Multiple-shot and unambiguous discrimination of von Neumann measurements,” Quantum 5, 425 (2021), doi:10.22331/q-2021-04-06-425.
4. C. Datta, T. Biswas, D. Saha, and R. Augusiak, “Perfect discrimination of quantum measurements using entangled systems,” New Journal of Physics 23, 043021 (2021), doi:10.1088/1367-2630/abecaf.
