# Parity-protected polynomial return on half-dephased quantum hypercubes

## Finding
Let \(d\ge1\) be an integer and let \(Q_d\) be the binary \(d\)-dimensional hypercube. A continuous-time quantum walker has Hamiltonian \(H=\omega A\), where \(A\) is the unweighted adjacency matrix and \(\omega\in\mathbb R\setminus\{0\}\). Every even-Hamming-parity vertex \(e\) is subject to independent, strictly positive site dephasing with rate \(\gamma_e>0\), while odd-parity vertices are not dephased. The generator is
\[
\mathcal L(\rho)=-i[H,\rho]+\sum_{e\in E}\gamma_e\left(P_e\rho P_e-\tfrac12\{P_e,\rho\}\right),\qquad P_e=|e\rangle\langle e|.
\]
Let \(D\) be the orthogonal projection onto the unmonitored, zero-energy subspace
\[
\mathcal D=\{\psi\in\mathbb C^{2^d}:\operatorname{supp}\psi\subseteq O,\ A\psi=0\},\qquad k_d=\operatorname{rank}D.
\]
Its dimension is exactly
\[
k_d=\begin{cases}0,&d\text{ odd},\\\tfrac12\binom d{d/2},&d\text{ even}.\end{cases}
\]
For **every** initial density matrix, all times tending to infinity produce the explicit limit
\[
\boxed{\lim_{t\to\infty}\rho(t)=D\rho(0)D+\frac{1-\operatorname{Tr}(D\rho(0))}{2^d-k_d}(I-D).}
\]
The stationary operator algebra is one scalar block on \(\mathcal D^\perp\) and the full matrix algebra on \(\mathcal D\); its complex dimension is \(1+k_d^2\). No other nondecaying oscillations occur.

For a localized initial state at **any odd vertex** \(v\), put
\[
p_d=\langle v|D|v\rangle=\begin{cases}0,&d\text{ odd},\\ 2^{-d}\binom d{d/2},&d\text{ even}.\end{cases}
\]
The exact long-time return probability is
\[
\boxed{R_d=\lim_{t\to\infty}\langle v|\rho(t)|v\rangle=p_d^2+\frac{(1-p_d)^2}{2^d-k_d}.}
\]
In odd dimensions \(R_d=2^{-d}\), but **along even dimensions**
\[
\boxed{R_d\sim\frac2{\pi d}\qquad(d\to\infty,\ d\text{ even}).}
\]
For comparison, an initially occupied even vertex has exact long-time return probability \((2^d-k_d)^{-1}\). The polynomial-versus-exponential contrast holds for every strictly positive choice of site-dephasing rates and every nonzero real hopping scale.

## Assumptions and scope
The Hilbert space is one particle on the vertices of a simple unweighted hypercube, not a tensor-product many-particle spin state. Even vertices have an even number of ones in their binary address. Write \(E\) and \(O\) for the even and odd parity sets, each of size \(2^{d-1}\). Dephasing is site-resolved: each jump operator is the **rank-one** projector \(P_e\), not a single collective projector onto the entire even sublattice and not a coordinate-bit projector. The rates \(\gamma_e\) are positive but need not agree. There is no absorption, on-site potential, hopping disorder, or parity-mixing extra edge. The infinite-dimension assertion takes \(t\to\infty\) at fixed \(d\) first.

## Proof
**1. Dissipation and peripheral spectrum.** On the Hilbert–Schmidt space of matrices, for any \(X\),
\[
\operatorname{Re}\operatorname{Tr}\bigl(X^\dagger\mathcal L(X)\bigr)=-\frac12\sum_{e\in E}\gamma_e\|[P_e,X]\|_2^2.
\]
Thus every eigenoperator with purely imaginary eigenvalue commutes with every \(P_e\). Such an operator has block form \(X=\operatorname{diag}(C,B)\) in the \(E\oplus O\) ordering, with \(C\) diagonal and \(B\) arbitrary. Because the adjacency Hamiltonian has only off-diagonal parity blocks, \([H,X]\) is off-diagonal. If \(\mathcal L(X)=i\nu X\) for real \(\nu\), the diagonal-block comparison forces \(\nu=0\) unless \(X=0\). Hence no nonzero imaginary spectral values exist.

**2. Exact fixed algebra.** Write
\[
A=\begin{pmatrix}0&T\\T^\dagger&0\end{pmatrix},\qquad X=\begin{pmatrix}C&0\\0&B\end{pmatrix}.
\]
The condition \([A,X]=0\) is \(TB=CT\) and \(BT^\dagger=T^\dagger C\). It follows that \(C TT^\dagger=TT^\dagger C\). For distinct even vertices \(e,f\), the entry \((TT^\dagger)_{e,f}\) equals two if their Hamming distance is two and zero otherwise. The distance-two graph on even words is connected for all \(d\ge2\). Since \(C\) is diagonal, it must therefore equal \(cI_E\). For \(d=1\) the same conclusion is automatic, since \(E\) contains only one vertex. Substitution yields \(T(B-cI_O)=0\) and \((B-cI_O)T^\dagger=0\), so
\[
B=cI_O+P_{\ker T} Y P_{\ker T}
\]
for an arbitrary operator \(Y\). The subspace \(\ker T\) embedded in the odd coordinates is exactly \(\mathcal D\). Consequently every fixed operator and only such an operator has the form \(c(I-D)+DYD\), with no coupling between bright and dark sectors.

**3. Rank of the dark block.** For each subset \(S\subseteq\{1,\ldots,d\}\), the normalized Walsh character \(\chi_S(x)=2^{-d/2}(-1)^{\sum_{j\in S}x_j}\) is an eigenvector of \(A\) with eigenvalue \(d-2|S|\). Hence \(\ker A=\{0\}\) in odd dimensions, while in even dimensions its dimension is \(\binom d{d/2}\). Multiplication by parity maps \(\chi_S\) to \(\chi_{S^c}\), and this involution pairs distinct zero-mode characters. Each pair contributes one even-supported and one odd-supported zero mode. Thus the odd subspace has precisely \(\binom d{d/2}/2\) independent dark vectors, establishing the formula for \(k_d\).

**4. Actual long-time limit.** The generated completely positive unital semigroup is a contraction in Hilbert–Schmidt norm by step 1. Therefore a nontrivial Jordan block at eigenvalue zero is impossible. Step 1 excludes every other imaginary eigenvalue; all remaining eigenvalues have strictly negative real parts. The limit is the Hilbert–Schmidt orthogonal projection onto the fixed algebra found in step 2. The projection of \(\rho\) is
\[
D\rho D+\frac{\operatorname{Tr}((I-D)\rho)}{2^d-k_d}(I-D).
\]
For a unit-trace initial density matrix, this is the stated formula. In particular the dark *coherences* remain, not just the dark population. This completes the all-initial-state assertion.

**5. Return probability and scale.** Translations by even-weight bit strings preserve \(A\), the parity partition and hence \(D\); they act transitively on \(O\). Therefore the diagonal of \(D\) is constant on \(O\) and equals \(\operatorname{rank}(D)/|O|=k_d/2^{d-1}\); its diagonal vanishes on \(E\). For \(\rho(0)=|v\rangle\langle v|\), the return contribution from \(D\rho(0)D\) is \(p_d^2\), and that from the bright component is \((1-p_d)^2/(2^d-k_d)\). Stirling's formula along even \(d\) gives \(p_d\sim\sqrt{2/(\pi d)}\) and \(k_d=2^{d-1}p_d\); the bright contribution is exponentially small. This proves \(R_d\sim2/(\pi d)\). For odd \(d\), \(D=0\) and the exact limit is maximally mixed.

## Verification
The standalone `verify.py` computes adjacency matrices and the odd-block nullspaces for dimensions \(1\le d\le6\), checks the predicted projector rank, support, orthogonality, and stationarity for positive **inhomogeneous** dephasing rates, and checks all localized return formulas. For \(d\le4\), it also evolves both a localized state and a seeded coherent pure state using the actual Lindblad matrix exponential to time \(t=500\), comparing with the claimed long-time limit. It prints additional central-binomial asymptotic checks for dimensions 20, 40, 100 and 200. Running `python verify.py` requires `numpy` and `scipy` as specified by `requirements.txt`. Numerical checks do not prove the all-dimension theorem; steps 1–5 do.

## Relationship to prior work
Alagić and Russell (arXiv:quant-ph/0501169) study a continuous-time walk on the hypercube with **coordinate-bit** dephasing; their jump observables and tensor-product mixing calculation differ from the present parity-selective rank-one monitoring. Strauch (arXiv:0808.3403) analyzes **all-vertex** dephasing and finds uniform long-time vertex probabilities, whereas exactly half of the vertices are monitored here and the return law exhibits a parity-dependent stationary memory. Baumgartner and Narnhofer (arXiv:0806.3164) give general finite-dimensional Lindblad stationary-state and asymptotic-structure theory. Such abstract principles justify using fixed algebras, but do not state the specific hypercube commutant, its \(\tfrac12\binom d{d/2}\) decoherence-free dimension, or the polynomial return coefficient. Earlier explicit one-dimensional half-dephased weighted cycles have at most one dark vector; their conditions do not imply the unbounded dark multiplicity and return law on hypercubes. Existing hypercube results for localized *absorption* or telegraph Hamiltonian noise employ different generators and observables. The present claim is limited to the explicit partial-site-dephasing hypercube family; no claim of novelty is made for the general fixed-point or Walsh-spectrum facts individually.

## Limitations
The result does not determine relaxation times uniformly in dimension: only the fixed-dimension long-time limit is proved, followed by the dimension asymptotic. Removing the positivity of any monitored rate can enlarge the stationary algebra; adding onsite fields, absorption, or other edges may remove or modify it. Dephasing on the entire even sector via one collective projector is **not** equivalent to the site-resolved jump operators used here. The identified algebraic steps rely on the distance-two connectivity of the hypercube and its Walsh spectrum. Equivalent explicit formulas may exist in specialized literature not captured by the inspected searches.

## References
1. Gorjan Alagić and Alexander Russell, *Decoherence in quantum walks on the hypercube*, first arXiv posting 2005-01-28, arXiv:quant-ph/0501169, https://arxiv.org/abs/quant-ph/0501169.
2. Frederick W. Strauch, *Reexamination of decoherence in quantum walks on the hypercube*, first arXiv posting 2008-08-25, arXiv:0808.3403, https://arxiv.org/abs/0808.3403.
3. Bernhard Baumgartner and Heide Narnhofer, *Analysis of quantum semigroups with GKS–Lindblad generators II. General*, first arXiv posting 2008-06-19, arXiv:0806.3164, https://arxiv.org/abs/0806.3164.
