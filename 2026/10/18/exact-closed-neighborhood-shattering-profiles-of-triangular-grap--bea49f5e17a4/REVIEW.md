# Scientific review: closed-neighborhood shattering in triangular graphs

## Correctness — PASS

The finite rank-two Johnson context uses the *closed* radius-one ball: intersecting a center edge, including the center itself. Every trace is exactly the union of two endpoint stars. Shattering the empty trace forces two distinct unused ground vertices. Shattering each singleton edge forces at least one leaf endpoint; hence the selected-edge graph is a star forest. Shattering the full set forces at most two components. Partial-subset witnesses exclude a star of four edges, and exclude a three-edge star combined with another component. The remaining six star forests are sufficient, giving the exact classification without reliance on finite enumeration. Their placements count to the displayed coefficients; the threshold of two unused vertices is applied to each shape. The executable independently confirms all candidate sets of sizes through five for dimensions two through nine, and through four for dimension ten. The general size-four ceiling rests on the proof, not these experiments.

## Originality — PASS (qualified)

The primary comparison is Adler, Benediktsson, and Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs* (arXiv:2007.16042, 2020), especially Theorems 3.6–3.7 and Figure 4. Their exact Johnson result is for *open* neighborhoods; Figure 4 already gives an open-neighborhood four-set at dimension seven for the rank-two Johnson graph. The inspected text states boundedness of *closed* neighborhoods, but does not list the six closed-neighborhood types or this coefficientwise polynomial. Its open-neighborhood theorem does not imply the closed variant because adjoining centers changes the singleton and three-subset traces. The present size-four threshold is eight, not seven.

Bousquet et al. (arXiv:1407.5833) formulate graph VC dimension using closed neighborhoods and study hereditary classes and identifying codes, without these triangular-graph counts. Coudert et al. (arXiv:2405.07588) design general methods for computing graph VC dimension and give general bounds, not a formula for every shattered set in this symmetric family. Searches for alternative formulations included line graphs of complete graphs, two-star trace systems, shattering polynomials, and rank-two Johnson balls. Relevant published mathematical records concerning triangular-graph neighborhood homology and Johnson-graph Rips complexes address different objects/invariants. A relevant earlier finding on *Hamming* closed-neighborhood shattering has a different ambient set system and does not imply this classification.

The contribution is not the VC-dimension definition, the equality between triangular and rank-two Johnson graphs, or the known *open*-neighborhood theorem. No search certifies mathematical uniqueness; an equivalent classification under different names remains a residual priority risk.

## Mathematical value — PASS

A finite-structure neighborhood relation with a growing vertex universe admits only six precise geometric shattering patterns. The result gives the entire shattering distribution, not just a maximum, and detects a genuine open-versus-closed difference at the smallest dimension supporting four. The two-star trace lemma explains the restriction structurally, allowing exact counts for every ground size. This closes a natural exact parameter left unspecified by the comparison paper's boundedness observation and provides concrete data for finite-model-theoretic neighborhood set systems.

## Scope and residual limitations

The result is restricted to closed radius-one neighborhoods on \(J(n,2)\); it claims neither higher-rank Johnson classifications nor formulas for arbitrary line graphs. Searches did not exhaust all synonyms and inaccessible sources, so independent publication-priority assessment remains useful. Finite checking is complementary to, not a replacement for, the all-size proof. No independent external review has taken place.

Self-review: passed. Independent audit: not yet performed.
