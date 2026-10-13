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

# Reproducible checks

The script `artifacts/verify_fixing.py` uses only Python's standard library, with no external files or network access. Run `python3 artifacts/verify_fixing.py` from the extracted package directory.

It independently checks two decision tests for every selected-edge subset of \(K(n,2)\), for \(n=5,6,7\): distinct incidence-membership signatures and the independent connected-component exclusion. These ranges cover \(2^{10}+2^{15}+2^{21}=2{,}130{,}944\) subsets. It then tests every size-\(\lfloor2n/3\rfloor\) subset for \(n=8,9\), comprising \(98{,}280+1{,}947{,}792=2{,}046{,}072\) subsets. In total, \(4{,}177{,}016\) candidate sets receive two different decision tests. For \(n=5,6,7\) every coefficient is compared directly; for \(n=8,9\) the minimum coefficient is compared. Finite coefficient extraction checks all minimum formulas through \(n=21\) and checks the top two polynomial coefficients.

The run output in `artifacts/checks.txt` is the actual output of the bundled script. The proof of the theorem is mathematical and does not rely on extrapolating from these finite cases.

The established automorphism-group identification \(\operatorname{Aut}(K(n,2))\cong S_n\) and the 2017 definition of fixing polynomial are cited in `RESULT.md`; they are not claims of new independent certification.
