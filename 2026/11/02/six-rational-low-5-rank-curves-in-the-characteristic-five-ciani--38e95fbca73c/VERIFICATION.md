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

# Verification of the characteristic-five low-rank locus

The proof in `RESULT.md` uses exact identities over \(\mathbb F_5\), not empirical extrapolation. The complete claim is that the \(5\)-rank-at-most-one locus on the stated smooth normalized parameter space is six explicitly parameterized rational curves with eight transverse triple crossings, leading to the all-extension counts of rank zero and one.

The symbolic verifier `verify_symbolic.py`, using SymPy, was executed and checked: the coefficient-of-\(y^4z^4\) Hasse expression; three pairwise differences; the two pair parametrizations and corresponding smoothness identities; and the factorization determining the eight triple points. The finite-field verifier `verify_ciani_p5.py` is pure Python and uses \(\mathbb F_{25}=\mathbb F_5[u]/(u^2-2)\). It exhausts the \(5^3\) and \(25^3\) coefficient triples, separately filters smoothness, and compares each supersingularity condition with the six parameter maps and their incidence multiplicities. Both programs were run from the paths included in this package; their outputs are in `verification_output.txt`.

The exact counts obtained were: over \(\mathbb F_5\), 23 smooth triples, of which 12 have two supersingular quotients and none have three; over \(\mathbb F_{25}\), 11,683 smooth triples, of which 96 have two supersingular quotients and eight have three. Each rational component has two rational parameters over \(\mathbb F_5\) and 20 over \(\mathbb F_{25}\). These are finite cross-checks. The proof's signed-factor identities, pairwise quadratic solving, nonvanishing Jacobian differentials, and simple quadratic-root count give the geometric and arbitrary-extension conclusions.

To replay, use `python3 verify_ciani_p5.py` and, after installing the dependency listed in `requirements.txt`, `python3 verify_symbolic.py`. Independent audit status is not performed; these checks provide reproducibility, not external certification.
