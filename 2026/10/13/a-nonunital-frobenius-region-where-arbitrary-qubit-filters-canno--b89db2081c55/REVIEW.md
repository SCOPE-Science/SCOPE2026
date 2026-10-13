# Review

## Correctness
**PASS.** For an arbitrary CPTP filter \(\Psi=(N,d)\), direct composition gives \(A=MNM\) and \(b=MNc+Md+c\). Schatten Hölder gives \(\|A\|_1\le\|MN\|_{\mathrm F}\|M\|_{\mathrm F}\). Lemma 7 of arXiv:1411.2517, applied to the filter with auxiliary matrix \(M\), gives \(\|Md\|_2+\|MN\|_{\mathrm F}\le\|M\|_{\mathrm F}\). Combining these inequalities yields the published sufficient criterion \(\|A\|_1+\|b\|_2\le1\), so Proposition 5 makes every \(\Phi\Psi\Phi\) entanglement breaking. The index equalities then follow from the definitions and stability of entanglement breaking under unitary composition. The generalized amplitude-damping witness is nonunital, lies strictly inside the norm region, and is non-entanglement-breaking by the source's exact PPT criterion.

## Originality
**PASS.** The defining paper states the qubit equality as Conjecture 1 and proves the index-two implication only for unital channels. Its full relevant section was inspected, including Proposition 5, Lemma 7, Theorem 8, and the generalized amplitude-damping example. A later full-text optical paper treats selected intermediate unitaries for rotated damping channels, while the cut-and-paste paper treats reordering distinct channel pieces. Searches using filtered-index notation, arbitrary/nonunitary filter language, Bloch-affine and Frobenius-norm aliases, the source identifier, and the explicit damping family did not locate a theorem implying this nonunital region. The residual risk is a later result stated in substantially different terminology or outside indexed sources.

## Value
**PASS.** The result advances an explicit open qubit-filtering conjecture on a continuum of nonunital channels rather than a single example. It shows that a simple, rotation-invariant affine norm condition is enough to defeat **every** intermediate CPTP correction at the second use, and it supplies a concrete finite-temperature amplitude-damping point where the source's unital theorem does not apply. The conclusion is operationally meaningful because it compares the strongest one-system filtering class considered in the conjecture with unitary filtering.

## Closest literature and limitations
The closest result is Theorem 8 of arXiv:1411.2517, which proves \(N_U(\Phi)=2\Rightarrow N(\Phi)=2\) for **unital** qubit channels. The present sufficient condition covers nonunital channels but does not prove the converse condition, characterize the entire index-two region, or resolve the conjecture for larger indices. The 2017 amendment experiment and the 2016 cut-and-paste construction concern different intervention classes and do not dominate the claim.

Self-review: passed. Independent audit: not yet performed.
