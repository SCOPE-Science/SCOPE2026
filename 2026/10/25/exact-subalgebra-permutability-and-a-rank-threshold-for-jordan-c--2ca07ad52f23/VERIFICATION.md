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

# Verification of the mathematical claims

Execute `python3 verify.py` using the Python 3 standard library. The program independently enumerates all linear subspaces, finds Lie subalgebras by testing brackets, and checks permutability of every ordered subalgebra pair by directly testing bracket containment in the vector-space sum.

For \((r,q)=(1,2),(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\), the observed pairs of *(number of subalgebras, number of ordered permutable pairs)* are respectively \((5,25)\), \((12,120)\), \((19,253)\), \((39,771)\), \((31,633)\), \((68,2086)\), and \((98,6108)\). The script also enumerates the complete permutability relation for all possible scalar shifts in ranks two and three over \(\mathbb F_2\) and \(\mathbb F_3\), finding identical relations after identifying the ambient vector spaces. It prints `VERIFY_OK` when every comparison succeeds.

The direct checker covers prime fields and finite ambient dimensions only. Nonprime fields and arbitrary ranks are covered by the algebraic proof, not by an exhaustive computational run. The checks do not provide an external or independent mathematical audit.
