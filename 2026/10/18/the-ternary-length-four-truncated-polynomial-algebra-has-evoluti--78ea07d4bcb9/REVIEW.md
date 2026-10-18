# Scientific review

## Correctness — PASS

The four coordinate quadrics of squaring in \(\mathbb F_3[t]/(t^4)\) are specified explicitly. An eight-square decomposition is checked by exact coefficient expansion. An exhaustive finite Grassmannian reduction proves the lower bound: there are \(33880\) quotient three-planes, and none supports all four target quadrics. The same row-echelon method enumerates all \(11011\) quotient four-planes and proves the exact \(252\)-support census. The provided `VERIFY.py` independently recomputes all arithmetic from definitions with no nonstandard dependencies. The unital evolution-envelope/Waring-rank equivalence is the established theorem of Costoya, Fernández Ouaridi and Viruel (arXiv:2609.32784, Sections 3–4).

## Originality — PASS, subject to bibliographic uncertainty

The September 26, 2026 motivating article treats the generic field-size regime and explicitly reports only the strict lower bound \(\operatorname{wr}>7\) in this exceptional ternary case (Remark 5.4). Its stated results do not give the exact eight-square witness or the \(252\)-space census. Relevant searchable published findings were queried under the finite-field algebra, Waring rank, square-zero comparison, and evolution-envelope aliases. The closest indexed square-zero result applies to a different algebra: this truncated polynomial ring has nonzero radical square. Earlier Winograd-type studies concern bilinear multiplication complexity; their abstracts do not settle the symmetric quadratic-support census. Unindexed, older algorithm-classification literature remains a specific residual risk, rather than a claim of proven uniqueness.

## Value — PASS

The object is the first finite-field exception explicitly singled out by the motivating paper's interpolation threshold, not an arbitrary unmotivated parameter choice. The exact minimal embedding dimension fills the specific numerical gap; the \(252\) support spaces and their \(243/9\) incidence split describe the landscape of optimal simultaneous decompositions. These are natural invariants of the minimal-envelope problem and a starting point for studying uniqueness questions. No equivalence of support spaces with isomorphism classes of envelopes is claimed.

## Closest literature and limits

Costoya–Fernández Ouaridi–Viruel, arXiv:2609.32784v1, Sections 3–5 and Remark 5.4, is the closest primary source. Winograd, DOI 10.1007/BF01683270, and Randriambololona, arXiv:1107.0336, are historical related references. The exact statement is over \(\mathbb F_3\) only, relies on an exhaustive finite certificate, and has no independently completed audit. The possible coverage by an inaccessible older symmetric-bilinear algorithm table is not excluded.

Self-review: passed. Independent audit: not yet performed.
