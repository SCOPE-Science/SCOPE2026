# Independent mathematical audit

## correctness

PASS

The closed-ball volume bound is sharp by the binary Hamming code, so minimum means perfect here. After translating a code through 0, the weight-two layer forces an STS(7). Each Fano line meets the six other lines once (use the two other lines through each of its three points); hence exactly 28 distinct four-sets contain a line, and the seven line complements are precisely the eligible weight-four words. Covering the other 28 weight-three words forces all seven complements. Only the weight-seven word can cover all seven remaining weight-six words with one center. The Fano-plane kernels are 4-dimensional linear codes and cube automorphisms act transitively on their translates. Distinct affine four-flats meet in at most eight words. An independent bounded regeneration compared all 240 code lists and 1680 edge pairs entrywise against the frozen certificate, verified pair-overlap counts 12600, 7680, 6720, 1680 at 0, 2, 4, 8, and reproduced triangle-freeness and (1,14,63,106,56) at each of the 240 roots. The independent code runs read-only against the frozen inputs: python3 /workspace/replay_checks.py 3. Certificate SHA-256 c781514e90db3505a668f3b39a284e8072605fb2d9967fa9504a7b913b21d89d. This establishes the stated Q7 graph only.

## originality

PASS

Credit the classical perfect-code census and the prior binary bitrade bound. The distinct supported contribution is the graph on all 240 minimum sets at the first feasible exchange radius, in particular the all-root distance spectrum and sharp diameter. No equivalent statement or controlling theorem was identified in the checked material; this is a bounded best-of-knowledge conclusion.

## value

PASS

This determines connectivity and sharp move complexity at the first exchange threshold for the entire state space of minimum dominating sets of a natural cube. The distance profile quantifies how far the optimal configurations lie from any given one, beyond what the classical minimum bitrade size can tell a reconfiguration researcher. The finite scope is part of the motivation, not extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
