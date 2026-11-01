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

# Finite verification and scope

Run `python3 verify.py` with the two text certificates `shelling_13.csv` and `shelling_14.csv` in the same directory. Only the Python 3 standard library is required.

The checker independently reconstructs all three-element induced subgraphs of the ordinary cubic cycle power and selects exactly the disconnected triples. It confirms that each certificate lists every facet once, then checks both the definition-level pure-codimension-one shelling condition and the complementary-triple pairwise witness criterion. It counts exactly one spanning facet at \(n=13\) and eight at \(n=14\). It also enumerates all faces and calculates exact reduced boundary ranks over \(\mathbb F_2\) for \(9\le n\le12\), establishing homological non-shellability obstructions. For \(3\le n\le8\), it confirms that there are no facets.

Executed from the package directory: `VERIFY_OK: all complete finite cases and both explicit shellings`.

The published theorem of Chauhan and Shukla, arXiv:2603.23155v1, supplies the infinite-parameter case \(n\ge15\). The finite checker does not independently prove that published theorem. It does prove all finite missing cases, conditional only on elementary simplicial-complex definitions, exact binary linear algebra, and the standard shelling-homotopy implication.
