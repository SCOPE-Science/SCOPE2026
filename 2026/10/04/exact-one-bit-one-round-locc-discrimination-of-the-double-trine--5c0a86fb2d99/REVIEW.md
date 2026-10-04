# Review of Exact one-bit one-round LOCC discrimination of the double trine

## Correctness
PASS. The claim is reduced from arbitrary binary Alice POVMs to rank-one projectors by convexity and the extreme-point characterization of qubit effects. A second convexity argument puts the projector axis in the trine plane. The remaining one-parameter problem is solved through the exact qubit Helstrom dual, interpreted as an additively weighted smallest-enclosing-circle problem. Both possible active-set regimes are treated analytically and shown to decrease away from the maximizing symmetry direction. At the maximizer, the stated radical follows from the binary Helstrom formula and the trine overlap \(1/4\). The standalone verifier independently reconstructs the dual candidates and checks the formulas numerically, but the finite scan is not used as the proof.

## Originality
PASS. The closest source is Dutra–Ohst–Nguyen–Gühne, whose double-trine table gives only \(0.8976\le P\le0.905\) for a two-symbol message. Chitambar–Hsieh analytically solve unrestricted one-way LOCC but use a three-outcome Alice measurement and therefore do not imply the one-bit optimum. Achenbach–Leppäjärvi–Lee–Heinosaari later repeats the numerical one-bit interval. Exact-formula, one-bit, binary-POVM, projective-sender, and alias searches in the published-finding database returned no covering result. A residual risk remains that the same two-symbol calculation appears under older communication-complexity terminology not found by these searches.

## Value
PASS. The result closes a certified numerical gap in a recent communication-bounded LOCC benchmark with an exact analytic constant, identifies the optimal sender measurement and receiver decision structure, and cleanly quantifies the performance loss caused solely by restricting the sender from three outcomes to one transmitted bit. This is a natural operational invariant of the canonical double-trine example, not an arbitrary parameter slice.

## Closest literature and limitations
The 2025/2026 communication-bounded LOCC work supplies the explicit unresolved interval. The 2013 paper supplies the unrestricted one-way benchmark \(1/2+\sqrt3/4\), while the 2026 multi-copy paper independently records the bounded-message interval. The theorem here is limited to equal priors, the double trine, one round, Alice-to-Bob communication, and a two-symbol message.

Same-model review: passed. Independent audit: not yet performed.
