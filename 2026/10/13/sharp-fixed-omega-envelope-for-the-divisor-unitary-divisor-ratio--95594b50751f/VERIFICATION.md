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
The proof is symbolic and unbounded. The executable check is deliberately secondary evidence.

`verify.py` enumerates every integer partition of each \(m\) for \(1\le m\le40\). It computes the ratio factor exactly as a rational number and checks both the predicted maximum and the complete set of maximizing exponent multisets. The stored run output is `VERIFY_OUTPUT.txt`.

The finite check does not prove the statement for larger \(m\). The unbounded step is supplied by the local-improvement proof in `RESULT.md`, which reduces every maximizing partition to the residue-class normal forms and then compares the only competing residue-two forms exactly.
