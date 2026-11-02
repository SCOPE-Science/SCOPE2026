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

The accompanying standard-library program enumerates all undirected Hamiltonian cycles of each \(K_n\) for \(3\le n\le6\) without isomorphic double-counting, computes VC and Littlestone dimensions exactly, and independently validates every node and leaf in the depth-five witness tree.

Run from the directory containing the attached files:

```sh
python check_hamiltonian_cycle_gap.py cycle_depth5_certificate.json
```

Expected terminal line: `ALL_HAMILTONIAN_CYCLE_GAP_CHECKS_PASS`. The program checks the explicit 31-query-node/32-leaf certificate rather than trusting the stored dimension. The unrestricted VC dimension for \(n\ge5\) and additive product formulas require the mathematical arguments in `RESULT.md`; finite computation does not prove them. Historical-priority coverage of one plausible 1997 paper remains unresolved.
