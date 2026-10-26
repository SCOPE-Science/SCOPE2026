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

Execute `python3 checker.py` with a current Python 3 installation providing SymPy, NumPy, and SciPy. The included `checker_output.txt` records the observed 4,724 passing assertions for exact tensor multiplicities, Chebyshev semicircle moments, polynomial derivatives, and numerical optimizer checks.

The full proof is `RESULT.md`. For every integer \(n\ge2\), the identities follow from the Clebsch–Gordan rule and finite exact multiplicity sums; strict optimality and all complex equality cases follow from exact derivative signs and the positivity of invariant multiplicities. A finite test cannot certify any infinite family or exhaustive literature priority. Source comparisons to the classical \(\mathrm{SU}(2)\) tensor-product and Haar formulas are given in `RESULT.md` and `REVIEW.md`. No independent audit has been performed.
