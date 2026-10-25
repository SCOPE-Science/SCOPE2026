# Review: fixed-prefix rigidity of finite atomic one-location stopping sets

## Correctness

**PASS.** Strictly positive Poisson means give full support on every finite count vector; hence an almost-sure one-occupied-site bound holds pointwise. The restriction property forces a first queried atom from the all-positive vector, forces its inclusion in every output, and then forces immediate stopping whenever its count is positive. The zero-count fiber inherits the stopping property, closing an induction on the number of atoms. Unique induction supplies the partial-permutation count; explicit one-atom jumps supply exact exploration. An independent cylinder-cover enumeration exhausts small binary/ternary instances. No finite enumeration is used as an infinite proof.

## Originality

**PASS, with residual risk.** Khezeli's arXiv:2610.22011v1 Theorem 1.3 assumes a diffuse intensity and gives attainability up to null-set modifications; its atomic CTDT definition does not supply the present exact finite-atomic classification. Last–Peccati–Yogeshwaran arXiv:2101.07180v3 provides general stopping-set axioms and nonattainability examples, not this one-location normal form or partial-permutation count. Targeted theorem-phrase searches and primary-literature comparisons did not identify a covering theorem. A classical finite decision-tree normal form may implicitly contain the result, and the present proof uses elementary induction.

## Mathematical value

**PASS.** The result answers the natural finite atomic analogue of one-point stopping-set attainability with a complete exact classification. It shows that a probabilistic one-occupied-location constraint eliminates all adaptive query-order choices despite arbitrarily large observed multiplicities, gives a closed count for the entire admissible class, and upgrades attainable equality to every count configuration. The two-occupied-location example sharply separates the rigid regime from genuinely adaptive branching. The result does not imply the diffuse or infinite-atomic analogue.

## Closest literature and limits

The nearest source is Khezeli, *On Stopping Sets and Continuous-Time Decision Trees*, arXiv:2610.22011v1, Theorem 1.3 and Remark 4.2. Last, Peccati and Yogeshwaran, arXiv:2101.07180v3, Appendix B, show that generic stopping sets need not be attainable. The all-configurations conclusion uses strict positivity of every Poisson rate. Finite verification does not replace the proof. Potential implicit coverage in classical finite sequential-query literature is a remaining risk.

Self-review: passed. Independent audit: not yet performed.
