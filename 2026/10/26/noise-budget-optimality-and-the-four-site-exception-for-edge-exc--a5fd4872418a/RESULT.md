# Noise-budget optimality and the four-site exception for edge-exchange Lindbladians

## Finding
Fix an integer \(N\ge3\), a noise budget \(B>0\), and nonnegative real edge rates \(w_{ij}\) on all unordered pairs of \(N\) sites, with \(\sum_{i<j}w_{ij}=B\). Let \(V_{ij}=|i\rangle\langle j|+|j\rangle\langle i|\), and define the purely dissipative quantum generator
\[
\mathcal L_w(X)=\sum_{i<j}w_{ij}\left(V_{ij}XV_{ij}-\tfrac12\{V_{ij}^2,X\}\right).
\]
Let \(d_i=\sum_{j\ne i}w_{ij}\), and let \(L_w\) be the weighted graph Laplacian. Its exact decay-rate spectrum on matrix operators consists of the \(N\) eigenvalues of \(L_w\), the \(\binom N2\) numbers
\[
r_{ij}=\frac{d_i+d_j}{2}-w_{ij},
\]
and the \(\binom N2\) numbers
\[
s_{ij}=\frac{d_i+d_j}{2}+w_{ij}.
\]
The sharp Hilbert--Schmidt relaxation rate toward the maximally mixed state, allowing zero rates for disconnected networks, is
\[
\Gamma(w)=\min\left\{\lambda_2(L_w),\min_{i<j}r_{ij}\right\}.
\]
At fixed total rate \(B\), the exact optimal relaxation rate is
\[
\boxed{\max_{\sum w=B}\Gamma(w)=\frac{(N-2)B}{\binom N2}.}
\]
For \(N=3\) and every \(N\ge5\), uniform rates \(w_{ij}=B/\binom N2\) are the **unique** optimal choice. At \(N=4\), the optimizer is nonunique: all rates
\[
w_{12}=\frac B6+t,\quad w_{34}=\frac B6-t,\quad
w_{13}=w_{14}=w_{23}=w_{24}=\frac B6,
\qquad -\frac B6\le t\le\frac B6,
\]
are optimal. In particular the entire displayed interval includes strictly positive, nonuniform noise allocations.

## Assumptions and scope
The Hilbert space is the single-excitation space \(\mathbb C^N\). All edge noises are independent at the effective-generator level (the covariance is diagonal in the edge basis). The coherent mean Hamiltonian is absent or compensated exactly; no assertion is made for an uncompensated Hamiltonian or for the exact finite-switching random-unitary channel. The rates are arbitrary nonnegative numbers and may vanish. The budget \(B\) is their sum, not a bound on a spectral norm or on a switching frequency. The spectral gap \(\Gamma\) is defined by the smallest decay rate **on traceless Hermitian matrices**, including zero when more than one stationary state exists; it is not the smallest *strictly positive* eigenvalue in the presence of extra conserved observables.

## Proof
Write \(E_{ij}=|i\rangle\langle j|\). Since \(V_{ij}^2=E_{ii}+E_{jj}\), the diagonal matrix units span an invariant subspace, where direct substitution gives
\[
\mathcal L_w(E_{ii})=\sum_{j\ne i}w_{ij}(E_{jj}-E_{ii}).
\]
Thus its positive decay matrix is exactly \(L_w\). For each \(i<j\), the two Hermitian off-diagonal operators \(A_{ij}=E_{ij}+E_{ji}\) and \(B_{ij}=i(E_{ij}-E_{ji})\) are eigenoperators. Edges other than \(\{i,j\}\) touching either endpoint contribute \(-(d_i+d_j-2w_{ij})/2\) times either operator. The edge \(\{i,j\}\) itself exchanges \(E_{ij}\) with \(E_{ji}\), giving zero on \(A_{ij}\) and \(-2w_{ij}\) on \(B_{ij}\). Consequently
\[
\mathcal L_w(A_{ij})=-r_{ij}A_{ij},\qquad
\mathcal L_w(B_{ij})=-s_{ij}B_{ij}.
\]
These diagonal and off-diagonal sectors have total dimension \(N+2\binom N2=N^2\) and are orthogonal for the Hilbert--Schmidt inner product. Because \(s_{ij}\ge r_{ij}\ge0\), deleting the identity eigenoperator gives the stated exact gap formula.

Summing the symmetric-coherence rates over all pairs yields
\[
\sum_{i<j}r_{ij}=\frac{N-1}{2}\sum_i d_i-\sum_{i<j}w_{ij}=(N-2)B.
\]
The minimum cannot exceed their mean: \(\Gamma\le\min r_{ij}\le(N-2)B/\binom N2\). Uniform rates \(a=B/\binom N2\) give \(d_i=(N-1)a\), hence \(r_{ij}=(N-2)a\) and \(\lambda_2(L_w)=Na\); they attain the bound.

Suppose equality holds. Since the sum of the \(r_{ij}\) is fixed and every \(r_{ij}\) must be at least their mean, equality forces \(r_{ij}=c=(N-2)B/\binom N2\) for **every** pair. Hence
\[
w_{ij}=\frac{d_i+d_j}{2}-c.
\]
Summing over \(j\ne i\), and using \(\sum_i d_i=2B\), gives
\[
(N-1)c=\frac{N-4}{2}d_i+B.
\]
When \(N\ne4\), this enforces \(d_i=2B/N\) for each vertex and therefore \(w_{ij}=B/\binom N2\) for all pairs. This proves the uniqueness statement without presupposing symmetry of an optimizer.

For \(N=4\) put \(a=B/6\). The displayed nonuniform weights have vertex degrees \(d_1=d_2=3a+t\) and \(d_3=d_4=3a-t\), so every \(r_{ij}=2a\). The diagonal Laplacian has eigenvalues
\[
0,\quad4a-2t,\quad4a+2t,\quad4a.
\]
For \(|t|\le a\), the smallest positive Laplacian eigenvalue is at least \(2a\), proving \(\Gamma=2a=B/3\). Thus the nonuniqueness is real, even with all rates strictly positive when \(|t|<a\).

Finally the orthogonal spectral decomposition gives \(\|e^{u\mathcal L_w}(\rho-I/N)\|_2\le e^{-u\Gamma(w)}\|\rho-I/N\|_2\) for \(u\ge0\). For each slow traceless Hermitian eigenoperator \(X\), the matrices \(I/N+\varepsilon X\) are density matrices for sufficiently small real \(\varepsilon\). They attain the contraction exponent, so it cannot be improved.

## Verification
Run `python3 artifacts/verify.py` with NumPy. It constructs the matrix superoperator independently using Kronecker products, compares its complete spectrum to the formula for every unweighted graph on \(N=3,4\), checks randomly weighted networks on \(N=3,4,5,6\), and tests the four-site continuum. The packaged run reported `CHECKS_PASSED 157`. These are finite reproducibility checks; the all-\(N\) claims are established by the preceding algebra rather than extrapolated from computation.

## Relationship to prior work
Nourmandipour and Mancini (2026) derive the covariance-based effective Lindblad generator for fluctuating quantum-network topology, including Hermitian edge-exchange operators, and analyze special collectively correlated ensembles and their decay modes. The generator's existence, its physical derivation, and their reported dissipative-gap phenomena are prior results. Their independent-edge limit does not state the complete arbitrary-rate spectrum, the fixed-budget bound with **all** equality cases for \(N\ne4\), or the nonuniform four-site optimal family proved here. Farooq and Mancini (2014) study random XY-network information spreading in a different switching setting; they do not establish this rate-allocation theorem. The result concerns optimization within a fixed, purely dissipative diagonal-covariance model, not a general optimality theorem over correlated noise or coherent drives.

## Limitations
The rates are coefficients of an effective Markovian dissipator, not independently achievable Bernoulli-edge variances without parameter constraints; realizability under a particular hardware model requires separate checking. A coherent mean Hamiltonian can alter the eigenoperators and gaps. The source's general covariance construction is prior knowledge. An uninspected general semigroup symmetrization or spectral-optimization theorem could subsume some or all of the derived inequality; priority is not independently certified. The result is exact in finite dimension for every \(N\ge3\), but it makes no bound on finite-switching discretization errors.

## References
1. Alireza Nourmandipour and Stefano Mancini, *Emergent Dissipation from Fluctuating Quantum-Network Topology*, arXiv:2610.03194v1, first publicly available 2026-10-02, https://arxiv.org/html/2610.03194v1.
2. Umer Farooq and Stefano Mancini, *Information Dissipation in Random Quantum Networks*, arXiv:1404.0508, first publicly available 2014-04-02, https://arxiv.org/abs/1404.0508.
