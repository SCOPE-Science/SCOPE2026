---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The final theorem is exactly the selected-set size polynomial Q_G(z)=sum_{S subset V(G), forall v outside S: |N(v) cap S| <= 1} z^{|S|} for every finite simple connected cactus, including K1. P3-convexity is equivalent to the exterior at-most-one-selected-neighbor condition because any induced 3-vertex path with selected endpoints forces its middle vertex selected. Reconstructed from RESULT.md rather than accepting its pre-existing review: root the vertex-block incidence tree, use X_v for selected v, Y_v^0 and Y_v^1 for unselected v having respectively 0 or 1 selected descendant neighbors. For each child block B, messages T_B^X,T_B^0,T_B^1 exclude the articulation vertex weight. Then X_v=z prod_B T_B^X, Y_v^0=prod_B T_B^0, Y_v^1=sum_B T_B^1 prod_{C != B} T_C^0. The pair update (p,q)->(pa,qa+pb) evaluates the product and single-chosen-block sum in one pass, with no division or assumptions that factors are invertible. For a bridge v-u, T_X=X_u+Y_u^0, T_0=Y_u^0+Y_u^1, T_1=X_u; these cover all four root/child boundary statuses correctly. For a cycle (v=u0,u1,...,u_{ell-1}) fix root bit c0, sum products of local R_i(c_{i-1},c_i,c_{i+1}); when child c_i=1 the factor is X_i, while for c_i=0 it is Y_i^0+Y_i^1 for 0 selected cycle neighbors, Y_i^0 for 1, and 0 for 2. For unselected root c0=0 restrict c1+c_{ell-1} to 0 or 1, never 2. A two-recent-bit transfer computes this cycle sum in O(ell) ring gates, including the ell=3 boundary case. The local factors impose precisely the as-yet-unchecked constraints of each descendant vertex, and the root check closes the remaining neighbor count; induction on the tree proves no legal subset missed and no illegal subset repeated. At the original root Q_G=X_r+Y_r^0+Y_r^1; for K1 this is 1+z. Every block is an edge or a chordless cycle; sum_B (|B|-1)=|V|-1, hence overall transfer uses O(|V|) polynomial-ring additions/multiplications after standard linear graph decomposition. Substituting z_v instead of z at selected v yields the claimed multivariate weighting, with each selected vertex counted once. Independent separate Python implementation using direct block-bit enumeration rather than the supplied cycle recurrence and a separate 2^n subset enumerator agreed coefficientwise on 468 independently generated cactus instances up to 15 vertices, including K1, C4, C7, C13, triangle chains and mixed bridged cycles. The source verifier and its VERIFY_OK 1211-case log were inspected but not accepted as proof or executed. The induction, not the finite tests, supports the unlimited graph-order claim. One arithmetic operation is a unit-cost operation over Z[z] or Z[z_v]; neither linear bit complexity nor a bound on expanded multivariate output size is claimed.

## originality

PASS

Qualified best-of-knowledge novelty assessment of the precise final mathematical object, not generic efficient solvability: an explicit three-vertex-state, constant-cycle-width, all-size-coefficients recurrence for every cactus, with arbitrary cycle lengths and articulation patterns. Dourado–Grippo–Lin–Protti (arXiv:2603.04706v1) studies the same P3-convex set invariant and establishes tree and threshold-graph algorithms (Theorems 3 and 14), split-graph #P hardness (Theorem 12), and general exponential algorithms; its inspected relevant 27-page preprint gives no explicit cactus cycle-block polynomial recurrence. A pre-existing claim on clique-block graphs is referenced in the source self-audit but its actual primary package was not independently recovered in this run, so it is a priority risk and not relied on as proof of noncoverage. The generic weighted MSO/Courcelle–Makowsky–Rotics bounded-treewidth theorem already implies existence of a linear arithmetic-operation counting circuit over all cacti (treewidth<=2); therefore neither general tractability nor the mere existence of a linear circuit is original. The asserted narrower novelty is the explicit small-state formulas for the full size distribution, including cyclic root boundary and multivariate weights. The available general metatheorem does not state or imply this particular three-state cyclic factorization as an explicit theorem, and the primary P3 counting paper does not provide it. Brešar–Valencia-Pabon studies structural convexity in Cartesian products, not cactus counting. Six topical published-record semantic searches and multiple bibliographic/primary searches found no displayed equivalent cactus polynomial formula. A standard unindexed treewidth implementation or prior bootstrap-closure/cactus DP could already use equivalent states, so priority remains qualified and the generic tractability overlap is expressly conceded.

## value

PASS

The explicitly specified P3-convex-set size polynomial of the natural infinite cactus class is a meaningful exact counting invariant: it refines cardinality alone, includes every cycle length, and supports arbitrary articulation patterns and individual vertex weights. The same invariant is #P-complete on split graphs in Dourado et al. 2026, while cactus structure retains arbitrary numbers of nontrivial cycles; a concise, fully constructive cycle-block solution is a motivated special-family classification beyond the known tree case. The three-state articulation interface and two-recent-bit cycle transfer concretely explain the interface constraints and yield a useful efficient algorithm with explicit polynomial coefficients in unit-cost ring arithmetic. This is not claimed as a new general tractability theorem: bounded-treewidth MSO weighted counting already gives abstract polynomial evaluation; the value is the small transparent, implementable, exact identity for the natural graph family. It is more than a rename or tiny finite table and does not require a downstream general theorem to have self-contained mathematical use. The bit-complexity and arbitrary 2-connected block limitations prevent overstated performance claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
