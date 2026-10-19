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

# Verification record

Run `python3 verify.py` from the directory containing this file. It must report `VERIFY_ALL_OK`. The script implements addition, multiplication, partial derivatives, and Jacobian changes directly in the four-dimensional quotient algebra, including a polynomial-basis implementation of \(\mathbb F_4\). It enumerates all algebra automorphisms and Poisson bracket parameters over \(\mathbb F_2\) and \(\mathbb F_4\), and independently enumerates all valid changes of generators and possible \(\{x,y\}=zxy\) parameters over prime fields of orders \(3\), \(5\), and \(7\).

Observed even-characteristic results: \(q=2\), \(16\) labeled brackets, \(24\) algebra automorphisms, \(6\) orbits with fixed-parameter orbit sizes \(1,3,4\); \(q=4\), \(256\) brackets, \(2880\) algebra automorphisms, \(12\) orbits with orbit sizes \(1,15,48\). Odd-characteristic cases have \(2\), \(3\), and \(4\) classes respectively, with sign-paired nonzero parameters. The proof in `RESULT.md` supplies the general-field algebraic derivation and explicitly excludes unverified scheme-theoretic or semilinear claims. Computational agreement alone is not proof for untested fields.
