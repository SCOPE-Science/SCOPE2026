# Exact equilibrium bias and entropy loss in exponential-Euler Lindblad dynamics on graphs

## Finding
For the full-rank exponential Euler (FREE) quantum channel of Chen, Borzì, Janković, Hartmann and Hervieux, a connected undirected weighted graph with Hermitian edge-flip Lindblad jumps gives an exactly solvable invariant-state problem. Although the continuous Lindblad evolution fixes the maximally mixed state, the numerical channel is unital **if and only if all weighted vertex degrees are equal**. On an irregular graph, every positive step changes the maximally mixed state and strictly decreases its von Neumann entropy. For at least three vertices, the numerical channel has a unique stationary density matrix: a degree-biased diagonal state with an explicit formula. Its equilibrium bias is first order in the step, whereas the one-step entropy defect at the maximally mixed state is fourth order.

More precisely, let \(G=(V,E)\) be a finite connected undirected graph on \(n\ge 2\) vertices, without loops, with symmetric strictly positive edge conductances \(w_{ij}=w_{ji}\) for \(\{i,j\}\in E\). Let \(W=(w_{ij})\), with zero entries at nonedges and on the diagonal, let \(d_i=\sum_j w_{ij}>0\), let \(D=\operatorname{diag}(d_i)\), and let \(L=D-W\). For \(h>0\), put \(f_h(x)=(1-e^{-hx})/x\) for \(x>0\). On diagonal density matrices the channel is the column-stochastic matrix
\[
(P_h)_{ij}=\begin{cases}e^{-hd_i},&i=j,\\w_{ij}f_h(d_j),&i\ne j.\end{cases}
\]
Its unique diagonal stationary probability vector is
\[
\pi_h(i)=\frac{d_i/(1-e^{-hd_i})}{\sum_{j=1}^n d_j/(1-e^{-hd_j})}.
\]
For every connected graph on \(n\ge3\) vertices, \(\operatorname{diag}(\pi_h)\) is the **unique stationary density matrix of the full quantum channel**, and all initial density matrices converge to it under iteration. At \(n=2\), the channel is unital and also admits non-diagonal stationary density matrices.

Writing \(\bar d=n^{-1}\sum_i d_i\) and \(\rho_*=I/n\), the exact asymptotics are
\[
\pi_h(i)=\frac1n+\frac{h}{2n}(d_i-\bar d)+O(h^2),\qquad
\lim_{h\to\infty}\pi_h(i)=\frac{d_i}{\sum_jd_j},
\]
\[
\log n-S(\mathcal E_h(\rho_*))
=\frac{h^4}{8n}\|Ld\|_2^2+O(h^5),
\qquad
\log n-S(\operatorname{diag}(\pi_h))
=\frac{h^2}{8n}\sum_i(d_i-\bar d)^2+O(h^3).
\]
Here \(S(\rho)=-\operatorname{tr}(\rho\log\rho)\). Both displayed leading coefficients are strictly positive exactly for irregular connected graphs. The smallest possible irregular connected graph has three vertices; the weighted three-vertex path with successive edge weights \(1\) and \(2\) has \(d=(1,3,2)\), \(Ld=(-2,4,-2)\), and
\[
\log3-S(\mathcal E_h(I/3))=h^4+O(h^5),\qquad
\lim_{h\to\infty}\pi_h=(1/6,1/2,1/3).
\]

## Assumptions and scope
Use the finite-dimensional Lindblad equation with Hamiltonian \(H=0\), unit jump rates and Hermitian edge-flip jumps \(J_{ij}=\sqrt{w_{ij}}(e_ie_j^{\mathsf T}+e_je_i^{\mathsf T})\). Then \(\sum_{\{i,j\}\in E}J_{ij}^{\dagger}J_{ij}=D\), so \(A=-D/2\). The exact Lindblad generator is \(\mathcal L(\rho)=A\rho+\rho A+\sum_{\{i,j\}\in E}J_{ij}\rho J_{ij}\). The numerical channel is **exactly** the published FREE formula, equation (2.6) of arXiv:2408.13601v1:
\[
\mathcal E_h(\rho)=e^{hA}\rho e^{hA^\dagger}
+\sum_{\{i,j\}\in E}\int_0^h J_{ij}e^{sA}\rho e^{sA^\dagger}J_{ij}\,ds.
\]
All graph sizes are fixed and finite, all edge weights and step sizes are strictly positive, and computations are in exact arithmetic unless numerical verification is explicitly identified. The conclusions are about this full-rank scheme, not a low-rank truncation or the distinct standard exponential Euler scheme.

## Proof
**1. Continuous equilibrium and the diagonal restriction.** Each jump is Hermitian, so the generator annihilates the identity: \(\mathcal L(I)=-D+\sum J_{ij}^2=0\). Thus the exact evolution fixes \(\rho_*=I/n\). On diagonal inputs, each no-jump term contributes \(e^{-hd_i}p_i\) to output coordinate \(i\), and the jump along \(\{i,j\}\) contributes \(w_{ij}\int_0^h e^{-sd_j}ds\,p_j=w_{ij}f_h(d_j)p_j\). This yields the displayed \(P_h\), equivalently \(P_h=I-L\operatorname{diag}(f_h(d_i))\). Its columns sum to one since \(d_jf_h(d_j)=1-e^{-hd_j}\); all entries are nonnegative and diagonals are strictly positive. Connectedness makes \(P_h\) irreducible, hence primitive.

**2. Invariant distribution and unitality.** The vector with components proportional to \(1/f_h(d_i)\) is invariant because for each edge \((P_h)_{ij}\pi_h(j)=w_{ij}/\sum_k1/f_h(d_k)=(P_h)_{ji}\pi_h(i)\). Irreducibility makes it unique. The full channel applied to \(I\) is diagonal, with diagonal \(P_h\mathbf1\). Therefore unitality is equivalent to \(L(f_h(d_i))=0\), since \(P_h\mathbf1-\mathbf1=-L(f_h(d_i))\). For a connected graph \(\ker L=\operatorname{span}\{\mathbf1\}\). The derivative of \(f_h\) has numerator \((1+hx)e^{-hx}-1<0\) for \(x>0\), hence \(f_h\) is strictly decreasing. Thus \(L(f_h(d))=0\) if and only if all degrees are equal. When irregular, \(\mathcal E_h(I/n)\ne I/n\), but it is a density matrix because the FREE channel is completely positive and trace preserving; the strict maximal-entropy principle yields \(S(\mathcal E_h(I/n))<\log n\) for all \(h>0\).

**3. Full quantum uniqueness and convergence.** For \(i\ne j\), let \(E_{ij}=e_ie_j^{\mathsf T}\) and set \(s_{ij}=(d_i+d_j)/2\). Direct substitution in the FREE formula gives
\[
\mathcal E_h(E_{ij})=e^{-hs_{ij}}E_{ij}+w_{ij}f_h(s_{ij})E_{ji},
\]
where \(w_{ij}=0\) for nonedges. Hence the invariant span of \(E_{ij},E_{ji}\) has eigenvalues \(\eta_{ij}^{\pm}=e^{-hs_{ij}}\pm w_{ij}f_h(s_{ij})\). On a connected graph with \(n\ge3\), every edge has \(w_{ij}<s_{ij}\) (an edge cannot itself be an isolated connected component). Therefore \(|\eta_{ij}^{\pm}|<1\); this is immediate at nonedges and follows at edges from \(0\le w_{ij}f_h(s_{ij})<1-e^{-hs_{ij}}\). Every off-diagonal component consequently decays, while the primitive diagonal Markov chain converges to \(\pi_h\). This proves uniqueness and global attraction of \(\operatorname{diag}(\pi_h)\). For \(n=2\), both degrees equal their unique edge weight, and the symmetric coherence \(E_{12}+E_{21}\) has eigenvalue one, explaining the exception.

**4. Bias and entropy coefficients.** The Taylor expansion \(f_h(d_i)=h-\frac12h^2d_i+O(h^3)\) implies \(1/f_h(d_i)=h^{-1}+d_i/2+O(h)\), and normalizing gives the stated expansion of \(\pi_h\). The large-step limit follows from \(f_h(d_i)\to1/d_i\). Also
\[
P_h\mathbf1-\mathbf1=-Lf_h(d)=\frac12h^2Ld+O(h^3),
\]
so \(\mathcal E_h(I/n)=\operatorname{diag}(u+\delta)\), where \(u=\mathbf1/n\), \(\delta=h^2Ld/(2n)+O(h^3)\), and \(\sum_i\delta_i=0\). Taylor expansion of Shannon entropy about \(u\) gives \(\log n-H(u+\delta)=\frac n2\|\delta\|_2^2+O(\|\delta\|_2^3)\), yielding the fourth-order coefficient. Applying the same expansion to \(\pi_h-u=h(d-\bar d\mathbf1)/(2n)+O(h^2)\) proves the stationary-entropy coefficient. Connectedness gives \(Ld=0\) precisely for regular graphs. The three-vertex path and minimal dimension follow by direct substitution; every connected two-vertex graph is weighted-regular.

## Verification
Run `python verify.py` with Python 3 standard library. It performs numerical evaluations of the exact graph-transition entries, direct evaluation of the FREE diagonal Kraus integrals, column stochasticity, detailed balance, the predicted stationary law, strict off-diagonal contraction blocks, the exceptional two-vertex coherence, the small-step entropy coefficient and the large-step stationary limit. It passes 109276 assertion families on deterministic examples and seeded connected random weighted graphs. The proof above, not those finite tests, establishes statements for every permitted graph and step size.

## Relationship to prior work
Chen, Borzì, Janković, Hartmann and Hervieux introduced the FREE map and proved unconditional positivity, trace preservation and finite-time accuracy (arXiv:2408.13601v1, §§2–4). These inherited properties and the formula of the integrator are not new. Their later midpoint work (arXiv:2506.00346v1) studies a different, second-order algorithm, not the same map. Cao and Lu (arXiv:2103.01194) develop alternative structure-preserving Lindblad numerical schemes. Classical finite-state Markov-chain theory supplies the standard detailed-balance, Perron convergence and entropy facts used here. The contribution assessed here is the **specific exact invariant state of the published FREE channel on Hermitian graph-jump Lindbladians, the if-and-only-if weighted-regularity criterion for quantum unitality, global quantum fixed-point convergence, and the quantitative one-step and stationary entropy defects**. Generic stochastic-matrix results are not claimed as original. No directly covering same-map statement was identified among the inspected primary sources and related searches; specialized equivalent results may exist.

## Limitations
This theorem assumes a finite connected undirected graph, strictly positive symmetric edge weights, edge-flip Hermitian jumps, vanishing Hamiltonian, exact integration of the FREE jump integrals, and fixed positive step size. It does not address arbitrary Lindblad operators, complex Hamiltonians, time-dependent coefficients, low-rank truncations, or alternative exponential integrators. The numerical channel is still completely positive, trace preserving and first-order consistent; the equilibrium bias concerns indefinite iteration at fixed step size and does not invalidate existing finite-horizon convergence theorems. The fourth-order and second-order entropy expansions are as the step tends to zero for a fixed graph. No independent scientific validation is asserted.

## References
1. H. Chen, A. Borzì, D. Janković, J.-G. Hartmann and P.-A. Hervieux, *Full- and low-rank exponential Euler integrators for the Lindblad equation*, arXiv:2408.13601v1, first public version 2024-08-24, especially equation (2.6) and Theorems 3.1 and 3.3. https://arxiv.org/html/2408.13601v1
2. H. Chen and A. Borzì, *Full- and low-rank exponential midpoint schemes for forward and adjoint Lindblad equations*, arXiv:2506.00346v1, 2025. https://arxiv.org/html/2506.00346v1
3. F. Cao and J. Lu, *Structure-preserving numerical schemes for Lindblad equations*, arXiv:2103.01194, 2021. https://arxiv.org/abs/2103.01194
