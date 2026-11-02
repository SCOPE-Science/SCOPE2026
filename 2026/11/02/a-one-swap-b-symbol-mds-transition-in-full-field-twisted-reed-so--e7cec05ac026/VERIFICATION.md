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

# Verification of the exact \(b\)-symbol transition

The standalone `verify.py` uses independent direct message evaluation rather than calling the proof's run-count identity to compute code distances. Execute it with Python 3.9 or later. The recorded `verification_output.txt` must end in `TWISTED_B_SYMBOL_VERIFY_OK`.

The verifier exhaustively evaluates 54 complete finite code instances, with 354,480 nonzero messages over the test primes and twist coefficients, checks the \(b\)-symbol distances at every length \(1\le b\le k+1\), and checks extremal multiplicities for the defective orders. It also checks all 120 coordinate orders at \(p=5\) separately for each dimension \(2,3,4\), and 4,056 additional explicit window-sum configurations through prime 29. All tests in the recorded run passed.

Mathematical limits: these examples do not certify infinitely many parameter values. The general proof uses a Vieta root-sum characterization, cyclic zero-run decomposition, rank of low-degree polynomial evaluations, and the two-window perturbation calculation. No external or independent certification has been performed.
