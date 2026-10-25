# Exact survival-time operator and sink-rate optimization on finite quantum paths

## Finding
Let a coherent nearest-neighbor quantum walker occupy the path of \(N\ge 2\) sites, with hopping amplitude \(J>0\) and one Lindblad sink of rate \(\kappa>0\) at site \(1\). The following gives **every entry** of the operator representing expected time until irreversible absorption, including coherent interference between distinct initial sites.

Set \(b_j=N+1-j\) and \(a_i=i/\kappa+(i-1)\kappa/(4J^2)\). For \(1\le i\le j\le N\), the Hermitian survival-time operator \(Q\) has exact entries
\[
Q_{ij}=\begin{cases}
a_i b_j,& j-i\text{ even},\\
-\mathrm{i}\,b_j/(2J),& j-i\text{ odd},
\end{cases}
\qquad Q_{ji}=\overline{Q_{ij}}.
\]
For every unit vector \(c\in\mathbb C^N\), its mean absorption time is \(\mathbb E_c[T]=c^*Qc\). The same identity extends by trace to any initial density matrix \(\rho\) on the chain: \(\mathbb E_\rho[T]=\operatorname{Tr}(Q\rho)\).

In particular, for a localized initial state at site \(m\),
\[
\mathbb E_m[T]=(N+1-m)\left(\frac{m}{\kappa}+\frac{(m-1)\kappa}{4J^2}\right).
\]
For every \(m\ge 2\), the unique globally optimal loss strength is
\[
\kappa_*(m)=2J\sqrt{\frac{m}{m-1}},\qquad
\min_{\kappa>0}\mathbb E_m[T]=\frac{N+1-m}{J}\sqrt{m(m-1)}.
\]
Thus the optimal sink rate depends on the injection site but **not on the length of the chain added beyond that site**. For \(m=1\), the mean is \(N/\kappa\) and has no finite positive minimizer.

## Assumptions and scope
Use the Hilbert space \(\mathbb C^N\) with orthonormal site vectors \(e_1,\ldots,e_N\). Let the closed-system Hamiltonian have equal on-site energies and uniform nearest-neighbor hopping \(-J\); a common on-site energy only supplies a global phase. In units with \(\hbar=1\), the sink jump is \(\sqrt\kappa\,|\emptyset\rangle\langle e_1|\), and there is no bulk dephasing, disorder, other loss or driving. Absorption removes the particle permanently. For the path adjacency matrix \(A\), the unnormalized surviving-state amplitude evolves under
\[
L=\mathrm{i}JA-\frac\kappa2e_1e_1^*,\qquad \psi(t)=e^{Lt}c.
\]
The survival probability is \(S_c(t)=\|\psi(t)\|_2^2\). The absorption-time law has density \(-S_c'(t)=\kappa|\langle e_1,e^{Lt}c\rangle|^2\). All assertions hold for every integer \(N\ge2\), every \(J,\kappa>0\), and every normalized initial state specified above.

## Proof
**Strict decay and existence.** If \(Lv=\lambda v\) for a nonzero eigenvector, taking real parts gives \(2\operatorname{Re}\lambda\,\|v\|^2=-\kappa|v_1|^2\). An eigenvalue on the imaginary axis would force \(v_1=0\), then the first component of \(Lv=\lambda v\) forces \(v_2=0\), and induction along the path forces \(v=0\), a contradiction. Every eigenvalue therefore has strictly negative real part; this also handles non-diagonalizable matrices. Consequently \(Q=\int_0^\infty e^{L^*t}e^{Lt}\,dt\) converges, is positive definite, and is the unique solution of
\[
L^*Q+QL=-I_N.
\]
Integration of \(S_c(t)\), or integration of the absorption density by parts, now shows \(\mathbb E_c[T]=c^*Qc\), with normalization of the absorbed probability to one.

**Exact solution of the Lyapunov equation.** Define \(b_j=N+1-j\) and \(a_i=i/\kappa+(i-1)\kappa/(4J^2)\), and define a Hermitian candidate \(Q\) by the parity rule in the Finding. Entries outside the index interval are treated as zero. Direct matrix multiplication yields
\[
(L^*Q+QL)_{ij}=\mathrm{i}J(Q_{i,j-1}+Q_{i,j+1}-Q_{i-1,j}-Q_{i+1,j})
-\frac\kappa2(\delta_{i1}Q_{1j}+Q_{i1}\delta_{j1}).
\]
For \(1<i<j\), the off-diagonal expression vanishes. When \(j-i\) is even, the four neighboring entries contain the same imaginary linear function of \(b_j\); when \(j-i\) is odd, cancellation is the discrete affine identity \(a_{i-1}+a_{i+1}=2a_i\). The neighboring case \(j=i+1\) obeys the same identities, with the diagonal formula used at the touching terms. At the right boundary, \(b_{N+1}=0\) gives precisely the missing-neighbor terms. For \(i=1<j\), the residual of the commutator is exactly \(\kappa Q_{1j}/2\), canceled by the sink term; this follows from \(a_2-2a_1=\kappa/(4J^2)\) and \(a_1=1/\kappa\). For \(2\le i\le N\), the diagonal commutator equals \(-1\). At \(i=1\), its value is \(N-1\), while the sink contributes \(-\kappa Q_{11}=-N\), leaving \(-1\). The lower triangle follows by taking adjoints. Hence \(L^*Q+QL=-I_N\) holds entrywise for every \(N\), and uniqueness gives the claimed operator.

**Optimization.** Taking the \(m\)-th diagonal yields the displayed scalar formula. For \(m\ge2\) its derivative in \(\kappa\) vanishes only at \(\kappa=2J\sqrt{m/(m-1)}\); its strictly positive second derivative, together with divergence at both endpoints, makes this the unique global minimizer. Substitution gives the minimum. The case \(m=1\) is monotone. The length-independence of the optimizer follows because \(N+1-m\) is a positive multiplicative factor in the objective.

## Verification
The accompanying standalone `verify.py` constructs the candidate operator and the generator independently, checks the Lyapunov residual and direct SciPy solution over dimensions \(2\) to \(15\), tests all localized diagonal formulas, compares four survival integrals against the exact result, and checks the optimization at many injection sites and chain lengths. Run `python verify.py` with NumPy and SciPy. The deterministic suite passes 1,309 numerical assertions. These tests supplement, but are not substitutes for, the entrywise proof for all dimensions.

## Relationship to prior work
Riberi's May 2026 continuous-time absorbing quantum walk uses a Lindblad boundary sink on the **semi-infinite** path, derives an exact propagator and first-passage statistics, and analyzes boundary-localized loss modes. The present result is for a **finite** uniform path and gives the complete integrated survival-time matrix in every dimension; it does not reproduce the semi-infinite propagator.

Earlier, Zhang, Celardo, Borgonovi and Kaplan (2017) studied finite coherent transport to a terminal sink. Their equation (17) **already gives** the clean end-to-end initial-state special case \(N/\kappa+(N-1)\kappa/(4J^2)\), and their equation (33), at zero dephasing, gives the three-site middle-injection case. Both cases are excluded from the novelty claim. The new contribution assessed here is the explicit **all-initial-coherences** mean-lifetime operator, with the all-size interior injection formula and its exact sink-rate optimizer; it is not implied by either of those reported special-case formulas alone. General finite-dimensional Lyapunov methods are classical and are not claimed as new.

## Limitations
The result is exact only for the stated homogeneous path, a single terminal Lindblad loss, no other decoherence, and finite size. It does not give the full absorption-time distribution or its variance. It makes no inference about mean absorption on a semi-infinite path, for which incomplete absorption can occur. The priority assessment is provisional: a more general coherent-transport result may imply the displayed matrix entries without matching their explicit wording. No independent audit has yet been performed.

## References
1. F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, arXiv:2605.08056v1, first posted 2026-05-08; subsequently titled *Boundary-localized non-Hermitian modes in an absorbing quantum walk*, arXiv:2605.08056v4. https://arxiv.org/abs/2605.08056
2. Y. Zhang, G. L. Celardo, F. Borgonovi and L. Kaplan, *Optimal Dephasing for Ballistic Energy Transfer in Disordered Linear Chains*, Physical Review E 96 (2017), 052103, arXiv:1706.09524, especially equations (17) and (33). https://arxiv.org/abs/1706.09524
