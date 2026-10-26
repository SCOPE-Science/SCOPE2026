# Scientific review: finite tree quotients onto three-level forks

## Correctness — PASS

The theorem concerns surjective bounded morphisms of the reflexive ancestor order on finite rooted trees onto the reflexive poset \(\(Q_m\)\) with one bottom, \(m\ge2\) incomparable middle points, and one top. The two root-image states are sufficient because all middle worlds are symmetric and a subtree root mapped to the top admits exactly one map. The bottom-root recurrence separates selections containing a bottom-root child (already covering all target worlds) from selections having no such child, where inclusion-exclusion precisely enforces presence of every middle colour. The branch criterion uses a maximal zero-preimage point and the forced distinct middle-colour children, each having a top descendant. The converse explicit colouring lifts at all vertices. The size extremum and \(\(m!\)\) minimal-spider count follow from this rigidity. In full branching trees, monotonicity of \(d^{-h}\log A_h\) follows from the all-bottom-child construction and boundedness from counting all functions. These are complete finite and infinite proofs, not deductions from experiments.

Directly checking the relation and the back condition on 1,928 sampled finite parent-array trees agreed with the exact recurrence. Independent Stirling recursion and inclusion-exclusion agreed in 40 regular-tree parameter pairs. Computation is corroboration only.

## Originality — PASS with residual risk

The classical definition and modal invariance of bounded morphisms are prior results. Bezhanishvili–Harding (2012), particularly Sections 2 and Proposition 2.5, explains finite tree S4 frames and the interior-map/bounded-morphism connection but does not enumerate these particular quotients. Endriss (2003), Sections 3.5–3.6, studies modal logic on ordered trees and additionally uses inverse-back and sibling relations; his morphism notion is therefore not identical to the present reflexive ancestor-order one. The separately inspected dated 2014 work on modal logics of metric spaces concerns modal-logic classification, not these map counts. Older counts from Boolean inclusion lattices or weak-order sources do not imply formulas for arbitrary rooted-tree sources: neither source family contains arbitrary branching rooted trees.

Target-specific recurrence and source-branching equivalence were searched under p-morphism, bounded-morphism, Kripke, and interior-map terminology, including parameter and source/target changes; no equivalent statement was identified. Search absence is not a guarantee: a general tree-automata procedure or an unindexed specialized work could subsume the recurrence. A separate independent originality audit remains necessary before any priority claim.

## Mathematical value — PASS

Determining when a finite tree has a given finite S4-frame as a bounded-morphic quotient is natural in finite modal semantics, because p-morphic images preserve modal validity. The theorem replaces a generic exponential search over functions by a complete structural obstruction, a size-sharp extremum, and an exact polynomial-arithmetic census for arbitrary rooted-tree sources. The additional regular-tree case supplies an exact recursively computable high-volume growth rate and proves its finite positive entropy, rather than only giving isolated small counts. This is a genuine complete restricted classification, not a renamed count of order maps; dropping the back condition invalidates the theorem.

## Limitations and literature

Novelty comparisons are necessarily best-knowledge and do not claim exhaustive world-literature coverage. No closed elementary formula for the regular-tree entropy is asserted. Counts concern labelled target worlds, not quotient-isomorphism classes; input frame is reflexive transitive, not strict-child-only. The checker is finite and cannot establish the infinite theorem by enumeration. Relevant literature: Bezhanishvili and Harding, *Modal Logics of Stone Spaces* (2012), DOI 10.1007/s11083-011-9224-2; Endriss, *Modal Logics of Ordered Trees* (2003); Bezhanishvili, Gabelaia and Lucero-Bryan, *Modal Logics of Metric Spaces* (first online 2014-12-18), DOI 10.1017/S1755020314000446.

Self-review: passed. Independent audit: not yet performed.
