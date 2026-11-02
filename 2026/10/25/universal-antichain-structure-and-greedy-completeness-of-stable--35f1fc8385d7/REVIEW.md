# Independent mathematical audit

## correctness

PASS

The finite-contract claim and all quantifiers were reconstructed from actual RESULT.md and the eight-file Git tree 45366ddf7246672a46e6e9d38d4d64e848dfc247. For each agent and A⊆B, SUB gives C(B)∩A⊆C(A); if all of M is chosen, every subset T⊆M is chosen, making the globally IR sets a nonempty hereditary family. Any nonempty blocking contract set Z contains an x chosen at both endpoints from M_i∪Z_i, so SUB implies x is chosen already from M_i∪{x}. When M is IR, IRP forces retention of M_i as well as x at both endpoints, hence M∪{x} is globally IR; conversely any IR extension gives singleton blocking. Nonmaximal hereditary members have a feasible one-contract extension, proving CY-stable iff facet. At any SMA step the two-endpoint acceptance predicate is equivalent to an IR one-contract extension; in the accepted case IRP makes the choice update exactly this extension. Rejected x stays infeasible as holdings grow by heredity, and processing a target facet first reaches it, proving both directions of order-surjectivity. For any nonempty antichain A, its hereditary downward hull D is realized on a one-firm star by firm choice C(S)=S for S∈D and ∅ otherwise, and each worker choosing its only offered contract. SUB holds by heredity/empty rejection and IRP by whole-menu acceptance on every feasible augmentation. Facets(D)=A. The edge cases n=0 and A={∅} are covered, and empty choices are permitted. An independent fresh checker (separate from the package verify.py) enumerated all 194 nonempty hereditary families for n≤4, all 4096 three-contract firm choice tables (67 satisfy SUB+IRP), and checked blocks, facets and order reachability. These bounded enumerations corroborate, and do not replace, the arbitrary finite proof. There is no assertion of responsiveness, path independence, or infinite-market behavior.

## originality

PASS

Best-of-knowledge: the strongest directly inspected current primary paper (Bansal et al. v9) proves each ordered SMA outcome stable and singleton block reduction, but not the reverse all-stable range or arbitrary-antichain construction. The closest earlier arbitrary-hereditary feasibility setting (Bando et al.) is acknowledged rather than claimed as new; its greedy priority rule may violate IRP, so it is not a dominating theorem about SUB–IRP stable outcomes. The universal antichain realization gives the strongest distinctive new statement, with facet/greedy statements logically short consequences once SUB and IRP are recognized. Related published Resultary records concern classical rank/fairness profiles or other matching objectives. A possibly equivalent abstract choice-theoretic representation theorem may exist under other terminology; no exhaustive priority or certification is claimed. Chambers–Yenmez full text was inaccessible and is retained as a risk, not deemed non-covering.

## value

PASS

The primary SUB–IRP matching paper explicitly raises structural questions about CY-stable outcomes (Section 6). This theorem identifies the exact general inclusion structure (facets of the IR simplicial complex), proves complete algorithmic accessibility of every stable outcome, and supplies a tight star-market realization showing that any nonempty finite antichain is possible. That pair of classification and universal construction results is useful for future structural or impossibility work; it is neither an arbitrary small instance nor a numerical parameter recomputation. The severity of choosing ∅ on infeasible menus is an explicit economic-model limitation but fully within the declared SUB–IRP axioms. The theorem does not establish incentive/welfare guarantees or the failure of every possible non-inclusion lattice order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
