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
The proof was reconstructed from the support model of ideals in a finite direct product of fields and the definition of metric-dimension threshold.

Exact symbolic checks:
- the annihilating-ideal graph is the graph on nonempty proper subsets with disjointness adjacency;
- for every pair \(A,B\), the four region sizes
  \(a=|A\cap B|\), \(b=|A\setminus B|\), \(c=|B\setminus A|\), \(d=|[n]\setminus(A\cup B)|\)
  determine the number of distinguishing vertices;
- the five possible pair configurations reduce to the four displayed formulas, with the two nested orientations symmetric;
- the nested formula is minimized exactly when the inclusion adds one coordinate and \(a,d\) are balanced;
- every nonnested formula is strictly larger for \(n\ge4\);
- the threshold is therefore
  \(2^n-2^{\lfloor(n-1)/2\rfloor}-2^{\lceil(n-1)/2\rceil}-2\)
  for \(n\ge4\), with direct exceptions \(1\) and \(3\) at \(n=2,3\).

`artifacts/verify.py` independently builds the graph for every \(2\le n\le9\), computes all-pairs shortest paths, finds every distinguishing set \(D(A,B)\), verifies the threshold formula, and checks the complete structural classification of minimizing pairs for \(4\le n\le9\). It returns `VERIFY_OK`.

Finite computation is not used to justify the universal statement.
