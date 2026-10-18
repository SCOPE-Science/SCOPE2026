# Exact absorption by the first Hamming shell of a quantum hypercube

## Finding
Let \(d\ge2\) be an integer. In the continuous-time quantum walk on the Boolean hypercube \(Q_d\), independently absorb at **all** the \(d\) Hamming-weight-one vertices, with an arbitrary strictly positive absorption rate at each such vertex. Then the space of nondecaying states and the eventual absorption probability of **every** vertex state are independent of these rates and of the positive uniform hopping strength.

Precisely, the bright and dark dimensions are
\[
\dim\mathcal B=d^2-d+2-\mathbf1_{2\mid d},\qquad
\dim\mathcal D=2^d-d^2+d-2+\mathbf1_{2\mid d}.
\]
For a vertex \(x\) of Hamming weight \(s\in\{0,\ldots,d\}\), define
\[
\mathsf K_k(s)=\sum_{j=\max(0,k-d+s)}^{\min(k,s)}
(-1)^j\binom{s}{j}\binom{d-s}{k-j}.
\]
Its exact probability of eventual absorption is
\[
\boxed{\ P_{\mathrm{abs}}(d,s)=
\frac{1+(d-1)\mathbf1_{1\le s\le d-1}}{\binom ds}
-\mathbf1_{2\mid d}\frac{\mathsf K_{d/2}(s)^2}{2^d\binom d{d/2}}.\ }
\]
In particular, although **every nearest neighbor** of the origin absorbs, an excitation initially at the origin is eventually absorbed with probability \(1\) for odd \(d\), but with probability \(1-2^{-d}\binom d{d/2}\) for even \(d\). This dimension-parity discontinuity persists at arbitrary unequal positive absorption rates.

## Assumptions and scope
The Hilbert space is \(\mathcal H=\mathbb C^{\{0,1\}^d}\), with orthonormal basis \(\{|x\rangle:x\in\{0,1\}^d\}\). Let \(e_i\) denote the bit string with only coordinate \(i\) equal to one, and let \(X_i\) flip coordinate \(i\). Fix \(J>0\) and rates \(\gamma_i>0\) for every \(i\in\{1,\ldots,d\}\). Define the Hermitian hopping Hamiltonian and lossy no-jump generator by
\[
H=J\sum_{i=1}^d X_i,\qquad
K=H-\frac{i}{2}\sum_{i=1}^d\gamma_i|e_i\rangle\langle e_i|.
\]
For every normalized initial state \(|\psi\rangle\), the no-jump survival probability at time \(t\ge0\) is \(S_\psi(t)=\|e^{-iKt}|\psi\rangle\|^2\), and the eventual absorption probability is \(P_{\mathrm{abs}}(\psi)=1-\lim_{t\to\infty}S_\psi(t)\). The limit exists because \(S_\psi\) is nonincreasing. The claimed site formula specializes to \(|\psi\rangle=|x\rangle\). This is **continuous absorption**, not discrete projective sampling or pure dephasing; no uniform-in-time convergence rate is asserted.

## Proof
**1. Reduction to a spectral bright subspace.** Write \(L=\sum_i\gamma_i|e_i\rangle\langle e_i|\). An eigenpair \(K|v\rangle=\lambda|v\rangle\) obeys
\[
\operatorname{Im}\lambda\,\|v\|^2
=-\tfrac12\langle v|L|v\rangle\le0.
\]
Equality holds precisely when \(\langle e_i|v\rangle=0\) for all \(i\); then \(Hv=\lambda v\) and \(\lambda\) is real. Let \(\mathcal D\) be the direct sum, over all eigenvalues of \(H\), of eigenspace vectors orthogonal to all \(|e_i\rangle\). This space is reducing for \(H\), annihilated by \(L\), and reducing for \(K\); its orthogonal complement \(\mathcal B\) contains no real-eigenvalue vector of \(K\). Every eigenvalue of \(K|_{\mathcal B}\) consequently has strictly negative imaginary part, even if Jordan blocks occur. Thus the exponential decays to zero on \(\mathcal B\), whereas evolution is unitary on \(\mathcal D\):
\[
P_{\mathrm{abs}}(\psi)=\|\Pi_{\mathcal B}\psi\|^2,
\qquad
\mathcal B=\operatorname{span}\{H^k|e_i\rangle:k\ge0,1\le i\le d\}.
\]
In particular, the eventual absorption law depends on the **support** of the positive rates, not their sizes.

**2. Only two permutation types are bright.** For each Hamming shell \(s\), set \(c_s=\binom ds\) and
\[
|u_s\rangle=c_s^{-1/2}\sum_{|x|=s}|x\rangle.
\]
For \(1\le s\le d-1\) define \(d\) vectors
\[
|v_{s,i}\rangle=\sum_{|x|=s}(x_i-s/d)|x\rangle,
\qquad 1\le i\le d.
\]
Their span \(\mathcal T_s\) has dimension \(d-1\): its only linear coefficient relation is \(\sum_i v_{s,i}=0\), because for \(0<s<d\) a linear form constant on all size-\(s\) subsets must have all coefficients equal. Each \(\mathcal T_s\) is perpendicular to \(|u_s\rangle\). Define mutually perpendicular spaces
\[
\mathcal R=\operatorname{span}\{|u_s\rangle:0\le s\le d\},
\quad \mathcal T=\bigoplus_{s=1}^{d-1}\mathcal T_s.
\]
Counting neighbors in adjacent shells gives
\[
H|v_{s,i}\rangle=J\big((d-s)|v_{s-1,i}\rangle+s|v_{s+1,i}\rangle\big),
\]
where \(v_{0,i}=v_{d,i}=0\); also
\[
H|u_s\rangle=J\sqrt{s(d-s+1)}|u_{s-1}\rangle
+J\sqrt{(s+1)(d-s)}|u_{s+1}\rangle,
\]
with absent boundary terms interpreted as zero. Hence \(\mathcal R\) and \(\mathcal T\) are invariant under \(H\). Since the detector space \(\operatorname{span}\{|e_i\rangle\}\) is exactly \(\operatorname{span}\{|u_1\rangle\}\oplus\mathcal T_1\), the bright space is contained in \(\mathcal R\oplus\mathcal T\). The first identity and its nonzero successive off-diagonal coefficients show inductively that the \(H\)-cyclic span of \(\mathcal T_1\) equals all of \(\mathcal T\), with dimension \((d-1)^2\).

**3. The unique parity exception in the radial sector.** For each \(k\in\{0,\ldots,d\}\), the normalized symmetric Walsh eigenvector
\[
|\phi_k\rangle=\frac{1}{\sqrt{2^d\binom dk}}
\sum_{|z|=k}\sum_x(-1)^{z\cdot x}|x\rangle
\]
has eigenvalue \(J(d-2k)\), is radial, and has coordinate \(\langle x|\phi_k\rangle=\mathsf K_k(|x|)/\sqrt{2^d\binom dk}\). The \(d+1\) such states are orthonormal and span \(\mathcal R\). Their overlap with \(|u_1\rangle\) vanishes exactly when \(\mathsf K_k(1)=\binom dk(d-2k)/d=0\). Therefore \(|u_1\rangle\) is cyclic for all of \(\mathcal R\) when \(d\) is odd, and for the codimension-one radial space \(\mathcal R\ominus\operatorname{span}\{|\phi_{d/2}\rangle\}\) when \(d\) is even. Consequently
\[
\mathcal B=\begin{cases}
\mathcal T\oplus\mathcal R,&d\text{ odd},\\
\mathcal T\oplus\bigl(\mathcal R\cap\operatorname{span}\{|\phi_{d/2}\rangle\}^{\perp}\bigr),&d\text{ even}.
\end{cases}
\]
This proves both dimension formulas.

**4. Sitewise projection.** At any site \(x\) of weight \(s\), \(\langle x|\Pi_{\mathcal R}|x\rangle=1/c_s\). For interior shells \(1\le s\le d-1\), the projector onto \(\mathcal T_s\) has rank \(d-1\) and constant diagonal under permutations of the \(c_s\) sites, so its diagonal is \((d-1)/c_s\); the standard sector is absent on the endpoint shells. When \(d\) is even, subtract the diagonal of \(|\phi_{d/2}\rangle\langle\phi_{d/2}|\), namely \(\mathsf K_{d/2}(s)^2/(2^d\binom d{d/2})\). This is exactly the stated formula. At \(s=0\), the Walsh sum gives \(\mathsf K_{d/2}(0)=\binom d{d/2}\), proving the origin parity formula.

## Verification
The self-contained companion `verify.py` constructs every Walsh eigenspace, projects its detected vectors by singular-value decomposition, and independently compares all diagonal bright-projector entries with the theorem for every \(2\le d\le8\). It also checks bright-space dimension, projector idempotence, and long-time no-jump propagation for several unequal positive rates in dimensions \(2,3,4\). Execution produced 557 passed assertions and maximum absolute numerical discrepancy below \(3.5\times10^{-12}\). These finite checks do not prove the all-dimension theorem; the proof is above. Reproduce with `python verify.py` after installing NumPy and SciPy.

## Relationship to prior work
Le, Donati, Severini, and Caruso (arXiv:1707.07482, first public 2017-07-24) develop the dark-subspace picture for dissipative quantum-network transfer, especially a **single** sink, plus graph constructions; that general framework is an ingredient here but does not supply the all-neighbor hypercube projector or parity formula. Thiel, Mualem, Meidan, Barkai, and Kessler (arXiv:1906.08112) compute bright/dark detection probabilities including a **single-node** hypercube example using **repeated projective** measurements. Thiel, Mualem, Kessler, and Barkai (arXiv:1909.02114) refine single-target symmetry bounds, again not multiple independent lossy sites. Strauch (arXiv:0808.3403) analyzes a different hypercube **decoherence** model and its hitting probabilities, not the present absorbing first shell. The new mathematical content is the exact cyclic-space decomposition for this whole detector shell, the unique even-dimensional radial zero mode, and every sitewise closed-form absorption probability valid for arbitrary heterogeneous strictly positive loss rates. These general theoretical precursors are not claimed as new.

## Limitations
The statement uses uniform coherent hypercube edge hopping and strictly positive rates on **every** Hamming-weight-one site; zeroing even one rate or changing edge weights may change the bright space. No coherent disorder, additional pure dephasing, many-particle interactions, or quantum-Zeno projective-measurement limit is included. The result is asymptotic in observation time and gives no convergence-rate bound. Equivalent unpublished or less easily located consequences of general spectral controllability methods remain a priority risk. Independent review of mathematical priority and correctness has not been performed.

## References
1. T. P. Le, L. Donati, S. Severini, and F. Caruso, “How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures,” arXiv:1707.07482 (2017), *Journal of Physics A* **51** (2018), 365306, doi:10.1088/1751-8121/aad3e6.
2. F. Thiel, I. Mualem, D. Meidan, E. Barkai, and D. A. Kessler, “Quantum total detection probability from repeated measurements I. The bright and dark states,” arXiv:1906.08112 (2019).
3. F. Thiel, I. Mualem, D. A. Kessler, and E. Barkai, “Quantum total detection probability from repeated measurements II. Exploiting symmetry,” arXiv:1909.02114 (2019).
4. F. W. Strauch, “Reexamination of decoherence in quantum walks on the hypercube,” arXiv:0808.3403 (2008), *Physical Review A* **79** (2009), 032319.
