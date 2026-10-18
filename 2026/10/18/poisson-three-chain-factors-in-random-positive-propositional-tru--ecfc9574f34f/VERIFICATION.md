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

# Reproducibility and limits

Execute `python3 verify.py` with standard Python 3. It deterministically enumerates all \(m\)-generator Boolean valuation matrices with \(0\le m\le3\), \(0\le n\le4\), and \(mn\le12\), recomputing bounded lattice closures by independent operations rather than trusting the claimed order representation. The result is `VERIFY_OK 5058 exhaustive finite valuations; 245 matching-poset factorizations; 6 exact moment bounds`.

For each eligible valuation, the program independently builds a family of truth sets by union/intersection closure and a family by checking all coordinatewise upset conditions. It checks Boolean expressivity against pairwise codeword distinctness and the three-chain product cardinality on all distinct-vector matching cases. Rational arithmetic checks the pair-comparison probability and an upper bound on shared-vertex comparison probability for six coordinate sizes.

The infinitary step uses the published local-dependence Poisson inequality; the separate proof bounds every overlap term and shows that the errors vanish. Finite enumeration does not establish this limit, independence across overlapping graph edges, or research priority. The random-set Poisson count was established in earlier literature; what is evaluated here is its application to the structure and size distribution of a generated positive propositional truth-set lattice.
