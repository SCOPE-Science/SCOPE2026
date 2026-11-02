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

# Verification of the mathematical claim

The checker `checks/verify.py` constructs the exact binary cut adjacency of \(Q_d\), deletes a matching by toggling its entries, and recomputes rank by elimination on arbitrary-precision integer bitsets. It imports no third-party packages and uses a fixed random seed for finite samples. Its actual output is `checks/verification_output.txt`.

At \(d=4\) it exhausts all matchings of sizes one, two, and three (32, 400, 2496). At \(d=6\) and \(d=8\), it samples each size from one through \(d-1\) and verifies both explicit size-\(d\) threshold arrangements. Odd-dimension edge deletions supply finite boundary checks. The final log reports `ALL_VERIFIED total_ranks=4031`.

The all-even-dimension conclusion instead follows from the proof and from the independently published even-cube code-distance input of Key and Seneviratne (2007). The verification does not classify fault sets containing adjacent edges, arbitrary cuts or noisy channels, and independent research-level assessment has not been performed.
