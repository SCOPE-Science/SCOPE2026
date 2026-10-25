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

# Reproducibility and scope

The bundled `verify_humbert17.py` uses exact arithmetic in \(\mathbb F_{25}\) and the Euclidean algorithm in \(\mathbb F_{25}[c]\); it has no nonstandard dependencies. Invoke `python3 verify_humbert17.py` from the extracted package directory. It constructs the two equianharmonic roots, counts \(12,6,3\) among the \(21\) finite shared-triple continuations at \(h=2,3,4\), and verifies every relevant genus-two Hasse determinant is nonzero. It also constructs the *two* disjoint-complement cross-ratio polynomials from their definitions and checks each is coprime to the corresponding genus-two Hasse determinant. The explicit six-point witness has \(h=4\) and an ordinary genus-two double quotient.

The proof separately justifies why these are all possible configurations: a triple has precisely two supersingular completions; four or more supersingular quadruples force a common triple; and the only other case with at least three is the disjoint-pair case with two polynomial equations. The finite calculations do not claim to enumerate all points of \(\mathbb P^1(\overline{\mathbb F}_5)\). The equality orbit is unique only for the maximum number of supersingular elliptic factors, not for every rank-minimizing curve.

Source arXiv:1507.02903, Section 5.3, supplies historical complex-analytic context for the genus-\(17\) isogeny; the characteristic-five prime-to-\(5\) kernel statement is proved directly in `RESULT.md`. Any independent audit is not yet performed.
