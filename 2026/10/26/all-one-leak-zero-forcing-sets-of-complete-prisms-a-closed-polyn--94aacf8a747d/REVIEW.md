# Self-review

## Correctness — PASS

The vertex-leak definition is quantified over every possible individual forbidden forcer. The proof first excludes initial configurations with two white vertices in each clique. For a nearly full layer with one omitted index, it identifies every possible initial forcer and proves the exact threshold of two eligible cross-layer supports, treating the three-vertex clique exception separately. It counts overlap between the two near-full cases without duplication and verifies the inclusion-minimal classification using single-deletion obstructions. The standalone `verify_leaky_prisms.py` independently implements the original one-leak process and exhausts all vertex subsets for the five graph orders from 3 through 7 (21,824 subsets), including complete and minimal histograms. Finite verification corroborates, rather than proves, the infinitely quantified statement.

## Originality — PASS, with priority limitations

The original leaky-forcing paper (Dillman–Kenter, arXiv:1910.00168, and its expanded journal version) defines the dynamics and provides graph-product bounds without the all-cardinality complete-prism polynomial. Alameda–Kritschgau–Warnberg–Young (arXiv:2008.06552) provide two-forcer resilience criteria, but their inspected results do not state the specialized polynomial or classify every inclusion-minimal complete-prism set. The similarly titled 2024 Herrman–Wisdom work treats categorical products, not the Cartesian prism here. The earlier zero-forcing-polynomial result for the same prism counts no-leak sets and cannot by itself determine the one-leak set family. General algorithms such as Wang's 2026 compression framework could in principle derive special cases but their consulted text does not present this formula. Mathematical-index searches and accessible prior research claims gave no explicit equivalent. Residual risk: an unindexed or alternative-reliability formulation might contain the same special-case statement, or a general result might specialize directly without being readily indexed.

## Mathematical value — PASS

The finding gives a complete all-budget robustness distribution, with an exact overlap-aware polynomial and a classification of inclusion-minimal robust configurations throughout an infinite graph family. It reveals that the ordinary zero-forcing and one-leak forcing minima both have size \(n\), but only the two whole layers attain the robust minimum, and nonminimum irredundant robust sets occur in \(2n\binom{n-1}{2}\) configurations of size \(n+1\) for \(n\ge4\). This is relevant to one-component failure tolerance and goes beyond a scalar optimum or a routine renaming of the ordinary forcing polynomial.

## Scope and limits

Finite checks stop at \(n=7\); the infinite claim depends on the supplied proof. The result assumes exactly the standard zero-forcing rule and at most one unavailable forcing vertex; no extension to two leaks or more is asserted. The interpretation of the 2026 general leaky-forcing polynomial literature is bounded by the inspected accessible text. Literature searches cannot rule out all prior specializations.

Self-review: passed. Independent audit: not yet performed.
