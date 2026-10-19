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

Run `python3 verify.py` in a directory containing the supplied standalone verifier. Only Python's standard library is needed; no network access or external files are required.

The program verifies the explicit legal edge set, number of repeats, local potential inequality over every binary length-\(k\) edge, required-edge potential deficit, balance and Euler circuit of the augmented legal graph, exact cyclic factor coverage, and absence of forbidden `11` factors for every \(2\le k\le12\). It also performs a separate exhaustive breadth-first shortest-cover walk search for \(2\le k\le5\) in the full unconstrained binary de Bruijn graph. The verified expected optimum lengths for orders \(2\) through \(12\) are respectively \(3,6,10,17,28,46,75,122,198,321,520\).

These checks are finite. The unbounded assertion and optimality for every order follow from the two mathematical arguments in `RESULT.md`; finite enumeration is not used in place of an infinite proof. No independent validation or external formal certification has been performed.
