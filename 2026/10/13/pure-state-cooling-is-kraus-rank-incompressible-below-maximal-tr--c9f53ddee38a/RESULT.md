# Pure-state cooling is Kraus-rank incompressible below maximal trace error
## Finding
Let \(\mathcal R_G\) be the pure replacer channel from a \(d\)-dimensional input Hilbert space to a finite-dimensional output Hilbert space,
\[
\mathcal R_G(\rho)=|G\rangle\langle G|.
\]
For every completely positive trace-preserving map \(\Phi\) with Kraus rank \(r<d\),
\[
\sup_{\rho}\left\|\Phi(\rho)-\mathcal R_G(\rho)\right\|_1=2.
\]
Thus a uniform trace-norm approximation with any tolerance \(\varepsilon<2\) requires Kraus rank at least \(d\). This is sharp: the exact pure replacer has Kraus rank \(d\), for example through Kraus operators \(K_j=|G\rangle\langle j|\) for an input basis \(\{|j\rangle\}_{j=1}^d\).

For a system of \(N\) fermionic modes, \(d=2^N\). If a protocol starts an \(m\)-mode fermionic bath in a pure state, applies one joint unitary, and discards the bath only at the end, the induced system channel has Kraus rank at most \(2^m\). Therefore any such protocol that sends every system input to within trace norm strictly smaller than \(2\) of one fixed pure target must obey
\[
m\ge N.
\]
The recent bath-assisted cooling construction of Yu, Chen, and Lin uses exactly two initially empty bath modes per system mode and provides a uniform global trace-norm guarantee with \(\varepsilon\in(0,1]\). Its coherent bath is therefore within a factor two in mode count of the absolute information-theoretic minimum in this single-contact pure-bath model.

## Assumptions and scope
The channel statement assumes finite-dimensional input and output spaces. Kraus rank means the minimum number of Kraus operators, equivalently the minimum Stinespring environment dimension. The approximation criterion is the source-relevant statewise uniform trace norm \(\sup_{\rho}\|\Phi(\rho)-|G\rangle\langle G|\|_1\); it is not diamond norm. The target is pure and independent of the input.

For the cooling consequence, the bath is initially pure, the joint evolution before discard is unitary, and the same physical bath is retained through the coherent contact and discarded only at the end. Each fermionic mode contributes a two-dimensional Fock factor, so an \(m\)-mode bath has Hilbert-space dimension \(2^m\). The lower bound does not assume locality, a gap, weak interaction, or a particular pulse shape.

## Proof
Choose a minimal Stinespring isometry
\[
V:\mathbb C^d\longrightarrow \mathcal H_{\mathrm{out}}\otimes\mathbb C^r
\]
for \(\Phi\), and put \(P=|G\rangle\langle G|\). Define the positive operator on the input space
\[
A=V^\dagger(P\otimes I_r)V.
\]
Because \(P\otimes I_r\) has rank \(r\),
\[
\operatorname{rank}(A)\le r.
\]
If \(r<d\), then \(A\) has a nonzero kernel. Choose a unit vector \(|\psi\rangle\in\ker A\). Positivity gives
\[
0=\langle\psi|A|\psi\rangle
 =\operatorname{Tr}\!\left(P\,\Phi(|\psi\rangle\langle\psi|)\right).
\]
Hence \(\Phi(|\psi\rangle\langle\psi|)\) has support orthogonal to \(|G\rangle\). Two density operators with orthogonal support have trace-norm distance \(2\), so
\[
\left\|\Phi(|\psi\rangle\langle\psi|)-P\right\|_1=2.
\]
Since trace distance between states never exceeds \(2\), this proves the exact supremum.

Conversely, the operators \(K_j=|G\rangle\langle j|\), \(1\le j\le d\), satisfy \(\sum_jK_j^\dagger K_j=I_d\) and realize \(\mathcal R_G\). Its Choi matrix is \(I_d\otimes P\) up to the chosen Choi normalization, and therefore has rank \(d\). The threshold \(d\) is exact.

For an \(m\)-mode pure bath, the physical dilation itself supplies a Stinespring environment of dimension \(2^m\), so the induced channel has Kraus rank at most \(2^m\). Combining this with the previous lower bound for the \(2^N\)-dimensional system gives \(2^m\ge2^N\), hence \(m\ge N\).

## Verification
The proof is rank-theoretic and contains no numerical or asymptotic step. The critical implications were checked directly: \(\operatorname{rank}(V^\dagger QV)\le\operatorname{rank}(Q)\); a positive output state with zero expectation on a rank-one projector has support orthogonal to that projector; and orthogonal density operators have trace-norm distance \(2\). The exact replacer construction with \(d\) Kraus operators establishes sharpness.

For the literature anchor, the inspected source states that its protocol starts from arbitrary mixed system states, targets the interacting pure ground state with global trace-norm error, uses two initially empty bath modes per system mode, maintains one coherent bath contact, and discards the bath only at the end. Those are precisely the channel-level assumptions used in the consequence above.

## Relationship to prior work
Yu, Chen, and Lin motivate their construction by entropy and information transfer into bath degrees of freedom and prove a concrete protocol with two empty bath modes per system mode. The inspected source does not state a minimum bath-mode theorem or a Kraus-rank incompressibility threshold.

Lancien and Winter study uniform output-norm approximation of quantum channels by maps with smaller Kraus rank. Their full text identifies Kraus rank with minimal Stinespring environment dimension, proves general compression results, and gives entropy-based lower bounds of order the input/output dimension for some channels. Their discussion explicitly leaves channel-dependent optimal approximating Kraus rank open. The inspected text contains no pure-replacer case and does not state the exact phenomenon proved here: for a pure replacer, reducing the Kraus rank below \(d\) forces the worst-case statewise trace-norm error all the way to its maximum value \(2\).

Standard Stinespring theory supplies the environment/Kraus-rank equivalence but does not by itself state this approximation threshold. Thus the result is a source-motivated exact specialization rather than a restatement of the general dilation theorem.

## Limitations
The lower bound is information-theoretic. It does not show that \(N\) bath modes suffice under the locality, weak-interaction, spectral-gap, pulse-sharing, or Hamiltonian constraints of the recent cooling construction. Therefore the factor-two comparison is only against the unconstrained coherent-bath mode minimum, not an optimality theorem for that construction class.

Purity of the bath is essential to the stated physical mode-count consequence. The channel theorem itself concerns Kraus rank and remains valid independently of how a channel is implemented. The argument also relies on a pure fixed target and a uniform guarantee over all system inputs; neither a mixed target nor an input-restricted promise is covered.

## References
1. X.-H. Yu, Z. Chen, and L. Lin, “Bath-assisted cooling without resets,” arXiv:2609.40328v1 (first public 2026-09-30).
2. C. Lancien and A. Winter, “Approximating quantum channels by completely positive maps with small Kraus rank,” arXiv:1711.00697v3; Quantum (2024).
3. F. vom Ende, “From Kraus Operators to the Stinespring Form of Quantum Maps: An Alternative Construction for Infinite Dimensions,” arXiv:2301.05488.
