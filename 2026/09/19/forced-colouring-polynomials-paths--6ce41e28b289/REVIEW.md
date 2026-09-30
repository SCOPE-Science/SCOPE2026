# Review

**Same-model correctness retained. Independent audit on 29 September 2026: correctness passed; originality/provenance repaired.**

## Correctness

The coefficient formula is correct. A successful path assignment omits an independent set of internal vertices; each omission imposes one equality on a disjoint pair of edge-difference signs. This gives exactly 3*2^(n-1-j) compatible full colourings for each omitted j-set and C(n-1-j,j) choices of that set. Independent enumeration during the audit reproduced the formula through n=6. The recurrence, minimum-domain count, exponential growth statement, and corrected P_3 value all follow.

## Originality and provenance correction

The earlier SCOPE record

`2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd`

was committed at 2026-09-17 23:56:20 UTC and already contains precisely the same path coefficient formula. This focused record was committed at 2026-09-19 08:44:58 UTC. The original standalone originality PASS is therefore withdrawn.

The record is retained as a focused alternate derivation and as a convenient source for path-specific corollaries (minimum-domain counts, recurrence and growth), not as a separate discovery of the main formula.

## Scientific value

The focused proof and corollaries are useful and independently verified, but their role is corroborative/refinement-oriented relative to the earlier broader SCOPE theorem.

## Limitations

- The core path coefficient law is prior within SCOPE.
- The new value is in presentation and consequences rather than first discovery.
- The theorem is specific to paths.
