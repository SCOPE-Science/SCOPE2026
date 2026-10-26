# Scientific review

## Correctness — PASS

The proof establishes the source-index-uniform dominant-root estimate, derives exponentially small algebraic-logarithm gaps from any hypothetical step, and applies the standard Baker–Wüstholz lower bound to exclude digit lengths below an exponential function. For existence, it obtains uniform interval visits from the Erdős–Turán inequality and a polynomial Diophantine bound on the algebraic logarithm ratio. The chosen visit has index increment at least exponential in the starting index, making the nondominant-root error smaller than one third of a digit unit; the interval endpoints then give an integer appended block with the required sign. The even-index restriction covers negative dominant roots. Exact finite arithmetic corroborates three sequence families. Nonstandard input is a standard published theorem about linear forms in logarithms, not a heuristic.

## Originality — PASS, with residual risk

The fully inspected source [1, Theorems 1.2–1.3 and Lemma 4.1] proves qualitative unbounded necessity and unlimited existence, not the two-sided exponential law for the minimal digit length. Full text [2, Theorems 3.1 and 4.2] bounds walk length for a prescribed digit cap, not this source-index-dependent invariant. Exact and conceptual literature searches for effective digit-appending steps, Diophantine approximations, exponential return times, and closest published mathematical records found no directly covering claim. A broader Diophantine-approximation source could nevertheless imply it indirectly; the absence of a search hit does not certify novelty. Earlier [5] was reviewed at abstract level only.

## Mathematical value — PASS

The natural invariant is the *least* outgoing appended digit length at a specified term, left unquantified by the qualitative existence theorem [1]. Establishing matching exponential order for every recurrence of the source's broad class is a structural transition, and the proof identifies both independent mechanisms that determine the scale: algebraic logarithm separation (necessity) and effective visits to a shrinking interval (sufficiency). It does not assert an exact exponent or a new result about bounded-length walk termination.

## Closest literature and limitations

Sources: [1] Mosahab et al., arXiv:2610.18919v1, full Sections 1–4; [2] Kominers, arXiv:2512.06446v1, full Sections 1–4; [5] Miller et al., arXiv:2204.08138, abstract. The result needs multiplicative independence and a unique simple dominant root. The constants are nonsharp, dependent on the recurrence, and may be very large; it makes no assertion for dependent bases. Independent external review is outstanding. Known general results about Baker bounds and Erdős–Turán discrepancy could make the proof method familiar but do not directly state the claimed invariant in the checked sources.

Self-review: passed. Independent audit: not yet performed.
