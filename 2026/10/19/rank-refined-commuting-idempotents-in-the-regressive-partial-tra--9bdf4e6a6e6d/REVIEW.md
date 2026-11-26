# Independent mathematical audit

## correctness

PASS

Idempotency fixes every defined image, so at a nonfixed coordinate the only possible defined value is the greatest previous fixed point. Before the first fixed point only undefined is possible; choosing the first fixed point and then allowing fixed, undefined, or mapped to the last fixed point gives (3^n+1)/2. The commuting product is idempotent, and regression forces any fixed point of the product to be fixed by both maps. For a nonfixed coordinate, the four definedness choices yield equal composite values exactly under the stated tests on the two cross-values. If only e gains a fixed point, the cross-value can be nonzero only when f's last fixed point is common, and the other cross-value is unchanged; similarly for f. This checks that before a common point the cross-values are both zero, and that after a common point two exclusive last fixed points cannot both have nonzero cross-values: the later arrived while the other point was already exclusive. These facts check the three prefix recurrences and each post-common transition in RESULT.md lines 45–65. At every common point both last fixed points and cross-values reset, giving z^k ZH^k without interaction across segments. Solving the finite recurrences gives the displayed F; Z decomposes as (1/5)/(1-z)+(2/3)/(1-3z)+(2/15)/(1-6z), also yielding the empty-chain value. Independent raw enumeration through n=6 filtered all partial regressions by monotonicity and idempotency, and compared actual image ranks of equal compositions against all rank coefficients. Separate direct composition enumeration through n=7 also recovered the stated totals and rank-four polynomial at n=4 (the full polynomial there, not only its top coefficient). The proof in RESULT.md lines 38–74 is the replay path for all n. The frozen verify.py was read, not run. Its list of twelve transfer-state entries repeats ('E','E',0,0), so there are eleven distinct tuples; the dictionary recursion does not double-count that tuple. This is a supplemental description issue, not a count error.

## originality

PASS

The strongest comparison supplies the analogous product-fiber and rank series for total Catalan transformations. The reset idea is not claimed new in isolation. Undefined values in the partial case introduce new cross-value and domain-compatibility possibilities and a genuinely new no-common prefix: every total regressive map fixes 1, whereas rank zero is a whole exponential layer here. The known total fibers do not furnish these transition counts or the claimed generating series. No source inspected gives a dominating partial-map count.

## value

PASS

This determines the entire rank distribution of a natural product of commuting idempotents in a standard partial chain-transformation semigroup, not just a short sequence. The distinction between a no-common prefix and resets after common fixed points yields separate structural factors for all product ranks and a useful closed empty-product count. The general rank-resolved formula is not a relabeling of the total-map case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
