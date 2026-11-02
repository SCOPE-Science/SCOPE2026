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

Run `python3 verify.py` from this directory. Only Python's standard library is used.

The program exhaustively evaluates the local polynomials for every prime below \(300\), compares both root counts against the residue-class formulas, and tests disjointness. It then compares all four joint counts obtained by enumerating all starting residue classes against the exact product probabilities for \(19\) sample values of \(h\) (\(75{,}293\) total starting classes). Selected cases also directly evaluate the rational sequence and test *integer* squares in its reduced numerators and denominators. The checker exercises finite no-later-failure and positive-witness examples.

Expected first output line:

`VERIFY_OK local_primes=62 crt_examples=19 starting_residues=75293 direct_rational_checks=yes classification_checks=yes`

These are finite checks; the universal assertions depend on the modular and quadratic-reciprocity arguments in `RESULT.md`. No external audit is claimed.
