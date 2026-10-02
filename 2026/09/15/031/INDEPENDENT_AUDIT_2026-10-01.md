# Independent scientific audit — Closed q-binomial expansion for the corner-weighted rectangle generating function

Audit date: 2026-10-01 (UTC) UTC.

## Disposition

**PASSED**

## Correctness

**PASS** — The proof was reconstructed from the multiplicity-marking product: expanding in elementary symmetric functions gives q^{i(i+1)/2}[m choose i]_q, summing complete symmetric functions gives [m+l-i choose l-i]_q, and applying the binomial transform L_z yields binom(z-1,i). Fresh exact enumeration matched the formula for (2,3,3), (3,4,3), (3,4,3/2), and (4,4,2), including the filed coefficient vector for (3,4,3).

## Originality

**PASS** — No equivalent or stronger prior formula was found after searches by statistic, q-factor, and rectangular partition language.

Equivalent formulations: The formula is not merely the ordinary Gaussian polynomial: it retains a corner/distinct-part-size weight and a nontrivial binomial transform.

Broader coverage: No stronger coverage was located that mechanically specializes to the stated identity.

Exact database or table: The claim is symbolic and uniform rather than a finite table entry, so exact-database coverage is inapplicable after targeted search.

Claim versus prior implication: Best-of-knowledge comparison supports originality; unsuccessful search is retained as a limitation, not treated as proof by itself.

Checked sources: https://doi.org/10.1016/j.jcta.2003.11.009, https://arxiv.org/search/?query=corners+partitions&searchtype=all, Resultary semantic search for 031 claim aliases.

Residual risks: A specialized older partition identity may encode the same transform under different notation; this remains the principal originality risk.

## Scientific value

**PASS** — This is a uniform closed-form identity for a natural statistic on all rectangular partitions, not a finite slice. It compresses the target weighted sequence into standard Gaussian-polynomial pieces and isolates why unimodality is nontrivial; that structural reduction is a worthwhile mathematical result even though the original unimodality problem remains open.

## Scope

This audit evaluates the mathematical claim and the cited reproducibility evidence. It does not convert computational evidence into a stronger theorem than the evidence actually establishes.
