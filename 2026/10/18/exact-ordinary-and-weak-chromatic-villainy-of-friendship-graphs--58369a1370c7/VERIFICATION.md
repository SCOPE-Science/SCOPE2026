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

# Reproduction and boundaries

Run `python verify.py` using Python 3 with only the standard library. The program builds the actual properly coloured targets and independently evaluates Hamming distances, rather than treating the local formula as ground truth. It exhausts all distinct colour assignments of profile \((k,k,1)\) for \(1\le k\le6\), including each of the \(3\cdot2^k\) properly coloured targets. The source counts for \(k=1,2,3,4,5,6\) are respectively 6, 30, 140, 630, 2772, and 12012; the corresponding checked pairs of worst repair distances are \((0,0),(3,2),(4,3),(5,5),(6,6),(7,7)\).

The program checks the closed local-agreement formula for every source of each tested size \(k\ge2\), checks the analytic constructions for \(2\le k\le18\), and directly compares each construction to all proper targets for \(k\le8\). It prints `ALL_TESTS_PASSED` when the checks agree.

These checks are finite and do not certify the unrestricted theorem by themselves. The full mathematical proof is the independent local-colour argument, parity-specific worst-case constructions, and two small-case reductions in `RESULT.md`. No claim of independent audit, exhaustive literature coverage or machine-verified infinity is made.
