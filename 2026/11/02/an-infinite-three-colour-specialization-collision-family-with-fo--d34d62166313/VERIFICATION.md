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

# Verification and scope

Execute `python verify.py` with Python 3 and SymPy. Its coefficient-certificate routine derives, rather than assumes, the six \([q^8]\)-pair contributions from the exact finite formula and proves the rational identity
\[
[q^8]\sum_{r\ge1}z^r\bigl(\operatorname{ps}_4(X_{A_r})-\operatorname{ps}_4(X_{B_r})\bigr)=-14z-4z^2-\frac{2z^3}{1-z}.
\]
It uses an independent tree-adjacency dynamic program for proper-colouring weights at \(r=1,\ldots,6\) for both palette sizes and direct exhaustive graph-colouring enumeration for \(r=1\) with three and four colours and \(r=2\) with three colours. These are checks of distinct implementations, not proofs for unbounded \(r\). The infinite proof is the paired-summation algebra and the coefficient recurrence in the RESULT document. Successful execution prints `VERIFY_OK` after all assertions. No independently conducted assessment is asserted.
