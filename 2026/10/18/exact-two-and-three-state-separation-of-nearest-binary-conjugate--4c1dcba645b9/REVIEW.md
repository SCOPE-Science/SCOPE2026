# Scientific review: exact one- and two-symbol cyclic separation

## Correctness — PASS

The proof is for complete one-way deterministic automata over every finite alphabet of size at least two, with only unequal rotations included in the maximum. Alphabet reduction and inverse-rotation symmetry are explicit. The one-step result has a direct two-state parity/last-letter witness. For two steps, equal-letter two-symbol prefixes use a three-state reset-and-three-cycle automaton. Mixed prefixes are controlled by a three-state transformation pair whose **entire** generated transition monoid is listed in a twelve-row table. Exact closure and the commuting-language equality with \((01)^*\) prove the upper bound at **all** lengths, not only tested ones. The lower bound supplies the analytic witness \(0^{n-2}10\) against its two-step rotation for all \(n\ge4\) and covers every possible two-state map. The attached standalone checker regenerates the closure and verifies the finite identities and additional finite examples.

Risk: the proof depends on the twelve exact transformation rows, but the construction makes them directly replayable from two explicit triples. No unproved infinite extrapolation from enumeration is used.

## Originality — PASS within inspected evidence

Nicol, *Further Remarks on Separating Words*, arXiv:2608.30928v1 (2026), Section 3, proves the general upper bound \(2\min\{k,n-k\}+1\), giving \(3\) for one-step and \(5\) for two-step rotations but not the exact \(2,3\) profile. Demaine–Eisenstat–Shallit–Wilson, *Remarks on separating words*, arXiv:1103.4513v1 (2011), supplies the isolated witness \(\operatorname{sep}(0010,1000)=3\) and discusses general conjugates; its result is not the uniform two-step upper bound. Earlier permutation-only separator formulas constrain a different machine class and therefore do not imply the present theorem. Searches using the source title, shift parameters, equivalent concatenation formulation and transformation-commutation formulation revealed no covering statement. This is a best-evidence comparison, not a proof that every indexed or unindexed paper has been checked.

Residual risk: an equivalent generalization may occur under another formulation in unindexed literature. In particular, a previously proved bound of three for all binary pairs \(AB,BA\) with \(|A|=2\) would subsume the new result, but no such accessible result was identified.

## Value — PASS

The extremal quantity for conjugate-word separation is explicitly defined in the 2026 literature; the first two shift distances are a natural boundary condition for its dependence on cyclic displacement. The theorem determines **exact worst-case state complexity for all word lengths and alphabets** at both distances, improving the published \(3,5\) upper estimates to tight \(2,3\). The new twelve-element centralizer construction is a structural universal witness for arbitrarily long partners, while the lower bound explains why the second step differs sharply from the first. It extends a known length-four example to the complete infinite family and does not merely restate a known numerical instance.

Limitation: shifts of larger distance, permutation automata, and nondeterministic separation are left open by this proof. Reproduction of the attached finite closure is checkable independently; full independent mathematical review has not occurred.

Self-review: passed. Independent audit: not yet performed.
