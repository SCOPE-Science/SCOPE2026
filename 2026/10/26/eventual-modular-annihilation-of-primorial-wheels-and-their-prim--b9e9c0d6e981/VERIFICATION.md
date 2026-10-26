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

# Reproducible checks and limits

Run `python3 verify.py` with an unmodified standard Python 3 interpreter. The script needs no third-party modules. It reconstructs the reduced-residue counts directly for the first five primorials, compares them with the exact wheel transition, computes the source's three initial binary states, and checks four modular residue-annihilation examples. Its successful output is:

`VERIFY_OK primorials=2,6,30,210,2310 modulus_pairs=4 first_special_prime=137 residues_after_special=7,6`

The infinite theorem relies on the proved polynomial identity, Dirichlet's theorem, and the invariant in reference [1], not on the script. The calculation at prime \(137\) tests an explicit sufficient threshold, not its optimality. Self-review has examined the claimed proof and these exact finite checks; no independent audit has been performed.
