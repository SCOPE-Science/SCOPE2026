# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The reduction from the original group \(R\) to its abelianization was checked separately for \(|T|\geq3\) and for the only two-element target \(T=C_2\). In both cases every coordinate copy of a basic commutator \([r,s]\) can be isolated as a commutator of two elements of the kernel-wreath group, so \((R')^T\leq G'\) and the abelianization is unchanged by coordinatewise passage to \(R^{\mathrm{ab}}\).

For an abelian base \(A\), the kernel group fits into \(1\to K\to H\to T\to1\), with \(K\) the kernel of the coordinate-sum map \(A^T\to T\). The coinvariant calculation follows from the exact sequence \(0\to K\to A^T\to T\to0\), Shapiro's lemma for the regular permutation module, and \(H_1(T,T)\cong T\otimes T\), yielding an injection \(T\otimes T\hookrightarrow K_T\) with cokernel \(\ker(A\twoheadrightarrow T)\).

The remaining correction was checked at the commutator level. Modulo \([H,K]\), commutators of lifts of \(u,v\in T\) map to the alternating tensors \(v\otimes u-u\otimes v\). These generate \(H'/[H,K]\). In an invariant-factor decomposition of \(T\), their independent orders are \(\gcd(n_i,n_j)\), so this subgroup has order \(|\bigwedge^2T|\). Combining this with the exact coinvariant size gives \(|H^{\mathrm{ab}}|=|A||T||\bigwedge^2T|\), and hence the stated formula for \(G\).

Edge cases were examined explicitly. Cyclic targets have trivial exterior square. For \(R=T=C_2\) with the identity quotient, the kernel is cyclic of order four, confirming both the order formula and the warning that the induced extension on abelianizations need not split. For \(T=C_2^2\), the exterior-square correction is nontrivial and agrees with direct small-group calculations.

## Originality

**PASS, to the best of our knowledge.** The primary source arXiv:2609.20401v1 was inspected at its construction theorem, multiplicative-group properties, preservation-of-abelian-quotients proposition, and iteration theorem. It proves the order of the kernel group and preservation of arbitrary finite abelian quotients, but does not state an abelianization, derived-subgroup, commutator, or exterior-square formula; full-text searches for those terms were negative.

The abelianization/augmentation structure of full wreath products is standard and is treated as prior art. Searches for the more specific index-kernel construction under terminology including augmentation kernel, regular wreath product, abelianization, commutator subgroup, Schur multiplier, and exterior square did not locate the formula \(|G^{\mathrm{ab}}|=|R^{\mathrm{ab}}||T||\bigwedge^2T|\), nor the resulting exact tower growth. Literature on Schur multipliers of wreath products concerns a different invariant of the full wreath product and does not by itself imply this first-homology calculation for the kernel.

The main residual originality risk is older wreath-product or group-extension literature using different terminology for this coupled augmentation kernel. Such literature was not exhaustively inspected theorem-by-theorem. The claim of originality is therefore explicitly limited to the best of our knowledge.

## Value

**PASS.** The result upgrades the source's qualitative preservation of abelian quotients to an exact first-derived-quotient formula. It identifies a new structural contribution from the target, namely the exterior-square/Schur-multiplier factor, gives the derived-subgroup order, and yields exact exponential laws for iterated kernel-wreath towers. The distinction between cyclic and noncyclic targets is mathematically informative: cyclic steps contribute only their order, while noncyclic targets contribute an additional homological factor.

## Review status

No independent validation, formal verification, expert attestation, or journal peer review is asserted.
