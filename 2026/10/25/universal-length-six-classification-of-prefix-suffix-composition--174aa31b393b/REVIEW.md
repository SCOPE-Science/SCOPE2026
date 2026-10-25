# Scientific review

## Correctness — PASS

The proof reduces a deck to two unordered inward Parikh paths and establishes a unique-matching lemma whenever both path vertices are separated at consecutive depths. At length six, an independent choice modulo reversal requires two separated excursions joined at depth two; this forces and completely classifies the four-word fibers. Counting palindromes and reversal doubletons gives the exact distribution for every finite alphabet size. The standard-library checker independently computes two deck representations and tests all fibers for alphabet sizes two through seven and word lengths one through six. Finite checks do not establish the unrestricted alphabet case; the matching lemma and case analysis do.

## Originality — PASS, with residual risk

Ye–Elishco (arXiv:2208.14963, Example III.6 and Corollary III.12) proves the binary minimal collision and the binary short-length reconstruction threshold; these are acknowledged as prior. The present claim adds all alphabet sizes, a canonical bijection of four-word fibers with ordered pairs of two-element subsets, the full exact fiber distribution and the resulting code cardinality. The inspected Gabrys–Pattabiraman–Milenkovic source (arXiv:2110.02352) addresses binary multistring reconstruction and rates; the inspected Chen work (arXiv:2503.12342) addresses binary error correction. Searches of mathematical records and published sources did not identify the alphabet-uniform formula. Unknown equivalences under alternate terminology remain a risk.

## Mathematical value — PASS

The first failure length and complete obstruction families are intrinsic reconstruction properties. In contrast to merely counting a few words, the theorem provides a full alphabet-uniform classification, an exact zero-error code-size benchmark and genuinely four-symbol collision families that cannot arise by binary relabeling. The result is limited to lengths through six; it does not claim an asymptotic extension.

Self-review: passed. Independent audit: not yet performed.
