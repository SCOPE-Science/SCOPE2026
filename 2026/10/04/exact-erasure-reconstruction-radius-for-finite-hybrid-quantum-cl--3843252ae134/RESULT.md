# Exact erasure reconstruction radius for finite hybrid quantum-classical algebras

## Finding

Let
\[
\mathcal H=\bigoplus_{i=1}^K(\mathcal H_{A_i}\otimes\mathcal H_{B_i}),\qquad d_i=\dim\mathcal H_{A_i},\qquad m_i=\dim\mathcal H_{B_i},
\]
and
\[
\mathcal A=\bigoplus_{i=1}^K(\mathcal B(\mathcal H_{A_i})\otimes I_{B_i}).
\]
Let \(P_i\) project onto the \(i\)-th summand. The canonical trace-preserving conditional expectation is
\[
\mathcal P_{\mathcal A}(\rho)=\bigoplus_{i=1}^K\operatorname{Tr}_{B_i}(P_i\rho P_i)\otimes\frac{I_{B_i}}{m_i}.
\]
For the flagged erasure channel
\[
\mathcal E_p(\rho)=(1-p)\rho\oplus p\operatorname{Tr}(\rho)|e\rangle\langle e|,\qquad 0\le p\le1,
\]
the exact optimal reconstruction error in unhalved diamond norm is
\[
\boxed{\epsilon_{\mathcal A}(\mathcal E_p)=\inf_{\mathcal R}\|\mathcal R\circ\mathcal E_p-\mathcal P_{\mathcal A}\|_\diamond=2p\left(1-\frac1S\right),\qquad S=\sum_{i=1}^K d_i^2=\dim_{\mathbb C}\mathcal A.}
\]
An optimal erased-branch replacement state is
\[
\boxed{\sigma_\star=\bigoplus_{i=1}^K\frac{d_i^2}{S}\left(\frac{I_{A_i}}{d_i}\otimes\frac{I_{B_i}}{m_i}\right).}
\]
Thus the exact erasure cost is independent of all gauge multiplicities \(m_i\). For a classical \(K\)-level memory it is \(2p(1-1/K)\), and for a full \(d\)-level quantum memory it is \(2p(1-1/d^2)\). If \(\lambda=(d_1,\ldots,d_K)\) is Kuperberg's hybrid-memory shape, then \(S=\|\lambda\|_2^2\).

## Assumptions and scope

The theorem is finite-dimensional. Every \(d_i,m_i\) is a positive integer. The protected algebra may have arbitrary direct-sum sectors and arbitrary multiplicity spaces. The noise is total flagged erasure of the whole physical input, and the recovery may be any completely positive trace-preserving map. The norm is the unhalved diamond norm, whose maximum channel distance is \(2\).

## Proof

Put \(S=\sum_i d_i^2\). The case \(S=1\) is trivial, so assume \(S>1\).

First solve complete erasure. Any recovery after complete erasure is a constant channel \(\mathcal R_\sigma(\rho)=\operatorname{Tr}(\rho)\sigma\). Choose
\[
\sigma_\star=\bigoplus_i\frac{d_i^2}{S}\left(\frac{I_{A_i}}{d_i}\otimes\frac{I_{B_i}}{m_i}\right).
\]
For an arbitrary reference \(R\) and arbitrary input state, write
\[
\tau=(\operatorname{id}_R\otimes\mathcal P_{\mathcal A})(\rho)=\bigoplus_i\eta_i^{RA_i}\otimes\frac{I_{B_i}}{m_i},
\]
and \(r_i^R=\operatorname{Tr}_{A_i}\eta_i^{RA_i}\). Then \(\sum_i r_i^R=\rho_R\).

The map
\[
X\longmapsto d_i\operatorname{Tr}(X)I-X
\]
is completely positive: its Choi matrix is \(d_iI\otimes I-|\Omega_i\rangle\langle\Omega_i|\ge0\). Therefore
\[
\eta_i^{RA_i}\le d_i r_i^R\otimes I_{A_i}\le d_i\rho_R\otimes I_{A_i}.
\]
Consequently, block by block,
\[
\tau_i\le S\bigl(\rho_R\otimes(\sigma_\star)_i\bigr),
\]
so \(\rho_R\otimes\sigma_\star\ge\tau/S\). Since both are states,
\[
\|\tau-\rho_R\otimes\sigma_\star\|_1\le2(1-S^{-1}).
\]
Taking the reference-assisted supremum proves the complete-erasure upper bound.

For the matching lower bound, let \(q_i=\operatorname{Tr}(P_i\sigma)\). Because \(\sum_iq_i=1\) and \(\sum_id_i^2=S\), some sector satisfies \(q_i/d_i^2\le1/S\). Use a \(d_i\)-dimensional reference and an input maximally entangled between it and \(A_i\), tensored with any pure state in \(B_i\). After \(\mathcal P_{\mathcal A}\), the effect
\[
Q_i=|\Phi_i\rangle\langle\Phi_i|_{RA_i}\otimes I_{B_i}
\]
has probability \(1\). After the constant channel its probability is \(q_i/d_i^2\). Data processing under this binary measurement gives
\[
\|\mathcal P_{\mathcal A}-\mathcal R_\sigma\|_\diamond\ge2\left(1-\frac{q_i}{d_i^2}\right)\ge2(1-S^{-1}).
\]
Thus complete erasure has exact radius \(2(1-S^{-1})\).

For general \(p\), any recovery after the flagged erasure channel has the form
\[
\mathcal R\circ\mathcal E_p=(1-p)\mathcal C+p\mathcal R_\sigma
\]
for some channel \(\mathcal C\) and state \(\sigma\). Choosing \(\mathcal C=\mathcal P_{\mathcal A}\) and \(\sigma=\sigma_\star\) gives the upper bound \(2p(1-S^{-1})\). For an arbitrary recovery, use the same sector and witness effect as above. The unerased branch can give that effect probability at most \(1\), while the erased branch gives \(q_i/d_i^2\). Hence the corrected output has witness probability at most \((1-p)+pq_i/d_i^2\), whereas the target has probability \(1\). The induced binary distributions therefore differ by at least
\[
2p\left(1-\frac{q_i}{d_i^2}\right)\ge2p(1-S^{-1}).
\]
The bounds coincide.

## Verification

The sharp upper bound is valid for arbitrary entangled references because it is based on a completely positive operator inequality, not on a state-by-state scalar estimate. The lower bound is a reference-assisted channel-discrimination witness and therefore is a legitimate diamond-norm lower bound.

The endpoints are exact: \(p=0\) gives zero error, and \(p=1\) gives the complete-erasure radius. The classical and fully quantum special cases reduce respectively to \(2p(1-1/K)\) and \(2p(1-1/d^2)\). No finite experiment or asymptotic approximation is used.

## Relationship to prior work

Bény introduced the diamond-norm reconstruction error for approximate correction of a general finite-dimensional algebra, gave the direct-sum subsystem form of such algebras, and derived dimension-independent information-disturbance bounds. The inspected full text does not specialize that optimization to a flagged erasure channel or give the direct-sum formula above.

Kuperberg described finite hybrid quantum-classical memories by a shape \(\lambda=(d_1,\ldots,d_K)\) and characterized their asymptotic capacity through all \(p\)-norms of the shape. In particular, the \(2\)-norm has a dense-coding interpretation. The present result is instead a single-shot worst-case diamond-norm statement and identifies \(\|\lambda\|_2^2\) as the exact erasure-radius parameter.

Bény and Oreshkov later formulated exact dual optimizations for worst-case entanglement fidelity and near-optimal recovery of subspace, subsystem, and hybrid codes. That is a different metric from the diamond distance claimed here. Targeted searches for hybrid erasure recovery, direct-sum conditional expectations, constant-channel diamond distance, and formulas involving \(\sum_i d_i^2\) did not locate an equivalent theorem.

## Limitations

Selective erasure of only some sectors, coherent leakage, or erasure that preserves side information is not covered. Infinite-dimensional algebras and energy-constrained diamond norms are outside the claim. The theorem gives an optimal channel-distance value, not the circuit complexity of implementing the recovery. An equivalent conditional-expectation/replacer identity may exist in operator-algebra or channel-discrimination literature under different terminology.

## References

1. C. Bény, “Conditions for the approximate correction of algebras,” arXiv:0907.4207, first submitted 24 July 2009; *Theory of Quantum Computation, Communication, and Cryptography*, LNCS 5906, 66–75.
2. G. Kuperberg, “The capacity of hybrid quantum memory,” arXiv:quant-ph/0203105, first submitted 21 March 2002; *IEEE Transactions on Information Theory* 49 (2003), 1465–1473.
3. C. Bény and O. Oreshkov, “General Conditions for Approximate Quantum Error Correction and Near-Optimal Recovery Channels,” arXiv:0907.5391; *Physical Review Letters* 104, 120501 (2010).
