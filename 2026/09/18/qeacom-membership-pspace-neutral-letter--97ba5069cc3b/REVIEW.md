# Review: QEACom membership and neutral-letter collapse

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The neutral-letter lemma follows directly from two statements in the source paper: for a neutral-letter language the stable syntactic semigroup is the whole syntactic monoid, and EACom is defined by the identities `epx^(omega+1)qf = epx^omega qf` and `epxyqf = epyxqf`. Substituting the monoid identity for `e,f,p,q` yields aperiodicity and commutativity; the converse is immediate.

The PSPACE upper bound reuses the source paper's polynomial-space procedures for testing stable transition-semigroup membership and syntactic equality of stable representatives. The only additional operation is computing `x^omega`. In a finite monogenic semigroup with at most `N` elements, an idempotent power occurs among the first `N` powers. Since an NFA with `q` states has at most `2^(q^2)` Boolean transition matrices, sequential powering needs only a polynomial-size matrix and counter. Every syntactic idempotent has an idempotent stable preimage by taking the omega-power of any stable preimage, so restricting `e,f` representatives to idempotent matrices does not miss witnesses.

The hardness reduction was checked for both branches of the special universality instances used in the source paper. The auxiliary language is `(Delta* \ Sigma+ c d) union L(A)c d`, so it is constructible without complementing the input NFA. After adding loops for the erasing neutral symbol, the universal branch becomes the universal positive-word language. In the one-missing-word branch, `wcd` is rejected and `wdc` accepted, which witnesses noncommutativity of the syntactic monoid. The neutral-letter lemma therefore excludes QEACom.

The circuit consequence correctly combines Proposition 6.8 (`QEACom` gives `O(log n)`), Corollary 4.16 (neutral-letter constant complexity iff idempotent and commutative), and Theorem 4.17 (failure of `QEJ1` gives Hardy--Littlewood `Omega(log n)`, i.e. a logarithmic lower bound on infinitely many lengths). It deliberately does not upgrade that weaker lower-bound convention to standard `Theta(log n)`.

The finite verification artifact is consistent with the algebraic claims but is not used as a substitute for proof.

## Originality

**PASS, to the best of our knowledge.**

The full text of Göller--Manuel arXiv:2609.18484 was inspected. It introduces QEACom, gives its algebraic/logical/congruence characterizations and its `O(log n)` circuit upper bound, and proves PSPACE-completeness of the separate problem of deciding constant circuit complexity from an NFA. It does not state PSPACE-completeness of QEACom membership, the neutral-letter QEACom=ACom collapse as a theorem, or the restricted hardness result.

Targeted searches used `QEACom`, `EACom`, NFA membership, PSPACE, neutral letter, commutative aperiodic, commutative star-free, and syntactic-monoid variants. The exact QEACom terminology returned the recent source paper but no separate complexity result. Older literature confirms that aperiodicity/star-freeness testing is PSPACE-complete and that commutative star-free languages are a classical class; those facts are excluded from the novelty claim.

The 2013 Delaney--Stapleton--Taylor--Thompson work on commutative star-free languages was identified as the closest structural prior literature. Its publicly available bibliographic/abstract description concerns expressive characterizations rather than NFA membership complexity. The generic truncated-Parikh/commutative-star-free viewpoint is therefore not claimed as new. No inaccessible source was identified as specifically likely to contain the QEACom membership theorem. The principal residual risk is temporal: QEACom itself was introduced only days ago, so a near-simultaneous note or later revision could contain the same observation.

## Value

**PASS.**

The result completes a natural algorithmic question left beside the source paper's QEACom characterization. It also shows that hardness survives a strong semantic restriction: the language can be promised to have a neutral letter. The delimiter construction is necessary because the source paper's one-missing-word neutralization need not leave QEACom: unary threshold behavior can remain aperiodic and commutative. Adding two ordered fresh delimiters forces a syntactic commutation failure in the negative branch.

The neutral-letter collapse supplies a concise interpretation of the class and turns the source paper's upper and lower bounds into an exact O(1)-versus-not-o(log n) jump inside an O(log n) envelope for this subclass.

## Verification state

- review_type: `same_model_review`
- independent: `false`
- same_model_review_status: `passed`
- independent_audit_status: `not_performed`
