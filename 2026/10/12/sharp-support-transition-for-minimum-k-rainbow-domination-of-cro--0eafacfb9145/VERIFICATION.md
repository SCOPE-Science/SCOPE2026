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

# Direct verification and limitations

The ordinary mathematical proof in `RESULT.md` establishes all integers \(k\ge3\), \(n\ge2k\). Reproduce the finite exhaustive incidence check using:

`c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`

The checker tests every subset of vertex-color incidences with total weight at most \(2k\), reconstructs the vertex subset labels, tests all empty vertices against their actual open neighborhoods, checks the structural family classification and computes the Stirling prediction directly. Expected output includes:

`k=3 n=6 tested=2391496 accepted=1446 predicted=1446 matched=1266 boundary=180 suboptimal_accepted=0`

`k=3 n=7 tested=6220768 accepted=2023 predicted=2023 matched=2023 boundary=0 suboptimal_accepted=0`

The run ends with `VERIFY_OK`. Tests for smaller \(k\) serve only as boundary consistency checks; the novel theorem is for \(k\ge3\). The direct program checks finite graphs only, and cannot by itself prove the general theorem. A 2018 one-page abstract on crown-graph \(3\)-rainbow bounds is known; possible fuller coverage remains a literature limitation. External independent audit was not performed.
