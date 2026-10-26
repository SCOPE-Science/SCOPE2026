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

# Reproducible exact checks

Run `python3 verify.py` with standard Python 3. No third-party modules or external data are required.

The checker regenerates the four-state Rule 110 predecessor graph and its two label relations, enumerates all 75 reachable Boolean relations by closure, and compares their cycle indicators. It verifies all 75 coordinates of the polynomial annihilation identity that establishes the integer recurrence for all lengths, then checks by exact polynomial multiplication the rational generating function and Artin–Mazur zeta logarithmic derivative. It independently enumerates ring antecedents with periods at most four times the output length for output lengths one through five, checks those five point counts, and verifies stabilization of the primitive-period witness relation.

The enumerated ring tests are consistency checks, **not** an argument that patterns continue indefinitely; the exact transfer identity, four-vertex graph cycle lemma and stabilization identity provide the unrestricted proof. The checker does not establish historical novelty or independent scientific validation. No external review has been performed.
