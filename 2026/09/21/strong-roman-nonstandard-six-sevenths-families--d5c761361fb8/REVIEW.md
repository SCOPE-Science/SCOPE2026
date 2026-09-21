# Scientific review

## Correctness

The central claim is supported by matching analytic lower and upper bounds. For either seven-vertex block, only the root may have neighbors outside the block. A case analysis on the root label proves that every strong Roman dominating function contributes at least six units to each block; external zero neighbors of the root can only strengthen the required defense threshold. Explicit weight-six labelings exist for both blocks and remain valid after roots are joined because every root is positive. Summing over disjoint blocks proves the exact global formula.

The nonisomorphism claim is also structural. A standard subdivided-claw rooted product on 7m vertices has exactly 3m degree-two vertices when m is at least two, whereas a mixed graph with r triangularized blocks has 3m-2r. The one-block case is separated by acyclicity versus unicyclicity.

A finite exhaustive check independently confirms the local minima and all connected graphs through seven vertices. The computation is evidence rather than a substitute for the proof.

**Correctness assessment: PASS.**

## Originality

The 2017 source proves the 6n/7 bound for trees, characterizes its tree equality cases, asks whether the upper bound extends to all connected graphs, and proposes the subdivided-claw rooted products as the equality class if it does. The new triangularized block has the same exact ratio but is not in that class, and it can replace any positive number of blocks over an arbitrary connected base.

The 2018 follow-up proves the bound for several special families and leaves the general problem open. The 2020 paper treats unicyclic graphs and proves an edge-addition observation for the known extremal tree family, but no exact classification or repeatable triangular-block equality mechanism equivalent to the present theorem was located. The 2026 specific-family paper likewise did not yield an equivalent statement under searches for the 6n/7 bound, rooted products, unicyclic equality, subdivided claws, or synonymous strong-Roman formulations.

The most important residual risk is the 2022 paper on linear-time computation for trees and unicyclic graphs: its abstract and bibliographic information were inspected, but its full theorem text was not. It could contain the seven-vertex unicyclic example or an equivalent local observation. A 2021 survey/book-chapter treatment of Roman-domination variants was also not checked theorem by theorem. Neither limitation presently gives concrete evidence that the mixed-block theorem is already covered.

**Originality assessment: PASS, to the best of our knowledge.**

## Value

The result corrects the proposed equality-side picture surrounding a long-standing general upper-bound problem without claiming to settle that upper bound itself. It supplies a second exact seven-vertex building block, a self-contained local mechanism, and infinitely many mixed connected equality families over arbitrary connected bases. This is more informative than an isolated counterexample because the construction explains why the exact 6/7 ratio persists under arbitrary root gluing.

**Value assessment: PASS.**

## Limitations

The universal conjecture gamma_StR(G) <= 6|V(G)|/7 for connected graphs remains open. The result does not classify all equality graphs. Originality is to the best of our knowledge, with the 2022 unicyclic-algorithm paper and broader survey literature remaining the most plausible unchecked sources for partial prior overlap. The finite enumeration only covers graphs through seven vertices.

**Same-model review: passed. Independent audit: not yet performed.**
