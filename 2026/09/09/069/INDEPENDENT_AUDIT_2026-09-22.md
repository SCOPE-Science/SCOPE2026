# Independent audit — 2026/09/09/069

## Correctness — PASS

Raising a permutation with three 15-cycles and three fixed coordinates to the fifth power gives 15 three-cycles and three fixed coordinates, so its fixed ambient subspace has dimension 18. The odd-order averaging idempotent is an orthogonal projection on the binary ambient space, and self-duality of C implies its fixed subcode is self-dual inside this 18-dimensional fixed space, of dimension 9. Thus the complementary τ-module inside C has dimension 24−9=15. It has no fixed vectors, so every nonzero vector has a three-element orbit; 3 must divide 2^15−1, whereas 2^15−1≡1 mod 3. This is a complete contradiction for every binary self-dual C, independently of minimum distance. I also checked the second descent: σ³ has nine 5-cycles and three fixed points; its fixed subcode dimension is 6, leaving dimension 18, but 2^18−1≡3 mod 5. Both arguments independently rule out the type.

## Originality — PASS, narrow scope

Bouyuklieva–Willems–Yankov treat order 15 in length 96, and Guenther–Nebe's alternating-group constraint does not itself forbid this even permutation at length 48. The specific length-48/type-wide exclusion was not found in those open works. The mechanism is elementary standard odd-order module parity, so its novelty is only the application to this cycle type.

## Scientific value — PASS, modest

It removes one possible automorphism window for all binary self-dual [48,24] codes, hence for extremal Type II codes. It does not classify length-48 codes or address other order-15 types.

## Sources

- Original RESULT.md and METADATA.json; independent fixed-subcode and orbit divisibility checks above.
- Bouyuklieva–Willems–Yankov, https://arxiv.org/abs/1403.4735 .
- Guenther–Nebe, https://arxiv.org/abs/0810.3787 .
