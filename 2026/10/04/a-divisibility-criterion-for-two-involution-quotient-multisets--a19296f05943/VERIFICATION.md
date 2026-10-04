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

The theorem is proved symbolically in `RESULT.md`. The computational check is deliberately finite and is not used to infer the arbitrary-\(n\) statement.

`verify_dihedral.py` represents \(D_{2n}\) as pairs for \(r^i f^e\), uses exact group multiplication, chooses two generating involutions \(s,t\) with \(st=r\), and enumerates every one of the \(2^{2n}\) maps assigning either \(s\) or \(t\) to each group element. For each assignment it checks whether \(x\mapsto g_xx\) is a permutation. This is exactly the permutation formulation of quotient-realizability for multisets supported on those two involutions.

For every \(3\le n\le10\), the only realized multiplicities are \(0,n,2n\); the counts of realizing labelings are respectively \(1,2,1\). The same script independently verifies the ambient block-sum arithmetic for \(1\le m\le6\). The saved output ends in `VERIFY_OK`.

Unproved by computation: no finite enumeration certifies all \(n\), all ambient groups \(G\), or literature novelty. Those points rest respectively on the symbolic proof and the documented literature comparison.
