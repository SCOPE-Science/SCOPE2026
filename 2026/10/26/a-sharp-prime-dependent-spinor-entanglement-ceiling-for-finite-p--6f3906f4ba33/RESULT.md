# A sharp prime-dependent spinor entanglement ceiling for finite \(p\)-adic Dirac walks

## Finding
For every prime \(p\), depth \(\ell\ge1\), radial nonnegative integrable hopping kernel, mass \(m\ge0\), and real time \(t\), a one-coordinate finite \(p\)-adic Dirac walk initialized in one spinor component at one position has spinor–position entanglement entropy
\[
0\le S(t)\le h_2(1/p),\qquad h_2(q)=-q\log_2q-(1-q)\log_2(1-q).
\]
The inequality is sharp at every depth, even when **every distinct pair of vertices has strictly positive hopping**. Consequently, one full ebit is accessible for \(p=2\) but impossible for every odd prime in this specified walk family. For zero mass an exact character formula and a necessary and sufficient phase-alignment criterion describe all entropy maximizers.

## Assumptions and scope
Fix a prime \(p\), integer \(\ell\ge1\), and let \(G_\ell=\mathbb Z/p^\ell\mathbb Z\), \(N=p^\ell\). The finite hopping operator \(A_\ell\) is a translation-invariant symmetric, radial convolution-minus-identity operator: for \(x\ne y\),
\[
(A_\ell)_{xy}=N^{-1}K(|x-y|_p)\ge0,\quad (A_\ell)_{xx}=-\sum_{y\ne x}(A_\ell)_{xy},
\]
where \(K\) is nonnegative, integrable, supported on \(\mathbb Z_p\), and radial. We write \(|x-y|_p\) using any representatives; it is well defined off the diagonal. The precise normalization may equivalently be specified by arbitrary nonnegative radial off-diagonal weights; the assertion does not require irreducibility unless stated in the sharpness construction.

On \(\mathbb C^2\otimes\ell^2(G_\ell)\), set
\[
H_{m,\ell}=m\sigma_z\otimes I_N+\sigma_x\otimes A_\ell.
\]
Initialize \(|\Psi(0)\rangle=|\uparrow\rangle\otimes|0\rangle\), evolve unitarily, and let \(S(t)=-\operatorname{Tr}(\rho_s(t)\log_2\rho_s(t))\) be the base-two von Neumann entropy of the reduced two-component spinor. This is the invariant two-spinor block of the finite three-coordinate Dirac construction when the second and third directional operators vanish; **the theorem does not concern general three-direction couplings or all possible initial states**. Translation invariance permits any localized initial vertex.

Let \(a_j\in\mathbb R\), \(j=0,\ldots,\ell\), denote the eigenvalue of \(A_\ell\) on characters of exact conductor \(p^j\), where \(a_0=0\). The multiplicity is \((p-1)p^{j-1}\) for \(j\ge1\); the maximal conductor \(j=\ell\) comprises exactly \((p-1)/p\) of the Fourier basis.

If \(m=0\), the entropy has the closed formula
\[
F_\ell(t)=\frac{e^{-2it a_0}+\sum_{j=1}^{\ell}(p-1)p^{j-1}e^{-2it a_j}}{p^\ell},\qquad
S(t)=h_2\!\left(\frac{1+|F_\ell(t)|}{2}\right).
\]
Equality with \(h_2(1/p)\) holds **if and only if**
\[
2t(a_j-a_\ell)\equiv\pi\pmod {2\pi}\qquad (j=0,1,\ldots,\ell-1).
\]
For \(t=0\), the condition cannot hold, consistently giving zero entanglement.

## Proof
Characters \(\chi_k(x)=e^{2\pi ikx/N}\) diagonalize \(A_\ell\). For \(k\ne0\), the character conductor is \(p^{\ell-v_p(k)}\). The radiality of \(K\) implies that the Fourier transform of each valuation shell depends only on the conductor, so all characters with \(p\nmid k\) share the same eigenvalue \(a_\ell\). Their number is \(N-N/p\); their total probability weight in the Fourier transform of the spatial point mass is \(w=1-1/p\).

In the Fourier representation the state is
\[
|\Psi(t)\rangle=N^{-1/2}\sum_{k\in G_\ell} e^{-it(m\sigma_z+a_{j(k)}\sigma_x)}|\uparrow\rangle\otimes|\chi_k\rangle.
\]
By orthogonality of the characters the spinor reduction is a convex combination of pure qubit states. The maximal-conductor terms are identical and therefore give
\[
\rho_s(t)=w|\phi_\ell(t)\rangle\langle\phi_\ell(t)|+(1-w)\tau(t),
\]
where \(\tau\) is another qubit density matrix. The Rayleigh quotient on \(|\phi_\ell\rangle\) gives \(\lambda_{\max}(\rho_s)\ge w\ge1/2\). For qubits the entropy equals \(h_2(\lambda_{\max})\), which is decreasing on \([1/2,1]\). Hence \(S(t)\le h_2(w)=h_2(1/p)\). This proof works for arbitrary mass and any radial nonnegative generator, including kernels with zero edges.

For zero mass, in the \(\sigma_x\) eigenbasis the initial up-spin is the balanced sum of the two eigenvectors. The two spin components in this basis acquire opposite character phases. Their reduced diagonal entries are both \(1/2\), and the off-diagonal magnitude is \(|F_\ell(t)|/2\), proving the exact formula. Separate the common highest-conductor phase from the others:
\[
F_\ell(t)=\frac{p-1}{p}e^{-2ita_\ell}+\frac1{p^\ell}\sum_{j=0}^{\ell-1}m_j e^{-2ita_j},
\]
with \(m_0=1\) and \(m_j=(p-1)p^{j-1}\) otherwise. The reverse triangle inequality gives \(|F_\ell(t)|\ge(p-2)/p\). Equality requires the smaller phase sum to have its maximum possible modulus \(1/p\) and to point opposite to the highest phase. Since all smaller weights are strictly positive, this happens precisely when all their unit phases coincide opposite the highest phase, which is the stated congruence (also valid at \(p=2\), where both weights are equal).

For sharpness, fix any \(g>0\) and select the following radial nonnegative integrable kernel on \(\mathbb Q_p\):
\[
K_\ell(y)=2g\,\mathbf1_{\mathbb Z_p}(y)+p^{\ell-1}g\,\mathbf1_{\{|y|_p=p^{-(\ell-1)}\}}(y).
\]
The finite convolution weights then have a uniform off-diagonal contribution \(2g/N>0\), so their associated graph is complete, with all rates positive. The uniform component has Fourier eigenvalue \(0\) for the trivial character and \(-2g\) for each nontrivial character. The extra smallest nonzero-radius shell consists, modulo \(p^\ell\), of residues \(p^{\ell-1}u\) with \(u=1,\ldots,p-1\), each weighted \(g/p\). Its eigenvalue contribution is \(0\) for \(p\mid k\), and
\[
\frac gp\left(\sum_{u=1}^{p-1}e^{2\pi iku/p}-(p-1)\right)=-g
\]
for \(p\nmid k\). Thus \(a_0=0\), \(a_j=-2g\) for \(1\le j<\ell\), and \(a_\ell=-3g\). At mass zero and time \(t=\pi/(2g)\), all the low-conductor phases equal \(+1\), and the high-conductor phase equals \(-1\). Accordingly the two nonzero eigenvalues of the reduced density matrix are exactly \(1/p\) and \((p-1)/p\), attaining the bound. At depth \(\ell=1\), the middle eigenvalue class is empty and the calculation still holds. For any fixed \(m>0\), scaling \(g\to\infty\) at time \(\pi/(2g)\) makes the mass term negligible in each finite Fourier two-by-two block, so the same ceiling is the sharp supremum in that mass class.

## Verification
The companion standard-library script `verify.py` directly forms finite positional matrices, computes Fourier spectra and spinor reduced density matrices from truncated exponential series, tests the closed formula on independently chosen radial weights, checks strictly positive edges, and checks massive and massless instances. Running `python3 verify.py` produced `VERIFICATION_OK 178 finite checks; arbitrary-depth proof is analytic`. Finite calculations do not certify universal quantifiers: those are established by the character and qubit arguments above.

## Relationship to prior work
Zúñiga-Galindo's 2026 construction supplies finite \(p\)-adic Dirac quantum walks and identifies characterization of spinor–position entanglement as an open direction; its equations specify the radial Markov-type directional generator. The present work supplies an exact sharp entanglement ceiling for the **one-coordinate invariant block**, a massless entropy formula, equality conditions, and a connected-kernel construction. It does not claim novelty of Fourier diagonalization, of the binary-entropy inequality, or of the general Dirac model. Konno's earlier ultrametric quantum-walk work studies scalar position localization and time-averaged position probabilities, not this reduced spinor state. General coin–position entanglement results for discrete-time walks employ different dynamics and do not establish this prime-dependent ceiling from conductor multiplicity. A more general uninspected representation-theoretic entanglement theorem might subsume this result.

## Limitations
The initial position must be a delta state and the initial spinor is the specified component in the invariant two-dimensional block; general four-component spinor states, anisotropic three-direction coupling, external potentials or nonradial kernels are not covered. The equality classification is for zero mass. With fixed positive mass only the ceiling and sharp-supremum construction are proved, not exact finite-coupling saturation. Numerical checks cover finitely many primes, depths and times and are separate from the analytic theorem. Priority is assessed relative to inspected literature and is not independently certified.

## References
1. W. A. Zúñiga-Galindo, *p-Adic Dirac Equations, Continuous-Time Quantum Walks, and Quantum Networks*, arXiv:2609.04358v1, first submitted September 3, 2026. https://arxiv.org/abs/2609.04358 (finite spatial approximation, radial generators, and entanglement question).
2. N. Konno, *Continuous-time quantum walks on ultrametric spaces*, arXiv:quant-ph/0602070, 2006, https://arxiv.org/abs/quant-ph/0602070 (scalar ultrametric transport and time-averaged localization; distinct observable).
3. Standard finite Fourier character orthogonality and elementary qubit entropy identities are derived as needed above and require no external specialized results.
