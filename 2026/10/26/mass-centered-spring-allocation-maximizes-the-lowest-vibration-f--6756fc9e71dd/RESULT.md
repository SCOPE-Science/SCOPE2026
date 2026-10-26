# Mass-centered spring allocation maximizes the lowest vibration frequency, with a logarithmic static-compliance cost

## Finding
For every integer \(n\ge 2\), all positive point masses \(m_1,\ldots,m_n\), and every prescribed total spring stiffness \(K>0\), consider a freely translating linear chain connected by \(n-1\) massless Hookean springs. Among **all** choices \(k_i>0\) with \(\sum_{i=1}^{n-1}k_i=K\), its smallest nonzero squared vibration frequency has the unique global maximizer
\[
 k_i^*=\frac{K}{V}\sum_{j=1}^{i}m_j(\mu-j),\quad
 \mu=\frac{\sum_{j=1}^{n}j m_j}{\sum_{j=1}^{n}m_j},\quad
 V=\sum_{j=1}^{n}m_j(j-\mu)^2.
\]
The sharp maximum is \(\omega_{\min,*}^2=K/V\). At the optimizer, the slowest non-translation eigenmode is exactly affine in the mass index: \(u_j=j-\mu\), independently of the mass heterogeneity. In particular, optimal springs grow towards the mass-center index and decrease after it, with a possible two-edge plateau when the mass center is an integer.

The dynamic optimum has an exact static penalty. For equal point masses \(m_j=m>0\), one obtains \(k_i^*=6K i(n-i)/[n(n^2-1)]\) and \(\omega_{\min,*}^2=12K/[mn(n^2-1)]\). If equal and opposite static forces act on the two free endpoints, their relative-displacement compliance \(\mathcal R=\sum_{i=1}^{n-1}1/k_i\) at the dynamic optimum is
\[
\mathcal R_* =\frac{(n^2-1)H_{n-1}}{3K},\qquad H_{n-1}=\sum_{j=1}^{n-1}\frac1j.
\]
Relative to the smallest compliance available at the same stiffness budget, \(\mathcal R_{\min}=(n-1)^2/K\), the penalty is exactly
\[
 \frac{\mathcal R_*}{\mathcal R_{\min}}=\frac{n+1}{3(n-1)}H_{n-1}\sim\frac13\log n.
\]
The logarithm is an asymptotic consequence of the explicit optimizing stiffnesses, not a claim of a novel general resistance principle.

## Assumptions and scope
The displacement \(u_i(t)\in\mathbb R\) of each positive mass obeys \(M\ddot u+Lu=0\), where \(M=\operatorname{diag}(m_1,\ldots,m_n)\) and \(L\) is the symmetric path Laplacian with \(L_{i,i+1}=L_{i+1,i}=-k_i\), \(L_{ii}=k_{i-1}+k_i\) and \(k_0=k_n=0\). The chain has free ends, no foundation stiffness, no external forcing or damping, and only nearest-neighbor linear springs. The translation eigenfrequency \(0\) is excluded. Frequencies are the roots of \(Lv=\omega^2 Mv\). The index positions \(i\) are dimensionless labels, not physical intermass distances. Positive mass and stiffness hypotheses ensure \(V>0\) and connectedness.

## Proof
Let \(w_j=j-\mu\). By construction, \(\sum_j m_jw_j=0\) and \(w_{j+1}-w_j=1\). The generalized Rayleigh minimum on the mass-orthogonal complement of constants therefore gives, for every admissible allocation,
\[
\omega_{\min}^2\leq\frac{\sum_{i=1}^{n-1}k_i(w_{i+1}-w_i)^2}{\sum_{j=1}^nm_jw_j^2}=\frac K V.
\]
Set \(C_i=\sum_{j=1}^i m_j(\mu-j)\) for \(1\le i<n\). Writing \(M_0=\sum_jm_j\), the identity
\[
 C_i=\frac1{M_0}\sum_{j\le i<\ell}m_jm_\ell(\ell-j)>0
\]
holds for every interior bond. Moreover, the weighted-variance identity yields \(\sum_{i=1}^{n-1}C_i=V\). Thus \(k_i^*=(K/V)C_i\) is strictly positive and exhausts the budget.

With \(\lambda=K/V\), the equations at the first, interior and last masses respectively are
\[
 (Lw)_1=-k_1^*=\lambda m_1(1-\mu),\quad
 (Lw)_i=k_{i-1}^*-k_i^*=\lambda m_i(i-\mu),\quad
 (Lw)_n=k_{n-1}^*=\lambda m_n(n-\mu).
\]
Hence \(Lw=\lambda Mw\). The matrix \(M^{-1/2}LM^{-1/2}\) is an irreducible symmetric Jacobi matrix (negative nearest-neighbor off-diagonal entries). Sturm's oscillation theorem says its eigenvector with exactly one sign crossing is the second eigenvector; the entries of \(w\) grow strictly, are mass-centered, and cross zero once, including the possibility of one zero entry. Consequently \(\lambda\) is the first positive eigenvalue and attains the universal Rayleigh bound.

Equality in the initial Rayleigh bound for any other design forces \(w\) to be a generalized eigenvector at eigenvalue \(K/V\). Its first-coordinate eigen-equation fixes \(k_1=\lambda C_1\); successive coordinates fix \(k_i=\lambda C_i\), proving uniqueness. Also \(k_i^*-k_{i-1}^*=\lambda m_i(\mu-i)\) for \(2\le i<n\), establishing the mass-center peak law.

For equal masses, \(\mu=(n+1)/2\), \(V=mn(n^2-1)/12\), and \(C_i=mi(n-i)/2\), giving the displayed optimizer. Under endpoint static forces \(+F,-F\), every spring carries force magnitude \(F\), so the relative displacement is \(F\sum_i1/k_i\). The partial-fraction identity \(1/[i(n-i)]=(1/i+1/(n-i))/n\) proves the stated harmonic-number compliance. Finally \(\sum_i1/k_i\ge(n-1)^2/K\) by Cauchy–Schwarz, with equality exactly for uniform springs; and \(H_{n-1}\sim\log n\).

## Verification
A standalone Python checker, `check.py`, independently constructs the generalized vibration eigenproblem for mass vectors drawn across more than six orders of magnitude, verifies the stated maximizing eigenvalue and affine eigenvector, and compares against random budget-preserving competitors. It also tests the equal-mass harmonic-number compliance identity and its optimal-stiffness formula. The checker passed 14,854 assertion groups in the reported execution. Finite numerical tests corroborate but do not prove the statements for arbitrary positive masses or arbitrary size; the preceding variational and Sturm argument supplies that proof. Run from this package with `python3 check.py` (requires NumPy and SciPy).

## Relationship to prior work
Boyd's 2006 survey developed convex spectral optimization of graph Laplacians and interprets a fixed edge-weight budget through algebraic connectivity and Markov-chain convergence. Wan et al. (2008) investigated optimal weighted edges of ordinary path and tree graph Laplacians, including equal-magnitude differences of the ordinary Fiedler vector across active edges. These are essential antecedents; the equal-mass optimization and its parabolic spring profile are **not** claimed to be new. The present mass-dependent formula addresses instead the generalized physical eigenproblem \(Lv=\omega^2Mv\) with arbitrary, **unequal** inertias, yielding the exact mass-center selection and unique stiffnesses for all chain sizes. It also quantifies the static-compliance penalty of the dynamically tuned equal-mass chain. The original source's structural reasoning is closely related to the proof, and potential coverage in differently phrased weighted birth–death or structural optimization literature remains a priority risk. Liu et al. (2015) investigated mass-arrangement effects in a ring, a distinct fixed-connectivity design problem.

## Limitations
No claim is made for nonlinear, damped, pinned, periodic, branching, or continuously distributed elastic systems, or for fixed manufacturing bounds on individual springs. In more general graphs, an affine-in-index test mode need not be a first excited mode and the stated formula does not apply. Static compliance is defined only for equal and opposite endpoint forces (the rigid translation is irrelevant). The unweighted graph method is prior art, and the equal-mass harmonic-number identity alone would not support novelty; this is a limitation on the scope of the proposed contribution.

## References
1. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, Proceedings of the ICM, vol. 3, 2006, pp. 1311–1319. https://stanford.edu/~boyd/papers/pdf/cvx_opt_graph_lapl_eigs.pdf
2. Y. Wan, S. Roy, X. Wang, A. Saberi, T. Yang, M. Xue, B. Malek, *On the Structure of Graph Edge Designs that Optimize the Algebraic Connectivity*, Proceedings of the IEEE CDC, 2008, pp. 805–810. DOI: 10.1109/CDC.2008.4738734.
3. S. Liu et al., *Optimal Configuration for Vibration Frequencies in a Ring of Harmonic Oscillators: The Nonidentical Mass Effect*, Frontiers of Physics 10 (2015), pp. 327–338. DOI: 10.1007/s11467-015-0462-4.
