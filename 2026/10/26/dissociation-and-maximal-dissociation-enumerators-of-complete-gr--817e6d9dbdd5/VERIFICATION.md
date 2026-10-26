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

# Reproducible checks
Run `python3 verify_subdivision.py` in a directory with the provided source. The program constructs every incidence edge from scratch and, for each vertex subset, computes induced degrees from adjacency masks. For each legal set it separately tests whether adding any omitted vertex remains legal. It compares the complete dissociation counts, all maximal-set cardinality counts, and finer counts grouped by omitted original-vertex count with two independent combinatorial expressions.

Exhaustive cases: \(n=3,4,5,6\), graph orders \(6,10,15,21\), representing a total of \(2{,}131{,}008\) examined subsets. The text file `verification_output.txt` records the direct computations. Expected summary of maximal polynomials: \(M_3(z)=2z^3+3z^4\), \(M_4(z)=z^4+24z^5+5z^6\), \(M_5(z)=z^5+150z^7+25z^8+z^{10}\), and \(M_6(z)=z^6+750z^9+246z^{10}+30z^{12}+z^{15}\). All reported comparisons passed.

The infinite case is established through the classification and counting proof in `RESULT.md`, not through extrapolation from the small instances. External mathematical validation remains unperformed.
