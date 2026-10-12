---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The infinite claim is proved analytically in `RESULT.md`; no finite experiment is used to infer an infinite statement.

The finite closure uses the symmetry of complete multipartite graphs. For a fixed palette, a coloring is completely represented by a matrix whose row for part \(V_i\) records the number of vertices of each color in that part. For any vertex of \(V_i\), the number of neighbors of a given color is the corresponding global column sum minus that row entry. Thus enumerating all weak compositions of each \(n_i\) among the palette colors exhausts all colorings up to irrelevant permutations of vertices within parts.

`verify.py` performs the following checks:

1. It enumerates every nondecreasing complete-multipartite profile of orders \(2\) through \(11\). Stars are excluded by the degree-one obstruction. For each remaining profile it checks the predicted minimum palette, exhausting smaller palettes when needed. The only profiles requiring four colors are \(K_4\) and \(K_{2,1,1}\).
2. It constructs the periodic three-coloring from the proof for every nonstar profile of orders \(12\) through \(40\) and checks the strong-majority inequalities directly.
3. It checks the half-half two-color construction on every all-even profile through order \(30\). Nonexistence when an odd part occurs is proved analytically, not inferred from this finite loop.

A replay from the verifier extracted from the packaged row returned:

`ALL CHECKS PASSED; small_profiles_N<=11=183; small_search_calls=495; small_witnesses=173; periodic_profiles_N=12..40=215055; two_color_profiles_N<=30=28569; exception_profiles=K_4,K_{2,1,1}`

The verifier uses only the Python standard library. Its bounded construction tests beyond order eleven are stress tests, not certificates for the unbounded range.
