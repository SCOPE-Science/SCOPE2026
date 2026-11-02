# Centered-exponential spectral law for collective cross-commutators on quadratic polydisc quotients

## Finding
For every integer \(d\ge2\), let \(N_d=H^2(\mathbb D^d)\ominus[z_1^2-z_2^2,\ldots,z_{d-1}^2-z_d^2]\), and let \(S_i\) be the compression of multiplication by \(z_i\) to \(N_d\). Define the **collective, self-adjoint cross-commutator**
\[\mathcal C_d=\sum_{1\le i\ne j\le d}[S_i^*,S_j].\]
Let \(J_d\) act on \(\ell^2(\mathcal P(\{1,\ldots,d\}))\) by sending each subset to the sum of all subsets obtained by replacing one of its elements with an element not already present. The exact model is
\[\mathcal C_d\cong J_d\otimes D_d,\qquad D_de_\ell=\frac{d-1}{(\ell+d-1)(\ell+d)}e_\ell.\]
The restriction of \(J_d\) to the \(k\)-subset sector has eigenvalues
\[\lambda_{d,k,r}=k(d-k)-r(d-r+1),\quad 0\le r\le\min(k,d-k),\]
with multiplicities \(m_{d,r}=\binom dr-\binom d{r-1}\), using \(\binom d{-1}=0\). Thus all nonzero eigenvalues of \(\mathcal C_d\) are \(\lambda_{d,k,r}(d-1)/[(\ell+d-1)(\ell+d)]\), with multiplicities understood as a multiset.

The spectral norm and trace norm are **exactly**
\[\|\mathcal C_d\|=\frac{\lfloor d^2/4\rfloor}{d},\qquad \|\mathcal C_d\|_1=\sum_{k=0}^d\sum_{r=0}^{\min(k,d-k)}m_{d,r}|\lambda_{d,k,r}|.\]
The new asymptotic phenomenon is a centered exponential spectral law. For the normalized eigenvalue counting measure \(\nu_d=2^{-d}\sum_{j=1}^{2^d}\delta_{\lambda_j(J_d)/d}\),
\[\nu_d\Rightarrow \operatorname{Law}((E-1)/2),\quad E\sim\mathrm{Exp}(1),\qquad\lim_{d\to\infty}\frac{\|\mathcal C_d\|_1}{d2^d}=\frac1e.\]

## Assumptions and scope
The Hilbert space is the complex polydisc Hardy space with its standard monomial orthonormal basis. All generators use the inner functions \(\eta_i(z)=z^2\), and \(d\ge2\) is an integer. The sum runs over **ordered distinct pairs**; thus each unordered pair occurs together with its adjoint. The limit is across ambient dimensions, not a fixed-dimension truncation of the infinite quotient operator. Multiplicities in the finite spectrum include coincidence across distinct \((k,r)\) labels.

## Proof
**Common quotient model.** Each model space \(K_i=H^2\ominus z^2H^2\) is \(\operatorname{span}\{1,z\}\); its rank-one defect map is \(T_i=|1\rangle\langle z|\). The orthonormal basis and common weighted-shift model for quotient modules give the *same* unitary identification of the entire quotient with \((\mathbb C^2)^{\otimes d}\otimes\ell^2(\mathbb N_0)\) for all coordinates simultaneously. Compressed shifts take the form \(S_i\cong A_i\otimes I+T_i\otimes B_d\), where the operators in the first two factors act only at site \(i\) and \(B_de_\ell=\sqrt{(\ell+1)/(\ell+d)}e_{\ell+1}\). For \(i\ne j\), the factors on distinct sites commute and the mixed commutator is
\[[S_i^*,S_j]\cong (|z\rangle\langle1|)_i(|1\rangle\langle z|)_j\otimes(B_d^*B_d-B_dB_d^*).\]
A direct subtraction of consecutive squared weights yields the stated positive diagonal \(D_d\). Hence the finite factor in the sum maps the basis state indexed by a subset \(A\subset\{1,\ldots,d\}\) to the sum of states obtained by moving one excitation from an occupied site to an unoccupied site; this is precisely \(J_d\). The identity \(\sum_{\ell\ge0}(d-1)/[(\ell+d-1)(\ell+d)]=1\) proves trace class and \(\|\mathcal C_d\|_1=\|J_d\|_1\).

**Finite-dimensional spectral classification.** Let \(V_k\) be the functions on \(k\)-subsets. Define \(U_k:V_k\to V_{k+1}\) by adding one element with coefficient one, and \(D_k=U_{k-1}^*\) by removing one element. Direct counting gives \(U_{k-1}D_k=J_d|_{V_k}+kI\) and \(D_{k+1}U_k-U_{k-1}D_k=(d-2k)I\). The last identity shows inductively that \(U_{r-1}\) is injective for \(r\le d/2\) and the harmonic space \(\ker D_r\) has dimension \(m_{d,r}=\binom dr-\binom d{r-1}\). If \(h\in\ker D_r\), repeated commutation yields
\[D_k U^{k-r}h=(k-r)(d-k-r+1)U^{k-r-1}h.\]
Therefore \(U^{k-r}h\), for \(r\le k\le d-r\), is an eigenvector of \(J_d|_{V_k}\) with eigenvalue \((k-r)(d-k-r+1)-k=\lambda_{d,k,r}\). Orthogonality of distinct eigenspaces and the telescoping dimension sum show these account for all \(\binom dk\) dimensions. The largest eigenvalue of the nonnegative symmetric adjacency is its maximal vertex degree, \(\max_k k(d-k)=\lfloor d^2/4\rfloor\). Since \(\|D_d\|=1/d\), the norm formula follows; the trace norm follows by summing the exact absolute eigenvalues.

**Limit law.** On \((\mathbb C^2)^{\otimes d}\), write \(\sigma_x^{(i)}\) and \(\sigma_y^{(i)}\) for Pauli matrices at site \(i\), and put \(X_d=d^{-1/2}\sum_i\sigma_x^{(i)}\), \(Y_d=d^{-1/2}\sum_i\sigma_y^{(i)}\). The elementary spin identity is
\[\frac{J_d}{d}=\frac{X_d^2+Y_d^2-2I}{4}.\]
Consider any fixed word in \(X_d,Y_d\) under normalized trace \(\tau_d=2^{-d}\operatorname{Tr}\). Expand its labels. If an index occurs only once, that term has zero trace because each Pauli matrix is traceless. Terms with fewer than half as many distinct indices as word length vanish after the \(d^{-m/2}\) normalization; the leading terms are pairings of positions, each pair at one site. Two unequal Pauli types at a paired site have trace zero, while matching types have trace one. Thus all joint noncommutative word moments converge to Wick moments of **two independent real standard Gaussians** \(G_x,G_y\). By polynomial substitution, every moment of \(J_d/d\) converges to that of \((G_x^2+G_y^2-2)/4\), which has law \((E-1)/2\) for \(E\sim\mathrm{Exp}(1)\). This limiting distribution has a moment-generating function finite near zero, so its moments determine it; convergence of moments therefore implies weak convergence of \(\nu_d\).

To pass to absolute values, note the exact normalized second moment: the diagonal of \(J_d^2\) at a \(k\)-subset is \(k(d-k)\); averaging a uniform random subset yields \(\tau_d(J_d^2)=d(d-1)/4\). Consequently \(\sup_d\int t^2d\nu_d(t)\le1/4\), which gives uniform integrability of \(|t|\). Hence \(\int|t|d\nu_d(t)\to\mathbb E|(E-1)/2|=1/e\). Because \(\|\mathcal C_d\|_1=\|J_d\|_1=d2^d\int|t|d\nu_d(t)\), the claimed trace-norm asymptotic follows.

## Verification
The included `checker.py` constructs all subset-exchange matrices for \(2\le d\le8\), verifies the exact characteristic eigenvalue multisets, trace norms, and the infinite-factor telescoping identity with rational arithmetic. It also checks the predicted constant by direct finite spectrum in larger dimensions. This finite work is a consistency test; the infinite-dimensional model and limiting theorem are established analytically above.

## Relationship to prior work
Xiang and Xu, arXiv:2610.02692v1 (2026-10-02), establish the common quotient basis and individual cross-commutator tensor formula (their Proposition 4.1), and compute Hilbert–Schmidt norms for individual pairs. Those facts are explicit inputs here and are **not** claimed as new. Classical Johnson-graph eigenvalues and the Pauli-matrix/Wick pairing principle are also standard. The contribution is their application to the **collective ordered-pair operator**, yielding a complete all-dimension spectral classification and especially its centered-exponential large-dimension law and sharp \(1/e\) trace-norm constant. The 2022 work of Zou, Yu, and Yang concerns individual compressed multipliers and commutator Hilbert–Schmidt norms; it does not explicitly present this collective all-dimension limit in the available abstract. A broader historical complete-graph exchange Hamiltonian density-of-states theorem could give another route to the same limit; publication priority is not independently certified.

## Limitations
The result concerns exactly the symmetric quadratic inner-function family and the ordered-pair sum, not arbitrary inner functions or arbitrary linear combinations. The finite spectral law includes many repeated or zero eigenvalues and no claim about fixed-dimensional singular-value asymptotics beyond the displayed tensor model. No assertion of independent mathematical review or absolute novelty is made.

## References
1. A. Xu and Y. Xiang, *Hilbert–Schmidt Norms of Self-Commutator and Cross-Commutator on N_eta-type Quotient Modules in Polydisc*, arXiv:2610.02692v1 (2026), Proposition 4.1 and Lemmas 2.3–2.4. https://arxiv.org/abs/2610.02692
2. H. Zou, T. Yu and Y. Yang, *The core operator and the compressed multipliers on M_psi,phi-type submodules*, Banach J. Math. Anal. **16** (2022), Article 26, DOI:10.1007/s43037-022-00180-y.
3. P.-A. Bernard, N. Crampé and L. Vinet, *Entanglement of Free Fermions on Johnson Graphs*, J. Math. Phys. (2022), DOI:10.1063/5.0099879 (classical Johnson-scheme context).
