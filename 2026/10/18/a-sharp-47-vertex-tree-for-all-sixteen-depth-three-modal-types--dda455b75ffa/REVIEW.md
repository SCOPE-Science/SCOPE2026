# Scientific review: 47-vertex depth-three modal type-complete tree

## Correctness

PASS. The object is an ordinary finite rooted arborescence with parent-to-child accessibility and no propositional letters. The characteristic-formula induction identifies 16 depth-three types. For each vertex, the weighted child-demand inequality counts a separate child for every required depth-two type; summing over edges yields the global bound in the main result. The exact 16-term potential table has nonnegative entries summing to 44, and every type-complete tree has a depth-three path and therefore root weight at least 3. Hence every qualifying tree has at least 47 vertices. `verify.py` independently checks the complete 47-vertex witness from `witness.json`, including all 16 bottom-up modal codes and the exact root and potential values. An exhaustive search over all smaller rooted trees is neither asserted nor required.

## Originality

PASS to the extent supported by accessible primary literature and claim-specific published-result searches. Papacchini and Schmidt (2011) prove a tableau procedure for **inclusion-minimal Herbrand models of a given set of modal clauses**; they neither impose simultaneous realization of all bounded modal types nor optimize tree cardinality. Their full author-hosted paper, particularly Sections 1–4 and the minimality definition, was checked. Bolander and Burigana (2024) prove **world and edge minimization of a pointed bounded-bisimilar Kripke model**, permitting non-tree representations; their Definitions 3.10 and Theorems 4.4 and 5.6 do not impose the present all-vertex coverage requirement. Section 6 uses a different labelled multi-modal tree construction. Claim-specific searches for a minimum universal finite modal-type tree, 16 modal three-types, 47 vertices, and bounded-bisimulation tree saturation did not retrieve an identical theorem or a table dominating the proposed bound. This is not a proof of priority: unpublished, unindexed or hard-to-find enumerations remain a concrete residual risk.

## Value

PASS. The invariant is a natural precise optimum: how much duplication of successor-type witnesses is forced when a **single connected rooted tree**, rather than a shared-state directed graph, must contain representatives of all depth-three logical observations. The comparison with a 16-vertex directed acyclic sharing construction motivates the exact 47-vertex cost and shows that it measures a real tree-only constraint. The elementary 16-case dual potential and the matching explicit certificate settle the complete finite optimisation problem at depth three. The finding does not claim a general formula at arbitrary depth, and the verified finite case has intrinsic value independently of a speculative downstream theorem.

## Closest literature, checks, and limits

Primary comparisons: Papacchini–Schmidt, *A Tableau Calculus for Minimal Modal Model Generation* (2011), DOI 10.1016/j.entcs.2011.10.013, author full text `https://www.csc.liv.ac.uk/~papacchf/papers/PapacchiniSchmidt11a.pdf`; and Bolander–Burigana, *Better Bounded Bisimulation Contractions* (2024), arXiv:2405.00480. The former's model minimality is inclusion-minimality of a Herbrand interpretation for supplied formulae; the latter's is minimization of a pointed bounded-bisimilar model. Neither result as stated bounds the universal type-complete **rooted-tree** optimum. The arXiv work is later supporting context, not a pre-2016 source. A direct finite table in material not found by the available searches would threaten originality, even though it would not invalidate the analytic proof.

Self-review: passed. Independent audit: not yet performed.
