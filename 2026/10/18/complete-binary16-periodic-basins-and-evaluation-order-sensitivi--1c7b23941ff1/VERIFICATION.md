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

Run `python3 verify.py` from the same directory. This uses only the Python standard library, integer arithmetic for authoritative transitions and `struct` half conversion as a separate computational check.

The verified finite state set contains \(32{,}769\) distinct numerical binary16 values in \([-2,2]\). Every one of the resulting \(65{,}538\) successor calculations was compared to the alternative half-conversion oracle. In each of the two functional graphs, an exact indegree-peeling census found all directed cycles, full basins and entry depths. A direct successor walk verified that each starting state's reported depth reaches its assigned cycle.

One final rounding produced periods \(1,94,6,5,5,1\), full basin sizes \(20785,11706,168,60,48,2\), and a maximum transient length of \(59\). Separate square and final rounding produced periods \(1,44,4,8,1\), full basin sizes \(20341,12156,62,208,2\), and a maximum transient length of \(69\). The protocols have exactly \(1{,}842\) different transitions. All quoted finite-state Cesàro means were calculated with exact `fractions.Fraction` arithmetic. The program asserts these figures and terminates normally.

Finite-state exhaustiveness is an algorithmic proof for the particular finite alphabet and rounding protocol, conditional on ordinary integer arithmetic and program correctness. The independently implemented half-conversion comparison is an additional check, not a claim of external certification. The almost-sure ergodic statement for the exact real map instead uses classical analytic conjugacy; it is not deduced from a numerical experiment. Nothing here verifies actual analogue-hardware behavior or any non-binary16 format.
