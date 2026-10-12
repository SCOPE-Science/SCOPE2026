# Sharp quarter-phase four-qubit purity frontier and its single symmetry orbit

## Finding

Consider four-qubit states with equal-magnitude computational amplitudes and fourth-root phases:
\[
|\psi_f\rangle=\frac14\sum_{x\in\{0,1\}^4}i^{f(x)}|x\rangle,
\qquad f:\{0,1\}^4\longrightarrow\mathbb Z_4.
\]
For each of the three inequivalent two-versus-two cuts \(A=12,13,14\), let \(P_A(f)=\operatorname{Tr}(\rho_A^2)\), where \(\rho_A\) is the reduced density operator on \(A\). The exact worst-cut optimum is
\[
\boxed{\min_f\max\{P_{12}(f),P_{13}(f),P_{14}(f)\}=\frac{11}{32}.}
\]
Every optimizer has all three purities equal to \(11/32\), and every single-qubit marginal maximally mixed. Identifying phase functions differing by arbitrary global and local diagonal fourth-root gates, there are exactly \(96\) optimal classes. All \(96\) belong to a single orbit under bit flips, qubit permutations, and complex conjugation. Without complex fourth roots, i.e. for phases restricted to \(\{+1,-1\}\), the sharp optimum is instead \(3/8\).

For each optimal \(f\), the sixteen states
\[
\left\{\left(\bigotimes_{j=1}^{4}Z_j^{a_j}\right)|\psi_f\rangle:a\in\{0,1\}^4\right\}
\]
form a complete orthonormal basis and are mutually locally unitarily equivalent. Thus the same worst-cut entanglement is available at all sixteen outcomes of this projective measurement.

## Assumptions and scope

The computational binary index is \(x=x_1+2x_2+4x_3+8x_4\), for \(x_j\in\{0,1\}\). The phase function is arbitrary with codomain \(\mathbb Z_4\), not necessarily quadratic and not restricted to Clifford circuits. A balanced cut consists of two of the four qubits versus its two-qubit complement. Because the global state is pure, the six labeled two-qubit purities occur in complementary pairs, so the three indicated cuts are complete.

Two functions are phase-gauge equivalent if their difference is \(c+\sum_{j=1}^{4}c_jx_j\pmod4\), with all coefficients in \(\mathbb Z_4\). These are exactly global and local diagonal quarter-phase gates. The subsequent orbit statement additionally allows qubit permutations, local computational-basis bit flips, and global complex conjugation. No equivalence under general local unitaries is asserted.

## Proof

**1. An unrestricted lower bound.** For any pure four-qubit state \(\rho=|\psi\rangle\langle\psi|\), let \(A_k\) be the sum of squares of all Pauli expectation values of exact weight \(k\), with \(A_0=1\). The normalized Pauli expansion yields \(\sum_{k=0}^4A_k=16\). Equality of purities of complementary single- and three-qubit reductions gives \(A_3=12+A_1-2A_2\), and consequently \(A_4=3-2A_1+A_2\).

Define the spin-flipped density operator \(\widetilde\rho=Y^{\otimes4}\rho^*Y^{\otimes4}\) and \(\tau=\operatorname{Tr}(\rho\widetilde\rho)=|\langle\psi|Y^{\otimes4}|\overline\psi\rangle|^2\ge0\). A weight-\(k\) Pauli expectation changes sign by \((-1)^k\) under spin flip. Substitution into the Pauli trace identity gives \(\tau=(A_2-A_1-2)/4\). Since each of the six unordered two-qubit reductions occurs twice among the three complementary pairs, the same Pauli expansion gives
\[
P_{12}+P_{13}+P_{14}=\frac34+\frac{3A_1+A_2}{8}
=1+\frac{A_1+\tau}{2}\ge1.
\]
This is a standard four-qubit inversion/monogamy identity, here reconstructed to make the numerical lower bound independent of an external lemma. Hence for every pure four-qubit state at least one balanced-cut purity is at least \(1/3\).

**2. Quarter-phase quantization.** On any balanced cut, reshape the sixteen unnormalized phase entries into a \(4\times4\) matrix \(M_A\) with entries from \(\{1,i,-1,-i\}\). Then \(\rho_A=M_AM_A^\dagger/16\) and
\[
256P_A=64+2\sum_{0\le r<s<4}\left|\sum_{c=0}^{3}(M_A)_{rc}\overline{(M_A)_{sc}}\right|^2.
\]
Each inner sum consists of four fourth roots. Its real and imaginary parts are integers of equal parity, so its squared magnitude is an even integer. Thus \(256P_A\) is divisible by \(4\), or \(P_A\in\frac1{64}\mathbb Z\). Combining this discreteness with the preceding \(1/3\) bound gives
\[
\max_A P_A\ge\frac{\lceil64/3\rceil}{64}=\frac{11}{32}.
\]

**3. Attainment.** One witness, specified by its complete phase vector in increasing computational index, is
\[
(f(0),\ldots,f(15))=(0,0,0,1,0,2,3,3,0,1,0,3,3,1,1,0).
\]
For each cut, the six squared magnitudes of distinct unnormalized row inner products of \(M_A\) are a permutation of \((0,2,2,2,2,4)\). Their sum is \(12\), hence \(256P_A=64+24=88\) for all three cuts. Therefore \(P_A=11/32\), matching the lower bound. Directly, for each qubit \(j\), the eight-term off-diagonal coherence sum \(\sum_{x:x_j=0}i^{f(x)-f(x\oplus e_j)}\) vanishes; the diagonal populations are equal. Thus the witness is one-uniform.

**4. Complete equality classification.** Subtract a unique affine phase \(c+\sum_{j=1}^4c_jx_j\) to impose \(f(0)=f(1)=f(2)=f(4)=f(8)=0\). Exactly eleven phase digits remain free, so this exhaustively and without duplication represents all \(4^{11}=4,194,304\) gauge classes. For each one, the preceding exact integer Gram formula computes all three purities, with no floating point or optimization heuristic. The included standalone C++17 verifier enumerates every eleven-digit base-four index and checks that precisely \(96\) gauge classes have worst-cut numerator \(88\) (when purities are scaled by \(256\)), and every one has the triple \((88,88,88)\). The verifier then generates the orbit of one such class under all \(24\) qubit permutations, \(16\) local bit-flip patterns, and conjugation, canonicalizing after every transformation; the resulting distinct set contains exactly those \(96\) classes. It also exhausts all \(2^{11}\) real-sign gauge classes and returns sharp numerator \(96\), equivalent to \(3/8\).

A separate pure-Python standard-library checker computes the Gram matrices by complex arithmetic rather than the integer phase-difference routine, verifies the representative and every distinct orbit point, checks all four one-qubit coherences, and independently checks the real-sign optimum. Thus every quarter-phase optimizer is one-uniform because all are in the orbit of the one-uniform witness and all allowed orbit operations preserve one-uniformity.

**5. The sixteen-state measurement basis.** For \(a,b\in\{0,1\}^4\), the overlap of the local \(Z\)-encoded vectors is
\[
\langle\psi_f|Z^{a\oplus b}|\psi_f\rangle
=\frac1{16}\sum_{x\in\{0,1\}^4}(-1)^{(a\oplus b)\cdot x}
=\begin{cases}1,&a=b,\\0,&a\ne b.\end{cases}
\]
There are sixteen such mutually orthogonal unit vectors in a sixteen-dimensional space, and their encoders are local unitaries, proving the claimed projective basis and equal cut-entanglement properties.

## Verification

Compile the embedded \(\texttt{verify.cpp}\) with any C++17 compiler and run its executable. It exhausts \(4,194,304\) gauge representatives, checks exact divisibility and all three Gram purities, compares the complete optimizer set with the generated symmetry orbit, and independently enumerates the \(2,048\) real-sign representatives. A second checker \(\texttt{verify_independent.py}\) uses only the Python standard library and calculates the actual complex Gram matrices and spin-flip overlap for the representative and the entire orbit.

The exact required outputs include \(\texttt{optimum=88/256}\), \(\texttt{canonical\_minimizers=96}\), \(\texttt{one\_symmetry\_orbit=96}\), and \(\texttt{real\_optimum=96/256}\). These finite exhaustive checks certify the finite classification; the unrestricted lower bound and gauge reduction have separate analytic proofs above. The main numerical witness also follows from the displayed six Gram-overlap squares.

## Relationship to prior work

Pauwels and Gühne, arXiv:2608.21185v1, develop the notion of equal-entanglement quantum measurement bases and characterize independent local encodings of flat states, as well as an unrestricted, highly entangled four-qubit basis. Consequently the fact that *some* local \(Z\) encoding produces a basis from a flat state is not new here. The new result is the sharp discrete **worst balanced-cut purity** frontier for the physical fourth-root phase alphabet and its exhaustive orbit classification.

Gour and Wallach, arXiv:1006.0036v2, determine universal four-qubit average linear-entanglement bounds and characterize global extrema; the general \(1/3\) average-purity bound and four-tangle identity above are known in substance. Those bounds do not select the quarter-phase constrained optimum \(11/32\) or count its optimizers. Chen and Wang, arXiv:1409.0928v1, classify four-qubit hypergraph states with real \(\pm1\) amplitudes and discuss their multipartite entanglement; that restriction does not include the phase alphabet \(\{1,i,-1,-i\}\).

## Limitations

The classification is finite and exact for four qubits only. It is not an optimization over arbitrary complex phases, arbitrary amplitudes, all local-unitary equivalence classes, higher party numbers, noisy-state entanglement, or gate-depth cost. The \(96\)-class census is computationally exhaustive but the orbit count is not separately reduced to a closed symbolic group-theoretic classification. The closed lower bound alone is known from earlier global entanglement theory; novelty relies on the discrete attaining constructions and complete constrained equality classification. An unindexed equivalent discrete-phase optimization remains a possible overlap risk.

## References

1. J. Pauwels and O. Gühne, *The Entanglement Content of Quantum Measurement Bases*, arXiv:2608.21185v1 (first public 21 August 2026), https://arxiv.org/abs/2608.21185.
2. G. Gour and N. R. Wallach, *All Maximally Entangled Four Qubits States*, arXiv:1006.0036v2, https://arxiv.org/html/1006.0036v2.
3. X.-Y. Chen and T.-C. Wang, *Locally inequivalent four qubit hypergraph states*, arXiv:1409.0928v1, https://arxiv.org/html/1409.0928v1.
