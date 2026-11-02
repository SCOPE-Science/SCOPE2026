# Scientific review

## Correctness — PASS

The claim has exact quantifiers: integers \(n\ge2\), arbitrary field sizes \(q=2^h\), arbitrary offsets and all permutation schedules of path vertices. Local parity maps are affine adjacent-coordinate swaps in the root-coordinate realization, where the product is an \((n+1)\)-cycle. Translation to an affine constant-sum hyperplane gives fixed-point counts by gcd and parity of the repetition length. The separate adjacency-kernel calculation identifies the one obstruction to fixed points, and primitive periods follow constructively. These steps prove the infinite statement; the replayed 4,696-case exhaustive checker independently tested 154,528 initial states, with additional random large-size checks. The finite checks are corroboration, not an infinite proof.

## Originality — PASS, qualified

The closest inspected primary source, Defant (arXiv:1511.06966), determines affine parity orbits on cycle graphs over the binary field and a specified update order. Macauley–McCammond–Mortveit (arXiv:0808.1238) focus on circular asynchronous cellular automata and general dynamics groups. Chen–Reidys (arXiv:1510.04930) provide a matrix-composition formula for arbitrary linear sequential systems, not the stated path-specific affine fixed and primitive-period counts. The type-\(A\) Coxeter identification and generic Möbius inversion are prior mathematical knowledge. The assessed new content is their combined exact all-size affine path orbit census, schedule universality, and alternating-forcing period restriction. Searches of published mathematical findings and recoverable prior claims did not identify equivalent or stronger coverage. The negative-search evidence is not proof of uniqueness; general affine-Coxeter literature not exhaustively checked remains a risk.

## Mathematical value — PASS

The path is the canonical finite spatial interval for asynchronous local updates. The full classification measures how static vertex forcing changes the available global clock periods rather than merely detecting invertibility. It identifies a sharp one-dimensional obstruction, explains why forcing removes all periods missing the largest power of two in \(n+1\), and yields a complete maximal-cycle regime for dyadic path lengths. These are natural, schedule-robust orbit properties for an infinite system family, beyond a single small computation.

## Relationship and limitations

This result is specifically for fixed permutation schedules, finite characteristic-two fields, and nearest-neighbor self-inclusive parity with constant offsets. It does not subsume previous theorems for asynchronous cycle graphs or arbitrary graph maps. Broader historical equivalences remain possible, and no independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
