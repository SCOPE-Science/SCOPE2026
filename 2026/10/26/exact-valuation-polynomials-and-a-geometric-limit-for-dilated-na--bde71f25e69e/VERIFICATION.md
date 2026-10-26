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

# Reproduction and scope

Run `python3 verify.py` using the Python 3 standard library. The script compares exact integer values of \(N(n,k)=\binom nk\binom n{k+1}/n\) against the closed valuation-polynomial coefficients over all legal entries of \(202\) rows with prime bases \(2,3,5,7\), multipliers up to \(27\), and exponents up to \(4\), under the row-size bound \(700\). It confirms all profile totals and representative multishifted examples.

The computations are finite checks only. The universal formula is justified by the base-\(p\) digit-sum block lemma and the exact shell census; the distributional convergence and its rate come from an explicit \(p\)-adic coupling. No external or independent audit has been conducted.
