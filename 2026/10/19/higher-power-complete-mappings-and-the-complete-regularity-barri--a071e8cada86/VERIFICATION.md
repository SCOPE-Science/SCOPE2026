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
Run `python3 verify.py` with Python 3.9+ and the standard library. It exhaustively tests all permutations for each finite multiplication table and powers \(k=2,3,4\) (limited to \(k=2,3\) in several larger tables), giving 42 distinct semigroup/exponent checks. The tested objects include cyclic groups of orders 2–6, \(C_2\times C_2\), \(C_2\times C_4\), \(C_3\times C_3\), two Brandt matrix units, symmetric partial bijections on two points, groups with adjoined zero, two finite bands and a two-element nilpotent semigroup. A separate comparison checks the Brandt \(k=1\) contrast. The table multiplication is asserted associative, and the brute criterion is exactly the two-permutation definition; no floating arithmetic is used.

Expected reproducibility output:

`VERIFY_OK 42 exhaustive semigroup/exponent tests; Brandt k=1 contrast`

These are finite sanity checks, not a certification of the universal theorem. General correctness follows from the proof in `RESULT.md`, which invokes the standard Rees principal-factor theorem and the known Hall–Paige existence characterization for finite abelian groups. No human or independent mathematical audit is claimed.
