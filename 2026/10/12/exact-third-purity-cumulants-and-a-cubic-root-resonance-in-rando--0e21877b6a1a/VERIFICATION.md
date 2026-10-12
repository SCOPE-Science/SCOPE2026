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
# Verification of exact third purity cumulants

Execute `python3 verify.py` from the extracted folder. This uses only the Python standard library and terminates with

`VERIFY_OK 30 exact monomial tests; 72706 complete phase-array state comparisons`

The verifier checks the expectation of monomials by root-of-unity exponent divisibility for every ordered pair and ordered triple of plaquettes on six small grids, covering \(q=2,3,4,5,6\). It separately enumerates complete finite phase ensembles on \(2\times2\), \(2\times4\), and \(4\times4\) grids at specified alphabets and checks the first three centered moments by exact integer sums/rational quotients. The Gram-matrix formula for purity is compared independently against the plaquette expression across all \(2\times2\) and \(2\times4\) states and a deterministic sample of \(4\times4\) real states.

The analytic proof in RESULT.md covers arbitrary \(U,V\ge2\) and every \(q\ge2\) or continuous independent phases. Exhaustive finite-grid tests do **not** establish an all-dimension theorem by themselves. Scientific verification here is a self-review; external independent audit was not performed. The September 2026 related preprint could not be inspected in complete primary full text, so an originality risk remains.
