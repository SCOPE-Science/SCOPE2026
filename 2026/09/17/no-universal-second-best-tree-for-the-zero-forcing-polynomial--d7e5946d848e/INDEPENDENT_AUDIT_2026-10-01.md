---
audit_date: 2026-10-01
status: passed
---

# Scientific audit

## Final claim

For every integer \(n\ge 11\), the coefficientwise poset of zero-forcing polynomials of nonpath \(n\)-vertex trees has no greatest element; explicitly the spiders \(A_n=S(2,2,n-5)\) and \(B_n=S(2,4,n-7)\) witness a strict loss for every nonpath tree in one of the coefficients \(2\), \(3\), or \(n-4\), so at least two coatoms lie below the path class.

## Correctness — PASS

The infinite proof was reconstructed from the package rather than inferred from its prior verdict. Menon–Singh path concatenation reduces every tree coefficientwise to a three-arm spider. For a spider \(S(a,b,c)\), the stated formulas \(z(2)=9-2t\) and \(z(3)=13n-66+2r\) give the first two case separations, while the fort argument separates \(A_n\) from \(B_n\) at size \(n-4\). An independent zero-forcing enumerator for \(n=11,12\) reproduced the critical counts, including \(z(A_{11};7)=329<330=z(B_{11};7)\) and \(z(A_{12};8)=494<495=z(B_{12};8)\). The finite check is corroboration; the case split and fort arguments establish all \(n\ge11\).

**Evidence.** RESULT.md; artifacts/spider_check.py blob 43e6e3d68f5c1b34dc1e360da6dbfd43dac7c055; Menon–Singh, Discrete Mathematics 348 (2025), 114516

**Residual risk.** The proof is for the tree subposet and does not identify all coatoms or claim a universal runner-up outside trees.

## Originality — PASS

The closest primary source proves path domination for trees and then explicitly asks what the coatoms below the path are; it does not answer the runner-up question. Boyer et al. introduce the polynomial but do not contain this second-level extremal theorem. A directly relevant 2025 paper on extremal forcing problems of trees was inspected in full and concerns zero, total, and connected forcing numbers rather than coefficient counts. Searches of the public findings corpus found the audited theorem itself and later, different zero-forcing extremal results, but no earlier theorem implying this pair-of-spiders obstruction.

**Equivalent formulations.** A greatest nonpath polynomial class is exactly a universal runner-up beneath the path in the tree subposet, so this search targets the same statement rather than a title match.

**Broader coverage.** Knowing the unique top class does not determine the coatoms or exclude a universal second-best nonpath tree.

**Exact database or table.** The claim is an infinite structural theorem, not a finite-table consequence.

**Claim versus prior implication.** An additional analysis of three-arm spiders and small forts is required to derive the final claim.

### Source inspections

- **Menon and Singh, DOI 10.1016/j.disc.2025.114516** — full open article, including Proposition 3.13, Corollary 3.14, and the concluding poset/coatom question. Supplies the reduction and explicitly leaves the audited second-level extremal question open.
- **Li, Cao and Ji, DOI 10.1007/s00373-025-02925-6** — full 10-page article. Concerns zero/total/connected forcing numbers, not zero-forcing polynomial coefficients or coatoms.
- **Boyer et al., arXiv:1801.08910** — abstract and indexed publication description. Introduces and studies the zero-forcing polynomial; no coverage of the audited tree coatom theorem found.

**Checked sources.** https://doi.org/10.1016/j.disc.2025.114516; https://arxiv.org/abs/1801.08910; https://doi.org/10.1007/s00373-025-02925-6; https://arxiv.org/abs/2605.10836; semantic search of the public findings corpus

**Residual risk.** A non-indexed specialist note could contain an equivalent coatom analysis, but the principal paper that introduced the current tree extremal question explicitly leaves it open.

## Value — PASS

The theorem answers a natural next extremal question explicitly posed after path domination, and does so uniformly for every \(n\ge11\) with a concrete two-witness obstruction. Determining the second layer of a natural coefficientwise poset is a motivated structural result rather than an arbitrary finite computation.

**Residual risk.** It proves nonexistence of a universal second-best tree rather than a complete classification of all coatoms.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
