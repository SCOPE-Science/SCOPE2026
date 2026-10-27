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

The proof establishes convergence for every \(n\ge2\), preference profile, initial matching, and legal history by a single bounded increasing integer potential. The key recurrence uses unique paths in the auxiliary line; the key counting injection maps each nontrivial reachable ordered selected pair \((s,t)\) to a distinct unreachable pair \((u,s)\) with \(u\notin S\).

A separate exact-integer program, `verify.py`, was executed with Python's standard library. It independently enumerates all matching states and both strict neighbor orders at every interior vertex, checks each legal one-edge blocking move, checks the matching potential bound, and calculates the longest sequence in the directed state graph.

Observed results (\(n\), profiles, matchings, maximum moves):

```
(2,1,2,1)
(3,2,3,2)
(4,4,5,4)
(5,8,8,6)
(6,16,13,9)
(7,32,21,12)
(8,64,34,16)
(9,128,55,20)
(10,256,89,25)
(11,512,144,30)
```

Every number of moves equals \(\lfloor n^2/4\rfloor\), every legal transition increases the tested potential, and every enumerated potential satisfies the claimed ceiling. The all-left sharp construction's legality and length were also verified for every integer \(2\le n\le80\). The program ended with `ALL CHECKS PASSED`.

These finite tests do not prove the universal claim; that follows only from the stated directed-reachability potential argument and matching injection. The checks do not concern graph topologies other than paths, preferences with ties, or simultaneous moves. No independent audit has been performed.
