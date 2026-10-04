# Review

## Correctness

PASS. In a finite local principal ideal ring, nonzero ideals form a chain, so two product ideals intersect nontrivially exactly when their active supports share a local factor. The support-incidence Gram matrix therefore has the exact graph pattern. Singleton-support ideals give full row rank \(r\), so maximum nullity is at least \(N-r\). In the nonreduced regime a nonzero maximal ideal in one factor supplies a proper full-support white vertex; the displayed chain of \(r\) white ideals is then forced one at a time. The universal inequality \(M(G)\le Z(G)\) closes equality. The local \(K_1\) boundary is handled separately.

The packaged checker independently reconstructs the exponent-vector graphs, verifies the Gram pattern and exact rational ranks, replays the forcing chain, and directly excludes one-smaller zero forcing sets in all moderate test cases.

## Originality

PASS. The inspected ring-intersection literature covers ordinary domination and other classical graph invariants, while targeted searches under zero forcing, maximum nullity, minimum rank, principal ideal ring, local-factor, nilpotency, and ideal-intersection formulations did not locate the theorem. A previously known reduced product-of-fields calculation does not imply the nonreduced theorem because the full-support proper ideal used by the forcing chain exists precisely because a nilpotent local factor is present.

Residual risk: minimum-rank work on algebraic graphs is dispersed, and an equivalent statement could use terminology not indexed under ideal-intersection graphs. No such source was located.

## Value

PASS. The result recovers a ring-theoretic decomposition invariant from an inverse-eigenvalue parameter: except for the one-vertex boundary, the real symmetric minimum rank equals the number of local principal factors. It simultaneously proves equality of zero forcing and maximum nullity for the entire nonreduced finite-principal-ideal regime, and the proof gives explicit extremal constructions rather than only bounds.

Same-model review: passed. Independent audit: not yet performed.
