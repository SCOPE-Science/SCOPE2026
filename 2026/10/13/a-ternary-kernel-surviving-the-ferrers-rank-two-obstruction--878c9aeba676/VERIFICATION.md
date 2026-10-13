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

Run `python3 verify_ferrers_q3.py` with the Python standard library. The checker reconstructs the field-spread matrices from the irreducible quartic, verifies that the twelve displayed matrices span the Frobenius-orthogonal complement, enumerates all \(3^{12}\) elements of that space, constructs the codimension-two kernel from the displayed coefficient matrix, enumerates all \(3^{10}\) kernel elements, and canonicalizes every rank-two right kernel.

The accepted checks are: \(\dim U=12\); the exact rank distribution of \(U\) is \((A_0,A_1,A_2,A_3,A_4)=(1,0,10400,220800,300240)\); \(\dim K=10\); \(K\) has exactly \(1040\) rank-two matrices; exactly \(130\) distinct two-dimensional right kernels occur; every such kernel occurs exactly \(8\) times; and the \(130\) kernels equal the complete set of planes in \(\mathbb F_3^4\).

The verification is finite and exhaustive. It does not test, assert, or certify the unresolved existence of a compatible lift map or a ternary dimension-\(12\) Ferrers-diagram code.
