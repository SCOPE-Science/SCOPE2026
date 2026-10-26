# Exact trajectory-purity memory in Haar-random coined walks on Abelian Cayley graphs

## Finding

A Haar-random coin can erase the *ensemble-averaged* coherence between two Fourier modes while the *mean purity of the individual reduced vertex states* retains a dimension-controlled excess. The distinction is exact at every time and for every number of vertices.

Let the setting and notation below hold. Define the normalized relative-mode trace and a real decay parameter by
\[
\lambda=\frac{1}{d}\sum_{j=1}^{d}\overline{b_j}a_j,\qquad
\gamma=\frac{d^2|\lambda|^2-1}{d^2-1}.
\]
For the random modal overlap \(Z_t\) and the resulting single-trajectory vertex density operator \(\rho_{V,t}\), for every integer \(t\geq0\),
\[
\boxed{\mathbb E Z_t=\lambda^t,\qquad
\mathbb E|Z_t|^2=\frac1d+\left(1-\frac1d\right)\gamma^t},
\]
\[
\boxed{\mathbb E\,\operatorname{Tr}(\rho_{V,t}^2)=
\frac{1+1/d}{2}+\frac{1-1/d}{2}\gamma^t},\qquad
\operatorname{Tr}\big[(\mathbb E\rho_{V,t})^2\big]
=\frac{1+|\lambda|^{2t}}2.
\]
If \(|\lambda|<1\), these last two purities tend to \((1+1/d)/2\) and \(1/2\), respectively, and the noncommutation-of-averaging gap tends to the **strictly positive universal limit \(1/(2d)\)**. The dimension \(d\) is the number of coin directions, not the number of vertices.

## Assumptions and scope

Let \(G\) be a finite Abelian group of order \(N\geq2\), and let \(S=\{s_1,\ldots,s_d\}\) be a symmetric generating set of distinct nonidentity elements, where \(d\geq2\). For each \(j\), let \(W_j\) be translation by \(s_j\) on the vertex Hilbert space \(\mathbb C^G\). (The proof actually needs only commuting unitary vertex shifts and two orthogonal joint eigenvectors.) Choose two distinct normalized vertex characters \(f,g\), with
\[
W_jf=a_j f,\qquad W_jg=b_jg,\qquad |a_j|=|b_j|=1.
\]
On coin \(\mathbb C^d\) and vertex \(\mathbb C^G\), set
\[
\Lambda_S=\sum_{j=1}^{d}|j\rangle\langle j|\otimes W_j,
\qquad U_t=\Lambda_S(V_t\otimes I),
\]
where \(V_1,V_2,\ldots\) are independent Haar-distributed random unitaries in \(U(d)\), sampled once per step and applied *identically* to both Fourier sectors. The initial state is the normalized product
\[
|\Psi_0\rangle=|\eta\rangle\otimes \frac{|f\rangle+|g\rangle}{\sqrt2},
\qquad \|\eta\|=1.
\]
At time \(t\), the pure state has the form
\[
|\Psi_t\rangle=\frac{1}{\sqrt2}(|\psi_t\rangle\otimes|f\rangle
+|\phi_t\rangle\otimes|g\rangle),\qquad
\|\psi_t\|=\|\phi_t\|=1.
\]
Define \(Z_t=\langle\phi_t,\psi_t\rangle\) and \(\rho_{V,t}=\operatorname{Tr}_{\mathrm{coin}}|\Psi_t\rangle\langle\Psi_t|\). All averages are over coin draws; they are not averages over measurements or initial states.

## Proof

**1. Invariant two-mode subspace.** The characters diagonalize each translation. Let \(D_f=\operatorname{diag}(a_1,\ldots,a_d)\), \(D_g=\operatorname{diag}(b_1,\ldots,b_d)\). The two coin vectors obey
\[
\psi_t=D_f V_t\psi_{t-1},\qquad
\phi_t=D_gV_t\phi_{t-1}.
\]
Writing \(A=D_g^\dagger D_f=\operatorname{diag}(\overline{b_j}a_j)\), we have \(AA^\dagger=I\), \(\operatorname{tr}A=d\lambda\), and
\[
Z_t=\langle\phi_{t-1},V_t^\dagger A V_t\psi_{t-1}\rangle,\qquad Z_0=1.
\]

**2. Exact conditional Haar identities.** For arbitrary fixed unit coin vectors \(x,y\), let \(z=\langle y,x\rangle\). The Haar first-moment identity is \(\mathbb E_V(V^\dagger A V)=\lambda I\). To obtain the second moment without an independence assumption between modal vectors, write \(A=\lambda I+B\) with \(\operatorname{tr}B=0\) and \(\|B\|_{\mathrm{HS}}^2=d(1-|\lambda|^2)\). Haar invariance on the traceless-matrix subspace gives the exact covariance
\[
\mathbb E_V\!\left[(V^\dagger B V)_{ij}
\overline{(V^\dagger B V)_{k\ell}}\right]
=\frac{\|B\|_{\mathrm{HS}}^2}{d^2-1}
\left(\delta_{ik}\delta_{j\ell}-\frac{\delta_{ij}\delta_{k\ell}}{d}\right).
\]
For completeness, conjugation preserves the Hilbert–Schmidt inner product, is irreducible on the complex traceless matrices, and averaging the rank-one tensor under this action gives the orthogonal projector onto that subspace divided by its dimension \(d^2-1\); this proves the displayed formula, including its normalization. Contracting against \(\overline y_i x_j y_k\overline x_\ell\), and noting that the scalar–traceless cross terms have zero mean, yields
\[
\mathbb E_V\langle y,V^\dagger A Vx\rangle=\lambda z,
\]
\[
\begin{aligned}
\mathbb E_V|\langle y,V^\dagger A Vx\rangle|^2
&=|\lambda|^2|z|^2+
\frac{d(1-|\lambda|^2)}{d^2-1}\left(1-\frac{|z|^2}{d}\right)\\
&=\frac{1-\gamma}{d}+\gamma|z|^2.
\end{aligned}
\]
These are conditional identities valid even when \(x,y\) depend on the *previous* random coins; only \(V_t\) is fresh and independent.

**3. Recurrence and exact solution.** Apply the conditional identities with \(x=\psi_{t-1}\) and \(y=\phi_{t-1}\):
\[
\mathbb E(Z_t\mid\mathcal F_{t-1})=\lambda Z_{t-1},\qquad
\mathbb E(|Z_t|^2\mid\mathcal F_{t-1})
=\frac{1-\gamma}{d}+\gamma|Z_{t-1}|^2.
\]
The first recurrence and \(Z_0=1\) give \(\mathbb E Z_t=\lambda^t\). Writing \(F_t=\mathbb E|Z_t|^2\), the second recurrence becomes \(F_t-1/d=\gamma(F_{t-1}-1/d)\) with \(F_0=1\). Thus \(F_t=1/d+(1-1/d)\gamma^t\) for every integer \(t\ge0\), including negative \(\gamma\) and all parameter endpoints.

**4. Reduced-state purity and boundary cases.** In the orthonormal basis \((f,g)\), the reduced vertex matrix is
\[
\rho_{V,t}=\frac12\begin{pmatrix}1&Z_t\\\overline{Z_t}&1\end{pmatrix}.
\]
Therefore \(\operatorname{Tr}\rho_{V,t}^2=(1+|Z_t|^2)/2\). The averaged matrix replaces \(Z_t\) by \(\lambda^t\), proving both purity formulas and their difference. Since \(0\le|\lambda|\le1\),
\[
-\frac1{d^2-1}\le\gamma\le1.
\]
If \(|\lambda|<1\), then \(|\gamma|<1\) because \(d\ge2\), yielding the asserted limits. If \(|\lambda|=1\), all diagonal entries of \(A\) are the same phase, so \(\gamma=1\), \(|Z_t|=1\), and both purities are exactly one. No asymptotic gap is claimed in that case.

**5. Concrete cycle.** On the undirected cycle \(C_N\) with \(N\ge3\), \(d=2\), directions \(+1,-1\), and Fourier labels \(k\ne k'\), let \(\theta=2\pi(k-k')/N\). Then \(\lambda=\cos\theta\),
\[
\gamma=\frac{1+2\cos(2\theta)}3,\qquad
\mathbb E\operatorname{Tr}\rho_{V,t}^2
=\frac34+\frac14\left(\frac{1+2\cos(2\theta)}3\right)^t.
\]
Whenever \(|\cos\theta|<1\), the trajectory-averaged purity tends to \(3/4\), whereas the purity of the averaged reduced state tends to \(1/2\). In the exceptional case \(|\cos\theta|=1\), the two sectors have identical relative coin phases and remain coherent; the general boundary formula applies.

## Verification

The proof is a finite-dimensional Haar-integration identity and a scalar recurrence; no numerical input is used for any universal statement. The standalone `verify.py` implements independent fresh Haar draws by complex Gaussian QR factorization. It checks the predicted complex first moment and real second moment against sample averages for coin dimensions two through four, for multiple step counts and both signs of the decay parameter. Execution: `python verify.py` with Python 3 and NumPy. Checks are stochastic sanity tests only: a finite sample does not certify the universal formulas. All limits are proved by \(|\gamma|<1\) and \(|\lambda|<1\), not by experiments.

## Relationship to prior work

Quillen's 2026 Haar-random-coin walk constructs this controlled-shift model on regular graphs and computes the **averaged linear quantum channel**, including its Fourier-sector dephasing eigenvalues for Abelian Cayley examples; it identifies fluctuations beyond such first moments as difficult. The present calculation instead handles a nonlinear single-realization observable, the two-mode reduced-state purity, and proves an exact persistent difference between averaging before and after that observable. For this probe, the first-moment multiplier \(\lambda\) agrees with the known Fourier dephasing mechanism; the second-moment multiplier \(\gamma\), its exact relaxation and the limiting purity gap are additional statements.

Earlier works on disordered quantum walks quantify coin–position entanglement or decoherence using different coin ensembles and initial conditions. In particular, Yao–Wald distinguish realization-wise from ensemble-wise entanglement conceptually, Vieira–Amorim–Rigolin analyze random dynamical coin disorder, and Ahlbrecht–Vogts–Werner–Werner establish position-distribution limits for Markov-selected finite sets of coins. Neither such general distinction nor standard Haar two-copy integration alone establishes the walk-specific exact two-mode time law and its nonzero limit. The available comparisons are not a guarantee of priority.

## Limitations

This theorem concerns equal-weight superpositions of exactly two orthogonal common eigenmodes, an initially identical pure coin vector in both sectors, fresh independent *global* Haar coins each step, and commuting vertex shifts. It does not give the purity for arbitrary multi-mode or localized vertex inputs, nor an entire output distribution or an almost-sure purity limit. The limiting nonzero difference concerns expectation of per-trajectory purity versus purity of the ensemble-averaged state, not persistence of the ensemble-averaged off-diagonal coherence. The group size \(N\) enters only through mode eigenphases; mixing at an individual vertex is not addressed. The originality conclusion rests on the literature inspected and permits unlocated equivalences.

## References

1. A. C. Quillen, “Quantum random walks on \(d\)-regular graphs with Haar-random coin operators,” arXiv:2607.04584v1 (first public 2026-07-06); Phys. Rev. A 114, 042410 (2026), DOI: 10.1103/rmmp-xdqy. https://arxiv.org/abs/2607.04584
2. R. Vieira, E. P. M. Amorim, and G. Rigolin, “Entangling Power of Disordered Quantum Walks,” arXiv:1402.5092 (2014). https://arxiv.org/abs/1402.5092
3. L. H. Yao and S. Wald, “Coined quantum walks on the line: Disorder, entanglement, and localization,” Phys. Rev. E 108, 024139 (2023), DOI: 10.1103/PhysRevE.108.024139.
4. D. K. Panda and C. Benjamin, “Phase versus coin versus position disorder as a probe for resilience and revival of entanglement in cyclic quantum walks,” arXiv:2410.12710 (2024). https://arxiv.org/abs/2410.12710
5. A. Ahlbrecht, H. Vogts, A. H. Werner and R. F. Werner, “Asymptotic evolution of quantum walks with random coin,” arXiv:1009.2019 (2010), J. Math. Phys. 52, 042201 (2011), DOI: 10.1063/1.3575568. https://arxiv.org/abs/1009.2019
