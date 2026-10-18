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

The mathematical proof in `RESULT.md` covers all \(k\ge2\), \(m\ge1\), all real \(B,t>0\), and all individually adjustable eligible conductances with connected support. Finite checks in `verification.py` are additional diagnostics and never replace that proof.

Run `python3 verification.py` with standard Python 3 from the extracted directory. The program assembles independent rational graph Laplacians, grounds one vertex, inverts with exact rational Gaussian elimination, computes every unordered-pair effective resistance, and compares the result to the claimed three-orbit identity. It verifies budget normalization and signs at the exact price boundary. Finite independently varied asymmetric competitor allocations are checked against the proposed exact optimum; these samples are **not** claimed to certify the infinite optimization statement.

No independent mathematical audit has been performed. The finite check is reproducible from the included standalone source file.
