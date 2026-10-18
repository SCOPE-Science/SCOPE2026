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

The standalone `check_exact.py` constructs seven-by-seven transient resolvent matrices directly from the stated transition rules. It computes the four integer-polynomial determinants with subset dynamic programming, cross-multiplies the Cramer numerators, and exact-divides by the proposed factor \(\lambda q(1-q)\). The computed quotient has precisely \(159\) nonzero coefficients, each positive, of maximum total degree \(8\) and coefficient range \(2\) to \(19670\). A reconstruction equality is asserted coefficientwise. Separate exact rational Gaussian eliminations at four parameter triples verify the independent resolvent calculation and its sign, including the undiscounted boundary \(z=0\).

Run `python3 check_exact.py` with Python 3.10 or newer. No non-standard packages or external files are required. The certificate is a deterministic exact symbolic computation, not simulation or finite parameter testing. Strict positivity of the resolvent denominators for \(q>0\) follows from finite-state absorption and nonsingular \(M\)-matrix theory; the checker verifies the algebraic identity but is not a replacement for this mathematical argument. When \(\lambda=0\) or \(q=1\), the equality arguments are analytical. Neither usual stochastic dominance nor claims beyond the three-patch model have been verified.
