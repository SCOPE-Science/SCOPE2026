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

# Reproducibility and mathematical verification

Run `python3 verify.py` with a standard Python 3 interpreter. The certificate uses only `itertools.combinations`, `itertools.product` and integer arithmetic in the quadratic number field \(\mathbb Q(\sqrt5)\); there is no random seed, floating-point operation, external dependency, or network access. The verifier itself contains full finite coordinate generation, squared-distance computation, and color classes for all 19 exact thresholds. It asserts the full ordered pair-distance spectra, checks every pair in each color class, then enumerates all relevant subsets to prove optimality.

The critical exhaustive counts for the dodecahedron are 12 five-point subsets with squared diameter at most 4; 100 seven-point subsets and zero eight-point subsets with squared diameter at most 8; and 820 disjoint unordered pairs of admissible seven-point subsets, none leaving an admissible six-point complement. The 12 five-sets have no four-set collection whose union covers the entire 20-vertex set. Four-part admissibility at squared cutoff eight and five-part admissibility at squared cutoff four are independently shown by explicit color arrays. Lower bounds for the smaller solids are supplied by enumerations excluding forbidden clique sizes, and their two-color thresholds have obvious diameter-pair obstructions.

The output must end with `EXACT_CERTIFICATE_OK 19 threshold witnesses, and all necessary obstructions`. These finite enumerations certify the entire finite theorem because all pair-distances are drawn from the explicitly checked finite spectra; the certificate is not a heuristic search. The proof covers only the five specified finite vertex sets, and no claim is made about historical novelty being formally or independently certified.
