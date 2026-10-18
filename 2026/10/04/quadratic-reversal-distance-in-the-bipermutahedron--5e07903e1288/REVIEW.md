# Independent mathematical audit

## correctness

PASS

The actual RESULT.md 14e56384049f27b5a51bb15b281573e12d88e657 uses Ardila’s exact adjacent-edge graph: swap distinct neighboring letters, or transfer singleton status via a doubled adjacent block. Duplicating the singleton makes a two-copy word; target block reversal reverses 4*choose(n,2) cross-label orders. An ordinary swap changes at most one copy inversion; a singleton swap at most two; transfer changes zero. If t=n-r labels were never singleton, their pairs force 2t(t-1) ordinary swaps; visiting r>=2 singleton labels in a closed walk forces at least r transfers, establishing L>=n*n-1 for n>=3, with r=1 separate. Explicit moves cross blocks with n(n-1) swaps and n-1 transfers. n=2 distance 2. Independently implemented BFS reproduces n=2,3,4 distances 2,8,15; script 6cbe8ae200570f317cda55103771033d90e8b3e7 reports n=5 distance 24.

## originality

PASS

The inspected primary article classifies vertices, local graph edges and descent-reversal symmetry, not the exact one-skeleton shortest path between this canonical reversal pair. Resultary search returns this result but no earlier dominating all-pairs distance or diameter theorem; other bipermutahedron records concern Euclidean radii. Best-of-knowledge exact metric statement survives.

## value

PASS

Bipermutahedron is a natural flag-matroid/generalized permutahedral polytope. An exact canonical antipodal/reversal distance in its one-skeleton, valid for every n and giving a quadratic diameter lower bound, addresses a natural graph metric invariant with a non-obvious inversion/transfer argument. It is not a renamed known inversion count because transfer changes singleton status.

The dated certificate retains the supplied scientific assessment, sources and limitations.
