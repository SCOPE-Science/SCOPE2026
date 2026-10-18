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

The self-contained Python 3 checker `verify.py` requires no third-party dependencies. Running `python3 verify.py` from the same directory returned:

```
VERIFY_OK independent_minterm_assignments=77230 minterm_case_checks=26 burnside_cases=26 2_atom_unique_collision_through_8_atoms=PASS
```

The checker enumerates all atom-colorings in 26 bounded parameter/arity cases, builds exact Boolean minterm signatures on every atom, compares type partitions against independently computed necklace supports and counts, and computes automorphism orbit numbers again from explicit permutations and Burnside's lemma. It additionally checks the unique-collision assertion among all uniform-cycle systems with at most eight atoms. The checks are finite and do not constitute a proof for arbitrary numbers of atoms or arities. The infinite claims are proved symbolically in `RESULT.md`; no external independent audit has been performed.
