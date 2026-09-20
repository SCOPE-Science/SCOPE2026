# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The two-message upper bound is obtained by changing which party sends the initial Gap-Hamming samples. Bob can send the sampled \(\mathbf y\)-bits first; Alice then has exactly the sampled XOR values that Bob has in the source protocol, so she computes the same random address \(h\). Because she also owns \(\mathbf u_h\), she can combine the \(k\)-bit address and her four fully linear-PCP field elements in the second message. Bob then selects \(\mathbf v_h\) and reconstructs precisely the same four global quantities as in Wang--Wu's Step IV. The message sizes remain \(kq\) and \(17k\), and the source error analysis is unchanged.

The one-way lower bound is an exact restriction. With Alice's base input fixed to zero, Bob can realize every address \(h\) by choosing each of his Gap-Hamming blocks to be all zero or all one. For this promised base input, certificate uniqueness gives a unique accepted word \(\mathbf c^{*(h)}\). Encoding the sender bit \(s_j\) by choosing Alice's \(j\)-th certificate share as either \(0\) or a fixed nonzero \(e\), while Bob sets the selected share to \(\mathbf c^{*(h)}\oplus e\), makes the total function equal exactly \(s_h\). Symmetry gives the reverse direction.

The included information-theoretic proof of the one-way INDEX lower bound is standard and checks the randomized/public-coin setting directly. The parameter conversion follows from the exact source formulas
\[
d=k(m(m+3)+1),\qquad
n=km(8d-3),\qquad
m=2^k,
\]
which imply \(n=\Theta(k^2m^3)\) and \(k=\Theta(\log n)\).

Adversarial checks considered whether the PCP response direction hides an extra message, whether Bob's selected certificate share could depend on the sender's INDEX string, whether all addresses are reachable by promised Gap-Hamming inputs, and whether a second accepted certificate could invalidate the restriction. The first issue is avoided by having Bob send the sampling sketch first; Bob's share depends only on \(h\); all \(2^k=m\) addresses are realized by all-zero/all-one blocks; and uniqueness rules out the alternative certificate.

## Originality

**PASS, to the best of our knowledge.**

The motivating Wang--Wu v1 (arXiv:2609.20763, submitted 17 September 2026) was inspected at Theorem 1.1, Lemma 3.6, Theorem 3.7, Definition 3.8, and Theorem 4.1 with its explicit communication steps. Their proof presents three transmissions: Alice's sampled bits, Bob's address bits, and Alice's four field elements. The manuscript does not state a message-round bound, and searches within the full text found no occurrence of “one-way” or “round.”

External searches used the exact title and arXiv identifier together with “one-way,” “two-message,” “two-round,” “INDEX,” “monochromatic rectangle,” and cheat-sheet/fully-linear-PCP terminology. No prior statement of the two-message classical protocol, the bidirectional INDEX restriction, or the resulting one-message/two-message gap was found. The current SCOPE archive was searched by source identifier, monochromatic-rectangle terminology, and one-way-randomized terminology, with no matching record.

There is relevant conceptual precedent: Gavinsky's earlier total-function quantum separation also organizes a cheat-sheet/fully-linear-PCP verification into two quantum messages. Accordingly, no novelty is claimed for the abstract idea that such verifications can be arranged in two messages. The novelty claim is restricted to the Wang--Wu classical function, the unchanged-cost two-message protocol, and the exact one-way INDEX embedding.

The strongest residual risk is priority rather than correctness: the source preprint is very recent, and the message rearrangement is short enough that the authors or other readers may independently note it in a near-term revision.

## Value

**PASS.**

The refinement strengthens the headline class separation: the Wang--Wu witness does not merely lie in unrestricted \(\mathsf{BPP}\); it lies in the two-message subclass \(\mathsf{BPP}[2]\). At the same time, the same function has polynomial one-way randomized complexity in either direction. Thus one additional message changes the complexity from
\[
\widetilde\Omega(n^{1/3})
\]
to
\[
O(\log n\log\log n)
\]
while preserving the source paper's extremely small monochromatic rectangles and adaptive-\(\mathsf{NP}\)-query lower bound.

This gives a clean round-complexity interpretation of a new total-function separation and identifies the cheat-sheet address/certificate dependency as the mechanism forcing interaction.

## Limitations

The one-way lower bound is not shown tight. No stronger lower bound for two-message communication is claimed, and no improvement is made to the source rectangle or \(\mathsf P^{\mathsf{NP}}\) bounds. The private-coin corollary uses the standard Newman reduction and is not a new derandomization theorem. The originality assessment is subject to elevated near-simultaneous risk because the source manuscript is recent.
