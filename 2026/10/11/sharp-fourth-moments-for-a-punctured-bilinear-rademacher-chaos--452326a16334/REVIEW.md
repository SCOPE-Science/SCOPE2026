# Scientific review of the punctured bilinear fourth-moment theorem

## Correctness — PASS

The statement treats all real arrays supported on exactly \(K_{n,n}\setminus\{(n,n)\}\), with \(n\ge2\) and normalized uniform sign measure. The complete fourth-moment expansion follows from counting repeated-edge terms and genuine four-cycles. The two independent root-mean-square symmetrizations have explicit Cauchy--Schwarz witnesses for every affected rectangle, and the quartic self-terms can only decrease. The reduced three-block form has the exact sum-of-squares deficit \((6k^2+k-4)(p-p_*)^2/k^2+(q-r)^2/k\); this proves sharpness globally, not just at tested dimensions. Positivity of every optimal magnitude and generation of graph cycles by four-cycles determine all possible signs. The actual embedded `verify.py` was executed and returned `VERIFY_OK`, including symbolic identities and direct sign sums. Neither numerical tests nor cycle-space checks at finitely many dimensions substitute for the written infinite-family proof.

## Originality — PASS with residual risk

Ibragimov--Sharakhmetov--Cecen [1, principal results and proofs] obtains moment estimates over variable distributions for complete ordinary/decoupled bilinear sums; its exact constants do not provide the weighted single-hole coefficient-space maximization. Pass--Spektor [2, Theorem 2.1] changes dependence assumptions among signs, rather than deleting one coefficient in a fixed independent two-family product. Döbler--Krokowski [3, Theorem 1.1] gives normal-approximation bounds driven by fourth moment and influence; it does not state the sharp punctured support norm. Direct finite-dimensional Khintchine tensorization covers the full support but gives the strictly weaker constant \((3-2/n)^2\). Searches of indexed mathematical records for coefficient-hole, missing-edge, Walsh-support and precise-formula equivalents did not identify a covering theorem. The known full quadratic chaos constants for all edge supports are also weaker than the claimed restricted-support optimum; restriction alone does not prove sharpness. There remains a material risk of unindexed or differently phrased prior work, and the entire unrelated literature has not been exhaustively inspected.

## Value — PASS

The support is a canonical one-edge deletion from a rank-one tensor product of first-level Rademacher spaces. The exact operator norm of its \(L^2\)-to-\(L^4\) identity embedding is a natural geometric/hypercontractive invariant. The theorem supplies an all-dimensional rational constant, complete two-level extremizers, and an exact strict loss relative to the full tensor product with \(n^2\)-rescaled limit \(6\). It therefore distinguishes a genuine structural effect of deleting a single interaction, rather than repackaging a general hypercontractive bound, selecting arbitrary coefficients, or computing a known table entry.

## Scope and bibliographic limitations

This is a real-scalar fourth-moment statement, not a complex-scalar bound, a Banach--Mazur distance computation, or a multiple-hole classification. Equation (9) of the result is a deficit identity on the symmetrized three-block family, not an asserted global coefficient-stability remainder. The closest original bilinear-moment source was inspected through its relevant theorems and proof; additional historical specialized texts may remain undiscovered. Independent assessment is not supplied.

## Primary references

[1] R. Ibragimov, Sh. Sharakhmetov, A. Cecen, *Exact Estimates for Moments of Random Bilinear Forms*, arXiv:math/9909111, https://arxiv.org/pdf/math/9909111.

[2] B. Pass, S. Spektor, *On Khinchine type inequalities for pairwise independent Rademacher random variables*, arXiv:1412.7859, https://arxiv.org/pdf/1412.7859.

[3] C. Döbler, K. Krokowski, *On the Fourth Moment Condition for Rademacher Chaos*, arXiv:1706.00751, https://arxiv.org/pdf/1706.00751.

Same-model review: passed. Independent audit: not yet performed.
