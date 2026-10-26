# Exact quantum-memory capacity and sharp spectral decay for Haar-coined Abelian walks

## Finding
Let \(G\) be a finite Abelian group of cardinality \(N\ge3\) and let \(S=S^{-1}\subseteq G\setminus\{e\}\) be a generating set of cardinality \(d\ge2\). On a \(d\)-state coin and an \(N\)-state position register, consider the independent-Haar-coin, conditional-translation averaged channel \(\mathcal F\) defined below. The output comprises **both** registers and the realization of each random coin is unavailable. Let \(\mu\) be uniform on \(S\), let \(p_t=\mu^{*t}\) with \(p_0=\delta_e\), and write \(H_2\) for Shannon entropy in bits.

**Exact capacity.** For every integer \(m\ge1\), the unassisted, asymptotic quantum communication capacity per independent use of the \(m\)-step channel is
\[
Q(\mathcal F^m)=\log_2 N-H_2(p_{m-1}). \tag{1}
\]
The exponent \(m-1\), rather than \(m\), is essential: the receiver has the final coin flag and can undo the last controlled translation. If that flag is discarded, the induced position-only channel instead uses \(p_m\).

**Period and sharp spectral law.** Let \(h=2\) precisely when there is a character \(\eta\in\widehat G\) with \(\eta(s)=-1\) for every \(s\in S\), and let \(h=1\) otherwise. Equivalently, \(h=2\) exactly when the Cayley graph is bipartite. Set \(\Xi=\{\mathbf1\}\) for \(h=1\), and \(\Xi=\{\mathbf1,\eta\}\) for \(h=2\). Define
\[
\lambda_\chi=\frac1d\sum_{s\in S}\chi(s)\in[-1,1],\qquad
r=\max_{\chi\notin\Xi}|\lambda_\chi|,
\]
with \(r=0\) if \(\widehat G\setminus\Xi\) is empty. Connectivity ensures \(r<1\). If \(0<r<1\), let \(M=\#\{\chi\notin\Xi:|\lambda_\chi|=r\}\). Then
\[
\boxed{\lim_{m\to\infty}
\frac{Q(\mathcal F^m)-\log_2 h}{r^{2(m-1)}}
=\frac{M}{2h\ln 2}.} \tag{2}
\]
In particular, the residual capacity is exactly \(\log_2 h\): it approaches **zero** on aperiodic graphs and **one qubit** on bipartite graphs. For \(r=0\), the capacity equals \(\log_2 h\) for every \(m\ge2\); (2) is not asserted.

**Hypercube specialization.** For \(G=(\mathbb Z/2\mathbb Z)^d\) and the \(d\) unit-vector generators, \(d\ge3\), formula (2) reads
\[
Q(\mathcal F^m)=1+\frac{d}{2\ln 2}
\left(1-\frac2d\right)^{2(m-1)}
+o_d\!\left(\left(1-\frac2d\right)^{2(m-1)}\right). \tag{3}
\]
The capacity is strictly above one qubit at every finite depth. In dimension \(d=2\), it is exactly one qubit for all \(m\ge2\).

## Assumptions and scope
Write \(L_g|x\rangle=|gx\rangle\) for the regular translation on \(\mathbb C[G]\), and index a standard orthonormal coin basis by \(s\in S\). Define the conditional unitary and its Haar average by
\[
U_S=\sum_{s\in S}|s\rangle\langle s|\otimes L_s,
\qquad
\mathcal F(\rho)=U_S\left(\frac{I_d}{d}\otimes\operatorname{Tr}_{\rm coin}\rho\right)U_S^\dagger.
\]
At every elementary time step a fresh, independent Haar-distributed unitary on the *entire* coin is drawn before the conditional translation and averaged out; no outcome recording these choices is supplied to the receiver. All logarithms of capacities and entropies are base two unless written \(\ln\). The quantum capacity \(Q(\mathcal F^m)\) means the standard unassisted quantum capacity of this fixed finite-dimensional CPTP map when many independent uses of the entire \(m\)-step experiment are available. It is **not** a capacity rate per elementary walk step, a one-shot capacity, or a capacity conditioned on knowledge of the Haar draw. The Cayley graph is simple and connected because \(e\notin S\) and \(S\) generates \(G\).

## Proof
**1. Remove the final coin flag.** Let
\[
\mathcal T(\sigma)=\frac1d\sum_{s\in S}L_s\sigma L_s^\dagger.
\]
By partial tracing the output of the preceding conditional shift, \(\operatorname{Tr}_{\rm coin}\mathcal F(\rho)=\mathcal T(\operatorname{Tr}_{\rm coin}\rho)\). Inductively, for each integer \(m\ge1\),
\[
\mathcal F^m(\rho)=U_S\left(\frac{I_d}{d}\otimes\mathcal T^{m-1}(\operatorname{Tr}_{\rm coin}\rho)\right)U_S^\dagger. \tag{4}
\]
A receiver-side application of \(U_S^\dagger\) produces a fixed coin state and \(\mathcal T^{m-1}\) on the vertex input. Conversely, a sender may encode any desired vertex input with a fixed coin state. The two channels therefore simulate each other up to preparation or discarding of a fixed ancillary register, which proves \(Q(\mathcal F^m)=Q(\mathcal T^{m-1})\).

**2. Exact capacity of the convolution channel.** Commutativity of regular translations gives
\[
\mathcal T^t(\sigma)=\sum_{g\in G}p_t(g)L_g\sigma L_g^\dagger. \tag{5}
\]
In the character basis \(\{|\chi\rangle:\chi\in\widehat G\}\), each \(L_g\) acts diagonally with unit-modulus eigenvalue \(\chi(g)\) (or its conjugate, depending on Fourier convention), so (5) is a generalized dephasing channel. A Stinespring isometry is
\[
V_t|\chi\rangle=|\chi\rangle\otimes|v_\chi\rangle,
\qquad
|v_\chi\rangle=\sum_{g\in G}\sqrt{p_t(g)}\,\chi(g)|g\rangle.
\]
Its complementary channel measures the Fourier diagonal and prepares \(|v_\chi\rangle\langle v_\chi|\). As the Fourier diagonal is preserved by \(\mathcal T^t\), a Fourier-basis measurement and conditional preparation degrade the output to the complement. Hence the channel is degradable, and its unassisted quantum capacity is the maximum of the single-use coherent information, using the standard degradable-channel coding theorem.

The coherent information is concave in the input state for degradable channels. It is invariant under both phase multiplication in the Fourier basis and translation of Fourier indices: the latter conjugates each \(L_g\) by a scalar and induces only a diagonal unitary on the environment. Twirling a state over these two finite unitary groups yields \(I_N/N\), so this maximally mixed state maximizes coherent information. The system output has entropy \(\log_2N\). At \(I_N/N\), orthogonality \(\operatorname{Tr}(L_g^\dagger L_{g'})=N\delta_{g,g'}\) makes the environment state diagonal with eigenvalues \(p_t(g)\), whose entropy is \(H_2(p_t)\). Thus \(Q(\mathcal T^t)=\log_2N-H_2(p_t)\), proving (1), including \(t=0\).

**3. Identify the period.** Symmetry \(S=S^{-1}\) makes every \(\lambda_\chi\) real. Convexity of averaging points on the unit circle shows that \(\lambda_\chi=1\) only for the trivial character, since \(S\) generates \(G\). Similarly, \(\lambda_\chi=-1\) exactly when \(\chi(s)=-1\) for all \(s\in S\), and any such character is unique because its values on a generating set determine it. Its kernel has index two, yielding the graph's bipartition. Therefore all eigenvalues outside \(\Xi\) have modulus strictly less than one.

By Fourier inversion, \(p_t(g)=N^{-1}\sum_{\chi\in\widehat G}\lambda_\chi^t\overline{\chi(g)}\). Define \(C_t=G\) when \(h=1\); when \(h=2\), define \(C_t=\{g:\eta(g)=(-1)^t\}\). Every step distribution is supported in \(C_t\). Let \(u_t\) be uniform on \(C_t\). The terms from \(\Xi\) give exactly \(u_t\), so \(p_t\to u_t\) in total variation. Since \(|C_t|=N/h\), (1) yields the limiting capacity \(\log_2 h\).

**4. Calculate the sharp coefficient.** On \(C_t\), write \(p_t(g)=u_t(g)(1+\delta_t(g))\). The finite Fourier expansion bounds \(\max_{g\in C_t}|\delta_t(g)|=O_G(r^t)\). The character restrictions to \(C_t\), indexed modulo multiplication by \(\Xi\), form an orthonormal system. The eigenvalues of paired characters differ by the same parity sign as their restriction, so their contributions add rather than cancel. Parseval gives the *exact* identity
\[
\frac1{|C_t|}\sum_{g\in C_t}\delta_t(g)^2
=\frac1h\sum_{\chi\notin\Xi}|\lambda_\chi|^{2t}. \tag{6}
\]
The mean of \(\delta_t\) is zero. For \(r>0\), Taylor's theorem for \((1+z)\ln(1+z)\), uniformly in \(|z|\le1/2\), implies
\[
\log_2|C_t|-H_2(p_t)=\frac1{2\ln2}\frac1{|C_t|}\sum_{C_t}\delta_t^2+O_G(r^{3t}). \tag{7}
\]
The finite sum in (6) is \((M/h)r^{2t}+o(r^{2t})\), proving (2). If \(r=0\), all eigenvalues outside \(\Xi\) vanish and Fourier inversion gives \(p_t=u_t\) for all \(t\ge1\).

**5. Evaluate the hypercube.** Its Walsh characters are labelled by subsets of \(\{1,\ldots,d\}\), with eigenvalues \(1-2j/d\) at subset size \(j\). The trivial and all-coordinate characters give \(1,-1\), so \(h=2\). For \(d\ge3\), the largest remaining modulus is \(r=1-2/d\) and it occurs at the \(d\) singleton and \(d\) co-singleton characters, giving \(M=2d\). Substitution into (2) proves (3). At finite positive \(t\), the distribution cannot equal the uniform parity-class distribution because its singleton Walsh coefficient is \(r^t>0\); the strict positivity of relative entropy gives \(Q(\mathcal F^m)>1\). For \(d=2\), the remaining two Walsh eigenvalues are zero, and the \(r=0\) case applies.

## Verification
The accompanying standard-library script `verify.py` independently iterates the classical walk, reconstructs its distribution by a Walsh Fourier inversion, checks the one-step final-coin identity on small complex density matrices, tests the parity support and entropy, and compares the sharp asymptotic coefficient numerically for several hypercubes. It also checks non-hypercube even and odd cycles. The script reports `CHECKS_PASSED_FINAL 7417` on Python 3. Finite numerical checks do not establish the capacity coding theorem, the infinite-depth limit, or the complete general-group assertion; those follow from the analytical steps above and the stated standard coding theorem.

## Relationship to prior work
Quillen [1] introduces and explicitly derives the Haar-coin averaged channel (especially equations (20)–(23)) and its Fourier eigenstructure on cycles, hypercubes, and finite Abelian Cayley graphs (Section IV). In particular, the existence of persistent Fourier coherence on bipartite examples is established there. These are premises, **not new discoveries here**. Brádler, Hayden, Touchette and Wilde [2] supply the general degradable/Hadamard framework and single-letter capacity machinery for generalized dephasing channels. Consequently, the abstract dephasing capacity principle itself is also **not claimed new**. The specific result evaluated here is the exact, coin-inclusive finite-depth quantum-memory capacity of Quillen's physical channel, together with the all-graph sharp spectral-multiplicity coefficient, exact bipartite residual capacity, and hypercube decay constant. These require a concrete final-coin channel equivalence, a convolutional noise-entropy evaluation, and parity-coset Fourier analysis. No claim is made that the theorem is independent of the general dephasing theory.

## Limitations
The averaging is over fresh independent Haar coins at every step, with no classical record available to the sender or receiver. The receiver retains both the coin and position registers. The group is finite Abelian, the graph is undirected and connected, and the coin is fully depolarized by averaging. The limit fixes the graph while the number of elementary steps grows; the asymptotic constant is not uniform in graph size. The capacity is an asymptotic many-copy communication rate per invocation of the entire depth-\(m\) channel, not a single-shot success probability or a per-step rate. Results for particular noisy physical implementations, correlated coin randomness, non-Abelian groups, or quenched single-trajectory channels are not implied. General dephasing capacity theory already contains much of the channel-theoretic machinery; an unlocated earlier specialization or general entropy-decay coefficient theorem could reduce the priority of the explicit formulas. Independent validation of novelty and proof has not been performed.

## References
[1] A. C. Quillen, *Quantum random walks on d-regular graphs with Haar-random coin operators*, arXiv:2607.04584, first public version 6 July 2026, sections III–IV. https://arxiv.org/abs/2607.04584

[2] K. Brádler, P. Hayden, D. Touchette and M. M. Wilde, *Trade-off capacities of the quantum Hadamard channels*, arXiv:1001.1732 (2010), especially sections II.3.2–II.3.3 and IV. https://arxiv.org/abs/1001.1732
