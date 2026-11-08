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

For finite loop-free simple labeled graphs and strict T(k)=1 iff k∈{0,2}, the provided bitmask equilibrium predicate is equivalent at each vertex to count(active neighbors)∈{0,2}. Independently reimplemented the census by explicit edge-by-edge active-neighbor tallies rather than executing the submitted verify.py. Exhausted all 1,2,8,64,1024,32768 labeled graphs for n=1,...,6 and all 2^n binary profiles of each (stopping after any equilibrium); obtained exactly 0,0,0,0,0,300 graphs without PNE. Independently enumerated 720 vertex permutations per supplied edge list: orbit sizes 180 (eight edges) and 120 (nine edges), disjoint and with union EXACTLY the 300 failure masks. Thus automorphism group orders are 4 and 6 and eight is minimal edge count at first failing order. Separately scanned NetworkX graph_atlas_g() across all isomorphism types through n=6 (1,2,4,11,34,156): only two n=6 types fail, with matching edge counts and degree sequences. An empty n=0 graph, if included, has the vacuous empty-strategy equilibrium. G8 degree-two parity equations imply s0=s2, s1=s5=1, s3+s4≡1+s0 (mod2); s0=s2=1 violates active vertex 0 (≥3 active neighbors), while s0=s2=0 forces s3=s4=1, contradicting parity. G9's three degree-four triangle vertices with pendant pair vertices cover r=0,1,2,3 active triangle cases: each forces a mismatch as in the actual proof. The Git tree recomputed from the seven actual file blob SHAs equals the assigned d300dbeee13f4734c57bc3ad8af51f40e0afa670. Finite enumeration supports precisely n≤6, not asymptotic statements.

## originality

PASS

Best-of-knowledge PASS for the precise novel conjunction (no failure below n=6, exactly two 6-vertex orbits with a distinct eight-edge witness, 300 labeled total). Prior full-text relevant sections establish the 3-sun and hardness, not this complete invariant. Broad searches and the exact graph atlas did not reveal a previously tabulated game-specific census; unindexed priority remains a real risk.

## value

PASS

A sharp smallest-obstruction order and exhaustive set of isomorphism types is a naturally motivated finite structural invariant for a well-studied strict homogeneous public-goods rule with NP-hard general equilibrium existence. Six-vertex 3-sun nonexistence was already known, but the new eight-edge nonisomorphic witness is sparser and the exact 180/120 labeled class decomposition is a meaningful complete first-obstruction layer, useful as a test family for model-specific algorithms and counterexample gadget selection. This is not an arbitrary slice or textbook corollary of NP-hardness; the two-class exhaustive boundary is a self-contained exact statement and need not imply a larger-n theorem. Its significance should not be overstated as a complexity improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
