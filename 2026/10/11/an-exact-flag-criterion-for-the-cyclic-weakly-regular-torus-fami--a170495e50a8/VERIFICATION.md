---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS. For n>=7 and 2<=k<=floor((n-3)/2), the triangulation faces are the two n-translation orbits from the defining paper. Their edges are precisely the six distinct differences +-1,+-k,+-(k+1). Any edge 3-cycle has nonzero oriented steps whose sum is a multiple of n. Since |x+y+z|<2n, orientation gives either 0 or +n. Zero sum gives only 1+k=k+1 (actual faces) or, if k=2, 1+1=k (n missing translates); no other signed 3-term identities are permitted. For +n, any negative step would force sum<=2(k+1)-1 <=n-2, so all steps are positive. In canonical range only step multisets {k,k,k}, {k+1,k+1,k+1}, {k,k,k+1}, {k,k+1,k+1}, {1,k+1,k+1} can sum to n; these yield n=3k,3(k+1),3k+1,3k+2,2k+3. Equal-step triangles have orbit n/3; mixed types have orbit n; distinct step multisets are distinct triangle orbits. These prove E(n,k) term-by-term and its six zero conditions. In a connected closed torus triangulation, a 4-clique with all triples facial would be a tetrahedron-boundary sphere subcomplex, impossible, so absence of missing triangles is exactly flagness. Direct finite analysis of n<=12 and n=13 verifies first possible flag n=13,k=3. A separately implemented face/1-skeleton/3-clique enumerator checked all 9,506 canonical pairs with 7<=n<=200, including first_flag=(13,3), but the universal theorem relies on the step argument.

## originality

PASS

Best-of-knowledge PASS after fresh statement-level comparison. Datta--Upadhyay give the exact face family and k-to-n-k-1 symmetry, but do not state the missing-triangle count or six-regime criterion in the inspected relevant text. Brehm--Kuehnel classify equivelar torus maps via translation-lattice quotients, yet do not state this step-relation criterion; that general geometric framework does not without new calculation imply the claimed multiplicities. Bibby et al. prove uniqueness of a global 12-vertex minimal flag torus, but do not characterize the Datta--Upadhyay family or identify its first flag parameter. Targeted searches found the exact result only as the same candidate record indexed in Resultary, not a distinct antecedent. Priority risk of an unindexed lattice-coordinate reformulation remains.

## value

PASS

PASS. Flagness is an intrinsic higher-dimensional clique-filling condition for a torus triangulation, and the Datta--Upadhyay six-regular cyclic family is a canonical infinite vertex-transitive class. The exact empty-triangle orbit census is a natural structural invariant, not an arbitrary finite slice: it classifies flagness for all canonical n,k and demonstrates the family first becomes flag at 13 vertices, distinguishing it from the unique globally minimal 12-vertex flag torus. The result is specialized and elementary but its exact all-parameter boundary and multiplicities can be reused in torus map or flag-complex studies without a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
