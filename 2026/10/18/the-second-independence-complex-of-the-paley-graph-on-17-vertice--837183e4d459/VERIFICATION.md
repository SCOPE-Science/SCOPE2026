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

# Reproducible finite verification

Run `python -S verify_paley17.py` with Python 3 and no third-party dependencies. The printed output begins with `PALEY17_SECOND_INDEPENDENCE_EXACT_CHECK_OK`; the subsequent JSON gives the computed certificate.

The checker performs two exhaustive membership tests on all \(2^{17}=131072\) subsets; verifies the face and facet numbers; constructs \(423\) unmatched-element-toggle pairs; and tests acyclicity by a full directed Hasse-diagram topological sort over \(867\) nonempty simplices and \(2856\) incidences.

The exact signed integer cancellation projection uses only pivots \(\pm1\). It checks that the sole nonzero critical boundary has three entries \(-1\) and greatest common divisor \(1\). Independently, direct mod-two simplicial boundary matrices have ranks \(16,120,220,68\), giving an eighteen-dimensional third homology over \(\mathbb F_2\).

Every nontrivial cyclic translation is explicitly checked to preserve all simplices without fixing any nonempty simplex setwise. Together with the homotopy classification, the rational Lefschetz character has values \(18\) at the identity and \(1\) elsewhere.

The checker does not constitute independent mathematical audit. The infinite-family problem, integral translation representation, and broader Paley-graph classifications are not certified.
