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

# Reproduce the exact finite checks

Install Python 3.8 or later. Put `verify.py`, `cert_p4_n17.json`, `cert_p4_n18.json`, `cert_p4_n19.json`, and `cert_p4_n20.json` in one directory. Run:

```sh
python3 verify.py
```

The checker independently constructs cyclic-distance adjacency, enumerates disconnected triples using breadth-first search, and forms each facet as the complement of such a triple. It verifies that no facets exist for \(3\le n\le10\). For each \(11\le n\le16\), it enumerates every face, computes every mod-two simplicial boundary by integer bit operations, and uses exact Gaussian elimination to produce all reduced Betti ranks; the single nonzero rank occurs strictly below dimension \(n-4\).

For each \(n=17,18,19,20\), the corresponding JSON file is a complete ordered list of complementary triples. The checker recomputes the entire facet set independently of this list, proves its exact coverage without repetition, tests the pairwise pure-shelling witness criterion for every new facet against every earlier facet, and counts those new facets whose entire boundary was present. Expected facet counts are respectively 408, 528, 665, and 820; expected spanning-facet counts are 1, 10, 20, and 31.

The finite computations are exhaustive because they iterate over all triples, all faces of all facet complements for the lower cases, and every earlier-facet comparison for the four certificates. They do not replace the cited general theorem for \(n\ge21\), do not establish integral lower-range homotopy types, and do not establish any result for powers other than four.

The relevant external theorems and tabulated previously known Betti values are cited in `RESULT.md`. No independent mathematical audit has been performed.
