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

# Reproducibility and checks

Run `python verify.py` with the Python standard library, from the directory containing the file. It enumerates all \(q^3\) algebra elements and every ordered pair for \(q\in\{3,5,7\}\), using the multiplication table \([X,Y]=Z\), \([Y,X]=cZ\) and no premade graph adjacency.

The verifier checks the exact two-sided commutant size of each element, the full connected-component decomposition after deleting the center, clique counts of sizes two and three, and ordered pairwise two-sided zero-bracket tuples of lengths one, two, three using intersection of bit masks. It runs ten prime-field \((q,c)\) cases. It additionally implements \(\mathbb F_9\) using irreducible \(t^2+1\) over \(\mathbb F_3\) and checks four parameter cases, including both exceptional types and two generic cases: complete component decompositions plus ordered two- and three-tuple counts. It also checks identical labeled adjacency graphs for \(c=2,3\) over \(\mathbb F_7\), the equal two-tuple counts for \(c=1,-1\), and the exact three-tuple difference \(q^3(q-1)^4\).

Observed conclusion: `VERIFY_OK: 10 complete prime-field adjacency and clique censuses, four GF(9) component and tuple censuses; exact graph collisions`. The calculation does **not** search or enumerate arbitrary extension fields, nor does it verify an infinite-family theorem by itself. The proof in `RESULT.md` handles all odd prime powers using field properties and rank calculations; the congruence-asymmetry argument establishes nonisomorphism independently of the graph tests.

External independent mathematical audit: not performed. Publication priority: provisional.
