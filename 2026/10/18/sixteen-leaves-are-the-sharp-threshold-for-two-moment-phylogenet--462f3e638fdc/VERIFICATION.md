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

# Exact verification evidence

Run `python3 verify.py`, from this directory, with a standard Python 3 interpreter and no third-party dependencies. Compare its standard output with `CERTIFICATE.json`; the output uses sorted JSON keys and fixed indentation.

The self-contained script generates all non-plane rooted full binary tree shapes through sixteen leaves by canonical root splits, constructs descendant leaf masks, and computes exact single-clade and two-clade-union histograms. It verifies one-to-one moment signatures through fifteen leaves and exactly one collision at sixteen leaves. It then enumerates all \(65536\) subsets of the two exceptional trees separately, checks equality of all first and second raw PD moments at all seventeen subset cardinalities, and verifies the exact two-leaf-sample binomial-third-moment totals \(5909\) and \(5910\). All arithmetic uses integer counts; the mathematical implication from integer signatures to complete moment curves is proved in `RESULT.md`.

A finite census proves only the finite threshold, while the unlimited-size construction has a separate combinatorial proof. Source inspection has not ruled out every possible earlier equivalent formulation, and independent external validation has not been performed.
