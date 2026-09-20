# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof was checked independently at each structural step.

The two-sum statement follows from the exact quadratic whose roots are the summands. Its discriminant is
\[
S^2\left(1-4/N(S)\right).
\]
For distinct norm-one roots, the normalized root difference is anti-invariant under conjugation and therefore squares to a nonsquare in the base field; the repeated-root case gives discriminant zero. Conversely, a nonsquare normalized discriminant produces conjugate-opposite square roots in the quadratic extension and the explicit roots have norm one; discriminant zero gives the repeated summand \(S/2\).

The two-fold sumset count uses the bijection \(a\mapsto1-4/a\) from \(\mathbb F_q^*\) to \(\mathbb F_q\setminus\{1\}\), plus the fact that every nonzero norm fiber has \(q+1\) elements. The three-sum argument is valid for every nonzero \(S\): outside \(T\), the map \(\beta\mapsto N(S-\beta)\) has fibers of size at most two, while the set of norm values admitting a two-sum has size \((q+1)/2\), forcing an intersection. Elements of \(T\) are three-sums by adding a cancelling pair. Zero is a three-sum exactly when \(T\cap(T+T)\) is nonempty, which is exactly the \(\chi(-3)\ne1\) condition.

Finite verification exhaustively confirms the stated length distribution and sumset cardinalities for thirteen odd prime fields through 43, and confirms the sumset formulas for \(q=9,25,49\). The computation is supplementary, not a substitute for the proof.

## Originality

**PASS, to the best of our knowledge.** The closest source inspected is Shi--Li--Xia--Helleseth--Ozbudak, arXiv:2609.20402 (submitted 17 September 2026). Its main additive theorem is explicitly restricted to \(q=3^m\), and its conclusion names norm-one tori in other odd characteristics as a natural direction. In the characteristic-three proof, the identities \(4=1\) and \(t=(-t)+(-t)\) are used at precisely the points where the present theorem changes form.

Targeted searches were made for equivalent formulations involving norm-one groups/tori, finite-field unit circles, sums of two or three norm-one elements, additive bases/diameter, and the formulas involving \(1-4/N(S)\), \(-3\), and \(|T+T|\). No prior statement matching the full odd-characteristic classification was found.

The 2023 and 2025 generalized Zetterberg-code covering-radius papers were also inspected because they are the most plausible older source of a hidden implication. Their odd-characteristic covering arguments concern sums from related multiplicative subgroups with base-field coefficients; the inspected statements do not supply the unweighted full-torus additive-length distribution proved here. The 2026 motivating paper itself cites that literature and still lists other odd characteristics for the norm-one torus as future work.

Residual originality risk is material because the proof is short once the characteristic-three argument is generalized, and the motivating preprint is extremely recent. A near-simultaneous observation, an unindexed finite-geometry formulation of the same unit-circle sumset, or a forthcoming revision of arXiv:2609.20402 could reduce priority. No such coverage was located in the sources inspected.

## Value

**PASS.** The result closes the first extension explicitly suggested by the recent torus-decoding paper and gives a complete formula rather than merely a covering-radius bound. It identifies two phenomena absent in characteristic three: a repeated-root two-sum at norm four, and a sharp congruence obstruction for exact three-fold coverage. The latter is especially structural: for \(q\equiv1\pmod3\), every nonzero element is still a three-sum but zero is not, while for \(q\not\equiv1\pmod3\) the three-fold sumset is the entire field.

The result also gives the exact length distribution and the additive diameter for every odd prime power, providing a compact reusable description of the additive geometry of the one-dimensional anisotropic torus.

## Scope and limitations

The theorem is about the full norm-one torus in \(\mathbb F_{q^2}\). It does not automatically transfer to arbitrary coding families, where parity-check columns and allowed error coefficients may not coincide with unweighted torus summands. It does not address higher-dimensional tori or higher extension degrees, and it does not claim that the direct decomposition procedure is computationally optimal.
