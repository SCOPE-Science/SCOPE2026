---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

An acyclic functional/inverse-functional directed graph has undirected components that are finite directed paths F (including singletons), forward rays A=omega, reverse rays B=omega*, or double rays Z=integer order. Every prescribed edge must be an immediate predecessor-successor relation in the new strict order; a foreign vertex between any two vertices on a component would interrupt one of finitely many prescribed adjacent edges, hence each whole component is convex and its internal order is fixed. For a finite number of component blocks, extra successors occur exactly at adjacent block boundaries with a maximal left block (F or B) and a minimal right block (F or A). Among f consecutive F blocks, each of the f-1 gaps that contains no Z necessarily contains a bad transition: either F->F, F->A, B->F or B->A. One Z can occupy at most one such F-F gap, so the lower bound max(0,f-z-1) follows. Order all A first, F blocks separated by up to f-1 of the Z blocks, any leftover Z next, and all B last; the constructed order attains the lower bound, including f=0,1 and z>=f-1. For infinitely many components of cardinal kappa, the order kappa times Q lexicographically is a dense without endpoints index order of cardinal kappa (assuming usual choice); the ordered sum across components has no cross-component immediate successors, giving defect zero, also uncountably. Independently coded endpoint-cost minimization, canonical witnesses and exhaustive permutation checks for all 714 four-type multisets with 1..9 blocks (349,524 distinct permutations), and DP for 900 cases f,z<30, all agreed. Finite tests are corroboration, not proof for all f,z/cardinals. No directed cycles are permitted; if present, no completion exists. The proof handles exactly one directed relation on a nonempty set.

## originality

PASS

Best-of-knowledge claim novelty is only the sharp finite-component, potentially infinite-path classification delta=max(0,f-z-1), the exact realizability threshold f<=z+1, and the optimal compulsory-edge count. The infinite-component dense completion is already established for countable graphs by Michaliszyn-Witkowski and is explicitly credited; its straightforward arbitrary-cardinal indexing extension is not asserted as a deep independent novelty. The finite-only z=0 case is elementary. Three primary article texts and three direct Resultary queries, plus external alias searches and GitHub SCOPE code queries, found no theorem that mathematically implies this exact finite-component endpoint optimum. This is a best-of-knowledge judgment, not a historical priority certificate.

## value

PASS

The source paper arXiv:2610.09758 treats exact successor relations as a semantic requirement and uses infinitely many components precisely to access dense-index completion. Its omitted finite-component case is a concrete structural obstruction: the formula classifies exactly which finite unions of potentially infinite chains admit a same-vertex exact completion, and calculates a sharp natural edge-augmentation invariant. The noninterchangeability of one-sided rays and double rays is mathematically meaningful (f=3,z=1 forces one edge, f=2,z=1 none), and the all-parameter classification is reusable when assessing whether a fixed sparse successor digraph can arise from an order without adding adjacencies. The f-1 finite-domain consequence and dense infinite-component case are credited/elementary; value is in the complementary exact formula and boundary, not in a general complexity theorem or paper-sized advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
