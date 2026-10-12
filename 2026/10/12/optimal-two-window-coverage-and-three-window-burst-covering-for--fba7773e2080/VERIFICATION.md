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
# Reproducibility and proof boundaries

The standalone artifact `verify.py` requires only Python 3.10+ and no external package. Extract it beside this document and run `python3 verify.py`. It enumerates all error-pattern syndromes supported in each width-two and width-three window for the explicit field-power ordering in all binary extension degrees from \(2\) through \(8\). For every degree it checks both cyclic and noncyclic conventions against the full set of \(2^{m+1}\) syndromes, confirms that only one syndrome is missing at width two, and checks all adjacent and two-apart labels. Independently, for the degree-two and degree-three binary vector spaces, it enumerates every permutation beginning at zero (\(6\) and \(5040\) orderings) to check the two-window impossibility for both conventions. Translation by the first label preserves every adjacent difference; this normalization is exhaustive for the tested small orders.

The expected final line is `VERIFY_OK`. These are finite consistency checks, not the proof of the all-degree theorem. The theoretical universal steps are the nonzero-element XOR identity, linear/cyclic telescoping, and the explicit primitive-power calculation. The field construction requires a primitive element, guaranteed for each finite field. Nothing here constitutes independent audit or external certification.
