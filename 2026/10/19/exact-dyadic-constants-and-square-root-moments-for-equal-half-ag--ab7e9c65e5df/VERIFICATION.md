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

# Verification of exact equal-half moment constants

`verify.py` uses only the Python standard library. Execute `python3 verify.py` from this directory to reproduce exact rational moment checks for indices \(1\) through \(13\), and 150 integer outward-rounded logistic/product iterations. Its printed intervals enclose \(\sigma\) and \(B\) via analytically proved global bounds; the numerical test is supplemental to the convergence, Pringsheim, and singularity-transfer arguments in `RESULT.md`.

At step 150 the enclosure widths are less than \(5.5\times10^{-47}\) for \(\sigma\) and \(5.1\times10^{-47}\) for \(B\). The script uses a stated rational enclosure of \(\pi\). None of the checks establish a pointwise physical density-tail estimate or an independent external review.
