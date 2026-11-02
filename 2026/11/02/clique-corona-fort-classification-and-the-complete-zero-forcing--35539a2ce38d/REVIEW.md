# Self-review

## Correctness — PASS

All hypotheses and quantifiers have been checked for an arbitrary finite simple base graph of positive order (including isolated vertices and disconnected bases) and private clique sizes at least two. The local-pair fort, the core/private singleton correspondence, and its minimality equivalence are proved by outside-neighbor counts; the fort-hitting characterization is established directly by the stalled-white-set argument. The independent local-case partition yields every coefficient with no double counting. Leading exponents prove the minimum and its multiplicity. The attached `VERIFY.py` tests 104 graph-corona instances and 537,504 vertex subsets, comparing both full distributions. Finite enumeration is corroboration rather than a proof for infinite families.

## Originality — PASS (provisional publication priority)

The closest directly inspected primary source is Becker et al., *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963v1 (2024-04-09), Section 5.2, Propositions 22 and 23 and adjoining comments (PDF pp. 13–15). It gives the existence of peripheral minimal forts and a cycle-base lifting construction. It warns that the lifted construction can fail for general bases with a single pendant attached vertex. It does not classify **all** minimal forts for arbitrary bases with private cliques of size at least two or derive the exact zero-forcing polynomial for these coronas. The 2016 Javaid et al. theorem yields the uniform scalar zero-forcing minimum but no coefficientwise formula. Boyer et al. (2018) define the zero-forcing polynomial without this transfer; Abara–Pelayo (2022) address maximal failed sets of graph products. Searches included possible corona/blowup, fort-transversal, polynomial-substitution, and full-strength implication formulations. The strongest identified comparisons are narrower, not equivalent. Unindexed literature and later journal revisions remain residual risks; no independent publication-priority certification has been performed.

## Mathematical value — PASS

The exact fort-hypergraph classification and full zero-forcing polynomial reduction work for **every** graph, not merely one family, and permit heterogeneous private clique orders. The polynomial computes every size-count and the exact multiplicity of minimum forcing sets; the scalar minimum had already been known. The essential threshold at private clique size two explains a genuine structural boundary. This is substantially more informative than a routine minimum-parameter corollary or a table of special examples.

## Verification limits

The independent calculations only cover bounded graph sizes and do not certify the infinite theorem or publication priority. The proof provides the infinite coverage. The attached reproducer was run successfully. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
