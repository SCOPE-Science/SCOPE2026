# Independent mathematical audit

## correctness

PASS

Every new nonalgebraic 1-type in the countable homogeneous random poset is an admissible ideal/filter pair (L,U) with all l<u. The identity counts separately L empty and U empty as 2J(P)-1. If min(U)={v}, every nonempty ideal L lies in P_<v and contributes D_v-2. For multiple minimal upper vertices with some common lower bound, the orientation of an undirected cover tree forces a unique final common branching ancestor v, with common lower set P_<=v; upper filters using at least two distinct upper-cover branches are counted by B_v=U_v-2-sum_{v<.w}(U_w-1), giving (D_v-1)B_v admissible nonempty lower ideals. Every profile belongs to exactly one class. Directed cover subtrees have disjoint branches, proving D_v=1+prod lower D_w and U_v=1+prod upper U_w. Two-state tree DP counts ideals J(P) in O(n) arithmetic operations of O(n)-bit integers. Independent brute enumeration of all 2143 labeled oriented tree-poset cases on <=5 vertices compared every admissible one-point relation with the formula; N-poset count 20. This bounded test corroborates but does not replace the unique-branching proof.

## originality

PASS

One-point extension types as compatible down/up sets are classical and expressly established by the earlier published general random-poset #P-completeness result. That stronger general counting-hardness theorem does not supply a linear algorithm on directed cover trees. The specific product recurrences and unique branching-ancestor contribution are a uniform structural solution for arbitrary orientations, including an N-poset outside series-parallel settings. Jochemko studies order polynomials rather than simultaneous lower/upper extension profiles. Pretzel studies a potentially related insertion-poset construction but its complete source was inaccessible, so the reported noncoverage is bounded to what was read. No relevant published result or Resultary hit was found to directly imply this tree-cover formula; best-of-knowledge PASS with a concrete priority caveat.

## value

PASS

Cover trees are the natural treewidth-one restriction of an otherwise #P-complete exact 1-type counting problem. A linear-operation exact formula for the entire class, including mixed upward/downward covers and non-series-parallel N configurations, is a motivated tractability boundary, not an arbitrary table of small cases. Researchers studying homogeneous poset reducts, orbit counts or parameterized counting can use this precise invariant and computation without converting the tree to a restricted rooted-forest order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
