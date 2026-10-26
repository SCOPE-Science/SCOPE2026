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

# Verification details

The included `verify.py` was run directly from its newly packaged source and ended with `VERIFY_OK`.

- For \(r=1\) and \(r=2\), the program enumerates every possible algebra element and every ordered pair over \(\mathbb F_2\) and \(\mathbb F_3\), checks the multiplication condition, and verifies that the canonical quotient coordinates vanish on all zero-product pairs.
- For \((r,q)=(1,2),(1,3),(2,2),(2,3),(2,5),(3,2),(3,3)\), it enumerates every nonzero radical element, computes the full kernel of its left multiplication on the radical, spans all resulting zero-product pure tensors, and confirms the exact expected tensor-span rank. This exhaustive linear-algebra step avoids enumerating every kernel vector but spans the same vector space by bilinearity.
- For \(r=2\), \(q=3\), it tests the explicit symmetric quotient coordinate distinguishing \(F(x_1,x_2)\) from \(F(1,x_1x_2)\).

These checks do not prove the unrestricted statement. The general argument is the squarefree splitting relation and local-unit decomposition in the mathematical proof. The program uses prime fields only; the theorem holds over every field. No independent audit or certification was performed.
