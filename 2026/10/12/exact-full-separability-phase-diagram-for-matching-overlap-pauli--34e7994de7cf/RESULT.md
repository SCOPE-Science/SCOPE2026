# Exact full-separability phase diagram for matching-overlap Pauli Gibbs states
## Finding
Let \(H=\sum_i J_iP_i\) be a finite \(n\)-qubit Hamiltonian with nonidentity Hermitian Pauli strings \(P_i\) and nonzero real coefficients \(J_i\). Define its *term-overlap graph* by joining two terms when their supports meet on at least one qubit. Assume that graph has maximum degree at most one. A single-term connected component always has a fully separable Gibbs state.

For each two-term component, write its Hamiltonian as \(aP+bQ\), and let
\[
 d(P,Q):=|\{r:P_r,Q_r\in\{X,Y,Z\},\;P_r\ne Q_r\}|.
\]
Thus \(d(P,Q)\) is the number of qubits on which both terms act with distinct nonidentity Pauli letters. Put
\[
 A=|a|,\qquad B=|b|,\qquad s=\tanh(\beta A),\qquad t=\tanh(\beta B).
\]
For every \(\beta\ge0\), **the full Gibbs state is fully separable if and only if every two-term connected component satisfies the applicable condition**:

1. If \(d(P,Q)=0\), there is no restriction: the pair is locally compatible and its Gibbs state is fully separable at every temperature.
2. If \(d(P,Q)=1\), there is again no restriction: a single site carries all local incompatibility and the Gibbs state is fully separable at every temperature.
3. If \(d(P,Q)\ge2\) is even, the exact condition is
\[
 \boxed{s+t+st\le1.}
\]
4. If \(d(P,Q)\ge3\) is odd, write \(r=\sqrt{A^2+B^2}\). The exact condition is
\[
 \boxed{\frac{A+B}{r}\tanh(\beta r)\le1.}
\]

This is an instance-wise, necessary-and-sufficient phase diagram, not merely a universal high-temperature sufficient bound. It distinguishes local compatibility, a single incompatible site, globally commuting pairs with an even number of incompatible sites, and globally anticommuting pairs with at least three incompatible sites. For positive \(A,B\), the last two cases have finite critical inverse temperatures, while the first two cases never become entangled.

For equal-magnitude couplings \(A=B=J\), the commuting incompatible regime has critical value
\[
 \beta J=\operatorname{atanh}(\sqrt2-1)=\frac12\log(1+\sqrt2)\approx0.4406867935,
\]
recovering the previously established sharp degree-one **uniform** threshold. The anticommuting regime with at least three locally incompatible sites instead has critical value
\[
 \boxed{\beta J=\frac{1}{\sqrt2}\operatorname{atanh}\!\left(\frac1{\sqrt2}\right)\approx0.6232252401.}
\]

A particularly instructive example is the three-qubit Hamiltonian
\[
 H_{\mathrm{odd}}=-J\bigl(X\otimes X\otimes X+Z\otimes Z\otimes Z\bigr).
\]
Above the second critical value, its Gibbs state is **not fully separable**, yet its partial transpose is positive under *every* bipartition: this is a concrete failure of multipartite PPT tests to certify full separability within the degree-one Pauli Hamiltonian class.

## Assumptions and scope
The term-overlap graph is formed from the given Pauli expansion, just as in the anchor source. Components of distinct graph vertices need not consist of distinct Pauli strings; proportional strings are automatically covered by the \(d(P,Q)=0\) case. Terms with zero coefficients can be discarded. The inverse temperature \(\beta\) is nonnegative and the underlying Hilbert space is a finite tensor product of physical qubits.

“Fully separable” means a convex combination of tensor products of single-qubit density operators. Some separable regimes admit mixtures of product Pauli eigenstates; the \(d(P,Q)=1\) regime at very low temperature may require a rotated single-qubit basis, so no stronger claim about Pauli-eigenstate mixtures is made there.

The criterion is exact for a term-overlap graph of maximum degree at most one. It is not asserted for graphs containing paths of three or more interacting terms. A state can be not fully separable while still being PPT with respect to every bipartition.

## Proof
Because the overlap graph has degree at most one, it is a matching plus isolated vertices. Terms from different connected components have disjoint unions of physical supports, so their Gibbs operators commute and tensor-factorize over disjoint sets of qubits. A tensor product is fully separable exactly when each component is fully separable: the forward direction follows by partial tracing a fully separable state, and the reverse direction by tensoring separable decompositions. It suffices to classify a pair \(aP+bQ\).

We use a simple Pauli-mixture fact. If \(T\) is a nonidentity Hermitian Pauli string, then
\[
 \frac{I+\lambda T}{2^k}
\]
is fully separable for \(|\lambda|\le1\), because it is diagonal with nonnegative eigenvalues in a product basis of local Pauli eigenvectors. More generally, if distinct nonidentity Hermitian Pauli strings \(T_j\) have real coefficients \(c_j\) satisfying \(\sum_j|c_j|\le1\), then
\[
 \frac{I+\sum_j c_jT_j}{2^k}
 =\left(1-\sum_j|c_j|\right)\frac I{2^k}
  +\sum_j|c_j|\frac{I+\operatorname{sgn}(c_j)T_j}{2^k}
\]
is a convex combination of fully separable states.

**Case \(d(P,Q)=0\).** At every physical site the two Pauli letters commute: either they agree, one is the identity, or both are identities. Choose a product of simultaneous local eigenbases. Both \(P\) and \(Q\) are diagonal in that basis, and so is the positive Gibbs operator. Its normalized diagonal is a probability mixture of the corresponding product vectors at every inverse temperature.

**Case \(d(P,Q)=1\).** Let \(r_0\) be the unique incompatible site. At every other site the local factors of \(P\) and \(Q\) commute, so choose their common local eigenbases. Conditional on any assignment of those external product eigenvalues, the Hamiltonian reduces on qubit \(r_0\) to a Hermitian operator \(\alpha P_{r_0}+\gamma Q_{r_0}\). Its exponential is a positive one-qubit operator. The full Gibbs state is block diagonal in the external product basis, with a positive one-qubit conditional density operator in each block. This is a convex mixture of product states for all \(\beta\).

**Even \(d(P,Q)\ge2\).** The global Pauli strings commute, since the number of local anticommutations is even. Absorb coefficient signs into Hermitian Pauli strings \(\widetilde P=-\operatorname{sgn}(a)P\) and \(\widetilde Q=-\operatorname{sgn}(b)Q\). Because \(\widetilde P^2=\widetilde Q^2=I\), the normalized Gibbs state is
\[
 \rho=2^{-k}\bigl(I+s\widetilde P+t\widetilde Q+st\widetilde P\widetilde Q\bigr),
\]
where \(k\) is the number of physical qubits in the component. Since the four Pauli strings are linearly independent when \(d(P,Q)\ge2\), the Pauli-mixture lemma proves full separability whenever \(s+t+st\le1\).

For necessity, choose an incompatible site. A local Clifford transformation at this site takes the two local nonidentity factors to \(X\) and \(Z\), without affecting separability or the spectrum of the relevant partial transpose. In this basis, transposition on that one qubit fixes \(\widetilde P\) and \(\widetilde Q\), but changes the sign of their product, because \((XZ)^T=-XZ\). Thus
\[
 \rho^{T_{r_0}}=2^{-k}\bigl(I+s\widetilde P+t\widetilde Q-st\widetilde P\widetilde Q\bigr).
\]
The two commuting, independent Pauli strings have a common \((-1,-1)\)-eigenspace of dimension \(2^{k-2}\). The corresponding eigenvalue of this partial transpose is
\[
 2^{-k}(1-s-t-st).
\]
If \(s+t+st>1\), it is negative. Since a fully separable state is positive under every single-qubit partial transpose, the Gibbs state is not fully separable. The even case is therefore exact, including equality.

**Odd \(d(P,Q)\ge3\).** The strings anticommute. Put \(r=\sqrt{A^2+B^2}\). Because \((aP+bQ)^2=r^2I\), direct exponentiation gives
\[
 \rho=2^{-k}\left(I-\frac{\tanh(\beta r)}r(aP+bQ)\right).
\]
Its nonidentity Pauli coefficient absolute sum is
\[
 c:=\frac{A+B}{r}\tanh(\beta r).
\]
If \(c\le1\), the Pauli-mixture lemma proves full separability.

For the converse, take any product state \(\sigma=\bigotimes_l\sigma_l\). At each of two distinct locally incompatible sites \(r_1,r_2\), the corresponding Pauli expectations satisfy
\[
 |\operatorname{Tr}(\sigma_lP_l)|^2+|\operatorname{Tr}(\sigma_lQ_l)|^2\le1,
\]
by the single-qubit Bloch-ball constraint. At all other sites the absolute expectation of either Pauli factor is at most one. Hence, with Cauchy–Schwarz at the selected two sites,
\[
 |\operatorname{Tr}(\sigma P)|+|\operatorname{Tr}(\sigma Q)|
 \le u_1u_2+v_1v_2
 \le\sqrt{u_1^2+v_1^2}\sqrt{u_2^2+v_2^2}\le1.
\]
The same bound holds for every fully separable mixed state by convexity. The thermal state above, however, has
\[
 |\operatorname{Tr}(\rho P)|+|\operatorname{Tr}(\rho Q)|
 =\frac{A+B}{r}\tanh(\beta r)=c.
\]
For \(c>1\), it therefore violates a valid full-separability witness and is not fully separable. This establishes necessity and completes the phase diagram.

For the final PPT example, take \(P=X^{\otimes3}\), \(Q=Z^{\otimes3}\), and \(a=b=-J\). Both \(X\) and \(Z\) are real symmetric, so the resulting Gibbs state is unchanged by partial transpose on any subset of qubits. It is positive at all temperatures, hence every such partial transpose is positive. On the other hand, the preceding product-state witness is violated precisely when
\[
 \sqrt2\tanh(\sqrt2\beta J)>1,
\]
which is equivalent to the displayed odd-pair critical inverse temperature. This proves the PPT-versus-full-separability contrast.

## Verification
All universal quantifiers follow from the exact component factorization, algebraic Pauli exponential formulas, an explicit negative-partial-transpose eigenvalue, and a product-state witness. The class is infinite in system size; the proof does not rely on finite enumeration or numerical diagonalization.

The accompanying checker reproduces the two-qubit commuting threshold from explicit matrices and partial transposition, checks the three-qubit anticommuting witness and positivity of all its partial transposes, and tests several locally compatible and one-incompatible-site examples. Those finite computations are transcription checks only.

## Relationship to prior work
Kiani's *Sharp universal death of entanglement threshold for Pauli Hamiltonians* proves a sharp **uniform** high-temperature guarantee for overlap degree at least two, together with a weighted-degree bound. It does not state an instance-wise, all-temperature characterization of maximum-degree-one Hamiltonians. The previously established degree-one uniform threshold shows full separability for every matching-overlap Hamiltonian at and below \(\operatorname{atanh}(\sqrt2-1)\), and the commuting \(XX+ZZ\) witness makes that worst-case bound sharp. That statement does not determine which individual graph-matching Hamiltonians remain separable at larger inverse temperature, nor the locally incompatible parity distinction or the all-cut-PPT yet non-fully-separable odd example.

Berry and Dowling analyze the much broader thermal-entanglement problem for *two-qubit* Hamiltonians, including Bell-diagonal models and a theorem about the number of thermal-entanglement intervals without local fields. Their analysis gives background for the commuting two-qubit witness, but it does not provide a full-separability criterion for arbitrary multi-qubit Pauli-string pairs or for their matching-overlap tensor products. Rosebush and collaborators study numerical/learning-based multipartite Pauli entanglement witnesses, rather than exact all-temperature Gibbs-state classifications of this graph family.

The new distinction is structural. The local incompatibility count classifies each two-term component into a never-entangled class, an NPT-transition class, or a witness-detected non-full-separability transition class whose three-qubit representative remains PPT under every cut. Since components factorize, these cases determine the global full-separability phase of every matching-overlap Pauli Hamiltonian.

## Limitations
The theorem assumes a specified Pauli-term decomposition and a maximum term-overlap degree of at most one. It does not cover a chain or tree of three or more overlapping terms. In the odd-parity sector, the conclusion above threshold is failure of **full separability**, not proof of entanglement across any particular bipartition; in particular the example is PPT on every cut. The classification concerns the Gibbs state itself and does not assert an efficient universal sampling algorithm for arbitrary precision or complex noise models.

## References
1. B. T. Kiani, *Sharp universal death of entanglement threshold for Pauli Hamiltonians*, arXiv:2609.30149v1 (first public 2026-09-24).
2. D. W. Berry and M. R. Dowling, *Two qubits can be entangled in two distinct temperature regions*, Physical Review A 74, 062301 (2006), arXiv:quant-ph/0605176v2, DOI 10.1103/PhysRevA.74.062301.
3. A. R. Rosebush, A. C. B. Greenwood, B. T. Kirby, and L. Qian, *An exponential reduction in training data sizes for machine learning derived entanglement witnesses*, Machine Learning: Science and Technology 5, 035068 (2024), arXiv:2311.18162, DOI 10.1088/2632-2153/ad7457.
