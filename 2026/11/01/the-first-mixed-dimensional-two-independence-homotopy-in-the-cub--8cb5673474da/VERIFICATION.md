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

# Reproducible verification
Run `python3 scripts/verify.py` from the directory containing the embedded package files. The code uses Python 3.10+ standard library only; the complete captured output is `verification_output.txt`.

Two separate face tests exhaust all \(4\), \(16\), \(256\), and \(65,536\) subsets for cubical dimensions \(1,2,3,4\), respectively. The nonempty face counts are \(3,10,76,3054\). The matching leaves one critical vertex and, respectively, zero, three one-, three two-, and sixteen three- plus one four-dimensional cells. All \(2,12,184,13568\) nonempty covering incidences are directed according to the matching; complete topological sorts visit every face, verifying acyclicity.

The integral calculation evaluates all sixteen Morse boundary coefficients of the single critical four-cell and finds all zero. Independent simplicial mod-two boundary ranks for the fourth complex are \((15,105,359,589,370,70,10)\) in differential degrees one through seven and give reduced Betti ranks sixteen and one in degrees three and four. Mod-two computations alone do not prove the integral attaching-map result; the signed integer Morse projection supplies it. No statement is verified beyond dimensions one through four, and no independent mathematical audit is represented.
