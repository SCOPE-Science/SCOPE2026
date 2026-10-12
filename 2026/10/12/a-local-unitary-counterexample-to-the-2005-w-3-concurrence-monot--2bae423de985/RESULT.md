# A local-unitary counterexample to the 2005 \(W^3\) concurrence monotonicity claim
## Finding
For the three-qubit functional called the \(W^3\) class concurrence in Eq. (23) of Heydari (2005), local-unitary invariance fails already on a biseparable Bell-pair state with a spectator qubit. Let
\[
|\psi_0\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}\otimes|0\rangle .
\]
Writing the positive normalization in Eq. (23) as \(N^W_3\), direct substitution gives
\[
C_{W^3}(\psi_0)^2=N^W_3.
\]
Now act only on the third qubit with \(U=iH\), where
\[
H=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad \det(iH)=1.
\]
Thus \(U\in SU(2)\subset SL(2,\mathbb C)\). Up to an irrelevant global phase,
\[
(I\otimes I\otimes U)|\psi_0\rangle
=
|\psi_+\rangle
=
\frac{|000\rangle+|001\rangle+|110\rangle+|111\rangle}{2}.
\]
The same Eq. (23) gives
\[
C_{W^3}(\psi_+)^2=\frac{N^W_3}{2}.
\]
Hence
\[
\frac{C_{W^3}(\psi_+)}{C_{W^3}(\psi_0)}=\frac1{\sqrt2},
\]
so the functional is not invariant even under a determinant-one local unitary. Consequently the paper's stated conclusion that this \(W^m\) concurrence is an entanglement monotone is false already for \(m=3\).

## Assumptions and scope
The claim concerns exactly the pure-state \(W^3\) concurrence defined by Eq. (23) of arXiv:quant-ph/0505109 / J. Phys. A 38 (2005) 8667--8679. The normalization constant \(N^W_3\) is assumed positive; its numerical value is immaterial because the counterexample changes the squared concurrence by a factor of two. The example is biseparable across the third-qubit cut, which is within the source's intended scope: immediately before its monotonicity claim, the paper states that its \(W^m\) class includes biseparable states and is intended to measure bipartite entanglement in a multipartite state.

The finding does not assert that every later concurrence proposed by the same author has the same defect. In a 2006 follow-up, the author explicitly states that a newly constructed concurrence is not equal to the 2005 concurrence classes.

## Proof
For three qubits, Eq. (23) is the square root of \(4N^W_3\) times a sum of squared \(2\times2\) coefficient minors, grouped by the three choices of an entangled pair while the remaining subsystem index is held fixed.

For \(|\psi_0\rangle\), the only nonzero coefficient minor is the pair-\(12\) minor in the third-qubit slice \(|0\rangle\). Its determinant is \(1/2\), so the sum of squared minors is \(1/4\). Therefore
\[
C_{W^3}(\psi_0)^2=4N^W_3\frac14=N^W_3.
\]

For \(|\psi_+\rangle\), the pair-\(12\) determinant equals \(1/4\) in each of the two third-qubit slices. All pair-\(13\) and pair-\(23\) minors vanish because qubits \(1\) and \(2\) remain in a Bell state tensor a pure spectator. Hence the squared-minor sum is
\[
2\left(\frac14\right)^2=\frac18,
\]
and
\[
C_{W^3}(\psi_+)^2=4N^W_3\frac18=\frac{N^W_3}{2}.
\]

Finally, any entanglement monotone \(E\) that is nonincreasing under deterministic LOCC must be invariant under a local unitary \(V\): applying \(V\) gives \(E(V\psi)\le E(\psi)\), while applying the local inverse \(V^\dagger\) gives \(E(\psi)\le E(V\psi)\). Thus equality is necessary. The displayed factor \(1/\sqrt2\) violates this necessary condition. Because \(iH\) has determinant one, the same example directly contradicts the source's stronger claimed \(SL(2,\mathbb C)\) invariance.

## Verification
The accompanying `verify.py` performs the coefficient-minor calculation in exact arithmetic over \(\mathbb Q(\sqrt2)\). It verifies that applying \(H\) to the third qubit maps the first state to the second, that \(\det(iH)=1\), and that the two values of \(C_{W^3}^2/N^W_3\) are exactly \(1\) and \(1/2\). Multiplication of the local \(H\) by \(i\) changes the three-qubit vector only by a global phase in this construction and therefore does not alter any squared minor. Running `python3 verify.py` prints `VERIFY_OK`.

The proof itself is symbolic and does not infer an infinite statement from finite enumeration; the executable check only replays the displayed exact counterexample.

## Relationship to prior work
Heydari (2005) defines the \(W^3\) functional in Eq. (23), explicitly includes biseparable states in the \(W^m\) class, and then states that for multi-qubit states these concurrences are invariant under SLOCC and hence are entanglement monotones. The counterexample targets that exact implication.

A later paper by the same author, arXiv:quant-ph/0608224, constructs a new multipartite concurrence and explicitly says that it is not equal to the earlier concurrence classes. That later redefinition therefore does not imply the present counterexample or repair the 2005 functional as written.

Wang's earlier arXiv:quant-ph/0406114 gives a different W-class concurrence-vector construction and emphasizes reduction to ordinary two-qubit concurrence when one qubit is separable. It does not contain the Eq. (23) functional or the local-unitary counterexample above.

Focused searches by title, arXiv identifier, the phrases "W class concurrence", "local unitary", "SLOCC invariant", "entanglement monotone", and the Bell-pair spectator construction found no published statement implication-equivalent to this exact counterexample.

## Limitations
The finding is a negative structural result about one specific 2005 \(W^3\) functional. It does not classify all states on which that functional changes under local unitaries, does not propose a replacement measure, and does not assess the separate \(GHZ^m\) concurrence classes. A later same-author concurrence is explicitly a different construction and is outside the claim.

Literature search cannot prove global absence. The residual originality risk is that an unindexed note, comment, or thesis may have observed the same local-unitary failure without using the searched terminology.

## References
1. H. Heydari, "Concurrence classes for general pure multipartite states," arXiv:quant-ph/0505109; J. Phys. A 38 (2005) 8667--8679, doi:10.1088/0305-4470/38/40/012.
2. H. Heydari, "Concurrence for multipartite states," arXiv:quant-ph/0608224.
3. A. M. Wang, "Generalized GHZ-class and W-class concurrence and entanglement vectors of the multipartite systems consisting of qubits," arXiv:quant-ph/0406114.
