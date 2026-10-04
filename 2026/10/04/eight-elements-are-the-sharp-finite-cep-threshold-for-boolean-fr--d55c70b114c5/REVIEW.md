# Review

## Correctness

PASS. Every two-element Boolean frame is trivially CEP. A four-element Boolean algebra has only one proper Boolean subalgebra, \(\{0,1\}\); if it is closed under the extra operation, its only congruences are identity and universal, both of which extend. This proves the lower bound without computation.

The displayed eight-element closure operator supplies a direct obstruction. The stable four-element subalgebra \(\{0,4,3,7\}\) has a congruence with classes \(\{0,4\}\) and \(\{3,7\}\). The only Boolean congruence on the whole powerset algebra with that restriction is the kernel determined by bit \(4\), and it is destroyed by the pair \(1\equiv_4 5\) because their images \(1\) and \(7\) are not congruent. Thus the threshold eight is rigorous.

The exact census is exhaustive. The checker examines every one of the \(8^8\) unary operations, every proper Boolean subalgebra, every local congruence, and every global congruence. Burnside fixed-point counts independently reduce the labelled census to the isomorphism counts. Closure-operator filtering and the four representatives are checked inside the same direct enumeration.

## Originality

PASS. The closest recent source studies CEP as the algebraic form of the local deduction-detachment theorem, exhibits finite strongly non-additive CEP examples, and proves non-elementarity of the CEP class. It does not state a least finite CEP-failure size or enumerate all unary expansions of the first possible Boolean carrier.

The earlier no-CEP paper constructs many varieties lacking CEP and shows that combinations of normality, monotonicity, extensiveness, and idempotence are compatible with variety-level failure. It does not give the eight-element minimum, the complete \(8^8\) census, or the four isomorphism classes of minimal closure-operator failures.

Targeted published-finding and literature searches for smallest finite Boolean-frame CEP failures, eight-element censuses, and closure-operator counterexamples found no equivalent statement.

## Value

PASS. The recent literature establishes both abundant CEP behavior and abundant failure but leaves the finite onset opaque. The result locates the exact first carrier where a local extension obstruction can exist and quantifies the whole first layer. Showing that thirteen of the forty-five normal closure operators already fail CEP is especially informative because these are precisely the order-theoretic conditions emphasized in the surrounding modal-logic work. The four-class closure census is a compact finite testbed for deduction-theorem and CEP phenomena.

## Closest literature and limitations

Gyenis–Molnár–Öztürk (2026) is the direct recent source for Boolean frames with CEP and strongly non-additive examples. Gyenis–Molnár (2026, first preprinted in 2024) is the closest source for systematic varieties without CEP under modal-algebraic side conditions.

The result concerns individual finite algebras, not automatically their generated varieties, and does not attempt the sixteen-element layer.

Same-model review: passed. Independent audit: not yet performed.
