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

# Verification details

The elementary symbolic proof in `RESULT.md` supplies the all-length argument; the enclosed `check.py` is a separate, reproducible finite consistency test. Run it from this directory with `python3 check.py` (Python 3 standard library; no network or dependencies). The code verifies each observed distinct Abelian-unbordered factor set against the classified families for all 2,300 triples of total zeros at most 22, tests exact cumulative counts and extrema for each such length, checks the associated ordinary/Abelian border equivalence on 3,810 small low-support words, and checks the sharp four-marker counterexample already described in previous literature. Its rational calculation at 600 zeros independently tests convergence to the claimed first and second moments.

These finite checks are not complete all-length formal verification. The proof's nonstandard claims needing scrutiny are (i) shortening a long Abelian border to its complement, (ii) the if-and-only-if gap inequality for factors containing both marked symbols, (iii) disjointness of the factor types, (iv) the lattice-slice count, and (v) the simplex integral and moment error bound. Each is argued in the proof, rather than inferred from the test output. Mathematical originality is assessed with residual historical-priority uncertainty, and an independent audit is not performed.
