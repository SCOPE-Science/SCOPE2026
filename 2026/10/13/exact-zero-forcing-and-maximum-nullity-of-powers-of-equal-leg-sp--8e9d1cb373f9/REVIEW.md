# Self-review

## Correctness
**PASS.** The proof supplies a concrete matrix in the graph-pattern class. The consecutive-window incidence matrix \(W\) has rank \(\ell-k\); hence \(D=WW^{\mathsf T}\) has a \(k\)-dimensional kernel and exactly the support of \(P_\ell^k\). The cross-leg block \(C\), within-leg block \(B=D+C\), and center vector reproduce the distance rules for the spider power. The subspace of \(m\) kernel vectors whose sum is zero has dimension \((m-1)k\) and is killed by the block matrix. This proves the lower bound on maximum nullity, while the standard \(M\le Z\) inequality and the published zero-forcing upper bound close the equality. Exact-arithmetic computation is corroborative, not foundational.

## Originality
**PASS.** The motivating preprint proves only the upper bound and then states exactly the equality as Conjecture 10. A plausible older dominating source, *Minimum rank of powers of trees* (2012), was inspected in full: it determines ordinary path-power minimum rank and studies strict powers of general trees, but does not state the ordinary equal-leg-spider power formula. Targeted searches across zero forcing, maximum nullity, spider powers, the \((m-1)k\) formula, and minimum-rank aliases found no covering theorem. The principal residual risk is the extreme recency of the conjecture and possible unindexed or later-revision work.

## Value
**PASS.** This is a natural exact classification for the canonical equal-leg spider family, resolves an explicit conjecture, and strengthens it by identifying maximum nullity. The proof exposes a simple matrix mechanism coupling path-power kernels across the legs, which is mathematically more informative than a bounded computation.

## Closest literature and limitations
The closest source is A. Abiad, M. Flagg, S. Ghasemi Nezhad, and S. Zeijlemaker, arXiv:2610.03892v1, Proposition 9 and Conjecture 10. The main older comparison is L. M. DeAlba et al., *Minimum rank of powers of trees*, DOI:10.13001/1081-3810.1511. The theorem does not address unequal-leg spiders, \(\ell\le k\), or arbitrary tree powers.

Self-review: passed. Independent audit: not yet performed.
