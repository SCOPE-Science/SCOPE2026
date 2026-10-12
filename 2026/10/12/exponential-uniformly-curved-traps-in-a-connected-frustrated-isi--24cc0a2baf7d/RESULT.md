# Exponential uniformly curved traps in a connected frustrated Ising VQE landscape
## Finding
Fix an integer \(m\ge1\) and put \(n=3m\). Consider the connected graph obtained by arranging \(m\) triangles in a chain. The \(j\)-th triangle has vertices \(a_j,b_j,c_j\) and three unit-strength antiferromagnetic bonds. Consecutive triangles are joined by a bridge from \(c_j\) to \(a_{j+1}\) of strength \(\varepsilon>0\). Every vertex has degree at most three.

Define the diagonal \(n\)-qubit Hamiltonian
\[
H_m=\sum_{j=1}^m
\left(Z_{a_j}Z_{b_j}+Z_{b_j}Z_{c_j}+Z_{c_j}Z_{a_j}
-h_1Z_{a_j}-h_2Z_{b_j}-h_3Z_{c_j}\right)
+\varepsilon\sum_{j=1}^{m-1}Z_{c_j}Z_{a_{j+1}}.
\]
This has the same product-rotation variational architecture as the diagonal Ising benchmark in Novak et al.: for
\[
|\psi(\theta)\rangle=\bigotimes_{i=1}^n R_y(\theta_i)|0\rangle,
\qquad
E_m(\theta)=\langle\psi(\theta)|H_m|\psi(\theta)\rangle,
\]
the energy is
\[
E_m(\theta)=\sum_{uv\in E(G_m)}J_{uv}\cos\theta_u\cos\theta_v
-\sum_{j=1}^m\left(h_1\cos\theta_{a_j}+h_2\cos\theta_{b_j}+h_3\cos\theta_{c_j}\right).
\]
The angles are understood modulo \(2\pi\).

**Theorem.** Suppose
\[
0<\varepsilon<h_1<h_2<h_3<2-\varepsilon,
\qquad h_2-h_1>2\varepsilon.
\]
Then \(E_m\) has exactly
\[
\boxed{3^m}
\]
strict local minima. These occur exactly at the \(\{0,\pi\}^n\) angle vectors whose computational-basis spin configuration contains exactly one minus spin in each triangle. All are nondegenerate. Every eigenvalue of each local-minimum Hessian belongs to the interval
\[
\boxed{
[c_-,c_+],\quad
c_-=\min\{h_1-\varepsilon,\,2-h_3-\varepsilon\}>0,
\quad
c_+=\max\{h_3+\varepsilon,\,2-h_1+\varepsilon\}.
}
\]
The unique global minimizer has the minus spin at \(a_j\) in every triangle. Every one of the other \(3^m-1\) strict local minima has the finite, size-independent energy gap
\[
\boxed{E_m(\theta)-E_{m,\min}\ge2(h_2-h_1-2\varepsilon)>0.}
\]
In particular the ground state is exactly reachable by the product-rotation ansatz, even though the number of strict nonglobal minima grows exponentially in the number of qubits.

For independent uniformly distributed angles on \([0,2\pi)\), the expected normalized squared gradient is exactly
\[
\boxed{
\frac{\mathbb E\|\nabla E_m(\theta)\|_2^2}{3m}
=\frac12+\frac{h_1^2+h_2^2+h_3^2}{6}
+\frac{m-1}{6m}\varepsilon^2.}
\]
Thus each coordinate gradient has variance at least \(1/2\), uniformly in \(m\): the proliferating strict traps do not require a vanishing-gradient or barren-plateau mechanism.

The parameter region is nonempty; one explicit rational choice is
\[
\varepsilon=\frac1{100},\qquad
(h_1,h_2,h_3)=\left(\frac1{10},\frac15,\frac3{10}\right).
\]
For these parameters the Hessians at every strict minimum have eigenvalues between \(9/100\) and \(191/100\), and there are exactly \(3^m-1\) strict spurious traps.

## Assumptions and scope
The construction uses diagonal Ising Hamiltonians with real, nonuniform edge strengths, antiferromagnetic triangles, weak inter-triangle bridges and positive longitudinal fields. It uses only single-qubit \(R_y\) rotations from \(|0\rangle^{\otimes n}\), with no entangling gates. The graph is connected and has maximum degree three; it need not be exactly the ring-plus-matching graph or the unit-magnitude disorder ensemble of the source's finite experiments. The claim classifies **strict** local minima in continuous parameter space, not arbitrary nonstrict stationary points or the performance of a particular optimization algorithm.

## Proof
Write \(z_i=\cos\theta_i\) and, for fixed values of the other coordinates, put
\[
\ell_i(z)=\sum_{k\sim i}J_{ik}z_k-h_i.
\]
Then
\[
\frac{\partial E_m}{\partial\theta_i}=-\sin\theta_i\,\ell_i(z).
\]
If a stationary point has \(\sin\theta_i\ne0\), stationarity forces \(\ell_i(z)=0\). Since the energy is affine in \(z_i=\cos\theta_i\) for fixed other coordinates, it is then independent of \(\theta_i\). Such a point cannot be a **strict** local minimum. Thus every strict local minimum lies at a spin vertex, with \(z_i=s_i\in\{+1,-1\}\).

At a spin vertex all sine factors vanish, so the Hessian is diagonal with entries
\[
\frac{\partial^2 E_m}{\partial\theta_i^2}
=-s_i\left(\sum_{k\sim i}J_{ik}s_k-h_i\right).
\]
Each triangle has two unit-strength neighbors per vertex and at most one weak bridge per vertex. In a triangle with precisely one minus spin, the minus vertex has two plus neighbors and Hessian diagonal entry at least \(2-h_3-\varepsilon\), while each plus vertex has one plus and one minus neighbor and Hessian entry at least \(h_1-\varepsilon\). Every such configuration is therefore a strict local minimum, and all its Hessian eigenvalues lie in \([c_-,c_+]\).

Conversely, a triangle with all spins plus has a site with Hessian entry at most \(-(2-h_3-\varepsilon)<0\); a triangle with all spins minus likewise has a negative Hessian entry. A triangle with exactly one plus and two minus spins has a minus-spin site with one plus and one minus neighbor, so its Hessian entry is at most \(-h_1+\varepsilon<0\). Thus no other spin vertex is a local minimum. There are three choices of the unique minus spin in each of the \(m\) triangles, proving the **exact** count \(3^m\).

Within each triangle, every allowed minimum has the same bond energy \(-1\). The longitudinal-field contribution with the unique minus spin at vertex \(k\in\{a,b,c\}\) is
\[
-h_1-h_2-h_3+2h_k.
\]
Replacing a minus spin at either \(b_j\) or \(c_j\) by a minus spin at \(a_j\) lowers this on-site contribution by at least \(2(h_2-h_1)\). Such a replacement changes at most two bridge products, each by at most \(2\varepsilon\). Hence its *total* energy reduction is at least
\[
2(h_2-h_1)-4\varepsilon=2(h_2-h_1-2\varepsilon)>0.
\]
Iterating this operation from any nonglobal strict local minimum reaches the unique preferred spin configuration. Every global minimizer must be one-spin stable, hence belongs to this classified set; therefore the preferred configuration is the unique global minimum among all spin vertices. Finally, since the energy is multi-affine in \(z\in[-1,1]^n\), any interior point is a convex combination, in its energy, of the vertices. With a unique minimal vertex, it cannot be another global minimizer. The energy-gap assertion follows from the last operation in the iteration.

For the gradient moment, independent uniform angles satisfy
\[
\mathbb E\sin^2\theta_i=\frac12,\qquad
\mathbb E\cos\theta_i=0,\qquad
\mathbb E\cos^2\theta_i=\frac12.
\]
The sine at vertex \(i\) is independent of every neighboring cosine. Therefore
\[
\mathbb E\left(\frac{\partial E_m}{\partial\theta_i}\right)^2
=\frac12\left(h_i^2+\frac12\sum_{k\sim i}J_{ik}^2\right).
\]
There are \(3m\) unit-strength triangle edges and \(m-1\) bridge edges of strength \(\varepsilon\). Summing the last identity over all \(3m\) vertices and dividing by \(3m\) gives precisely the asserted normalized-gradient formula. By symmetry each coordinate derivative has mean zero, so this second moment is its variance.

## Verification
The analytic proof establishes the theorem for all integers \(m\ge1\) and all real parameters in the displayed open region. No extrapolation from finite enumeration is used. The bundled reproducibility script performs exact rational enumeration of all spin vertices for the explicit rational instance up to \(m=4\), verifies the strict-minimum count and Hessian bounds, checks uniqueness of the ground configuration and its energy gap, and independently recomputes the exact gradient-moment formula. It prints `VERIFY_OK` on success. The finite tests do not certify the universal quantifiers; those follow from the local Hessian sign argument and the multilinear energy identity.

## Relationship to prior work
Novák, Zelinka, Das and Beseda treat the diagonal Ising \(R_y\)-product ansatz as a benchmark with zero variational gap but many optimization basins. Their full article enumerates one-spin-flip-stable configurations for selected instances through \(16\) qubits and reports \(28\), \(72\) and \(130\) such configurations at three sizes. Their conclusion emphasizes separating exact reachability, multimodal optimization geometry, and gradient size. The theorem here supplies an exact all-system-size connected family that separates these features quantitatively, including a count, uniform positive Hessian curvature, a uniform nonglobal energy gap, and a nonvanishing gradient-variance formula. It is not a claim about the specific disorder realization in their tables.

Wacław and Burda study the number of one-spin-stable states of classical Ising spin glasses on arbitrary graphs with random Gaussian couplings and derive perturbative statistical estimates for regular random graphs and lattices. This prior literature establishes that exponential metastability is familiar in spin glasses; **exponential growth alone is not claimed as new**. Their analyzed ensemble does not contain the present deterministic open family of pinned frustrated-triangle chains, nor does it give its exact \(3^m\) count together with the continuous ansatz Hessian and gradient-moment statements.

Faílde et al. study optimizer escape from local minima numerically, including a one-dimensional Ising model, but do not give the all-size degree-three parametric classification above. No claim of a new general spin-glass counting principle is made; the contribution is the exact, robust simultaneous VQE-landscape calibration.

## Limitations
The Hamiltonian is diagonal and admits an elementary classical description. The proof says nothing about hardness of escaping these minima for arbitrary local algorithms, or the distribution of their attraction-basin volumes. A nonvanishing *mean squared* gradient does not rule out gradients vanishing at individual stationary points; indeed they vanish at every strict minimum. The graph has weak inter-triangle bridges, not equal-magnitude Ising bonds. The result does not extend unchanged to noncommuting spin Hamiltonians or entangling variational ansätze.

## References
1. V. Novák, I. Zelinka, S. Das and M. Beseda, *Optimization Landscape Geometry in VQE for Frustrated Quantum Spin Models*, arXiv:2609.00235v1 (first public 2026-08-31), full-text version arXiv:2609.00235v2 (2026-09-11).
2. B. Wacław and Z. Burda, *Counting metastable states of Ising spin glasses on arbitrary graphs*, Physical Review E 77, 041114 (2008), arXiv:0801.1224, DOI:10.1103/PhysRevE.77.041114.
3. D. Faílde, J. D. Viqueira, M. Mussa Juane and A. Gómez, *Using Differential Evolution to avoid local minima in Variational Quantum Algorithms*, Scientific Reports 13, 16230 (2023), DOI:10.1038/s41598-023-43404-3.
