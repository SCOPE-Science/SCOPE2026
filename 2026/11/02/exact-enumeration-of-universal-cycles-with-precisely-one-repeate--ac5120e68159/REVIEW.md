# Scientific review

## Correctness — PASS

The overlap digraph has a vertex for each ordered pair and exactly one edge per allowed length-three triple. Its diagonal degrees are \(q-1\), off-diagonal degrees are \(2\), and it is strongly connected, so the Euler-tour interpretation is exact. Prescribing the edge `001` fixes one rotation per universal cycle. The directed BEST factor is consequently \(((q-2)!)^q\). The directed Laplacian Schur complement is \(2(qI-J)/3\) after eliminating all off-diagonal vertices, and the rooted cofactor is \(2^{q-1}3^{(q-1)(q-2)/2}q^{q-2}\). These steps establish the all-\(q\) formula, independently of finite checks. Exact integer cofactors were recomputed through \(q=8\); direct Euler-tour counts through \(q=4\) and constructive witnesses through \(q=25\) independently agree. The remaining scientific boundary is the stipulated alphabet and factor predicate.

## Originality — PASS, qualified

Relevant complete published sources inspected include Gardner–Godbole (2017), especially its restricted/equitable/onto-word theorems, and Sawada–Sears–Trautrim–Williams (2023), especially its cycle-joining construction results; the Chen–Kitaev–Sun (2019) deletion paper was also examined. Their relevant claims provide existence, general construction principles, or small deletion enumeration, not the exact count for the three-letter pattern with exactly one repeated symbol. Targeted source/alias searches and comparison against available specialized records found no covering result. Existing BEST and matrix-tree machinery is acknowledged: originality concerns the evaluated closed product for this complete natural restricted language. The 2013 Champlin–Godbole–Tomlinson paper was accessible as an abstract and by its quotation in Gardner–Godbole, but its original full text was unavailable; a specialized count there or in other unindexed literature remains the leading originality risk. Absence of a search hit is not proof of uniqueness.

## Mathematical value — PASS

Universal cycles are minimal exact compact listings of constrained word families. This natural family is the complete length-three equality-pattern class with exactly two equal symbols, removing both the all-distinct and constant triples. The theorem gives a closed all-alphabet count rather than just an existence criterion or a finite small-alphabet list, and determines the rooted arborescence count for its nontrivial \(q^2\)-vertex overlap graph. The explicit factorization and exact symbol balance support sequence-design enumeration under local equality constraints. This is a motivated complete enumeration of the restricted language; it does not purport to improve the general BEST theorem.

## Closest literature and limits

- Gardner and Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029v1 (2017): related existence theorems for restricted words; no reported full-alphabet count for this exact class.
- Chen, Kitaev and Sun, arXiv:1908.01116v1 (2019): deletion-family existence probabilities, not this exhaustive restricted triple family.
- Sawada, Sears, Trautrim and Williams, arXiv:2308.12405v1 (2023): efficient cycle-joining, not this arborescence evaluation.
- Champlin, Godbole and Tomlinson, arXiv:1303.3323 (2013): related non-injective language result, but full text was not available for inspection.

Finite checks are not infinite proofs, and no claim is made for unlabeled or reversal-quotiented cycles, longer factors, or other constraints.

Self-review: passed. Independent audit: not yet performed.
