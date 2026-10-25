# Review

## Correctness

**PASS.** The proof counts all nonempty right quotients at every prefix length. At internal even depths the count is three; at the first odd depth it is two; at internal odd depths before the last one it is five; at the last odd depth it is three. The sum is \(8d-6\), and the single empty quotient gives \(8d-5\) states. The symbolic distinction arguments apply to every \(d\ge2\). The script independently checks the profile for \(2\le d\le8\) but is not used as the universal proof.

## Originality

**PASS, bounded claim.** The closest inspected source gives the rank-width upper bound and a ternary witness, while noting an obstruction at a binary endpoint rank. The binary two-bit encoding is motivated by that witness; the new content is the exact binary quotient profile and the exact additive-five extremal gap within the stated operand profile. published-finding corpus searches for the exact profile and the explicit block sets returned no matching result. Search absence does not prove novelty, and unindexed prior work remains a risk.

## Value

**PASS.** The result quantifies precisely how close a binary family can come to the rank-width upper bound under a natural, explicitly specified pair of operand profiles. It separates the endpoint restrictions forced by a binary alphabet from all interior ranks, providing a reproducible benchmark for further work on binary block-language unions.

## Closest literature and limits

Duarte et al., “Operational State Complexity of Block Languages,” arXiv:2409.06970, prove the general rank-width upper bound and tightness for alphabets of size at least three. The author's thesis version contains the same result and points to future work on state-count bounds. The current claim does not solve the global binary-alphabet extremal problem.

Self-review: passed. Independent audit: not yet performed.
