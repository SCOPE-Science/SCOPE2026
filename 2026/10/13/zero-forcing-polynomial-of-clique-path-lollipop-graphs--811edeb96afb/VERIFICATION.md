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
# Verification

The symbolic proof is the basis for the infinite claim. The standalone checker independently constructs every graph in the finite test range, exhaustively tests every initial set under the standard zero forcing rule, compares that result with the three-case characterization, and then compares the observed coefficient vector with the displayed polynomial.

The test range is every \(3\le k\le6\) and \(1\le\ell\le8\), so the largest tested graph has order \(14\). The script also verifies \(Z(L(k,\ell))=k-1\) and exactly \(2k-1\) minimum sets for every tested parameter pair.

Replay with:

`python verify.py`

Executed package check:

`VERIFY_OK parameter_pairs=32 subset_checks=61200 criterion_checks=61200 coefficient_checks=208 minimum_checks=64 max_order=14`
