# Review: delay-spread robustness of master-sequence extinction

## Correctness — PASS

The exact normalized delay equations give \(S'=\Phi(1-S)\), coordinatewise positive invariance, and \(\Phi\leq NM\). Applying \(x_j'\geq-NMx_j\) between the delayed sampling times and their common earliest time yields the essential nonstandard bound \(\sum_jx_j(t-\tau_j(t))\geq e^{-NM(b-a)}\) for \(t\geq b\). Fitness dominance produces a uniform lower bound on \(\Phi\) relative to \(f_0\). A scalar retarded supersolution, with its rate defined by a strictly monotone characteristic equation, gives the stated exponential estimate. Each assumption is used; the full infinite-time claim follows by comparison, not by simulation. The exact example is checked by `verify.py`.

## Originality — PASS with declared residual risk

The closest directly relevant 2026 primary result (Morales–Turner–Zapata, Theorem 3) explicitly assumes equal delays, whereas the new proof provides a quantified unequal-delay criterion and exponential bound. Full readings of arXiv:2412.10475 and arXiv:2508.12424 show equal-lag stability conclusions for the earlier two-genotype model and different backward-mutation periodicity results for a generalized model, respectively. Scientific queries for heterogeneous quasispecies delays, delay-spread extinction and exponential comparison uncovered no directly dominating result in the checked literature or published mathematical-record results. These searches are not a proof of universal uniqueness. The motivating article's indexed Theorem 3 and proof discussion were inspected, but its full publisher text could not be retrieved; an unindexed theorem or appendix remains a material residual risk.

## Value — PASS

Equal delays permit an exact normalization of the delayed genotype masses, but heterogeneous delays destroy that identity. The new asynchronous sampling inequality repairs it quantitatively: an extinction guarantee depends on \(b-a\), not on the size of the common lag. In applications to delayed genotype replication this distinguishes biologically interpretable delay dispersion from slow absolute synthesis, and yields an infinite-time rate for an open family of parameter choices rather than a single simulation or tiny arithmetic refinement. The three-class rational example demonstrates genuinely unequal delays and nonconstant fitness. The threshold is conservative and no empirical prediction is asserted.

## Literature and limitations

References: Morales–Turner–Zapata (2026), DOI 10.1080/17513758.2026.2631218; Turner–Crespo–Sardanyés–Morales (2024), arXiv:2412.10475; Morales–Turner (2025), arXiv:2508.12424. The original 2026 article could not be read in full during this comparison, and general-purpose scalar delay-comparison methods are pre-existing mathematics. Strict condition only; equality and failure of the condition are not classified.

Self-review: passed. Independent audit: not yet performed.
