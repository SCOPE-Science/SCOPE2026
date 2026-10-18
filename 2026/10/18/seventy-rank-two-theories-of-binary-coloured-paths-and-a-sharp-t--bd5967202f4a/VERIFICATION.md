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

The exact result is a consequence of the rank-two profile lemma and a complete finite-state reachability computation, not of a guessed maximum path length. `enumerate_profiles.py` explores all reachable states under both possible symbol appends, verifies that the queue is exhausted and computes the set of realized rank-two signatures. Its recorded output is `finite_state_output.txt`. The 70 canonical witnesses are in `certificate_70_types.json`.

The independent implementation `verify_direct.py` computes rank-one pointed types directly from the set of all quantifier-free two-point atomic diagrams and lists every word of lengths one through fourteen. It does not reuse transition states or the truncated multiplicity representation. Its recorded output is `direct_output.txt`. This independent *implementation* is not an independent scientific audit.

Commands (Python standard library only):

```bash
python3 enumerate_profiles.py --write-certificate certificate_70_types.json
python3 verify_direct.py
```

The closure computation reports 760 reachable states and 70 rank-two theories. The shortest-representative counts at lengths one through ten are 2, 3, 6, 10, 14, 18, 10, 5, 0, 2. The direct enumeration independently reproduces those counts through length fourteen. The proof covers all nonempty finite vertex-coloured paths, not arbitrary graphs or logical ranks above two.
