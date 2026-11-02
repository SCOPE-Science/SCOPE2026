# Scientific review: five-bit binary square superstrings

## Correctness — PASS

The reduction from ordinary linear factor containment to a \(32\)-vertex weighted overlap Hamiltonian path is valid in both directions for equal-length distinct required squares. The five-bit root necklace partition has two singleton classes and six five-cycles. Every cross-necklace edge costs at least six appended bits; every within-necklace edge costs at least one. Hence at least seven crossings are needed and nine or more imply a word of length at least \(86\). The seven-crossing case is an exact eight-block subset dynamic program, producing minimum \(82\). At eight crossings, the only possible length-\(81\) paths require one split five-cycle and solely minimum-cost edges; all \(120\) split configurations fail a finite nine-block reachability test. The literal \(82\)-bit witness was directly checked by exhaustive enumeration of all \(32\) required factors. Both the standard-library verifier and the alternate integer optimization code executed successfully. The conclusion does not rely on finite enumeration to extrapolate to other root lengths.

## Originality — PASS, with bounded priority risk

The closest primary source is Au's 2009 preprint, revised in 2015. Its exact square-covering definitions and generic lower bound cover this parameter, and its Algorithm E already provides an \(82\)-bit construction here. Neither inspected presentation claims that the length \(82\) is *minimum*: the lower bound from its general proposition is only \(72\), and its experimental graphic measures construction length relative to the weaker lower bound. This finding claims the sharpness proof, not invention of the numerical upper bound. Searches for exact binary square-superstring optima and semantically related published research records found no stronger result implying this lower bound. As with any bounded literature search, an unindexed exact census remains a residual risk.

## Value — PASS

This addresses the specific square-language shortest-cover question posed in a primary paper on generalized de Bruijn words. The five-bit instance has all \(32\) distinct ten-bit square targets and cannot be certified using the cited general lower bound; the sharp lower certificate distinguishes a genuinely optimum greedy construction from a merely short one. The structural division into eight necklaces and a finite two-case obstruction offers a reusable proof template for further square-cover optima. The value claim is exact finite optimality of a natural unresolved parameter, not a proposed general theorem.

## Scope and qualification

This review applies only to the stated linear binary five-bit-square theorem, with all factors checked contiguously and no wraparound. The alternative solver check is corroboration, not independent scientific certification. Relevant primary sources were inspected at the claim level and the historical priority risk is recorded in the structured audit.

Self-review: passed. Independent audit: not yet performed.
