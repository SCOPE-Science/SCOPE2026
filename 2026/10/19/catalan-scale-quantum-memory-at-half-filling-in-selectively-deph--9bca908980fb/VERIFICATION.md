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
# Verification of the Johnson-walk calculation

Execute `python verify_johnson.py` with the packages listed in `requirements.txt`. Execution tested all selected \(15\) Johnson pairs with \(3\le n\le7\) and at most \(16\) vertices, including the central square case, both sides of half filling, and endpoints. The program builds the graph adjacency from the defining set intersection relation and constructs the incidence matrix directly. It checks full incidence rank, \(B^*B=kI+A_U\), orthogonality and rank of the dark projector, its eigenvalue \(-k\), and equal unmonitored local projector diagonals. For up to \(15\) vertices it explicitly assembles the full complex Lindbladian with different positive rates, checks the predicted \(1+d^2\) stationary eigenvalue multiplicity and the absence of other modes on the imaginary axis. For up to \(10\) vertices it evaluates a finite-time matrix exponential and compares the results for monitored and unmonitored localized initial states with the predicted limiting density matrix. It independently evaluates the first fourteen Catalan identities at the central odd-rank boundary.

All the checks completed without exceptions in the execution accompanying this result. They are finite consistency checks only; the full parameter range and asymptotic conclusions follow from the proof in `RESULT.md`. The mathematical proof itself does not rely on floating-point eigenvalue thresholds. No independent audit or external experimental validation has occurred.
