---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

For every nonempty set of radii \(\mathcal R\subset(0,\infty)\) with unbounded logarithmic diameter and every \(1<p<\infty\), the one-dimensional centered Hardy–Littlewood maximal operator restricted to \(\mathcal R\) has exact \(L^p\) norm \(p'=p/(p-1)\); finite subsets of \(\mathcal R\) already admit smooth compactly supported near-extremizers.

## Correctness — PASS

The unrestricted upper bound is Madrid's exact norm. The lower construction was independently reconstructed: the finite product martingale has maximal-to-terminal ratio tending to \(p'\); unbounded logarithmic diameter supplies arbitrarily long multiplicatively separated finite radius chains; the base-\(B\) digit model freezes past coordinates and averages future coordinates with explicit boundary error; periodic localization and \(L^p\)-stable smoothing preserve the ratio. Numerical checks of the martingale constant \((1-q)/(1-q^{1/p'})\) for large \(B\) converge to \(p'\) for several \(p\).

**Checked sources.** frozen assigned RESULT.md; Madrid arXiv:2609.12440 abstract; Wei–Nie–Wu–Yan 2016 open-access full article

**Residual risks.** Madrid's full preprint remained inaccessible, so only its exact unrestricted theorem from the primary abstract was used.

## Originality — PASS

Wei–Nie–Wu–Yan prove equality for the continuous truncation \(0<r<\gamma\), and Madrid's current work gives the unrestricted exact norm; the assigned result is stronger in a different direction, allowing arbitrary irregular or superlacunary prescribed sets with only scale escape. Resultary returned no earlier arbitrary-radius theorem.

### Equivalent formulations

A full interval of radii is much richer than an arbitrary escaping sparse set, so the 2016 truncation theorem does not imply the final claim.

### Broader coverage

A single geometric sequence does not dominate all arbitrary irregular sets.

### Exact database or table

No numerical table is relevant.

### Claim versus prior implication

The finite-subfamily near-extremizer theorem is the additional nontrivial implication.

**Checked sources.** https://doi.org/10.1186/s13660-016-0963-x; https://arxiv.org/abs/2609.12440; Resultary semantic search

**Residual risks.** Madrid's full text was not obtained; if it contains a theorem for arbitrary prescribed radius sets, originality would need revision. This inaccessible plausible source alone was not taken as a failure under the stated audit rule.

## Value — PASS

The theorem shows a sharp rigidity phenomenon under arbitrarily severe scale thinning and gives finite prescribed-scale near-extremizers. That is a natural structural strengthening of a newly solved sharp-norm problem and is not an arbitrary finite slice.

**Residual risks.** The result is one-dimensional and leaves radius sets in a compact annulus and endpoint/higher-dimensional questions open.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
