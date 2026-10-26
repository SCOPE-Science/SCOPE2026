# Scientific review: minimal total domination in complete-graph direct products

## Correctness — PASS

For every cell \((i,j)\), total domination is equivalent to a selected incidence edge avoiding both its row and column. A three-edge matching directly witnesses domination, while Kőnig's theorem forces an incidence edge set without a three-edge matching into a two-vertex cover. Mixed covers fail, and two-same-side covers yield exactly the two-plus-two minimality rule. The three structural classes give the stated labeled coefficients by independent choices and inclusion--exclusion. All eleven exhaustive small-parameter checks of the original open-neighborhood definition passed. The proof, not the finite sample, supports every integer \(2\le p\le q\).

## Originality — PASS, with residual risk

The minimum total domination number of \(K_p\times K_q\) is known from Henning--Kazemi (2012), and the \(K_n\times K_2\) upper parameter is known from Kazemi (arXiv:1603.02428). This result is instead the **complete inclusion-minimal set polynomial**, plus the all-factor upper value and the WTD classification. Kazemi's Question 1 asks the all-factor upper equality, and its \(k=1\) instance was not answered by the inspected text. Bahadır--Ekim--Gözüpek (arXiv:2010.02341) study WTD graphs; Burcroff--O'Brien (arXiv:2110.00709) study ordinary, rather than minimal total, domination polynomials for these products. Accessible published results and indexed mathematical records did not show the same statement or a stronger one implying it. Full-text and database coverage is not exhaustive; an independently published equivalent may exist.

## Mathematical value — PASS

The polynomial exactly counts all irredundant total-dominating configurations of a natural product family, not merely an optimum. The structural matching/vertex-cover dichotomy establishes a sharp two-versus-three factor-size transition in WTD behavior. The upper parameter also settles the \(k=1\) case of an explicit earlier question; no contribution for \(k>1\) is claimed. These consequences would not follow from the known scalar minimum, ordinary domination polynomial, or the special two-row upper result.

## Verification and limits

The bundled `check_minimal_total.py` reconstructs adjacency and checks every subset for eleven product graphs using open neighborhoods and one-vertex deletions. The argument uses Kőnig's matching--vertex-cover theorem for finite bipartite graphs. Remaining originality risk arises from unindexed or uninspected alternative literature, and the mathematical theorem is restricted to two complete factors and one-fold total domination.

Self-review: passed. Independent audit: not yet performed.
