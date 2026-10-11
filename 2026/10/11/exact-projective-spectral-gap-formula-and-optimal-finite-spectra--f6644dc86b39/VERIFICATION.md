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

# Mathematical verification

The analytic argument checks the normalization \(1/(2\pi)\) by reducing a \(\pi\)-periodic integrand to \(1/\pi\). For a singleton projective spectrum the unique complementary arc has length \(\pi\), giving \(\omega_2(U)^2=1/2\); for a full projective spectrum there are no open gaps, giving \(1\). For \(q\) equally spaced projective points each gap has length \(\pi/q\), yielding \(\tfrac12+q\sin(\pi/q)/(2\pi)\). The derivative test \(\sin x-x\cos x>0\) is valid for all \(0<x\le\pi\).

Run `python3 verify_phase_gaps.py` using Python's standard library to compare the exact finite-gap formula against midpoint integration of the defining angular radius for both equally spaced and nonuniform examples, and to test the strict Jensen inequality in nonuniform examples. The script checks only finite cases and is not a certificate for the infinite-spectrum assertion; the latter follows from countable additivity in the proof.

No external/independent audit has been performed.
