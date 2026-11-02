# Four snapshots are the sharp chronology threshold for periodic SIS on undirected simple contact networks

## Finding
Consider a continuous-time deterministic network-mean-field susceptible–infectious–susceptible (SIS) model with a periodically repeated list of contact snapshots, each having a symmetric adjacency matrix and a prescribed positive duration. The disease-free Floquet multiplier is **unchanged by every permutation of at most three snapshots**, even though intermediate infected-state trajectories need not agree. The first possible epidemic-threshold change caused solely by reordering snapshots occurs with **four snapshots and three vertices**, and both bounds are sharp among finite simple undirected contact networks.

For an exact three-vertex witness, one time unit is spent on each of the four edge snapshots, and each snapshot activates one edge. Write \(A=\{12\}\), \(B=\{23\}\), \(C=\{13\}\); the fourth snapshot repeats \(A\). Fix transmission rate \(\beta=\log 2\) and recovery rate \(\mu=(\log 7)/4\). Under repeated chronological order \(A,A,B,C\), the disease-free state is unstable and a unique positive four-periodic SIS state attracts every nonzero initial infection vector. Under order \(A,B,A,C\), with *exactly the same snapshots, aggregate contact exposures, and parameters*, every infection vector converges exponentially to zero.

## Assumptions and scope
Let \(n\ge1\) and let each snapshot \(G_j\) be a finite, undirected, loopless, unweighted graph on the same labeled vertex set with symmetric adjacency \(A_j\). Its duration \(\tau_j>0\) is attached to the snapshot and travels with it when snapshots are reordered. The deterministic SIS equation is
\[
\dot x_i(t)=-\mu x_i(t)+\beta(1-x_i(t))\sum_{k=1}^{n}(A(t))_{ik}x_k(t),\qquad x(t)\in[0,1]^n,
\]
with common \(\beta,\mu>0\). The snapshots repeat indefinitely in their prescribed order; the comparison fixes each snapshot together with its duration. A Floquet multiplier refers to the disease-free linearization, not to the finite-population stochastic SIS chain.

## Proof
**Three-snapshot invariance.** Put \(Q_j=\exp(\tau_j(\beta A_j-\mu I))\). Each \(Q_j\) is symmetric, invertible, and positive definite. A period matrix for the ordering \(1,2,3\) is \(Q_3Q_2Q_1\). A cyclic rotation of factors preserves every eigenvalue by similarity: \(XYZ\) and \(YZX\) are similar for invertible matrices. Reversing the factors transposes the product, because each factor is symmetric, so its eigenvalues are unchanged. Every permutation of three symbols follows from cyclic rotation and reversal. The same argument covers one or two snapshots and repeated snapshots. Thus the full Floquet spectrum, and hence the disease-free threshold, is independent of ordering for any \(n\) when the period has at most three snapshots. This asserts neither equality of trajectories nor equivalence of nonlinear periodic states.

**Sharpness in vertex number.** On at most two vertices a loopless undirected contact adjacency is either the zero matrix or the same single-edge matrix. These matrices commute, and so do their exponentials: no number of snapshots on at most two vertices can create spectral chronology dependence. It suffices to build the stated three-vertex, four-snapshot witness.

**Exact four-snapshot certificate.** With \(\beta=\log2\) and unit snapshot duration, the contact exponential \(E_{ij}=\exp(\beta A_{ij})\) equals the identity away from vertices \(i,j\), with \(2\times2\) contact block \(\bigl(\begin{smallmatrix}5/4&3/4\\3/4&5/4\end{smallmatrix}\bigr)\). Set \(E_A=E_{12}\), \(E_B=E_{23}\), \(E_C=E_{13}\). The contact-only monodromy matrices for the two chronological orders are
\[
M_{\mathrm{adj}}=E_CE_BE_A^2=
\begin{pmatrix}
475/128&453/128&15/16\\
75/32&85/32&3/4\\
429/128&435/128&25/16
\end{pmatrix},
\]
\[
M_{\mathrm{sep}}=E_CE_AE_BE_A=
\begin{pmatrix}
833/256&855/256&105/64\\
135/64&161/64&15/16\\
615/256&705/256&127/64
\end{pmatrix}.
\]
All entries are positive. The exact rational positive vectors \(u=(16,11,16)^\mathsf T\) and \(v=(16,11,14)^\mathsf T\) satisfy
\[
M_{\mathrm{adj}}u-7u=(167/128,55/32,513/128)^\mathsf T>0,
\]
\[
7v-M_{\mathrm{sep}}v=(59/256,157/64,381/256)^\mathsf T>0.
\]
The Perron–Frobenius comparison theorem (or elementary iteration of positive matrices) therefore gives \(\rho(M_{\mathrm{adj}})>7>\rho(M_{\mathrm{sep}})\). Because \(e^{-4\mu}=1/7\), their true disease-free period matrices are exactly \(M_{\mathrm{adj}}/7\) and \(M_{\mathrm{sep}}/7\). The first is supercritical and the second strictly subcritical. Their characteristic polynomials are, respectively,
\[
z^3-\frac{1015}{128}z^2+\frac{745}{128}z-1,
\qquad
z^3-\frac{1985}{256}z^2+\frac{1553}{256}z-1.
\]

**Nonlinear outcomes.** Write \(P\) for the one-period nonlinear time map on \([0,1]^3\), and \(U=DP(0)\) for its positive monodromy matrix. The SIS vector field is cooperative, and the quadratic saturation term is nonpositive. Consequently \(0\le P(x)\le Ux\) on the infection cube. Under \(\rho(U)<1\), iteration gives \(0\le P^k(x)\le U^kx\to0\) exponentially; bounded propagation between period endpoints yields continuous-time extinction.

When \(\rho(U)>1\), let \(w>0\) be its Perron right eigenvector. Differentiability at zero gives \(P(\varepsilon w)>\varepsilon w\) for sufficiently small \(\varepsilon>0\); recovery yields \(P(\mathbf 1)<\mathbf1\). Monotone iteration of these lower and upper solutions produces at least one fixed point strictly inside the cube. All three edges activate in each period, so \(P(x)>0\) componentwise for any nonzero \(x\ge0\). Moreover for every \(y>0\) and \(0<\theta<1\), the SIS saturation term yields **strict subhomogeneity** \(P(\theta y)>\theta P(y)\) componentwise: along a period every node receives positive input while its infection probability is positive. If there were two different positive fixed points, compare their largest attainable componentwise scalar ratio and use strict subhomogeneity to contradict a coordinate of equality. Hence the positive fixed point is unique. Monotone upper/lower iteration, followed by a positive-time iterate of any nonzero state, sandwiches every nonzero trajectory and proves global attraction to its periodic continuation. This establishes the claimed opposite nonlinear outcomes, not merely a linearization contrast.

## Verification
Run `python verify.py` using Python's standard library. The checker constructs each contact exponential as an exact rational matrix; verifies every one of six three-snapshot permutations; recomputes both characteristic polynomials; validates both strict Perron vector certificates; and checks the 24 labeled permutations of the four-snapshot multiset against the two stated polynomial classes. These finite checks corroborate the exact witness but are not substitutes for the universal permutation and nonlinear monotonicity proofs above.

## Relationship to prior work
Sejunti, Taylor and Masuda (2024) developed SIS Floquet thresholds and a paradox in two-snapshot temporal contact systems; their paper explores general weighted two- and three-node snapshots, but does not state the universal three-snapshot spectral permutation invariance or the sharp four-snapshot/three-vertex order-controlled disease switch here. Allen, Moore and Hébert-Dufresne (2022) analyze noncommuting contact snapshots and errors from compressing their chronology; their analysis concerns transient epidemic spreading/aggregation, rather than this sharp all-parameters periodic epidemic-threshold invariance and rational bistatus certificate. Cai, Nie and Holme (2023) address temporally evolving *stochastic activity-driven* networks; their underlying process is not this deterministic periodic snapshot model. General Floquet product formulations underlie the argument but do not by themselves specify the minimal phase and vertex budgets of the example. These distinctions do not establish absolute priority across uninspected mathematical matrix-product literature.

## Limitations
The invariant theorem requires a common scalar recovery rate and symmetric snapshots (equivalently, every linear snapshot generator symmetric); directed contacts need not enjoy transposition invariance. The sharpness construction is for a deterministic mean-field approximation, not stochastic persistence in a finite SIS Markov chain, which has an absorbing disease-free state. The two schedules are periodically repeated indefinitely, and the four snapshots are *not distinct* (one edge appears twice). The result asserts threshold and long-run infection differences, not equality of all intermediate trajectories for at most three snapshots. Priority against more general algebraic matrix-product results remains a residual risk; independent validation has not been performed.

## References
1. M. I. Sejunti, D. Taylor and N. Masuda, *A Parrondo paradox in susceptible-infectious-susceptible dynamics over periodic temporal networks*, arXiv:2406.16787v1, publicly released 24 June 2024. https://arxiv.org/html/2406.16787v1
2. A. J. Allen, C. Moore and L. Hébert-Dufresne, *Compressing the chronology of a temporal network with graph commutators*, arXiv:2205.11566v1 (23 May 2022); accessible full text arXiv:2205.11566v3. https://arxiv.org/html/2205.11566v3
3. C.-R. Cai, Y.-Y. Nie and P. Holme, *The nature of epidemic criticality in temporal networks*, arXiv:2311.12175v1, 20 November 2023. https://arxiv.org/html/2311.12175v1
4. E. Valdano, L. Ferreri, C. Poletto and V. Colizza, *Analytical Computation of the Epidemic Threshold on Temporal Networks*, Phys. Rev. X 5, 021005 (2015). https://doi.org/10.1103/PhysRevX.5.021005
5. S. Sanatkar et al., *Epidemic Threshold of an SIS Model in Dynamic Switching Networks*, arXiv:1501.02472. https://arxiv.org/abs/1501.02472
